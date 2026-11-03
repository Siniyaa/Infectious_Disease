# TITLE PAGE

**Title.** Threshold and time-window choices determine whether nirsevimab escape substitutions appear to have increased: an analysis of 38,925 public respiratory syncytial virus genomes

**Running head.** RSV F escape substitutions in public genomes (44 characters)

**Authors.** [To be completed by the authors.]

**Affiliations.** [To be completed by the authors.]

**Corresponding author.** [Name, postal address, email, telephone - to be completed.]

**Keywords.** respiratory syncytial virus; nirsevimab; resistance-associated substitution; genomic surveillance; fusion protein

**Word counts.** Abstract 193 words (limit 200). Text approximately 3,400 words (limit 4,000). References 14 (limit 50). Display items 8: Figures 1-5 and Tables 1-3 (limit 8).

---

## ABSTRACT

Reported frequencies of nirsevimab resistance-associated substitutions in respiratory syncytial virus (RSV) differ between studies that use different reference sequences, different functional thresholds and different time spans. We combined 25,384 GenBank records with a GISAID EpiRSV export (69,659 records), processed both uniformly, called fusion (F) protein variants against each subtype's own consensus, and classified residues using published deep mutational scanning (DMS) scores. After de-duplication 38,925 records remained. Among records collected from 2017 onward, none of 10,598 predating 1 July 2023 carried a DMS-defined high-escape substitution against 35 of 26,064 collected on or after that date (0.134%, 95% CI 0.094-0.187; Fisher p = 1.3 x 10-5). That contrast is contingent on two analyst choices. Including records from before 2016 adds 13 historical carriers, mostly one 2015 Argentinian cluster, and the comparison becomes null (13/12,861 versus 35/26,064, p = 0.44). Lowering the Fab-escape cutoff from 2.036 to 1.0 reverses its direction. High-escape residues were reconstructed on 32 independent branches, 26 leading to a single sampled carrier. Of 689 F variants tested for temporal trend, 105 changed significantly (50 increasing, 55 decreasing) and none was high-escape. Archive-derived resistance frequencies require their threshold and window to be stated.

**KEYWORDS:** respiratory syncytial virus; nirsevimab; resistance-associated substitution; genomic surveillance; fusion protein

---

## 1 INTRODUCTION

RSV causes a large burden of lower respiratory tract infection in infants worldwide [9-11]. Long-acting
monoclonal antibodies directed at the prefusion conformation of the F protein are now used for infant
prophylaxis; nirsevimab binds antigenic site Ø, and clesrovimab, licensed more recently, binds a separate
epitope. In the Phase 2b and MELODY randomised trials more than 99% of RSV isolates retained susceptibility
to nirsevimab, and binding-site substitutions reducing susceptibility were found in isolates from two
participants [2].

Since prophylaxis became widespread, individual groups have reported F substitutions in circulating virus.
A 2026 systematic review of antigenic site Ø substitutions pooled seven studies and 2,156 samples, reporting
limited variability in RSV-A with K65R most common and higher substitution frequencies in RSV-B, while
distinguishing common polymorphisms that retain susceptibility from resistance-associated variants [1].
Primary reports include breakthrough RSV-B infections in France during 2024-25 [4], three children in Spain
in 2025/26 carrying F:N201T with recombinant expression confirming reduced nirsevimab recognition [5], 68
isolates from Eastern Spain in 2023/24 [6], and a single adult case carrying F:K68Q [7]. These studies use
different reference sequences, different definitions of a resistance-associated substitution and different
observation periods, so their reported frequencies are not directly comparable.

A deep mutational scan (DMS) of RSV F has since measured how nearly all F mutations affect cell entry and
neutralisation by nirsevimab and clesrovimab, reporting that resistant strains have arisen sporadically but
remain rare, and showing that bivalent IgG binding buffers escape so that Fab potency is the more sensitive
readout [3]. We applied that functional classification to the combined public sequence archive. Our aim is
not to estimate a resistance frequency, which archive data cannot support, but to measure how strongly such
an estimate depends on two choices an analyst must make and rarely reports: where the functional threshold is
set, and which collection years are included.

## 2 MATERIALS AND METHODS

### 2.1 Sequence assembly

