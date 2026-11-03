#!/usr/bin/env python3
"""
Reproducible pipeline: nirsevimab resistance-associated substitutions in public RSV genomes.

Stages
  fetch-genbank   retrieve GenBank genomes for taxon 11250 (13-16 kb)
  sort            assign subtype with the Nextclade minimizer index
  align           run Nextclade per subtype -> translations, lineages, aligned nucleotides
  build-cohort    QC, metadata join, date-precision flagging, cross-database de-duplication
  call            subtype-consensus variant calling and DMS escape scoring
  stats           carriage, period tests, threshold sweep, window sweep, stratified inference
  sensitivity     de-duplication, date-precision and cell-entry-floor sensitivity analyses
  trend           Cochran-Armitage scan across all F variants
  clesrovimab     exploratory application of the same cutoff to the clesrovimab DMS table
  phylo           prints the exact phylogenetic commands used (run once, interactively)
  all             every stage above except phylo

Figure generation is not part of this script; the deposited tables under tables/ are its inputs.

GISAID sequences cannot be redistributed and are NOT downloaded by this script. Export them
yourself from https://gisaid.org using manifests/gisaid_epi_isl.txt and place the FASTA at
--gisaid-fasta with the metadata TSV at --gisaid-meta.

The GenBank arm retrieves exactly the versioned accessions in manifests/genbank_accessions.txt.
fetch_genbank() aborts if that file is absent and reports any accession the server does not
return; every analysis stage makes the same check, and a cached Nextclade dataset directory is
reused only when its recorded release tag matches the pinned one. A silent fall-back to current
holdings or to an unpinned dataset is therefore not possible. Pass --frozen-accessions ""
to deliberately query live holdings instead; this will not reproduce the published cohort.

Reproducing the validation log: the analysis stages need F translations, which the deposited
manifests do not contain (they carry metadata and calls only). Run build-cohort first from
tr_A_F.fasta / tr_B_F.fasta, produced by the align stage, then:
  python pipeline.py stats       --gisaid-meta gisaid.tsv
  python pipeline.py sensitivity --gisaid-meta gisaid.tsv
  python pipeline.py trend       --gisaid-meta gisaid.tsv
  python pipeline.py clesrovimab --gisaid-meta gisaid.tsv
Their combined stdout is logs/validation_run.txt.

Usage
  python pipeline.py all --gisaid-fasta gisaid.fasta --gisaid-meta gisaid.tsv --email you@example.org

Pinned versions: Nextclade 3.28.0; datasets nextstrain/rsv/a/EPI_ISL_412866 and
nextstrain/rsv/b/EPI_ISL_1653999, both at release tag 2026-04-14--11-55-23Z (passed to
`nextclade dataset get --tag`); VeryFastTree 4.0.4; phylo-treetime 0.12.1.
DMS scores: github.com/dms-vep/RSV_Long_F_DMS pinned at commit
3ecdfaa661304e3c284acdbeacc9662d2baa1dd9 (2026-09-16). Expected sha256 prefixes of the two
summary files: Nirsevimab.csv f7e69d60fccd5b719cc1306539c08c49,
Clesrovimab.csv 860a6d56e381205be55f251e850cb761; verify_dms() checks them.
Retrieval date of the published analysis: 2 November 2026.
"""
import argparse
import hashlib, io, collections, json, os, re, subprocess, sys, time, urllib.parse, urllib.request, zipfile
import numpy as np, pandas as pd
from scipy import stats as stats_mod
from statsmodels.stats.proportion import proportion_confint

F_COORDS = {"A": (5697, 7421), "B": (5676, 7400)}      # F CDS in each reference
PRIMARY_START = 2017
ERA_BOUNDARY = pd.Timestamp("2023-07-01")
FAB_CUTOFF = 2.036       # anchored on N201T, the weakest variant with published phenotypic support
ENTRY_FLOOR = -0.5
NEXTCLADE_DATASET_TAG = "2026-04-14--11-55-23Z"
DMS_COMMIT = "3ecdfaa661304e3c284acdbeacc9662d2baa1dd9"
DMS_URL = ("https://raw.githubusercontent.com/dms-vep/RSV_Long_F_DMS/"
           + DMS_COMMIT + "/results/summaries/{antibody}.csv")
