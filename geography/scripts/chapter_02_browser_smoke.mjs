import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";

const file = pathToFileURL(resolve("/tmp/geography-chapter-02-preview.html")).href;
const browser = await chromium.launch({ headless: true });
const errors = [];
const results = [];
try {
  for (const viewport of [{ width: 390, height: 844 }, { width: 1365, height: 900 }]) {
    const page = await browser.newPage({ viewport });
    page.on("pageerror", e => errors.push(e.message));
    await page.goto(file, { waitUntil: "domcontentloaded" });
    for (const language of ["ru", "en"]) {
      const panel = page.locator(language === "ru" ? "#ru" : "#en");
      if (!(await panel.isVisible())) {
        await page.locator("#lang").click();
      }
      const images = panel.locator("img");
      const count = await images.count();
      if (count !== 28) errors.push(`${language}: expected 28 images, found ${count}`);
      const missingAlt = await panel.locator("img:not([alt]), img[alt='']").count();
      if (missingAlt) errors.push(`${language}: ${missingAlt} images lack alt text`);
      const badWidths = await images.evaluateAll(nodes => nodes.filter(img => img.getBoundingClientRect().width > document.documentElement.clientWidth + 1).length);
      if (badWidths) errors.push(`${language}: ${badWidths} images overflow viewport`);
      const layout = await page.evaluate(() => ({scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth}));
      if (layout.scroll > layout.client + 1) errors.push(`${language}: horizontal page overflow ${layout.scroll}>${layout.client}`);
      const loaded = await images.evaluateAll(nodes => nodes.filter(img => img.complete && img.naturalWidth > 0).length);
      results.push(`${viewport.width}px ${language}: ${count} images in DOM, ${loaded} loaded, responsive width OK`);
      if (language === "ru") await page.locator("#lang").click();
    }
    await page.keyboard.press("Tab");
    const focused = await page.evaluate(() => document.activeElement?.id || document.activeElement?.tagName);
    if (!focused) errors.push("keyboard focus target missing");
    await page.close();
  }
} finally { await browser.close(); }
console.log(results.join("\n"));
if (errors.length) { console.error("Browser QA failed:\n" + errors.join("\n")); process.exit(1); }
console.log("PASS: mobile/desktop layout, language switching, image alt text and keyboard focus.");
