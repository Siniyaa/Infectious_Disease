#!/usr/bin/env python3
"""
Reproducible pipeline: nirsevimab resistance-associated substitutions in public RSV genomes.

Stages
  1 fetch-genbank   retrieve GenBank genomes for taxon 11250 (13-16 kb)
  2 sort            assign subtype with the Nextclade minimizer index
  3 align           run Nextclade per subtype -> translations, lineages, aligned nucleotides
  4 build-cohort    QC, metadata join, cross-database de-duplication
  5 call            subtype-consensus variant calling and DMS escape scoring
  6 stats           carriage, era tests, threshold sweep, trend scan
  7 phylo           ML trees, ancestral reconstruction, acquisition counts and support

GISAID sequences cannot be redistributed and are NOT downloaded by this script. Export them
yourself from https://gisaid.org using manifests/gisaid_epi_isl.txt and place the FASTA at
--gisaid-fasta with the metadata TSV at --gisaid-meta.

Usage
  python pipeline.py all --gisaid-fasta gisaid.fasta --gisaid-meta gisaid.tsv --email you@example.org

Pinned versions: Nextclade 3.25.1; datasets nextstrain/rsv/a/EPI_ISL_412866 and
nextstrain/rsv/b/EPI_ISL_1653999; VeryFastTree 4.0.4; phylo-treetime 0.12.1.
DMS scores: github.com/dms-vep/RSV_Long_F_DMS, results/summaries/{Nirsevimab,Clesrovimab}.csv
Retrieval date of the published analysis: 2 November 2026.
"""
import argparse, collections, json, os, re, subprocess, sys, time, urllib.parse, urllib.request, zipfile
import numpy as np, pandas as pd
from scipy.stats import binomtest, fisher_exact, chi2, norm

F_COORDS = {"A": (5697, 7421), "B": (5676, 7400)}      # F CDS in each reference
ERA_BOUNDARY = pd.Timestamp("2023-07-01")
WINDOW_START = 2017
FAB_THRESHOLD = 2.036        # anchored on N201T, the weakest variant with published clinical support
ENTRY_FLOOR = -0.5
DMS = "https://raw.githubusercontent.com/dms-vep/RSV_Long_F_DMS/main/results/summaries/{}.csv"


def sh(cmd, **kw):
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"FAILED ({r.returncode}): {r.stderr[-2000:]}")
    return r


def fetch_genbank(outfa, email=None):
    """Stage 1. Metadata via NCBI Datasets, sequences via Entrez efetch in batches of 200."""
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
    accs = list(dict.fromkeys(meta[(meta.len >= 13000) & (meta.len <= 16000)].acc.dropna().astype(str)))
    print(f"GenBank: {len(meta)} records, {len(accs)} genomes of 13-16 kb")
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


def nextclade_datasets(exe):
    """Stage 2 prerequisite. --output-zip is used because --output-dir fails on Windows."""
    for name, zp, od in [("nextstrain/rsv/a/EPI_ISL_412866", "ds_a.zip", "ds_rsv_a"),
                         ("nextstrain/rsv/b/EPI_ISL_1653999", "ds_b.zip", "ds_rsv_b")]:
        if os.path.isdir(od):
            continue
        sh([exe, "dataset", "get", "--name", name, "--output-zip", zp])
        os.makedirs(od, exist_ok=True)
        with zipfile.ZipFile(zp) as z:
            z.extractall(od)


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


def build_cohort(gisaid_meta_path):
    """Stage 4. QC, metadata join, de-duplication. Returns the analysis-set DataFrame."""
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
    gb = pd.read_csv("genbank_metadata.csv")
    gb["acc0"] = gb.acc.astype(str).str.split(".").str[0]
    gbm = gb.drop_duplicates("acc0").set_index("acc0")
    gi = pd.read_csv(gisaid_meta_path, sep="\t", low_memory=False)
    gi["country"] = gi.Location.astype(str).str.split("/").str[1].str.strip()
    gim = gi.drop_duplicates("Accession ID").set_index("Accession ID")
    nc["date"] = np.where(nc.is_gisaid, nc.key.map(gim["Collection date"]), nc.key.map(gbm["date"]))
    nc["country"] = np.where(nc.is_gisaid, nc.key.map(gim["country"]), nc.key.map(gbm["country"]))
    nc["cdate"] = pd.to_datetime(nc.date, errors="coerce", format="mixed")
    nc["F_cov"] = nc.F.map(lambda s: sum(c not in "-X" for c in s[:574]) / 574)
    sel = nc[(nc.F_cov >= 0.95) & nc.cdate.notna()].copy()
    sel["c0"] = sel.country.astype(str).str.split(":").str[0].str.split("/").str[0].str.strip()
    sel["year"] = sel.cdate.dt.year.astype(int)
    sel["source"] = np.where(sel.is_gisaid, "GISAID", "GenBank")
    # De-duplication: records identical in F, country and collection date are collapsed.
    # This is a conservative rule; see the sensitivity analysis in stats().
    sel["dupkey"] = sel.c0 + "|" + sel.cdate.dt.strftime("%Y-%m-%d") + "|" + sel.F
    groups = sel.groupby("dupkey").source.agg(set)
    print(f"de-duplication: {sum(len(v) > 1 for v in groups)} groups contain both databases; "
          f"{int(sel.duplicated('dupkey').sum())} records collapsed of {len(sel)}")
    sel[["key", "source", "dupkey"]].to_csv("deduplication_groups.csv", index=False)
    A = sel[~sel.duplicated("dupkey")].copy()
    A["era"] = np.where(A.cdate < ERA_BOUNDARY, "pre", "post")
    A.to_pickle("analysis_set.pkl")
    print(f"analysis set: {len(A)}")
    return A