DMS_SHA256_PREFIX = {"Nirsevimab": "f7e69d60fccd5b719cc1306539c08c49",
                     "Clesrovimab": "860a6d56e381205be55f251e850cb761"}


def verify_dms(antibody, blob):
    """Warn if the fetched DMS summary differs from the version used in the published analysis."""
    got = hashlib.sha256(blob).hexdigest()[:32]
    want = DMS_SHA256_PREFIX.get(antibody)
    if want and got != want:
        print(f"WARNING: {antibody}.csv sha256 {got} != expected {want}; "
              f"results may differ from the published analysis.")
    return got


def sh(cmd, **kw):
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"FAILED ({r.returncode}): {r.stderr[-2000:]}")
    return r


def fetch_genbank(outfa, email=None, frozen_accessions="manifests/genbank_accessions.txt"):
    """Stage 1. Retrieve exactly the frozen versioned accession list.

    Metadata still comes from NCBI Datasets (it is needed for dates and countries), but the
    sequence set retrieved is the deposited list, not whatever currently matches the taxon and
    length query. If the list is missing the run aborts rather than silently falling back.
    """
    base = "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/virus/taxon/11250/dataset_report"
    rows, token = [], None
    while True:
        url = base + "?page_size=1000" + (f"&page_token={token}" if token else "")
        with urllib.request.urlopen(url, timeout=120) as fh:
            page = json.load(fh)
        for rep in page.get("reports", []):
            iso, loc = rep.get("isolate") or {}, rep.get("location") or {}
            rows.append((rep.get("accession"), rep.get("length"), iso.get("collection_date"),
                         loc.get("geographic_region"), loc.get("geographic_location"),
                         (rep.get("virus") or {}).get("organism_name")))
        token = page.get("next_page_token")
        if not token:
            break
    meta = pd.DataFrame(rows, columns=["acc", "len", "date", "region", "country", "organism"])
    meta.to_csv("genbank_metadata.csv", index=False)

    if frozen_accessions:
        if not os.path.exists(frozen_accessions):
            sys.exit(f"frozen accession list {frozen_accessions} not found. It is required to "
                     f"reproduce the published cohort; pass --frozen-accessions '' to override "
                     f"and query live holdings instead (this will NOT reproduce the cohort).")
        accs = [l.strip() for l in open(frozen_accessions) if l.strip()]
        print(f"GenBank: retrieving {len(accs)} frozen versioned accessions "
              f"from {frozen_accessions}")
    else:
        accs = list(dict.fromkeys(
            meta[(meta.len >= 13000) & (meta.len <= 16000)].acc.dropna().astype(str)))
        print(f"GenBank: LIVE query, {len(meta)} records, {len(accs)} genomes of 13-16 kb. "
              f"This will not reproduce the published cohort.")

    contact = {"email": email, "tool": "rsv-f-surveillance"} if email else {}
    with open(outfa, "w", encoding="utf-8") as out:
        for i in range(0, len(accs), 200):
            payload = {"db": "nuccore", "id": ",".join(accs[i:i + 200]),
                       "rettype": "fasta", "retmode": "text", **contact}
            for attempt in range(4):
                try:
                    req = urllib.request.Request(
                        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                        data=urllib.parse.urlencode(payload).encode())
                    with urllib.request.urlopen(req, timeout=300) as fh:
                        out.write(fh.read().decode("utf-8", "replace"))
                    break
                except Exception:
                    time.sleep(4 * (attempt + 1))
            time.sleep(0.35)
    got = set()
    for line in open(outfa, encoding="utf-8", errors="replace"):
        if line.startswith(">"):
            got.add(line[1:].split()[0])
    missing = [a for a in accs if a not in got and a.split(".")[0] not in
               {g.split(".")[0] for g in got}]
    print(f"GenBank: wrote {len(got)} sequences; {len(missing)} requested accessions not returned")
    if missing:
        with open("genbank_missing_accessions.txt", "w") as fh:
            fh.write("\n".join(missing) + "\n")
        print("  missing accessions written to genbank_missing_accessions.txt")