GenBank contributed 25,384 sequence records for human orthopneumovirus (taxon 11250) of 13-16 kb. A GISAID
EpiRSV export contributed 56,856 unique records, of which 44,275 passed filtering for human host, 13-16 kb
length and a resolvable collection date; 4,267 records lacked an accompanying metadata row and were excluded.
GISAID holdings begin in 2020, so earlier coverage rests on GenBank alone. Retrieval date was 2 November 2026.

The combined 69,659 records were assigned to subtype with the Nextclade minimizer index (RSV-A 37,290,
RSV-B 32,365; one record sorted to human metapneumovirus and three were unassigned, all excluded) and aligned
to the corresponding reference dataset [12], which supplied consortium lineage assignments and
reference-anchored F translations. Alignment-based extraction was used rather than deposited CDS annotation,
which is present in only 60-65% of GenBank genome records and varies by year. Records were retained with F
coverage of at least 95% of the 574-residue frame, leaving 65,416. Table 1 gives the full accounting.

| Stage | Records |
|---|---|
| GenBank sequence records retrieved (taxon 11250, 13-16 kb) | 25,384 |
| GISAID EpiRSV records retrieved (unique) | 56,856 |
| GISAID records passing host, length and date filters | 44,275 |
| Combined input to subtype assignment | 69,659 |
| Assigned RSV-A / RSV-B (1 human metapneumovirus, 3 unassigned excluded) | 37,290 / 32,365 |
| F coverage >=95% and a resolvable collection date | 65,416 |
| After de-duplication on identical F, country and collection date | 38,925 |
| Primary analysis window, 2017 onward | 36,662 |

**Table 1.** Cohort assembly.

### 2.2 Collection dates and their precision

Deposited collection dates vary in precision. Of the 65,416 dated records, 63,033 carry a full date, 1,429 a
year and month, and 954 a year only. Partial dates were expanded to the first day of the stated month or
year and flagged; the precision flag is deposited for every record, alongside the date exactly as deposited.
A year-only date cannot be allocated across a mid-year boundary, so the primary comparison was repeated with
those records excluded. In the de-duplicated analysis set 37,804 records carry a full date, 583 a month and
538 a year only, of which 29 fall in 2023 and are assigned to the earlier period by this convention. None of
the 538 year-only records is a carrier, and excluding them does not materially change the result (Section
3.4).

### 2.3 De-duplication across databases

Records identical in F sequence, country and collection date were collapsed to one. Cross-database
redundancy was measured rather than assumed: 12,325 such groups contained both a GenBank and a GISAID
record, and 52.2% of GISAID records (21,669 of 41,514) collapsed into a record already present. Of the
38,925 resulting groups, 16,171 contain more than one record. This rule will collapse genuinely distinct
infections that share an F sequence, a country and a date, so full group membership - an opaque group
identifier, every member accession, its database, date and precision flag, and which member was retained -
is deposited, and the primary comparison was repeated with no de-duplication at all (Section 3.4). Because
the archive is a convenience sample, the resulting records are described throughout as **de-duplicated
archive records**, not as a population denominator.

### 2.4 Variant calling and functional classification

Variants were called against each subtype's own consensus, computed from the analysis set, because the two
subtype consensuses differ at 59 of 574 F residues. Observed residues were joined to the DMS tables [3] on
site and mutant residue; the scan's numbering matched the RSV-A consensus at 98.4% of its 504 scored sites.

A residue was classified **DMS-defined high-escape** when its Fab-escape score was at least 2.036 with cell
entry at or above -0.5 (12 nirsevimab and 6 clesrovimab mutations of 9,812 scored). The cutoff is anchored on
F:N201T, for which reduced nirsevimab recognition has been demonstrated by recombinant expression [5]. This
is a deliberately narrow, score-based category and is **not** equivalent to the set of all known
resistance-associated variants: F:K68Q, reported in a severe adult case [7], scores 0.572 and falls outside
it at every cutoff examined, while the DMS study itself reports subtype-dependent effects at position 201 and
reduced IgG neutralisation for K68Q on an RSV-B background [3]. Because the category is defined by score
rather than phenotype, and because no virus in this study was tested functionally, all classifications are
described as predicted.

Twelve nirsevimab mutations fall at five F positions (68, 201, 208, 209, 210). Across the primary window
99.69% of records have all five positions callable and mean callability at those positions is 99.93%, so at
least 95% overall F coverage is not materially diluting the denominator at the positions that matter.

