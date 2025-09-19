"""Check for broken links in markdown files."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import traceback

from typing import Dict, List, Optional, Tuple

# Constants
DEFAULT_EXCEPTION_URLS = [
    "https://www.linkedin.com/",
]

STATUS_CODE_429 = "429"
STATUS_CODE_TIMEOUT = "timeout"

# Regex patterns for parsing linkcheckmd output
ERROR_LINE_PATTERN = re.compile(
    r"^\(.*?\)\s*(.+?)\s*\[(\d+|timeout)\]", re.IGNORECASE
)
URL_PATTERN = re.compile(r"https?://[^\s\[\]]+")


class LinkCheckStats:
    """Statistics for link checking results."""

    def __init__(self) -> None:
        self.total_checked = 0
        self.failed_links: List[dict] = []
        self.rate_limited_links: List[dict] = []
        self.whitelisted_links: List[dict] = []
        self.successful_links = 0


def is_url_whitelisted(line: str, exception_urls: List[str]) -> bool:
    """
    Check if any URL in the line is whitelisted.

    Args:
        line: Log line from linkcheckmd
        exception_urls: List of exception URLs to check against

    Returns
    -------
        True if any exception URL is found in the line
    """
    return any(exception_url in line for exception_url in exception_urls)


def parse_error_line(line: str) -> Optional[Dict[str, str]]:
    """
    Parse an error line to extract URL and status code.

    Args:
        line: Error line from linkcheckmd output

    Returns
    -------
        Dictionary with 'url', 'status', and 'full_line' keys,
        or None if parsing fails
    """
    clean_line = line.strip()

    # Try regex pattern first
    match = ERROR_LINE_PATTERN.match(clean_line)
    if match:
        url_part, status = match.groups()
        url_match = URL_PATTERN.search(url_part)
        if url_match:
            return {
                "url": url_match.group(),
                "status": status,
                "full_line": clean_line,
            }

    # Fallback: look for URL and status in brackets
    url_match = URL_PATTERN.search(clean_line)
    status_match = re.search(r"\[(\d+|timeout)\]", clean_line, re.IGNORECASE)

    if url_match and status_match:
        return {
            "url": url_match.group(),
            "status": status_match.group(1),
            "full_line": clean_line,
        }

    return None


def run_linkcheckmd_command(
    args: Optional[List[str]] = None,
) -> Tuple[str, str, int]:
    """
    Run linkcheckmd command and return results.

    Args:
        args: Additional arguments for linkcheckmd

    Returns
    -------
        Tuple of (stdout, stderr, return_code)
    """
    default_args = [
        "python",
        "-m",
        "linkcheckmd",
        "-r",
        "-v",
        "-m",
        "get",
        "pages",
    ]
    if args:
        default_args.extend(args)

    try:
        result = subprocess.run(
            default_args,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=300,  # 5 minute timeout
        )
        return result.stdout, result.stderr, result.returncode

    except subprocess.TimeoutExpired:
        return "", "Command timed out", 1
    except FileNotFoundError:
        return "", "linkcheckmd module not found. Please install it first.", 1
    except Exception as e:
        return "", f"Error running command: {e}", 1


def process_output(
    stdout: str, stderr: str, exception_urls: List[str]
) -> LinkCheckStats:
    """
    Process linkcheckmd output and categorize results.

    Args:
        stdout: Standard output from linkcheckmd
        stderr: Standard error from linkcheckmd
        exception_urls: List of URLs to whitelist

    Returns
    -------
        LinkCheckStats object with categorized results
    """
    stats = LinkCheckStats()

    all_lines = stderr.splitlines() + stdout.splitlines()

    for raw_line in all_lines:
        line = raw_line.strip()
        if not line or not line.startswith("("):
            continue

        stats.total_checked += 1
        parsed = parse_error_line(line)

        if not parsed:
            if any(
                indicator in line.lower()
                for indicator in ["error", "failed", "broken"]
            ):
                if not is_url_whitelisted(line, exception_urls):
                    stats.failed_links.append(
                        {
                            "url": "unknown",
                            "status": "unknown",
                            "full_line": line,
                        }
                    )
            continue

        if is_url_whitelisted(line, exception_urls):
            stats.whitelisted_links.append(parsed)
            continue

        status = parsed["status"].lower()
        if status == STATUS_CODE_429:
            stats.rate_limited_links.append(parsed)
        elif status in ["timeout", "connection"] or not status.startswith("2"):
            stats.failed_links.append(parsed)
        else:
            stats.successful_links += 1

    return stats


def print_results(stats: LinkCheckStats, verbose: bool = False) -> None:
    """
    Print formatted results of the link check.

    Args:
        stats: LinkCheckStats object with results
        verbose: Whether to print verbose output
    """
    print("\n" + "=" * 60)
    print("LINK CHECK RESULTS")
    print("=" * 60)
    print(f"Total links processed: {stats.total_checked}")
    print(f"Successful links: {stats.successful_links}")
    print(f"Failed links: {len(stats.failed_links)}")
    print(f"Rate limited (429): {len(stats.rate_limited_links)}")
    print(f"Whitelisted (skipped): {len(stats.whitelisted_links)}")

    if stats.failed_links:
        print(f"\nFAILED LINKS ({len(stats.failed_links)}):")
        print("-" * 40)
        for link in stats.failed_links:
            print(f"  {link['url']} [Status: {link['status']}]")
            if verbose:
                print(f"    Full line: {link['full_line']}")

    if stats.rate_limited_links:
        print(f"\nRATE LIMITED LINKS ({len(stats.rate_limited_links)}):")
        print("-" * 40)
        for link in stats.rate_limited_links:
            print(f"  {link['url']}")

    if verbose and stats.whitelisted_links:
        print(f"\nWHITELISTED LINKS ({len(stats.whitelisted_links)}):")
        print("-" * 40)
        for link in stats.whitelisted_links:
            print(f"  {link['url']}")


def load_exception_urls_from_file(file_path: str) -> List[str]:
    """
    Load exception URLs from a JSON file.

    Args:
        file_path: Path to JSON file containing exception URLs

    Returns
    -------
        List of exception URLs
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            if isinstance(data, dict) and "exception_urls" in data:
                return data["exception_urls"]
            print(
                f"Warning: Invalid format in {file_path}, "
                "expected list or dict with 'exception_urls' key"
            )
            return []
    except FileNotFoundError:
        print(f"Warning: Exception file {file_path} not found")
        return []
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON in {file_path}: {e}")
        return []


