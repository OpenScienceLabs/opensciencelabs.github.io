"""Offline synthetic tests; none of these numbers are production statistics."""

from __future__ import annotations

import copy
import json
import os
import tempfile
import unittest

from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace as Obj
from unittest.mock import patch

from jsonschema import Draft202012Validator, ValidationError

from scripts.analytics import export, hook, report, restore
from scripts.analytics.audit import audit

NOW = datetime(2026, 9, 16, 6, 23, tzinfo=timezone.utc)
SETTINGS = export.Settings("123456789", ["opensciencelabs.org"])
FIXTURE = Path(__file__).parent / "fixtures/analytics.json"


def response(metrics, rows, dimensions=(), zone="America/New_York", **meta):
    """Build an SDK-shaped synthetic response, not an API recording."""
    metadata = dict(
        time_zone=zone,
        empty_reason="",
        subject_to_thresholding=False,
        data_loss_from_other_row=False,
        sampling_metadatas=[],
        data_truncation_reasons=[],
        schema_restriction_response=Obj(active_metric_restrictions=[]),
    )
    metadata.update(meta)
    return Obj(
        metadata=Obj(**metadata),
        row_count=len(rows),
        metric_headers=[Obj(name=name) for name in metrics],
        dimension_headers=[Obj(name=name) for name in dimensions],
        rows=[
            Obj(
                dimension_values=[Obj(value=value) for value in dims],
                metric_values=[Obj(value=str(value)) for value in counts],
            )
            for dims, counts in rows
        ],
    )


class FakeClient:
    """Return deterministic fixtures while recording every query."""

    def __init__(self, results=None):
        """Deliberately reorder metrics to test name-based mapping."""
        self.requests = []
        self.results = (
            results
            if results is not None
            else [
                response(["screenPageViews"], [([], [10])]),
                response(
                    ["sessions", "activeUsers", "screenPageViews"],
                    [([], [70, 31, 120])],
                ),
                response(
                    ["screenPageViews"],
                    [(["202608"], [100]), (["202607"], [0])],
                    ["yearMonth"],
                ),
                response(
                    ["sessions", "screenPageViews", "activeUsers"],
                    [([], [55, 90, 25])],
                ),
                response(
                    ["screenPageViews"],
                    [(["20260914"], [70]), (["20260915"], [50])],
                    ["date"],
                ),
                response(
                    ["screenPageViews", "activeUsers"],
                    [(["Brazil"], [90, 20]), (["France"], [30, 5])],
                    ["country"],
                ),
                response(
                    ["screenPageViews", "activeUsers"],
                    [(["desktop"], [100, 20]), (["mobile"], [20, 10])],
                    ["deviceCategory"],
                ),
                response(
                    ["sessions", "activeUsers"],
                    [(["Direct"], [40, 18]), (["Organic Search"], [30, 15])],
                    ["sessionDefaultChannelGroup"],
                ),
            ]
        )

    def run_report(self, *, request):
        """Never contact any remote service."""
        self.requests.append(request)
        result = self.results[len(self.requests) - 1]
        if isinstance(result, Exception):
            raise result
        return result


class DateTests(unittest.TestCase):
    """Calendar boundaries across timezones, leap days and DST."""

    def test_year_boundary_and_local_yesterday(self):
        """At UTC new year, western properties may still be in December."""
        now = datetime(2026, 1, 1, 0, 30, tzinfo=timezone.utc)
        rolling, history = report.periods(now, "America/Los_Angeles")
        self.assertEqual(rolling, {"start": "2025-12-01", "end": "2025-12-30"})
        self.assertEqual(history, {"start": "2024-12-01", "end": "2025-11-30"})
        east, _ = report.periods(now, "Pacific/Kiritimati")
        self.assertEqual(east["end"], "2025-12-31")

    def test_leap_month(self):
        """Use February 29 rather than a fixed month length."""
        rolling, history = report.periods(
            datetime(2024, 3, 1, 12, tzinfo=timezone.utc), "UTC"
        )
        self.assertEqual(rolling, {"start": "2024-01-31", "end": "2024-02-29"})
        self.assertEqual(history["end"], "2024-02-29")
        self.assertEqual(report.month_period("2024-02")["end"], "2024-02-29")

    def test_dst_calendar_days(self):
        """Both daylight-saving transitions preserve exactly 30 dates."""
        for now in [
            datetime(2026, 3, 9, 4, 30, tzinfo=timezone.utc),
            datetime(2026, 11, 2, 5, 30, tzinfo=timezone.utc),
        ]:
            with self.subTest(now=now):
                rolling, _ = report.periods(now, "America/New_York")
                delta = datetime.fromisoformat(
                    rolling["end"]
                ) - datetime.fromisoformat(rolling["start"])
                self.assertEqual(delta.days, 29)
                self.assertEqual(
                    rolling["end"],
                    (now.date() - timedelta(days=1)).isoformat(),
                )

    def test_aware_time_and_valid_timezone_required(self):
        """Never silently use the runner's local timezone."""
        with self.assertRaises(ValueError):
            report.periods(datetime(2026, 1, 1), "UTC")
        with self.assertRaises(KeyError):
            report.periods(NOW, "Not/A_Timezone")

    def test_staleness_strictly_more_than_three_days(self):
        """A failed build cannot advance the successful refresh timestamp."""
        fixture = json.loads(FIXTURE.read_text())
        self.assertFalse(report.is_stale(fixture, NOW + timedelta(days=3)))
        self.assertTrue(
            report.is_stale(fixture, NOW + timedelta(days=3, seconds=1))
        )
        self.assertFalse(report.is_stale(report.unavailable(), NOW))


