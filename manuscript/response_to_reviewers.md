# RESPONSE TO THE SECOND REVIEW

**Manuscript.** Threshold and time-window choices determine whether nirsevimab escape substitutions appear to have increased: an analysis of 38,925 public respiratory syncytial virus genomes

We thank the reviewer. One comment changed the conclusion of the paper rather than its wording, and we
have rebuilt the study around it. Every numerical claim in the review was independently recomputed; all
were confirmed. Changes are summarised below with their location in the revised manuscript.

---

## Comment 1. Report the sensitivity to the analysis window

**Confirmed, and decisive.** We reproduced the reviewer's calculation exactly: across the full archive the
comparison is 13/12,861 (0.101%) before 1 July 2023 against 35/26,064 (0.134%) after, Fisher p = 0.44. We
also ran the start year as a continuous sweep and found the transition is a cliff rather than a gradient:
the comparison is significant for every first-included year from 2016 onward and null for every earlier
one. Twelve of the 13 historical carriers are a single 2015 Argentinian RSV-B cluster at site 209, with two
from Viet Nam in 2014 and one from Germany in 2002.

**Action.** The paper no longer claims that escape substitutions increased after prophylaxis. Its claim is
now that whether they appear to have increased is determined by the classification threshold and the
analysis window, with both sweeps reported as co-primary results. The title, abstract, Results (new Section
3.2), Discussion and Conclusions were rewritten accordingly. Table 3a and Figure 2c are new. We did not
manufacture a result-independent justification for the 2017 start: Section 3.2 states the ways pre-2017
records differ (25 countries against 82, no GISAID deposits, predating the lineage nomenclature) and then
states plainly that these are not strong enough to carry the inference, which is why both windows are
reported.

**Confirmed contradiction.** The Discussion and Conclusions sentences asserting onset in 2023 while Section
3.1 reported 13 historical carriers were a flat self-contradiction. Both are now scoped explicitly, and the
Conclusions state that the contrast does not hold across the full archive.

## Comment 2. Document the date correction and preserve date precision

**Confirmed.** Source precision is now recovered and carried through: of 65,416 dated records, 63,033 have a
full date, 1,429 a year and month, 954 a year only. In the analysis set the figures are 37,804 / 583 / 538,
of which 29 year-only records fall in 2023 and are assigned to the earlier period by the expansion
convention. None of the 538 is a carrier.

**Action.** New Section 2.2 states the parsing rule and the convention. Every deposited manifest now carries
a `date_precision` column alongside the date exactly as deposited. The comparison was rerun three ways
(Section 3.4): excluding the 29 ambiguous 2023 records (p = 1.3e-5), excluding all year-only records
(p = 1.3e-5), and restricting to full-date records (p = 1.4e-5). As the reviewer anticipated, this does not
explain the association.

## Comment 3. Complete and validate the advertised workflow

**Confirmed; the previous script over-claimed.** `code/pipeline.py` now implements every analysis it
advertises: carriage, the threshold sweep, the new window sweep, stratified inference by subtype, country,
country-by-subtype and country-by-subtype-by-database, the de-duplication, date-precision and
cell-entry-floor sensitivity analyses, the Cochran-Armitage trend scan, and the clesrovimab analysis.

**Validation.** Rather than describe it, we executed it. The analysis functions were run against the
deposited analysis set and reproduce every number in the Results except the acquisition counts, which come
from the deposited trees. The output is deposited as `logs/validation_run.txt`, including the exclusion
counts at each assembly stage.

**Version control.** The GenBank arm now consumes the frozen accession list by default rather than current
holdings. The DMS source is pinned to commit `3ecdfaa661304e3c284acdbeacc9662d2baa1dd9`, and the sha256 of
the fetched bytes is verified at run time by `verify_dms()`, which `escape_set()` calls on every fetch.
Nextclade dataset tags and all tool versions are recorded in the module docstring.

**Scope limited to what is demonstrated.** The phylogenetic stage is not wrapped in a function; `pipeline.py
phylo` prints the exact commands used, and the trees, annotated TreeTime output and branch-mutation tables
are deposited under `phylogenetics/`. Figure generation is not included. The Data Availability statement now
says precisely this instead of claiming complete reproducibility.

**Missing deliverable.** `manifests/deduplication_groups.csv` is now deposited: 65,416 member rows across
38,925 groups, keyed by an opaque group identifier with the retained representative flagged, and with no
sequence data, as the reviewer suggested.

## Comment 4. Test the impact of de-duplication

**Confirmed that the rule needed testing; the result is reassuring.** Retaining every record, the primary
window gives 0/17,318 against 53/45,318 (p = 6.8e-8), a stronger association than the de-duplicated
analysis, while the full archive gives 14/20,098 against 53/45,318 (p = 0.086) and remains null.
De-duplication is therefore not generating the primary contrast, and the window dependence survives its
removal. Reported in Section 3.4 and Table S11; the Limitations no longer call the rule "conservative"
without evidence.

