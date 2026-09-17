"""Exercise the real Makim preview CLI without starting a web server."""

import json
import os
import subprocess
import sys
import tempfile
import unittest

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = "tests/fixtures/analytics-explorer.json"
SNAPSHOT = ROOT / ".cache/analytics/data.json"


class PreviewTaskTests(unittest.TestCase):
    """Keep automatic synthetic analytics confined to local preview."""

    def run_preview(self, flags=(), inherited=None):
        """Capture the task's MkDocs invocation, not a mocked YAML render."""
        previous = SNAPSHOT.read_bytes() if SNAPSHOT.exists() else None
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            captured = directory / "invocation.json"
            executable = directory / "mkdocs"
            executable.write_text(
                f"#!{sys.executable}\n"
                "import json, os, pathlib, sys\n"
                "pathlib.Path(os.environ['PREVIEW_TEST_OUTPUT']).write_text("
                "json.dumps({'args': sys.argv[1:], 'fixture': "
                "os.environ.get('ANALYTICS_PREVIEW_FIXTURE')}))\n"
            )
            executable.chmod(0o755)
            env = {
                **os.environ,
                "PATH": f"{directory}{os.pathsep}{os.environ['PATH']}",
                "PREVIEW_TEST_OUTPUT": str(captured),
            }
            env.pop("ANALYTICS_PREVIEW_FIXTURE", None)
            if inherited is not None:
                env["ANALYTICS_PREVIEW_FIXTURE"] = inherited
            result = subprocess.run(
                [sys.executable, "-m", "makim", "pages.preview", *flags],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
            self.assertEqual(
                result.returncode, 0, result.stdout + result.stderr
            )
            invocation = json.loads(captured.read_text())
        current = SNAPSHOT.read_bytes() if SNAPSHOT.exists() else None
        self.assertEqual(current, previous)
        self.assertEqual(
            invocation["args"],
            ["serve", "--watch", "pages", "--watch", "theme"],
        )
        return invocation, result.stdout

    def test_default_enables_labeled_explorer_fixture(self):
        """Select the known preview fixture, not inherited data."""
        for inherited in (None, "not-the-preview-fixture.json"):
            with self.subTest(inherited=inherited):
                invocation, output = self.run_preview(inherited=inherited)
                self.assertEqual(invocation["fixture"], FIXTURE)
                self.assertIn("TEST FIXTURE", output)
        report = json.loads((ROOT / FIXTURE).read_text())
        self.assertEqual(report["data_kind"], "fixture")

    def test_opt_out_clears_even_inherited_fixture(self):
        """The flag delegates to the hook's saved snapshot/unavailable path."""
        for inherited in (None, FIXTURE):
            with self.subTest(inherited=inherited):
                invocation, output = self.run_preview(
                    flags=("--no-analytics-fixture",), inherited=inherited
                )
                self.assertIsNone(invocation["fixture"])
                self.assertIn("saved snapshot", output)
                self.assertNotIn("TEST FIXTURE", output)

    def test_fixture_is_preview_scoped_and_pre_build_still_optional(self):
        """No shared environment or production task opts into test data."""
        config = yaml.safe_load((ROOT / ".makim.yaml").read_text())
        pages = config["groups"]["pages"]
        tasks = pages["tasks"]
        self.assertEqual(
            tasks["preview"]["hooks"]["pre-run"],
            [
                {
                    "task": "pages.pre-build",
                    "if": "${{ args.run_pre_build }}",
                }
            ],
        )
        del tasks["preview"]
        self.assertNotIn("ANALYTICS_PREVIEW_FIXTURE", yaml.safe_dump(config))


if __name__ == "__main__":
    unittest.main()