The DMS was performed on an RSV-A background, so its transfer to RSV-B is an assumption stated per
substitution. The two RSV-B substitutions contributing most carriers sit at sites where the RSV-B consensus
matches the scan's wildtype (N208D: wildtype N, RSV-B consensus N; K68I: wildtype K, RSV-B consensus K), and
the RSV-A carriers are scored on the scan's own background. Matching the wildtype residue does not establish
that the score transfers unchanged across backgrounds, and no such claim is made.

**Two naming conventions are used and should not be conflated.** Carriage is reported relative to each
subtype's consensus, so the RSV-B departure at site 209 is R209E. Acquisition branches are named by the
ancestral state reconstructed at that branch, which may differ from the consensus; the same RSV-B event is
K209E because the reconstructed ancestor carried lysine. Acquisitions are therefore reported as site and
acquired residue (for example, 209 to E).

### 2.5 Statistics and phylogenetics

Proportions and their intervals are Clopper-Pearson throughout, including zero-count upper bounds. Periods
were compared with Fisher's exact test at a fixed calendar boundary of 1 July 2023, and with a
continuity-corrected Cochran-Mantel-Haenszel (CMH) test as the stratified inference. Stratified analyses are
reported by subtype, by country, by country and subtype jointly, and by country, subtype and source database
jointly; strata with no events or no records in one period contribute nothing and the number of informative
strata is reported with each statistic. Temporal trend used the Cochran-Armitage test with per-year counts
reported beside every statistic, Bonferroni-corrected across all variants carried by at least five records.

Two sensitivity analyses are treated as primary rather than supplementary: the period comparison was repeated
across Fab-escape cutoffs from 1.0 to 2.6, and across first-included collection years from the full archive
through 2020. Three further sensitivity analyses are reported in Section 3.4 (de-duplication, date
precision, cell-entry floor). The trend scan, the acquisition analysis and the clesrovimab analysis were run
at the primary cutoff only.

Maximum-likelihood F phylogenies were built per subtype with VeryFastTree under GTR+gamma [13] (20,767 and
18,158 tips, midpoint-rooted) and amino-acid ancestral states reconstructed with TreeTime [14] under an
inferred GTR model. Acquisitions were counted as branches on which a high-escape residue appears, and their
spread measured as descendant tips that actually carry that residue. Branch support was taken from the
maximum-likelihood topology by matching nodes on descendant tip sets; support is undefined for terminal
branches, and acquisitions whose clade is not recovered as a bipartition are reported as unsupported rather
than assigned a value. Trees, annotated TreeTime output and branch-mutation tables are deposited.

## 3 RESULTS

### 3.1 Carriage in the primary window

Among 36,662 records collected from 2017 onward, none of the 10,598 collected before 1 July 2023 carried a
DMS-defined high-escape substitution, against 35 of 26,064 collected on or after that date (Table 2,
Figure 1). This is an absence of detection in the analysed sample, not demonstrated biological absence.

| Subtype | Era | Carriers / n | Carriage (%) | 95% CI (%) |
|---|---|---|---|---|
| RSV-A | Before rollout | 0/5,584 | 0.0 | 0.000-0.066 |
| RSV-A | After rollout | 9/14,013 | 0.064 | 0.029-0.122 |
| RSV-B | Before rollout | 0/5,014 | 0.0 | 0.000-0.074 |
| RSV-B | After rollout | 26/12,051 | 0.216 | 0.141-0.316 |
| Both | Before rollout | 0/10,598 | 0.0 | 0.000-0.035 |
| Both | After rollout | 35/26,064 | 0.134 | 0.094-0.187 |

**Table 2.** Carriage among de-duplicated archive records collected from 2017 onward. Intervals are
Clopper-Pearson; zero counts are shown as exact upper bounds.

Pooled, Fisher p = 1.3 x 10^-5. Stratified by subtype, CMH p = 3.0 x 10^-4 (2 informative strata); by
country, p = 0.0060 (6 strata); by country and subtype, p = 0.0059 (9 strata); by country, subtype and
database, p = 0.0082 (12 strata). Country-by-period-by-subtype denominators for all 156 combinations are
deposited. The 35 carriers span 7 countries and 13 lineages and derive from both databases (20 GISAID, 15
GenBank). Because individual prophylaxis exposure is unrecorded, national implementation dates differ, and
sequencing effort rose sharply over the same interval, this association must not be read as evidence that
prophylaxis caused the difference.

