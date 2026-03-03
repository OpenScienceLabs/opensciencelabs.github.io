"""One-off helper to migrate blog posts to Quarto (.qmd).

This script converts existing blog posts under ``pages/blog`` to ``.qmd``
files so that Quarto can be used as the single canonical source format.

Behaviours:
- For each ``index.ipynb`` notebook, a matching ``index.qmd`` is created
  using ``nbconvert.MarkdownExporter`` (if it does not already exist).
- For each Markdown blog post (``.md``), a ``.qmd`` copy is created with
  the same content (again, if it does not already exist).

Existing ``.qmd`` files are left untouched.

Usage (from the repository root):

    conda activate osl-web
    poetry install
    python scripts/convert-blog-posts-to-qmd.py

After running this script and reviewing the generated ``.qmd`` files, you
can rely on the normal ``makim pages.build`` pipeline, which will render
``.qmd`` files to ``.md`` using Quarto.
"""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbconvert import MarkdownExporter


REPO_ROOT = Path(__file__).resolve().parents[1]
BLOG_ROOT = REPO_ROOT / "pages" / "blog"


def _convert_notebook_to_qmd(ipynb_path: Path) -> None:
    """Convert a single ``.ipynb`` blog post to ``.qmd``."""
    qmd_path = ipynb_path.with_suffix(".qmd")
    if qmd_path.exists():
        print(f"[SKIP] {qmd_path} already exists")
        return

    print(f"[II] Converting notebook -> qmd: {ipynb_path} -> {qmd_path}")
    nb = nbformat.read(ipynb_path, as_version=4)
    exporter = MarkdownExporter()
    body, _ = exporter.from_notebook_node(nb)
    qmd_path.write_text(body, encoding="utf-8")


def _convert_markdown_to_qmd(md_path: Path) -> None:
    """Create a ``.qmd`` copy of an existing Markdown blog post."""
    # Keep the main blog index as Markdown-only.
    if md_path == BLOG_ROOT / "index.md":
        return

    qmd_path = md_path.with_suffix(".qmd")
    if qmd_path.exists():
        print(f"[SKIP] {qmd_path} already exists")
        return

    print(f"[II] Copying markdown -> qmd: {md_path} -> {qmd_path}")
    qmd_path.write_text(md_path.read_text(encoding="utf-8"), encoding="utf-8")


def main() -> None:
    if not BLOG_ROOT.exists():
        raise SystemExit(f"Blog directory not found: {BLOG_ROOT}")

    # 1) Convert all notebooks first
    for ipynb_path in BLOG_ROOT.rglob("*.ipynb"):
        _convert_notebook_to_qmd(ipynb_path)

    # 2) Ensure every Markdown blog post (except the index listing) has a .qmd
    for md_path in BLOG_ROOT.rglob("*.md"):
        _convert_markdown_to_qmd(md_path)

    print("[II] Conversion complete. Review generated .qmd files and commit them.")


if __name__ == "__main__":
    main()

