# Public analytics: operations and setup

## Design and deployment

- `/analytics/` uses the existing MkDocs custom theme and its light/dark tokens.
  The cards, CSS bar chart, and accessible table are server-rendered from the
  same validated report as `/analytics/data.json`. No Google request or token
  reaches the browser. JavaScript only updates the three-day stale notice.
- `scripts/analytics/export.py` uses Google's Python GA4 Data API client. A
  small filtered report discovers the property's IANA timezone from response
  metadata; no Admin API or manually synchronized timezone variable is needed.
  The next query requests `screenPageViews`, `activeUsers`, and `sessions`
  without dimensions across the entire 30-day window ending yesterday. The third
  query requests `screenPageViews` by `yearMonth` for the prior 12 completed
  months.
- Every request applies an exact, case-insensitive `hostName` allowlist AND
  `platform = web`. Never put previews, localhost or unrelated domains in the
  allowlist. Hostnames are not inferred from the property, URL, or site tag.
- All windows are inclusive property-local calendar dates. Every refresh
  re-queries the entire rolling and historical windows to capture late
  processing and revisions. A timezone change or midnight crossing mid-export
  fails safely.
- Monthly rows absent from GA4 are omitted, not imputed as zeros. Explicit zero
  rows remain zero. A successful unrestricted empty summary means zero measured
  events for that scope. An empty reason, restriction, sampling, thresholding,
  truncation, malformed response, timeout, or failed request instead aborts the
  refresh. Counts are not a census of people or all actual visits.
- `pages/analytics/schema.json` is the closed, versioned public contract.
  `additionalProperties: false` and fixed source fields prevent raw responses,
  property IDs, credentials, or visitor details leaking into the JSON. Further
  validation checks calendar boundaries and unique, chronological months.
  `status: unavailable` has null dates, timezone and metrics, not fabricated
  zeros.

### Durable snapshot storage

The existing **`gh-pages` Git branch** stores the validated generated site,
including `analytics/data.json`. It is durable Git history, not an expiring
Actions cache or artifact. Do not delete or force-reset it. The local working
copy `.cache/analytics/data.json` is ignored and disposable.

Every trusted production run acquires the **same workflow-level concurrency
lock** before checking out current `main`, restoring the branch snapshot,
optionally refreshing, building, archiving, and deploying. Ordinary `push`
builds restore and reuse the snapshot without Google authentication. Schedules
and manual runs try to refresh it. A retrieval/network error or invalid stored
report **blocks publication** rather than risking data loss. Only a genuinely
absent branch/file means first deployment. PRs have a separate lock, never
restore or refresh production data, and build the honest unavailable state.

The archive is updated only after a successful build and credential audit. A
report's `generated_at` always means **last successful GA4 export**, not last
build, attempt, Git commit, or Pages deployment. If Pages deployment fails after
archiving, the valid export survives in Git and will be reused next time; the
live site remains on its previous deployment until publication succeeds.

Publication now uses `upload-pages-artifact` and `deploy-pages` **in the same
workflow run**, including `schedule`. The branch commit is storage, not a
request for a second workflow. This explicitly avoids depending on
`GITHUB_TOKEN` pushes triggering another workflow. Set Pages' source to **GitHub
Actions** once, below. All production writers must use this workflow/lock; do
not run `mkdocs gh-deploy` or a separate publishing workflow against this
branch. Existing Netlify settings are not used for this GitHub Pages production
deployment.

Production runs are not canceled in progress. GitHub may replace pending runs;
each surviving run checks out the latest `main`, and loads the current snapshot
inside the lock, so superseded content or analytics do not overwrite newer data.
A pending scheduled refresh replaced by a content build is retried the next day
(or manually); the content build still preserves the existing report.

Refresh errors are continued only long enough to build and publish the retained
report (or the initial unavailable state). After publication the workflow is
marked failed, with annotations and a job summary, so failure is observable. A
restore, build, audit, or archive error stops publication entirely.

## One-time Google configuration

Do this as an authorized Google Cloud and GA4 administrator. No private keys are
needed, and none should be pasted into chat, committed, or saved in repository
secrets. Identifiers below are **not** credentials.

### 1. Verify collection and find the property ID

1. In Google Analytics, select OSL's **GA4 property**, then **Admin → Property
   details**. Confirm the numeric **Property ID** matches `365530978`, which is
   configured in the workflow from the supplied Analytics URL. This is not a
   `G-...` Measurement ID, `UA-...` ID, account ID, stream ID, or Google Cloud
   project number. Confirm the reporting timezone and that this is the intended
   property; the URL alone does not verify collection.
2. Under **Admin → Data streams**, open the intended Web stream and verify that
   it is actually collecting the production website in this property. Review
   recent reports with the exact production hostname scope.
