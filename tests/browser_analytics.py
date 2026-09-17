"""Optional real-browser checks and local preview screenshots."""

import argparse
import json

from pathlib import Path
from urllib.parse import urlsplit

REQUIRED_MOBILE_WIDTH = 390


def check_chart_controls(page, output, width, mode):
    """Exercise genuine controls, not only the presence of a screenshot."""
    if not page.locator("#analytics-window").count():
        return
    report = json.loads(page.locator("#analytics-report-data").text_content())
    for days in ("7", "30", "90"):
        option = page.locator(f'#analytics-window option[value="{days}"]')
        if option.is_disabled():
            continue
        page.locator("#analytics-window").select_option(days)
        if report.get("windows"):
            window = report["windows"][days]
            for key, value in window["summary"].items():
                text = page.locator(
                    f'[data-metric="{key}"] .analytics-metric-value'
                ).inner_text()
                if text != f"{value:,}":
                    raise AssertionError("Selected period summary mismatch")
        for key in ("pageviews", "active_users", "sessions"):
            button = page.locator(f'[data-metric="{key}"]')
            if button.is_disabled():
                continue
            button.focus()
            page.keyboard.press("Enter")
            if button.get_attribute("aria-pressed") != "true":
                raise AssertionError("Metric selection failed")
        page.locator("#analytics-table-toggle").click()
        if not page.locator("#analytics-series-table table").is_visible():
            raise AssertionError("Daily table is hidden")
        page.locator("#analytics-table-toggle").click()
    page.locator("#analytics-window").select_option("30")
    pageviews = page.locator('[data-metric="pageviews"]')
    if not pageviews.is_disabled():
        pageviews.click()
    page.screenshot(
        path=str(output / f"overview-{width}-{mode}.png"), full_page=True
    )
    check_dimension_controls(page, output, width, mode)


def check_dimension_controls(page, output, width, mode):
    """Inspect report navigation, table search/sort and real CSV downloads."""
    for key in ("countries", "devices", "channels", "pages"):
        page.locator(f'.analytics-sidebar [data-report="{key}"]').click()
        panel = page.locator(f"#report-{key}")
        if not panel.is_visible():
            raise AssertionError("Selected report is hidden")
        search = page.locator(f'[data-search="{key}"]')
        if not search.is_disabled():
            search.fill("no-matching-category-TEST")
            if "No matching categories" not in panel.inner_text():
                raise AssertionError("Table search did not update")
            search.fill("")
            sort = page.locator(f'[data-panel="{key}"][data-sort="label"]')
            sort.click()
            with page.expect_download() as pending:
                page.locator(f'[data-export="{key}"]').click()
            download = pending.value
            if download.failure():
                raise AssertionError("CSV download failed")
            download.save_as(str(output / f"{key}-{width}-{mode}.csv"))
        if page.evaluate(
            "document.documentElement.scrollWidth > innerWidth + 1"
        ):
            raise AssertionError(f"Report overflow: {key}, {width}px")
        page.screenshot(
            path=str(output / f"{key}-{width}-{mode}.png"), full_page=True
        )
    page.locator('.analytics-sidebar [data-report="overview"]').click()


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
                check_chart_controls(page, output, width, mode)
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
        for panel in page.locator("[data-section]").all():
            if not panel.is_visible():
                raise AssertionError("A report requires JavaScript")
            if not panel.locator("table").first.is_visible():
                raise AssertionError("A data table requires JavaScript")
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