### 3.2 The comparison depends on which collection years are included

The 2017 start date is a choice, and it determines the result. Extending the window backwards adds 13
historical carriers and the comparison becomes null (Table 3a, Figure 2c): across the full archive, 13 of
12,861 records predating the boundary carry a high-escape substitution (0.101%) against 35 of 26,064
afterwards (0.134%), Fisher p = 0.44.

The transition is abrupt rather than gradual. Significance is present for every start year from 2016 onward
and absent for every earlier start. Twelve of the 13 historical carriers are RSV-B records carrying glutamate
at site 209, ten from Argentina in 2015 and two from Viet Nam in 2014; the thirteenth is a German RSV-B
record from 2002 carrying N201T. The entire contrast therefore turns on whether one 2015 outbreak cluster is
inside or outside the window.

| First year included | Before 1 Jul 2023 | On/after 1 Jul 2023 | Fisher p | CMH p |
|---|---|---|---|---|
| all years | 13/12,861 (0.101%) | 35/26,064 (0.134%) | 0.44 | 0.44 |
| 2000 | 13/12,697 (0.102%) | 35/26,064 (0.134%) | 0.45 | 0.46 |
| 2005 | 12/12,643 (0.095%) | 35/26,064 (0.134%) | 0.35 | 0.35 |
| 2010 | 12/12,527 (0.096%) | 35/26,064 (0.134%) | 0.35 | 0.36 |
| 2014 | 12/11,592 (0.104%) | 35/26,064 (0.134%) | 0.53 | 0.48 |
| 2015 | 10/11,338 (0.088%) | 35/26,064 (0.134%) | 0.26 | 0.28 |
| 2016 | 0/11,040 (0.000%) | 35/26,064 (0.134%) | 6.7e-06 | 0.00021 |
| 2017 | 0/10,598 (0.000%) | 35/26,064 (0.134%) | 1.3e-05 | 0.0003 |
| 2018 | 0/10,055 (0.000%) | 35/26,064 (0.134%) | 1.4e-05 | 0.00049 |
| 2019 | 0/9,088 (0.000%) | 35/26,064 (0.134%) | 4.9e-05 | 0.001 |
| 2020 | 0/7,742 (0.000%) | 35/26,064 (0.134%) | 0.00017 | 0.0025 |

**Table 3a.** Period comparison as a function of the first collection year included.

Pre-2017 records differ from later ones in ways that motivate a modern-era restriction independently of this
result: they come from 25 countries against 82, contain no GISAID deposits against 54.1%, and predate the
consortium lineage nomenclature used here. But these differences are not strong enough to carry the
inference on their own - the concentration of sampling in the three largest contributing countries is
similar in the two eras (55.9% against 49.6%) - and we therefore report both windows and treat neither as
definitive. **Within the primary window the high-escape substitutions were not detected before mid-2023;
across the full archive they are not new.**

### 3.3 The comparison depends on where the functional threshold is set

Repeating the comparison across Fab-escape cutoffs shows three regimes (Table 3b, Figure 2a,b). Above 2.0 the
pre-boundary count is zero and the difference is significant up to 2.5, beyond which no record qualifies in
either period. Between 1.2 and 1.8 the comparison is null and the point estimate is higher before mid-2023.
At 1.0 the difference is significant in the reverse direction (5.38% before versus 4.45% on or after).

| Fab cutoff | Qualifying mutations | Before 1 Jul 2023 | On/after 1 Jul 2023 | Fisher p |
|---|---|---|---|---|
| 1.000 | 52 | 570/10,598 (5.378%) | 1161/26,064 (4.454%) | 0.0002 |
| 1.200 | 44 | 32/10,598 (0.302%) | 74/26,064 (0.284%) | 0.75 |
| 1.400 | 32 | 26/10,598 (0.245%) | 41/26,064 (0.157%) | 0.08 |
| 1.600 | 23 | 24/10,598 (0.227%) | 38/26,064 (0.146%) | 0.093 |
| 1.800 | 16 | 24/10,598 (0.227%) | 38/26,064 (0.146%) | 0.093 |
| 2.036 | 12 | 0/10,598 (0.000%) | 35/26,064 (0.134%) | 1.3e-05 |
| 2.200 | 10 | 0/10,598 (0.000%) | 27/26,064 (0.104%) | 0.00015 |
| 2.400 | 6 | 0/10,598 (0.000%) | 21/26,064 (0.081%) | 0.0011 |
| 2.500 | 4 | 0/10,598 (0.000%) | 17/26,064 (0.065%) | 0.0053 |
| 2.600 | 2 | 0/10,598 (0.000%) | 0/26,064 (0.000%) | 1 |

