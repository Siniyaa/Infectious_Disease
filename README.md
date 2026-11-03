# Threshold and time-window choices determine whether nirsevimab escape substitutions appear to have increased: an analysis of 38,925 public respiratory syncytial virus genomes

Analysis code, manifests and derived tables for a study of nirsevimab- and clesrovimab-escape
substitutions in the respiratory syncytial virus (RSV) fusion (F) protein, using the combined
public sequence archive (GenBank and GISAID EpiRSV).

## What the study found

Among 36,662 de-duplicated archive records collected from 2017 onward, none of the 10,598
collected before 1 July 2023 carried a substitution classified as high-escape by published deep
mutational scanning (DMS), against 35 of 26,064 collected on or after that date (0.134%,
95% CI 0.094-0.187; Fisher p = 1.3e-5; CMH by country and subtype p = 0.0059).

**That contrast depends on two analyst choices.** Including records from before 2016 adds 13
historical carriers - twelve of which fall in one 2014-15 RSV-B site-209 acquisition clade
(ten Argentina, two Viet Nam) - and the comparison becomes
null (13/12,861 versus 35/26,064, p = 0.44). Lowering the Fab-escape cutoff from 2.036 to 1.0
reverses its direction. The substitutions are not new; they are in the archive from 2002 and
2014-15.

The conclusion of the study is therefore methodological: archive-derived resistance frequencies
are uninterpretable without the classification threshold, the reference baseline and the
collection-year span from which they were derived. These are observations about deposited
sequences, not population prevalence, and no causal claim about prophylaxis is made.

## Contents

- `code/pipeline.py` - the analysis workflow. Stages: fetch-genbank, sort, align, build-cohort,
  call, stats, sensitivity, trend, clesrovimab, phylo. Run `python pipeline.py --help`.
  Figure generation is not included; the tables under `tables/` are its inputs.
- `logs/validation_run.txt` - output of executing the analysis functions against the deposited
  analysis set, reproducing every number in the Results except the acquisition counts.
- `manifests/analysis_set_38925.csv` - one row per analysed record: accession, database, subtype,
  lineage, country, collection date, **date-precision flag**, F coverage, carrier call, period.
- `manifests/deduplication_groups.csv` - the complete de-duplication mapping, 65,416 member rows
  across 38,925 groups, by opaque group identifier, with the retained representative flagged.
  No sequence data.
- `manifests/genbank_accessions.txt`, `manifests/gisaid_epi_isl.txt` - the frozen input lists.
- `phylogenetics/` - maximum-likelihood trees, annotated TreeTime output, branch-mutation tables.
- `tables/`, `figures/`, `manuscript/`, `supplementary/`.

## Reproducing

GISAID sequences cannot be redistributed. Export them from https://gisaid.org using
`manifests/gisaid_epi_isl.txt`, then:

```
python code/pipeline.py all --gisaid-fasta gisaid.fasta --gisaid-meta gisaid.tsv --email you@example.org
```

The GenBank arm consumes `manifests/genbank_accessions.txt` by default so that the cohort is the
frozen one rather than current holdings. DMS scores are pinned to commit
`3ecdfaa661304e3c284acdbeacc9662d2baa1dd9` of https://github.com/dms-vep/RSV_Long_F_DMS and
checksum-verified at run time.

## Caveats

The public archive is a convenience sample dominated by a small number of countries. Prophylaxis
exposure is not recorded in public metadata and national implementation dates differ. Escape
classification is a DMS score, not a measured phenotype; no virus was tested functionally here,
and the narrow high-escape category deliberately excludes some known resistance-associated
variants, including K68Q. The clesrovimab analysis is exploratory: the cutoff was derived for
nirsevimab.

## Data sources

GenBank (NCBI taxon 11250) and GISAID EpiRSV, retrieved 2 November 2026. Lineage assignments and
F translations from Nextclade datasets `nextstrain/rsv/a/EPI_ISL_412866` and
`nextstrain/rsv/b/EPI_ISL_1653999`.
