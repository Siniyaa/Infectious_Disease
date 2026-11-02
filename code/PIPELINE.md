# Pipeline

The analysis was run interactively; this file records every step with the exact commands and
parameters used, so the result can be reproduced. It is documentation, not a tested end-to-end script.

## 1. GenBank retrieval

Metadata via NCBI Datasets (paged, 1,000 records per page):

    https://api.ncbi.nlm.nih.gov/datasets/v2alpha/virus/taxon/11250/dataset_report?page_size=1000

Genomes filtered to length 13,000-16,000 nt, then fetched with Entrez efetch by POST in batches of
200 accessions:

    db=nuccore, rettype=fasta, retmode=text

Notes that cost time to discover: the Datasets accession download endpoint requires the path segment
`/virus/accession/{accessions}/genome/download` (without `/genome/` it returns 404), and a whole-taxon
CDS stream truncates with IncompleteRead. Only 60-65% of RSV genome deposits carry an annotated F CDS
and the proportion varies by year, which is why alignment-based extraction is used instead of
deposited annotation.

## 2. GISAID

EpiRSV export (FASTA plus the metadata table), filtered to human host, 13,000-16,000 nt and a
resolvable collection date. Records are keyed on the EPI_ISL accession parsed from the FASTA header.

## 3. Subtype assignment, alignment and lineages

    nextclade sort combined.fasta --output-results-tsv sort.tsv --jobs 8
    nextclade dataset get --name nextstrain/rsv/a/EPI_ISL_412866 --output-zip ds_a.zip
    nextclade dataset get --name nextstrain/rsv/b/EPI_ISL_1653999 --output-zip ds_b.zip
    nextclade run --input-dataset ds_rsv_a --output-tsv nc_A.tsv \
        --output-translations 'tr_A_{cds}.fasta' --output-fasta aln_A.fasta --jobs 8 comb_A.fasta

`dataset get --output-dir` fails on Windows with "Access is denied (os error 5)"; use `--output-zip`
and unzip separately. F spans reference coordinates 5697-7421 (RSV-A) and 5676-7400 (RSV-B).

## 4. Inclusion and de-duplication

Retain F coverage >= 95% of the 574-residue frame and a resolvable collection date. Exclude laboratory
constructs by record title. Collapse records identical in F sequence, country and collection date;
report the cross-database overlap explicitly rather than assuming it.

## 5. Variant calling and escape scoring

Call amino-acid variants against each subtype's own consensus, computed from the analysis set - not
against a single reference, which would misclassify the 59 residues at which the subtype consensuses
differ. Join observed residues to the deep mutational scanning tables on (site, mutant residue); no
coordinate conversion is required. Validate the join by checking that the highest-escape mutations fall
in antigenic site O (sites 204-215 and 143) and that the scan's wildtype matches the RSV-A consensus
(98.4% of 504 scored sites).

Escape definition: Fab escape >= 2.036 with cell entry >= -0.5, anchored on the weakest clinically
confirmed escape variant (N201T). Repeat every analysis across thresholds 1.0-2.6.

## 6. Statistics

Clopper-Pearson intervals; Wilson upper bounds for zero counts; Fisher exact for era comparisons;
Cochran-Mantel-Haenszel stratified by subtype as the primary inference; a country-matched analysis
restricted to countries sequenced in both eras; Cochran-Armitage for temporal trend with per-year
counts reported beside every statistic; Bonferroni correction across all variants with >= 5 carriers.

## 7. Phylogenetics

    python -m veryfasttree -nt -gtr -gamma -threads 8 -log tree_A.log -out F_A.nwk F_nt_A.fasta
    python -m treetime ancestral --aln F_aa_A.fasta --tree F_A.nwk --aa --outdir tt_A

Install `phylo-treetime`, not the PyPI package named `treetime` (an unrelated GUI tool that shadows the
module name).

**Measure spread as descendants that actually carry the escape residue.** Naive descendant-tip counts
from ancestral reconstruction are unreliable: the largest apparent clade here had 122 tips of which only
2 carried the substitution, the reconstruction having placed the acquisition on a deep branch and
reverted it in every other descendant. Parse the NEXUS newick directly for node-to-tip mapping -
Bio.Phylo's nexus reader drops internal node labels, and TreeTime's auspice JSON stores empty
nucleotide mutation lists for amino-acid runs.