class ExportTests(unittest.TestCase):
    """Query contracts and failure semantics using synthetic SDK responses."""

    def test_configuration(self):
        """Reject missing property IDs, measurement IDs and unsafe scopes."""
        for env in [
            {},
            {"GA4_PROPERTY_ID": "G-ABC"},
            {"GA4_PROPERTY_ID": "123"},
            {"GA4_PROPERTY_ID": "0", "GA4_HOSTNAMES": "example.org"},
        ]:
            with self.subTest(env=env), self.assertRaises(ValueError):
                export.Settings.from_env(env)
        self.assertEqual(
            report.hostnames("WWW.Example.org, example.org,example.org"),
            ["example.org", "www.example.org"],
        )
        for value in [
            "",
            "localhost",
            "127.0.0.1",
            "*.example.org",
            "https://example.org",
            "example.org/path",
            "example.org:443",
            "preview.localhost",
            "example.org,",
            "foo.test",
            "-a.org",
        ]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                report.hostnames(value)

    def test_hostname_and_web_filter_on_every_query(self):
        """No substrings, previews, apps or implicit www inclusion."""
        client = FakeClient()
        export.collect(client, SETTINGS, NOW)
        for request in client.requests:
            filters = request["dimension_filter"]["and_group"]["expressions"]
            self.assertEqual(filters[0]["filter"]["field_name"], "hostName")
            host_filter = filters[0]["filter"]["in_list_filter"]
            platform_filter = filters[1]["filter"]["string_filter"]
            self.assertFalse(host_filter["case_sensitive"])
            self.assertEqual(platform_filter["match_type"], "EXACT")
            for host, platform, expected in [
                ("opensciencelabs.org", "web", True),
                ("OPENSCIENCELABS.ORG", "Web", True),
                ("preview.opensciencelabs.org", "web", False),
                ("opensciencelabs.org.evil.org", "web", False),
                ("www.opensciencelabs.org", "web", False),
                ("localhost", "web", False),
                ("other.org", "web", False),
                ("opensciencelabs.org", "Android", False),
            ]:
                self.assertEqual(
                    host.lower() in host_filter["values"]
                    and platform.lower() == platform_filter["value"],
                    expected,
                )

    def test_mapping_and_period_level_users(self):
        """Distinct active users come from a dimensionless period query."""
        client = FakeClient()
        result = export.collect(client, SETTINGS, NOW)
        self.assertEqual(
            result["summary"],
            {"pageviews": 120, "active_users": 31, "sessions": 70},
        )
        self.assertEqual(client.requests[1]["dimensions"], [])
        self.assertEqual(
            client.requests[1]["date_ranges"],
            [{"start_date": "2026-08-17", "end_date": "2026-09-15"}],
        )
        self.assertEqual(
            client.requests[2]["metrics"], [{"name": "screenPageViews"}]
        )
        self.assertEqual(
            client.requests[2]["date_ranges"],
            [{"start_date": "2025-09-01", "end_date": "2026-08-31"}],
        )
        self.assertEqual(
            [item["month"] for item in result["monthly_history"]],
            ["2026-07", "2026-08"],
        )
        self.assertEqual(result["monthly_history"][0]["pageviews"], 0)
        self.assertNotIn("property_id", json.dumps(result))

    def test_successful_empty_is_zero_but_history_not_invented(self):
        """An unrestricted empty summary is not an authentication failure."""
        client = FakeClient()
        client.results[1] = response(list(report.METRICS), [])
        client.results[2] = response(["screenPageViews"], [], ["yearMonth"])
        result = export.collect(client, SETTINGS, NOW)
        self.assertEqual(
            result["summary"], dict.fromkeys(report.METRICS.values(), 0)
        )
        self.assertEqual(result["monthly_history"], [])
        self.assertEqual(result["status"], "available")

    def test_failures_preserve_original_bytes_and_timestamp(self):
        """No partial update when any API request or validation fails."""
        failures = [
            RuntimeError("Synthetic API failure"),
            response(list(report.METRICS), [], empty_reason="Unavailable"),
            response(list(report.METRICS), [], subject_to_thresholding=True),
            response(list(report.METRICS), [], data_loss_from_other_row=True),
            response(list(report.METRICS), [], sampling_metadatas=[Obj()]),
            response(
                list(report.METRICS), [], data_truncation_reasons=[Obj()]
            ),
            response(list(report.METRICS), [], zone="UTC"),
            response(["unexpected"], [([], [1])]),
            response(list(report.METRICS), [([], [1, 2, -1])]),
        ]
        original = export.collect(FakeClient(), SETTINGS, NOW)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "snapshot.json"
            report.write_snapshot(path, original)
            before = path.read_bytes()
            for failure in failures:
                with self.subTest(failure=failure):
                    client = FakeClient()
                    client.results[1] = failure
                    with self.assertRaises(Exception):
                        export.refresh(path, client, SETTINGS, NOW)
                    self.assertEqual(path.read_bytes(), before)
            client = FakeClient()
            client.results[2] = RuntimeError(
                "History failed after summary succeeded"
            )
            with self.assertRaises(RuntimeError):
                export.refresh(path, client, SETTINGS, NOW)
            self.assertEqual(path.read_bytes(), before)

    def test_new_success_revises_recent_months(self):
        """Do not freeze prior months while GA4 is still processing."""
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "snapshot.json"
            export.refresh(path, FakeClient(), SETTINGS, NOW)
            client = FakeClient()
            client.results[2].rows[0].metric_values[0].value = "105"
            export.refresh(path, client, SETTINGS, NOW + timedelta(days=1))
            result = report.read_snapshot(path)
            self.assertEqual(result["monthly_history"][-1]["pageviews"], 105)
            self.assertNotEqual(result["generated_at"], NOW.isoformat())

    def test_live_cli_restricted_to_ci_and_missing_configuration(self):
        """Local execution and missing CI configuration never touch a file."""
        trusted = dict(
            GITHUB_ACTIONS="true",
            GITHUB_REPOSITORY=export.REPOSITORY,
            GITHUB_REF="refs/heads/main",
            GITHUB_EVENT_NAME="schedule",
        )
        for env in [
            {},
            trusted,
            {**trusted, "GITHUB_EVENT_NAME": "pull_request"},
        ]:
            with (
                self.subTest(env=env),
                patch.dict("os.environ", env, clear=True),
                patch.object(export, "refresh") as refresh,
            ):
                self.assertEqual(export.main(), 1)
                refresh.assert_not_called()

    def test_sdk_request_compatibility_if_installed(self):
        """Check real protobuf request construction in credential-free CI."""
        try:
            from google.analytics.data_v1beta.types import RunReportRequest
        except ImportError:
            if os.environ.get("CI") == "true":
                raise
            self.skipTest("Google SDK unavailable locally; installed in CI.")
        client = FakeClient()
        export.collect(client, SETTINGS, NOW)
        for request in client.requests:
            parsed = RunReportRequest(request)
            self.assertEqual(parsed.property, "properties/123456789")


