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

**De-duplication framing.** Adopted. Results 3.4 now compares fractions (0% against 0.117% in the primary
window; 0.070% against 0.117% across the full archive) and states that the smaller p value obtained
without de-duplication is not stronger evidence, because records matching on F sequence, country and date
are not independent observations, and that the de-duplicated analysis remains the principal comparison.

## Comment 5. Figure annotations

- **Figure 2a title.** Confirmed: "three orders of magnitude" was unsupported. Among non-zero values
  carriage falls about 70-fold (4.45% to 0.065%); the title now says so and the legend states that no
  finite ratio is defined where a period count is zero.
- **Figure 2b title.** Confirmed: significance is not simply lost. The title now reads "Not significant
  between cutoffs of 1.2 and 1.8; reversed at 1.0", and the legend notes that the open circles include the
  significant reversal.
- **Figure 2c and Figure 4 legends.** Corrected dates and countries as above.
- **Table 2 and figure legends.** "Before/after rollout" is replaced by the fixed 1 July 2023 calendar
  boundary, with an explicit statement that national rollout timing was not used to assign periods.

## Additional corrections

- **GISAID matching.** Confirmed that the collapsed total conflated within-database repetition with
  cross-database matches, and the previous "half were re-depositions" figure was wrong. Recomputed: of
  41,514 GISAID records passing QC, 16,973 (40.9%) fall in a group that also contains a GenBank record;
  7,660 fall in GISAID-only groups of two or more, which is within-database repetition; 9,344 (22.5%) were
  not retained as representatives. Methods 2.3 and the Discussion now give this breakdown, use "match on F
  sequence, country and collection date" rather than "re-deposition", and state that matching on these
  three fields is consistent with but does not demonstrate the same specimen.
- **Abstract denominator.** Clarified to "25,384 GenBank records with 44,275 eligible GISAID EpiRSV records
  (69,659 in total)".
- **Year-only records.** Confirmed: 538 is the full archive and only 190 are in the primary window (177
  before the boundary, 13 after). Methods 2.2 and Results 3.4 now say so.
- **Table S1.** Confirmed 83 categories including an unnamed one with 4 records. Reported as 82 named
  countries plus 4 records with no country, labelled "(country not stated)" in the table, and stated in
  Results 3.10.
- **Display items.** Tables 3a and 3b are merged into a single Table 3 with panels A and B, giving eight
  display items with Figures 1-5. The title page states this.
- **Supplement legibility.** The supplement is now landscape with wider columns and 8-point table text;
  headers repeat and rows do not split.

## Outstanding, for the authors

Author names, affiliations, corresponding-author details, funding, conflicts of interest, CRediT
contributions, the GISAID EPI_SET acknowledgement identifier, and the author placeholders in references 2,
4-8, 10 and 11, of which reference 8 (the lineage nomenclature consortium paper) is still to be selected.
Final journal requirements should be checked directly rather than relying on the limits stated on the title
page.
