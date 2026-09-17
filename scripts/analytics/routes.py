"""Derive the analytics page-path allowlist from public MkDocs documents."""

import re

from mkdocs.config import load_config
from mkdocs.structure.files import get_files

from scripts.analytics.report import ROOT

PUBLIC_PATH = re.compile(r"/(?:[A-Za-z0-9_-]+/)*(?:[A-Za-z0-9_-]+\.html)?")
MAX_PUBLIC_ROUTES = 500
MAX_ROUTE_LENGTH = 240


def public_routes(config_path=ROOT / "mkdocs.yml"):
    """Use MkDocs URL rules, excluding hidden/non-document and excluded files.

    Only canonical routes are accepted. No query strings, aliases, visitor
    paths, URLs or page titles from Google are added to the allowlist.
    """
    config = load_config(str(config_path))
    routes = set()
    for file in get_files(config).documentation_pages():
        inclusion = getattr(file, "inclusion", None)
        if inclusion is not None and inclusion.is_excluded():
            continue
        route = "/" if file.url == "./" else "/" + file.url
        if len(route) <= MAX_ROUTE_LENGTH and PUBLIC_PATH.fullmatch(route):
            routes.add(route)
    if not routes or len(routes) > MAX_PUBLIC_ROUTES:
        raise ValueError("Missing or excessive public route allowlist")
    return sorted(routes)