def nextclade_datasets(exe, tag=NEXTCLADE_DATASET_TAG):
    """Stage 2 prerequisite. --output-zip is used because --output-dir fails on Windows.

    The release tag is pinned so that lineage assignments and reference-anchored translations
    match the published analysis; omit it only if you intend to use current datasets.
    """
    for name, zp, od in [("nextstrain/rsv/a/EPI_ISL_412866", "ds_a.zip", "ds_rsv_a"),
                         ("nextstrain/rsv/b/EPI_ISL_1653999", "ds_b.zip", "ds_rsv_b")]:
        if os.path.isdir(od):
            # A cached directory is reused only if its recorded tag matches.
            pj = os.path.join(od, "pathogen.json")
            cached = (json.load(open(pj, encoding="utf-8")).get("version", {}).get("tag")
                      if os.path.exists(pj) else None)
            if tag and cached != tag:
                sys.exit(f"cached dataset {od} has tag {cached}, expected {tag}. Remove {od} to "
                         f"re-download, or pass tag=None to accept the cached version.")
            print(f"  {od}: reusing cached dataset at tag {cached}")
            continue
        cmd = [exe, "dataset", "get", "--name", name, "--output-zip", zp]
        if tag:
            cmd += ["--tag", tag]
        sh(cmd)
        os.makedirs(od, exist_ok=True)
        with zipfile.ZipFile(zp) as z:
            z.extractall(od)
        got = json.load(open(os.path.join(od, "pathogen.json"), encoding="utf-8"))
        got_tag = got.get("version", {}).get("tag")
        if tag and got_tag != tag:
            print(f"WARNING: {name} resolved to tag {got_tag}, expected {tag}")



def sort_and_align(exe, combined, jobs=8):
    """Stages 2-3."""
    sh([exe, "sort", combined, "--output-results-tsv", "sort.tsv", "--jobs", str(jobs)])
    assign = dict(zip(*[pd.read_csv("sort.tsv", sep="\t")[c].astype(str) for c in ("seqName", "dataset")]))
    handles = {s: open(f"comb_{s}.fasta", "w", encoding="utf-8") for s in "AB"}
    cur, counts = None, collections.Counter()
    for line in open(combined, encoding="utf-8", errors="replace"):
        if line.startswith(">"):
            ds = assign.get(line[1:].strip(), "")
            cur = "A" if "/rsv/a/" in ds else ("B" if "/rsv/b/" in ds else None)
            counts[cur or "unassigned"] += 1
        if cur:
            handles[cur].write(line)
    for h in handles.values():
        h.close()
    print("subtype assignment:", dict(counts))
    for sub, ds in (("A", "ds_rsv_a"), ("B", "ds_rsv_b")):
        sh([exe, "run", "--input-dataset", ds, "--output-tsv", f"nc_{sub}.tsv",
            "--output-translations", f"tr_{sub}_{{cds}}.fasta", "--output-fasta", f"aln_{sub}.fasta",
            "--jobs", str(jobs), "--silent", f"comb_{sub}.fasta"])


def read_fasta(path):
    seqs, key, buf = {}, None, []
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith(">"):
            if key:
                seqs[key] = "".join(buf)
            key, buf = line[1:].strip(), []
        else:
            buf.append(line.strip())
    if key:
        seqs[key] = "".join(buf)
    return seqs


def parse_date(s):
    """Return (timestamp, precision). Partial dates expand to the first day; precision is recorded."""
    s = str(s).strip()
    for fmt, prec in (("%Y-%m-%d", "day"), ("%Y-%m", "month"), ("%Y", "year")):
        try:
            return pd.Timestamp(pd.to_datetime(s, format=fmt)), prec
        except Exception:
            pass
    return pd.NaT, "none"


