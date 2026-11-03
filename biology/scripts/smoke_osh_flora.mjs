import { chromium } from "playwright";
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1365, height: 900 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const response = await page.goto("http://127.0.0.1:4173/biology/chapters/flora-kyrgyzstan.html", { waitUntil: "networkidle" });
  if (!response?.ok()) throw new Error("Flora chapter HTTP response was not successful");
  const figure = page.locator('figure#image-brief-flora-osh');
  if (await figure.count() !== 1) throw new Error("Expected one Osh flora figure at the original insertion anchor");
  const img = figure.locator("img");
  await img.evaluate(el => { el.loading = "eager"; el.scrollIntoView(); });
  await img.evaluate(el => el.decode());
  const state = await img.evaluate(el => ({
    src: el.getAttribute("src"), width: el.naturalWidth, height: el.naturalHeight,
    alt: el.alt, visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length),
    caption: el.closest("figure")?.querySelector("figcaption")?.innerText || "",
    attribution: el.closest("figure")?.querySelector('a[href="https://commons.wikimedia.org/wiki/File:Inbound1554290775583060652.jpg"]') !== null
  }));
  if (!state.src?.endsWith("flora-osh.webp") || state.width !== 4640 || state.height !== 3472 ||
      Math.abs(state.width / state.height - 4 / 3) > 0.005 || !state.alt.includes("/") || !state.visible || !state.attribution ||
      !state.caption.includes("CC BY-SA 4.0") || !state.caption.includes("Talantbekkyzymalika")) {
    throw new Error("Osh flora image failed browser validation: " + JSON.stringify(state));
  }
  if (errors.length) throw new Error("Browser page errors: " + errors.join("; "));
  console.log("PASS Osh flora image integration", JSON.stringify(state));
} finally {
  await browser.close();
}
