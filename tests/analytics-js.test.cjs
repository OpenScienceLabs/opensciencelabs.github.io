/* Synthetic data/model/DOM tests. Browser layout is tested separately. */
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const M = require("../theme/js/analytics-model.js");
const setup = require("./analytics-dom.cjs");
const fixture = JSON.parse(
  fs.readFileSync("tests/fixtures/analytics-explorer.json"),
);

test("every preset retains independent whole-period users and dates", () => {
  const windows = M.windows(fixture);
  assert.deepEqual(Object.keys(windows).sort(), ["30", "7", "90"]);
  for (const [days, window] of Object.entries(windows)) {
    assert.equal(M.series(window, "active_users", true).length, Number(days));
    assert.equal(
      window.summary.active_users,
      fixture.windows[days].summary.active_users,
    );
    assert.notEqual(
      window.summary.active_users,
      window.daily_history.reduce((s, r) => s + r.active_users, 0),
    );
    const series = M.series(window, "pageviews", true);
    assert.equal(
      series[0].previousDate,
      window.comparison.reporting_period.start,
    );
    assert.equal(
      series.at(-1).previousDate,
      window.comparison.reporting_period.end,
    );
  }
});
test("missing, zero and absent legacy capabilities stay distinct", () => {
  const window = structuredClone(fixture.windows["7"]);
  window.daily_history[0].pageviews = 0;
  window.daily_history.splice(1, 1);
  const rows = M.series(window, "pageviews", false);
  assert.equal(rows[0].value, 0);
  assert.equal(rows[1].value, null);
  assert.ok(rows.every((row) => row.previous === null));
  const legacy = JSON.parse(
    fs.readFileSync("tests/fixtures/analytics-v1.json"),
  );
  assert.deepEqual(Object.keys(M.windows(legacy)), ["30"]);
  assert.equal(M.windows(legacy)["30"].comparison, null);
  assert.deepEqual(M.windows({ status: "unavailable" }), {});
});
test("sorting, search and shares use published rows and full panel totals", () => {
  const panel = fixture.windows["30"].breakdowns.countries;
  const rows = M.rows(panel, "brazil", "label", "asc");
  assert.equal(rows.length, 1);
  assert.equal(rows[0].label, "Brazil");
  assert.equal(rows[0].share, (panel.rows[0].value / panel.total) * 100);
  assert.deepEqual(M.rows({ status: "withheld" }), []);
  assert.equal(M.rows(panel, "no such country").length, 0);
  assert.ok(M.rows(panel).some((row) => row.other));
  const sorted = M.rows(panel, "", "value", "asc");
  assert.ok(sorted.every((row, i) => !i || sorted[i - 1].value <= row.value));
});
test("CSV quotes cells and neutralizes spreadsheet formulas", () => {
  const csv = M.csv([
    ["=cmd()", "+1", "-1", "@cmd", " \t=cmd", 'a,"b"', "/projects/"],
  ]);
  assert.ok(csv.startsWith("\ufeff"));
  assert.ok(csv.includes('"\'=cmd()"'));
  assert.ok(csv.includes('"\'+1"'));
  assert.ok(csv.includes('"\'-1"'));
  assert.ok(csv.includes('"\'@cmd"'));
  assert.ok(csv.includes('"a,""b"""'));
  assert.ok(csv.includes('"/projects/"'));
});
test("comparison labels do not invent growth from zero or missing baselines", () => {
  assert.match(M.change(2, 0), /No percentage baseline/);
  assert.match(M.change(2, null), /No comparison/);
  assert.equal(M.change(50, 100), "−50.0%");
  assert.equal(M.change(10001, 10000), "Less than 0.1% change");
});
test("actual explorer script switches windows, metrics, reports and tables", async () => {
  const page = setup();
  assert.equal(page.$("#report-overview").hidden, false);
  assert.equal(page.$("#report-countries").hidden, true);
  const selector = page.$("#analytics-window");
  selector.value = "7";
  selector.dispatch("change");
  assert.equal(
    page.$('[data-metric="active_users"] .analytics-metric-value').textContent,
    M.number(fixture.windows["7"].summary.active_users),
  );
  page.$('[data-metric="active_users"]').click();
  assert.equal(
    page.$('[data-metric="active_users"]').getAttribute("aria-pressed"),
    "true",
  );
  assert.equal(
    page.$("#analytics-trend-title").textContent,
    "Active users over time",
  );
  assert.match(page.$("#analytics-chart-subtitle").textContent, /Do not add/);
  page.$("#analytics-table-toggle").click();
  assert.equal(page.$("#analytics-series-table").hidden, false);
  assert.equal(page.$$("#analytics-series-table tbody tr").length, 7);
  const inspect = page.$("#analytics-inspect-date");
  inspect.value = "0";
  inspect.dispatch("input");
  assert.match(
    page.$("#analytics-point-detail").textContent,
    new RegExp(fixture.windows["7"].reporting_period.start),
  );
  const compare = page.$("#analytics-compare");
  compare.checked = false;
  compare.dispatch("change");
  assert.equal(page.$("#analytics-previous-legend").hidden, true);
  assert.equal(page.$$("#analytics-series-table thead th").length, 2);
  page.$('[data-report="countries"]').click();
  assert.equal(page.$("#report-countries").hidden, false);
  assert.equal(page.$("#report-overview").hidden, true);
  const search = page.$('[data-search="countries"]');
  search.value = "Brazil";
  search.dispatch("input");
  assert.equal(page.$$('[data-table="countries"] tbody tr').length, 1);
  page.$('[data-sort="label"][data-panel="countries"]').click();
  assert.equal(
    page
      .$('[data-sort="label"][data-panel="countries"]')
      .parentElement.getAttribute("aria-sort"),
    "descending",
  );
  page.$('[data-export="countries"]').click();
  const csv = await page.blobs[0].text();
  assert.match(csv, /Brazil/);
  assert.match(csv, /fixture/);
  assert.match(csv, /Reporting timezone/);
  assert.doesNotMatch(csv, /United States/);
  search.value = "no such country";
  search.dispatch("input");
  assert.match(
    page.$('[data-table="countries"] tbody').textContent,
    /No matching/,
  );
  selector.value = "90";
  selector.dispatch("change");
  assert.equal(
    page.$('[data-metric="pageviews"] .analytics-metric-value').textContent,
    M.number(fixture.windows["90"].summary.pageviews),
  );
});
test("legacy controls cannot select unqueried periods or metric histories", () => {
  const page = setup("tests/fixtures/analytics.json");
  assert.equal(page.$("#analytics-window").options[0].disabled, true);
  assert.equal(page.$('[data-metric="active_users"]').disabled, true);
  assert.equal(page.$("#analytics-compare").disabled, true);
  assert.equal(page.$('[data-export="pages"]').disabled, true);
  assert.match(
    page.$("#analytics-capabilities").textContent,
    /successful new refresh/,
  );
  const first = setup("tests/fixtures/analytics-v1.json");
  assert.equal(first.$('[data-metric="pageviews"]').disabled, true);
  assert.match(first.$("#analytics-chart").textContent, /not available/);
  assert.equal(setup("unavailable").timers.length, 0);
});
test("staleness updates at the exact three-day boundary and on visibility", () => {
  let now = Date.parse(fixture.generated_at) + 3 * 86400000;
  const notice = {},
    listeners = {},
    timestamp = { dateTime: fixture.generated_at };
  const context = {
    OSLAnalytics: { windows: () => ({}) },
    JSON,
    Date: { now: () => now, parse: Date.parse },
    document: {
      getElementById: (id) =>
        id === "analytics-report-data"
          ? { textContent: JSON.stringify(fixture) }
          : id === "analytics-stale"
          ? notice
          : timestamp,
      addEventListener: (name, fn) => {
        listeners[name] = fn;
      },
    },
    window: {
      setInterval: (fn) => {
        listeners.timer = fn;
      },
    },
  };
  vm.runInNewContext(fs.readFileSync("theme/js/analytics.js", "utf8"), context);
  assert.equal(notice.hidden, true);
  now++;
  listeners.timer();
  assert.equal(notice.hidden, false);
  now--;
  listeners.visibilitychange();
  assert.equal(notice.hidden, true);
});
