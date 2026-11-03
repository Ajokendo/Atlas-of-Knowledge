import { chromium } from "playwright";

const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1365, height: 900 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const response = await page.goto("http://127.0.0.1:4173/biology/chapters/fauna-kyrgyzstan.html", { waitUntil: "networkidle" });
  if (!response?.ok()) throw new Error("Fauna chapter HTTP response was not successful");
  const images = page.locator('img[src*="-chuy-"]');
  const count = await images.count();
  if (count !== 5) throw new Error(`Expected 5 local Chuy fauna and habitat images, found ${count}`);
  for (let i = 0; i < count; i++) {
    const img = images.nth(i);
    await img.evaluate(el => { el.loading = "eager"; el.scrollIntoView(); });
    await img.evaluate(el => el.decode());
    const state = await img.evaluate(el => ({
      src: el.getAttribute("src"),
      naturalWidth: el.naturalWidth,
      naturalHeight: el.naturalHeight,
      alt: el.alt,
      visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length),
    }));
    if (!state.src?.endsWith(".webp") || state.naturalWidth < 1000 || state.naturalHeight < 1000 || !state.alt || !state.visible) {
      throw new Error("Local Chuy fauna image failed browser validation: " + JSON.stringify(state));
    }
    console.log("PASS", JSON.stringify(state));
  }
  if (errors.length) throw new Error("Browser page errors: " + errors.join("; "));
  console.log("Chuy fauna and habitat browser smoke test passed.");
} finally {
  await browser.close();
}