**Table 3b.** Period comparison as a function of the Fab-escape cutoff, primary window.

Twenty-six records collected before the boundary and six afterwards carry a substitution scoring between 1.4
and 2.036, dominated by N201S. Substitutions of intermediate score were therefore already circulating.

### 3.4 Robustness to de-duplication, date precision and the cell-entry floor

De-duplication is not generating the primary contrast. Retaining every record, the primary window gives 0 of
17,318 before the boundary against 53 of 45,318 after (p = 6.8 x 10^-8), a stronger association than the
de-duplicated analysis; across the full archive it gives 14 of 20,098 against 53 of 45,318 (p = 0.086), still
null. The window dependence described in Section 3.2 therefore survives removal of the de-duplication rule
while the significance of the primary window does not depend on it.

Date imprecision is not generating it either. Excluding the 29 year-only records dated 2023 leaves 0 of
10,569 against 35 of 26,064 (p = 1.3 x 10^-5); excluding all 538 year-only records leaves 0 of 10,421
against 35 of 26,051 (p = 1.3 x 10^-5); restricting to full-date records only leaves 0 of 10,117 against 35
of 25,802 (p = 1.4 x 10^-5).

The cell-entry floor is likewise not critical: varying it from -2.0 to 0.0 changes the number of qualifying
mutations from 23 to 9 and the carrier count from 36 to 31, with p between 7.6 x 10^-6 and 3.4 x 10^-5.

### 3.5 Reconstructed acquisitions and observed cluster sizes

High-escape residues were reconstructed on 32 independent branches across six site-and-residue combinations
(Figure 4a). These branches are counted on the full 38,925-record archive and so include the historical
carriers; the 35 carriers of Section 3.1 are the post-boundary subset of the primary window.

Twenty-six acquisitions lead to a single sampled carrier. No cluster collected on or after 1 July 2023
exceeded two carriers under this sampling; the largest cluster in the archive is the twelve-carrier 2015
site-209 group (Figure 4b). Branch support separates these sharply: support is undefined for the 26 terminal
acquisitions; of the six internal acquisitions, two are recovered as clades in the maximum-likelihood
topology and well supported (the 2015 site-209 cluster, SH-like support 0.888, and one 2025/26 site-201 pair,
0.982), while the remaining four, all site 208 to D, are not recovered as bipartitions and are therefore
uncertain reconstructions. This includes the branch whose naive descendant count was 122 but which contains
only two carriers. The count of 32 is a reconstruction-dependent estimate conditional on one topology and one
ancestral-state model.

Formal comparison against other F substitutions is uninformative at this sample size (median carrier
descendants 1 versus 1, Mann-Whitney p = 0.133; single-carrier fraction 26/32 versus 6,402/9,178, Fisher
p = 0.181). **Large recent clusters were not observed under this sampling and analysis. This does not
demonstrate absence of onward transmission**, which sparse sampling, de-duplication, the recency of the
carriers and limited phylogenetic resolution could each produce independently.

### 3.6 Subtype consensus and the interpretation of reported frequencies

In this archive, methionine at site 206 is carried by 90.7% of RSV-B records, arginine at site 209 by 84.9%
and asparagine at site 211 by 77.3%, against 0.01%, 0.05% and 0.01% in RSV-A (Figure 3). Their DMS Fab-escape
scores are 0.598, 0.042 and -0.036.

This is concordant with, and does not extend, the trial analysis that first characterised these residues:
I206M:Q209R was reported as highly prevalent in RSV-B and shown to **increase** nirsevimab susceptibility [2],
and the systematic review explicitly distinguishes such common polymorphisms from resistance-associated
variants [1]. We make no claim that earlier investigators used an inappropriate reference. The practical
point for pooled surveillance is narrower: a substitution count is meaningful only relative to a stated
baseline, and frequencies computed against different baselines should not be combined.

The genuine RSV-B variants remain distinguishable on this basis: the RSV-B consensus is asparagine at site
201 and lysine at site 68, so F:N201T and F:K68Q are departures from it.

### 3.7 Concordance with an independently reported variant