3. **Important existing-site finding:** `theme/base.html` currently contains a
   legacy `UA-213158050-1` Universal Analytics tag. This exporter does not
   create a GA4 property, migrate old data, or invent a GA4 measurement ID.
   Confirm whether GA4 is installed elsewhere (for example through Tag Manager).
   If not, install the correct Web stream's Google tag using **Data streams →
   Web stream → View tag instructions**, replacing the legacy tag through the
   normal site review/deployment process and respecting consent requirements.
   Avoid duplicate tags. The exporter can only publish data GA4 actually has;
   historical data is not backfilled by enabling it. Do not turn consent
   controls off for reporting.

### 2. Enable APIs and create a dedicated service account

Run these commands in an administrator's own authenticated shell. The workflow
uses project `osl-general` (project number `11701823742`). If using another
project or different pool/account names, update the workflow identifiers as
well. The Cloud project may differ from the GA4 property/account. Reuse existing
resources rather than repeating their creation commands.

```bash
export PROJECT_ID='osl-general'
export REPO='OpenScienceLabs/opensciencelabs.github.io'
export PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
export SA="osl-analytics-exporter@${PROJECT_ID}.iam.gserviceaccount.com"

# gh must be authenticated to GitHub; these numeric IDs prevent name-reuse risks.
export REPO_ID="$(gh api "repos/$REPO" --jq '.id')"
export OWNER_ID="$(gh api "repos/$REPO" --jq '.owner.id')"

gcloud services enable \
  analyticsdata.googleapis.com iam.googleapis.com \
  iamcredentials.googleapis.com sts.googleapis.com \
  --project="$PROJECT_ID"

gcloud iam service-accounts create osl-analytics-exporter \
  --project="$PROJECT_ID" \
  --display-name='OSL aggregate analytics exporter'
```

In the **specific GA4 property's** **Admin → Property access management**, add
`$SA` as a user with **Viewer** access. Disable email notification for this
service account if offered. Do not grant account-wide Analytics access, Editor,
or Administrator. A Google Cloud project Viewer role is **not** a substitute for
GA4 property access; the exporter needs no broad project data role.

### 3. Create repository-and-branch-restricted Workload Identity Federation

The following is a dedicated pool/provider for this export. Do not reuse an
unrestricted provider. Keep `main` as the protected, trusted deployment/default
branch. The condition restricts the immutable owner/repository IDs, current repo
name, branch, workflow file, and scheduled/manual events.

```bash
gcloud iam workload-identity-pools create osl-analytics \
  --project="$PROJECT_ID" --location=global \
  --display-name='OSL analytics GitHub Actions'

gcloud iam workload-identity-pools providers create-oidc github \
  --project="$PROJECT_ID" --location=global \
  --workload-identity-pool=osl-analytics \
  --issuer-uri='https://token.actions.githubusercontent.com' \
  --attribute-mapping='google.subject=assertion.sub,attribute.repository_id=assertion.repository_id,attribute.repository_owner_id=assertion.repository_owner_id,attribute.repository=assertion.repository,attribute.ref=assertion.ref,attribute.workflow_ref=assertion.workflow_ref,attribute.event_name=assertion.event_name' \
  --attribute-condition="assertion.repository_owner_id == '${OWNER_ID}' && assertion.repository_id == '${REPO_ID}' && assertion.repository == '${REPO}' && assertion.ref == 'refs/heads/main' && assertion.workflow_ref == '${REPO}/.github/workflows/main.yaml@refs/heads/main' && assertion.event_name in ['schedule', 'workflow_dispatch']"

export POOL="projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/osl-analytics"
gcloud iam service-accounts add-iam-policy-binding "$SA" \
  --project="$PROJECT_ID" \
  --role='roles/iam.workloadIdentityUser' \
  --member="principalSet://iam.googleapis.com/${POOL}/attribute.repository_id/${REPO_ID}"

gcloud iam workload-identity-pools providers describe github \
  --project="$PROJECT_ID" --location=global \
  --workload-identity-pool=osl-analytics --format='value(name)'
```

Compare the last command's full resource name with `GA4_WIF_PROVIDER` in
`jobs.build.env` in `.github/workflows/main.yaml`. Allow several minutes for IAM
propagation. No service-account key, domain-wide delegation, Cloud project Owner
role, or broad Token Creator grant is required for this service-account
impersonation setup. The auth action requests a 15-minute access token scoped
only to `https://www.googleapis.com/auth/analytics.readonly`. It creates **no
credential file** and exports no global credential environment. The token is
passed only to the exporter step; the build receives no token.

## One-time GitHub configuration

In **OpenScienceLabs/opensciencelabs.github.io**, not a fork:

