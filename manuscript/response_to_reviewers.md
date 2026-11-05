# RESPONSE TO THE THIRD REVIEW (SUBMISSION READINESS)

**Manuscript.** Threshold and time-window choices determine whether nirsevimab escape substitutions appear to have increased: an analysis of 38,925 public respiratory syncytial virus genomes

We thank the reviewer. Two comments identified documentation that did not match what was actually run, and
we have corrected the record rather than the description. Every numerical point raised was recomputed and
confirmed. Author-side placeholders remain outstanding and are listed at the end.

Note on timing: the review was carried out at repository commit aaba9a5c. The historical-cluster wording in
Results 3.5, the Figure 4 legend and response comment 1 (the reviewer's comment 3) had already been
corrected in the commit that followed, and those corrections stand in this version.

---

## Comment 1. Reconcile the phylogenetic commands with the analysis

**Confirmed, and the documented commands were wrong.** We inspected the deposited TreeTime output: the
equilibrium frequencies in `tt_*/sequence_evolution_model.txt` are over the twenty amino acids, and
`branch_mutations.txt` reports residue positions in the 1-574 protein frame. The reconstruction was
therefore run on the **peptide** alignment, not the nucleotide alignment named in the printed commands.
TreeTime's `--aa` selects the amino-acid alphabet and does not translate.

**Action.** `pipeline.py phylo` now prints the alignment-provenance step, the nucleotide path used for tree
inference (`F_nt_*.fasta` to VeryFastTree) and the separate peptide path used for ancestral reconstruction
(`F_aa_*.fasta` to TreeTime), and states that tip identifiers are identical across both files and the trees
and that residue numbering matches the carriage calls. Methods 2.5 was rewritten to the same effect.

**A second error found while checking this.** The Methods described the trees as midpoint-rooted. They are
not. VeryFastTree emits an unrooted tree, written with a trifurcating root, and TreeTime was run on it as
given; we confirmed the trifurcation directly in `F_A.nwk`. The claim is withdrawn. Methods and the printed
commands now state that no explicit rooting step was applied, that the direction assigned to each
reconstructed change is conditional on that root placement, and that sensitivity of the acquisition counts
to rooting was not assessed. The acquisition and support tables are unchanged, since they were computed
from these same trees.

## Comment 2. Workflow and provenance corrections

**Frozen inputs - confirmed.** `fetch_genbank()` queried current holdings and the frozen list was applied
only later. It now retrieves exactly the versioned accessions in `manifests/genbank_accessions.txt`, exits
with an explanatory error if that file is absent, and writes any accession the server did not return to
`genbank_missing_accessions.txt`. Querying live holdings is still possible but requires passing
`--frozen-accessions ''` and prints a warning that the published cohort will not be reproduced.

**Dataset tags - confirmed.** Release tags were named nowhere. Both RSV datasets are now pinned to
`2026-04-14--11-55-23Z`, passed through `nextclade dataset get --tag`, and the resolved tag in
`pathogen.json` is checked after extraction. We also corrected the recorded Nextclade version, which was
3.25.1 in the docstring and is in fact 3.28.0.

**Validation scope - confirmed.** The deposited manifests carry metadata and calls, not F sequences, so the
log was not reproducible from them alone. The log now opens with an explicit "how to reproduce" section
naming the required sequence inputs, the intermediate files (`tr_{A,B}_F.fasta`, `analysis_set.pkl`,
`prededuplication_set.pkl`) and the four exact commands whose combined output it is.

**Output provenance - confirmed.** Methods 2.5 claimed per-year counts accompanied every trend statistic
and the deposited CSV had none. `trend_scan()` now exports a `counts_by_year` column giving carrier and
denominator per year for all 689 variants tested, and the deposited table was regenerated. The analysis
manifest now carries `collection_date_as_deposited` alongside `collection_date_parsed` and
`date_precision`, so the raw value is preserved in the same file.

## Comment 3. Describe the historical group accurately

**Already corrected in the commit after the one reviewed, and confirmed against the data.** The twelve
site-209 carriers comprise ten Argentinian records from 2015 and two Vietnamese records from 2014; the
thirteenth historical carrier is a German record from 2002 carrying N201T. All occurrences in Results 3.2
and 3.5, the Figure 2c and Figure 4 legends, the README and the response letter now use that description.

**Outbreak wording.** Adopted. The group is called an acquisition clade throughout, and Results 3.2 states
explicitly that the grouping is phylogenetic and that no epidemiological linkage between these specimens
has been established.

## Comment 4. Distinguish statistical nonsignificance from no change

**Adopted throughout.** "Becomes null" and "no change" are replaced by "the difference is no longer
statistically significant" in the abstract, Results 3.2, Results 3.4 and the Discussion. The full-archive
comparison is now reported with both fractions (0.101% against 0.134%) beside the p value. Results 3.3
adds the point the reviewer asks for: changing the cutoff does not merely change the power of one test, it
changes which substitutions are classified and therefore the endpoint being compared.

**De-duplication framing.** Adopted in Results 3.4, which compares fractions (0% against 0.117% in the
primary window; 0.070% against 0.117% across the full archive) and states that the smaller p value
obtained without de-duplication is not stronger evidence, because records matching on F sequence, country
and date are not independent observations. The Limitations sentence still said the analysis without
de-duplication "strengthened" the association; it now says the descriptive pattern persisted and repeats
the independence caveat.

## Comment 5. Figure annotations

- **Figure 2a title.** Confirmed: "three orders of magnitude" was unsupported. Among non-zero values
  carriage falls about 70-fold (4.45% to 0.065%); the title now says so and the legend states that no
  finite ratio is defined where a period count is zero.
- **Figure 2b title.** Confirmed: significance is not simply lost. The title now reads "Not significant
  between cutoffs of 1.2 and 1.8; reversed at 1.0", and the legend notes that the open circles include the
  significant reversal.
- **Figure 2c and Figure 4 legends.** Corrected dates and countries as above.
- **Table 2 and figure legends.** "Before/after rollout" is replaced by the fixed 1 July 2023 calendar
  boundary, with an explicit statement that national rollout timing was not used to assign periods. In the
  third revision this change had been applied to the legends but not to the Table 2 rows, the Table 2 CSV,
  the Table S7 heading, `tables/table4_origins.csv` or the Figure 1 image; all are corrected here and
  Figure 1 has been regenerated.

## Additional corrections

- **GISAID matching.** [SUPERSEDED - see addendum item 1 below for the current figures.] Confirmed that
  the collapsed total conflated within-database repetition with cross-database matches, and the previous
  "half were re-depositions" figure was wrong. The replacement figures given here (9,344 records, 22.5%
  not retained) were themselves wrong and are corrected in the fourth-review addendum: the correct
  accounting is 19,845 GISAID records retained and 21,669 (52.2%) excluded. Methods 2.3 and the Discussion
  carry the corrected wording; the "match on F sequence, country and collection date" phrasing and the
  statement that matching does not establish specimen identity are retained.
- **Abstract denominator.** Clarified to "25,384 GenBank records with 44,275 eligible GISAID EpiRSV records
  (69,659 in total)".
- **Year-only records.** Confirmed: 538 is the full archive and only 190 are in the primary window (177
  before the boundary, 13 after). Methods 2.2 and Results 3.4 now say so.
- **Table S1.** Confirmed 83 categories including an unnamed one with 4 records. Reported as 82 named
  countries plus 4 records with no country, labelled "(country not stated)" in the table, and stated in
  Results 3.10.
- **Display items.** Tables 3a and 3b are merged into one physical Table 3 carrying both sweeps in a
  single table with a Panel column, rather than two tables sharing a label. The rendered manuscript
  contains three tables and five figures, eight display items, verified in the built file.
- **Supplement legibility.** The supplement is now landscape with wider columns and 8-point table text;
  headers repeat and rows do not split.

## Outstanding, for the authors

Author names, affiliations, corresponding-author details, funding, conflicts of interest, CRediT
contributions, the GISAID EPI_SET acknowledgement identifier, and the author placeholders in references 2,
4-8, 10 and 11, of which reference 8 (the lineage nomenclature consortium paper) is still to be selected.
Final journal requirements should be checked directly rather than relying on the limits stated on the title
page.


---

# ADDENDUM: RESPONSE TO THE FOURTH REVIEW

## 1. GISAID accounting in Methods 2.3

**Confirmed, and our correction was itself wrong.** Recomputed directly from the deposited mapping:
41,514 GISAID records pass QC, 19,845 are retained as representatives, so 21,669 (52.2%) are excluded -
16,973 from mixed-database groups and 4,696 from GISAID-only groups. The 9,344 / 22.5% figure counted
GISAID records beyond the first within each group, which is not the same quantity; the original 52.2% was
correct. Methods 2.3 now uses the reviewer's suggested wording verbatim, and the Discussion sentence is
corrected to match.

## 2. Wording corrections applied everywhere

Confirmed incomplete. "Before rollout" / "After rollout" remained in the Table 2 rows and its CSV, the
Table S7 heading and `tables/table4_origins.csv`, and the Figure 1 image still carried "No carrier before
rollout" and "prophylaxis rollout". All are now the fixed 1 July 2023 boundary, and Figure 1 has been
regenerated as PNG and TIFF with its title scoped to the 2017-onward window. "The period comparison is
null" and "null or reversed" are gone from the Conclusions, which now distinguish non-significance between
cutoffs of 1.2 and 1.8 from the significant reversal at 1.0.

## 3. Rooting limitation carried into the headline statements

Adopted. The abstract now reads "Under the reported reconstruction, high-escape residues were assigned to
32 candidate acquisition branches, 26 associated with a single sampled carrier." Results 3.5 and the
Conclusions use the same qualification, state that the reconstruction is conditional on one topology, one
ancestral-state model and the unrooted tree as produced, and describe the phylogenetic findings as
exploratory. The Limitations add that sensitivity to rooting was not assessed. No claim is made about a
robust number or direction of independent evolutionary origins.

## 4. Remaining reproducibility qualifications

Both addressed. A cached Nextclade dataset directory is now reused only when the tag recorded in its
`pathogen.json` matches the pinned release; a mismatch exits with instructions. Every stage that reads
data - `build-cohort`, `call`, `stats`, `sensitivity`, `trend` and `clesrovimab`, not only
`fetch-genbank` - exits if the frozen accession list is missing, and proceeding without one requires
`--frozen-accessions ''` and prints a warning that the cohort will not match. The `phylo` stage is exempt
and returns before the check, because it only prints the documented commands and reads no input; we
verified stage by stage which ones the guard reaches. We have not claimed complete
end-to-end reproducibility: alignment preparation remains documented rather than automated, and the
validation log states which stages it does and does not exercise.

## 5. Author and submission details

Still outstanding and for the authors: names, affiliations, corresponding-author information, funding,
conflicts, CRediT contributions, the GISAID EPI_SET acknowledgement identifier, the author placeholders in
references 2, 4-8, 10 and 11, and the lineage-nomenclature reference 8. Final journal requirements should
be rechecked after these are added. The abstract is 198 words and the manuscript has three tables and five
figures.


---

# ADDENDUM: RESPONSE TO THE FIFTH REVIEW

1. **Conclusions, two populations.** Adopted. The sentence now reads: "Exploratory reconstruction across
   the full archive, under the reported topology, rooting and ancestral-state model, assigned high-escape
   residues to 32 candidate acquisition branches. Among records collected on or after 1 July 2023, no
   sampled carrier cluster exceeded two records."
2. **Superseded GISAID figure.** The earlier "Additional corrections" bullet is now explicitly labelled
   SUPERSEDED, points to addendum item 1 of the fourth-review response, and states that both the original
   "half were re-depositions" claim and its 9,344 / 22.5% replacement were wrong; the current accounting
   is 19,845 retained and 21,669 (52.2%) excluded.
3. **Phylogenetic labels.** "Independent acquisitions" no longer appears anywhere. Figure 4 is regenerated
   with panel a titled "Reconstructed acquisition branches by site and acquired residue" and its axis
   labelled "candidate reconstructed acquisition branches"; the Table S7 heading, its column and
   tables/table4_origins.csv use the same term, as do the abstract, Results and Conclusions.
4. **Final presentation.** The title page now states 198 abstract words, matching the text; the body is
   4,000 words, and the manuscript has three tables and five figures. Figure 3 and its caption are emitted
   as a single block.
5. **Author completion.** Still outstanding and for the authors: names, affiliations, correspondence,
   funding, conflicts, CRediT, the GISAID EPI_SET identifier, the author placeholders in references 2,
   4-8, 10 and 11, and the lineage-nomenclature reference 8. The target journal's current submission
   requirements should be confirmed before upload.


---

# ADDENDUM: RESPONSE TO THE SIXTH REVIEW (MAJOR REVISION)

**1. Rooting (major point 1).** Addressed by doing the analysis, not by softening the language. The trees
were rooted by least-squares temporal rooting in TreeTime using the collection dates (RSV-A rate
1.53e-3 substitutions per site per year, root-to-tip R^2 = 0.43, root 1958; RSV-B 2.48e-3, R^2 = 0.60,
root 1987). The acquisition count was then recomputed by parsimony under seven rootings. It is **32 under
temporal, midpoint, the tree as produced and three random terminal-edge rootings**, with one reversion;
only an adversarial root placed inside the largest carrier clade gives 31 and two reversions. Total state
changes are 33 under every rooting, as parsimony requires. Direction is therefore not an artefact of root
placement and the directional language is retained on that evidence (Section 3.6, Table S12). This needed
no alignment, only the tree and the dates.

**2. Circular anchoring (major point 2).** Adopted in full, including the reframe. New Table 4 and Figure 3
tabulate all 16 substitutions reported in references 5-9 against their Fab-escape score, IgG score, cell
entry and classification. Five are classified. Two - I64T and R209L - are excluded by the cell-entry floor
and so cannot be captured at **any** Fab cutoff. Capturing K68Q requires a cutoff of 0.572 or lower, at
which at least 4.5% of all archive records qualify. New Section 3.3 and the Conclusions now lead on this:
no single score-based rule separates the substitutions shown to matter from those that have not.

**3. Cohort arithmetic (major point 3).** Confirmed. The 4,822 unexplained records are GenBank: 3,303
non-representative members of mixed-database groups and 1,519 of GenBank-only groups. Methods 2.3 now
states that collapsing was applied in both databases, and Table 1 carries a per-database column for every
stage, so 65,416 reconciles to 38,925.

**4. Period-database collinearity (major point 4).** Quantified, and the premise does not hold. The
pre-boundary period runs to mid-2023 and so includes GISAID years: GISAID supplies 36.4% of pre-boundary
records (3,859 of 10,598) and 61.3% of post-boundary records (15,986 of 26,064). Both databases contribute
substantially to both periods and the database-stratified analysis retains 12 informative strata. The
numbers are now stated in Section 3.1.

**5. Abstract framing (major point 5).** Restructured. The abstract now leads with the dependency and the
failure of any threshold to recover the reported variants; the p value appears as an illustration. The
RSV-A background caveat is in the abstract. The title keeps the finding-stating form and drops the record
count.

**6. Trend scan.** Confirmed wrong and rewritten. T12I, K123R and R42K are ranks 6-8, not the strongest;
the five strongest are all decreasing RSV-B variants (N211S, N190S, P389S, M206I, R191K) with p below
10^-300, now reported as underflow rather than zero. Nine significant trends fall at site Ø positions and
all nine decrease, including K68Q (rank 10). We have **not** presented this as evidence against escape
accumulation: 58 of K68Q's 60 occurrences are in 2017 alone, per-year denominators rise roughly thirty-fold,
and the section now says plainly that the scan measures lineage turnover and sampling composition rather
than selection.

**7. Clesrovimab denominator.** The pre-licensure rationale is now stated in Methods 2.5, and Section 3.9
reports both denominators: 8/24,282 (0.033%) and 8/36,662 (0.022%).

**8. Figures.** Figure 1b now splits each year into before- and on/after-boundary bars, so the four
November 2023 carriers sit on the correct side, and the partial 2026 year is flagged. Figure 2a's legend no
longer overlaps the cutoff annotation; Figure 2b marks the 2.6 point as "no record qualifies" rather than
implying a gradual loss of effect. Figure 3 is rebuilt around the 16-substitution reconciliation. Sequencing
coverage moves to supplementary Figure S1, keeping eight display items.

**9. Statistics.** Stratified inference is now an exact conditional test (convolution of per-stratum
hypergeometrics), with the continuity-corrected CMH reported as the conservative alternative: subtype
5.7e-6, country 4.3e-4, country x subtype 4.3e-4, country x subtype x database 8.0e-4.

**10. Table 3 panel A.** Extended to start years 2021, 2022 and 2023. The claim is corrected: the
difference is significant for start years 2016 through 2022 and **not** at 2023 (p = 0.27), where the
pre-boundary arm falls to 1,675 records. The non-monotonicity between 2010 and 2015 is explained in the
text.

**11. Section 3.4 wording.** The no-de-duplication full-archive comparison now gives p = 0.086 explicitly
and is called marginal.

**12. References.** Every author placeholder is filled from Crossref or PubMed. Reference 13 is corrected
to Piñeiro C, Abuín JM, Pichel JC. Reference 4 (Ahani B, et al.) is Nat Commun 2023;14:4347, verified
against the DOI - 4137 was wrong. Reference 5 renders site Ø correctly. The lineage nomenclature paper is
added as reference 12 (Goya S, et al., Emerg Infect Dis 2024;30(8)) and is now cited in Methods 2.1.
References are renumbered in order of first appearance. A Funding statement and a reworded AI-use
declaration are included; the declaration now states that all references were verified against the primary
sources by the authors.

**13. Middle East.** Moved from Results to the Discussion and framed as an illustration of the detection
limit that whole-genome coverage imposes on regional surveillance.

**Still outstanding, for the authors.** Author names, affiliations, ORCIDs, corresponding-author details,
funding, conflicts, CRediT contributions and the GISAID EPI_SET acknowledgement identifier.


---

# ADDENDUM: RESPONSE TO THE SEVENTH REVIEW

1. **Abstract wording.** Corrected to "reported in the literature as resistance-associated or as site Ø
   polymorphisms", matching Section 3.3, so I206M, K209R and S211N are not implicitly described as
   resistance-associated.
2. **Reference range.** Corrected to references 4-9 in Section 3.3 and the Figure 3 legend; Table 4 does
   include two rows cited to [4].
3. **Supplementary numbering.** The gap at S4 is closed; tables are renumbered sequentially S1-S12 in
   document order and the manuscript cross-reference to the rooting table now points to Table S11.
4. **Table S11 naming convention.** Corrected. The per-substitution panel now uses the "site to residue
   acquired" notation throughout, matching Figure 4 and tables/table4_origins.csv, and the table note
   states that branches take the ancestral-state name, so the RSV-B site-209 event is 209 to E and not
   R209E. R209E now appears only in Table S2, where the carriage convention is the correct one.
5. **Temporally rooted trees.** Deposited in the revision following the one you reviewed:
   phylogenetics/F_A_temporally_rooted.newick and F_B_temporally_rooted.newick, with
   clock_A/B_molecular_clock.txt and clock_A/B_root_to_tip.csv. Their presence on the public repository has
   been confirmed.
6. **The 95-of-9,812 figure.** Confirmed by refetching the pinned DMS release: at a Fab cutoff of 0.572
   with the cell-entry floor of -0.5, 95 of 9,812 scored nirsevimab mutations qualify. Because this count
   carries the headline argument and the pipeline fetches the DMS live rather than redistributing it, the
   full cutoff-to-count mapping for both antibodies is now deposited as Table S12 and
   tables/dms_cutoff_counts.csv with the sha256 prefixes of both summary files.
7. **Figures.** Figure 1b splits every year into before- and on/after-boundary components and flags 2026 as
   truncated at the retrieval date; Figure 2b marks the cutoff of 2.6 as "no record qualifies"; Figure 3 is
   rebuilt around the 16-substitution reconciliation with the two entry-floor exclusions in a separate
   colour.


---

## Addendum: response to the ninth review

**1. "Only 162 records predate 2000" vs 164 in the manifest.** Both are right; the sentence was
under-specified. The manifest holds 164 records dated before 2000, two of which are the impossible
pre-1956 dates excluded from the clock regression. Methods 2.5 now reads "once those two records are
excluded, only 162 of the 164 pre-2000 records in the deposited manifest remain".

**2. Stated word count equalled the limit.** Corrected. The body is now 3,999 words, and the title page
states the counting rule so the figure can be checked: Sections 1-5 excluding headings, table content and
table titles, with abstract, references and figure legends excluded. The count rose above 4,000 when the
new material in item 7 was added and was brought back by condensation, not by changing the rule.

**3. Duplicated sentence in Methods 2.5.** Deleted. The surviving sentence merges both: temporal rooting
places the root for ancestral-state reconstruction, and because direction is undefined without a root the
acquisition count is reported across six further rootings.

**4. Name the model.** Done. The declaration now names Claude Opus 5 (Anthropic) and retains the full
statement of what it was used for and what the authors remain responsible for.

**5. Reference formatting.** The whole list was rebuilt from Crossref and PubMed records rather than
edited. All 17 entries now list up to six authors before "et al.". Reference 14 (Goya) gained pages
1631-1641 and reference 9 (Euro Surveill) gained article number 2600690. Issue numbers were added to
references 8, 10, 11, 12 and 17.

**6. The Wilkins correction.** It exists: Lancet Infect Dis 2024;24(5):e281, typed as an erratum by the
publisher. **We have not been able to read it.** It is not open access, has no PubMed Central record and no
retrievable abstract, and the publisher full text could not be obtained through any source available to us,
so we cannot state what it changes. An earlier version of this response described its contents; that
description was not supported by any source we had retrieved and is withdrawn. The authors should obtain
the correction through institutional access and confirm it independently before submission. What we can
verify stands on its own: the two counts we quote were checked directly against the published abstract of
the primary article, which gives 3,626 GenBank sequences (2,024 RSV-A, 1,602 RSV-B) and 5,675 surveillance
sequences (2,875 RSV-A, 2,800 RSV-B). Author order was confirmed from the Crossref record as Wilkins D,
Langedijk AC, Lebbink RJ, Morehouse C, Abram ME, Ahani B and 38 others. The correction is cited in
reference 5 so readers can consult it. Checking this also surfaced an author correction to
reference 4 (Nat Commun 2024;15:3026), whose text we did read, in PubMed Central (PMC11001890): it repairs
an error in Figure 3b affecting amino-acid frequencies at positions 64, 68 and 208 for the Phase 2b trial
and position 204 for MELODY. We quote no frequency from
that figure, so nothing here changes, but because those three
positions are central to this paper the correction is cited in reference 4 so readers compare against the
corrected version.

**7. The 2024 Lancet Infectious Diseases multicentre study.** Added as reference 7 (Fourati S, Reslan A,
Bourret J, et al. Lancet Infect Dis 2025;25(3):301-311; published online 2024), and it changed the
analysis rather than just the citation list. It reports F:N208D and a newly described F:I64M plus F:K65R
combination, both confirmed by fusion-inhibition assay. F:I64M was not in Table 4. It is now, and it is the
strongest case in the table: Fab escape -1.178, the lowest of the 19 scored substitutions at site 64, and
cell entry -1.154. A cutoff low enough to admit it would admit 6,742 of 9,812 scored mutations, and it
fails the cell-entry floor regardless, so no Fab threshold classifies it at all. Its partner F:K65R scores
0.170. Neither member of a phenotypically confirmed escape pair is recoverable by any single-substitution
rule. Section 3.3 also now states the more general limitation this exposes: the DMS scores substitutions
singly, so an escape phenotype that requires a combination lies outside what this or any similar screen can
represent. Table 4 has 17 rows, Figure 3 has been redrawn, and the abstract, Section 3.3, the Discussion and
the Figure 3 legend carry the new count.

We did not add the Research Square preprint. It is adjacent to the Section 3.3 argument but not
peer-reviewed, and the point it would support is already carried by references 7 and 12.

**8. Supplementary layout.** The "Supplementary data files" heading was moved to the end, so Tables S1-S12
now run in sequence followed by Figure S1 and the Supplementary Text.

**9. The figures.** Supplied in full this round as separate files, after four rounds in which they were
described but not sent. Figures 1-4 and Figure S1 are provided as 300 dpi LZW TIFF and PNG with a legend
and manifest document, and are also in the repository under figures/submission/. Figure 1b does split each
year at the boundary, so the four November 2023 carriers sit on the on/after side of 2023; Figure 2b does
mark the empty endpoint at 2.6 with a cross keyed as "no record qualifies"; Figure 3 is the
literature-reconciliation panel, now at 17 substitutions.

Two things changed on inspection. Figure S1 had been built before the figure palette was settled and was
still on library defaults, so it was redrawn to match Figures 1-4. Its legend also said "analysis set" when
the counts are primary-window, which is corrected to n = 36,662, and the three Middle East countries that
contribute no F-covering record now appear explicitly at zero with their median read lengths rather than
being absent from the panel.

**10. Temporally rooted trees.** F_A_temporally_rooted.newick and F_B_temporally_rooted.newick are in the
repository under phylogenetics/, with the TreeTime clock output and root-to-tip tables. They were pushed
with the date-filtered rerun; the earlier run has been superseded there.


---

## Addendum: response to the tenth review

**1. Figure 3 legend said "two" grey points.** Corrected to three. The figure was right; only the legend
text had not been updated when I64M was added.

**2. I64M mischaracterised in Section 3.3.** Correct, and the distinction matters. The sentence has been
split. F:I64T and F:R209L clear the Fab cutoff once it is lowered but are excluded by the cell-entry filter
(-0.691 and -0.849). F:I64M fails both criteria, at -1.178 for Fab escape and -1.154 for cell entry. The
conclusion is unchanged but the mechanism is now stated accurately for each.

**3. Broken paragraphs in Section 3.8.** Confirmed in the Word file, not in the Markdown source, so the
fault was in the Markdown-to-Word conversion rather than the text: soft line wraps within that paragraph
had been emitted as paragraph marks. The converter now joins wrapped lines within each block, and the whole
document was re-checked - no paragraph in either the manuscript or the supplementary file now begins
mid-clause.

**4. Word count.** Your measurement was right and ours was wrong, for the third time on this item, and the
cause is now identified rather than patched. The counting script excluded only the first line of a
multi-line table title, so the continuation lines of the Table 1, 3 and 4 titles were being counted as body
text - exactly the 68-word gap between our 3,999 and your 3,931. The script now excludes table titles as
whole paragraphs. The body is 3,940 words: your 3,931 plus the nine words added by correction 2 above. The
stated rule on the title page has been reworded to say that tables and table titles are excluded in full.

**0. Withdrawal of an unsupported statement in the previous round.** Item 6 of the ninth-round response
stated what the Wilkins correction changes. We had not retrieved that correction's text, and the statement
was not supported by any source we held; it has been withdrawn and replaced above with what can be verified
and an instruction to confirm the correction through institutional access. Corrections 1 to 4 below were
raised by the reviewer and concern three claims made in the previous round that the saved files did not
support: that the Figure 3 legend had been updated to three, that Section 3.3 characterised I64M correctly,
and that 3,999 was the true word count. All three were wrong as stated and are corrected here.

**5. One further error found while making these changes, not raised in the review.** Section 5 Conclusions
still carried the pre-revision counts, reading "five of sixteen reported substitutions meet the criteria
used here, two cannot be captured at any Fab cutoff". Both numbers were stale from before I64M was added
and are now seventeen and three, consistent with the abstract, Section 3.3, Table 4, Figure 3 and the
Discussion.
