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
    const images = page.locator("#visuals img");
    const count = await images.count();
    if (count !== 56) errors.push(`${viewport.width}px: expected 56 embeds, found ${count}`);
    const missingAlt = await page.locator("#visuals img:not([alt]), #visuals img[alt='']").count();
    if (missingAlt) errors.push(`${viewport.width}px: ${missingAlt} images lack alt text`);
    const missingSrc = await images.evaluateAll(nodes => nodes.filter(img => !img.getAttribute("src")?.startsWith("https://")).length);
    if (missingSrc) errors.push(`${viewport.width}px: ${missingSrc} images lack HTTPS src`);
    const decoded = await images.evaluateAll(async nodes => {
      await Promise.all(nodes.map(img => { img.loading = "eager"; return img.decode().catch(() => null); }));
      return nodes.filter(img => img.complete && img.naturalWidth > 0).length;
    });
    if (decoded !== 56) errors.push(`${viewport.width}px: only ${decoded}/56 images decoded in Chromium`);
    const overflowImages = await images.evaluateAll(nodes => nodes.filter(img => img.getBoundingClientRect().width > document.documentElement.clientWidth + 1).length);
    if (overflowImages) errors.push(`${viewport.width}px: ${overflowImages} images overflow viewport`);
    const dimensions = await page.evaluate(() => ({ scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth }));
    if (dimensions.scroll > dimensions.client + 1) errors.push(`${viewport.width}px: horizontal page overflow ${dimensions.scroll}>${dimensions.client}`);
    await page.keyboard.press("Tab");
    const focus = await page.evaluate(() => ({ tag: document.activeElement?.tagName, href: document.activeElement?.getAttribute("href") }));
    if (focus.tag !== "A" || focus.href !== "#visuals") errors.push(`${viewport.width}px: skip link is not first keyboard focus target`);
    await page.keyboard.press("Enter");
    if (await page.evaluate(() => location.hash) !== "#visuals") errors.push(`${viewport.width}px: skip link did not navigate to visual section`);
    results.push(`${viewport.width}px: ${count} embeds, alt/HTTPS checks passed, no horizontal overflow, skip link keyboard test passed`);
    await page.close();
  }
} finally { await browser.close(); }
console.log(results.join("\n"));
if (errors.length) { console.error("Browser QA failed:\n" + errors.join("\n")); process.exit(1); }
console.log("PASS: responsive DOM layout, 56/56 real image decodes, alt attributes, HTTPS sources and keyboard skip navigation.");
