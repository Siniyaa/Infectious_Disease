# Functionally scored nirsevimab escape is absent before prophylaxis and 0.134% after in 36,662 respiratory syncytial virus genomes, and three substitutions reported as RSV-B escape are subtype-consensus residues
**Authors.** [To be completed by the authors.]

**Running title.** Population-level RSV F escape surveillance

---

## Abstract

**Background.** Long-acting monoclonal antibodies against the respiratory syncytial virus (RSV) fusion
(F) protein are now given to infants in many countries. Reports of escape substitutions have come from
single-country clinical cohorts; the largest published synthesis pooled seven studies and 2,156
samples. Whether escape is accumulating in globally circulating virus has not been established, and
published escape frequencies are not mutually comparable.

**Methods.** All near-complete public RSV genomes from GenBank were combined with a GISAID EpiRSV
export, aligned uniformly to subtype reference datasets, and F amino-acid variants were called against
each subtype's own consensus. Every observed residue was scored against a published deep mutational
scan measuring neutralisation escape from nirsevimab and clesrovimab. Carriage before and after
prophylaxis rollout was compared with exact intervals, subtype-stratified testing and a country-matched
analysis, and repeated across a range of escape thresholds. Acquisition events were counted by
amino-acid ancestral reconstruction on maximum-likelihood F phylogenies, with spread measured as
descendants that actually carry the escape residue.

**Results.** The analysis set held 38,925 de-duplicated sequences, 36,662 in the primary window
(2017 onward): 10,598 before and 26,064 after rollout. No pre-rollout sequence carried a functionally
scored escape substitution, against 35 of 26,064 afterwards (0.134%, 95% CI 0.094-0.187; Fisher
p = 1.3 x 10^-5; subtype-stratified p = 3.1 x 10^-4; country-matched 33/24,421 versus 0/10,045,
p = 2.0 x 10^-5). The effect is confined to the strongest escape class: between Fab thresholds of 1.2
and 1.8 the comparison is null, and at 1.0 it reverses. Escape residues were acquired on 32 independent
branches across eight substitutions; 26 remained a single carrier, the largest post-rollout cluster was
two sequences, and the only larger cluster (12) predates prophylaxis. Three substitutions widely
reported as RSV-B escape are majority residues of RSV-B (90.7%, 84.9%, 77.3%) with no measurable escape
activity. Of 689 F variants tested for temporal trend, 105 rose
significantly and none had escape activity. The pre-exposure clesrovimab baseline was 9 of 26,545
(0.034%), with escape positions that do not overlap those of nirsevimab.

**Conclusions.** Functionally validated escape appears in circulating RSV only after prophylaxis
rollout, remains below 0.25%, and arises repeatedly without any lineage having expanded. A substantial
part of the published RSV-B escape signal is an artefact of scoring RSV-B against an RSV-A reference.
RSV escape frequencies should be reported with both the escape threshold and the subtype baseline
against which they were called.

---

## 1. Introduction

RSV is a leading cause of lower respiratory tract infection in infants, and the introduction of
long-acting monoclonal antibodies directed at the prefusion conformation of the F protein has
substantially reduced infant hospitalisation [8-10]. Nirsevimab binds antigenic site Ø at the apex of
prefusion F; clesrovimab, licensed more recently, binds a separate epitope. As infant prophylaxis has
become universal in a growing number of countries, the question of whether the virus population is
accumulating escape has moved from theoretical concern to operational surveillance.

The published evidence remains thin relative to that question. A 2026 systematic review of site Ø
substitutions following the implementation of monoclonal prophylaxis pooled seven studies and 2,156
RSV-positive samples, reporting limited variability in RSV-A with K65R the commonest substitution, and
substantially higher substitution frequencies in RSV-B involving residues at sites 206, 209 and 211 [1].
The primary reports are national in scope: breakthrough RSV-B infections across France during the
2024-25 season [2]; three children in Spain in 2025/26 carrying F:N201T, where recombinant expression
confirmed reduced nirsevimab recognition and the genomic data indicated sporadic emergence on distinct
backgrounds rather than expansion of a single lineage [3]; 68 isolates from Eastern Spain in 2023/24
[4]; and a single adult case carrying F:K68Q [6]. Each is informative about the viruses it sequenced,
but none supplies a population denominator, and the frequencies they report are not directly comparable
because they are computed against different reference sequences and different definitions of what
counts as an escape substitution.

