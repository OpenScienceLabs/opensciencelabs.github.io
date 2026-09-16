"""Restore the durable gh-pages report; fail closed on retrieval errors."""

import subprocess

from scripts.analytics.report import SNAPSHOT, validate, write_snapshot

MISSING_REF = 2


def git(*args):
    """Run git without a shell, hiding remote diagnostics from public logs."""
    return subprocess.run(
        ["git", *args], capture_output=True, check=False, text=True
    )


def restore(path=SNAPSHOT, run=git):
    """Distinguish first deployments from retrieval errors and corruption."""
    import json

    lookup = run("ls-remote", "--exit-code", "--heads", "origin", "gh-pages")
    if lookup.returncode == MISSING_REF:
        if path.exists():
            raise RuntimeError("Unexpected local snapshot on first deployment")
        return False
    if lookup.returncode:
        raise RuntimeError(
            "Cannot inspect snapshot branch; refusing to deploy"
        )
    fetched = run("fetch", "--no-tags", "--depth=1", "origin", "gh-pages")
    if fetched.returncode:
        raise RuntimeError("Cannot fetch snapshot branch; refusing to deploy")
    listing = run(
        "ls-tree", "--name-only", "FETCH_HEAD", "analytics/data.json"
    )
    if listing.returncode:
        raise RuntimeError("Cannot inspect snapshot tree; refusing to deploy")
    if not listing.stdout.strip():
        if path.exists():
            raise RuntimeError("Unexpected local snapshot without remote copy")
        return False
    blob = run("show", "FETCH_HEAD:analytics/data.json")
    if blob.returncode:
        raise RuntimeError("Cannot read snapshot; refusing to deploy")
    report = json.loads(blob.stdout)
    validate(report)
    write_snapshot(path, report)
    return True


if __name__ == "__main__":
    restored = restore()
    print(
        "Analytics snapshot restored." if restored else "No previous snapshot."
    )
