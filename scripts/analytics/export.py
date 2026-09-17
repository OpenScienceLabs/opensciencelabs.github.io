"""Export only aggregate GA4 statistics, using a CI-only read-only token."""

from __future__ import annotations

import os
import re
import sys

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from scripts.analytics.report import (
    MAX_GROUP_ROWS,
    METRICS,
    MIN_GROUP_USERS,
    SNAPSHOT,
    hostnames,
    month_period,
    periods,
    previous_period,
    unavailable,
    validate,
    write_snapshot,
)

SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
REPOSITORY = "OpenScienceLabs/opensciencelabs.github.io"
PAGE_SIZE = 100
MAX_QUERY_ROWS = 1000
BREAKDOWNS = {
    "countries": ("country", "screenPageViews", "pageviews"),
    "devices": ("deviceCategory", "screenPageViews", "pageviews"),
    "channels": ("sessionDefaultChannelGroup", "sessions", "sessions"),
}


class RestrictedReport(ValueError):
    """GA4 supplied an explicit privacy or metric restriction, not zeros."""

    def __init__(self, zone):
        """Retain only the timezone, never a raw API response."""
        super().__init__("GA4 withheld this report")
        self.zone = zone


class GoogleClient:
    """Small SDK boundary so offline tests never need Google authentication."""

    def __init__(self, token):
        """Load the optional CI dependency only for authenticated exports."""
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.oauth2.credentials import Credentials

        self.client = BetaAnalyticsDataClient(
            credentials=Credentials(token=token, scopes=[SCOPE])
        )

    def run_report(self, *, request):
        """Bound transient retries to keep the short-lived token sufficient."""
        from google.api_core.retry import Retry

        return self.client.run_report(
            request=request,
            retry=Retry(initial=1, maximum=8, deadline=60),
            timeout=30,
        )


@dataclass(frozen=True)
class Settings:
    """Private query configuration, deliberately absent from the report."""

    property_id: str
    hosts: list[str]

    @classmethod
    def from_env(cls, env):
        """Fail closed on missing or malformed production scope."""
        property_id = env.get("GA4_PROPERTY_ID", "")
        if not re.fullmatch(r"[1-9][0-9]*", property_id):
            raise ValueError("GA4_PROPERTY_ID must be a numeric property ID")
        return cls(property_id, hostnames(env.get("GA4_HOSTNAMES", "")))


def dimension_filter(hosts: list[str]) -> dict:
    """AND exact allowed hostnames with Web to exclude apps and other sites."""
    return {
        "and_group": {
            "expressions": [
                {
                    "filter": {
                        "field_name": "hostName",
                        "in_list_filter": {
                            "values": hosts,
                            "case_sensitive": False,
                        },
                    }
                },
                {
                    "filter": {
                        "field_name": "platform",
                        "string_filter": {
                            "match_type": "EXACT",
                            "value": "web",
                            "case_sensitive": False,
                        },
                    }
                },
            ]
        }
    }


