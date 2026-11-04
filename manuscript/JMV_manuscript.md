# TITLE PAGE

**Title.** Threshold and time-window choices determine whether nirsevimab escape substitutions appear to have increased in public respiratory syncytial virus genomes

**Running head.** RSV F escape substitutions in public genomes (44 characters)

**Authors.** [To be completed by the authors, with ORCIDs.]

**Affiliations.** [To be completed by the authors.]

**Corresponding author.** [Name, postal address, email, telephone - to be completed.]

**Keywords.** respiratory syncytial virus; nirsevimab; resistance-associated substitution; genomic surveillance; fusion protein

**Word counts.** Abstract 198 words (limit 200). Text 3,999 words (limit 4,000). References 17 (limit 50). Display items 8: Figures 1-4 and Tables 1-4 (limit 8). Text counted as Sections 1-5 excluding
headings, table content and table titles; abstract, references and figure legends excluded.

**Funding.** [To be completed by the authors. If the work was unfunded, state that no specific funding was received.]

**Conflict of interest.** [To be completed by the authors.]

**Declaration of generative AI use.** Claude Opus 5 (Anthropic) was used substantially throughout this
work: to write and debug the analysis code, to run the analyses, to draft and revise the manuscript, and to
propose and carry out several of the sensitivity analyses reported here. The authors defined the research
question, directed the analysis, reviewed the code and outputs, verified every reference against its
primary source, and take full responsibility for the content, the accuracy of the results and the
conclusions. The analysis workflow, the manifests needed to reproduce the cohort and a log of the executed
analyses are deposited so that readers can check the results independently.

---

## ABSTRACT

Reported frequencies of nirsevimab resistance-associated substitutions in respiratory syncytial virus (RSV) differ between studies using different references, thresholds and time spans. We combined 25,384 GenBank with 44,275 eligible GISAID EpiRSV records (69,659 total), processed both uniformly, called fusion (F) protein variants against each subtype's own consensus, and classified them using published deep mutational scanning (DMS) scores. After de-duplication 38,925 records remained. The central finding is that archive-derived escape frequencies are governed by two analyst choices that are rarely reported. A score-based definition anchored on F:N201T classifies 5 of 17 substitutions reported in the literature as resistance-associated or as site Ø polymorphisms; two are excluded by the cell-entry filter at any Fab cutoff, and capturing the phenotypically confirmed F:K68Q requires a cutoff at which at least 4.5% of all records qualify. Within a 2017-onward window the same definition gives no carrier before 1 July 2023 against 35 of 26,064 after (0.134%, 95% CI 0.094-0.187; Fisher p = 1.3e-5), but across the full archive the difference is not significant (p = 0.44), and at a permissive cutoff it reverses. Temporal rooting confirms 32 candidate acquisition branches. DMS scores derive from an RSV-A background whereas 26 of 35 carriers are RSV-B.

**KEYWORDS:** respiratory syncytial virus; nirsevimab; resistance-associated substitution; genomic surveillance; fusion protein

---

## 1 INTRODUCTION

RSV causes a large burden of lower respiratory tract infection in infants worldwide [1-3]. Long-acting
monoclonal antibodies against the prefusion F protein are now used for infant prophylaxis; nirsevimab binds
antigenic site Ø and clesrovimab a separate epitope. In the Phase 2b and MELODY trials more than 99% of
isolates retained susceptibility to nirsevimab, and binding-site substitutions reducing it were found in two
participants [4].

The binding site has already been examined at archive scale: Wilkins and colleagues analysed 3,626 GenBank F
sequences from 1956-2021 with 5,675 from three prospective surveillance studies and concluded that the site
was highly conserved and escape variants rare and not increasing [5]. We revisit that question on an archive roughly ten times larger that
now spans the introduction of prophylaxis, using a classification unavailable in 2023.

Since prophylaxis became widespread, individual groups have reported F substitutions in circulating virus.
A 2026 systematic review pooled seven studies and 2,156 samples, reporting limited variability in RSV-A with
K65R most common and higher frequencies in RSV-B, while distinguishing polymorphisms that retain
susceptibility from resistance-associated variants [6]. Primary reports include a national multicentre study of 545 genomes
from the 2023-24 French season, in which two of 24 RSV-B breakthrough infections carried
resistance-associated substitutions confirmed by fusion-inhibition assay [7], further breakthrough RSV-B
infections in France [8], three children in Spain carrying F:N201T with recombinant expression confirming
reduced recognition [9], 68 isolates from Eastern Spain [10], and an adult case carrying F:K68Q [11]. These
use different reference sequences, definitions and observation periods, so their frequencies are not
directly comparable.

A deep mutational scan (DMS) of RSV F has since measured how nearly all F mutations affect cell entry and
neutralisation by both antibodies, finding resistant strains rare and bivalent IgG binding buffering escape,
so Fab potency is the more sensitive readout [12]. Applying that classification to the combined archive, we
ask not what the resistance frequency is - archive data cannot support such an estimate - but how far any
estimate is determined by two choices an analyst must make and rarely reports: where the threshold is set
and which collection years are included. We then ask whether any threshold recovers the substitutions
actually reported as resistance-associated.

## 2 MATERIALS AND METHODS

### 2.1 Sequence assembly

