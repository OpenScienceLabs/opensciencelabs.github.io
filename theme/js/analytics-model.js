/* Pure report operations, shared by the browser and offline Node tests. */
((root) => {
  const metrics = {
    pageviews: "Pageviews",
    active_users: "Active users",
    sessions: "Sessions",
  };
  const dimensions = {
    countries: "Countries",
    devices: "Devices",
    channels: "Acquisition",
    pages: "Pages",
  };
  const number = (value) =>
    value == null ? "Not reported" : new Intl.NumberFormat("en").format(value);
  function dates(period) {
    const values = [];
    for (
      let day = Date.parse(period.start + "T00:00:00Z");
      day <= Date.parse(period.end + "T00:00:00Z");
      day += 86400000
    )
      values.push(new Date(day).toISOString().slice(0, 10));
    return values;
  }
  function windows(report) {
    if (report.status !== "available") return {};
    if (report.windows) return report.windows;
    return {
      30: {
        reporting_period: report.reporting_period,
        summary: report.summary,
        comparison: report.comparison || null,
        daily_history: report.daily_history || [],
        breakdowns: report.breakdowns || {},
      },
    };
  }
  function change(current, previous) {
    if (previous == null) return "No comparison available";
    if (previous === 0) return "No percentage baseline (previously 0)";
    const delta = ((current - previous) / previous) * 100;
    if (!delta) return "No change";
    if (Math.abs(delta) < 0.05) return "Less than 0.1% change";
    return `${delta > 0 ? "+" : "−"}${Math.abs(delta).toFixed(1)}%`;
  }
  function series(window, metric, compare) {
    const current = new Map(
      window.daily_history.map((row) => [row.date, row[metric]]),
    );
    const previous = new Map(
      (window.comparison?.daily_history || []).map((row) => [
        row.date,
        row[metric],
      ]),
    );
    const previousDates = window.comparison
      ? dates(window.comparison.reporting_period)
      : [];
    return dates(window.reporting_period).map((date, i) => ({
      date,
      value: current.get(date) ?? null,
      previousDate: compare ? previousDates[i] : null,
      previous: compare ? previous.get(previousDates[i]) ?? null : null,
    }));
  }
  function rows(
    panel,
    search = "",
    sort = "value",
    direction = "desc",
    otherLabel = "Other / unknown",
  ) {
    if (!panel || panel.status !== "available") return [];
    const values = [
      ...panel.rows,
      { label: otherLabel, value: panel.other, other: true },
    ];
    const query = search.trim().toLocaleLowerCase("en");
    return values
      .filter((row) => row.label.toLocaleLowerCase("en").includes(query))
      .map((row) => ({
        ...row,
        share: panel.total ? (row.value / panel.total) * 100 : 0,
      }))
      .sort((a, b) => {
        const order =
          sort === "label"
            ? a.label.localeCompare(b.label, "en")
            : a.value - b.value;
        return (
          (direction === "asc" ? order : -order) ||
          a.label.localeCompare(b.label, "en")
        );
      });
  }
  function share(value) {
    return value > 0 && value < 0.1 ? "<0.1%" : `${value.toFixed(1)}%`;
  }
  function csv(records) {
    // Quote every cell; neutralize spreadsheet formula injection as well.
    return (
      "\ufeff" +
      records
        .map((row) =>
          row
            .map((value) => {
              let cell = String(value ?? "");
              if (/^[\s]*[=+@-]/u.test(cell) || /^[\t\r\n]/u.test(cell))
                cell = "'" + cell;
              return '"' + cell.replaceAll('"', '""') + '"';
            })
            .join(","),
        )
        .join("\r\n") +
      "\r\n"
    );
  }
  const api = {
    metrics,
    dimensions,
    number,
    dates,
    windows,
    change,
    series,
    rows,
    share,
    csv,
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.OSLAnalytics = api;
})(globalThis);
