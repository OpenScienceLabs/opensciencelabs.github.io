"""Check if ther eis any broken links."""

from __future__ import annotations

import subprocess
import sys

# List of exception URLs
exception_urls = [
    "https://www.linkedin.com/",
]


def process_log() -> None:
    """Run the command and capture the output."""
    log_err = ""
    exitcode = 0

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "linkcheckmd",
                "-r",
                "-v",
                "-m",
                "get",
                "pages",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        exitcode = e.returncode
        # for some reason they were swapped
        log_err = e.stdout

    if exitcode == 0:
        print("[II] All links are ok.")
        return

    flagged_errors = []
    for line in log_err.splitlines():
        line = line.strip()  # noqa: PLW2901
        # Check if the line starts with '('
        if not line.startswith("("):
            continue

        if line.endswith("429)") or line.endswith("403)"):
            # Rate limit / forbidden crawler error
            continue

        # Check if URL is in exception list
        if any(exception_url in line for exception_url in exception_urls):
            continue

        flagged_errors.append(line)

    # Print flagged errors
    if not flagged_errors:
        print("[II] All links are ok.", flush=True)
        print(
            "No errors flagged. All URLs are in the exception list.",
            flush=True,
        )
        return

    print("Errors flagged for the following URLs:", flush=True)
    for line in flagged_errors:
        print(line, flush=True)
    sys.exit(1)


# Run the script
if __name__ == "__main__":
    process_log()
