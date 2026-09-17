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

Open `http://localhost:8000/analytics/` to explore the dashboard with clearly
labeled synthetic data. Local preview includes this TEST FIXTURE by default; no
Google credentials are needed. To use the saved real analytics snapshot (or show
the unavailable state if none exists):

```bash
makim pages.preview --no-analytics-fixture
```

Fixtures do not overwrite the saved snapshot or affect `makim pages.build` or
production deployments. Either preview mode supports `--run-pre-build`.

## Linter

Ensure you have installed the pre-commit config locally:

```bash
# with your conda env active, run:
$ pre-commit install
```

## Public analytics

See [analytics setup and operations](docs/analytics.md) for the GA4 exporter,
keyless Google/GitHub configuration, snapshot retention, local fixture tests,
and live/browser acceptance checks.