Two developments make a population-level analysis possible. First, the public sequence archive has
grown to tens of thousands of near-complete genomes spanning both sides of rollout, distributed across
two databases with substantial but unquantified redundancy. Second, a deep mutational scan of RSV F has
measured how nearly all F mutations affect cell entry and neutralisation by nirsevimab, clesrovimab and
other antibodies, providing a functional score for every observed residue rather than a hand-curated
marker list; the authors report that resistant strains have arisen sporadically but remain rare, and
show that the buffering of bivalent IgG binding makes Fab potency the more sensitive readout, which is
also why escape is more readily tolerated in subtype B [5].

We combined the two: every F residue in the public archive, scored against the functional map, with
carriage, temporal trend, threshold sensitivity and mode of emergence estimated at archive scale.

## 2. Methods

### 2.1 Sequence assembly

GenBank contributed 25,377 near-complete genomes (13-16 kb) for human orthopneumovirus. A GISAID
EpiRSV export contributed 56,856 unique records, of which 44,275 passed filtering for human host,
13-16 kb length and a resolvable collection date; 4,267 records lacked an accompanying metadata row and
were excluded. GISAID holdings begin in 2020, so coverage before that year rests on GenBank alone.

All 69,655 sequences were assigned to subtype with the Nextclade minimizer index (RSV-A 37,290,
RSV-B 32,365; one record sorted to human metapneumovirus and three were unassigned, all excluded) and
aligned to the corresponding reference dataset [11], which also supplied consortium lineage assignments
and reference-anchored F translations. Uniform alignment was preferred to deposited CDS annotation,
which is present in only 60-65% of GenBank genome records and varies systematically by year (48.6% in
2017, 91.1% in 2019); depending on it would have discarded a third of the archive for reasons unrelated
to the question. Sequences were retained with F coverage of at least 95% of the 574-residue frame.
Four laboratory constructs were excluded by record title.

### 2.2 De-duplication across databases

Records identical in F sequence, country and collection date were collapsed to one. The redundancy
between databases was measured rather than assumed: 12,325 such groups contained both a GenBank and a
GISAID record, and 52.2% of GISAID records (21,669 of 41,514) collapsed into a sequence already
present. Table 1 gives the full flow.

| Stage | Sequences |
|---|---|
| GenBank near-complete genomes retrieved | 25,377 |
| GISAID EpiRSV records retrieved (unique) | 56,856 |
| GISAID passing host/length/date filters | 44,275 |
| Combined, subtype-assigned and aligned | 69,655 |
| F coverage >=95% and a resolvable collection date | 65,416 |
| After de-duplication on identical F, country and date | 38,925 |
| Primary analysis window, 2017 onward | 36,662 |

**Table 1.** Cohort assembly. The primary window excludes pre-2017 material, which in the GenBank-only
archive accounted for a quarter of the pre-rollout arm and mixed decades-old deposits with contemporary
surveillance.

In the primary window, 19,845 sequences originate from GISAID and 16,817 from GenBank. The era boundary
was 1 July 2023, the start of the first season with universal infant programmes.

### 2.3 Variant calling and functional scoring

Variants were called against each subtype's own consensus, computed from the analysis set. This choice
is load-bearing: the two subtype consensuses differ at 59 of 574 F residues, including sites 201, 206,
209 and 211, so calling RSV-B variants against an RSV-A reference misclassifies RSV-B consensus residues
as substitutions. Observed residues were joined to the deep mutational scanning tables [5] on site and
mutant residue. The scan's numbering matched the RSV-A consensus at 98.4% of its 504 scored sites,
confirming frame alignment, and the RSV-B consensus at 91.7%.

