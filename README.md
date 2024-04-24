![PyPI - Downloads](https://img.shields.io/pypi/dm/snakefetch)
[![Pylint](https://github.com/niekwit/snakefetch/actions/workflows/pylint.yml/badge.svg)](https://github.com/niekwit/snakefetch/actions/workflows/pylint.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/niekwit/snakefetch/badge)](https://www.codefactor.io/repository/github/niekwit/snakefetch)

# snakefetch
A tool to fetch workflow and config files from a Snakemake repository on GitHub

Although `snakedeploy` can be used to prepare `Snakemake` workflows, this does not always work.

`snakefetch` is basically a simpler version of `snakedeploy` that will copy the config and workflow directories of any `Snakemake` workflow on github into any directory.

## Installation

`snakefetch` can be installed via pip:

```shell
$ pip install snakefetch
```

## Usage

### Help message

```shell
$ snakefetch --help
usage: snakefetch [-h] [--outdir OUTDIR] --url URL --repo-version REPOVERSION [--target-dirs TARGETDIRS] [--version]

Fetch config and workflow directories from a versioned Snakemake repository on GitHub

options:
  -h, --help            show this help message and exit
  --outdir OUTDIR, -o OUTDIR
                        Directory to save the files to
  --url URL, -u URL     URL of the Snakemake repository on GitHub
  --repo-version REPOVERSION, -v REPOVERSION
                        Release version of the Snakemake repository on GitHub
  --target-dirs TARGETDIRS, -t TARGETDIRS
                        Directories to fetch from the Snakemake repository on GitHub (default: config,workflow)
  --version             Print snakefetch version and exit
```

### `snakefetch` version:

```shell
$ snakefetch --version
snakefetch version 0.5.1
```

### Fetching files from Snakemake workflow

```shell
$ snakefetch -o /home/niek/TEST -v v0.4.0 -u https://github.com/niekwit/damid-seq
Downloading archive file for version v0.4.0 from https://github.com/niekwit/damid-seq...
Extracting config and workflow directories from tar.gz file to /home/niek/Downloads/TEST...
Done!
$ cd /home/niek/TEST
$ tree
.
├── config
│   ├── config.yaml
│   ├── README.md
│   └── samples.csv
└── workflow
    ├── envs
    │   ├── damid.yaml
    │   ├── deeptools.yaml
    │   ├── peak_calling.yaml
    │   ├── R.yaml
    │   └── trim.yaml
    ├── report
    │   ├── annotated_peaks.rst
    │   ├── correlation.rst
    │   ├── distance_to_tss.rst
    │   ├── feature_distributions.rst
    │   ├── heatmap.rst
    │   ├── mapping_rates.rst
    │   ├── pca.rst
    │   ├── profile_plot.rst
    │   ├── scree.rst
    │   └── workflow.rst
    ├── rules
    │   ├── bedgraph_processing.smk
    │   ├── bed.smk
    │   ├── damid.smk
    │   ├── deeptools.smk
    │   ├── fastqc.smk
    │   ├── motifs.smk
    │   ├── peak_calling.smk
    │   ├── plotting.smk
    │   ├── resources.smk
    │   └── trimming.smk
    ├── schemas
    │   └── config.schema.yaml
    ├── scripts
    │   ├── annotate_peaks.R
    │   ├── average_bigwig.py
    │   ├── average_wig.py
    │   ├── bowtie2_align_to_plasmid.py
    │   ├── convert_bed2fasta.py
    │   ├── create_annotation_file.R
    │   ├── create_background_fasta.py
    │   ├── create_blacklist.py
    │   ├── damidseq_pipeline.py
    │   ├── filter_overlapping_peaks.py
    │   ├── general_functions.smk
    │   ├── get_resource.sh
    │   ├── mask_fasta.py
    │   ├── peak_annotation_plots.R
    │   ├── plot_mapping_rates.R
    │   ├── plot_PCA.R
    │   ├── quantile_norm_bedgraph.py
    │   ├── resources.py
    │   ├── reverse_log2.py
    │   ├── run_find_peaks.py
    │   └── trim_galore.py
    └── Snakefile

7 directories, 51 files
```
