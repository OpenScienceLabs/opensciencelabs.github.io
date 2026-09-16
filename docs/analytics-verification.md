# Analytics implementation verification

Verified locally on 2026-09-16 against the `add-analytics` checkout, initially
at `adb48813`. This is **not a live GA4 or deployed-site acceptance report**.

## Passed

- Local inspection confirmed MkDocs, content in `pages/`, the custom `theme/`,
  and `.github/workflows/main.yaml`. The original publish condition omitted
  schedules. No `AGENTS.md` was found; local `.codex/instructions.md` was read.
- Python unittest suite: **22 passed, 1 skipped**. Coverage includes
  property-local calendar boundaries, leap days, DST, hostname/Web filters on
  all queries, metric-name mapping, a dimensionless period-level active-user
  total, successful zero/empty results, schema and date invariants,
  restricted/failed API responses, re-querying monthly history, snapshot
  preservation and restoration failures, fixture isolation, credential scanning,
  static accessibility, and workflow regression checks.
- JavaScript tests: **3 passed**, including staleness at the exact three-day
  boundary and aging an already-open/background page without another deployment.
- `poetry check`, Ruff lint and formatting, Prettier checks on changed non-theme
  files, `git diff --check`, and available cached pre-commit static hooks
  (whitespace, final newline, JSON, Python syntax/literals/docstrings,
  private-key detection) passed.
- `mkdocs build --clean` passed. The full **`makim pages.build` also passed**,
  including Quarto blog rendering and the pre-built search index, using local
  environment overrides below to repair the installed launcher paths without
  editing the repository or system installation:

  ```bash
  TMPDIR="$PWD/.cache/tmp" \
  QUARTO_DENO="$(command -v deno)" \
  QUARTO_SHARE_PATH="/home/xmn/miniforge3/envs/osl-web/share/quarto" \
  QUARTO_PANDOC="$(command -v pandoc)" \
  DENO_DIR="$PWD/.cache/deno" XDG_CACHE_HOME="$PWD/.cache" \
    makim pages.build
  ```

  The initial unmodified launcher failed looking for `bin/tools/x86_64/deno`.
  The final build emitted expected new-page warnings about absent Git history
  and RSS dates, not analytics failures. No unrelated blog changes remain.

- The generated `build/analytics/data.json` validates and honestly reports
  `status: unavailable`, null metrics/dates/timezone, and no fabricated traffic.
  The generated schema, page, stylesheet and script are present. The whole-build
  credential audit passed.
- An explicitly labeled fixture build in `.cache/analytics-preview/` passed. Its
  three metric cards and 12 table rows match `tests/fixtures/analytics.json`.
  The TEST FIXTURE banner is present; the normal build has no fixture
  statistics. Static template tests cover all-zero bars, stale text, table
  captions/header scopes and the no-data state. The fixture build cannot pass
  the production audit.
- Filesystem resolution of all same-site links/assets from the generated
  analytics page passed for both the normal and fixture builds (including JSON,
  schema, stylesheet/script and sponsorship links).

## Not verified here / required before release

- **Live Google authentication and GA4 results:** no account configuration was
  supplied. The SDK is not installed locally, and package downloads fail because
  network/DNS access is unavailable. The real protobuf request-compatibility
  test is therefore the single skipped test; CI installs
  `requirements-analytics.txt` and runs it. Mocked tests do not establish live
  API compatibility or access.
- **Desktop/mobile browser visual verification:** no usable browser or
  Playwright installation is available. Package installation is unavailable, and
  local TCP socket creation is denied by this environment. No screenshots,
  interactive color-mode inspection, or browser accessibility audit is claimed.
  Static markup/style checks are not a substitute. `tests/browser_analytics.py`
  supplies repeatable smoke checks/screenshots at 1440px, 390px and 320px in
  both modes for a capable local environment; it still requires execution and
  PNG inspection.
- **HTTP link crawler:** the existing internal-link checker could not start its
  localhost server (`PermissionError: Operation not permitted`). Filesystem link
  checks passed instead. The full network-dependent pre-commit suite was not
  run.
- **Production deployment/settings:** the local workflow and public homepage
  were inspected, but authenticated GitHub Pages settings, Cloud IAM, GA4
  configuration, and deployment execution were not inspected or changed. No
  commit, push, deployment, cloud resource creation, or live refresh was made.
- **Existing collection:** the local template still has a legacy UA tag. Confirm
  the actual GA4 Web stream is collecting production traffic before interpreting
  an export; this feature intentionally does not invent a measurement ID.

Follow [analytics setup and acceptance checks](analytics.md), including changing
Pages source to **GitHub Actions**, verifying the workflow's analytics
identifiers and restricted WIF service account, dispatching the first refresh,
comparing GA4 reports, and confirming a subsequent content deployment preserves
the JSON.
