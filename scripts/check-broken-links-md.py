import subprocess
import sys
import re
import json
from pathlib import Path
from typing import List, Tuple

# ==== BASIC SETTINGS ====
IGNORE_URLS = ["https://www.linkedin.com/"]  # URLs to skip
RETRY_STATUS = 429  # Too many requests
SCAN_FOLDER = "pages"  # default folder to check
HTTP_MODE = "get"  # request type


# ==== HELPERS ====
def load_whitelist(path: str) -> List[str]:
    """Load extra ignored links from a JSON file (if available)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("[ii] Using default ignore list.")
        return IGNORE_URLS


def run_checker(folder: str, method: str) -> Tuple[int, str]:
    """Run linkcheckmd and capture what it says."""
    try:
        task = subprocess.run(
            ["python", "-m", "linkcheckmd", "-r", "-v", "-m", method, folder],
            capture_output=True,
            text=True,
            check=True,
        )
        return task.returncode, task.stdout
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout + e.stderr


def extract_bad_links(log: str) -> List[Tuple[str, str, int]]:
    """
    Pull out (file, url, status) from linkcheckmd logs.
    """
    regex = re.compile(r"\(([^)]+)\)\s+(https?://[^\s]+)\s+\[status:(\d+)\]")
    found = regex.findall(log)
    return [(f, u, int(s)) for f, u, s in found]


def skip_allowed(links: List[Tuple[str, str, int]], ignore_list: List[str]):
    """Remove whitelisted or rate-limited links."""
    final = []
    for file, url, code in links:
        if any(skip in url for skip in ignore_list):
            continue
        if code == RETRY_STATUS:
            continue
        final.append((file, url, code))
    return final


def print_report(bad_links: List[Tuple[str, str, int]]):
    """Display summary in a friendlier way."""
    if not bad_links:
        print(" Everything looks good! No broken links 🎉")
        return

    print(f"[!!] Found {len(bad_links)} broken link(s):\n")
    for file, url, code in bad_links:
        print(f"- In: {file}\n  → {url}\n  (Status: {code})\n")
    sys.exit(1)


#  MAIN WORK 
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple Markdown link checker.")
    parser.add_argument("-d", "--dir", default=SCAN_FOLDER, help="Folder to check.")
    parser.add_argument(
        "-e", "--exceptions", default="", help="Path to JSON file of links to skip."
    )
    parser.add_argument(
        "-m", "--method", default=HTTP_MODE, help="HTTP method (default: get)."
    )
    args = parser.parse_args()

    whitelist = load_whitelist(args.exceptions)
    code, output = run_checker(args.dir, args.method)

    if code == 0:
        print(" All clear! No broken links reported.")
        return

    bad_links = extract_bad_links(output)
    final_list = skip_allowed(bad_links, whitelist)
    print_report(final_list)


if __name__ == "__main__":
    main()
