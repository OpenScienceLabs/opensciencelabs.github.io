"""Render real analytics templates offline with synthetic reports."""

import json
import unittest

from pathlib import Path
from types import SimpleNamespace as Obj

import yaml

from bs4 import BeautifulSoup
from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader

from scripts.analytics.export import Settings
from scripts.analytics.presentation import dashboard
from scripts.analytics.report import unavailable


class PresentationTests(unittest.TestCase):
    """Static accessibility and data consistency, not browser visual tests."""

    def render(self, report, stale=False):
        """Use the real analytics template while isolating the shared shell."""
        env = Environment(
            loader=ChoiceLoader(
                [
                    DictLoader(
                        {"base.html": "{% block content %}{% endblock %}"}
                    ),
                    FileSystemLoader("theme"),
                ]
            )
        )
        env.filters["url"] = lambda value: "/" + value
        html = env.get_template("analytics.html").render(
            config=Obj(
                extra=Obj(
                    analytics_report=report,
                    analytics_stale=stale,
                    analytics_view=dashboard(report),
                )
            ),
            page=Obj(content=""),
        )
        return BeautifulSoup(html, "html.parser")

    def test_unavailable_has_no_fake_metrics(self):
        """First deployments expose absence, not synthetic numbers."""
        page = self.render(unavailable())
        self.assertIn("Analytics data is not available yet", page.get_text())
        self.assertFalse(page.select(".analytics-metrics"))
        self.assertFalse(page.select("time"))
        self.assertEqual(
            page.select_one("a[download]")["href"], "/analytics/data.json"
        )

    def test_report_table_and_cards_match_json(self):
        """All data remains available without JavaScript or a chart library."""
        fixture = json.loads(Path("tests/fixtures/analytics.json").read_text())
        page = self.render(fixture)
        self.assertIn("TEST FIXTURE", page.get_text())
        self.assertEqual(
            [node.get_text() for node in page.select(".analytics-metrics dd")],
            [f"{value:,}" for value in fixture["summary"].values()],
        )
        rows = page.select("#monthly-table tbody tr")
        self.assertEqual(len(rows), len(fixture["monthly_history"]))
        for node, item in zip(rows, fixture["monthly_history"], strict=True):
            self.assertEqual(
                node.select_one('th[scope="row"]').get_text(), item["month"]
            )
            self.assertIn(f'{item["pageviews"]:,}', node.get_text())
            self.assertEqual(
                [time["datetime"] for time in node.select("td time")],
                [item["start"], item["end"]],
            )
        self.assertIsNotNone(page.select_one("table caption"))
        self.assertEqual(
            len(page.select('#monthly-table thead th[scope="col"]')), 3
        )
        self.assertEqual(
            page.select_one("#analytics-refreshed")["datetime"],
            fixture["generated_at"],
        )
        self.assertTrue(page.select_one("#analytics-stale").has_attr("hidden"))

    def test_zero_chart_and_stale_state(self):
        """Avoid zero division; indicate staleness in text."""
        fixture = json.loads(Path("tests/fixtures/analytics.json").read_text())
        for month in fixture["monthly_history"]:
            month["pageviews"] = 0
        page = self.render(fixture, stale=True)
        bars = page.select(".analytics-bar")
        self.assertEqual(len(bars), 12)
        self.assertTrue(all(float(bar["height"]) == 0 for bar in bars))
        notice = page.select_one("#analytics-stale")
        self.assertFalse(notice.has_attr("hidden"))
        self.assertIn("Stale data", notice.get_text())


class WorkflowTests(unittest.TestCase):
    """Guard the credential-free PR path and scheduled publication wiring."""

    def test_shared_analytics_configuration(self):
        """Use workflow identifiers without repository-variable overrides."""
        workflow_text = Path(".github/workflows/main.yaml").read_text()
        workflow = yaml.load(
            workflow_text,
            Loader=yaml.BaseLoader,
        )
        build = workflow["jobs"]["build"]
        settings = Settings.from_env(build["env"])
        self.assertEqual(settings.property_id, "365530978")
        self.assertEqual(settings.hosts, ["opensciencelabs.org"])
        self.assertEqual(
            build["env"]["GA4_SERVICE_ACCOUNT"],
            "osl-analytics-exporter@osl-general.iam.gserviceaccount.com",
        )
        self.assertEqual(
            build["env"]["GA4_WIF_PROVIDER"],
            "projects/11701823742/locations/global/"
            "workloadIdentityPools/osl-analytics/providers/github",
        )
        self.assertNotIn("GA4_ACCESS_TOKEN", build["env"])
        self.assertNotIn("vars.GA4_", workflow_text)
        self.assertNotIn("secrets.GA4_", workflow_text)
        for step in build["steps"]:
            with self.subTest(step=step.get("name", step.get("uses"))):
                self.assertTrue(
                    build["env"].keys().isdisjoint(step.get("env", {}))
                )

    def test_workflow_safety_contract(self):
        """Cover scheduled and content runs with one deployment lock."""
        workflow = yaml.load(
            Path(".github/workflows/main.yaml").read_text(),
            Loader=yaml.BaseLoader,
        )
        self.assertEqual(workflow["on"]["schedule"][0]["cron"], "23 6 * * *")
        self.assertIn("workflow_dispatch", workflow["on"])
        self.assertIn("osl-production-pages", workflow["concurrency"]["group"])
        self.assertIn(
            "pull_request", workflow["concurrency"]["cancel-in-progress"]
        )
        steps = workflow["jobs"]["build"]["steps"]
        auth = next(step for step in steps if step.get("id") == "google_auth")
        self.assertEqual(
            auth["with"]["service_account"], "${{ env.GA4_SERVICE_ACCOUNT }}"
        )
        self.assertEqual(
            auth["with"]["workload_identity_provider"],
            "${{ env.GA4_WIF_PROVIDER }}",
        )
        self.assertEqual(auth["with"]["create_credentials_file"], "false")
        self.assertEqual(auth["with"]["export_environment_variables"], "false")
        self.assertEqual(
            auth["with"]["access_token_scopes"],
            "https://www.googleapis.com/auth/analytics.readonly",
        )
        restore = next(
            step
            for step in steps
            if step.get("run") == "python -m scripts.analytics.restore"
        )
        self.assertIn("!= 'pull_request'", restore["if"])
        deploy = workflow["jobs"]["deploy"]
        self.assertIn("'schedule'", deploy["if"])
        self.assertIn("refs/heads/main", deploy["if"])
        self.assertIn(
            "actions/deploy-pages@v4",
            [step.get("uses") for step in deploy["steps"]],
        )
        self.assertEqual(deploy["needs"], "build")


if __name__ == "__main__":
    unittest.main()