class ContractTests(unittest.TestCase):
    """Closed schema and accidental fixture/credential publication defenses."""

    def setUp(self):
        """Start with an explicitly synthetic, versioned report."""
        self.fixture = json.loads(FIXTURE.read_text())

    def test_schema_and_fixture_contract(self):
        """Both a real empty state and labeled fixtures validate."""
        Draft202012Validator.check_schema(
            json.loads(report.SCHEMA.read_text())
        )
        report.validate(report.unavailable())
        report.validate(self.fixture, allow_fixture=True)
        with self.assertRaises(ValueError):
            report.validate(self.fixture)

    def test_extra_fields_and_invalid_values_rejected(self):
        """Only explicitly allowed aggregate fields can reach publication."""
        mutations = [
            lambda data: data.update(access_token="SYNTHETIC"),
            lambda data: data["summary"].update(visitor_id="SYNTHETIC"),
            lambda data: data["summary"].update(pageviews=-1),
            lambda data: data["summary"].update(pageviews=True),
            lambda data: data.update(schema_version=3),
            lambda data: data.update(generated_at="not-a-date"),
            lambda data: data.update(timezone="Invalid/Zone"),
            lambda data: data["reporting_period"].update(end="2026-09-16"),
            lambda data: data["monthly_history"][0].update(start="2025-09-02"),
            lambda data: data["monthly_history"].append(
                data["monthly_history"][0]
            ),
        ]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                data = copy.deepcopy(self.fixture)
                mutate(data)
                with self.assertRaises(
                    (ValueError, ValidationError, KeyError)
                ):
                    report.validate(data, allow_fixture=True)

    def test_absent_and_corrupt_snapshot(self):
        """Corruption must block deployment, not erase previous statistics."""
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            self.assertEqual(
                report.read_snapshot(path)["status"], "unavailable"
            )
            path.write_text("{broken")
            with self.assertRaises(ValueError):
                report.read_snapshot(path)

    def test_hook_emits_same_report_and_blocks_ci_fixtures(self):
        """HTML context and JSON use the identical validated snapshot."""
        with tempfile.TemporaryDirectory() as folder:
            config = Obj(extra={}, site_dir=folder)
            with patch.dict(
                "os.environ",
                {"ANALYTICS_PREVIEW_FIXTURE": str(FIXTURE)},
                clear=True,
            ):
                hook.on_config(config)
                hook.on_post_build(config)
            self.assertEqual(
                json.loads((Path(folder) / "analytics/data.json").read_text()),
                config.extra["analytics_report"],
            )
            with (
                patch.dict(
                    "os.environ",
                    {"CI": "true", "ANALYTICS_PREVIEW_FIXTURE": str(FIXTURE)},
                    clear=True,
                ),
                self.assertRaises(ValueError),
            ):
                hook.on_config(config)

    def test_credential_audit(self):
        """Detect accidentally copied credential files before publishing."""
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            report.write_snapshot(
                directory / "analytics/data.json", report.unavailable()
            )
            audit(directory)
            for name, content in [
                ("gha-creds-test.json", "{}"),
                ("secret.json", '{"type":"external_account"}'),
                ("secret.txt", '{"access_token":"SYNTHETIC"}'),
            ]:
                path = directory / name
                path.write_text(content)
                with self.assertRaises(ValueError):
                    audit(directory)
                path.unlink()
            report.write_snapshot(
                directory / "analytics/data.json",
                self.fixture,
                allow_fixture=True,
            )
            with self.assertRaises(ValueError):
                audit(directory)


