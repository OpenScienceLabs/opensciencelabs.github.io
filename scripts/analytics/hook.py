"""Render the page and JSON from one validated snapshot; never call Google."""

import os
import sys

from pathlib import Path

# MkDocs loads hooks by filename, not as modules in the project package.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.analytics.report import (
    SNAPSHOT,
    is_stale,
    read_snapshot,
    write_snapshot,
)


def on_config(config):
    """Load aggregates with a guarded opt-in for local fixture previews."""
    fixture = os.environ.get("ANALYTICS_PREVIEW_FIXTURE")
    if fixture and (os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS")):
        raise ValueError("Analytics fixture previews are forbidden in CI")
    report = read_snapshot(
        Path(fixture) if fixture else SNAPSHOT, allow_fixture=bool(fixture)
    )
    if fixture and report["data_kind"] != "fixture":
        raise ValueError("Preview input must be explicitly labeled fixture")
    config.extra["analytics_report"] = report
    config.extra["analytics_stale"] = is_stale(report)
    return config


def on_post_build(config):
    """Write only the validated public contract."""
    report = config.extra["analytics_report"]
    write_snapshot(
        Path(config.site_dir) / "analytics/data.json",
        report,
        allow_fixture=report["data_kind"] == "fixture",
    )