GenBank contributed 25,384 records for human orthopneumovirus (taxon 11250), 13-16 kb. A GISAID EpiRSV
export contributed 56,856 unique records, of which 44,275 passed filtering for human host, length and a
resolvable collection date. GISAID holdings begin in 2020, so earlier coverage rests on GenBank alone;
retrieval date 2 November 2026. The combined 69,659 records were assigned to subtype with the Nextclade
minimizer index (RSV-A 37,290, RSV-B 32,365; four excluded) and aligned to the corresponding reference
dataset [13], supplying reference-anchored F translations and lineage assignments [14]. Alignment-based extraction was used rather than deposited CDS annotation,
present in only 60-65% of GenBank genome records; records with F coverage of at least 95% were retained,
leaving 65,416 (Table 1).

| Stage | GenBank | GISAID | Total |
|---|---|---|---|
| GenBank records retrieved (taxon 11250, 13-16 kb) | 25,384 | - | 25,384 |
| GISAID EpiRSV records retrieved (unique) | - | 56,856 | 56,856 |
| GISAID records passing host, length and date filters | - | 44,275 | 44,275 |
| Combined input to subtype assignment | 25,384 | 44,275 | 69,659 |
| F coverage >=95% and a resolvable collection date | 23,902 | 41,514 | 65,416 |
| Removed: non-representative in a mixed-database group | 3,303 | 16,973 | 20,276 |
| Removed: non-representative in a single-database group | 1,519 | 4,696 | 6,215 |
| Retained as group representative (analysis set) | 19,080 | 19,845 | 38,925 |
| Primary analysis window, 2017 onward | 16,817 | 19,845 | 36,662 |

**Table 1.** Cohort assembly and de-duplication, by database.

### 2.2 Collection dates and their precision

Deposited dates vary in precision. Partial dates were expanded to the first day of the stated month or year
and flagged; both the flag and the date as deposited are in the manifest. The analysis set holds 37,804
full dates, 583 month-only and 538 year-only; 190 year-only records fall in the primary window, 29 dated
2023 and assigned to the earlier period. None is a carrier (Section 3.5).

### 2.3 De-duplication across databases

Records identical in F sequence, country and collection date were collapsed to one **across both databases**; a
GenBank record was retained in all 12,325 mixed groups. Of 41,514 GISAID records passing QC, 21,669 (52.2%)
were excluded - 16,973 matching a GenBank record, 4,696 from GISAID-only groups - leaving 19,845. Of 23,902
GenBank records, 4,822 were excluded (3,303 in mixed groups, 1,519 in GenBank-only groups), leaving 19,080.
Total removals are 26,491 and the analysis set 38,925 (Table 1). Matching on these fields is consistent with the same specimen deposited
twice but does not demonstrate it; group membership is deposited and the comparison repeated without
de-duplication (Section 3.5). As a convenience sample these are **de-duplicated archive
records**, not a population denominator. The primary window holds 36,662 records, 10,598 before and 26,064
on or after 1 July 2023.

### 2.4 Variant calling and functional classification

Variants were called against each subtype's own consensus, computed from the analysis set, because the two
consensuses differ at 59 of 574 F residues. Observed residues were joined to the DMS tables [12] on site and
mutant residue.

A residue was classified **DMS-defined high-escape** when its Fab-escape score was at least 2.036 with cell
entry at or above -0.5 (12 nirsevimab and 6 clesrovimab mutations of 9,812 scored), anchored on F:N201T, for
which reduced recognition has been shown by recombinant expression [9]. The anchoring is circular with
respect to N201T, and Section 3.3 quantifies how poorly the category recovers substitutions reported
elsewhere. All classifications are predicted; no virus was tested functionally.

The twelve nirsevimab mutations fall at five F positions (68, 201, 208, 209, 210); 99.69% of primary-window
records have all five callable, so the coverage filter is not diluting the denominator where it matters.

The DMS was performed on an RSV-A background while 26 of the 35 primary-window carriers are RSV-B. The two
RSV-B substitutions contributing most carriers sit at sites where the RSV-B consensus matches the scan's
wildtype (N208D: wildtype N, RSV-B consensus N; K68I: wildtype K, RSV-B consensus K). Matching the wildtype
residue does not establish that a score transfers unchanged across backgrounds, and the DMS study itself
reports background-dependent effects at position 201 and for K68Q on RSV-B [12]; this is a limitation of the
endpoint, not only of its interpretation.

**Two naming conventions are used and should not be conflated.** Carriage is reported relative to each
subtype's consensus, so the RSV-B departure at site 209 is R209E. Acquisition branches are named by the
ancestral state reconstructed at that branch, which may differ; the same RSV-B event is K209E because the
reconstructed ancestor carried lysine. Acquisitions are reported as site and acquired residue.

### 2.5 Statistics and phylogenetics

Proportions and intervals are Clopper-Pearson throughout, including zero-count upper bounds. Periods were
compared with Fisher's exact test at a fixed boundary of 1 July 2023. Because several strata contain no
pre-boundary events, stratified inference uses an **exact conditional test**, the convolution of per-stratum
hypergeometric distributions conditional on both margins; the continuity-corrected Cochran-Mantel-Haenszel
statistic is reported as the conservative alternative. Temporal trend
used the Cochran-Armitage test, Bonferroni-corrected across variants carried by at least five records.

Two sensitivity analyses are primary: the comparison was repeated across Fab-escape cutoffs from 1.0 to 2.6
and across first-included years through 2023. Three further analyses appear in
Section 3.5 (de-duplication, date precision, cell-entry floor); the trend, acquisition and clesrovimab
analyses were run at the primary cutoff only. The clesrovimab analysis uses a pre-licensure window, 2017 to end-2024;
both that denominator and the full window are reported in Section 3.9.