class RestoreTests(unittest.TestCase):
    """Durable snapshot retrieval must distinguish missing from failed."""

    def test_restore_and_transport_failures(self):
        """Keep timestamps; abort on unreadable remote state."""
        original = export.collect(FakeClient(), SETTINGS, NOW)
        ok = Obj(returncode=0, stdout="")
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            for results in [
                [Obj(returncode=128, stdout="")],
                [ok, Obj(returncode=128, stdout="")],
                [ok, ok, Obj(returncode=128, stdout="")],
                [
                    ok,
                    ok,
                    Obj(returncode=0, stdout="analytics/data.json"),
                    Obj(returncode=128, stdout=""),
                ],
            ]:
                with (
                    self.subTest(results=results),
                    self.assertRaises(RuntimeError),
                ):
                    restore.restore(
                        path, run=unittest.mock.Mock(side_effect=results)
                    )
                self.assertFalse(path.exists())
            self.assertFalse(
                restore.restore(
                    path,
                    run=unittest.mock.Mock(
                        return_value=Obj(returncode=2, stdout="")
                    ),
                )
            )
            self.assertFalse(
                restore.restore(
                    path, run=unittest.mock.Mock(side_effect=[ok, ok, ok])
                )
            )
            steps = [
                ok,
                ok,
                Obj(returncode=0, stdout="analytics/data.json"),
                Obj(returncode=0, stdout=json.dumps(original)),
            ]
            self.assertTrue(
                restore.restore(
                    path, run=unittest.mock.Mock(side_effect=steps)
                )
            )
            self.assertEqual(report.read_snapshot(path), original)
            before = path.read_bytes()
            steps[-1] = Obj(returncode=0, stdout="{broken")
            with self.assertRaises(ValueError):
                restore.restore(
                    path, run=unittest.mock.Mock(side_effect=steps)
                )
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