1. Protect `main`, require code review for workflow/exporter changes, and keep
   it the default branch. Authentication and publication are both hard-gated to
   this repository and branch. PRs, forks and manual runs on other branches do
   not authenticate or publish. Do not use `pull_request_target` for this work.
2. Verify the four **non-secret identifiers** already configured once in
   `.github/workflows/main.yaml` under `jobs.build.env`:

   ```yaml
   GA4_PROPERTY_ID: "365530978"
   GA4_HOSTNAMES: "opensciencelabs.org"
   GA4_SERVICE_ACCOUNT: "osl-analytics-exporter@osl-general.iam.gserviceaccount.com"
   GA4_WIF_PROVIDER: "projects/11701823742/locations/global/workloadIdentityPools/osl-analytics/providers/github"
   ```

   You do **not** need GitHub repository variables or secrets for these values.
   Any existing repository variables with these names are no longer used and may
   be removed. To change an identifier, edit the workflow through normal code
   review and ensure the corresponding Google configuration and GA4 property
   access match. Add `www.opensciencelabs.org` only if it actually serves
   measured production traffic; never include previews or localhost. These
   values remain workflow configuration, not hard-coded Python values.

   There is intentionally no timezone variable: GA4 supplies it. No private
   credential secret is required. The access token is generated at runtime by
   OIDC/WIF, not stored in the workflow. Do not configure `GA4_ACCESS_TOKEN`
   manually or use `credentials_json`.

3. Under **Settings → Actions → General**, allow the actions used by the
   workflow and repository `GITHUB_TOKEN` write permissions where organization
   policy requires enabling them. The workflow explicitly requests
   `contents: write` for archiving, `id-token: write` for OIDC, and
   `pages: write` for deployment. Fork PR tokens remain read-only; the WIF
   condition also rejects all PR refs. Permit the Actions bot to update
   `gh-pages` under any applicable ruleset, without granting it a bypass for
   `main` review requirements.
4. **Before the first production run**, set **Settings → Pages → Build and
   deployment → Source: GitHub Actions**. Keep the custom domain
   `opensciencelabs.org`, DNS, and HTTPS enforcement intact. In **Environments →
   github-pages**, permit deployments only from `main`. If unattended daily
   publication is desired, do not require a manual environment approval on each
   run. The old branch remains the snapshot archive, not the Pages build source.
5. Enable the `main` workflow on the default branch. Daily cron is `23 6 * * *`
   (06:23 UTC). GitHub schedules can be delayed or dropped, and
   public-repository schedules can be disabled after 60 days without activity.
   Monitor workflow notifications and the endpoint timestamp; re-enable the
   workflow if needed.

## First refresh and acceptance checks

1. Merge the feature into `main` after configuring Pages. The ordinary push
   publishes either the retained snapshot or “Analytics data is not available
   yet”; it does not require Google configuration.
2. In **Actions → main → Run workflow**, choose **main**. Or use:

   ```bash
   gh workflow run main.yaml --ref main \
     --repo OpenScienceLabs/opensciencelabs.github.io
   ```

3. Check the configuration, Google auth, export, audit, archive, and direct
   Pages deployment steps. The first successful export should log only the
   success message, not raw responses. An unsuccessful refresh leaves a failed
   workflow after safely publishing the retained/unavailable report.
4. Open `https://opensciencelabs.org/analytics/` and download
   `https://opensciencelabs.org/analytics/data.json`. Check `status: available`,
   `data_kind: production`, exact hostnames and property timezone, the dates
   ending yesterday **in that timezone at export time**, and `generated_at`. The
   page cards/table must match the JSON. A successful export with all zeros
   should prompt verification of collection/property/hostname configuration; it
   does not prove zero actual visitors.
5. Compare the summary with GA4 using the identical completed dates, timezone,
   Web platform and hostname filters. Check `activeUsers` as one period total,
   not a sum. Compare available monthly `screenPageViews` separately. This is
   **live GA4 validation**; mocked tests cannot replace it.
6. Make an ordinary content deployment and confirm that the JSON, including
   `generated_at`, remains identical. Confirm the next scheduled/manual success
   updates it. If refreshes stop, the browser shows a stale notice after three
   days even without another deployment.

## Local verification (no Google authentication)

In the existing `osl-web` environment:

```bash
poetry install
python -m pip install -r requirements-analytics.txt
python -m unittest discover -s tests -v
node tests/analytics-js.test.cjs
poetry check
ruff check scripts/analytics tests
ruff format --check scripts/analytics tests
makim pages.build
python -m scripts.analytics.audit
```

The Google SDK compatibility test is skipped only if the SDK is unavailable
locally; CI installs the pinned extras and runs it. Offline tests use synthetic
SDK-shaped responses, not recordings or credentials. The website already
receives `jsonschema` through its locked notebook dependencies; the extras file
also declares that dependency explicitly and pins it to the existing lock.

