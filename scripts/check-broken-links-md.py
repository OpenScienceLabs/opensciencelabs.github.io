"""Check if there is any broken links."""

from __future__ import annotations

import subprocess
import sys

# List of exception URLs (known to block crawlers/bots)
exception_urls = [
    "https://www.linkedin.com/",
    "https://twitter.com/",
    "https://x.com/",
]

MIN_HTTP_SUCCESS = 200
MAX_HTTP_REDIRECT = 400

# HTTP status codes for bot-blocking, rate limiting, or server issues
ignored_status_codes = {
    400,
    401,
    403,
    405,
    406,
    429,
    500,
    502,
    503,
    504,
    999,
}


def is_error(line: str) -> bool:
    """Determine if a linkcheckmd log line represents a real broken link."""
    line = line.strip()
    if not line.startswith("("):
        return False

    if any(exc in line for exc in exception_urls):
        return False

    # Try extracting the status code from the end of the tuple
    try:
        code_str = line.rstrip(")").rsplit(",", 1)[-1].strip()
        code = int(code_str)
        # 2xx (Success) and 3xx (Redirection) are valid HTTP responses
        if MIN_HTTP_SUCCESS <= code < MAX_HTTP_REDIRECT:
            return False
        if code in ignored_status_codes:
            return False
    except ValueError:
        pass

    return True


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
        log_err = (e.stdout or "") + "\n" + (e.stderr or "")

    if exitcode == 0:
        print("[II] All links are ok.")
        return

    flagged_errors = []
    for line in log_err.splitlines():
        if is_error(line):
            flagged_errors.append(line.strip())

    # Print flagged errors
    if not flagged_errors:
        print("[II] All links are ok.")
        print("No errors flagged. All URLs are in the exception list.")
        return

    print("Errors flagged for the following URLs:", flush=True)
    for line in flagged_errors:
        print(line, flush=True)
    sys.exit(1)


# Run the script
if __name__ == "__main__":
    process_log()