## Comment 5. Country composition and sparse-event adjustment

**Addressed with analysis rather than a limitation statement.** Continuity-corrected CMH: by subtype
p = 3.0e-4 (2 informative strata); by country p = 0.0060 (6); by country and subtype p = 0.0059 (9); by
country, subtype and database p = 0.0082 (12). The number of informative strata is reported with each
statistic. Country-by-period-by-subtype denominators for all 156 combinations are deposited and the 40
largest appear as Table S10. The period association is described as exploratory throughout; the fixed
calendar boundary is used consistently and country-specific rollout dates were not introduced.

## Comment 6. Retain uncertainty in the phylogenetic claims

**Addressed.** Section 3.5 now states that the count of 32 is a reconstruction-dependent estimate
conditional on one topology and one ancestral-state model, and that the 32 branches are counted on the full
38,925-record archive whereas the 35 carriers are the post-boundary subset of the primary window. Four of
the six internal acquisitions remain unrecovered as bipartitions and are reported as uncertain. Trees,
annotated NEXUS output and branch-mutation tables are deposited. Figure 4 was regenerated: the panel-b
assertion of no onward spread is gone, replaced by carrier-descendant counts keyed by branch-support status.

**Additional correction found while regenerating Figure 4.** The same RSV-B event is named R209E under the
consensus-relative convention used for carriage and K209E under the ancestral-state convention used for
acquisitions, because the reconstructed ancestor carried lysine. Methods 2.4 now states both conventions
explicitly and the acquisition figures and tables use "site to acquired residue" notation.

## Comment 7. Finish defining the functional endpoint

**Addressed.** The twelve qualifying nirsevimab mutations fall at five positions (68, 201, 208, 209, 210);
99.69% of primary-window records have all five callable and mean callability at those positions is 99.93%,
so the 95% overall coverage filter is not diluting the denominator where it matters (Section 2.4). The
cell-entry floor was varied from -2.0 to 0.0, changing the qualifying set from 23 to 9 mutations and the
carrier count from 36 to 31, with p between 7.6e-6 and 3.4e-5 (Section 3.4). The claim that every analysis
was repeated across cutoffs is withdrawn: Section 2.5 now states that the trend scan, the acquisition
analysis and the clesrovimab analysis were run at the primary cutoff only. The clesrovimab analysis is
labelled exploratory in the Results, the Discussion and the Limitations.

## Comment 8. Remove contradictions across the files

**Addressed.** The repository was rebuilt from the final outputs. README.md is rewritten around the revised
conclusion and no longer describes a population-level study or the reference-artefact claim. PIPELINE.md is
deleted and replaced by the executable workflow. The four superseded `RSV_F_escape_*` manuscript files are
removed from the repository. Table S6 now separates the eight primary-window clesrovimab carriers from the
2016 Australian record and labels both populations. The supplement carries the revised title and framing.
Figures 2 and 4 are regenerated; the other three are unchanged and remain correct.

## Comment 9. Smaller factual and presentation errors

- **Figure 1 legend.** Confirmed: there are four 2023 carriers, not three (one RSV-A from Spain on 5
  November and three RSV-B from France and Spain, 10-23 November). The legend now gives four and retains
  the calendar-year aggregation explanation.
- **Database claim.** Confirmed. The claim now carries its 2017-onward qualifier, and Section 3.7 reports
  the older GenBank record MZ568972 from Germany, 18 March 2002, which also carries N201T.
- **Terminology.** "post-2023" is replaced throughout by "on or after 1 July 2023". Site Ø now uses the
  correct notation in the text; the only remaining "site O" is inside the published title of reference 1,
  which we have not altered.
- **Running head.** Confirmed at 41 characters. The running head was rewritten and is now "RSV F escape
  substitutions in public genomes", 44 characters, matching the stated count.
- **Table pagination.** Rows are set not to split and header rows repeat across pages. Supplementary
  accession columns were narrowed and the table font reduced.
- **Placeholders.** Author names, affiliations, corresponding author, conflict of interest, funding,
  reference 8 (the lineage nomenclature consortium paper) and the GISAID EPI_SET identifier remain for the
  authors to complete before submission.

---

## Summary of what changed scientifically

The previous version reported that escape substitutions were absent before prophylaxis and present
afterwards. That finding was an artefact of the 2017 start date. The revised paper reports instead that the
same archive yields a significant increase, no change, or a significant decrease depending on two analyst
choices, and that published frequencies stating neither cannot be compared or pooled. The substitutions are
not new: they are present in the archive from 2002 and 2014-15.
