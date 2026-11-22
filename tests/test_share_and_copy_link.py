"""Test LinkedIn share and Copy Link markup."""

from __future__ import annotations

import unittest

from pathlib import Path

from bs4 import BeautifulSoup


class TestShareAndCopyLinks(unittest.TestCase):
    """Test LinkedIn share and Copy Link in templates and output."""

    def setUp(self) -> None:
        """Set up test paths."""
        self.root = Path(__file__).resolve().parents[1]
        self.theme_dir = self.root / "theme"

    def test_blog_post_template_markup(self) -> None:
        """Verify blog-post.html has correct LinkedIn and Copy Link tags."""
        template_file = self.theme_dir / "blog-post.html"
        self.assertTrue(template_file.exists())
        content = template_file.read_text(encoding="utf-8")

        # Check LinkedIn share URL endpoint
        expected_endpoint = (
            "https://www.linkedin.com/sharing/share-offsite/"
            "?url={{ page.canonical_url or url }}"
        )
        self.assertIn(expected_endpoint, content)
        self.assertNotIn('href="#linkedinshare"', content)

        # Check target and rel
        self.assertIn('target="_blank"', content)
        self.assertIn('rel="nofollow noopener"', content)

        # Check Copy Link button
        self.assertIn('class="link link_yank"', content)
        self.assertIn('href="{{ page.canonical_url or url }}"', content)

    def test_blog_list_template_markup(self) -> None:
        """Verify blog-list.html has correct LinkedIn and Copy Link tags."""
        template_file = self.theme_dir / "blog-list.html"
        self.assertTrue(template_file.exists())
        content = template_file.read_text(encoding="utf-8")

        # Check LinkedIn share URL endpoint
        expected_endpoint = (
            "https://www.linkedin.com/sharing/share-offsite/?url={{ url }}"
        )
        self.assertIn(expected_endpoint, content)
        self.assertNotIn('href="#linkedinshare"', content)

        # Check target and rel
        self.assertIn('target="_blank"', content)
        self.assertIn('rel="nofollow noopener"', content)

        # Check Copy Link button
        self.assertIn('class="link link_yank"', content)
        self.assertIn('href="{{ url }}"', content)

    def test_theme_js_copy_link_handler(self) -> None:
        """Verify theme.js has click handler for .link_yank and feedback."""
        js_file = self.theme_dir / "js" / "theme.js"
        self.assertTrue(js_file.exists())
        content = js_file.read_text(encoding="utf-8")

        self.assertIn(".link_yank", content)
        self.assertIn("preventDefault", content)
        self.assertIn("writeText", content)
        self.assertIn("copy-tooltip", content)
        self.assertIn("Copied!", content)
        self.assertIn("execCommand", content)

    def test_blog_css_copy_link_styles(self) -> None:
        """Verify blog.css styles .link_yank, .copied, and .copy-tooltip."""
        css_file = self.theme_dir / "css" / "blog.css"
        self.assertTrue(css_file.exists())
        content = css_file.read_text(encoding="utf-8")

        self.assertIn(".link_yank", content)
        self.assertIn(".link_yank.copied", content)
        self.assertIn(".copy-tooltip", content)

    def test_rendered_blog_list_html(self) -> None:
        """Verify rendered blog/index.html elements."""
        build_html = self.root / "build" / "blog" / "index.html"
        if not build_html.exists():
            return

        soup = BeautifulSoup(
            build_html.read_text(encoding="utf-8"), "html.parser"
        )
        post_cards = soup.find_all("li", class_="post-card")
        self.assertGreater(len(post_cards), 0)

        for card in post_cards:
            share = card.find("div", class_="post_share")
            self.assertIsNotNone(share)

            # LinkedIn button
            linkedin = share.find("a", class_="linkedin")
            self.assertIsNotNone(linkedin)
            href = linkedin.get("href", "")
            share_prefix = (
                "https://www.linkedin.com/sharing/share-offsite/?url="
            )
            self.assertTrue(
                href.startswith(share_prefix),
                f"Unexpected LinkedIn href: {href}",
            )
            self.assertEqual(linkedin.get("target"), "_blank")
            self.assertEqual(linkedin.get("rel"), ["nofollow", "noopener"])
            self.assertEqual(linkedin.get("title"), "Share on LinkedIn")
            svg_use = linkedin.find("use")
            self.assertIsNotNone(svg_use)
            self.assertEqual(svg_use.get("xlink:href"), "#linkedin")

            # Copy link button
            copy_btn = share.find("a", class_="link_yank")
            self.assertIsNotNone(copy_btn)
            self.assertTrue(bool(copy_btn.get("href")))
            self.assertIn(copy_btn.get("title"), ["Copy link", "Copy Link"])
            copy_svg_use = copy_btn.find("use")
            self.assertIsNotNone(copy_svg_use)
            self.assertEqual(copy_svg_use.get("xlink:href"), "#copy")

    def test_rendered_blog_post_html(self) -> None:
        """Verify rendered blog post pages share panel elements."""
        build_dir = self.root / "build" / "blog"
        if not build_dir.exists():
            return

        for post_html in build_dir.glob("*/index.html"):
            soup = BeautifulSoup(
                post_html.read_text(encoding="utf-8"), "html.parser"
            )
            panel = soup.find("aside", class_="blog-share-panel")
            if not panel:
                continue

            # LinkedIn button
            linkedin = panel.find("a", class_="linkedin")
            self.assertIsNotNone(
                linkedin, f"Missing LinkedIn button in {post_html}"
            )
            href = linkedin.get("href", "")
            share_prefix = (
                "https://www.linkedin.com/sharing/share-offsite/?url="
            )
            self.assertTrue(
                href.startswith(share_prefix),
                f"Unexpected LinkedIn href in {post_html}: {href}",
            )
            self.assertEqual(linkedin.get("target"), "_blank")
            self.assertEqual(linkedin.get("rel"), ["nofollow", "noopener"])
            self.assertEqual(linkedin.get("title"), "Share on LinkedIn")
            svg_use = linkedin.find("use")
            self.assertIsNotNone(svg_use)
            self.assertEqual(svg_use.get("xlink:href"), "#linkedin")

            # Copy link button
            copy_btn = panel.find("a", class_="link_yank")
            self.assertIsNotNone(
                copy_btn, f"Missing Copy link button in {post_html}"
            )
            self.assertTrue(bool(copy_btn.get("href")))
            self.assertEqual(copy_btn.get("title"), "Copy link")
            copy_svg_use = copy_btn.find("use")
            self.assertIsNotNone(copy_svg_use)
            self.assertEqual(copy_svg_use.get("xlink:href"), "#copy")


if __name__ == "__main__":
    unittest.main()