def build_cohort(gisaid_meta_path, frozen_accessions=None):
    """Stage 4. QC, metadata join, date-precision flagging, de-duplication."""
    translations = {}
    for sub in "AB":
        translations.update({k: ("RSV-" + sub, v) for k, v in read_fasta(f"tr_{sub}_F.fasta").items()})
    nc = pd.concat([pd.read_csv(f"nc_{s}.tsv", sep="\t", low_memory=False).assign(subtype="RSV-" + s)
                    for s in "AB"], ignore_index=True)
    nc["F"] = nc.seqName.map(lambda s: translations.get(s, (None, None))[1])
    nc = nc[nc.F.notna()].copy()
    nc["is_gisaid"] = nc.seqName.str.startswith("EPI_ISL_")
    nc["key"] = np.where(nc.is_gisaid, nc.seqName.str.strip(),
                         nc.seqName.str.split().str[0].str.split(".").str[0])
    if frozen_accessions:
        keep = set(l.strip().split(".")[0] for l in open(frozen_accessions) if l.strip())
        before = len(nc)
        nc = nc[nc.is_gisaid | nc.key.isin(keep)].copy()
        print(f"frozen accession list: {before - len(nc)} GenBank records dropped, {len(nc)} retained")
    gb = pd.read_csv("genbank_metadata.csv")
    gb["acc0"] = gb.acc.astype(str).str.split(".").str[0]
    gbm = gb.drop_duplicates("acc0").set_index("acc0")
    gi = pd.read_csv(gisaid_meta_path, sep="\t", low_memory=False)
    gi["country"] = gi.Location.astype(str).str.split("/").str[1].str.strip()
    gim = gi.drop_duplicates("Accession ID").set_index("Accession ID")
    nc["date"] = np.where(nc.is_gisaid, nc.key.map(gim["Collection date"]), nc.key.map(gbm["date"]))
    nc["country"] = np.where(nc.is_gisaid, nc.key.map(gim["country"]), nc.key.map(gbm["country"]))
    parsed = nc.date.map(parse_date)
    nc["cdate"] = [p[0] for p in parsed]
    nc["date_precision"] = [p[1] for p in parsed]
    nc["F_cov"] = nc.F.map(lambda s: sum(c not in "-X" for c in s[:574]) / 574)
    sel = nc[(nc.F_cov >= 0.95) & nc.cdate.notna()].copy()
    sel["c0"] = sel.country.astype(str).str.split(":").str[0].str.split("/").str[0].str.strip()
    sel["year"] = sel.cdate.dt.year.astype(int)
    sel["source"] = np.where(sel.is_gisaid, "GISAID", "GenBank")
    print(f"QC pass: {len(sel)}; date precision: {sel.date_precision.value_counts().to_dict()}")
    # De-duplication. The grouping key hashes the F sequence so that the deposited group mapping
    # carries an opaque identifier rather than sequence data.
    fh = sel.F.map(lambda s: hashlib.md5(s.encode()).hexdigest()[:16])
    sel["dupkey"] = fh + "|" + sel.c0 + "|" + sel.cdate.dt.strftime("%Y-%m-%d")
    sel["group_id"] = sel.dupkey.map(lambda k: "G" + hashlib.md5(k.encode()).hexdigest()[:12])
    both = sel.groupby("dupkey").source.nunique()
    print(f"de-duplication: {int((both > 1).sum())} groups contain both databases; "
          f"{int(sel.duplicated('dupkey').sum())} of {len(sel)} records collapsed")
    sel["is_representative"] = ~sel.duplicated("dupkey")
    sel[["group_id", "key", "source", "subtype", "c0", "cdate", "date", "date_precision",
         "is_representative"]].rename(columns={"key": "accession", "c0": "country"}) \
        .to_csv("deduplication_groups.csv", index=False)
    sel.to_pickle("prededuplication_set.pkl")
    A = sel[sel.is_representative].copy()
    A["era"] = np.where(A.cdate < ERA_BOUNDARY, "pre", "post")
    A.to_pickle("analysis_set.pkl")
    print(f"analysis set: {len(A)}")
    return A


def consensus(A):
    """Per-subtype consensus of the analysis set."""
    out = {}
    for sub, g in A.groupby("subtype"):
        M = np.array([list(s[:574].ljust(574, "-")) for s in g.F])
        out[sub] = "".join(pd.Series(M[:, i]).replace({"-": np.nan, "X": np.nan})
                           .dropna().mode().iat[0] if pd.Series(M[:, i]).replace(
                               {"-": np.nan, "X": np.nan}).notna().any() else "-" for i in range(574))
    return out


