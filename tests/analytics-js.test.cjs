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