The reference escape definition was a Fab-escape score of at least 2.036 with cell entry at or above
-0.5. It is anchored on the weakest clinically confirmed escape variant, F:N201T (Fab 2.036), and Fab
rather than IgG escape was used because the clinically confirmed variants separate on the Fab scale
(K209E 2.368, N201T 2.036) whereas the frequently reported RSV-B residues do not (I206M 0.598, residue
R at site 209 0.042, S211N -0.036). Twelve nirsevimab and six clesrovimab mutations of 9,812 scored
qualify. Because this definition determines the result, every analysis was repeated across thresholds
from 1.0 to 2.6 and the sensitivity is reported as a primary result.

The transfer of an RSV-A-background scan to RSV-B is stated per substitution. The two RSV-B
substitutions driving the result sit at sites where the RSV-B consensus matches the scan's wildtype
(N208D: wildtype N, RSV-B consensus N; K68I: wildtype K, RSV-B consensus K). K209E and K201E carriers
are exclusively RSV-A and are therefore scored on the scan's own background. The assumption does not
generalise across subtypes: at site 209 the RSV-A consensus is K and the RSV-B consensus is R.

### 2.4 Statistics and phylogenetics

Carriage is reported with Clopper-Pearson intervals, and zero counts as Wilson upper bounds. Eras were
compared with Fisher's exact test; the primary inference is a Cochran-Mantel-Haenszel test stratified by
subtype, with a country-matched analysis restricted to countries sequenced in both eras. Temporal trend
used the Cochran-Armitage test with per-year counts reported beside every statistic. Every F variant
carried by at least five sequences was tested against a Bonferroni threshold.

Maximum-likelihood F phylogenies were built per subtype with VeryFastTree under GTR+gamma [12]
(20,767 and 18,158 tips) and amino-acid ancestral states reconstructed with TreeTime [13], yielding
4,893 and 4,317 branch substitutions. Spread was measured as the number of descendant tips that
actually carry the escape residue, not the total descendant count. This correction is necessary rather
than cosmetic: the largest naive clade (122 tips, lineage B.D.E.1.1) contained only two sequences
carrying the substitution, the reconstruction having placed an acquisition on a deep branch and
reverted it in every other descendant.

## 3. Results

### 3.1 Escape is absent before rollout and rare after it

No sequence collected before July 2023 carried a functionally scored escape substitution, in either
subtype. After rollout, carriage was 0.064% in RSV-A and 0.216% in RSV-B (Table 2, Figure 1), the
subtype difference being in the direction predicted by the lower Fab potency of nirsevimab against
subtype B [5].

| Subtype | Era | Carriers / n | Carriage (%) | 95% CI (%) |
|---|---|---|---|---|
| RSV-A | Before rollout | 0/5,584 | 0.0 | 0.000-0.066 |
| RSV-A | After rollout | 9/14,013 | 0.064 | 0.029-0.122 |
| RSV-B | Before rollout | 0/5,014 | 0.0 | 0.000-0.074 |
| RSV-B | After rollout | 26/12,051 | 0.216 | 0.141-0.316 |
| Both | Before rollout | 0/10,598 | 0.0 | 0.000-0.035 |
| Both | After rollout | 35/26,064 | 0.134 | 0.094-0.187 |

**Table 2.** Carriage of a functionally scored nirsevimab-escape substitution, primary window.
Zero counts are reported as exact upper bounds.

Pooled, the difference gives Fisher p = 1.3 x 10^-5. Stratifying by subtype gives Cochran-Mantel-
Haenszel chi-square 13.04, p = 3.1 x 10^-4. Restricting to the 48 countries sequenced in both eras
retains 33 of the 35 carriers and gives 33/24,421 versus 0/10,045 (p = 2.0 x 10^-5), so the result is
not an artefact of countries that began sequencing only after rollout.

### 3.2 The result belongs to the strongest escape class only

Repeating the comparison across escape thresholds reveals three regimes (Table 3, Figure 2).