F:N201T, reported from Spain in 2025/26 [5], is recovered here without being sought. Within the primary
window there are 5 carriers, 4 Spanish (two in 2025, two in 2026) and 1 South African (2024), all GISAID
deposits absent from the GenBank-only subset; the archive also contains one much older GenBank record
carrying N201T, from Germany in 2002. This is concordance with published observation, not independent
validation, since the cutoff was anchored on N201T itself.

### 3.8 Temporal trend across F

Of 689 F variants carried by at least five records, 105 changed significantly across 2017-2026 against a
Bonferroni threshold of 7.3 x 10^-5: 50 increased and 55 decreased. None was DMS-defined high-escape. The
strongest trends (T12I, K123R, R42K) lie in the signal peptide and other non-epitope regions.

### 3.9 Clesrovimab

Applying the same numerical cutoff to the clesrovimab DMS table, 8 of 24,282 records collected from 2017
onward and before 2025 carried a qualifying substitution (0.033%, 95% CI 0.014-0.065), all RSV-A; no RSV-B
record qualified. Carriers came from France, Spain and Portugal. One further carrier, an Australian record
from 2016, lies outside the primary window and is reported separately in the supplement. The cutoff was
derived for nirsevimab and its appropriateness for a different antibody with a different score scale has not
been established, so this analysis is exploratory and descriptive only. Qualifying sites for the two
antibodies did not overlap (429/443/445/470 versus 68/201/208/209/210) and no record carried both, which does
not establish that cross-resistance cannot occur.

### 3.10 Geographical coverage

The archive is dominated by a small number of countries (Figure 5a). In the primary window the Middle East
contributes 252 records: Qatar 150, Kuwait 79, Jordan 10, Iraq 7 and Egypt 6 (Figure 5b). Records from the
United Arab Emirates, Saudi Arabia and Iran are short partial sequences (median 836, 687 and 321 nucleotides)
spanning the attachment glycoprotein and ending before the F coding sequence, so they cannot contribute.
Under a simple independent-sampling model at the observed post-boundary frequency, 150 records give
approximately an 18% probability of containing at least one carrier, and about 1,200 would be needed for
80%; this is an illustrative calculation, not an assessment of national surveillance performance.

## 4 DISCUSSION

Reading the whole public archive rather than one country at a time yields a result that is mainly a warning
about how such numbers are produced.

The headline contrast is real within its window: among records collected from 2017 onward, high-escape
substitutions appear only from late 2023, across seven countries and thirteen lineages, and the association
survives stratification by country, subtype and database, removal of the de-duplication rule, exclusion of
imprecisely dated records, and variation of the cell-entry floor. What it does not survive is a change to
either of two choices that are seldom reported. Extending the window back to include a single 2015
Argentinian outbreak cluster makes the comparison null. Lowering the functional cutoff makes it null, and
then reverses it. The substitutions are not new - they are in the archive from 2002 and 2014-15 - and
intermediate-score substitutions were circulating throughout.

We therefore do not claim that escape substitutions have increased since prophylaxis began. We claim
something narrower and better supported: that whether they appear to have increased is determined by the
threshold and the window, and that published frequencies which state neither cannot be compared with one
another or pooled. This is consistent with the DMS authors' report that resistant strains have arisen
sporadically but remain rare [3] and with the sporadic emergence on distinct backgrounds described from
Spain [5].

Acquisitions are reconstructed repeatedly across countries and lineages, and no large recent cluster was
observed. We deliberately offer no fitness-cost explanation: the data cannot distinguish a cost from sparse
sampling, recency, de-duplication or phylogenetic uncertainty, and four of the six internal acquisitions are
uncertain reconstructions.

What this study does not show is that RSV-B consensus residues were previously misreported. The trial
analysis that characterised I206M:Q209R identified its prevalence and measured its effect on susceptibility
[2], and the systematic review separates polymorphisms from resistance-associated variants [1]. Our
contribution there is confirmation at archive scale and a procedural recommendation about pooling, not a
correction.

Two methodological results deserve emphasis for future work of this kind. Half of the GISAID records were
re-depositions of sequences already in GenBank, so naive pooling would have inflated the denominator by tens
of thousands; yet the non-overlapping half contained every N201T record in the primary window. Neither
database alone is adequate, and the overlap must be measured. Separately, naive descendant-tip counts from
ancestral reconstruction were misleading here, and acquisition counts should be reported with branch support.