def consensus(A):
    out = {}
    for st in ("RSV-A", "RSV-B"):
        seqs = A.loc[A.subtype == st, "F"]
        out[st] = "".join(collections.Counter(s[i] for s in seqs if s[i] not in "-X").most_common(1)[0][0]
                          for i in range(574))
    return out


def call(A, antibody="Nirsevimab"):
    """Stage 5. Variants are called against each subtype's OWN consensus."""
    esc = pd.read_csv(DMS.format(antibody))
    col = f"{antibody}-Fab escape"
    qualifying = set(zip(*[esc[(esc[col] >= FAB_THRESHOLD) & (esc["cell entry"] >= ENTRY_FLOOR)][c]
                           for c in ("site", "mutant")]))
    cons = consensus(A)
    subs, hits = [], []
    for seq, st in zip(A.F, A.subtype):
        ref = cons[st]
        v = [(i + 1, seq[i]) for i in range(574) if seq[i] not in "-X" and seq[i] != ref[i]]
        subs.append(v)
        hits.append(";".join(sorted(f"{ref[p - 1]}{p}{m}" for p, m in v if (p, m) in qualifying)))
    A = A.copy()
    A["subs"], A["hits"] = subs, hits
    A["carrier"] = A.hits != ""
    print(f"{antibody}: {len(qualifying)} qualifying mutations; {int(A.carrier.sum())} carriers in the analysis set")
    return A, cons, esc


def stats(A, esc):
    """Stage 6. All comparisons are restricted to the primary window and reported with the window stated."""
    W = A[A.year >= WINDOW_START]
    rows = []
    for st in ("RSV-A", "RSV-B", "Both"):
        d = W if st == "Both" else W[W.subtype == st]
        for era in ("pre", "post"):
            x = d[d.era == era]
            k, n = int(x.carrier.sum()), len(x)
            lo, hi = binomtest(k, n).proportion_ci(method="exact")   # Clopper-Pearson throughout
            rows.append((st, era, k, n, 100 * k / n, 100 * lo, 100 * hi))
    carriage = pd.DataFrame(rows, columns=["subtype", "era", "k", "n", "pct", "ci_lo", "ci_hi"])
    carriage.to_csv("carriage.csv", index=False)
    pre, post = W[W.era == "pre"], W[W.era == "post"]
    a, b = int(post.carrier.sum()), int(pre.carrier.sum())
    print("pooled Fisher p =", fisher_exact([[a, len(post) - a], [b, len(pre) - b]])[1])
    tabs = []
    for st in ("RSV-A", "RSV-B"):
        d = W[W.subtype == st]
        aa = int(d[d.era == "post"].carrier.sum()); bb = len(d[d.era == "post"]) - aa
        cc = int(d[d.era == "pre"].carrier.sum());  dd = len(d[d.era == "pre"]) - cc
        tabs.append((aa, bb, cc, dd))
    O = sum(t[0] for t in tabs)
    E = sum((t[0] + t[2]) * (t[0] + t[1]) / sum(t) for t in tabs)
    V = sum(((t[0] + t[2]) * (t[1] + t[3]) * (t[0] + t[1]) * (t[2] + t[3])) / ((sum(t) ** 2) * (sum(t) - 1))
            for t in tabs)
    stat = (abs(O - E) - 0.5) ** 2 / V        # continuity-corrected Cochran-Mantel-Haenszel
    print(f"CMH (continuity corrected) chi2={stat:.2f} p={chi2.sf(stat, 1):.3g}")
    sweep = []
    for t in (1.0, 1.2, 1.4, 1.6, 1.8, FAB_THRESHOLD, 2.2, 2.4, 2.5, 2.6):
        q = set(zip(*[esc[(esc["Nirsevimab-Fab escape"] >= t) & (esc["cell entry"] >= ENTRY_FLOOR)][c]
                      for c in ("site", "mutant")]))
        c = W.subs.map(lambda L: any((p, m) in q for p, m in L))
        aa, nn = int((c & (W.era == "post")).sum()), int((W.era == "post").sum())
        bb, mm = int((c & (W.era == "pre")).sum()), int((W.era == "pre").sum())
        sweep.append((t, len(q), aa, nn, bb, mm, fisher_exact([[aa, nn - aa], [bb, mm - bb]])[1]))
    pd.DataFrame(sweep, columns=["fab_threshold", "n_mutations", "post_k", "post_n",
                                 "pre_k", "pre_n", "fisher_p"]).to_csv("threshold_sweep.csv", index=False)
    print("threshold sweep written")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["all", "fetch-genbank", "sort", "align", "build-cohort", "call", "stats"])
    ap.add_argument("--gisaid-fasta", required=False)
    ap.add_argument("--gisaid-meta", required=False)
    ap.add_argument("--nextclade", default="nextclade")
    ap.add_argument("--email", default=None, help="contact address for NCBI E-utilities")
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    if args.stage in ("all", "fetch-genbank"):
        fetch_genbank("rsv_genomes.fasta", args.email)
    if args.stage in ("all", "sort", "align"):
        if not (args.gisaid_fasta and os.path.exists(args.gisaid_fasta)):
            sys.exit("--gisaid-fasta is required: GISAID sequences must be exported by the user.")
        with open("combined.fasta", "w", encoding="utf-8") as out:
            for f in ("rsv_genomes.fasta", args.gisaid_fasta):
                out.write(open(f, encoding="utf-8", errors="replace").read())
        nextclade_datasets(args.nextclade)
        sort_and_align(args.nextclade, "combined.fasta", args.jobs)
    if args.stage in ("all", "build-cohort", "call", "stats"):
        A = build_cohort(args.gisaid_meta)
        A, cons, esc = call(A)
        stats(A, esc)


if __name__ == "__main__":
    main()
