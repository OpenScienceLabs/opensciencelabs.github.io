"""Pure, credential-free dashboard formatting; never alters published data."""

import math

from datetime import date, timedelta

from scripts.analytics.report import month_period

PERCENT_PRECISION = 0.1


def change(current, previous):
    """Avoid infinite growth claims when the previous period is zero."""
    if previous is None:
        return {"text": "Comparison not available yet", "direction": "neutral"}
    if previous == 0:
        return {
            "text": "No percentage baseline · previously 0",
            "direction": "neutral",
        }
    percent = (current - previous) / previous * 100
    direction = "up" if percent > 0 else "down" if percent < 0 else "neutral"
    if abs(percent) < PERCENT_PRECISION / 2:
        label = "Less than 0.1% change" if percent else "No change"
    else:
        label = f"{abs(percent):,.1f}% {'more' if percent > 0 else 'less'}"
    return {"text": label, "direction": direction}


def chart(rows, period, *, monthly=False):
    """Draw honest zero-based SVG charts with gaps for unreported dates."""
    key = "month" if monthly else "date"
    lookup = {row[key]: row["pageviews"] for row in rows}
    start = date.fromisoformat(period["start"])
    end = date.fromisoformat(period["end"])
    dates = []
    cursor = start
    while cursor <= end:
        dates.append(
            cursor.strftime("%Y-%m") if monthly else cursor.isoformat()
        )
        cursor = (
            (cursor.replace(day=28) + timedelta(days=4)).replace(day=1)
            if monthly
            else cursor + timedelta(days=1)
        )
    maximum = max(lookup.values(), default=0)
    magnitude = 10 ** math.floor(math.log10(max(maximum, 1)))
    ceiling = max(4, math.ceil(maximum / magnitude) * magnitude)
    ceiling = math.ceil(ceiling / 4) * 4
    # 720x240 viewBox with margins for unambiguous axes. Never smooth curves.
    width, height, left, bottom = 600, 160, 100, 190
    slots, segments, segment = [], [], []
    for index, day in enumerate(dates):
        value = lookup.get(day)
        x = left + (index + 0.5) * width / len(dates)
        y = None if value is None else bottom - value / ceiling * height
        point = {"date": day, "value": value, "x": round(x, 2), "y": y}
        if monthly:
            point.update(month_period(day))
        point["bar_height"] = None if y is None else bottom - y
        slots.append(point)
        if y is None:
            if segment:
                segments.append(" ".join(segment))
            segment = []
        else:
            segment.append(f"{x:.2f},{y:.2f}")
    if segment:
        segments.append(" ".join(segment))
    return {
        "slots": slots,
        "segments": segments,
        "bar_width": min(28, width / len(dates) * 0.6),
        "ticks": [
            {"y": bottom - i * height / 4, "label": f"{ceiling * i / 4:,.0f}"}
            for i in range(5)
        ],
        "first": dates[0],
        "last": dates[-1],
        "has_data": bool(rows),
        "period": period,
    }


def dashboard(report):
    """Prepare derived display values separately from the JSON contract."""
    result = {"metrics": [], "notices": [], "panels": []}
    if report["status"] != "available":
        return result
    comparison = report.get("comparison")
    for key, label, definition in [
        (
            "pageviews",
            "Pageviews",
            "Measured page loads, including repeat views",
        ),
        (
            "active_users",
            "Active users",
            "Distinct active users over all 30 days",
        ),
        (
            "sessions",
            "Sessions",
            "Visits that began during this reporting period",
        ),
    ]:
        previous = comparison["summary"][key] if comparison else None
        result["metrics"].append(
            {
                "key": key,
                "label": label,
                "definition": definition,
                "value": report["summary"][key],
                "previous": previous,
                **change(report["summary"][key], previous),
            }
        )
    result["monthly"] = chart(
        report["monthly_history"], report["history_period"], monthly=True
    )
    result["daily"] = chart(
        report.get("daily_history", []), report["reporting_period"]
    )
    if report["schema_version"] == 1:
        result["notices"].append(
            "This retained report predates the expanded dashboard. Daily "
            "trends, comparisons and audience panels await a successful "
            "refresh."
        )
    if report["summary"]["pageviews"] == 0:
        result["notices"].append(
            "GA4 returned no measured pageviews for this scope. This does not "
            "prove there were no visits; collection and hostname settings "
            "should be checked before interpreting the result."
        )
    elif (
        report["schema_version"] != 1
        and sum(row["pageviews"] for row in report["daily_history"])
        != report["summary"]["pageviews"]
    ):
        result["notices"].append(
            "Daily and headline pageview totals differ in this export. "
            "Processing or reporting differences may be responsible; no "
            "figures have been adjusted to force a match."
        )
    for key, title, description in [
        ("countries", "Where our audience is", "Country-level pageviews"),
        ("devices", "How people visit", "Pageviews by device category"),
        ("channels", "How people find us", "Sessions by acquisition channel"),
    ]:
        panel = (report.get("breakdowns") or {}).get(key)
        item = {"key": key, "title": title, "description": description}
        item.update(panel or {"status": "missing"})
        item["display_rows"] = []
        if panel and panel["status"] == "available":
            rows = panel["rows"] + [
                {"label": "Other / unknown", "value": panel["other"]}
            ]
            for row in rows:
                share = (
                    row["value"] / panel["total"] * 100
                    if panel["total"]
                    else 0
                )
                item["display_rows"].append(
                    {
                        **row,
                        "share": share,
                        "share_label": (
                            "<0.1%"
                            if 0 < share < PERCENT_PRECISION
                            else f"{share:.1f}%"
                        ),
                    }
                )
        result["panels"].append(item)
    return result
