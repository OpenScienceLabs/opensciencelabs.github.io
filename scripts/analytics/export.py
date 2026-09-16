"""Export only aggregate GA4 statistics, using a CI-only read-only token."""

from __future__ import annotations

import os
import re
import sys

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from scripts.analytics.report import (
    METRICS,
    SNAPSHOT,
    hostnames,
    month_period,
    periods,
    unavailable,
    validate,
    write_snapshot,
)

SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
REPOSITORY = "OpenScienceLabs/opensciencelabs.github.io"


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


def query(client, settings, period, metrics, dimensions=()):
    """Use bounded retries and never request visitor-level dimensions."""
    request = dict(
        property=f"properties/{settings.property_id}",
        date_ranges=[
            {"start_date": period["start"], "end_date": period["end"]}
        ],
        metrics=[{"name": name} for name in metrics],
        dimensions=[{"name": name} for name in dimensions],
        dimension_filter=dimension_filter(settings.hosts),
        keep_empty_rows=True,
        limit=100,
    )
    response = client.run_report(request=request)
    metadata = response.metadata
    if (
        metadata.empty_reason
        or metadata.subject_to_thresholding
        or metadata.data_loss_from_other_row
        or metadata.sampling_metadatas
        or getattr(metadata, "data_truncation_reasons", ())
        or metadata.schema_restriction_response.active_metric_restrictions
    ):
        raise ValueError("GA4 report is unavailable, restricted or incomplete")
    if response.row_count != len(response.rows):
        raise ValueError("Incomplete GA4 rows")
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
    return metadata.time_zone, result


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
    if len(summary_rows) > 1:
        raise ValueError("Expected one period-level summary, not daily users")
    # A successful empty report without an emptyReason/restriction means no
    # measured events for this scope, NOT a failed or unconfigured request.
    counts = summary_rows[0][1] if summary_rows else dict.fromkeys(METRICS, 0)
    report = unavailable()
    report.update(
        status="available",
        hostnames=settings.hosts,
        timezone=zone,
        reporting_period=rolling,
        history_period=history,
        summary={public: counts[api] for api, public in METRICS.items()},
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
