"""Expanded dashboard contracts using explicitly synthetic offline data."""

import copy
import json
import tempfile
import unittest

from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace as Obj
from unittest.mock import patch

import test_analytics_presentation as presentation_tests

from jsonschema import ValidationError
from test_analytics import NOW, SETTINGS, FakeClient, response

from scripts.analytics import export, hook, presentation, report

FIXTURE = Path("tests/fixtures/analytics.json")
LEGACY = Path("tests/fixtures/analytics-v1.json")


class ExpandedExportTests(unittest.TestCase):
    """Whole-period users, safe pagination and honest partial availability."""

    def test_comparison_has_independent_period_users(self):
        """No daily or category user counts construct either headline."""
        client = FakeClient()
        result = export.collect(client, SETTINGS, NOW)
        self.assertEqual(
            result["comparison"]["summary"],
            {"pageviews": 90, "active_users": 25, "sessions": 55},
        )
        self.assertEqual(result["summary"]["active_users"], 31)
        self.assertEqual(client.requests[3]["dimensions"], [])
        self.assertEqual(
            client.requests[3]["date_ranges"],
            [{"start_date": "2026-07-18", "end_date": "2026-08-16"}],
        )
        for request in client.requests[4:]:
            self.assertEqual(
                request["date_ranges"], client.requests[1]["date_ranges"]
            )
        self.assertEqual(
            client.requests[7]["metrics"],
            [{"name": "sessions"}, {"name": "activeUsers"}],
        )

    def test_preceding_window_calendar_boundaries(self):
        """Comparison periods are adjacent across leap days and local years."""
        for now, zone, expected in [
            (
                datetime(2024, 3, 31, 12, tzinfo=timezone.utc),
                "UTC",
                {"start": "2024-01-31", "end": "2024-02-29"},
            ),
            (
                datetime(2026, 1, 1, 0, 30, tzinfo=timezone.utc),
                "America/Los_Angeles",
                {"start": "2025-11-01", "end": "2025-11-30"},
            ),
        ]:
            with self.subTest(zone=zone):
                rolling, _ = report.periods(now, zone)
                self.assertEqual(report.previous_period(rolling), expected)

    def test_small_unknown_and_remaining_categories_are_grouped(self):
        """Apply the active-user threshold, not a pageview threshold."""
        rows = [([f"Country {i:02}"], [100 + i, 10]) for i in range(12)]
        rows.extend(
            [(["Small country"], [500, 9]), (["(not set)"], [200, 100])]
        )
        client = FakeClient()
        client.results[5] = response(
            ["screenPageViews", "activeUsers"], rows, ["country"]
        )
        panel = export.collect(client, SETTINGS, NOW)["breakdowns"][
            "countries"
        ]
        self.assertEqual(len(panel["rows"]), report.MAX_GROUP_ROWS)
        self.assertEqual(
            panel["rows"][0], {"label": "Country 11", "value": 111}
        )
        self.assertEqual(panel["other"], 901)
        self.assertEqual(panel["total"], 1966)
        self.assertNotIn("Small country", json.dumps(panel))
        self.assertNotIn("(not set)", json.dumps(panel))
        self.assertNotIn("activeUsers", json.dumps(panel))

    def paginated_country_client(self):
        """Build three sorted pages where the largest category is last."""
        count = 205
        rows = [([f"Country {i:03}"], [i, 10]) for i in range(count)]
        pages = []
        for offset in range(0, count, export.PAGE_SIZE):
            page = response(
                ["screenPageViews", "activeUsers"],
                rows[offset : offset + export.PAGE_SIZE],
                ["country"],
            )
            page.row_count = count
            pages.append(page)
        client = FakeClient()
        client.results[5:6] = pages
        return client

    def test_paginated_rankings_preserve_scope_and_denominator(self):
        """Pagination must not truncate rankings or the other row."""
        client = self.paginated_country_client()
        panel = export.collect(client, SETTINGS, NOW)["breakdowns"][
            "countries"
        ]
        self.assertEqual(panel["total"], sum(range(205)))
        self.assertEqual(panel["rows"][0]["value"], 204)
        requests = client.requests[5:8]
        self.assertEqual([item["offset"] for item in requests], [0, 100, 200])
        for request in requests:
            self.assertEqual(
                request["dimension_filter"],
                export.dimension_filter(SETTINGS.hosts),
            )
            self.assertEqual(
                request["order_bys"],
                [{"dimension": {"dimension_name": "country"}}],
            )

    def test_bad_pagination_preserves_legacy_snapshot(self):
        """Changing pages, duplicate keys and failures are rejected."""
        mutations = [
            lambda page: setattr(page, "row_count", 206),
            lambda page: setattr(page.metadata, "time_zone", "UTC"),
            lambda page: setattr(page, "rows", []),
            lambda page: setattr(
                page.rows[0].dimension_values[0], "value", "Country 000"
            ),
        ]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_bytes(LEGACY.read_bytes())
            for mutate in mutations:
                with self.subTest(mutate=mutate):
                    client = self.paginated_country_client()
                    mutate(client.results[6])
                    with self.assertRaises(ValueError):
                        export.refresh(path, client, SETTINGS, NOW)
                    self.assertEqual(path.read_bytes(), LEGACY.read_bytes())
            client = self.paginated_country_client()
            client.results[6] = RuntimeError("Synthetic timeout")
            with self.assertRaises(RuntimeError):
                export.refresh(path, client, SETTINGS, NOW)
            self.assertEqual(path.read_bytes(), LEGACY.read_bytes())

    def test_explicit_privacy_restriction_is_withheld_not_zero(self):
        """Explicit GA4 restrictions produce unavailable panels."""
        for metadata in [
            {"subject_to_thresholding": True},
            {
                "schema_restriction_response": Obj(
                    active_metric_restrictions=[Obj()]
                )
            },
        ]:
            client = FakeClient()
            client.results[5] = response(
                ["screenPageViews", "activeUsers"], [], ["country"], **metadata
            )
            result = export.collect(client, SETTINGS, NOW)
            panel = result["breakdowns"]["countries"]
            self.assertEqual(panel["status"], "withheld")
            self.assertIsNone(panel["total"])
            self.assertIsNone(panel["other"])
            self.assertEqual(panel["rows"], [])
            self.assertEqual(result["summary"]["pageviews"], 120)
            self.assertEqual(
                result["breakdowns"]["devices"]["status"], "available"
            )

    def test_each_new_query_failure_preserves_snapshot(self):
        """No partial v2 upgrade or changed timestamp on failed new queries."""
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_bytes(LEGACY.read_bytes())
            for index in range(3, 8):
                with self.subTest(query=index):
                    client = FakeClient()
                    client.results[index] = RuntimeError("Synthetic failure")
                    with self.assertRaises(RuntimeError):
                        export.refresh(path, client, SETTINGS, NOW)
                    self.assertEqual(path.read_bytes(), LEGACY.read_bytes())
            client = FakeClient()
            client.results[5].metadata.sampling_metadatas = [Obj()]
            with self.assertRaises(ValueError):
                export.refresh(path, client, SETTINGS, NOW)
            self.assertEqual(path.read_bytes(), LEGACY.read_bytes())
            export.refresh(path, FakeClient(), SETTINGS, NOW)
            self.assertEqual(report.read_snapshot(path)["schema_version"], 2)

    def test_missing_days_and_empty_panels_not_fabricated(self):
        """Explicit zeros survive, while absent dates stay absent from JSON."""
        client = FakeClient()
        client.results[4] = response(
            ["screenPageViews"], [(["20260915"], [0])], ["date"]
        )
        client.results[5] = response(
            ["screenPageViews", "activeUsers"], [], ["country"]
        )
        result = export.collect(client, SETTINGS, NOW)
        self.assertEqual(
            result["daily_history"], [{"date": "2026-09-15", "pageviews": 0}]
        )
        panel = result["breakdowns"]["countries"]
        self.assertEqual(panel["status"], "available")
        self.assertEqual(panel["total"], 0)


