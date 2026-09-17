/* Synthetic DOM/time tests; no browser or third-party dependencies required. */
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const code = fs.readFileSync("theme/js/analytics.js", "utf8");
const generated = Date.parse("2026-01-01T06:23:00Z");
const threeDays = 3 * 24 * 60 * 60 * 1000;

function run(age, available = true) {
  let now = generated + age;
  const notice = { hidden: false };
  let interval;
  let visibility;
  vm.runInNewContext(code, {
    Date: { parse: Date.parse, now: () => now },
    Number,
    window: {
      setInterval: (fn) => {
        interval = fn;
      },
    },
    document: {
      querySelector: () => null,
      getElementById: (id) =>
        !available
          ? null
          : id === "analytics-stale"
          ? notice
          : { dateTime: new Date(generated).toISOString() },
      addEventListener: (_, fn) => {
        visibility = fn;
      },
    },
  });
  return {
    notice,
    interval,
    visibility,
    setAge: (age) => {
      now = generated + age;
    },
  };
}

test("stale only after three days", () => {
  assert.equal(run(threeDays).notice.hidden, true);
  assert.equal(run(threeDays + 1).notice.hidden, false);
});

test("already open and background tabs age without another deployment", () => {
  const page = run(0);
  page.setAge(threeDays + 1);
  page.interval();
  assert.equal(page.notice.hidden, false);
  page.setAge(0);
  page.visibility();
  assert.equal(page.notice.hidden, true);
});

test("unavailable state needs no timer or refresh date", () => {
  assert.equal(run(0, false).interval, undefined);
});

test("chart switches preserve pressed state and start with available history", () => {
  for (const defaultChart of ["daily", "monthly"]) {
    const panels = { daily: { hidden: false }, monthly: { hidden: false } };
    const buttons = Object.keys(panels).map((name) => ({
      dataset: { chartTarget: name },
      attributes: { "aria-controls": `analytics-${name}` },
      getAttribute(key) {
        return this.attributes[key];
      },
      setAttribute(key, value) {
        this.attributes[key] = value;
      },
      addEventListener(event, fn) {
        this.click = fn;
      },
    }));
    const switcher = {
      hidden: true,
      dataset: { defaultChart },
      querySelectorAll: () => buttons,
    };
    vm.runInNewContext(code, {
      document: {
        querySelector: () => switcher,
        getElementById: (id) => panels[id.replace("analytics-", "")] || null,
      },
    });
    assert.equal(switcher.hidden, false);
    assert.equal(panels[defaultChart].hidden, false);
    buttons[1].click();
    assert.equal(panels.daily.hidden, true);
    assert.equal(panels.monthly.hidden, false);
    assert.equal(buttons[0].attributes["aria-pressed"], "false");
    assert.equal(buttons[1].attributes["aria-pressed"], "true");
    buttons[0].click();
    assert.equal(panels.daily.hidden, false);
    assert.equal(panels.monthly.hidden, true);
  }
});
