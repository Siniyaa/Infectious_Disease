# Cover letter

[Date]

The Editorial Board
*Scientific Reports*

Dear Editors,

We are pleased to submit our manuscript, **"Threshold and time-window choices determine whether nirsevimab
escape substitutions appear to have increased in public respiratory syncytial virus genomes"**, for
publication as an Article in *Scientific Reports*.

Nirsevimab is now given to infants in national programmes across Europe, North America and beyond, and
whether resistance to it is emerging is a question of immediate public-health importance. Several groups
have published frequencies of resistance-associated substitutions in the fusion (F) protein since rollout,
and those frequencies disagree. Our manuscript establishes why they disagree, and what has to be reported
for them to be comparable.

We assembled and uniformly reprocessed the entire public RSV sequence archive: 25,384 GenBank and 44,275
eligible GISAID EpiRSV records, 69,659 in total, reduced to 38,925 after de-duplication across both
databases. To our knowledge this is the largest analysis of the nirsevimab binding site yet performed,
roughly ten times the size of the previous archive-scale study, and the first to combine both repositories
with explicit cross-database de-duplication. That step proves to be essential rather than cosmetic: half of
the GISAID records matched a GenBank deposit, so naive pooling inflates the denominator by tens of
thousands of records, yet the retained GISAID records contained every primary-window F:N201T carrier.
Neither database alone is adequate, and we quantify this for the first time.

Three findings follow. First, applying the recently published deep mutational scanning measurements to the
whole archive shows that no score-based rule applied to one substitution at a time reproduces the
substitutions reported as resistance-associated: five of seventeen meet the criteria, three fail the
cell-entry filter at any escape cutoff, and capturing F:K68Q, which has a published clinical case, requires
a cutoff at which at least 4.5% of all archive records would be classified as carriers. Because the scan
scores substitutions individually, a phenotypically confirmed escape pair is invisible to any such rule at
all. Second, the apparent post-rollout increase is determined by the collection-year window: within a
2017-onward window the contrast is strong, with no carrier before 1 July 2023 against 35 of 26,064 after
(0.134%, 95% CI 0.094-0.187; Fisher p = 1.3 × 10⁻⁵), yet across the full archive the same comparison is not
significant (p = 0.44), because the same substitutions are present in deposits from 2002 and 2014-15.
Third, it is equally determined by where the threshold is set, reversing at permissive cutoffs.

The practical consequence is concrete and immediately usable: reported RSV resistance frequencies should
always be accompanied by the classification rule, the reference baseline and the collection-year span from
which they derive. Without these, two careful groups analysing the same archive can report opposite trends
and both be correct. We also show that the apparent emergence of substitutions can be an artefact of which
consensus is used as a baseline, and we document a published instance of this in the current literature.

The work is reproducible end to end from public data. Accession manifests for every analysis population,
the complete de-duplication group mapping, the maximum-likelihood and temporally rooted phylogenies, the
TreeTime output, every derived table and the full analysis workflow are deposited at
https://github.com/Siniyaa/Infectious_Disease. Sequence data are not redistributed, in accordance with
GISAID terms, but the manifests allow any user with GISAID access to reconstitute the cohort exactly. We
report sensitivity analyses across thresholds, windows, de-duplication, date precision, cell-entry filtering
and seven tree rootings, so that every claim can be checked against the choice that produced it.

The manuscript is original, has not been published previously and is not under consideration elsewhere. All
authors have approved the submission. The study used only existing public sequence deposits, with no human
participants, clinical specimens or identifiable individual data, so ethical approval was not required. As
declared in the manuscript, a generative artificial-intelligence assistant was used in writing and
debugging the analysis code, running the analyses and drafting and revising the text; the authors defined
the research question, directed the analysis, reviewed the code and outputs, verified every reference
against its primary source, and take full responsibility for the content and the conclusions. The authors
declare no competing interests and received no specific funding for this work.

We hope you find the manuscript suitable for *Scientific Reports* and look forward to your decision.

Yours sincerely,

Andreas Henschel, on behalf of all authors
Department of Computer Science, Khalifa University of Science and Technology, Abu Dhabi, United Arab Emirates
Email: [to be completed]