class ExpandedContractTests(unittest.TestCase):
    """Version coexistence and closed nested aggregate schemas."""

    def test_legacy_preview_keeps_document_and_timestamp(self):
        """A render is not a new export or a silent schema migration."""
        original = json.loads(LEGACY.read_text())
        with tempfile.TemporaryDirectory() as folder:
            config = Obj(extra={}, site_dir=folder)
            with patch.dict(
                "os.environ",
                {"ANALYTICS_PREVIEW_FIXTURE": str(LEGACY)},
                clear=True,
            ):
                hook.on_config(config)
                hook.on_post_build(config)
            result = json.loads(
                (Path(folder) / "analytics/data.json").read_text()
            )
            self.assertEqual(result, original)
        page = presentation_tests.PresentationTests().render(original)
        self.assertIn("predates the expanded dashboard", page.get_text())
        self.assertEqual(
            len(page.select(".analytics-breakdown .analytics-panel-empty")), 3
        )

    def test_new_nested_schema_rejects_invalid_or_private_data(self):
        """Reject invalid dates, counts, labels and private fields."""
        mutations = [
            lambda data: data["comparison"]["reporting_period"].update(
                end="2026-08-17"
            ),
            lambda data: data["comparison"]["summary"].update(
                visitor_id="SYNTHETIC"
            ),
            lambda data: data["daily_history"][0].update(date="2026-02-30"),
            lambda data: data["daily_history"][0].update(date="2026-08-16"),
            lambda data: data["daily_history"].reverse(),
            lambda data: data["daily_history"].append(
                data["daily_history"][0]
            ),
            lambda data: data["breakdowns"]["countries"].update(total=1),
            lambda data: data["breakdowns"]["countries"].update(
                minimum_active_users=0
            ),
            lambda data: data["breakdowns"]["countries"]["rows"][0].update(
                label="<script>"
            ),
            lambda data: data["breakdowns"]["countries"]["rows"][0].update(
                active_users=12
            ),
            lambda data: data["breakdowns"]["countries"]["rows"].reverse(),
            lambda data: data["breakdowns"]["countries"].update(
                status="withheld"
            ),
            lambda data: data["breakdowns"]["channels"].update(
                metric="active_users"
            ),
            lambda data: data.update(schema_version=1),
            lambda data: data.pop("comparison"),
        ]
        original = json.loads(FIXTURE.read_text())
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                data = copy.deepcopy(original)
                mutate(data)
                with self.assertRaises((ValueError, ValidationError)):
                    report.validate(data, allow_fixture=True)


