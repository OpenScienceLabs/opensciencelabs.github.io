"""Check for broken internal links."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import threading

from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


def start_http_server(folder_path: Path, port: int) -> HTTPServer:
    """Start a local HTTP server to serve files from the folder."""
    os.chdir(folder_path)  # Change to the target directory
    handler = SimpleHTTPRequestHandler
    server = HTTPServer(("localhost", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def check_links(folder_path: Path, port: int):
    """Use wget to check links recursively from the local HTTP server."""
    url = f"http://localhost:{port}/"
    cmd = [
        "wget",
        "--spider",  # Check links without downloading files
        "-r",  # Follow links recursively
        "-nd",  # Don't create a directory structure
        "-nv",  # Less verbose output
        "-l",
        "10",  # Maximum link depth to follow
        url,
    ]

    exitcode = 0
    log_err = ""

    try:
        print(f"[II] Checking links starting from {url}")
        subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except KeyboardInterrupt:
        print("[EE] Interrupted by user.")
        os._exit(1)

    except subprocess.CalledProcessError as e:
        exitcode = e.returncode
        log_err = e.stderr

    if exitcode == 0:
        print("[II] All links are ok.")
        return

    # Check for broken links section in stderr
    flagged_errors = []
    if "Found" in log_err:
        lines = log_err.splitlines()
        start_index = (
            lines.index(
                [line for line in lines if line.startswith("Found")][0]  # noqa: RUF015
            )
            + 2
        )
        for line in lines[start_index:]:
            line = line.strip()  # noqa: PLW2901
            if not line or line.startswith("FINISHED"):
                break
            flagged_errors.append(line)

    # Print flagged errors
    if not flagged_errors:
        print("[II] All links are ok.")
        print("No errors flagged.")
        return

    total_errors = len(flagged_errors)
    print(f"{total_errors} errors flagged for the following URLs:")
    for line in flagged_errors:
        print(line)
    sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check for broken internal links."
    )
    parser.add_argument(
        "--port", "-p", default=8000, type=int, help="Port for HTTP server."
    )
    parser.add_argument(
        "--folder", "-f", default="build", type=str, help="Folder to serve."
    )
    args = parser.parse_args()

    folder_path = Path(args.folder)
    HTTP_PORT = args.port

    if not folder_path.exists():
        print(f"Error: The path {folder_path} doesn't exist.")
        sys.exit(1)

    # Start the HTTP server
    server = start_http_server(folder_path, HTTP_PORT)
    try:
        check_links(folder_path, HTTP_PORT)
    finally:
        server.shutdown()
        print("[II] HTTP server stopped.")