Maximum-likelihood F phylogenies were built per subtype from the aligned F coding sequences with
VeryFastTree under GTR+gamma [15] (20,767 and 18,158 tips). Amino-acid ancestral states were reconstructed
on those topologies with TreeTime [16] under an inferred GTR model, from the translated peptide alignment
over the same tips. VeryFastTree emits an unrooted tree, so the trees were rooted by **least-squares temporal rooting** in
TreeTime. Two GenBank records dated before the first isolation of RSV in 1956 (PX851455.1,
1941-01-05; PX851473.1, 1951-07-13) are impossible and were excluded from the regression; both are flagged
in the deposited manifest. The estimates are RSV-A 1.53 x 10^-3 substitutions per site per year
(root-to-tip R^2 = 0.43) and RSV-B 2.52 x 10^-3 (R^2 = 0.60). **The regression intercepts are not dates of
origin.** They fall in 1958 and 1987, postdating 3 and 23 sampled tips respectively, so they are not
credible common-ancestor dates: 94.2% of the analysis set was collected from 2017 onward and, once those
two records are excluded, only 162 of the 164 pre-2000 records in the deposited manifest remain, leaving
the extrapolation poorly constrained. Temporal rooting is used solely to place the root for ancestral-state
reconstruction, and because direction of change is undefined without a root the acquisition count is
reported across six further rootings (Section 3.6). Branch support was taken from the maximum-likelihood topology by matching nodes on descendant tip sets and
is undefined for terminal branches. Trees and TreeTime output are deposited.

## 3 RESULTS

### 3.1 Carriage in the primary window

Among 36,662 records collected from 2017 onward, none of the 10,598 collected before 1 July 2023 carried a
DMS-defined high-escape substitution, against 35 of 26,064 collected on or after that date (Table 2,
Figure 1). This is absence of detection, not demonstrated biological absence.

| Subtype | Period | Carriers / n | Carriage (%) | 95% CI (%) |
|---|---|---|---|---|
| RSV-A | Before 1 Jul 2023 | 0/5,584 | 0.0 | 0.000-0.066 |
| RSV-A | On/after 1 Jul 2023 | 9/14,013 | 0.064 | 0.029-0.122 |
| RSV-B | Before 1 Jul 2023 | 0/5,014 | 0.0 | 0.000-0.074 |
| RSV-B | On/after 1 Jul 2023 | 26/12,051 | 0.216 | 0.141-0.316 |
| Both | Before 1 Jul 2023 | 0/10,598 | 0.0 | 0.000-0.035 |
| Both | On/after 1 Jul 2023 | 35/26,064 | 0.134 | 0.094-0.187 |

**Table 2.** Carriage among de-duplicated archive records collected from 2017 onward, split at the fixed
calendar boundary of 1 July 2023. National prophylaxis rollout dates were not used to assign periods.
Intervals are Clopper-Pearson; zero counts are shown as exact upper bounds.

Pooled, Fisher p = 1.3 x 10^-5. By exact conditional test, stratified by subtype p = 5.7 x 10^-6 (2
informative strata), by country 4.3 x 10^-4 (6), by country and subtype 4.3 x 10^-4 (9), and by country,
subtype and database 8.0 x 10^-4 (12); the conservative CMH gives 3.0 x 10^-4, 0.0060, 0.0059 and 0.0082.
The 35 carriers span 7 countries and 13 lineages and derive from both databases (20 GISAID, 15 GenBank).
Database and period are correlated but not collinear: GISAID supplies 36.4% of pre-boundary and 61.3% of
post-boundary records, so both contribute substantially to both periods. Because prophylaxis exposure is
unrecorded, implementation dates differ and sequencing effort rose sharply, this association must not be
read as evidence that prophylaxis caused the difference.

### 3.2 The comparison depends on which collection years are included

Extending the window backwards adds 13 historical carriers, twelve of which fall in one 2014-15 acquisition
clade, and the difference is no longer statistically significant (Table 3 panel A, Figure 2c): across the
full archive, 13 of 12,861 records predating the boundary carry a high-escape substitution (0.101%) against
35 of 26,064 afterwards (0.134%), Fisher p = 0.44.

The transition is abrupt. The difference reaches significance for start years 2016
through 2022 and for none earlier; at a start year of 2023 the pre-boundary arm falls to 1,675 records and
significance is lost again through loss of power (p = 0.27). The sweep is not monotone between 2010 and 2015
because both numerator and denominator move as historical carriers and their contemporaries enter the
window. Twelve of the 13 historical carriers are RSV-B records carrying glutamate at site 209 - ten from
Argentina in 2015, two from Viet Nam in 2014 - and the thirteenth is a German RSV-B record from 2002
carrying N201T. The entire contrast therefore turns on whether one 2014-15 acquisition clade, sampled in
Argentina and Viet Nam, is inside or outside the window. We describe it as a clade rather than an outbreak:
the grouping is phylogenetic and no epidemiological linkage between these specimens has been established.

