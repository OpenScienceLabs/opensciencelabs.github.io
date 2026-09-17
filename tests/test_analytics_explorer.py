"""Multi-period query and public-route safety tests, with no credentials."""

import copy
import json
import tempfile
import unittest

from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from jsonschema import ValidationError
from test_analytics import NOW, SETTINGS, FakeClient, response

from scripts.analytics import export, report
from scripts.analytics.routes import public_routes

FIXTURE = Path("tests/fixtures/analytics-explorer.json")


class ExplorerTests(unittest.TestCase):
    """Every selectable period must have independently measured totals."""

    def test_all_windows_queries_and_compatibility(self):
        """Never sum daily users or re-label a 30-day summary as 90 days."""
        client = FakeClient()
        result = export.collect(client, SETTINGS, NOW)
        self.assertEqual(set(result["windows"]), {"7", "30", "90"})
        self.assertEqual(result["summary"], result["windows"]["30"]["summary"])
        for days, window in result["windows"].items():
            self.assertEqual(
                window["reporting_period"],
                report.window_period(NOW, result["timezone"], int(days)),
            )
            for data in [window, window["comparison"]]:
                matches = [
                    request
                    for request in client.requests
                    if not request["dimensions"]
                    and request["metrics"]
                    == [{"name": m} for m in report.METRICS]
                    and request["date_ranges"]
                    == [
                        {
                            "start_date": data["reporting_period"]["start"],
                            "end_date": data["reporting_period"]["end"],
                        }
                    ]
                ]
                self.assertEqual(len(matches), 1)
        self.assertNotEqual(
            sum(
                row["active_users"]
                for row in result["windows"]["30"]["daily_history"]
            ),
            result["summary"]["active_users"],
        )
        self.assertEqual(len(client.requests), 26)

    def test_calendar_presets_across_leap_dst_and_year(self):
        """All six windows are inclusive property-local dates."""
        for now, zone in [
            (datetime(2024, 3, 1, 3, tzinfo=timezone.utc), "America/New_York"),
            (
                datetime(2026, 11, 2, 6, tzinfo=timezone.utc),
                "America/New_York",
            ),
            (
                datetime(2026, 1, 1, 0, tzinfo=timezone.utc),
                "Pacific/Kiritimati",
            ),
        ]:
            for days in report.WINDOW_PRESETS:
                current = report.window_period(now, zone, days)
                previous = report.previous_period(current)
                for period in (current, previous):
                    self.assertEqual(
                        (
                            datetime.fromisoformat(period["end"])
                            - datetime.fromisoformat(period["start"])
                        ).days
                        + 1,
                        days,
                    )
                self.assertEqual(
                    (
                        datetime.fromisoformat(current["start"])
                        - datetime.fromisoformat(previous["end"])
                    ).days,
                    1,
                )
        with self.assertRaises(ValueError):
            report.window_period(NOW, "UTC", 14)

    def test_pages_filtered_at_api_and_response_boundaries(self):
        """Only exact known public paths can enter a page ranking."""
        client = FakeClient()
        with patch.object(
            export, "public_routes", return_value=["/", "/projects/"]
        ):
            export.collect(client, SETTINGS, NOW)
        for request in client.requests:
            if request["dimensions"] != [{"name": "pagePath"}]:
                continue
            filters = request["dimension_filter"]["and_group"]["expressions"]
            self.assertEqual(
                filters[-1]["filter"],
                {
                    "field_name": "pagePath",
                    "in_list_filter": {
                        "values": ["/", "/projects/"],
                        "case_sensitive": True,
                    },
                },
            )
            self.assertEqual(filters[0]["filter"]["field_name"], "hostName")
            self.assertEqual(filters[1]["filter"]["field_name"], "platform")
        for unsafe in [
            "/private/person-123/",
            "/?email=private",
            "//evil.org/",
            "/projects",
            "/projects/index.html",
        ]:
            client = FakeClient()
            client.results[8] = response(
                ["screenPageViews", "activeUsers"],
                [([unsafe], [100, 50])],
                ["pagePath"],
            )
            with self.subTest(path=unsafe), self.assertRaises(ValueError):
                export.collect(client, SETTINGS, NOW)

    def test_route_catalog_uses_mkdocs_urls_not_visitor_input(self):
        """Exclude hidden files, assets and unsafe route syntax."""
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            pages = root / "pages"
            pages.mkdir()
            for name in (
                "index.md",
                "project.md",
                ".private.md",
                "a?b.md",
                "image.svg",
            ):
                (pages / name).write_text("# Synthetic route fixture")
            config = root / "mkdocs.yml"
            config.write_text("site_name: Synthetic\ndocs_dir: pages\n")
            self.assertEqual(public_routes(config), ["/", "/project/"])
            config.write_text(
                "site_name: Synthetic\ndocs_dir: pages\n"
                "use_directory_urls: false\n"
            )
            self.assertEqual(
                public_routes(config), ["/index.html", "/project.html"]
            )

    def test_failures_anywhere_preserve_all_snapshot_versions(self):
        """Do not publish partial exports when later requests fail."""
        for source in [
            Path("tests/fixtures/analytics-v1.json"),
            Path("tests/fixtures/analytics.json"),
            FIXTURE,
        ]:
            with tempfile.TemporaryDirectory() as folder:
                target = Path(folder) / "data.json"
                target.write_bytes(source.read_bytes())
                for index in range(8, 26):
                    client = FakeClient()
                    client.results[index] = RuntimeError("Synthetic failure")
                    with (
                        self.subTest(version=source.name, index=index),
                        self.assertRaises(RuntimeError),
                    ):
                        export.refresh(target, client, SETTINGS, NOW)
                    self.assertEqual(target.read_bytes(), source.read_bytes())

    def test_v3_schema_and_window_invariants(self):
        """Reject invalid periods, private fields and unsafe URLs."""
        original = json.loads(FIXTURE.read_text())
        report.validate(original, allow_fixture=True)
        mutations = [
            lambda data: data["windows"].pop("7"),
            lambda data: data["windows"].update({"14": data["windows"]["7"]}),
            lambda data: data["windows"]["7"]["reporting_period"].update(
                start="2026-09-01"
            ),
            lambda data: data["windows"]["90"]["comparison"]["daily_history"][
                0
            ].update(date="2026-09-15"),
            lambda data: data["windows"]["30"]["summary"].update(
                active_users=999
            ),
            lambda data: data["windows"]["7"]["daily_history"][0].update(
                visitor_id="SYNTHETIC"
            ),
            lambda data: data["windows"]["7"]["breakdowns"]["pages"]["rows"][
                0
            ].update(label="/?private=query"),
            lambda data: data["windows"]["7"]["breakdowns"]["pages"].update(
                total=0
            ),
        ]
        for mutate in mutations:
            data = copy.deepcopy(original)
            mutate(data)
            with (
                self.subTest(mutate=mutate),
                self.assertRaises((ValueError, ValidationError)),
            ):
                report.validate(data, allow_fixture=True)


if __name__ == "__main__":
    unittest.main()
