"""Render labeled fixtures for offline Node tests, never for publication."""

import json
import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from bs4 import Tag
from test_analytics_presentation import PresentationTests

from scripts.analytics.report import read_snapshot, unavailable


def tree(node):
    """Serialize markup, not layout or browser behavior."""
    if not isinstance(node, Tag):
        return str(node)
    return {
        "tag": node.name,
        "attrs": {
            key: " ".join(value) if isinstance(value, list) else value
            for key, value in node.attrs.items()
        },
        "nodes": [tree(child) for child in node.contents],
    }


def render():
    """Keep all generated test material in an ignored, unpublished folder."""
    fixtures = {}
    for filename in (
        "tests/fixtures/analytics-explorer.json",
        "tests/fixtures/analytics.json",
        "tests/fixtures/analytics-v1.json",
        "unavailable",
    ):
        report = (
            unavailable()
            if filename == "unavailable"
            else read_snapshot(Path(filename), allow_fixture=True)
        )
        fixtures[filename] = tree(PresentationTests().render(report))
    target = Path(".cache/analytics-dom-fixtures.json")
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(fixtures))


if __name__ == "__main__":
    render()