| Panel | Value | Qualifying mutations | Before 1 Jul 2023 | On/after 1 Jul 2023 | Fisher p |
|---|---|---|---|---|---|
| A. First collection year | all years | 12 | 13/12,861 (0.101%) | 35/26,064 (0.134%) | 0.44 |
| A. First collection year | 2000 | 12 | 13/12,697 (0.102%) | 35/26,064 (0.134%) | 0.45 |
| A. First collection year | 2005 | 12 | 12/12,643 (0.095%) | 35/26,064 (0.134%) | 0.35 |
| A. First collection year | 2010 | 12 | 12/12,527 (0.096%) | 35/26,064 (0.134%) | 0.35 |
| A. First collection year | 2014 | 12 | 12/11,592 (0.104%) | 35/26,064 (0.134%) | 0.53 |
| A. First collection year | 2015 | 12 | 10/11,338 (0.088%) | 35/26,064 (0.134%) | 0.26 |
| A. First collection year | 2016 | 12 | 0/11,040 (0.000%) | 35/26,064 (0.134%) | 6.7e-06 |
| A. First collection year | 2017 | 12 | 0/10,598 (0.000%) | 35/26,064 (0.134%) | 1.3e-05 |
| A. First collection year | 2018 | 12 | 0/10,055 (0.000%) | 35/26,064 (0.134%) | 1.4e-05 |
| A. First collection year | 2019 | 12 | 0/9,088 (0.000%) | 35/26,064 (0.134%) | 4.9e-05 |
| A. First collection year | 2020 | 12 | 0/7,742 (0.000%) | 35/26,064 (0.134%) | 0.00017 |
| A. First collection year | 2021 | 12 | 0/6,809 (0.000%) | 35/26,064 (0.134%) | 0.00051 |
| A. First collection year | 2022 | 12 | 0/5,584 (0.000%) | 35/26,064 (0.134%) | 0.0027 |
| A. First collection year | 2023 | 12 | 0/1,675 (0.000%) | 35/26,064 (0.134%) | 0.27 |
| B. Fab-escape cutoff | 1.000 | 52 | 570/10,598 (5.378%) | 1161/26,064 (4.454%) | 0.0002 |
| B. Fab-escape cutoff | 1.200 | 44 | 32/10,598 (0.302%) | 74/26,064 (0.284%) | 0.75 |
| B. Fab-escape cutoff | 1.400 | 32 | 26/10,598 (0.245%) | 41/26,064 (0.157%) | 0.08 |
| B. Fab-escape cutoff | 1.600 | 23 | 24/10,598 (0.227%) | 38/26,064 (0.146%) | 0.093 |
| B. Fab-escape cutoff | 1.800 | 16 | 24/10,598 (0.227%) | 38/26,064 (0.146%) | 0.093 |
| B. Fab-escape cutoff | 2.036 | 12 | 0/10,598 (0.000%) | 35/26,064 (0.134%) | 1.3e-05 |
| B. Fab-escape cutoff | 2.200 | 10 | 0/10,598 (0.000%) | 27/26,064 (0.104%) | 0.00015 |
| B. Fab-escape cutoff | 2.400 | 6 | 0/10,598 (0.000%) | 21/26,064 (0.081%) | 0.0011 |
| B. Fab-escape cutoff | 2.500 | 4 | 0/10,598 (0.000%) | 17/26,064 (0.065%) | 0.0053 |
| B. Fab-escape cutoff | 2.600 | 2 | 0/10,598 (0.000%) | 0/26,064 (0.000%) | 1.0 |

**Table 3.** Sensitivity of the period comparison to two analyst choices. Panel A varies the first
collection year included at a fixed cutoff of 2.036; panel B varies the cutoff within the primary window.
Periods are split at 1 July 2023.

Pre-2017 records differ from later ones in ways that motivate a modern-era restriction independently of the
result: 25 countries against 82, no GISAID deposits against 54.1%, and they predate the lineage
nomenclature used here. These are not strong enough to carry the inference alone, so we report both windows
and treat neither as definitive. **Within the primary window these substitutions were not detected before
mid-2023; across the full archive they are not new.**

### 3.3 No threshold recovers the substitutions reported as resistance-associated

The classification is anchored on a single variant, and it is worth asking what it does to the others. Of 17
substitutions reported as resistance-associated or as site Ø polymorphisms in references 4 and 6-11, five
meet the criteria (Table 4).

| Substitution | Reported in | Fab escape | IgG escape | Cell entry | Meets cutoff (Fab >=2.036) | Meets entry floor (>=-0.5) | Classified high-escape |
|---|---|---|---|---|---|---|---|
| N208D | [7], [8] | 2.561 | 1.218 | 0.192 | yes | yes | yes |
| K68I | [8] | 2.469 | 0.363 | -0.245 | yes | yes | yes |
| K209E | [8] | 2.368 | 0.253 | 0.322 | yes | yes | yes |
| N208T | [10] | 2.178 | 0.405 | 0.107 | yes | yes | yes |
| N201T | [9] | 2.036 | 0.244 | 0.258 | yes | yes | yes |
| N201S | [6] | 1.8 | 0.315 | -0.095 | no | yes | no |
| I64T | [6] | 1.619 | -0.043 | -0.691 | no | no | no |
| D73N | [6] | 1.394 | 0.636 | -0.071 | no | yes | no |
| R209L | [6] | 1.379 | 0.099 | -0.849 | no | no | no |
| K68E | [6] | 1.231 | 0.356 | -0.097 | no | yes | no |
| R209Q | [6] | 1.154 | 0.439 | 0.568 | no | yes | no |
| I206M | [4] | 0.598 | 0.416 | -0.275 | no | yes | no |
| K68Q | [11] | 0.572 | -0.068 | 0.915 | no | yes | no |
| K65R | [6], [7] | 0.17 | -0.162 | -0.421 | no | yes | no |
| K209R | [4] | 0.042 | -0.25 | 0.274 | no | yes | no |
| S211N | [6] | -0.036 | 0.088 | -0.25 | no | yes | no |
| I64M | [7] | -1.178 | -0.149 | -1.154 | no | no | no |