class DashboardFormattingTests(unittest.TestCase):
    """Inspect actual markup and derived display values without a browser."""

    def test_comparisons_zero_tiny_and_negative(self):
        """Avoid infinite growth and misleading rounded comparisons."""
        self.assertIn("not available", presentation.change(4, None)["text"])
        self.assertIn(
            "No percentage baseline", presentation.change(4, 0)["text"]
        )
        self.assertEqual(
            presentation.change(4, 8),
            {"text": "50.0% less", "direction": "down"},
        )
        self.assertEqual(presentation.change(8, 8)["text"], "No change")
        self.assertEqual(
            presentation.change(10001, 10000)["text"], "Less than 0.1% change"
        )

    def test_charts_keep_gaps_and_exact_zero(self):
        """Missing dates split lines instead of interpolating data."""
        rows = [
            {"date": "2026-09-01", "pageviews": 0},
            {"date": "2026-09-03", "pageviews": 5},
        ]
        graph = presentation.chart(
            rows, {"start": "2026-09-01", "end": "2026-09-03"}
        )
        self.assertEqual(
            [row["value"] for row in graph["slots"]], [0, None, 5]
        )
        self.assertEqual(len(graph["segments"]), 2)
        self.assertEqual(graph["slots"][0]["y"], 190)
        self.assertEqual(
            [tick["label"] for tick in graph["ticks"]],
            ["0", "2", "4", "6", "8"],
        )

    def test_accessible_controls_and_tables_match_fixture(self):
        """Every visible aggregate has an exact table; no JS is required."""
        fixture = json.loads(FIXTURE.read_text())
        page = presentation_tests.PresentationTests().render(fixture)
        ids = [node["id"] for node in page.select("[id]")]
        self.assertEqual(len(ids), len(set(ids)))
        for control in page.select("[aria-controls]"):
            self.assertIn(control["aria-controls"], ids)
            self.assertFalse(
                page.find(id=control["aria-controls"]).has_attr("hidden")
            )
        self.assertTrue(
            page.select_one("[data-chart-switch]").has_attr("hidden")
        )
        for row, data in zip(
            page.select("#daily-table tbody tr"),
            fixture["daily_history"],
            strict=True,
        ):
            self.assertEqual(row.select_one("time")["datetime"], data["date"])
            self.assertEqual(
                row.select_one("td").get_text(), f'{data["pageviews"]:,}'
            )
        view = presentation.dashboard(fixture)
        for panel in view["panels"]:
            table = page.select_one(
                f'.analytics-breakdown--{panel["key"]} table'
            )
            for row, data in zip(
                table.select("tbody tr"), panel["display_rows"], strict=True
            ):
                self.assertEqual(
                    row.select_one("th").get_text(), data["label"]
                )
                self.assertEqual(
                    [node.get_text() for node in row.select("td")],
                    [f'{data["value"]:,}', data["share_label"]],
                )
        self.assertAlmostEqual(
            sum(row["share"] for row in view["panels"][0]["display_rows"]), 100
        )


if __name__ == "__main__":
    unittest.main()