def escape_set(antibody="Nirsevimab", fab=FAB_CUTOFF, entry=ENTRY_FLOOR):
    with urllib.request.urlopen(DMS_URL.format(antibody=antibody), timeout=120) as r:
        blob = r.read()
    verify_dms(antibody, blob)
    dms = pd.read_csv(io.BytesIO(blob))
    col = f"{antibody}-Fab escape"
    q = dms[(dms[col] >= fab) & (dms["cell entry"] >= entry)]
    return set(zip(q.site, q.mutant)), dms


def call(A, cons=None, antibody="Nirsevimab", fab=FAB_CUTOFF, entry=ENTRY_FLOOR):
    """Stage 5. Call variants against each subtype's own consensus and classify against the DMS."""
    if cons is None:
        cons = consensus(A)
    esc, dms = escape_set(antibody, fab, entry)

    def one(F, sub):
        c = cons[sub]
        return ";".join(f"{a}{i}{b}" for i, (a, b) in enumerate(zip(c, F), 1)
                        if b != a and b not in ("X", "-", "*") and (i, b) in esc)

    A = A.copy()
    A["escape_substitutions"] = [one(F, s) for F, s in zip(A.F, A.subtype)]
    A["carrier"] = A.escape_substitutions.ne("")
    return A, cons, esc


def _fisher(sub):
    a = sub[sub.cdate < ERA_BOUNDARY]
    b = sub[sub.cdate >= ERA_BOUNDARY]
    ka, na = int(a.carrier.sum()), len(a)
    kb, nb = int(b.carrier.sum()), len(b)
    p = stats_mod.fisher_exact([[kb, nb - kb], [ka, na - ka]])[1] if na and nb else float("nan")
    return ka, na, kb, nb, p


def cmh(df, keys):
    """Continuity-corrected Cochran-Mantel-Haenszel across the given strata."""
    num = den = 0.0
    informative = 0
    for _, g in df.groupby(keys):
        post = g.cdate >= ERA_BOUNDARY
        a = int(g[post].carrier.sum()); b = int(post.sum()) - a
        c = int(g[~post].carrier.sum()); d = int((~post).sum()) - c
        n = a + b + c + d
        if n < 2 or (a + c) == 0 or (a + b) == 0 or (c + d) == 0:
            continue
        informative += 1
        num += a - (a + b) * (a + c) / n
        den += (a + b) * (c + d) * (a + c) * (b + d) / (n ** 2 * (n - 1))
    if den <= 0:
        return float("nan"), informative
    return stats_mod.chi2.sf((abs(num) - 0.5) ** 2 / den, 1), informative


