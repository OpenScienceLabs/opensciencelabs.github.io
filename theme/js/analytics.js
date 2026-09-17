/* Progressive enhancement only: figures, dates and table are static HTML. */
(() => {
  const switcher = document.querySelector("[data-chart-switch]");
  if (switcher) {
    const buttons = [...switcher.querySelectorAll("[data-chart-target]")];
    const select = (name) => {
      buttons.forEach((button) => {
        const selected = button.dataset.chartTarget === name;
        button.setAttribute("aria-pressed", String(selected));
        document.getElementById(button.getAttribute("aria-controls")).hidden =
          !selected;
      });
    };
    buttons.forEach((button) =>
      button.addEventListener("click", () =>
        select(button.dataset.chartTarget),
      ),
    );
    select(switcher.dataset.defaultChart);
    switcher.hidden = false;
  }
  const refreshed = document.getElementById("analytics-refreshed");
  const notice = document.getElementById("analytics-stale");
  if (!refreshed || !notice) return;
  const generatedAt = Date.parse(refreshed.dateTime);
  if (!Number.isFinite(generatedAt)) return;
  const update = () => {
    notice.hidden = Date.now() - generatedAt <= 3 * 24 * 60 * 60 * 1000;
  };
  update();
  // Also age a page that stays open across the three-day boundary.
  window.setInterval(update, 60 * 1000);
  document.addEventListener("visibilitychange", update);
})();
