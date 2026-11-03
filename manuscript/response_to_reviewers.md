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