| Fab threshold | Qualifying mutations | After rollout | Before rollout | Fisher p |
|---|---|---|---|---|
| 1.000 | 52 | 1161/26,064 (4.454%) | 570/10,598 (5.378%) | 0.0002 |
| 1.200 | 44 | 74/26,064 (0.284%) | 32/10,598 (0.302%) | 0.75 |
| 1.400 | 32 | 41/26,064 (0.157%) | 26/10,598 (0.245%) | 0.08 |
| 1.600 | 23 | 38/26,064 (0.146%) | 24/10,598 (0.227%) | 0.093 |
| 1.800 | 16 | 38/26,064 (0.146%) | 24/10,598 (0.227%) | 0.093 |
| 2.036 | 12 | 35/26,064 (0.134%) | 0/10,598 (0.000%) | 1.3e-05 |
| 2.200 | 10 | 27/26,064 (0.104%) | 0/10,598 (0.000%) | 0.00015 |
| 2.400 | 6 | 21/26,064 (0.081%) | 0/10,598 (0.000%) | 0.0011 |
| 2.500 | 4 | 17/26,064 (0.065%) | 0/10,598 (0.000%) | 0.0053 |
| 2.600 | 2 | 0/26,064 (0.000%) | 0/10,598 (0.000%) | 1 |

**Table 3.** Era comparison as a function of the Fab-escape threshold.

Above 2.0 the pre-rollout count is exactly zero and the difference is significant up to 2.5, beyond
which no carrier exists in either era. Between 1.2 and 1.8 the comparison is null and the point estimate
is higher before rollout. At 1.0 the difference is significant in the reverse direction (5.38% before
versus 4.45% after). The moderate-escape class is part of standing diversity: 26 pre-rollout and 6
post-rollout sequences carry a substitution scoring between 1.4 and 2.036, dominated by N201S.

Any statement about RSV escape frequency is therefore meaningless without its threshold, and we
recommend reporting the escape-score distribution of circulating virus rather than a single count.

### 3.3 Repeated independent emergence without onward spread

Escape residues were acquired on 32 independent branches across eight substitutions (Table 4). The 35
post-rollout carriers span 7 countries and 13 lineages and come from both databases (20 GISAID,
15 GenBank), so the pattern is not a property of any one surveillance programme.

| Subtype | Substitution | Independent acquisitions | Largest carrier cluster | Post-rollout carriers |
|---|---|---|---|---|
| RSV-A | K201E | 2 | 1 | 2 |
| RSV-A | K201T | 1 | 1 | 1 |
| RSV-A | K209E | 6 | 1 | 6 |
| RSV-B | K209E | 1 | 12 | 0 |
| RSV-B | K68I | 4 | 1 | 4 |
| RSV-B | N201T | 5 | 2 | 5 |
| RSV-B | N208D | 11 | 2 | 15 |
| RSV-B | N208T | 2 | 1 | 2 |

**Table 4.** Independent acquisitions and their carrier clusters. A cluster of one is an acquisition that
produced no further sampled sequence carrying the residue. The final column counts distinct post-rollout
carriers, so it is zero for the RSV-B site-209 cluster, which predates prophylaxis; the seven non-zero
values sum to the 35 post-rollout carriers.

26 of the 32 acquisitions remained a single carrier, and the largest post-rollout cluster contained two
carriers (Figure 4). The only larger cluster, 12 carriers of glutamate at site 209 in RSV-B, predates
prophylaxis: 10 sequences from Argentina in 2015 and 2 from Viet Nam in 2014.

The formal comparison against other F substitutions remains a bound rather than a finding: median
carrier descendants 1 versus 1 (Mann-Whitney p = 0.133) and a single-carrier fraction of 26/32 versus
6,402/9,178 (Fisher p = 0.181). These data show that no escape acquisition has been observed to expand;
they do not establish that escape variants spread less than other substitutions, and they cannot exclude
future expansion.

### 3.4 Three widely reported RSV-B substitutions are consensus residues

In the combined cohort, methionine at site 206 is carried by 90.7% of RSV-B sequences, arginine at site
209 by 84.9% and asparagine at site 211 by 77.3%, against 0.01%, 0.05% and 0.01% in RSV-A (Table 5,
Figure 3). None has measurable escape activity. They appear as substitutions only when an RSV-A
reference supplies the baseline.