def carriage(A, out="table2_carriage.csv"):
    """Primary carriage table with Clopper-Pearson intervals."""
    rows = []
    W = A[A.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")]
    for sub in sorted(W.subtype.unique()) + ["pooled"]:
        g = W if sub == "pooled" else W[W.subtype == sub]
        ka, na, kb, nb, p = _fisher(g)
        for lab, k, n in (("before 1 Jul 2023", ka, na), ("on/after 1 Jul 2023", kb, nb)):
            lo, hi = proportion_confint(k, n, method="beta")
            rows.append(dict(subtype=sub, period=lab, carriers=k, records=n,
                             percent=100 * k / n, ci_low=100 * lo, ci_high=100 * hi))
    T = pd.DataFrame(rows)
    T.to_csv(out, index=False)
    return T


def threshold_sweep(A, cons, out="threshold_sweep.csv"):
    """Primary sensitivity analysis 1: vary the Fab-escape cutoff."""
    W = A[A.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")]
    rows = []
    for fab in [1.0, 1.2, 1.4, 1.6, 1.8, FAB_CUTOFF, 2.2, 2.4, 2.5, 2.6]:
        B, _, esc = call(W, cons, fab=fab)
        ka, na, kb, nb, p = _fisher(B)
        rows.append(dict(fab_threshold=fab, n_mutations=len(esc), pre_k=ka, pre_n=na,
                         pre_pct=100 * ka / na, post_k=kb, post_n=nb, post_pct=100 * kb / nb, fisher_p=p))
    T = pd.DataFrame(rows)
    T.to_csv(out, index=False)
    return T


def window_sweep(A, out="window_sweep.csv"):
    """Primary sensitivity analysis 2: vary the first collection year included."""
    rows = []
    for sy in [None, 2000, 2005, 2010, 2014, 2015, 2016, 2017, 2018, 2019, 2020]:
        sub = A if sy is None else A[A.cdate >= pd.Timestamp(f"{sy}-01-01")]
        ka, na, kb, nb, p = _fisher(sub)
        pc, _ = cmh(sub, ["subtype"])
        lo, hi = proportion_confint(ka, na, method="beta")
        rows.append(dict(start="all years" if sy is None else str(sy), pre_k=ka, pre_n=na,
                         pre_pct=100 * ka / na, pre_lo=100 * lo, pre_hi=100 * hi,
                         post_k=kb, post_n=nb, post_pct=100 * kb / nb, fisher_p=p, cmh_p=pc))
    T = pd.DataFrame(rows)
    T.to_csv(out, index=False)
    return T


def stratified(A, out="supp_country_period_subtype.csv"):
    """Stratified inference and the country-by-period-by-subtype denominators."""
    W = A[A.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")].copy()
    for keys, lab in ((["subtype"], "subtype"), (["c0"], "country"),
                      (["c0", "subtype"], "country x subtype"),
                      (["c0", "subtype", "source"], "country x subtype x database")):
        p, n = cmh(W, keys)
        print(f"  CMH by {lab:30s} p={p:.4g}  informative strata={n}")
    W["post"] = W.cdate >= ERA_BOUNDARY
    T = (W.groupby(["c0", "subtype", "post"]).agg(n=("carrier", "size"), k=("carrier", "sum"))
         .reset_index().pivot_table(index=["c0", "subtype"], columns="post",
                                    values=["n", "k"], fill_value=0))
    T.columns = [f"{a}_{'post' if b else 'pre'}" for a, b in T.columns]
    T.reset_index().sort_values("n_post", ascending=False).to_csv(out, index=False)
    return T


def dedup_sensitivity(A, cons):
    """Repeat the primary comparison with no de-duplication at all."""
    full = pd.read_pickle("prededuplication_set.pkl")
    B, _, _ = call(full, cons)
    for lab, sub in (("no de-duplication, all years", B),
                     ("no de-duplication, primary window",
                      B[B.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")])):
        ka, na, kb, nb, p = _fisher(sub)
        print(f"  {lab:36s} pre {ka}/{na:,}  post {kb}/{nb:,}  p={p:.4g}")


def date_sensitivity(A):
    """Repeat the primary comparison excluding imprecisely dated records."""
    W = A[A.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")]
    amb = (W.date_precision == "year") & (W.cdate.dt.year == 2023)
    for lab, sub in (("primary", W), ("exclude year-only 2023", W[~amb]),
                     ("exclude all year-only", W[W.date_precision != "year"]),
                     ("full-date records only", W[W.date_precision == "day"])):
        ka, na, kb, nb, p = _fisher(sub)
        print(f"  {lab:28s} pre {ka}/{na:,}  post {kb}/{nb:,}  p={p:.4g}")


def entry_sensitivity(A, cons):
    """Repeat the primary comparison across cell-entry floors."""
    W = A[A.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")]
    for ce in [-2.0, -1.5, -1.0, ENTRY_FLOOR, -0.25, 0.0]:
        B, _, esc = call(W, cons, entry=ce)
        ka, na, kb, nb, p = _fisher(B)
        print(f"  entry >= {ce:5.2f}: {len(esc):2d} mutations  pre {ka}/{na:,}  post {kb}/{nb:,}  p={p:.3g}")


def trend_scan(A, cons, out="trend_scan_combined.csv", min_records=5):
    """Cochran-Armitage trend test across every F variant carried by >= min_records records."""
    W = A[A.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")].copy()
    rows = []
    for sub, g in W.groupby("subtype"):
        c = cons[sub]
        years = g.cdate.dt.year.values
        uy = np.array(sorted(set(years)))
        ny = np.array([(years == y).sum() for y in uy])
        counts = {}
        for F, y in zip(g.F, years):
            for i, (a, b) in enumerate(zip(c, F), 1):
                if b != a and b not in ("X", "-", "*"):
                    counts.setdefault(f"{a}{i}{b}", {}).setdefault(y, 0)
                    counts[f"{a}{i}{b}"][y] += 1
        for mut, per in counts.items():
            tot = sum(per.values())
            if tot < min_records:
                continue
            k = np.array([per.get(y, 0) for y in uy])
            p_bar = tot / ny.sum()
            num = (ny * (uy - (ny * uy).sum() / ny.sum()) * (k / np.maximum(ny, 1) - p_bar)).sum()
            var = p_bar * (1 - p_bar) * (ny * (uy - (ny * uy).sum() / ny.sum()) ** 2).sum()
            z = num / np.sqrt(var) if var > 0 else 0.0
            rows.append(dict(subtype=sub, mut=mut, n=tot, z=z,
                             p=2 * stats_mod.norm.sf(abs(z)),
                             direction="increase" if z > 0 else "decrease",
                             counts_by_year=";".join(
                                 f"{y}:{per.get(y, 0)}/{n_y}" for y, n_y in zip(uy, ny))))
    T = pd.DataFrame(rows)
    bonf = 0.05 / len(T)
    T["significant"] = T.p < bonf
    T.to_csv(out, index=False)
    sig = T[T.significant]
    print(f"  {len(T)} variants tested, Bonferroni {bonf:.3g}: {len(sig)} significant "
          f"({int((sig.direction == 'increase').sum())} increasing, "
          f"{int((sig.direction == 'decrease').sum())} decreasing)")
    return T


def clesrovimab(A, cons, out="supp_S6_clesrovimab_carriers.csv"):
    """Exploratory: the same numerical cutoff applied to the clesrovimab DMS table."""
    B, _, _ = call(A, cons, antibody="Clesrovimab")
    cc = B[B.carrier]
    pre25 = B[B.cdate < pd.Timestamp("2025-01-01")]
    win = pre25[pre25.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01")]
    k, n = int(win.carrier.sum()), len(win)
    lo, hi = proportion_confint(k, n, method="beta")
    print(f"  clesrovimab, primary window before 2025: {k}/{n:,} "
          f"({100 * k / n:.4f}%, CI {100 * lo:.4f}-{100 * hi:.4f})")
    out_df = cc[["key", "subtype", "c0", "cdate", "source", "escape_substitutions"]].copy()
    out_df["window"] = np.where(out_df.cdate >= pd.Timestamp(f"{PRIMARY_START}-01-01"),
                                "primary", "pre-{} historical".format(PRIMARY_START))
    out_df.to_csv(out, index=False)
    return out_df


PHYLO_COMMANDS = """\
Stage 7, phylogenetics. These are the commands that produced the deposited results. They are
documented rather than wrapped in a function because they take several hours and were run once,
interactively.

  # 1. Alignments, restricted to the 38,925 analysis-set tips. Nextclade emits both the aligned
  #    nucleotide CDS and the translated peptide; no separate translation step is needed.
  #    F_nt_{A,B}.fasta  aligned F coding sequence   (1722 nt)
  #    F_aa_{A,B}.fasta  translated F peptide        (574 aa)
  #    Tip identifiers are identical in both files and in the trees.

  # 2. Tree inference on the NUCLEOTIDE alignment
  veryfasttree -nt -gtr -gamma -threads 24 F_nt_A.fasta > F_A.nwk
  veryfasttree -nt -gtr -gamma -threads 24 F_nt_B.fasta > F_B.nwk

  # 3. Ancestral reconstruction of AMINO-ACID states on that topology. TreeTime's --aa selects
  #    the amino-acid alphabet, so the alignment passed here is the PEPTIDE alignment, not the
  #    nucleotide one used for tree inference. Residue numbering is 1-574 of the F protein and
  #    matches the numbering used for carriage calls.
  treetime ancestral --aln F_aa_A.fasta --tree F_A.nwk --outdir tt_A --gtr infer --aa
  treetime ancestral --aln F_aa_B.fasta --tree F_B.nwk --outdir tt_B --gtr infer --aa

ROOTING. No explicit rooting step was applied. VeryFastTree emits an unrooted tree, written with
a trifurcating root, and TreeTime's `ancestral` was run on it as given. The direction assigned to
each reconstructed change is therefore conditional on that root placement. Sensitivity of the
acquisition counts to rooting was not assessed. An earlier version of the Methods described these
trees as midpoint-rooted; that was incorrect and has been corrected.

Acquisition branches are the branches of tt_*/annotated_tree.nexus on which a high-escape residue
appears; spread is the count of descendant tips that themselves carry that residue (not the total
descendant count); support is taken from the maximum-likelihood topology by matching nodes on
their descendant tip sets. Branch labels use the reconstructed ancestral state, which may differ
from the subtype consensus used for carriage reporting.

The resulting trees, annotated NEXUS output and branch-mutation tables are deposited under
phylogenetics/.
"""

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["all", "fetch-genbank", "sort", "align", "build-cohort",
                                      "call", "stats", "trend", "clesrovimab", "sensitivity", "phylo"])
    ap.add_argument("--gisaid-fasta")
    ap.add_argument("--gisaid-meta")
    ap.add_argument("--frozen-accessions", default="manifests/genbank_accessions.txt",
                    help="retrieve exactly this versioned accession list; '' queries live holdings")
    ap.add_argument("--nextclade", default="nextclade")
    ap.add_argument("--email", default=None, help="contact address for NCBI E-utilities")
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()

    if args.stage == "phylo":
        print(PHYLO_COMMANDS)
        return
    if args.stage in ("all", "fetch-genbank"):
        fetch_genbank("rsv_genomes.fasta", args.email, args.frozen_accessions)
    if args.stage in ("all", "sort", "align"):
        if not (args.gisaid_fasta and os.path.exists(args.gisaid_fasta)):
            sys.exit("--gisaid-fasta is required: GISAID sequences must be exported by the user.")
        with open("combined.fasta", "w", encoding="utf-8") as out:
            for f in ("rsv_genomes.fasta", args.gisaid_fasta):
                out.write(open(f, encoding="utf-8", errors="replace").read())
        nextclade_datasets(args.nextclade)
        sort_and_align(args.nextclade, "combined.fasta", args.jobs)
    if args.stage in ("all", "build-cohort", "call", "stats", "trend", "clesrovimab", "sensitivity"):
        if args.frozen_accessions:
            if not os.path.exists(args.frozen_accessions):
                sys.exit(f"frozen accession list {args.frozen_accessions} not found. Every analysis "
                         f"stage requires it to reproduce the published cohort; pass "
                         f"--frozen-accessions '' to proceed without it (results will differ).")
            frozen = args.frozen_accessions
        else:
            frozen = None
            print("WARNING: running without a frozen accession list; the cohort will not match "
                  "the published analysis.")
        A = build_cohort(args.gisaid_meta, frozen)
        A, cons, esc = call(A)
        print(f"qualifying mutations at the primary cutoff: {len(esc)}")
    if args.stage in ("all", "stats"):
        print("carriage:"); print(carriage(A).to_string(index=False))
        print("threshold sweep:"); print(threshold_sweep(A, cons).to_string(index=False))
        print("window sweep:"); print(window_sweep(A).to_string(index=False))
        print("stratified:"); stratified(A)
    if args.stage in ("all", "sensitivity"):
        print("de-duplication sensitivity:"); dedup_sensitivity(A, cons)
        print("date-precision sensitivity:"); date_sensitivity(A)
        print("cell-entry floor sensitivity:"); entry_sensitivity(A, cons)
    if args.stage in ("all", "trend"):
        print("trend scan:"); trend_scan(A, cons)
    if args.stage in ("all", "clesrovimab"):
        print("clesrovimab:"); clesrovimab(A, cons)


if __name__ == "__main__":
    main()