For an **explicit fixture preview**, use a separate output directory:

```bash
ANALYTICS_PREVIEW_FIXTURE=tests/fixtures/analytics.json \
  mkdocs build --site-dir .cache/analytics-preview
python -m http.server 8000 --directory .cache/analytics-preview
```

Visit `http://localhost:8000/analytics/`. The prominent TEST FIXTURE banner and
`data_kind: fixture` must be present. Never deploy this preview directory. CI
rejects the preview environment variable, and the publication audit rejects
fixture JSON even if copied to `build/`. Without the variable, normal builds use
only the ignored restored snapshot or the unavailable state. The live exporter
refuses to authenticate outside trusted CI.

For reproducible real-browser screenshots, with the preview server running:

```bash
python -m pip install playwright
python -m playwright install chromium
python tests/browser_analytics.py
```

This optional smoke check uses
[Playwright](https://playwright.dev/python/docs/emulation), checks both modes at
1440px, 390px and 320px, rejects horizontal page overflow, checks the download
link's keyboard focus and a JavaScript-disabled page, and writes screenshots
under `.cache/analytics-screenshots/`. It blocks Google tracking requests, and
accepts only localhost URLs. Run it for both the normal unavailable build and
the explicit fixture build. Inspect the PNGs rather than assuming automated
checks prove visual quality.

Before release, inspect desktop (1440px) and mobile (390px and 320px) in both
shared color modes, keyboard focus, table scrolling, browser zoom, the zero-data
chart, stale notice, and unavailable state. All figures and the table must also
work with JavaScript disabled. The base viewport now permits user zoom.

## Troubleshooting

| Symptom                                          | Checks / action                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration missing / first report unavailable | Verify all four identifiers in `jobs.build.env`, the WIF service-account binding and GA4 property access; run the workflow on `main`. Do not fill the JSON with example numbers.                                                                                                                                                  |
| OIDC denied                                      | Check numeric repository/owner IDs, exact repository case, ref, workflow path, issuer, full provider resource name, WIF service-account binding, Actions `id-token: write`, and IAM propagation. Do not weaken the branch condition to make a PR work.                                                                            |
| `PermissionDenied` / 403                         | Enable the Data API in the Cloud project; grant the service account Viewer on the specific GA4 property; check the readonly scope and property ID. Cloud IAM Viewer alone is insufficient.                                                                                                                                        |
| `Unauthenticated` / 401                          | Re-run to get a fresh token; do not copy tokens out of logs. Authentication should remain immediately before the export, not before dependency installation.                                                                                                                                                                      |
| `InvalidArgument` / `ValueError`                 | Check property ID, comma-separated hostnames (no URL, wildcard, port, empty entry), the SDK version, and the report schema. The exporter also conservatively rejects GA4 thresholding/sampling/restrictions/empty reasons/truncation and timezone changes. Check these in the authenticated GA4 UI, not by logging raw responses. |
| Timeout / quota / service unavailable            | Transient retries are bounded; keep the last report and retry later. Check Google API quotas and service health. Do not substitute zeros.                                                                                                                                                                                         |
| Snapshot restore or validation failure           | Stop publication. Check repository access and `gh-pages:analytics/data.json`. Recover a known valid report from that branch's Git history through an authorized maintenance change. Never delete the snapshot simply to make CI green.                                                                                            |
| Pages deployment failed                          | Check Pages source is GitHub Actions, environment permits `main`, custom domain, and `pages: write`. A successfully archived report remains recoverable; rerun publication.                                                                                                                                                       |
| Schedule stopped / report stale                  | Check default branch, Actions enabled, inactivity auto-disable, queue delays and failed runs. Re-enable and dispatch manually. The old timestamp is intentionally retained.                                                                                                                                                       |
| Local Quarto failure                             | Repair the local Quarto installation; `mkdocs build` can separately verify committed Markdown and the analytics page, but does not replace the full blog pre-build check.                                                                                                                                                         |

The exporter logs an exception **class**, never a potentially sensitive raw
error message. Avoid `set -x`, SDK debug logging, or artifact uploads of the
repository root, `.cache`, environment variables, credentials, or raw API
responses. Only `build/` is published, after the aggregate schema and credential
audit pass. The audit is defense in depth, not permission to place secrets in
content.

## Official references

- [GA4 Data API and client quickstart](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [GA4 metrics and dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)
- [Response metadata and property timezone](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/ResponseMetaData)
- [Google authentication for GitHub Actions](https://github.com/google-github-actions/auth)
- [WIF deployment pipeline security and configuration](https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
- [GitHub scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [GitHub custom Pages deployments](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [GitHub token-trigger behavior](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
