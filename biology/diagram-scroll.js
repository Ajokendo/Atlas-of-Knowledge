// Keyboard support for horizontally scrollable Biology diagrams.
document.addEventListener("keydown", event => {
  if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
  if (event.altKey || event.ctrlKey || event.metaKey) return;
  const target = event.target;
  if (!(target instanceof Element)) return;
  const viewport = target.closest('[aria-keyshortcuts~="ArrowLeft"][aria-keyshortcuts~="ArrowRight"]');
  if (!viewport) return;
  const maxScroll = viewport.scrollWidth - viewport.clientWidth;
  if (maxScroll <= 1) return;
  const step = Math.max(80, Math.round(viewport.clientWidth * 0.35));
  const direction = event.key === "ArrowRight" ? 1 : -1;
  const next = Math.max(0, Math.min(maxScroll, viewport.scrollLeft + direction * step));
  if (next !== viewport.scrollLeft) {
    viewport.scrollTo({ left: next, behavior: "auto" });
    event.preventDefault();
  }
});
