# opensciencelabs.github.io

A blog page for OpenScienceLabs with mkdocs site generator.

## To deploy locally

Clone the repository

```bash
git clone git@github.com:opensciencelabs/opensciencelabs.github.io
cd opensciencelabs.github.io
```

```bash
mamba env create -f conda/dev.yaml --yes
conda activate osl-web
poetry install
```

```bash
makim pages.preview
```

## Linter

Ensure you have installed the pre-commit config locally:

```bash
# with your conda env active, run:
$ pre-commit install
```