def query_page(client, settings, period, metrics, dimensions, offset):
    """Validate one bounded page; retain only counts and requested labels."""
    request = dict(
        property=f"properties/{settings.property_id}",
        date_ranges=[
            {"start_date": period["start"], "end_date": period["end"]}
        ],
        metrics=[{"name": name} for name in metrics],
        dimensions=[{"name": name} for name in dimensions],
        dimension_filter=dimension_filter(settings.hosts),
        keep_empty_rows=True,
        limit=PAGE_SIZE,
        offset=offset,
        order_bys=[
            {"dimension": {"dimension_name": name}} for name in dimensions
        ],
    )
    response = client.run_report(request=request)
    metadata = response.metadata
    if (
        metadata.subject_to_thresholding
        or metadata.schema_restriction_response.active_metric_restrictions
    ):
        raise RestrictedReport(metadata.time_zone)
    if (
        metadata.empty_reason
        or metadata.data_loss_from_other_row
        or metadata.sampling_metadatas
        or getattr(metadata, "data_truncation_reasons", ())
    ):
        raise ValueError("GA4 report is unavailable, restricted or incomplete")
    if (
        not 0 <= response.row_count <= MAX_QUERY_ROWS
        or len(response.rows) > PAGE_SIZE
        or offset + len(response.rows) > response.row_count
        or (not response.rows and response.row_count != 0)
    ):
        raise ValueError("Incomplete or excessive GA4 rows")
    if [header.name for header in response.dimension_headers] != list(
        dimensions
    ):
        raise ValueError("Unexpected GA4 dimensions")
    names = [header.name for header in response.metric_headers]
    if len(names) != len(metrics) or set(names) != set(metrics):
        raise ValueError("Unexpected GA4 metrics")
    result = []
    for row in response.rows:
        if len(row.metric_values) != len(names):
            raise ValueError("Incomplete GA4 metrics")
        if len(row.dimension_values) != len(dimensions):
            raise ValueError("Incomplete GA4 dimensions")
        values = [item.value for item in row.metric_values]
        if any(not re.fullmatch(r"[0-9]+", value) for value in values):
            raise ValueError("Invalid GA4 count")
        result.append(
            (
                [item.value for item in row.dimension_values],
                dict(zip(names, map(int, values), strict=True)),
            )
        )
    return metadata.time_zone, response.row_count, result


def query(client, settings, period, metrics, dimensions=()):
    """Paginate with stable ordering; reject changing or duplicated rows."""
    zone, total, result = query_page(
        client, settings, period, metrics, dimensions, 0
    )
    while len(result) < total:
        next_zone, next_total, rows = query_page(
            client, settings, period, metrics, dimensions, len(result)
        )
        if (next_zone, next_total) != (zone, total):
            raise ValueError("GA4 report changed during pagination")
        result.extend(rows)
    keys = [tuple(dims) for dims, _ in result]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate GA4 rows")
    return zone, result


def summary_counts(rows):
    """Map one period-level report; never sum distinct-user counts."""
    if len(rows) > 1:
        raise ValueError("Expected one period-level summary")
    counts = rows[0][1] if rows else dict.fromkeys(METRICS, 0)
    return {public: counts[api] for api, public in METRICS.items()}


def breakdown(client, settings, period, dimension, api_metric, public_metric):
    """Publish coarse rankings, grouping small and unclassified categories."""
    panel = {
        "status": "withheld",
        "metric": public_metric,
        "minimum_active_users": MIN_GROUP_USERS,
        "rows": [],
        "total": None,
        "other": None,
    }
    try:
        zone, rows = query(
            client, settings, period, [api_metric, "activeUsers"], [dimension]
        )
    except RestrictedReport as error:
        # An explicit GA4 restriction is an honest unavailable panel. Network,
        # permission, sampling, pagination and validation errors still abort
        # the entire refresh, leaving the previous snapshot untouched.
        return error.zone, panel
    total = sum(counts[api_metric] for _, counts in rows)
    visible = []
    for dims, counts in rows:
        label = dims[0]
        if counts["activeUsers"] < MIN_GROUP_USERS or label.lower() in {
            "",
            "(not set)",
            "(other)",
            "unknown",
        }:
            continue
        if not re.fullmatch(r"[^\x00-\x1f<>]{1,80}", label):
            raise ValueError("Invalid aggregate label")
        visible.append({"label": label, "value": counts[api_metric]})
    visible.sort(key=lambda row: (-row["value"], row["label"]))
    panel.update(
        status="available",
        rows=visible[:MAX_GROUP_ROWS],
        total=total,
        other=total - sum(row["value"] for row in visible[:MAX_GROUP_ROWS]),
    )
    return zone, panel


