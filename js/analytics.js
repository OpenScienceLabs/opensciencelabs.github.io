/* Progressive enhancement only: figures, dates and table are static HTML. */
(() => {
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
