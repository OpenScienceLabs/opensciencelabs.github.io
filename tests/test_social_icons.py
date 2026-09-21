"""Test social icons including Bluesky icon in templates and pages."""

from __future__ import annotations

import unittest

from pathlib import Path

from bs4 import BeautifulSoup


class TestSocialIcons(unittest.TestCase):
    """Test social icons definition and usage."""

    def setUp(self) -> None:
        """Set up paths."""
        self.root = Path(__file__).resolve().parents[1]
        self.theme_dir = self.root / "theme"
        self.sprites_file = self.theme_dir / "icons" / "sprites.svg"
        self.partners_template = self.theme_dir / "partners.html"
        self.base_template = self.theme_dir / "base.html"

    def test_bluesky_symbol_in_sprites(self) -> None:
        """Verify bluesky symbol is defined in sprites.svg."""
        self.assertTrue(self.sprites_file.exists())
        content = self.sprites_file.read_text(encoding="utf-8")

        soup = BeautifulSoup(content, "html.parser")
        symbol = soup.find("symbol", id="bluesky")
        self.assertIsNotNone(
            symbol, "symbol with id='bluesky' must be present in sprites.svg"
        )
        self.assertEqual(symbol.get("viewbox"), "0 0 24 24")

        path = symbol.find("path")
        self.assertIsNotNone(path, "bluesky symbol must contain a path")
        self.assertTrue(
            len(path.get("d", "")) > 0,
            "bluesky path 'd' attribute must not be empty",
        )

    def test_sprites_included_in_base_template(self) -> None:
        """Verify sprites.svg is included in theme/base.html."""
        content = self.base_template.read_text(encoding="utf-8")
        self.assertIn('{% include "icons/sprites.svg" %}', content)

    def test_partners_template_renders_bluesky(self) -> None:
        """Verify theme/partners.html includes bluesky icon link."""
        content = self.partners_template.read_text(encoding="utf-8")
        self.assertIn("'bluesky' in partner", content)
        self.assertIn('xlink:href="#bluesky"', content)

    def test_rendered_partners_page(self) -> None:
        """Verify rendered partners HTML has bluesky symbol and links."""
        partners_html = (
            self.root / "build" / "partnership" / "partners" / "index.html"
        )
        if not partners_html.exists():
            return

        soup = BeautifulSoup(
            partners_html.read_text(encoding="utf-8"), "html.parser"
        )

        # 1. bluesky symbol must be present in the document
        bluesky_symbol = soup.find("symbol", id="bluesky")
        self.assertIsNotNone(
            bluesky_symbol,
            "Rendered partners page must contain <symbol id='bluesky'> in DOM",
        )

        # 2. Check pyOpenSci partner card has bluesky link
        pyopensci_bsky = soup.find(
            "a", href="https://bsky.app/profile/pyopensci.bsky.social"
        )
        self.assertIsNotNone(
            pyopensci_bsky, "pyOpenSci Bluesky link must be present"
        )
        self.assertEqual(pyopensci_bsky.get("aria-label"), "Bluesky")

        use_tag = pyopensci_bsky.find("use")
        self.assertIsNotNone(
            use_tag, "Bluesky link must contain <use> SVG tag"
        )
        href = use_tag.get("xlink:href") or use_tag.get("href")
        self.assertEqual(href, "#bluesky")

        # 3. All <use> references should have matching <symbol> or element id
        all_symbols = {
            s.get("id") for s in soup.find_all("symbol") if s.get("id")
        }
        for use in soup.find_all("use"):
            target = use.get("xlink:href") or use.get("href")
            if target and target.startswith("#"):
                target_id = target[1:]
                self.assertTrue(
                    target_id in all_symbols
                    or soup.find(id=target_id) is not None,
                    f"Referenced symbol #{target_id} not found in DOM",
                )