**Table 4.** Substitutions reported in the cited literature, their DMS scores and their classification under
the criteria used here. Scores are from the pinned release of the nirsevimab DMS summary [12].

Three features matter more than the count. F:I64T, F:R209L and F:I64M are excluded by the cell-entry filter
(-0.691, -0.849, -1.154) rather than the Fab cutoff, so **no Fab threshold combined with this entry floor
classifies them**. F:I64M matters most: reported with F:K65R as a pair whose high-level resistance was
confirmed by fusion-inhibition assay [7], it scores -1.178 for Fab escape, the lowest at that site, while
F:K65R scores 0.170. Neither member of a phenotypically confirmed escape pair is recoverable by any
single-substitution rule; and because the DMS scores substitutions singly, an escape phenotype requiring a
combination lies outside what this or any similar screen can represent. And F:K68Q - with a published severe adult case [11] and reduced IgG neutralisation on an RSV-B
background [12] - scores 0.572; capturing it requires a cutoff of 0.572 or lower, at which 95 of 9,812
scored mutations qualify. Carriage at a cutoff of 1.0, far above that, is already 4.45% and 5.38% of the two
periods (Table 3 panel B), so at 0.572 at least 4.5% of all records would be carriers. A definition that
captures the confirmed variants is not a surveillance signal but a description of ordinary F diversity.

This, rather than threshold sensitivity alone, is the study's principal result: within this DMS, no single
score-based rule applied to one substitution at a time separates those shown to matter from those not.

### 3.4 The comparison also depends on where the threshold is set

Repeating the comparison across cutoffs shows three regimes (Table 3 panel B, Figure 2a,b). Above 2.0 the
pre-boundary count is zero and the difference is significant to 2.5, beyond which no record qualifies. Between 1.2 and 1.8 the difference is not statistically significant and the point estimate
is higher before the boundary. At 1.0 the difference is significant in the reverse direction (5.38% before
versus 4.45% on or after). Changing the cutoff does not merely change the power of one test: it changes
which substitutions are classified, and therefore the endpoint being compared. Twenty-six records before the
boundary and six after carry a substitution scoring between 1.4 and 2.036, dominated by N201S.

### 3.5 Robustness to de-duplication, date precision and the cell-entry floor

Neither de-duplication nor date imprecision generates the primary contrast. Retaining every record, the
primary window gives 0 of 17,318 against 53 of 45,318 (0% against 0.117%) and the full archive 14 of 20,098
against 53 of 45,318 (0.070% against 0.117%, p = 0.086, marginal); the fractions are close to the
de-duplicated estimates in both windows, and the smaller p value without de-duplication is not stronger
evidence because matching records are not independent. Excluding the 29 year-only 2023 records, all 190
year-only records in the window, or every partial date each leaves p between 1.3 and 1.4 x 10^-5. Varying
the cell-entry floor from -2.0 to 0.0 changes the qualifying set from 23 to 9 mutations and p from
7.6 x 10^-6 to 3.4 x 10^-5 (Table S10).

### 3.6 Reconstructed acquisitions are robust to rooting

The acquisition count does not depend on rooting. High-escape residues are assigned to 32 candidate
acquisition branches across six site-and-residue combinations (Figure 4a) under midpoint rooting, three
random terminal-edge rootings, the unrooted tree as produced and least-squares temporal rooting, with one
reversion in each case; only an adversarial root inside the largest carrier clade gives 31 and two
reversions (Table S11). Total state changes are 33 throughout, as parsimony requires. Because the result is
invariant across every rooting tested it does not rest on the temporal root, whose intercept is unreliable
(Methods 2.5).

These branches are counted on the full archive and include the historical carriers; the 35 carriers of
Section 3.1 are the post-boundary subset. Twenty-six acquisitions have a single sampled carrier, and no
cluster collected on or after 1 July 2023 exceeded two; the largest in the archive is a twelve-carrier
site-209 clade, ten records from Argentina in 2015 and two from Viet Nam in 2014 (Figure 4b). Support is
undefined for the 26 terminal acquisitions; of the six internal ones, two are well-supported clades (0.888
and 0.982) and four, all site 208 to D, are not recovered as bipartitions. Comparison against other F
substitutions is uninformative at this sample size (p = 0.133 and 0.181). **Large recent clusters were not observed under
this sampling. This does not demonstrate absence of onward transmission**, which sparse sampling,
de-duplication and the recency of the carriers could each produce.

### 3.7 Subtype consensus and the interpretation of reported frequencies

Methionine at site 206 is carried by 90.7% of RSV-B records, arginine at 209 by 84.9% and
asparagine at 211 by 77.3%, against 0.01%, 0.05% and 0.01% in RSV-A (Figure 3); their Fab-escape scores are
0.598, 0.042 and -0.036. This is concordant with, and does not extend, the trial analysis that first
characterised these residues: I206M:Q209R was highly prevalent in RSV-B and **increases** nirsevimab
susceptibility [4], and the systematic review distinguishes such polymorphisms from resistance-associated
variants [6]. We make no claim that earlier investigators used an inappropriate reference. The point is
narrower: a substitution count is meaningful only against a stated baseline, and counts from different
baselines should not be combined. Genuine RSV-B variants remain distinguishable: the consensus is
asparagine at 201 and lysine at 68, so F:N201T and F:K68Q are departures from it.

