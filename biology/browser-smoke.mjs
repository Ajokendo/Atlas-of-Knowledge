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

async function sampleTextContrast(page) {
  return await page.evaluate(() => {
        const parse = value => {
          const m = value.match(/rgba?\(([^)]+)\)/);
          if (!m) return null;
          const parts = m[1].split(",").map(x => Number.parseFloat(x.trim()));
          return { r: parts[0], g: parts[1], b: parts[2], a: parts.length > 3 ? parts[3] : 1 };
        };
        const composite = (fg, bg) => {
          const a = fg.a + bg.a * (1 - fg.a);
          if (!a) return { r: 255, g: 255, b: 255, a: 1 };
          return {
            r: (fg.r * fg.a + bg.r * bg.a * (1 - fg.a)) / a,
            g: (fg.g * fg.a + bg.g * bg.a * (1 - fg.a)) / a,
            b: (fg.b * fg.a + bg.b * bg.a * (1 - fg.a)) / a,
            a
          };
        };
        const luminance = c => {
          const channel = v => {
            v /= 255;
            return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
          };
          return 0.2126 * channel(c.r) + 0.7152 * channel(c.g) + 0.0722 * channel(c.b);
        };
        const ratio = (a, b) => {
          const x = luminance(a), y = luminance(b);
          return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
        };
        const white = { r: 255, g: 255, b: 255, a: 1 };
        const rows = [];
        for (const el of document.querySelectorAll("body *")) {
          const directText = [...el.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim());
          const style = getComputedStyle(el);
          if (!directText || style.display === "none" || style.visibility === "hidden" ||
              Number(style.opacity) === 0 || !el.getClientRects().length) continue;
          const fg = parse(style.color);
          if (!fg) continue;
          let bg = white, node = el;
          while (node && node !== document.documentElement) {
            const s = getComputedStyle(node);
            const candidate = parse(s.backgroundColor);
            if (candidate && candidate.a > 0) {
              bg = composite(candidate, bg);
              if (bg.a >= 0.999) break;
            }
            if (s.backgroundImage && s.backgroundImage !== "none") { bg = null; break; }
            node = node.parentElement;
          }
          if (!bg || bg.a < 0.999) continue;
          const size = Number.parseFloat(style.fontSize) || 16;
          const weight = Number.parseInt(style.fontWeight, 10) || 400;
          const large = size >= 24 || (size >= 18.66 && weight >= 700);
          const measured = ratio(fg, bg);
          rows.push({
            text: (el.innerText || el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 90),
            selector: el.tagName.toLowerCase() + (el.id ? "#" + el.id : "") +
              (typeof el.className === "string" && el.className ? "." + el.className.trim().split(/\s+/).join(".") : ""),
            ratio: Number(measured.toFixed(2)),
            required: large ? 3 : 4.5,
            pass: measured >= (large ? 3 : 4.5)
          });
        }
        return { measured: rows.length, failures: rows.filter(x => !x.pass) };
  });
}
const browser = await chromium.launch({ headless: true });
const errors = [];
let languageChecks = 0;
let contrastSamples = 0;
let contrastFailures = 0;
try {
  for (const viewport of [{ width: 390, height: 844 }, { width: 1365, height: 900 }]) {
    const page = await browser.newPage({ viewport });
    let current = "";
    page.on("pageerror", e => errors.push(current + ": " + e.message + " | " + e.stack));
    for (const file of pages) {
      current = file;
      const response = await page.goto("http://127.0.0.1:4173/" + file, { waitUntil: "domcontentloaded" });
      if (!response || !response.ok()) errors.push(file + ": HTTP " + (response?.status() ?? "no response"));

      // Preliminary WCAG 2.2 contrast sampling for visible, ordinary DOM text.
      // Background images/gradients and translucent layered effects are excluded from this automated pass.
      const contrast = await sampleTextContrast(page);
      contrastSamples += contrast.measured;
      contrastFailures += contrast.failures.length;
      if (contrast.failures.length) {
        errors.push(file + ": preliminary text contrast failures " + JSON.stringify(contrast.failures.slice(0, 8)) +
          (contrast.failures.length > 8 ? " (+" + (contrast.failures.length - 8) + " more)" : ""));
      }
      if (!(await page.locator("main").count())) errors.push(file + ": missing main landmark");
      const lang = page.locator("#lang, #language").first();
      if (await lang.count()) {
        const before = (await lang.innerText()).trim();
        await lang.click();
        const after = (await lang.innerText()).trim();
        const englishContrast = await sampleTextContrast(page);
        contrastSamples += englishContrast.measured;
        contrastFailures += englishContrast.failures.length;
        if (englishContrast.failures.length) {
          errors.push(file + ": English-state contrast failures " + JSON.stringify(englishContrast.failures.slice(0, 8)) +
            (englishContrast.failures.length > 8 ? " (+" + (englishContrast.failures.length - 8) + " more)" : ""));
        }
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
          const photoChoice = page.locator('#carbon-controls button[data-carbon="photosynthesis"]');
          await photoChoice.focus();
          await page.keyboard.press("Space");
          if (await photoChoice.getAttribute("aria-pressed") !== "true" ||
              !(await page.locator("#carbon-output").innerText()).startsWith("Photosynthesis:")) {
            errors.push(file + ": Space key did not activate the photosynthesis control");
          }
          const ecologyStateContrast = await sampleTextContrast(page);
          contrastSamples += ecologyStateContrast.measured;
          contrastFailures += ecologyStateContrast.failures.length;
          if (ecologyStateContrast.failures.length) {
            errors.push(file + ": post-keyboard Ecology state contrast failures " +
              JSON.stringify(ecologyStateContrast.failures.slice(0, 8)));
          }
          const selectedStateContrast = await sampleTextContrast(page);
          contrastSamples += selectedStateContrast.measured;
          contrastFailures += selectedStateContrast.failures.length;
          if (selectedStateContrast.failures.length) {
            errors.push(file + ": selected-control state contrast failures " + JSON.stringify(selectedStateContrast.failures.slice(0, 8)));
          }
        }

        if (file.endsWith("/botany.html")) {
          const answer = page.locator("#answers button").first();
          if (await answer.count()) {
            const beforeAnswer = await page.locator("#result").innerText();
            await answer.focus();
            await page.keyboard.press("Enter");
            const afterAnswer = await page.locator("#result").innerText();
            if (!afterAnswer || afterAnswer === beforeAnswer) {
              errors.push(file + ": Enter key did not activate the first quiz answer");
            }
            const quizStateContrast = await sampleTextContrast(page);
            contrastSamples += quizStateContrast.measured;
            contrastFailures += quizStateContrast.failures.length;
            if (quizStateContrast.failures.length) {
              errors.push(file + ": post-quiz state contrast failures " +
                JSON.stringify(quizStateContrast.failures.slice(0, 8)));
            }
            const feedbackStateContrast = await sampleTextContrast(page);
            contrastSamples += feedbackStateContrast.measured;
            contrastFailures += feedbackStateContrast.failures.length;
            if (feedbackStateContrast.failures.length) {
              errors.push(file + ": quiz-feedback state contrast failures " + JSON.stringify(feedbackStateContrast.failures.slice(0, 8)));
            }
          } else {
            errors.push(file + ": quiz answer control not found for keyboard activation test");
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

      // Check practical accessible-name sources, including native <label> associations
      // and valid aria-labelledby references (rather than treating the attribute itself as a name).
      const nameIssues = await page.locator("button, a[href], input, select, textarea, [role='button']")
        .evaluateAll(elements => {
          const visible = el => {
            const style = getComputedStyle(el);
            return style.display !== "none" && style.visibility !== "hidden" &&
              el.getClientRects().length > 0;
          };
          const textOf = el => (el.innerText || el.textContent || "").trim();
          return elements.filter(el => visible(el) && !el.disabled).flatMap(el => {
            const issues = [];
            const labelledby = (el.getAttribute("aria-labelledby") || "").trim();
            const referencedText = labelledby ? labelledby.split(/\s+/)
              .map(id => document.getElementById(id)).filter(Boolean).map(textOf).filter(Boolean).join(" ").trim() : "";
            const ariaLabel = (el.getAttribute("aria-label") || "").trim();
            const nativeLabels = el.labels ? Array.from(el.labels).map(textOf).filter(Boolean).join(" ").trim() : "";
            const nestedImageAlt = Array.from(el.querySelectorAll("img[alt]"))
              .map(img => (img.getAttribute("alt") || "").trim()).filter(Boolean).join(" ").trim();
            const imageInputAlt = el.tagName === "INPUT" && el.type === "image"
              ? (el.getAttribute("alt") || "").trim() : "";
            const valueName = el.tagName === "INPUT" && /^(button|submit|reset)$/i.test(el.type)
              ? (el.value || "").trim() : "";
            const title = (el.getAttribute("title") || "").trim();
            const content = textOf(el);
            const hasName = !!(referencedText || ariaLabel || nativeLabels ||
              nestedImageAlt || imageInputAlt || valueName || content || title);
            if (!hasName) issues.push("no usable accessible name");
            if (labelledby && !referencedText) issues.push("aria-labelledby has no resolvable non-empty text");
            if (el.getAttribute("aria-label") !== null && !ariaLabel) issues.push("aria-label is empty");
            if (el.getAttribute("role") === "button" &&
                !/^(BUTTON|INPUT)$/i.test(el.tagName) && el.tabIndex < 0) {
              issues.push("custom role=button is not keyboard focusable");
            }
            return issues.length ? [{
              tag: el.tagName.toLowerCase(), id: el.id || "",
              className: typeof el.className === "string" ? el.className : "",
              issues, html: el.outerHTML.slice(0, 500)
            }] : [];
          });
        });
      if (nameIssues.length) errors.push(file + ": " + nameIssues.length +
        " visible interactive control(s) have accessible-name/keyboard-semantics issues: " +
        JSON.stringify(nameIssues));

      // Compare the complete in-page Tab sequence with the visible, enabled DOM focus order.
      // Temporary probe attributes identify actual focused nodes without relying on CSS-selector reconstruction.
      const expectedTabOrder = await page.locator(
        "a[href], area[href], button, input:not([type='hidden']), select, textarea, iframe, object, embed, summary, audio[controls], video[controls], [contenteditable='true'], [tabindex]"
      ).evaluateAll(elements => {
        const candidates = elements.filter(el => {
          const style = getComputedStyle(el);
          return style.display !== "none" && style.visibility !== "hidden" &&
            style.visibility !== "collapse" && el.getClientRects().length > 0 &&
            !el.disabled && !el.closest("[inert]") && el.tabIndex >= 0;
        });
        const radios = new Map();
        const filtered = candidates.filter(el => {
          if (el.tagName !== "INPUT" || el.type !== "radio" || !el.name) return true;
          const key = (el.form ? "form-" + Array.from(document.forms).indexOf(el.form) : "no-form") + ":" + el.name;
          if (!radios.has(key)) radios.set(key, []);
          radios.get(key).push(el);
          return true;
        });
        const radioSkip = new Set();
        for (const group of radios.values()) {
          if (group.length > 1) {
            const stop = group.find(el => el.checked) || group[0];
            for (const el of group) if (el !== stop) radioSkip.add(el);
          }
        }
        const ordered = filtered.filter(el => !radioSkip.has(el)).map((el, domIndex) => ({
          el, domIndex, tabIndex: el.tabIndex
        })).sort((a, b) => {
          const ap = a.tabIndex > 0, bp = b.tabIndex > 0;
          if (ap && bp) return a.tabIndex - b.tabIndex || a.domIndex - b.domIndex;
          if (ap) return -1;
          if (bp) return 1;
          return a.domIndex - b.domIndex;
        });
        return ordered.map((item, index) => {
          item.el.setAttribute("data-a11y-tab-probe", String(index));
          return {
            index, tag: item.el.tagName.toLowerCase(), id: item.el.id || "",
            name: (item.el.getAttribute("aria-label") || item.el.innerText ||
              item.el.value || item.el.getAttribute("title") || "").trim()
          };
        });
      });
      await page.evaluate(() => {
        if (document.activeElement && document.activeElement !== document.body) document.activeElement.blur();
        const sentinel = document.createElement("button");
        sentinel.type = "button";
        sentinel.tabIndex = -1;
        sentinel.setAttribute("aria-hidden", "true");
        sentinel.setAttribute("data-a11y-tab-sentinel", "true");
        sentinel.style.cssText = "position:fixed;left:-10000px;top:0;width:1px;height:1px;";
        document.body.prepend(sentinel);
        sentinel.focus();
      });
      for (const expected of expectedTabOrder) {
        await page.keyboard.press("Tab");
        const actual = await page.evaluate(() =>
          document.activeElement && document.activeElement.getAttribute("data-a11y-tab-probe"));
        if (actual !== String(expected.index)) {
          errors.push(file + ": Tab order mismatch at position " + expected.index +
            " (expected " + expected.tag + "#" + expected.id + " '" + expected.name +
            "', focused probe was " + actual + "; expected sequence length " + expectedTabOrder.length + ")");
          break;
        }
      }

      await page.evaluate(() => {
        const sentinel = document.querySelector("[data-a11y-tab-sentinel]");
        if (sentinel) sentinel.remove();
        if (document.activeElement && document.activeElement !== document.body) document.activeElement.blur();
      });

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
        const focusIndicator = await page.evaluate(() => {
          const s = getComputedStyle(document.activeElement);
          return (s.outlineStyle !== "none" && Number.parseFloat(s.outlineWidth) > 0) ||
            s.boxShadow !== "none" || s.filter !== "none";
        });
        if (!focusIndicator) errors.push(file + ": first keyboard-focused control has no detectable focus indicator");
        const focusedContrast = await sampleTextContrast(page);
        contrastSamples += focusedContrast.measured;
        contrastFailures += focusedContrast.failures.length;
        if (focusedContrast.failures.length) {
          errors.push(file + ": keyboard-focus-state contrast failures " + JSON.stringify(focusedContrast.failures.slice(0, 8)));
        }
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
console.log("Biology browser smoke tests passed: " + pages.length + " pages at mobile and desktop widths; " + languageChecks + " language-toggle interactions; no uncaught page errors. Preliminary contrast sampling: " + contrastSamples + " text instances, " + contrastFailures + " below-threshold instances; first keyboard focus indicator checked.");