Nothing in these data supports changing prophylaxis policy. Carriage of a scored substitution is not a
confirmed resistant virus, the measurements are pseudovirus-based, and the overwhelming majority of deposited
records carry no qualifying substitution.

### 4.1 Limitations

This study has several limitations. The public archive is a convenience sample dominated by a small number of
countries, so the figures reported here describe de-duplicated archive records and are not population
prevalence. Public metadata does not record prophylaxis exposure, national implementation dates differ while
a single global boundary of 1 July 2023 was applied, and later sequencing effort was markedly greater, so the
period comparison is observational and exploratory; stratification by country reduces but does not remove
this concern, and the choice of first included year changes the conclusion outright. Classifications are DMS
scores rather than measured phenotypes, no virus here was tested functionally, the scan was performed on an
RSV-A background, and the high-escape category excludes known resistance-associated variants such as K68Q;
the clesrovimab cutoff is unvalidated for that antibody. Collapsing records identical in F sequence, country
and collection date may remove genuinely distinct infections, although repeating the analysis without it
strengthened rather than weakened the primary association. A single sampled carrier does not establish
absence of transmission, the count of 32 acquisitions is conditional on one topology and one ancestral-state
model, and four of six internal acquisitions are uncertain. Clinical severity, prophylaxis failure rates,
within-host minor variants and antibody exposure history are not recoverable from consensus deposits and were
not assessed.

## 5 CONCLUSIONS

Among public RSV records collected from 2017 onward, DMS-defined high-escape substitutions to nirsevimab were
detected only from late 2023 and remained below 0.25% of records collected on or after 1 July 2023, arising
as repeated independent acquisitions with no observed cluster larger than two sequences. This contrast does
not hold across the full archive, where the same substitutions are present from 2002 and 2014-15 and the
period comparison is null, and it does not hold at more permissive functional cutoffs, where it is null or
reversed. Reported RSV resistance frequencies should therefore always be accompanied by the classification
threshold, the reference baseline and the collection-year span from which they were derived, and
archive-based estimates should be described as properties of deposited sequences rather than of circulating
virus populations.

## ACKNOWLEDGEMENTS

We gratefully acknowledge all data contributors, namely the authors and their originating laboratories
responsible for obtaining the specimens, and their submitting laboratories for generating the genetic
sequence and metadata and sharing via the GISAID Initiative, on which this research is based. A GISAID
EPI_SET acknowledgement identifier listing every accession used will be registered and cited in the final
version. We also acknowledge the submitters of the GenBank records analysed here.

## CONFLICT OF INTEREST STATEMENT

[To be completed by the authors.]

## AUTHOR CONTRIBUTIONS

[To be completed by the authors, following CRediT taxonomy.]

## ETHICS STATEMENT

This study used only publicly deposited viral genome sequences and their associated metadata. No human
subjects, clinical specimens or identifiable patient information were involved, and no ethical approval was
required.

## DATA AVAILABILITY STATEMENT

Deposited at https://github.com/Siniyaa/Infectious_Disease: accession manifests for every analysis
population, with per-record date-precision flags and carrier calls; the complete de-duplication group
mapping (65,416 member rows across 38,925 groups, by opaque group identifier, without sequence data); the
maximum-likelihood trees, annotated TreeTime output and branch-mutation tables; every derived table
underlying the figures; and the analysis workflow. The deposited workflow covers cohort assembly, variant
calling, the carriage, threshold-sweep and window-sweep analyses, the trend scan and the clesrovimab
analysis; the phylogenetic stage is documented as the exact commands used rather than as a tested function,
and figure generation is not included. In accordance with the GISAID Database Access Agreement, sequence data
are not redistributed: GISAID-derived records are identified by EPI_ISL accession and must be obtained from
https://gisaid.org, and GenBank records by accession. DMS scores are available at
https://github.com/dms-vep/RSV_Long_F_DMS. Retrieval date for all sequence data was 2 November 2026.

## REFERENCES