F:N201T, reported from Spain in 2025/26 [9], is recovered without being sought: 5 carriers in the primary
window, 4 Spanish and 1 South African, all GISAID deposits absent from the GenBank-only subset, plus an
older German record from 2002. This is concordance, not independent validation, since the cutoff was
anchored on N201T.

### 3.8 Temporal trend across F reflects lineage turnover

Of 689 F variants carried by at least five records, 105 changed significantly against a Bonferroni threshold
of 7.3 x 10^-5: 50 increased, 55 decreased, none high-escape. The five strongest are all decreasing RSV-B
variants - N211S, N190S, P389S, M206I and R191K - with p below 10^-300.

Nine significant trends fall at site Ø positions and all nine decrease: N211S (rank 1), M206I (4), K68Q
(10), R209Q (18), N197D (40), R209K (51), N201S (52), K68R (57) and K68N (78). Two are the RSV-B majority
residues of Section 3.7, declining as B.D.4 lineages are replaced by B.D.E.1. These trends are not evidence about
selection: per-year denominators rise roughly thirty-fold (RSV-A 165 to 4,740; RSV-B 378 to 4,081), and the
apparent decline of K68Q is one historical cluster leaving the archive, 58 of its 60 occurrences falling in
2017. A Cochran-Armitage statistic across denominators of that shape measures which lineages were
sequenced, not which variants were selected. The scan is reported because no high-escape substitution
increases.

### 3.9 Clesrovimab

Applying the same cutoff to the clesrovimab DMS table, 8 records carried a qualifying substitution, all
RSV-A, from France, Spain and Portugal, the latest on 5 January 2024; no RSV-B record qualified. Against the
pre-licensure denominator this is 8 of 24,282 (0.033%, 95% CI 0.014-0.065); against the whole primary window
8 of 36,662 (0.022%, 0.009-0.043). Both are reported because the denominator changes the estimate by half,
which is this paper's point. One further carrier, an Australian record from 2016, lies outside the window
and is in the supplement. The cutoff was derived for nirsevimab, so this is exploratory only. Qualifying
sites did not overlap (429/443/445/470 versus 68/201/208/209/210) and no record carried both, which does not
establish that cross-resistance cannot occur.

## 4 DISCUSSION

The central problem is not that a threshold is hard to choose but that no choice works. Of 17 reported
substitutions this definition classifies five; three are excluded by the cell-entry filter at any Fab
cutoff, including one member of a phenotypically confirmed escape pair; and capturing the one with a
published clinical case requires a cutoff at which roughly one record in twenty is a carrier. Such a definition can be sensitive or specific but not both, so frequencies resting on one
are not comparable across studies unless the rule is stated in full.

The period comparison makes the same point twice. Within a 2017-onward window the contrast survives
stratification by country, subtype and database, removal of de-duplication, exclusion of imprecisely dated
records and variation of the cell-entry floor - but not a change to either choice: extending the
window to include one 2014-15 clade removes significance, and lowering the cutoff removes and then reverses it while
changing which substitutions the endpoint contains. The substitutions are not new; they are in the archive from 2002 and
2014-15. Whether they appear to have increased is determined by the threshold and the window.

Candidate acquisitions recur across countries and lineages and the count of 32 is stable under every
rooting tested, so the recurrence is not an artefact of root placement. We offer no fitness-cost
explanation: the data cannot distinguish a cost from sparse sampling, recency or phylogenetic uncertainty.

Our full-archive result is concordant with the prior archive-scale analysis: Wilkins and colleagues found
escape variants rare and not increasing across 1956-2021 [5], and across our full archive the difference is
likewise not significant. What is new is that the same data restricted to a modern window produce a
significant increase, so the two conclusions reflect different spans rather than a conflict.

The baseline problem has a documented counterpart. OUTSMART-RSV reports site 211 as S211N and increasing in
RSV-B since 2020/21 [17]; against the modern RSV-B consensus the identical change is N211S and decreasing,
from 378 of 378 records in 2017 to 12 of 1,969 in 2026. Both are correct and describe the same event; neither can be
reconciled with the other without knowing each baseline.

This study does not show that RSV-B consensus residues were previously misreported: the trial analysis that
characterised I206M:Q209R measured its effect on susceptibility [4], and the systematic review separates
polymorphisms from resistance-associated variants [6].

Two methodological results deserve emphasis. Half the GISAID records were excluded by de-duplication and
two fifths matched a GenBank record, so naive pooling would have inflated the denominator by tens of
thousands; yet the retained GISAID records contained every primary-window N201T record, so neither database
alone is adequate. Naive descendant-tip counts were also misleading: acquisition counts should carry branch
support and a rooting check.

The archive also shows where it cannot see. Whole-genome coverage is absent or F-truncated across much of
the Middle East, where at the observed post-boundary frequency the largest national collection would have
roughly an 18% chance of containing one carrier (Supplementary Text, Figure S1).

Nothing here supports changing prophylaxis policy: carriage of a scored substitution is not a confirmed
resistant virus, and almost all deposited records carry none.

### 4.1 Limitations

