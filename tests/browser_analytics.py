"""Optional real-browser checks and local preview screenshots."""

import argparse
import json

from pathlib import Path
from urllib.parse import urlsplit

REQUIRED_MOBILE_WIDTH = 390


def check(url: str, output: Path) -> None:
    """Inspect responsive color modes without sending synthetic GA traffic."""
    from playwright.sync_api import sync_playwright

    if urlsplit(url).hostname not in {"localhost", "127.0.0.1"}:
        raise ValueError("Use a local preview URL, not the production website")
    output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as engine:
        browser = engine.chromium.launch()
        for width in (1440, REQUIRED_MOBILE_WIDTH, 320):
            for mode, color in (("lit", "light"), ("dim", "dark")):
                context = browser.new_context(
                    viewport={"width": width, "height": 1000},
                    color_scheme=color,
                    is_mobile=width <= REQUIRED_MOBILE_WIDTH,
                    has_touch=width <= REQUIRED_MOBILE_WIDTH,
                )
                context.route(
                    "**/*googletagmanager.com/**", lambda r: r.abort()
                )
                context.route(
                    "**/*google-analytics.com/**", lambda r: r.abort()
                )
                context.add_init_script(
                    "localStorage.setItem('osl-color-mode', "
                    f"{json.dumps(mode)})"
                )
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.goto(url, wait_until="networkidle")
                if page.locator("html").get_attribute("data-mode") != mode:
                    raise AssertionError("Color mode not applied")
                if not page.locator("[data-analytics-report]").is_visible():
                    raise AssertionError("Analytics report missing")
                overflow = page.evaluate(
                    "document.documentElement.scrollWidth > innerWidth + 1"
                )
                if overflow:
                    raise AssertionError(f"Horizontal overflow at {width}px")
                page.locator("a[download]").focus()
                if not page.locator("a[download]").evaluate(
                    "el => el === document.activeElement"
                ):
                    raise AssertionError("Download link is not focusable")
                page.screenshot(
                    path=str(output / f"analytics-{width}-{mode}.png"),
                    full_page=True,
                )
                if errors:
                    raise AssertionError(errors)
                context.close()
        context = browser.new_context(java_script_enabled=False)
        page = context.new_page()
        page.goto(url)
        if not page.locator("[data-analytics-report]").is_visible():
            raise AssertionError("Report requires JavaScript")
        context.close()
        browser.close()
    print(f"Browser smoke checks passed; inspect screenshots in {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "url", nargs="?", default="http://localhost:8000/analytics/"
    )
    parser.add_argument(
        "--output", type=Path, default=Path(".cache/analytics-screenshots")
    )
    args = parser.parse_args()
    check(args.url, args.output)