1. Berikopoulou MM, et al. Systematic review of the mutations in the active antigenic site O of the prefusion F protein of the respiratory syncytial virus (RSV) following the implementation of monoclonal antibody prophylaxis. *Vaccine*. 2026;91:129069. doi:10.1016/j.vaccine.2026.129069
2. [Authors]. Molecular and phenotypic characteristics of RSV infections in infants during two nirsevimab randomized clinical trials. *Nat Commun*. 2023;14:4137. doi:10.1038/s41467-023-40057-8
3. Simonich CAL, et al. Mutational constraints on RSV F and its neutralization by antibodies. *Nature*. 2026. doi:10.1038/s41586-026-11030-4
4. [Authors]. Real-world emergence of nirsevimab resistance in breakthrough infections with respiratory syncytial virus-B: a multicentre observational study in France. *Lancet Microbe*. 2026. doi:10.1016/j.lanmic.2026.101353
5. [Authors]. Detection of nirsevimab-resistant RSV-B variants in children carrying the F:N201T substitution through genomic surveillance, Spain, 2025/26 season. *Euro Surveill*. 2026;31(35). doi:10.2807/1560-7917.ES.2026.31.35.2600690
6. [Authors]. Genomic surveillance of respiratory syncytial virus during 2023/2024 nirsevimab prophylaxis, Eastern Spain, early results. *Clin Microbiol Infect*. 2026. doi:10.1016/j.cmi.2026.04.003
7. [Authors]. Detection of a nirsevimab-resistant RSV-B variant (F:K68Q) in an adult with severe infection. *Infect Dis Ther*. 2026. doi:10.1007/s40121-026-01442-0
8. [Authors]. [RSV lineage nomenclature - consortium paper defining the A.D/B.D system. To be completed by the authors; lineage assignments follow the Nextclade RSV datasets.]
9. Li Y, et al. Global, regional, and national disease burden estimates of acute lower respiratory infections due to respiratory syncytial virus in children younger than 5 years in 2019: a systematic analysis. *Lancet*. 2022;399(10340):2047-2064. PMID:35598608
10. [Authors]. Global, regional, and national disease burden estimates of acute lower respiratory infections due to respiratory syncytial virus in young children in 2015. *Lancet*. 2017. PMID:28689664
11. [Authors]. Global disease burden of and risk factors for acute lower respiratory infections caused by respiratory syncytial virus in preterm infants and young children in 2019. *Lancet*. 2024. PMID:38367641
12. Aksamentov I, Roemer C, Hodcroft EB, Neher RA. Nextclade: clade assignment, mutation calling and quality control for viral genomes. *J Open Source Softw*. 2021;6(67):3773. doi:10.21105/joss.03773
13. Pineiro VC, Marco-Sola S, Moreto M, Espinosa A. Very Fast Tree: speeding up the estimation of phylogenies for large alignments through parallelization and vectorization strategies. *Bioinformatics*. 2020;36(17):4658-4659. PMID:32573652
14. Sagulenko P, Puller V, Neher RA. TreeTime: maximum-likelihood phylodynamic analysis. *Virus Evol*. 2018;4(1):vex042. PMID:29340210

## FIGURE LEGENDS

**FIGURE 1** Records carrying a DMS-defined high-escape substitution, by subtype and period (a) and by
collection year (b), primary window from 2017. Intervals are Clopper-Pearson; zero counts are shown as upper
bounds. Panel b aggregates by calendar year, so the 2023 column spans both sides of the 1 July 2023 boundary;
all four carriers collected in 2023 were collected in November, after that date.

**FIGURE 2** The period comparison depends on two analyst choices. (a) Carriage in each period as a function
of the Fab-escape cutoff. (b) The period-comparison p value against the cutoff; open circles mark cutoffs at
which carriage is higher before the boundary. (c) The p value against the first collection year included;
open circles mark windows containing pre-boundary carriers. Significance appears only when the window
excludes the 2015 Argentinian cluster.

**FIGURE 3** Named substitutions. (a) Fab-escape score with the cutoff marked; orange indicates residues that
are the RSV-B consensus. (b) Frequency of the same residues in each subtype.

**FIGURE 4** Reconstructed acquisitions across the full 38,925-record archive. (a) Independent acquisition
branches per site and acquired residue, named by reconstructed ancestral state rather than by consensus (see
Methods 2.4). (b) Sequences in each acquisition's clade carrying the residue, by branch-support status. The
twelve-carrier cluster is the 2015 Argentinian RSV-B group.

**FIGURE 5** Sequencing coverage. (a) The twelve largest national contributions. (b) The Middle East.

## TABLES

Tables 1, 2, 3a and 3b appear in the main text and count as three display items.
