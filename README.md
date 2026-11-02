# Nirsevimab-escape surveillance in the respiratory syncytial virus fusion protein

Analysis code, figures, tables and manuscript for a population-level study of functionally scored
nirsevimab- and clesrovimab-escape substitutions in RSV F, across the combined public sequence archive.

## Summary of findings

- **No pre-rollout carrier.** Of 10,598 sequences collected before 1 July 2023, none carried a
  functionally scored nirsevimab-escape substitution; 35 of 26,064 collected afterwards did
  (0.134%, 95% CI 0.094-0.187; Fisher p = 1.3e-5; subtype-stratified p = 3.1e-4; restricted to the 48
  countries sequenced in both eras, 33/24,421 vs 0/10,045, p = 2.0e-5).
- **The result is threshold-specific.** Between Fab-escape thresholds of 1.2 and 1.8 the era comparison
  is null; at 1.0 it reverses, with escape commoner *before* rollout. Only the strongest escape class
  behaves as a post-rollout phenomenon.
- **Reported RSV-B escape frequencies need a subtype-matched baseline.** Three substitutions widely
  reported as RSV-B escape (I206M, residue R at site 209, S211N) are majority residues of RSV-B itself -
  90.7%, 84.9% and 77.3% of RSV-B sequences - and carry no measurable escape activity. They appear as
  substitutions only when an RSV-A reference supplies the baseline.
- **Repeated emergence, no expansion.** Escape residues were acquired on 32 independent branches across
  eight substitutions; 26 remained a single carrier and the largest post-rollout cluster was two
  sequences. The only larger cluster (12) predates prophylaxis.
- **Clesrovimab baseline.** 9 of 26,545 pre-2025 sequences (0.034%), all RSV-A. Its escape positions
  (429, 443, 445, 470) do not overlap those of nirsevimab (68, 201, 208, 209, 210), and no sequence
  carries both.

## Data availability and GISAID terms

**This repository contains no sequence data.** The analysis combined GenBank records with a GISAID
EpiRSV export. GISAID data may not be redistributed, so every table here carries accessions
(GenBank accession or GISAID EPI_ISL) and derived calls only. To reproduce the analysis:

1. Retrieve GenBank genomes for taxon 11250 (see `code/PIPELINE.md`).
2. Obtain the GISAID EpiRSV sequences yourself from https://gisaid.org using the accessions listed in
   `data/combined_escape_calls.csv`. A GISAID account is required and the terms of access apply.
3. The deep mutational scanning escape scores are public at
   https://github.com/dms-vep/RSV_Long_F_DMS (`results/summaries/`).

An EPI_SET acknowledgement DOI for the GISAID sequences will accompany the published article.

## Layout

| Path | Contents |
|---|---|
| `manuscript/` | Manuscript and supplementary material, Markdown and Word |
| `figures/` | The five main figures, 300 dpi |
| `tables/` | Main-text Tables 1-5 as CSV |
| `supplementary/` | Supplementary Tables S1-S6 |
| `data/` | Per-sequence escape calls (accessions and derived calls only), carriage and cohort tables |
| `code/` | Pipeline documentation with exact commands and parameters |

## Software

Nextclade 3.25.1 (subtype assignment, alignment, lineage calls, F translation); VeryFastTree 4.0.4
(GTR+gamma maximum-likelihood trees); TreeTime 0.12.1 (amino-acid ancestral reconstruction);
Python 3.12 with pandas, numpy, scipy and matplotlib.

## Status

Manuscript draft, not yet submitted. Outstanding before submission: a non-de-duplicated sensitivity
analysis of the spread result, branch support values for the 32 acquisition branches, country-specific
rollout dates, and completion of reference 7 (RSV lineage nomenclature).
