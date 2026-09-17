"""Public analytics contract and snapshot handling (no Google credentials)."""

from __future__ import annotations

import json
import re

from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = ROOT / ".cache/analytics/data.json"
SCHEMA = ROOT / "pages/analytics/schema.json"
SOURCE = {
    "publisher": "Open Science Labs",
    "system": "Google Analytics 4",
    "api": "Google Analytics Data API v1beta",
}
SITE = "https://opensciencelabs.org"
METRICS = {
    "screenPageViews": "pageviews",
    "activeUsers": "active_users",
    "sessions": "sessions",
}
WINDOW_DAYS = 30
STALE_DAYS = 3
MAX_HOSTNAME_LENGTH = 253
MIN_GROUP_USERS = 10
MAX_GROUP_ROWS = 10


def hostnames(value: str) -> list[str]:
    """Require explicit, exact public DNS names, never URLs or wildcards."""
    names = [name.strip().lower() for name in value.split(",")]
    pattern = r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?"
    for name in names:
        if (
            len(name) > MAX_HOSTNAME_LENGTH
            or not re.fullmatch(rf"(?:{pattern}\.)+{pattern}", name)
            or name.endswith((".localhost", ".local", ".test", ".invalid"))
            or not re.search(r"[a-z]", name.rsplit(".", 1)[-1])
        ):
            raise ValueError("Invalid analytics hostname allowlist")
    return sorted(set(names))


def periods(now: datetime, zone: str) -> tuple[dict, dict]:
    """Return inclusive calendar dates, not elapsed 24-hour intervals."""
    if now.tzinfo is None:
        raise ValueError("An aware datetime is required")
    today = now.astimezone(ZoneInfo(zone)).date()
    first = today.replace(day=1)
    summary = {
        "start": (today - timedelta(days=WINDOW_DAYS)).isoformat(),
        "end": (today - timedelta(days=1)).isoformat(),
    }
    history = {
        "start": first.replace(year=first.year - 1).isoformat(),
        "end": (first - timedelta(days=1)).isoformat(),
    }
    return summary, history


def month_period(month: str) -> dict:
    """Expand a YYYY-MM month to inclusive calendar boundaries."""
    first = date.fromisoformat(month + "-01")
    following = (first.replace(day=28) + timedelta(days=4)).replace(day=1)
    return {
        "start": first.isoformat(),
        "end": (following - timedelta(days=1)).isoformat(),
    }


def previous_period(period: dict) -> dict:
    """Use the preceding 30 calendar days, without elapsed-time arithmetic."""
    start = date.fromisoformat(period["start"])
    return {
        "start": (start - timedelta(days=WINDOW_DAYS)).isoformat(),
        "end": (start - timedelta(days=1)).isoformat(),
    }


def unavailable() -> dict:
    """Represent an unconfigured first deployment without invented values."""
    return {
        "schema_version": 2,
        "data_kind": "production",
        "status": "unavailable",
        "source": dict(SOURCE),
        "site": SITE,
        "hostnames": [],
        "timezone": None,
        "generated_at": None,
        "reporting_period": None,
        "history_period": None,
        "summary": None,
        "monthly_history": [],
        "comparison": None,
        "daily_history": [],
        "breakdowns": None,
    }


def validate(report: dict, *, allow_fixture: bool = False) -> None:
    """Validate the closed JSON schema and cross-field date invariants."""
    schema = json.loads(SCHEMA.read_text())
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(
        report
    )
    if report["data_kind"] == "fixture" and not allow_fixture:
        raise ValueError("Fixture reports are forbidden in production")
    if report["status"] == "unavailable":
        return
    if hostnames(",".join(report["hostnames"])) != report["hostnames"]:
        raise ValueError("Noncanonical hostname scope")
    generated = datetime.fromisoformat(
        report["generated_at"].replace("Z", "+00:00")
    )
    expected_summary, expected_history = periods(generated, report["timezone"])
    if report["reporting_period"] != expected_summary:
        raise ValueError("Incorrect rolling reporting period")
    if report["history_period"] != expected_history:
        raise ValueError("Incorrect completed-month history period")
    months = []
    for item in report["monthly_history"]:
        bounds = month_period(item["month"])
        if any(item[key] != bounds[key] for key in bounds):
            raise ValueError("Incorrect monthly boundaries")
        if not (
            expected_history["start"]
            <= item["start"]
            <= item["end"]
            <= expected_history["end"]
        ):
            raise ValueError("Month outside historical reporting period")
        months.append(item["month"])
    if months != sorted(set(months)):
        raise ValueError("Monthly history must be unique and chronological")
    if report["schema_version"] == 1:
        # Preserve the original document and successful timestamp, not an
        # invented v2 export. The renderer explains missing dashboard panels.
        return
    if report["comparison"]["reporting_period"] != previous_period(
        expected_summary
    ):
        raise ValueError("Incorrect comparison period")
    dates = [row["date"] for row in report["daily_history"]]
    if dates != sorted(set(dates)) or any(
        not expected_summary["start"] <= day <= expected_summary["end"]
        for day in dates
    ):
        raise ValueError("Daily history must be unique and within the period")
    for panel in report["breakdowns"].values():
        if panel["status"] != "available":
            continue
        labels = [row["label"] for row in panel["rows"]]
        if len(labels) != len(set(labels)):
            raise ValueError("Duplicate breakdown labels")
        if panel["rows"] != sorted(
            panel["rows"], key=lambda row: (-row["value"], row["label"])
        ):
            raise ValueError("Breakdown rows must be ranked deterministically")
        if (
            sum(row["value"] for row in panel["rows"]) + panel["other"]
            != (panel["total"])
        ):
            raise ValueError("Breakdown counts do not reconcile")


def read_snapshot(path: Path, *, allow_fixture: bool = False) -> dict:
    """Treat absence as unavailable; never silently discard corrupt data."""
    if not path.exists():
        return unavailable()
    report = json.loads(path.read_text())
    validate(report, allow_fixture=allow_fixture)
    return report


def write_snapshot(path: Path, report: dict, *, allow_fixture=False) -> None:
    """Validate before atomically replacing any previous successful report."""
    validate(report, allow_fixture=allow_fixture)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(report, indent=2, ensure_ascii=True) + "\n"
    )
    temporary.replace(path)


def is_stale(report: dict, now: datetime | None = None) -> bool:
    """Determine freshness from the successful export, never the build time."""
    if report["generated_at"] is None:
        return False
    generated = datetime.fromisoformat(
        report["generated_at"].replace("Z", "+00:00")
    )
    return (now or datetime.now(timezone.utc)) - generated > timedelta(
        days=STALE_DAYS
    )
