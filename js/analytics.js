/* A static, credential-free report explorer. No browser API requests. */
(() => {
  const M = globalThis.OSLAnalytics;
  const source = document.getElementById("analytics-report-data");
  if (!source || !M) return;
  const report = JSON.parse(source.textContent);
  const windows = M.windows(report);
  const refreshed = document.getElementById("analytics-refreshed");
  const stale = document.getElementById("analytics-stale");
  if (refreshed && stale) {
    const update = () => {
      stale.hidden =
        Date.now() - Date.parse(refreshed.dateTime) <= 3 * 86400000;
    };
    update();
    window.setInterval(update, 60000);
    document.addEventListener("visibilitychange", update);
  }
  if (!windows["30"]) return;
  const app = document.querySelector("[data-analytics-report]");
  const $ = (selector) => app.querySelector(selector);
  const $$ = (selector) => [...app.querySelectorAll(selector)];
  const state = {
    window: "30",
    metric: "pageviews",
    section: "overview",
    table: false,
    filters: {},
  };
  const current = () => windows[state.window];
  const otherLabel = (key) =>
    key === "pages" ? "Other public pages" : "Other / unknown";
  const el = (tag, text, cls) => {
    const node = document.createElement(tag);
    if (text != null) node.textContent = text;
    if (cls) node.className = cls;
    return node;
  };
  const rangeLabel = (period) => `${period.start} – ${period.end}`;
  const fullSeries = report.schema_version >= 3;
  const selector = $("#analytics-window");
  [...selector.options].forEach((option) => {
    option.disabled = !windows[option.value];
  });
  if (!fullSeries) {
    $("#analytics-capabilities").hidden = false;
    $("#analytics-capabilities").textContent =
      "Retained 30-day snapshot. A successful new refresh enables 7/90-day reports, all metric trends, chart comparisons and public-page statistics. Missing features are not zero traffic.";
    $("#analytics-compare").checked = false;
    $("#analytics-compare").disabled = true;
  }
  $$("[data-enhance]").forEach((node) => {
    node.hidden = false;
  });
  $$("[data-sort]").forEach((node) => {
    node.disabled = false;
  });
  app.classList.add("analytics-enhanced");

  function navigate(name, focus = false) {
    if (name !== "overview" && !Object.hasOwn(M.dimensions, name)) return;
    state.section = name;
    $$("[data-section]").forEach((node) => {
      node.hidden = node.dataset.section !== name;
    });
    $$("[data-report]").forEach((node) => {
      if (node.dataset.report === name)
        node.setAttribute("aria-current", "page");
      else node.removeAttribute("aria-current");
    });
    $("#analytics-view-title").textContent =
      name === "overview" ? "Reports overview" : M.dimensions[name];
    if (focus) $("#analytics-view-title").focus({ preventScroll: true });
  }
  app.addEventListener("click", (event) => {
    const link = event.target.closest("[data-report]");
    if (!link) return;
    event.preventDefault();
    navigate(link.dataset.report, true);
    history.replaceState(null, "", "#report-" + link.dataset.report);
  });
  window.addEventListener("hashchange", () =>
    navigate(location.hash.replace("#report-", "")),
  );

  function metadataRows(title) {
    return [
      ["OSL-published Google Analytics report", title],
      ["Data kind", report.data_kind],
      ["Site", report.site],
      ["Hostnames", report.hostnames.join(", ")],
      ["Reporting timezone", report.timezone],
      ["Reporting dates", rangeLabel(current().reporting_period)],
      ["Last successful refresh (UTC)", report.generated_at],
    ];
  }
  function download(records, name) {
    const url = URL.createObjectURL(
      new Blob([M.csv(records)], { type: "text/csv;charset=utf-8" }),
    );
    const anchor = el("a");
    anchor.href = url;
    anchor.download = `osl-${name}-${state.window}days.csv`;
    app.append(anchor);
    anchor.click();
    anchor.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function metrics() {
    const data = current();
    $("#analytics-dates").textContent = rangeLabel(data.reporting_period);
    $("#analytics-comparison-dates").textContent = data.comparison
      ? `Compared with ${rangeLabel(
          data.comparison.reporting_period,
        )}. Dates are inclusive. Active users are independently measured for each full period.`
      : "Comparison not available in this snapshot.";
    $$("[data-metric]").forEach((button) => {
      const key = button.dataset.metric;
      button.title = `Show the daily ${M.metrics[
        key
      ].toLowerCase()} trend in Overview`;
      button.disabled =
        !fullSeries && (key !== "pageviews" || !data.daily_history.length);
      button.setAttribute("aria-pressed", String(key === state.metric));
      button.querySelector(".analytics-metric-value").textContent = M.number(
        data.summary[key],
      );
      const previous = data.comparison?.summary[key];
      $(`[data-change="${key}"]`).textContent = `${M.change(
        data.summary[key],
        previous,
      )}${previous == null ? "" : ` · previous ${M.number(previous)}`}`;
    });
    const notices = [];
    if (!data.summary.pageviews)
      notices.push(
        "No measured pageviews for this scope. Check collection and hostname settings before concluding that nobody visited.",
      );
    else if (
      data.daily_history.length &&
      data.daily_history.reduce((sum, row) => sum + row.pageviews, 0) !==
        data.summary.pageviews
    )
      notices.push(
        "Daily and headline pageviews differ. Processing or reporting differences may be responsible; figures have not been adjusted to force a match.",
      );
    $("#analytics-notices").replaceChildren(
      ...notices.map((text) => el("p", text, "analytics-alert")),
    );
  }

  let chartRows = [];
  function chart() {
    const data = current(),
      compare = $("#analytics-compare").checked && fullSeries;
    chartRows = M.series(data, state.metric, compare);
    $("#analytics-trend-title").textContent = `${
      M.metrics[state.metric]
    } over time`;
    $("#analytics-chart-subtitle").textContent =
      state.metric === "active_users"
        ? "Each point is a daily distinct count. Do not add these to obtain the whole-period total."
        : "All website traffic in the selected reporting window · zero-based scale";
    $("#analytics-previous-legend").hidden = !compare;
    const target = $("#analytics-chart");
    target.replaceChildren();
    const svgNS = "http://www.w3.org/2000/svg";
    const svgEl = (tag, attrs, text) => {
      const node = document.createElementNS(svgNS, tag);
      Object.entries(attrs).forEach(([key, value]) =>
        node.setAttribute(key, String(value)),
      );
      if (text != null) node.textContent = text;
      return node;
    };
    const any = chartRows.some(
      (row) => row.value != null || row.previous != null,
    );
    const inspect = $("#analytics-inspect-date");
    inspect.max = String(chartRows.length - 1);
    inspect.value = String(chartRows.length - 1);
    inspect.disabled = !any;
    const tbody = $("#analytics-series-table tbody");
    tbody.replaceChildren();
    const header = el("tr");
    [
      "Date",
      M.metrics[state.metric],
      ...(compare ? ["Previous date", "Previous value"] : []),
    ].forEach((label) => {
      const th = el("th", label);
      th.scope = "col";
      header.append(th);
    });
    $("#analytics-series-table thead").replaceChildren(header);
    $("#analytics-series-table caption").textContent = `Daily ${M.metrics[
      state.metric
    ].toLowerCase()} · ${report.timezone}. Gaps are not reported, not zero.`;
    chartRows.forEach((row) => {
      const tr = el("tr");
      const th = el("th", row.date);
      th.scope = "row";
      tr.append(th, el("td", M.number(row.value)));
      if (compare)
        tr.append(el("td", row.previousDate), el("td", M.number(row.previous)));
      tbody.append(tr);
    });
    if (!any) {
      target.append(
        el(
          "p",
          "Daily history is not available for this metric and window. No values have been inferred.",
          "analytics-empty",
        ),
      );
      $("#analytics-point-detail").textContent = "No reported daily points";
      inspect.oninput = null;
      return;
    }
    // Both periods share one scale and day index. Gaps split lines.
    const values = chartRows
      .flatMap((row) => [row.value, row.previous])
      .filter((value) => value != null);
    const max = Math.max(1, ...values),
      step = 10 ** Math.floor(Math.log10(max));
    const ceiling =
      Math.ceil(Math.max(4, Math.ceil(max / step) * step) / 4) * 4;
    const width = 900,
      height = 290,
      left = 78,
      right = 875,
      top = 24,
      bottom = 245;
    const x = (index) =>
      left + (index * (right - left)) / Math.max(1, chartRows.length - 1);
    const y = (value) => bottom - (value / ceiling) * (bottom - top);
    const svg = svgEl("svg", {
      viewBox: `0 0 ${width} ${height}`,
      "aria-hidden": "true",
      focusable: "false",
    });
    for (let tick = 0; tick <= 4; tick++) {
      const value = (ceiling * tick) / 4;
      svg.append(
        svgEl("line", {
          x1: left,
          x2: right,
          y1: y(value),
          y2: y(value),
          class: "analytics-gridline",
        }),
      );
      svg.append(
        svgEl(
          "text",
          { x: left - 12, y: y(value) + 4, "text-anchor": "end" },
          new Intl.NumberFormat("en", { notation: "compact" }).format(value),
        ),
      );
    }
    [0, Math.floor((chartRows.length - 1) / 2), chartRows.length - 1].forEach(
      (i, labelIndex) =>
        svg.append(
          svgEl(
            "text",
            {
              x: x(i),
              y: 280,
              "text-anchor": ["start", "middle", "end"][labelIndex],
            },
            chartRows[i].date,
          ),
        ),
    );
    function line(key, cls) {
      let points = [];
      const flush = () => {
        if (points.length)
          svg.append(
            svgEl("polyline", { points: points.join(" "), class: cls }),
          );
        points = [];
      };
      chartRows.forEach((row, index) => {
        if (row[key] == null) flush();
        else {
          points.push(`${x(index)},${y(row[key])}`);
          svg.append(
            svgEl("circle", {
              cx: x(index),
              cy: y(row[key]),
              r: 2,
              class: cls + "-point",
            }),
          );
        }
      });
      flush();
    }
    if (compare) line("previous", "analytics-previous-line");
    line("value", "analytics-line");
    const cursor = svgEl("line", {
      x1: right,
      x2: right,
      y1: top,
      y2: bottom,
      class: "analytics-cursor",
    });
    svg.append(cursor);
    function detail(index) {
      const row = chartRows[index];
      cursor.setAttribute("x1", x(index));
      cursor.setAttribute("x2", x(index));
      $("#analytics-point-detail").textContent = `${row.date}: ${M.number(
        row.value,
      )} ${M.metrics[state.metric].toLowerCase()}${
        compare ? ` · ${row.previousDate}: ${M.number(row.previous)}` : ""
      }`;
      inspect.setAttribute(
        "aria-valuetext",
        $("#analytics-point-detail").textContent,
      );
    }
    inspect.oninput = () => detail(Number(inspect.value));
    function inspectPointer(event) {
      const bounds = svg.getBoundingClientRect();
      const relative = ((event.clientX - bounds.left) / bounds.width) * width;
      const index = Math.max(
        0,
        Math.min(
          chartRows.length - 1,
          Math.round(
            ((relative - left) / (right - left)) * (chartRows.length - 1),
          ),
        ),
      );
      inspect.value = String(index);
      detail(index);
    }
    svg.addEventListener("pointermove", inspectPointer);
    svg.addEventListener("pointerdown", inspectPointer);
    target.append(svg);
    detail(chartRows.length - 1);
  }

  function ranking(items, metric) {
    const list = el("ol", null, "analytics-ranking");
    items.forEach((row) => {
      const li = el("li"),
        title = el("div", null, "analytics-ranking-title");
      title.append(el("span", row.label), el("strong", M.number(row.value)));
      const track = el("div", null, "analytics-rank-track");
      track.setAttribute("aria-hidden", "true");
      const bar = el("span");
      bar.style.width = `${row.share}%`;
      track.append(bar);
      li.append(
        title,
        track,
        el("small", `${M.share(row.share)} of ${metric}`),
      );
      list.append(li);
    });
    return list;
  }
  function status(panel) {
    if (!panel)
      return "This retained snapshot does not include this report. A successful new refresh is needed.";
    if (panel.status === "withheld")
      return "Google Analytics restricted this breakdown. No values have been inferred.";
    if (!panel.total)
      return `No measured ${panel.metric} were returned. This does not prove there were no visits.`;
    return `${M.number(panel.total)} ${
      panel.metric
    } returned for this breakdown. Shares use this total, not the headline user count.`;
  }
  function table(key) {
    const panel = current().breakdowns[key],
      filter = state.filters[key] || {
        search: "",
        sort: "value",
        direction: "desc",
      };
    const items = M.rows(
      panel,
      filter.search,
      filter.sort,
      filter.direction,
      otherLabel(key),
    );
    const target = $(`[data-table="${key}"]`),
      body = target.querySelector("tbody");
    body.replaceChildren();
    items.forEach((row) => {
      const tr = el("tr"),
        label = el("th");
      label.scope = "row";
      if (key === "pages" && !row.other) {
        const link = el("a", row.label);
        link.href = row.label;
        label.append(link);
      } else label.textContent = row.label;
      tr.append(
        label,
        el("td", M.number(row.value)),
        el("td", M.share(row.share)),
      );
      body.append(tr);
    });
    if (!items.length) {
      const tr = el("tr"),
        cell = el(
          "td",
          panel?.status === "available"
            ? "No matching categories."
            : "No published rows.",
        );
      cell.colSpan = 3;
      tr.append(cell);
      body.append(tr);
    }
    $(`[data-panel-status="${key}"]`).textContent = `${status(panel)}${
      panel?.status === "available" ? ` Showing ${items.length} rows.` : ""
    }`;
    $$(`[data-panel="${key}"]`).forEach((button) => {
      const active = button.dataset.sort === filter.sort;
      button.parentElement.setAttribute(
        "aria-sort",
        active
          ? filter.direction === "asc"
            ? "ascending"
            : "descending"
          : "none",
      );
      button.textContent = `${
        button.dataset.sort === "label"
          ? "Category"
          : panel?.metric === "sessions"
          ? "Sessions"
          : "Pageviews"
      } ${active ? (filter.direction === "asc" ? "↑" : "↓") : "↕"}`;
    });
    $(`[data-ranking="${key}"]`).replaceChildren(
      ranking(items.slice(0, 5), panel?.metric || "pageviews"),
    );
    $(`[data-export="${key}"]`).disabled = panel?.status !== "available";
    $(`[data-search="${key}"]`).disabled = panel?.status !== "available";
    return items;
  }
  function overview() {
    const grid = $("#analytics-overview-panels");
    grid.replaceChildren();
    Object.entries(M.dimensions).forEach(([key, title]) => {
      const panel = current().breakdowns[key],
        card = el("section", null, "analytics-card analytics-preview");
      const heading = el("div", null, "analytics-card-heading"),
        link = el("a", "View report →");
      link.href = `#report-${key}`;
      link.dataset.report = key;
      heading.append(el("h3", title), link);
      card.append(heading);
      if (panel?.status === "available" && panel.total)
        card.append(
          ranking(
            M.rows(panel, "", "value", "desc", otherLabel(key)).slice(0, 4),
            panel.metric,
          ),
        );
      else card.append(el("p", status(panel), "analytics-empty"));
      grid.append(card);
    });
  }
  function render() {
    metrics();
    chart();
    Object.keys(M.dimensions).forEach(table);
    overview();
  }
  selector.addEventListener("change", () => {
    if (!windows[selector.value]) return;
    state.window = selector.value;
    render();
  });
  $$("[data-metric]").forEach((button) =>
    button.addEventListener("click", () => {
      state.metric = button.dataset.metric;
      navigate("overview");
      history.replaceState(null, "", "#report-overview");
      metrics();
      chart();
    }),
  );
  $("#analytics-compare").addEventListener("change", chart);
  $("#analytics-table-toggle").addEventListener("click", () => {
    state.table = !state.table;
    $("#analytics-series-table").hidden = !state.table;
    $("#analytics-table-toggle").setAttribute(
      "aria-expanded",
      String(state.table),
    );
    $("#analytics-table-toggle").textContent = state.table
      ? "Hide data table"
      : "View data table";
  });
  $("#analytics-series-table").hidden = true;
  $("#analytics-series-csv").addEventListener("click", () => {
    const compare = $("#analytics-compare").checked && fullSeries;
    download(
      [
        ...metadataRows(`Daily ${M.metrics[state.metric]}`),
        [
          "Date",
          M.metrics[state.metric],
          ...(compare ? ["Previous date", "Previous value"] : []),
        ],
        ...chartRows.map((row) => [
          row.date,
          row.value ?? "Not reported",
          ...(compare
            ? [row.previousDate, row.previous ?? "Not reported"]
            : []),
        ]),
      ],
      "daily",
    );
  });
  $$("[data-search]").forEach((input) =>
    input.addEventListener("input", () => {
      const key = input.dataset.search;
      state.filters[key] = {
        ...(state.filters[key] || { sort: "value", direction: "desc" }),
        search: input.value,
      };
      table(key);
    }),
  );
  $$("[data-sort]").forEach((button) =>
    button.addEventListener("click", () => {
      const key = button.dataset.panel,
        old = state.filters[key] || {
          search: "",
          sort: "value",
          direction: "desc",
        };
      state.filters[key] = {
        ...old,
        sort: button.dataset.sort,
        direction:
          old.sort === button.dataset.sort && old.direction === "desc"
            ? "asc"
            : "desc",
      };
      table(key);
    }),
  );
  $$("[data-export]").forEach((button) =>
    button.addEventListener("click", () => {
      const key = button.dataset.export,
        panel = current().breakdowns[key];
      if (panel?.status !== "available") return;
      download(
        [
          ...metadataRows(M.dimensions[key]),
          ["Search", state.filters[key]?.search || ""],
          ["Breakdown total", panel.total],
          ["Category", panel.metric, "Share of full breakdown"],
          ...table(key).map((row) => [
            row.label,
            row.value,
            M.share(row.share),
          ]),
        ],
        key,
      );
    }),
  );
  render();
  const initial = location.hash.startsWith("#report-")
    ? location.hash.slice(8)
    : "overview";
  navigate(
    initial === "overview" || Object.hasOwn(M.dimensions, initial)
      ? initial
      : "overview",
  );
})();