| Substitution | Fab escape score | Frequency in RSV-A (%) | Frequency in RSV-B (%) | RSV-B consensus residue |
|---|---|---|---|---|
| S211N | -0.036 | 0.01 | 77.28 | yes |
| K209R | 0.042 | 0.048 | 84.94 | yes |
| K65R | 0.17 | 0.997 | 0.05 | no |
| K68Q | 0.572 | 0.0 | 0.34 | no |
| I206M | 0.598 | 0.014 | 90.71 | yes |
| N201T | 2.036 | 0.005 | 0.03 | no |
| K209E | 2.368 | 0.029 | 0.07 | no |
| K68I | 2.469 | 0.0 | 0.02 | no |
| N208D | 2.561 | 0.0 | 0.08 | no |

**Table 5.** Named substitutions, their escape scores and their frequency in each subtype.

The genuine RSV-B variants survive the correction: the RSV-B consensus at site 201 is asparagine and at
site 68 is lysine, so F:N201T and F:K68Q are true departures from RSV-B. For clarity of nomenclature,
the RSV-A consensus at site 209 is lysine and the RSV-B consensus is arginine, so the subtype contrast
is K209R; the designation Q209R used in the published review is retained only when referring to that
source.

### 3.5 External validation against an independently reported variant

The F:N201T substitution reported from Spain in the 2025/26 season [3] is recovered by this pipeline
without being sought: 5 carriers, of which 4 are Spanish (2 in 2025, 2 in 2026) and 1 South African
(2024), all from GISAID deposits. The GenBank-only cohort contained none of them, a direct
demonstration that single-database surveillance misses escape events.

### 3.6 F is drifting, but not at escape positions

Of 689 F variants carried by at least five sequences, 105 rose
significantly across 2017-2026 against a Bonferroni threshold of 7.3 x 10^-5. None reached the escape
threshold. The strongest trends (T12I z = 33.4, K123R z = 25.8, R42K z = 25.6) lie in the signal peptide
and other non-epitope regions and track lineage turnover rather than antibody pressure.

### 3.7 Pre-exposure clesrovimab baseline

Before 2025, 9 of 26,545 sequences carried a clesrovimab-escape substitution (0.034%, CI 0.016-0.064),
all of them RSV-A; no RSV-B sequence carried one (0/12,370, upper bound 0.030%). Carriers came from
Spain, France, Portugal and Australia. The clesrovimab escape positions passing the threshold (429, 443,
445, 470) do not overlap the nirsevimab positions (68, 201, 208, 209, 210), and no sequence carried
escape substitutions for both antibodies.

### 3.8 Where surveillance can and cannot be done

The cohort is dominated by a small number of countries (Figure 5a). In the primary window the entire
Middle East contributes 252 sequences: Qatar 150, Kuwait 79, Jordan 10, Iraq 7 and Egypt 6 (Figure 5b).
The United Arab Emirates, Saudi Arabia and Iran have deposited RSV sequences, but these are short
partial sequences (median 836, 687 and 321 nucleotides) spanning the attachment glycoprotein region and
ending before the F coding sequence begins, so they cannot contribute to escape surveillance even in
principle. Qatar is the only Gulf state with genome-level depth. At the post-rollout carriage estimated
here, detecting at least one carrier with 80% probability requires on the order of 1,200 sequences.

## 4. Discussion

Four findings follow from reading the whole public archive rather than one country at a time.

**Escape is real, recent and rare.** It is absent from every one of 10,598 sequences collected before
July 2023 and present in 0.134% afterwards, and the result survives subtype stratification and country
matching. This corroborates at archive scale, and with a population denominator, the deep mutational
scanning authors' statement that resistant strains have arisen sporadically but remain rare [5], and is
consistent with the sporadic emergence on distinct backgrounds reported from Spain [3].

**The claim is specific to the strongest escape class.** Escape of intermediate strength was not only
present before rollout but slightly commoner, and at a permissive threshold the era comparison reverses
outright. A single-threshold analysis would have concealed this, and it explains why published escape
frequencies vary by orders of magnitude: they are measuring different things. The practical consequence
is that an RSV escape frequency without a stated threshold is uninterpretable.