The public archive is a convenience sample dominated by a few countries, so these figures describe
de-duplicated archive records, not population prevalence (Figure S1). Prophylaxis exposure is unrecorded, national
implementation dates differ while a single boundary was applied, and later sequencing effort was far
greater, so the period comparison is exploratory; stratification by country reduces but does not remove
this, and the first included year changes the conclusion outright. Classifications are DMS scores,
not measured phenotypes; the scan used an RSV-A background while most carriers are RSV-B; and the category
excludes known resistance-associated variants including K68Q and I64M. The
clesrovimab cutoff is unvalidated for that antibody. De-duplication may remove genuinely distinct
infections, though repeating the analysis without it left the pattern in place. A single sampled carrier does not establish absence of transmission; the
phylogenetic results are conditional on one topology and ancestral-state model, though the acquisition
count is stable across rootings. The trend scan reflects lineage turnover, not selection. Clinical severity, prophylaxis failure rates, within-host variants
and exposure history are not recoverable from consensus deposits.

## 5 CONCLUSIONS

Within this deep mutational scan, no single score-based rule separates the F substitutions that have been
shown to reduce nirsevimab activity from those that have not: five of sixteen reported substitutions meet
the criteria used here, two cannot be captured at any Fab cutoff, and capturing the one with a published
clinical case would classify roughly one archive record in twenty as a carrier. Among records collected from
2017 onward, substitutions meeting those criteria were detected only from late 2023 and remained below 0.25%
of records collected on or after 1 July 2023. Exploratory reconstruction across the full archive, stable
under temporal, midpoint and random rootings, assigned them to 32 candidate acquisition branches, and among
records collected on or after 1 July 2023 no sampled carrier cluster exceeded two records. The period
contrast does not hold across the full archive, where the same substitutions are present from 2002 and
2014-15, nor at more permissive cutoffs, where it is not significant or reverses. Reported RSV resistance
frequencies should therefore always be accompanied by the classification rule, the reference baseline and
the collection-year span from which they were derived.

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
population, with per-record deposited dates, date-precision flags and carrier calls; the complete
de-duplication group mapping (65,416 member rows across 38,925 groups, by opaque group identifier, without
sequence data); the maximum-likelihood trees, temporally rooted trees, annotated TreeTime output and
branch-mutation tables; every derived table underlying the figures; and the analysis workflow. The deposited
workflow covers cohort assembly, variant calling, the carriage, threshold-sweep and window-sweep analyses,
the trend scan and the clesrovimab analysis; the phylogenetic stage is documented as the exact commands
used, and figure generation is not included. In accordance with the GISAID Database Access Agreement,
sequence data are not redistributed: GISAID-derived records are identified by EPI_ISL accession and must be
obtained from https://gisaid.org, and GenBank records by accession. DMS scores are available at
https://github.com/dms-vep/RSV_Long_F_DMS. Retrieval date for all sequence data was 2 November 2026.

## REFERENCES