def collect(client, settings: Settings, now: datetime | None = None) -> dict:
    """Re-query all periods; activeUsers is one period-level distinct total."""
    # Relative dates are interpreted by GA4 in its property timezone. This
    # small probe discovers that timezone without requiring the Admin API.
    zone, _ = query(
        client,
        settings,
        {"start": "yesterday", "end": "yesterday"},
        ["screenPageViews"],
    )
    started = now or datetime.now(timezone.utc)
    rolling, history = periods(started, zone)
    summary_zone, summary_rows = query(
        client, settings, rolling, list(METRICS)
    )
    history_zone, history_rows = query(
        client, settings, history, ["screenPageViews"], ["yearMonth"]
    )
    if zone != summary_zone or zone != history_zone:
        raise ValueError("Property timezone changed during export; retry")
    # A successful empty report without an emptyReason/restriction means no
    # measured events for this scope, NOT a failed or unconfigured request.
    report = unavailable()
    report.update(
        status="available",
        hostnames=settings.hosts,
        timezone=zone,
        reporting_period=rolling,
        history_period=history,
        summary=summary_counts(summary_rows),
    )
    for dimensions, values in history_rows:
        value = dimensions[0]
        if not re.fullmatch(r"[0-9]{6}", value):
            raise ValueError("Invalid GA4 month")
        month = value[:4] + "-" + value[4:]
        report["monthly_history"].append(
            {
                "month": month,
                **month_period(month),
                "pageviews": values["screenPageViews"],
            }
        )
    # Missing months remain absent: GA4 cannot prove whether collection was
    # enabled then. Explicit returned zeros, however, are preserved.
    report["monthly_history"].sort(key=lambda item: item["month"])
    comparison = previous_period(rolling)
    comparison_zone, comparison_rows = query(
        client, settings, comparison, list(METRICS)
    )
    report["comparison"] = {
        "reporting_period": comparison,
        "summary": summary_counts(comparison_rows),
    }
    daily_zone, daily_rows = query(
        client, settings, rolling, ["screenPageViews"], ["date"]
    )
    if (comparison_zone, daily_zone) != (zone, zone):
        raise ValueError("Property timezone changed during export; retry")
    for dims, counts in daily_rows:
        day = dims[0]
        if not re.fullmatch(r"[0-9]{8}", day):
            raise ValueError("Invalid GA4 date")
        report["daily_history"].append(
            {
                "date": f"{day[:4]}-{day[4:6]}-{day[6:]}",
                "pageviews": counts["screenPageViews"],
            }
        )
    report["daily_history"].sort(key=lambda row: row["date"])
    report["breakdowns"] = {}
    for key, spec in BREAKDOWNS.items():
        panel_zone, panel = breakdown(client, settings, rolling, *spec)
        if panel_zone != zone:
            raise ValueError("Property timezone changed during export; retry")
        report["breakdowns"][key] = panel
    finished = now or datetime.now(timezone.utc)
    if periods(finished, zone) != (rolling, history):
        raise ValueError("Property midnight crossed during export; retry")
    report["generated_at"] = (
        finished.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    )
    validate(report)
    return report


def refresh(path: Path, client, settings: Settings, now=None) -> dict:
    """Replace a snapshot only after every request and validation succeeds."""
    report = collect(client, settings, now)
    write_snapshot(path, report)
    return report


def main() -> int:
    """Export in trusted CI without logging raw responses or tokens."""
    try:
        if (
            os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY
            or os.environ.get("GITHUB_REF") != "refs/heads/main"
            or os.environ.get("GITHUB_EVENT_NAME")
            not in {"schedule", "workflow_dispatch"}
        ):
            raise ValueError("Live exports are restricted to trusted CI")
        settings = Settings.from_env(os.environ)
        token = os.environ.get("GA4_ACCESS_TOKEN")
        if not token:
            raise ValueError("Missing short-lived analytics access token")
        client = GoogleClient(token)
        refresh(SNAPSHOT, client, settings)
    except Exception as error:
        # Library exception messages can include private request details.
        print(
            "::warning::Analytics refresh failed "
            f"({type(error).__name__}); previous snapshot left unchanged. "
            "See docs/analytics.md for troubleshooting.",
            file=sys.stderr,
        )
        return 1
    print("Analytics snapshot refreshed and validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