**Reported RSV-B site-O substitution frequencies substantially reflect subtype-consensus residues.** Three of
the substitutions the systematic review highlights as frequent in RSV-B [1] are the majority residues of
RSV-B and carry no escape activity. The review itself notes that most identified substitutions appear to
represent naturally occurring polymorphisms; this analysis identifies which ones and explains why they
looked like substitutions. Scored against an RSV-A reference, RSV-B appears to carry site Ø "escape" at
77-91%; scored against its own consensus, functionally validated escape in post-rollout RSV-B is 0.216%.

**Escape is generated repeatedly and has not expanded.** Thirty-two independent acquisitions in seven
countries and thirteen lineages, 26 of which produced no further sampled carrier, is the signature of a
variant that arises recurrently but either carries a fitness cost or has not yet met the right
epidemiological conditions. The two clusters that did spread predate prophylaxis entirely. This is not
evidence that expansion cannot happen, and the bound these data place on it is weak.

A fifth, methodological result deserves emphasis because it affects any future study of this kind. Half
of the GISAID records were re-depositions of sequences already in GenBank, so naive pooling would have
inflated the denominator by tens of thousands; but the non-overlapping half contained the independently
reported Spanish N201T cases, which the GenBank-only analysis missed entirely. Neither database alone is
adequate, and the overlap must be measured rather than assumed - in two influenza datasets from our own
group the equivalent redundancy was 96% in one and zero in the other.

Clinically, nothing here supports changing prophylaxis policy. Carriage of a scored mutation is not a
confirmed resistant virus, the measurements are pseudovirus-based, and at 0.134% the overwhelming
majority of circulating RSV remains susceptible on genotypic grounds. The operationally useful finding
is the opposite one: the two antibodies in use have non-overlapping escape routes, so a virus escaping
one is not expected to escape the other, and no sequence in the archive carries both.

### 4.1 Limitations

**Geographic bias.** The archive is a convenience sample dominated by a few countries; carriage is
reported per region as well as pooled, and the pooled figure is not a global prevalence.

**No exposure data.** Public metadata does not record whether a patient received prophylaxis, so the era
comparison is ecological. Carriage cannot be attributed to selection within treated individuals.

**Genotype is not phenotype.** Escape scores are pseudovirus deep mutational scanning measurements. No
virus in this study was phenotypically tested.

**Transfer of an RSV-A map to RSV-B.** Variant calling uses each subtype's own consensus, but the escape
scores themselves remain RSV-A measurements; the assumption is stated per substitution in Methods.

**Sampling-frame change at the era boundary.** The post-rollout arm is drawn from a period of markedly
denser sequencing. The country-matched analysis mitigates this but does not eliminate it.

**A single global era boundary.** Programmes started at different times and some contributing countries
have none, which dilutes the exposed group; country-specific rollout dates remain to be applied.

**De-duplication.** Collapsing records identical in F, country and date may remove genuine same-outbreak
transmission pairs and therefore deflate cluster sizes; a non-de-duplicated sensitivity analysis remains
outstanding, and the spread conclusion should be read with that in mind.

**Phylogenetic support.** Branch support values for the 32 acquisition branches are not reported and
should be added before submission.

**Not assessed.** Clinical severity, prophylaxis failure rates, within-host minor variants and antibody
exposure history are not recoverable from consensus sequence deposits.

## 5. Conclusions

Functionally scored escape from nirsevimab is detectable in circulating RSV only after the introduction
of prophylaxis, remains below 0.25% in both subtypes, and arises by repeated independent substitution
with no lineage yet observed to expand. The effect is confined to the strongest escape class, and
escape frequencies should always be reported with both the threshold and the subtype baseline against
which they were called. A pre-exposure clesrovimab baseline is established at 0.034%, with escape
routes that do not overlap those of nirsevimab. Across the Gulf, only Qatar currently deposits RSV
sequence at a depth that would allow escape to be detected.

---

## Figure legends

**Figure 1.** Escape carriage before and after prophylaxis rollout. (a) By subtype and era, with
Clopper-Pearson intervals; zero counts shown as upper bounds. (b) By collection year, with numerator and
denominator at every non-zero point. Primary window 2017 onward; 10,598 pre-rollout and 26,064
post-rollout sequences; era boundary 1 July 2023.