1. Li Y, Wang X, Blau DM, Caballero MT, Feikin DR, Gill CJ, et al. Global, regional, and national disease burden estimates of acute lower respiratory infections due to respiratory syncytial virus in children younger than 5 years in 2019: a systematic analysis. *Lancet*. 2022;399(10340):2047-2064. doi:10.1016/S0140-6736(22)00478-0
2. Shi T, McAllister DA, O'Brien KL, Simoes EAF, Madhi SA, Gessner BD, et al. Global, regional, and national disease burden estimates of acute lower respiratory infections due to respiratory syncytial virus in young children in 2015: a systematic review and modelling study. *Lancet*. 2017;390(10098):946-958. doi:10.1016/S0140-6736(17)30938-8
3. Wang X, Li Y, Shi T, Bont LJ, Chu HY, Zar HJ, et al. Global disease burden of and risk factors for acute lower respiratory infections caused by respiratory syncytial virus in preterm infants and young children in 2019: a systematic review and meta-analysis. *Lancet*. 2024;403(10433):1241-1253. doi:10.1016/S0140-6736(24)00138-7
4. Ahani B, Tuffy KM, Aksyuk AA, Wilkins D, Abram ME, Dagan R, et al. Molecular and phenotypic characteristics of RSV infections in infants during two nirsevimab randomized clinical trials. *Nat Commun*. 2023;14:4347. doi:10.1038/s41467-023-40057-8. Author correction: *Nat Commun*. 2024;15:3026. doi:10.1038/s41467-024-47421-2
5. Wilkins D, Langedijk AC, Lebbink RJ, Morehouse C, Abram ME, Ahani B, et al. Nirsevimab binding-site conservation in respiratory syncytial virus fusion glycoprotein worldwide between 1956 and 2021: an analysis of observational study sequencing data. *Lancet Infect Dis*. 2023;23(7):856-866. doi:10.1016/S1473-3099(23)00062-2. Correction: *Lancet Infect Dis*. 2024;24(5):e281. doi:10.1016/S1473-3099(24)00177-4
6. Berikopoulou MM, Tatsi EB, Siahanidou T, Michos A. Systematic review of the mutations in the active antigenic site Ø of the prefusion F protein of the respiratory syncytial virus (RSV) following the implementation of monoclonal antibody prophylaxis. *Vaccine*. 2026;91:129069. doi:10.1016/j.vaccine.2026.129069
7. Fourati S, Reslan A, Bourret J, Casalegno JS, Rahou Y, Chollet L, et al. Genotypic and phenotypic characterisation of respiratory syncytial virus after nirsevimab breakthrough infections: a large, multicentre, observational, real-world study. *Lancet Infect Dis*. 2025;25(3):301-311. doi:10.1016/S1473-3099(24)00570-X
8. Fourati S, Reslan A, Bourret J, Casalegno JS, Rahou Y, Softic L, et al. Real-world emergence of nirsevimab resistance in breakthrough infections with respiratory syncytial virus-B: a multicentre observational study in France. *Lancet Microbe*. 2026;7(7):101353. doi:10.1016/j.lanmic.2026.101353
9. Iglesias-Caballero M, Infantes JA, Campoy A, Camarero-Serrano S, Moreno S, Cano O, et al. Detection of nirsevimab-resistant RSV-B variants in children carrying the F:N201T substitution through genomic surveillance, Spain, 2025/26 season. *Euro Surveill*. 2026;31(35):2600690. doi:10.2807/1560-7917.ES.2026.31.35.2600690
10. Mengual-Chuliá B, Launes C, Cazorla E, López-Lacort M, Muñoz-Quiles C, Mira-Iglesias A, et al. Genomic surveillance of respiratory syncytial virus during 2023/2024 nirsevimab prophylaxis, Eastern Spain. *Clin Microbiol Infect*. 2026;32(11):1890-1895. doi:10.1016/j.cmi.2026.04.003
11. de Prost N, Le Goff M, Cappy P, Bay P, N'debi M, Soulier A, et al. Detection of a nirsevimab-resistant RSV-B variant (F:K68Q) in an adult with severe infection. *Infect Dis Ther*. 2026;15(11):3221-3226. doi:10.1007/s40121-026-01442-0
12. Simonich CAL, McMahon TE, Juviler G, Kampman L, Chu HY, Bloom JD. Mutational constraints on RSV F and its neutralization by antibodies. *Nature*. 2026;658(8137):998-1007. doi:10.1038/s41586-026-11030-4
13. Aksamentov I, Roemer C, Hodcroft EB, Neher RA. Nextclade: clade assignment, mutation calling and quality control for viral genomes. *J Open Source Softw*. 2021;6(67):3773. doi:10.21105/joss.03773
14. Goya S, Ruis C, Neher RA, Meijer A, Aziz A, Hinrichs AS, et al. Standardized phylogenetic classification of human respiratory syncytial virus below the subgroup level. *Emerg Infect Dis*. 2024;30(8):1631-1641. doi:10.3201/eid3008.240209
15. Piñeiro C, Abuín JM, Pichel JC. Very Fast Tree: speeding up the estimation of phylogenies for large alignments through parallelization and vectorization strategies. *Bioinformatics*. 2020;36(17):4658-4659. doi:10.1093/bioinformatics/btaa582
16. Sagulenko P, Puller V, Neher RA. TreeTime: maximum-likelihood phylodynamic analysis. *Virus Evol*. 2018;4(1):vex042. doi:10.1093/ve/vex042
17. Mahool KA, Kijak GH, Ahani B, Brady TM, Nguyen A, Schaefer E, et al. Nirsevimab binding site conservation in RSV F protein between 2019 and 2024: analysis of sequencing data from the US OUTSMART-RSV surveillance study and public databases. *Open Forum Infect Dis*. 2026;13(Suppl 1):ofaf695.063. doi:10.1093/ofid/ofaf695.063

## FIGURE LEGENDS

**FIGURE 1** Records carrying a DMS-defined high-escape substitution, by subtype and period (a) and by
collection year and period (b), primary window from 2017. Periods are split at the fixed calendar boundary
of 1 July 2023; national rollout dates were not used. Intervals in panel a are Clopper-Pearson, with zero
counts shown as upper bounds and a stub mark at zero. In panel b each year is split into its before- and
on/after-boundary components, so the four carriers collected in November 2023 appear on the correct side of
the boundary. The 2026 bar is a partial year, truncated at the 2 November 2026 retrieval date.

**FIGURE 2** The period comparison depends on two analyst choices. Periods are split at 1 July 2023
throughout. (a) Carriage in each period as a function of the Fab-escape cutoff; among non-zero values
carriage falls about 70-fold between cutoffs of 1.0 and 2.5, and no finite ratio is defined where a period
count is zero. (b) The period-comparison p value against the cutoff; open circles mark cutoffs at which
carriage is higher before the boundary, including the significant reversal at 1.0, and the cross marks the
cutoff at which no record qualifies in either period. (c) The p value against the first collection year
included; open circles mark windows containing pre-boundary carriers.

**FIGURE 3** The 17 substitutions reported in references 4 and 6-11, ordered by Fab-escape score. (a) Score
against the cutoff of 2.036; red marks the five that are classified, grey the two excluded by the
cell-entry floor at any Fab cutoff. (b) Frequency of the same residues in each subtype in the analysis set;
substitutions not tabulated for frequency are marked. The three commonest are RSV-B majority residues.

**FIGURE 4** Candidate reconstructed acquisition branches across the full 38,925-record archive, under
least-squares temporal rooting. (a) Branches per site and acquired residue, named by reconstructed ancestral
state rather than by consensus (Methods 2.4). (b) Sequences in each branch's clade carrying the residue, by
branch-support status. The twelve-carrier cluster is the RSV-B site-209 clade: ten records from Argentina in
2015 and two from Viet Nam in 2014. Rooting sensitivity is given in Table S11.

## TABLES

Tables 1-4 appear in the main text. With Figures 1-4 this is eight display items. Sequencing coverage by
country is supplementary Figure S1.