def process_log(
    exception_urls: Optional[List[str]] = None,
    verbose: bool = False,
    extra_args: Optional[List[str]] = None,
) -> None:
    """
    Run the linkcheckmd command and process the results.

    Args:
        exception_urls: List of URLs to whitelist (ignore)
        verbose: Enable verbose output
        extra_args: Additional arguments for linkcheckmd
    """
    if exception_urls is None:
        exception_urls = DEFAULT_EXCEPTION_URLS.copy()

    print(
        f"[INFO] Starting link check with "
        f"{len(exception_urls)} whitelisted URLs..."
    )
    if verbose:
        print(f"[DEBUG] Whitelisted URLs: {exception_urls}")

    stdout, stderr, exitcode = run_linkcheckmd_command(extra_args)

    if exitcode == 0 and not stderr:
        print("[OK] All links are working correctly!")
        return

    if not stdout and not stderr:
        print(
            "[ERROR] linkcheckmd produced no output. "
            "Check if the command is working correctly."
        )
        sys.exit(1)

    stats = process_output(stdout, stderr, exception_urls)
    print_results(stats, verbose)

    if stats.failed_links:
        print(f"\n[ERROR] Found {len(stats.failed_links)} broken links!")
        sys.exit(1)
    if stats.rate_limited_links and not stats.failed_links:
        print(
            "\n[WARNING] All errors were due to rate limiting. "
            "Consider this a warning."
        )
        print("[OK] No actually broken links found!")
    else:
        print(
            f"\n[OK] No broken links found! "
            f"All {stats.total_checked} checked links are working."
        )


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Check for broken links in markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--exceptions-file",
        type=str,
        help="JSON file containing exception URLs to whitelist",
    )
    parser.add_argument(
        "--add-exception",
        action="append",
        help="Add an additional exception URL (can be used multiple times)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "--linkcheckmd-args",
        nargs="*",
        help="Additional arguments to pass to linkcheckmd",
    )
    return parser.parse_args()


def main():
    """Run the command line interface entry point."""
    try:
        args = parse_arguments()

        exception_urls = DEFAULT_EXCEPTION_URLS.copy()
        if args.exceptions_file:
            file_exceptions = load_exception_urls_from_file(
                args.exceptions_file
            )
            exception_urls.extend(file_exceptions)
            print(
                f"[INFO] Loaded {len(file_exceptions)} additional exceptions "
                f"from {args.exceptions_file}"
            )

        if args.add_exception:
            exception_urls.extend(args.add_exception)
            print(
                f"[INFO] Added {len(args.add_exception)} additional "
                "exceptions from command line"
            )

        exception_urls = list(dict.fromkeys(exception_urls))

        process_log(
            exception_urls=exception_urls,
            verbose=args.verbose,
            extra_args=args.linkcheckmd_args,
        )

    except KeyboardInterrupt:
        print("\n[INFO] Link check cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        if "args" in locals() and args.verbose:
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
