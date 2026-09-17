# Public analytics: operations and setup

This is the maintained setup and operations guide. The four non-secret analytics
identifiers are already in `.github/workflows/main.yaml`; **no GA4 repository
variables or secrets are required**. Their presence does not verify Google
permissions or successful traffic collection.

If the service account and WIF provider already exist, verify their restrictions
in [Google setup](#one-time-google-configuration), complete the service-account
binding and GA4 Viewer access, then follow
[GitHub setup](#one-time-github-configuration) and
[the first refresh checks](#first-refresh-and-acceptance-checks). Do not
recreate working resources or generate private keys.

## Design and deployment

- `/analytics/` is a compact report workspace: Overview, Acquisition, Countries,
  Devices and Pages. It uses OSL's shared light/dark tokens, native SVG charts
  and accessible HTML tables, with no chart-library or remote dashboard embed.
  The 30-day fallback is server-rendered. JavaScript reads the same validated
  public report embedded with safe JSON escaping; it makes no network requests.
  Without JavaScript, the 30-day figures, monthly history and dimension tables
  remain available. Existing site tracking is separate.
- `scripts/analytics/export.py` uses Google's Python GA4 Data API client. A
  small filtered report discovers the property's IANA timezone from response
  metadata. It queries **7, 30 and 90 completed days**, each with its own
  dimensionless summary, immediately preceding equal-length summary,
  current/previous daily metric series, and four current-period breakdowns.
  Monthly pageviews cover the prior 12 completed calendar months independently
  of the selected window. This is 26 requests before pagination, not 26 browser
  calls. Every summary's active-user count is queried independently; daily users
  are never summed into a period total. No Admin API or timezone variable is
  needed.
- Every request applies an exact, case-insensitive `hostName` allowlist AND
  `platform = web`. Never put previews, localhost or unrelated domains in the
  allowlist. Hostnames are not inferred from the property, URL, or site tag.
- This is **OSL-published data sourced from Google Analytics**, not a Google
  certification of audience size. Consent choices and blockers can prevent
  measurement, and recent figures may change during GA4 processing. The public
  page explains these limitations and links to OSL's sponsorship page.
- All windows are inclusive property-local calendar dates. Every refresh
  re-queries the entire rolling and historical windows to capture late
  processing and revisions. A timezone change or midnight crossing mid-export
  fails safely.
- Daily/monthly rows absent from GA4 are omitted, not imputed as zeros. Charts
  show gaps and tables say Not reported. Explicit zero rows remain zero. A
  successful unrestricted empty summary means zero measured events for that
  scope. An empty reason, sampling, truncation, malformed response, timeout, or
  failed request instead aborts the refresh. Core-report thresholding or metric
  restrictions also abort it. An explicit privacy/metric restriction on an
  audience breakdown produces a `withheld` panel with null totals, not zeros;
  other validated panels and headline statistics can still be published. Counts
  are not a census of people or all actual visits.
- `pages/analytics/schema.json` is the closed, versioned public contract.
  `additionalProperties: false` and fixed source fields prevent raw responses,
  property IDs, credentials, or visitor details leaking into the JSON. Further
  validation checks calendar boundaries, unique chronological dates/months,
  adjacent comparison dates, ranking order and reconciled breakdown totals.
  `status: unavailable` has null dates, timezone and metrics, not fabricated
  zeros.

The public metric mapping follows the
[GA4 API schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema):

| JSON summary field | GA4 metric        | Meaning within the configured Web/hostname scope                                                        |
| ------------------ | ----------------- | ------------------------------------------------------------------------------------------------------- |
| `pageviews`        | `screenPageViews` | Measured page views, including repeated views.                                                          |
| `active_users`     | `activeUsers`     | GA4's distinct active-user count over the entire reporting period, never a sum of daily/monthly counts. |
| `sessions`         | `sessions`        | Sessions that began during the reporting period.                                                        |

### Using the dashboard

1. Choose **Last 7 / 30 / 90 completed days**. Exact dates are shown beside the
   selector; all cards and dimension reports update together. Unsupported
   presets on older snapshots are disabled, not approximated.
2. Select **Pageviews**, **Active users** or **Sessions** to change the main
   daily chart. Hover/touch the plot or use the keyboard-accessible date slider
   to inspect exact current/previous values. Daily users count users on that
   date only, not a portion of an additive total.
3. Toggle **Previous period** to overlay the preceding equal-length daily series
   on a shared scale, aligned by day index. Card comparisons always show the
   independently queried period totals. A zero baseline has no percentage
   comparison. Use **View data table** for exact daily figures.
4. Open a report from the sidebar or an overview card. Search and sort the
   visible table; the ranking preview follows it. **Search filters that table
   only**, not the headline totals, other dimensions or the global trend. There
   is no unsupported cross-dimension drilldown or arbitrary date picker.
5. **CSV** exports the selected metric's current/previous daily series, or the
   currently searched/sorted dimension table. CSV includes dates, timezone,
   source/scope, refresh timestamp and fixture/production identity. Shares use
   the full panel total even when searching. Cells are quoted and spreadsheet
   formula prefixes neutralized. **Download JSON** provides the complete static
   snapshot. Neither action contacts Google.

### Dashboard contract and grouping

New successful exports use **schema version 3**. Version 1 and 2 snapshots
remain readable without inventing missing features or changing their original
refresh timestamp. `windows` is null when unavailable, otherwise a closed map
with exactly `"7"`, `"30"` and `"90"`. Each contains:

- `reporting_period` and `summary` for that independently queried full period.
- `comparison` with the preceding equal-length `reporting_period`, independently
  queried `summary` and `daily_history`.
- `daily_history`: only returned rows, containing `date`, `pageviews`,
  `active_users` and `sessions`. Missing dates remain absent, not inferred zero.
- `breakdowns`: countries, devices, channels and pages for that current period.
  Countries/devices use `screenPageViews` by `country`/`deviceCategory`;
  channels use `sessions` by `sessionDefaultChannelGroup`, not first-user
  acquisition.

For compatibility, the existing root 30-day `reporting_period`, `summary`,
`comparison`, pageview-only `daily_history` and three audience `breakdowns`
remain exact projections of `windows["30"]`, validated against it. Root
`monthly_history` still contains up to 12 completed calendar months. Consumers
must check `schema_version` and `status`; v1/v2 reports have no `windows` map.

**Public-page safety:** `scripts/analytics/routes.py` derives canonical public
routes from MkDocs' file collection and URL rules. The exporter combines those
exact, case-sensitive routes with the Web/hostname filters in a `pagePath`
allowlist on every page of the request. It also rejects returned paths outside
that list. No arbitrary visitor path, query string, full URL, GA-supplied title,
referrer or identifier is published. Only simple canonical route syntax is
accepted; hidden files and non-document assets are excluded. Unknown paths,
noncanonical aliases and routes no longer in the current site are excluded, so
page totals can be lower than headline pageviews. Query parameters on visits to
known pages are not published; GA4's `pagePath` dimension excludes them. The
route catalog has a 500-route safety limit; review the scope rather than
silently truncating if that limit is reached.

Each breakdown includes `status`, `metric`, `minimum_active_users`, `total`,
`other` and `rows` (`label`, `value`). The exporter uses per-category
**whole-period** `activeUsers` only to require at least ten active users before
naming a category; it does not publish those user counts. At most ten eligible
categories are ranked by the additive metric, with deterministic tie ordering.
Small, remaining and unclassified categories contribute only to `other`.
Grouping reduces published detail but is **not a formal anonymity guarantee**.
No city, arbitrary path, referrer URL, user identifier, raw response or
cross-dimensional report is published. Named page routes use the same
whole-period active-user threshold. Their grouped row is labeled **Other public
pages**; unknown visitor paths are excluded entirely.

Shares are display-only and use each panel's own returned additive `total`,
including `other`, not distinct users or the headline denominator. Rounded
shares may not sum to exactly 100%. A panel's `total` may differ from the
headline during processing or because of reporting semantics; neither is
rewritten to force agreement. The page also flags daily/headline discrepancies
and zero pageviews as reasons to check collection and scope, not proven faults.

Rankings paginate in dimension order with 100 rows per request and a safety
limit of 1,000 rows per report. The exporter rejects duplicate rows, changing
row counts/timezones, missing pages and explicit data loss rather than
publishing a truncated top-ten denominator. All recent windows and panels are
queried again on every refresh. Only a valid complete export is written
atomically; a network or permission failure in a new query retains even an old
version 1 or 2 snapshot byte-for-byte locally, with its original refresh
timestamp. Explicit GA4-restricted breakdowns are the documented exception:
their `status: withheld`, null `total`/`other`, and empty `rows` honestly signal
non-publication. A successful unrestricted empty panel is instead `available`
with zero totals.

**Upgrading an existing deployment:** merge the dashboard changes, then start a
**new** manual run on `main`. No new Google APIs, roles, secrets or workflow
identifiers are needed. The push renders the retained report; only a successful
scheduled/manual export fills the new panels. Re-running only a deploy job does
not fetch new statistics. A rollback must keep a schema-v3-capable reader once
the durable snapshot is v3; do not delete the report to bypass validation.

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

Use **Bash** in Google Cloud Shell or a local shell with `gcloud` installed and
signed in to the intended administrator account (`gcloud auth list`). Run the
blocks in order in the **same shell**; rerun the variable block after opening a
new shell. The administrator needs permission to enable APIs, create/manage the
service account and workload identity pool/provider, and edit the service
account's IAM policy. GA4 property access management is a separate permission.
Do not grant these administrative permissions to the exporter account.

Google's
[WIF prerequisites](https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
include a billing-enabled Cloud project; confirm this with the project
administrator. This exporter does not provision a VM, Cloud Run service, or
BigQuery dataset.

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
export PROJECT_NUMBER="$(
  gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)'
)"
export SA="osl-analytics-exporter@${PROJECT_ID}.iam.gserviceaccount.com"
export POOL="projects/${PROJECT_NUMBER}/locations/global"
POOL+="/workloadIdentityPools/osl-analytics"

# OSL's numeric GitHub IDs prevent repository/organization name-reuse risks.
export REPO_ID='540982912'
export OWNER_ID='56703773'

printf 'PROJECT_NUMBER=%s\nGA4_SERVICE_ACCOUNT=%s\n' "$PROJECT_NUMBER" "$SA"
```

Expect project number `11701823742` and service account
`osl-analytics-exporter@osl-general.iam.gserviceaccount.com`. Stop if project
lookup fails or the values differ unexpectedly. If adapting this setup for a
different repository/owner, look up its numeric IDs rather than reusing OSL's.
With the GitHub CLI (`gh`) installed and authenticated, verify the IDs using:

```bash
gh api "repos/$REPO" --jq '{repository_id: .id, owner_id: .owner.id}'
```

Enable the APIs, then create the account **only if it does not exist**:

```bash
gcloud services enable \
  analyticsdata.googleapis.com iam.googleapis.com \
  cloudresourcemanager.googleapis.com \
  iamcredentials.googleapis.com sts.googleapis.com \
  --project="$PROJECT_ID"

gcloud iam service-accounts create osl-analytics-exporter \
  --project="$PROJECT_ID" \
  --display-name='OSL aggregate analytics exporter'
```

Inspect an existing or newly created account with:

```bash
gcloud iam service-accounts describe "$SA" \
  --project="$PROJECT_ID" --format='yaml(email,disabled)'
```

In the **specific GA4 property's** **Admin → Property access management**, add
the email printed as `$SA` as a user with **Viewer** access (not the literal
text `$SA`). Disable email notification for this service account if offered. Do
not grant account-wide Analytics access, Editor, or Administrator. A Google
Cloud project Viewer role is **not** a substitute for GA4 property access; the
exporter needs no broad project data role.

### 3. Create repository-and-branch-restricted Workload Identity Federation

The following is a dedicated pool/provider for this export. Do not reuse an
unrestricted provider. Keep `main` as the protected, trusted deployment/default
branch. The condition restricts the immutable owner/repository IDs, current repo
name, branch, workflow file, and scheduled/manual events.

Create the pool **only if it does not exist**:

```bash
gcloud iam workload-identity-pools create osl-analytics \
  --project="$PROJECT_ID" --location=global \
  --display-name='OSL analytics GitHub Actions'
```

Assemble the arguments below in Bash. Copy the code blocks, not visually wrapped
terminal output. Never split a flag such as `--attribute-mapping`, a claim name,
or the `refs/heads/main` string across lines. A continuation backslash must be
the last character on its line.

```bash
: "${PROJECT_ID:?Run the variable block in step 2 first}"
: "${REPO_ID:?Run the variable block in step 2 first}"
: "${OWNER_ID:?Run the variable block in step 2 first}"
: "${REPO:?Run the variable block in step 2 first}"

MAPPINGS=(
  'google.subject=assertion.sub'
  'attribute.repository_id=assertion.repository_id'
  'attribute.repository_owner_id=assertion.repository_owner_id'
  'attribute.repository=assertion.repository'
  'attribute.ref=assertion.ref'
  'attribute.workflow_ref=assertion.workflow_ref'
  'attribute.event_name=assertion.event_name'
)
ATTRIBUTE_MAPPING="$(IFS=,; echo "${MAPPINGS[*]}")"
WORKFLOW_REF="${REPO}/.github/workflows/main.yaml@refs/heads/main"
ATTRIBUTE_CONDITION="assertion.repository_id == '${REPO_ID}'"
ATTRIBUTE_CONDITION+=" && assertion.repository_owner_id == '${OWNER_ID}'"
ATTRIBUTE_CONDITION+=" && assertion.repository == '${REPO}'"
ATTRIBUTE_CONDITION+=" && assertion.ref == 'refs/heads/main'"
ATTRIBUTE_CONDITION+=" && assertion.workflow_ref == '${WORKFLOW_REF}'"
ATTRIBUTE_CONDITION+=" && assertion.event_name in "
ATTRIBUTE_CONDITION+="['schedule', 'workflow_dispatch']"

PROVIDER_ARGS=(
  --project="$PROJECT_ID"
  --location=global
  --workload-identity-pool=osl-analytics
  --issuer-uri='https://token.actions.githubusercontent.com'
  --attribute-mapping="$ATTRIBUTE_MAPPING"
  --attribute-condition="$ATTRIBUTE_CONDITION"
)
```

For a **new** provider, run:

```bash
gcloud iam workload-identity-pools providers create-oidc github \
  "${PROVIDER_ARGS[@]}"
```

For an **existing** provider, inspect it first:

```bash
gcloud iam workload-identity-pools providers describe github \
  --project="$PROJECT_ID" --location=global \
  --workload-identity-pool=osl-analytics \
  --format='yaml(name,state,disabled,oidc,attributeMapping,attributeCondition)'
```

The provider must be active, not disabled, with the issuer, mapping and
condition assembled above. Leave allowed audiences at the default; the auth
action uses the provider resource name. If this dedicated provider has a broken
mapping or condition (for example from a pasted line break), repair it with the
same arguments rather than deleting the pool:

```bash
gcloud iam workload-identity-pools providers update-oidc github \
  "${PROVIDER_ARGS[@]}"
```

See Google's
[provider update reference](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc).
Do not overwrite a shared provider without reviewing its other consumers.

### 4. Bind the repository identity and verify configuration

Provider creation alone does **not** authorize service-account impersonation.
Add this binding even when reusing an existing pool/provider, then inspect it:

```bash
: "${POOL:?Run the variable block in step 2 first}"
: "${SA:?Run the variable block in step 2 first}"
: "${REPO_ID:?Run the variable block in step 2 first}"
MEMBER="principalSet://iam.googleapis.com/${POOL}"
MEMBER+="/attribute.repository_id/${REPO_ID}"

gcloud iam service-accounts add-iam-policy-binding "$SA" \
  --project="$PROJECT_ID" \
  --role='roles/iam.workloadIdentityUser' \
  --member="$MEMBER"

gcloud iam service-accounts get-iam-policy "$SA" \
  --project="$PROJECT_ID" --format='yaml(bindings)'

gcloud iam workload-identity-pools describe osl-analytics \
  --project="$PROJECT_ID" --location=global \
  --format='yaml(name,state,disabled)'

gcloud iam workload-identity-pools providers describe github \
  --project="$PROJECT_ID" --location=global \
  --workload-identity-pool=osl-analytics --format='value(name)'
```

Confirm the IAM policy grants `roles/iam.workloadIdentityUser` to exactly the
repository-scoped `$MEMBER`, the pool/account are not disabled, and the provider
condition still rejects PRs, pushes and other branches. Check for unexpected
broader impersonation bindings with the administrator. Cloud IAM checks cannot
confirm GA4 Viewer access; verify that separately in the property's access
management screen.

Compare the last command's full resource name with `GA4_WIF_PROVIDER` in
`jobs.build.env` in `.github/workflows/main.yaml`. Allow several minutes for IAM
propagation. No service-account key, domain-wide delegation, Cloud project Owner
role, or broad Token Creator grant is required for this service-account
impersonation setup. The auth action requests a 15-minute access token scoped
only to `https://www.googleapis.com/auth/analytics.readonly`. It creates **no
credential file** and exports no global credential environment. The token is
passed only to the exporter step; the build receives no token.

This follows the auth action's
[WIF through a service account setup](https://github.com/google-github-actions/auth#workload-identity-federation-through-a-service-account).

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
   new report should have `schema_version: 3`; cards, both charts and all
   audience tables must match the JSON. Withheld panels must have null totals,
   not zero. A successful export with all zeros should prompt verification of
   collection/property/hostname configuration; it does not prove zero actual
   visitors.
5. Compare the summary with GA4 using the identical completed dates, timezone,
   Web platform and hostname filters. Check `activeUsers` as one period total,
   not a sum. Check the comparison period separately, and compare daily/monthly
   `screenPageViews` and country/device/channel additive totals using their
   respective dimensions. Apply the documented grouping before comparing visible
   rankings; small named categories intentionally do not appear. This is **live
   GA4 validation**; mocked tests cannot replace it.
6. Make an ordinary content deployment and confirm that the JSON, including
   `generated_at`, remains identical. Confirm the next scheduled/manual success
   updates it. If refreshes stop, the browser shows a stale notice after three
   days even without another deployment.

To download and validate the **published public aggregate report**, run from the
repository root with the local Python dependencies installed. This is not a
Google API call and requires no credentials:

```bash
mkdir -p .cache
curl --fail --silent --show-error --location \
  https://opensciencelabs.org/analytics/data.json \
  --output .cache/analytics-published.json && \
python - <<'PY'
from pathlib import Path
from scripts.analytics.report import read_snapshot

report = read_snapshot(Path('.cache/analytics-published.json'))
if report['status'] != 'available':
    raise SystemExit('No successful report has been published yet.')
print('Last successful refresh (UTC):', report['generated_at'])
print('Reporting timezone:', report['timezone'])
print('Hostname scope:', report['hostnames'])
print('Reporting period:', report['reporting_period'])
print('Summary:', report['summary'])
PY
```

`read_snapshot` rejects fixtures and validates both the closed schema and
calendar invariants. Leave the downloaded file separate from
`.cache/analytics/data.json`, which is the build's restored snapshot. A valid
but old report still needs its `generated_at` checked for staleness.

## Local verification (no Google authentication)

In the existing `osl-web` environment:

```bash
poetry install
python -m pip install -r requirements-analytics.txt
python -m unittest discover -s tests -v
python tests/render_analytics_dom.py
node tests/analytics-js.test.cjs
poetry check
ruff check scripts/analytics tests
ruff format --check scripts/analytics tests
makim pages.build
python -m scripts.analytics.audit
```

The DOM preparation command writes labeled fixture markup only to ignored
`.cache/analytics-dom-fixtures.json`; it is never a publication artifact.
`tests/fixtures/analytics.json` retains the version 2 migration fixture and
`analytics-v1.json` the version 1 fixture. The explorer fixture is synthetic
throughout, including its daily users and public-page counts.

The Google SDK compatibility test is skipped only if the SDK is unavailable
locally; CI installs the pinned extras and runs it. Offline tests use synthetic
SDK-shaped responses, not recordings or credentials. The website already
receives `jsonschema` through its locked notebook dependencies; the extras file
also declares that dependency explicitly and pins it to the existing lock.

### Local dashboard preview

The existing Makim preview task uses the synthetic explorer fixture by default,
so the full dashboard works locally without Google credentials or a downloaded
snapshot:

```bash
makim pages.preview
```

Visit `http://localhost:8000/analytics/`. The prominent TEST FIXTURE banner and
`data_kind: fixture` in `/analytics/data.json` identify the synthetic report. To
preview the saved real snapshot at `.cache/analytics/data.json` instead:

```bash
makim pages.preview --no-analytics-fixture
```

Without a saved snapshot, this opt-out shows **Analytics data is not available
yet**, not invented statistics. Both commands support `--run-pre-build` when
blog sources need rendering first.

The fixture environment variable is set only in the preview task's process. The
opt-out explicitly clears it, including an inherited value. Neither mode
overwrites the saved snapshot or fetches data from Google. `makim pages.build`
and production deployments do **not** enable fixtures by default.

For a **static fixture preview**, use a separate output directory:

```bash
ANALYTICS_PREVIEW_FIXTURE=tests/fixtures/analytics-explorer.json \
  mkdocs build --site-dir .cache/analytics-preview
python -m http.server 8000 --directory .cache/analytics-preview
```

The TEST FIXTURE banner and `data_kind: fixture` must be present in this mode
too. Never deploy this preview directory. CI rejects the preview environment
variable, and the publication audit rejects fixture JSON even if copied to
`build/`. Without the variable, normal builds use only the ignored restored
snapshot or the unavailable state. The live exporter refuses to authenticate
outside trusted CI.

### Browser verification

For reproducible real-browser screenshots, with the preview server running in
another terminal:

```bash
python -m pip install playwright
python -m playwright install chromium
python tests/browser_analytics.py \
  --output .cache/analytics-screenshots/fixture
```

This optional smoke check uses
[Playwright](https://playwright.dev/python/docs/emulation), checks both modes at
1440px, 390px and 320px, rejects horizontal page overflow, checks download
focus, date/metric switching, report navigation, table search/sort, CSV
downloads and JavaScript-disabled pages, and writes screenshots under
`.cache/analytics-screenshots/fixture/`. It blocks Google tracking requests in
its color-mode checks, and accepts only localhost URLs. Stop the fixture server,
serve the normal `build/` with `python -m http.server 8000 --directory build`,
then run the smoke check again with
`--output .cache/analytics-screenshots/normal`. When no restored snapshot
exists, this covers the honest unavailable state. Inspect the PNGs rather than
assuming automated checks prove visual quality. Ordinary browser previews may
execute the base theme's tracking tag; block analytics requests locally rather
than sending synthetic preview visits to Google.

Before release, inspect desktop (1440px) and mobile (390px and 320px) in both
shared color modes, keyboard focus, table scrolling, browser zoom, the zero-data
chart, stale notice, and unavailable state. The default 30-day report and its
tables must also work with JavaScript disabled; other presets remain
downloadable in the JSON. The base viewport now permits user zoom.

### Release evidence checklist

Record the commit, workflow run URL, results and any skipped checks in the PR or
release discussion. Keep disposable local logs and screenshots under ignored
`.cache/`, not as a second tracked verification report. Never include tokens,
raw API responses, or private account information in those records.

- [ ] Python/JavaScript tests, lint, the full `makim pages.build`, and the
      whole-build credential audit pass. CI must run the real Google SDK
      compatibility test, not skip it.
- [ ] Normal build includes `build/analytics/index.html`, `data.json` and
      `schema.json`, with no fixture values. The explicit fixture preview is
      clearly labeled and cannot pass the production audit.
- [ ] Desktop/mobile, light/dark, keyboard, zoom, horizontal scrolling and
      JavaScript-disabled views are inspected, including zero and stale states.
- [ ] A real manual refresh authenticates, publishes, and matches GA4 with the
      same reporting periods and filters. Check the actual GA4 collection tag;
      the legacy UA tag alone cannot supply GA4 data.
- [ ] A content-only deployment preserves the snapshot/timestamp; a later
      scheduled or manual refresh updates it. The retained/unavailable state and
      failed-run signal are checked for refresh failures.

Mocked tests and a populated workflow are **not live GA4 verification**. The
Node DOM harness executes real explorer code against rendered fixture markup,
but is **not browser visual verification**. If SDK downloads, a browser or
localhost sockets are unavailable in the testing environment, record those
checks as skipped and run them in a capable environment before release. Do not
replace missing evidence with fixture statistics or an assumed successful run.

## Troubleshooting

| Symptom                                                      | Checks / action                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `unrecognized arguments: --attribute-` / Bash “No such file” | A copy/paste inserted newlines inside a flag or value. Rerun the Bash argument-assembly block in Google setup step 3, then create or update the provider as appropriate. Do not split `--attribute-mapping`, claim names or `refs/heads/main`.                                                                                                       |
| Resource already exists                                      | Inspect and reuse it. Use `providers update-oidc` only to repair the dedicated provider's reviewed configuration; still complete the service-account binding and GA4 Viewer access. Do not delete the pool to retry setup.                                                                                                                           |
| Configuration missing / first report unavailable             | Verify all four identifiers in `jobs.build.env`, the WIF service-account binding and GA4 property access; run the workflow on `main`. Do not fill the JSON with example numbers.                                                                                                                                                                     |
| OIDC denied                                                  | Check numeric repository/owner IDs, exact repository case, ref, workflow path, issuer, full provider resource name, WIF service-account binding, Actions `id-token: write`, and IAM propagation. Do not weaken the branch condition to make a PR work.                                                                                               |
| `PermissionDenied` / 403                                     | Enable the Data API in the Cloud project; grant the service account Viewer on the specific GA4 property; check the readonly scope and property ID. Cloud IAM Viewer alone is insufficient.                                                                                                                                                           |
| `Unauthenticated` / 401                                      | Re-run to get a fresh token; do not copy tokens out of logs. Authentication should remain immediately before the export, not before dependency installation.                                                                                                                                                                                         |
| `InvalidArgument` / `ValueError`                             | Check property ID, comma-separated hostnames (no URL, wildcard, port, empty entry), the SDK version, and the report schema. Core restrictions, sampling, empty reasons, truncation and timezone changes abort export; explicit audience restrictions produce withheld panels. Check these in the authenticated GA4 UI, not by logging raw responses. |
| Timeout / quota / service unavailable                        | Transient retries are bounded; keep the last report and retry later. Check Google API quotas and service health. Do not substitute zeros.                                                                                                                                                                                                            |
| Snapshot restore or validation failure                       | Stop publication. Check repository access and `gh-pages:analytics/data.json`. Recover a known valid report from that branch's Git history through an authorized maintenance change. Never delete the snapshot simply to make CI green.                                                                                                               |
| Pages deployment failed                                      | Check Pages source is GitHub Actions, environment permits `main`, custom domain, and `pages: write`. A successfully archived report remains recoverable; rerun publication.                                                                                                                                                                          |
| Schedule stopped / report stale                              | Check default branch, Actions enabled, inactivity auto-disable, queue delays and failed runs. Re-enable and dispatch manually. The old timestamp is intentionally retained.                                                                                                                                                                          |
| Local Quarto failure                                         | Repair the local Quarto installation; `mkdocs build` can separately verify committed Markdown and the analytics page, but does not replace the full blog pre-build check.                                                                                                                                                                            |

The exporter logs an exception **class**, never a potentially sensitive raw
error message. Avoid `set -x`, SDK debug logging, or artifact uploads of the
repository root, `.cache`, environment variables, credentials, or raw API
responses. Only `build/` is published, after the aggregate schema and credential
audit pass. The audit is defense in depth, not permission to place secrets in
content.

### Figures look unexpected

Do not replace surprising numbers with the previously observed 1,699 or adjust
them to match a screenshot with unknown dates. Download the public JSON using
the command above and compare the following in the authenticated GA4 UI:

1. **Freshness and version:** read the actual `generated_at`, not the deployment
   time. A retained report can be valid but stale. A v1/v2 snapshot lacks the
   new presets and page report until a successful new export; it has not lost
   that data.
2. **Property and collection:** verify property `365530978`, its Web stream and
   the live Google tag. The checked-in legacy `UA-213158050-1` tag alone does
   not establish GA4 collection. Check for an existing GA4/Tag Manager
   installation before adding anything; avoid duplicate tracking. This is a
   diagnostic lead, not proof of why a particular report looks unusual.
3. **Dates and scope:** match the exact inclusive dates and property timezone,
   `platform = web`, and only `opensciencelabs.org`. An unfiltered property UI
   can include other sites; never broaden the allowlist just to raise totals.
   The rolling window, previous window and completed months differ.
4. **Definitions:** compare Views with `screenPageViews`, Active users (not
   Total users) with `activeUsers`, and Sessions with `sessions`. Do not sum
   distinct users across dates, countries or devices. Channels use session
   default channel group, not first-user channel or source/medium.
5. **Availability:** inspect GA4's data-quality indicators, consent/tag
   coverage, filters and processing delays. `withheld` panels are explicitly
   restricted, not empty. `Other / unknown` includes intentional grouping and
   cannot be interpreted as a single country. Daily gaps do not prove zero
   activity.
6. **Recheck after processing:** dispatch again later to re-query all windows.
   Do not edit snapshot values or timestamps, disable consent, weaken Google
   restrictions or expose raw API responses to force a plausible dashboard.

For review, share only the already-public aggregate JSON or a redacted GA4
screenshot with matching dates/filters. Never share access tokens or visitor
details. Offline fixtures and successful deployment logs cannot establish why
the production figures differ; reconcile the actual reports separately.

### Local Quarto runtime lookup failures

If the Conda Quarto launcher looks for a missing bundled `deno` or `pandoc`,
repair the environment. If `quarto`, `deno` and `pandoc` are already installed
in the active environment, this local-only override uses those executables and
keeps caches in the workspace, without changing the site or CI configuration:

```bash
mkdir -p .cache/tmp
QUARTO_PREFIX="$(dirname "$(dirname "$(command -v quarto)")")"
TMPDIR="$PWD/.cache/tmp" \
QUARTO_DENO="$(command -v deno)" \
QUARTO_SHARE_PATH="$QUARTO_PREFIX/share/quarto" \
QUARTO_PANDOC="$(command -v pandoc)" \
DENO_DIR="$PWD/.cache/deno" XDG_CACHE_HOME="$PWD/.cache" \
  makim pages.build
python -m scripts.analytics.audit
```

The full build re-renders blog Markdown. Review `git diff` afterward and do not
include unrelated generated blog changes in an analytics/documentation change.
`mkdocs build --clean` can check the static site separately, but does not verify
the Quarto pre-build step.

## Official references

- [GA4 Data API and client quickstart](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [GA4 metrics and dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)
- [Response metadata and property timezone](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/ResponseMetaData)
- [Google authentication for GitHub Actions](https://github.com/google-github-actions/auth)
- [WIF deployment pipeline security and configuration](https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
- [GitHub scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [GitHub custom Pages deployments](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [GitHub token-trigger behavior](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
