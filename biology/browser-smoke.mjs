import { chromium } from "playwright";
import { readdir } from "node:fs/promises";
import path from "node:path";

const root = path.resolve("biology");
const pages = [];
async function walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) await walk(full);
    else if (entry.isFile() && entry.name.endsWith(".html") && entry.name !== "FEEDBACK_WIDGET_TEMPLATE.html") pages.push(path.relative(process.cwd(), full).replaceAll(path.sep, "/"));
  }
}
await walk(root);
const browser = await chromium.launch({ headless: true });
const errors = [];
let languageChecks = 0;
try {
  for (const viewport of [{ width: 390, height: 844 }, { width: 1365, height: 900 }]) {
    const page = await browser.newPage({ viewport });
    let current = "";
    page.on("pageerror", e => errors.push(current + ": " + e.message + " | " + e.stack));
    for (const file of pages) {
      current = file;
      const response = await page.goto("http://127.0.0.1:4173/" + file, { waitUntil: "domcontentloaded" });
      if (!response || !response.ok()) errors.push(file + ": HTTP " + (response?.status() ?? "no response"));
      if (!(await page.locator("main").count())) errors.push(file + ": missing main landmark");
      const lang = page.locator("#lang, #language").first();
      if (await lang.count()) {
        const before = (await lang.innerText()).trim();
        await lang.click();
        const after = (await lang.innerText()).trim();
        if (before === after) errors.push(file + ": language toggle did not change");
        if (file.endsWith("/biochemistry.html")) {
          const controls = await page.locator("#enzyme-controls button, #factor-controls button, #atp-controls button, #respiration-controls button")
            .evaluateAll(elements => elements.map(el => {
              const ru = el.querySelector(".ru"), en = el.querySelector(".en");
              return {
                label: (el.innerText || "").trim(),
                hasBoth: !!ru && !!en,
                activeLanguageVisible: !!en && getComputedStyle(en).display !== "none" && en.getClientRects().length > 0,
                inactiveLanguageHidden: !!ru && (getComputedStyle(ru).display === "none" || ru.getClientRects().length === 0)
              };
            }));
          if (!controls.length || controls.some(x => !x.hasBoth || !x.activeLanguageVisible || !x.inactiveLanguageHidden)) {
            errors.push(file + ": biochemistry model controls do not expose the active English label after language switch");
          }
        }

        if (file.endsWith("/ecology.html")) {
          const selectors = ["#carbon-controls button", "#pressure-controls button"];
          for (const selector of selectors) {
            const controls = await page.locator(selector).evaluateAll(elements => elements.map(el => {
              const ru = el.querySelector(".ru"), en = el.querySelector(".en");
              return {
                hasBoth: !!ru && !!en,
                englishVisible: !!en && getComputedStyle(en).display !== "none" && en.getClientRects().length > 0,
                russianHidden: !!ru && (getComputedStyle(ru).display === "none" || ru.getClientRects().length === 0),
                pressed: el.getAttribute("aria-pressed")
              };
            }));
            if (!controls.length || controls.some(x => !x.hasBoth || !x.englishVisible || !x.russianHidden ||
                !["true", "false"].includes(x.pressed))) {
              errors.push(file + ": " + selector + " controls lack bilingual labels, English visibility or pressed state");
            }
            if (controls.filter(x => x.pressed === "true").length !== 1) {
              errors.push(file + ": " + selector + " must have exactly one initially selected control");
            }
          }
          const carbonChoice = page.locator('#carbon-controls button[data-carbon="respiration"]');
          await carbonChoice.click();
          if (await carbonChoice.getAttribute("aria-pressed") !== "true" ||
              await page.locator('#carbon-controls button[data-carbon="photosynthesis"]').getAttribute("aria-pressed") !== "false") {
            errors.push(file + ": carbon-cycle selection does not update aria-pressed state");
          }
          if (!(await page.locator("#carbon-output").innerText()).startsWith("Cellular respiration:")) {
            errors.push(file + ": carbon-cycle output did not update in English after selection");
          }
        }
        await lang.click();
        languageChecks++;
      } else errors.push(file + ": language switch control not found");
      const missingType = await page.locator("button:not([type='button'])").count();
      if (missingType) errors.push(file + ": " + missingType + " button(s) lack type=button");

      // Catch horizontal overflow at the two representative viewport widths.
      const overflow = await page.evaluate(() => ({
        document: document.documentElement.scrollWidth,
        viewport: document.documentElement.clientWidth,
        body: document.body ? document.body.scrollWidth : 0
      }));
      if (overflow.document > overflow.viewport + 1 || overflow.body > overflow.viewport + 1) {
        errors.push(file + ": horizontal overflow at " + viewport.width + "px (document " +
          overflow.document + "px, body " + overflow.body + "px)");
      }

      // Every visible interactive control should expose a usable accessible name.
      const unnamed = await page.locator("button, a[href], input, select, textarea, [role='button']")
        .evaluateAll(elements => elements.filter(el => {
          const style = getComputedStyle(el);
          const visible = style.display !== "none" && style.visibility !== "hidden" &&
            el.getClientRects().length > 0;
          if (!visible || el.disabled) return false;
          const text = (el.innerText || el.value || "").trim();
          const name = el.getAttribute("aria-label") || el.getAttribute("aria-labelledby") ||
            el.getAttribute("title") || text;
          return !name;
        }).map(el => ({
          tag: el.tagName.toLowerCase(),
          id: el.id || "",
          className: typeof el.className === "string" ? el.className : "",
          html: el.outerHTML.slice(0, 500)
        })));
      if (unnamed.length) errors.push(file + ": " + unnamed.length +
        " visible interactive control(s) lack an accessible name: " + JSON.stringify(unnamed));

      // Confirm keyboard navigation can enter, advance through, and reverse between controls.
      await page.keyboard.press("Tab");
      const firstFocus = await page.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body || el === document.documentElement ||
            !el.matches("a[href], button, input, select, textarea, [tabindex]:not([tabindex='-1'])")) return null;
        return { tag: el.tagName, id: el.id, name: el.getAttribute("aria-label") || el.innerText || el.value || "" };
      });
      if (!firstFocus) {
        errors.push(file + ": Tab key did not reach an interactive control");
      } else {
        await page.keyboard.press("Tab");
        const advanced = await page.evaluate(() => {
          const el = document.activeElement;
          return !!el && el !== document.body && el !== document.documentElement;
        });
        if (!advanced) errors.push(file + ": forward Tab navigation lost focus");
        await page.keyboard.press("Shift+Tab");
        const returnedToFirst = await page.evaluate(first => {
          const el = document.activeElement;
          return !!el && el.tagName === first.tag && el.id === first.id &&
            ((el.getAttribute("aria-label") || el.innerText || el.value || "") === first.name);
        }, firstFocus);
        if (!returnedToFirst) errors.push(file + ": Shift+Tab did not return to the previous control");
      }
    }
    await page.close();
  }
} finally { await browser.close(); }
if (errors.length) {
  console.error("Biology browser smoke tests failed:\\n" + errors.map(x => " - " + x).join("\\n"));
  process.exit(1);
}
console.log("Biology browser smoke tests passed: " + pages.length + " pages at mobile and desktop widths; " + languageChecks + " language-toggle interactions; no uncaught page errors.");