**Figure 2.** Sensitivity to the escape threshold. (a) Carriage in each era as a function of the
Fab-escape threshold. (b) The era-comparison p-value; the direction of the difference flips below
approximately 2.0.

**Figure 3.** Named substitutions. (a) Fab-escape score, with the threshold marked; orange marks
substitutions that are the RSV-B consensus residue. (b) Frequency of the same residues in each subtype
(RSV-A n = 20,767; RSV-B n = 18,158).

**Figure 4.** Emergence. (a) Independent acquisition branches per substitution. (b) Number of sequences
in each acquisition's clade that carry the escape residue.

**Figure 5.** Sequencing coverage. (a) The twelve largest national contributions. (b) The Middle East in
detail.

## Supplementary material

S1 Sequences per country; S2 the 35 post-rollout carriers with accession, lineage, country and
substitution; S3 all 32 acquisition branches with naive and carrier-corrected descendant counts;
S4 the full temporal-trend scan (689 variants); S5 Middle East sequence counts; S6 clesrovimab
escape carriers.

## Data availability

In line with GISAID terms the per-sequence table carries accessions and derived escape calls only, never
sequences; GISAID-derived rows are identified by EPI_ISL accession and an EPI_SET acknowledgement will
be minted before submission. Analysis used Nextclade 3.25.1, VeryFastTree 4.0.4 and TreeTime 0.12.1.

## References

1. Systematic review of the mutations in the active antigenic site Ø of the prefusion F protein of the
   Respiratory Syncytial Virus (RSV) following the implementation of monoclonal antibody prophylaxis.
   *Vaccine* 2026. PMID 42632373. doi:10.1016/j.vaccine.2026.129069
2. Real-world emergence of nirsevimab resistance in breakthrough infections with respiratory syncytial
   virus-B: a multicentre observational study in France. *The Lancet Microbe* 2026. PMID 42229496.
   doi:10.1016/j.lanmic.2026.101353
3. Detection of nirsevimab-resistant RSV-B variants in children carrying the F:N201T substitution
   through genomic surveillance, Spain, 2025/26 season. *Eurosurveillance* 2026. PMID 42695189.
   doi:10.2807/1560-7917.ES.2026.31.35.2600690
4. Genomic surveillance of respiratory syncytial virus during 2023/2024 nirsevimab prophylaxis, Eastern
   Spain, early results. *Clinical Microbiology and Infection* 2026. PMID 41974354.
   doi:10.1016/j.cmi.2026.04.003
5. Mutational constraints on RSV F and its neutralization by antibodies. *Nature* 2026. PMID 42749798.
   doi:10.1038/s41586-026-11030-4
6. Detection of a Nirsevimab-Resistant RSV-B Variant (F:K68Q) in an Adult with Severe Infection.
   *Infectious Diseases and Therapy* 2026. PMID 42734717. doi:10.1007/s40121-026-01442-0
7. [Reserved - RSV lineage nomenclature. The consortium paper defining the A.D / B.D lineage system
   could not be retrieved through PubMed during preparation; the authors should add it from their
   reference manager. Lineage assignments here follow the Nextclade RSV datasets.]
8. Global, regional, and national disease burden estimates of acute lower respiratory infections due to
   respiratory syncytial virus in children younger than 5 years. *Lancet* 2022. PMID 35598608.
9. Global, regional, and national disease burden estimates of acute lower respiratory infections due to
   respiratory syncytial virus in young children. *Lancet* 2017. PMID 28689664.
10. Global disease burden of and risk factors for acute lower respiratory infections caused by
    respiratory syncytial virus. *Lancet* 2024. PMID 38367641.
11. Nextclade: clade assignment, mutation calling and quality control for viral genomes. *Journal of
    Open Source Software* 2021. (Software reference; not indexed in PubMed.)
12. Very Fast Tree: speeding up the estimation of phylogenies for large alignments through
    parallelization and vectorization strategies. *Bioinformatics* 2020. PMID 32573652.
13. TreeTime: Maximum-likelihood phylodynamic analysis. *Virus Evolution* 2018. PMID 29340210.

*Author lists are omitted and should be completed from the authors' reference manager. Every entry with
a PMID was verified against PubMed during preparation.*
