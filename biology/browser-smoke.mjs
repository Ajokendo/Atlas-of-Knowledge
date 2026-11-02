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

      await page.addScriptTag({ path: path.resolve("node_modules/axe-core/axe.min.js") });
      const runAxeAudit = async (languageState) => {
        const violations = await page.evaluate(async () => {
          const result = await window.axe.run(document, {
            runOnly: {
              type: "tag",
              values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"]
            }
          });
          return result.violations.map(v => ({
            id: v.id,
            impact: v.impact,
            help: v.help,
            nodes: v.nodes.slice(0, 8).map(n => ({
              target: n.target,
              summary: n.failureSummary
            }))
          }));
        });
        if (violations.length) {
          errors.push(file + ": axe WCAG audit (" + languageState + ") found " +
            violations.length + " violation type(s): " + JSON.stringify(violations));
        }
      };
      await runAxeAudit("initial language");

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
      if (await page.locator("main").count() !== 1) errors.push(file + ": expected exactly one main landmark");
      if ((await page.locator("h1").count()) !== 1) errors.push(file + ": expected exactly one top-level h1 heading");
      if (!(await page.title()).trim()) errors.push(file + ": document title is empty");
      const headingSequence = await page.locator("h1, h2, h3, h4, h5, h6").evaluateAll(nodes =>
        nodes.map(el => Number(el.tagName.slice(1))));
      for (let i = 1; i < headingSequence.length; i++) {
        if (headingSequence[i] > headingSequence[i - 1] + 1) {
          errors.push(file + ": heading hierarchy skips from h" + headingSequence[i - 1] +
            " to h" + headingSequence[i] + " at heading " + i);
          break;
        }
      }
      const chapterNavigation = page.locator("nav.chapter-nav");
      if (await chapterNavigation.count()) {
        const label = await chapterNavigation.first().evaluate(el =>
          (el.getAttribute("aria-label") || "").trim() ||
          (el.getAttribute("aria-labelledby") || "").trim());
        if (!label) errors.push(file + ": chapter navigation landmark has no accessible name");
      }

      // Reload before keyboard checks so prior scripted focus/clicks cannot contaminate them.
      await page.goto("http://127.0.0.1:4173/" + file, { waitUntil: "domcontentloaded" });
      // Reload clears injected scripts; restore axe before the language-state audit below.
      await page.addScriptTag({ path: path.resolve("node_modules/axe-core/axe.min.js") });
      // Every page must provide a working, keyboard-reachable skip link to its main content.
      const skipLink = page.locator("a.skip-link").first();
      if (!(await skipLink.count())) {
        errors.push(file + ": missing skip link");
      } else {
        const target = await skipLink.getAttribute("href");
        const targetExists = target && target.startsWith("#") &&
          await page.locator(target).count() === 1;
        if (!targetExists) {
          errors.push(file + ": skip link target is missing or ambiguous: " + target);
        } else {
          await skipLink.focus();
          const visibleOnFocus = await skipLink.evaluate(el => {
            const style = getComputedStyle(el);
            const rect = el.getBoundingClientRect();
            return style.visibility !== "hidden" && style.display !== "none" &&
              rect.width > 0 && rect.height > 0 && rect.top >= 0;
          });
          if (!visibleOnFocus) errors.push(file + ": skip link is not visibly revealed on keyboard focus");
          await skipLink.press("Enter");
          try {
            await page.waitForFunction(expected => location.hash === expected, target, { timeout: 1000 });
          } catch {
            errors.push(file + ": Enter did not activate skip link to " + target);
          }
          const mainReceivedFocus = await page.waitForFunction(
            expected => document.activeElement?.id === expected.slice(1), target, { timeout: 1000 }
          ).then(() => true).catch(() => false);
          if (!mainReceivedFocus) {
            errors.push(file + ": skip link changed the URL but did not move focus to its main-content target");
          }
        }
      }
      const lang = page.locator("#lang, #language").first();
      if (await lang.count()) {
        const before = (await lang.innerText()).trim();
        await lang.click();
        const after = (await lang.innerText()).trim();
        await runAxeAudit("alternate language");
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

        // Representative keyboard activation for the remaining chapter models.
        const modelChecks = {
          "/zoology.html": { control: '#animal-controls [data-group="mammals"]', output: "#animal-output", key: "Enter" },
          "/cell-biology.html": { control: '#org-controls [data-org="mitochondria"]', output: "#org-output", key: "Space" },
          "/anatomy.html": { control: '#system-controls [data-system="nervous"]', output: "#system-output", key: "Enter" },
          "/genetics.html": { control: '#template-controls [data-template="GGA"]', output: "#rna-output", key: "Space" },
          "/microbiology.html": { control: '#group-controls [data-group="archaea"]', output: "#group-output", key: "Enter" },
          "/evolution.html": { control: '#mechanism-controls [data-mech="drift"]', output: "#mechanism-output", key: "Space" },
          "/biochemistry.html": { control: '#enzyme-controls [data-enzyme="wrong"]', output: "#enzyme-output", key: "Enter" },
          "/systematics.html": { control: '#domain-controls [data-domain="eukarya"]', output: "#domain-output", key: "Space" }
        };
        const modelCheck = Object.entries(modelChecks).find(([suffix]) => file.endsWith(suffix))?.[1];
        if (modelCheck) {
          const control = page.locator(modelCheck.control);
          const output = page.locator(modelCheck.output);
          if (!(await control.count()) || !(await output.count())) {
            errors.push(file + ": representative interactive model control/output not found");
          } else {
            const before = await output.innerText();
            await control.focus();
            await page.keyboard.press(modelCheck.key);
            const after = await output.innerText();
            if (await control.getAttribute("aria-pressed") !== "true" || !after || after === before) {
              errors.push(file + ": " + modelCheck.key +
                " did not update the selected state and output for " + modelCheck.control +
                " (before: " + before + "; after: " + after + ")");
            }
          }
        }

        const verifyModelChoices = async (groupSelector, outputSelector, cases, label) => {
          for (const [value, expected] of cases) {
            const control = page.locator(groupSelector + '[data-' + label + '="' + value + '"]');
            if (!(await control.count())) {
              errors.push(file + ": missing " + label + " model choice " + value);
              continue;
            }
            await control.click();
            const pressed = await page.locator(groupSelector).evaluateAll(elements =>
              elements.filter(el => el.getAttribute("aria-pressed") === "true").length);
            const output = (await page.locator(outputSelector).innerText()).trim();
            if (await control.getAttribute("aria-pressed") !== "true" || pressed !== 1 ||
                !output.toLowerCase().includes(expected.toLowerCase())) {
              errors.push(file + ": " + label + "=" + value +
                " did not produce the expected single-selection output (expected: " + expected +
                "; got: " + output + "; pressed: " + pressed + ")");
            }
          }
        };

        const verifyAnyChoiceGroup = async (groupSelector, outputSelector, attribute, label) => {
          const controls = page.locator(groupSelector);
          const count = await controls.count();
          if (!count) {
            errors.push(file + ": " + label + " model controls not found");
            return;
          }
          for (let i = 0; i < count; i++) {
            const control = controls.nth(i);
            await control.click();
            const pressed = await controls.evaluateAll(elements =>
              elements.filter(el => el.getAttribute("aria-pressed") === "true").length);
            const output = (await page.locator(outputSelector).innerText()).trim();
            if (await control.getAttribute("aria-pressed") !== "true" || pressed !== 1 || !output) {
              errors.push(file + ": " + label + " option " + i +
                " did not produce one selected control and a non-empty output (pressed: " + pressed +
                "; output: " + output + ")");
            }
          }
        };

        if (file.endsWith("/botany.html")) {
          await verifyAnyChoiceGroup("button[data-organ]", "#organ-output", "organ", "plant organ");
          for (const condition of ["light", "water", "co2"]) {
            const control = page.locator('[data-condition="' + condition + '"]');
            if (!(await control.count())) {
              errors.push(file + ": photosynthesis condition control missing: " + condition);
              continue;
            }
            await control.click();
            if (await control.getAttribute("aria-pressed") !== "false" ||
                !(await page.locator("#photo-status").innerText()).trim()) {
              errors.push(file + ": disabling " + condition + " did not update photosynthesis state");
            }
            await control.click();
            if (await control.getAttribute("aria-pressed") !== "true") {
              errors.push(file + ": re-enabling " + condition + " did not restore its active state");
            }
          }
        }
        if (file.endsWith("/zoology.html")) {
          await verifyAnyChoiceGroup("#animal-controls button[data-group]", "#animal-output", "group", "animal group");
        }
        if (file.endsWith("/cell-biology.html")) {
          await verifyAnyChoiceGroup("#org-controls button[data-org]", "#org-output", "org", "organelle");
          await verifyAnyChoiceGroup("#transport-controls button[data-mode]", "#transport-output", "mode", "membrane transport");
          await verifyAnyChoiceGroup("#mitosis-controls button[data-stage]", "#mitosis-output", "stage", "mitosis stage");
        }
        if (file.endsWith("/anatomy.html")) {
          await verifyAnyChoiceGroup("#system-controls button[data-system]", "#system-output", "system", "body system");
        }
        if (file.endsWith("/microbiology.html")) {
          await verifyAnyChoiceGroup("#group-controls button[data-group]", "#group-output", "group", "microbial group");
          await verifyAnyChoiceGroup("#shape-controls button[data-shape]", "#shape-output", "shape", "bacterial shape");
          await verifyAnyChoiceGroup("#phase-controls button[data-phase]", "#phase-output", "phase", "growth phase");
        }
        if (file.endsWith("/evolution.html")) {
          await verifyAnyChoiceGroup("#selection-controls button[data-selection]", "#selection-output", "selection", "selection pressure");
          await verifyAnyChoiceGroup("#mechanism-controls button[data-mech]", "#mechanism-output", "mech", "evolutionary mechanism");
          await verifyAnyChoiceGroup("#homology-controls button[data-homology]", "#homology-output", "homology", "homology comparison");
          await verifyAnyChoiceGroup("#timeline-controls button[data-era]", "#timeline-output", "era", "evolutionary timeline");
        }

        if (file.endsWith("/genetics.html")) {
          await verifyModelChoices("#template-controls button", "#rna-output",
            [["TAC", "AUG"], ["GGA", "CCU"], ["ATG", "UAC"], ["CCT", "GGA"]], "template");
          await verifyModelChoices("#codon-controls button", "#codon-output",
            [["AUG", "Methionine"], ["UUU", "Phenylalanine"], ["GGG", "Glycine"],
             ["UAA", "Stop codon"], ["GCU", "Alanine"]], "codon");
          await verifyModelChoices("#mutation-controls button", "#mutation-output",
            [["substitution", "substitution"], ["insertion", "insertion"], ["deletion", "deletion"]], "mutation");
          for (const [mutation, sequenceToken] of [["substitution", "UCU"], ["insertion", "AGC"], ["deletion", "CUU"]]) {
            await page.locator('#mutation-controls [data-mutation="' + mutation + '"]').click();
            const sequence = await page.locator("#mutation-seq").innerText();
            if (!sequence.includes(sequenceToken)) {
              errors.push(file + ": " + mutation + " model did not display the expected altered reading frame: " + sequence);
            }
          }
        }

        if (file.endsWith("/biochemistry.html")) {
          await verifyModelChoices("#enzyme-controls button", "#enzyme-output",
            [["fit", "compatible substrate"], ["wrong", "do not fit"], ["heat", "excessive heat"]], "enzyme");
          await verifyModelChoices("#factor-controls button", "#factor-output",
            [["temperature", "temperature"], ["ph", "pH"], ["substrate", "substrate"]], "factor");
          await verifyModelChoices("#atp-controls button", "#atp-output",
            [["hydrolysis", "ATP + H₂O"], ["synthesis", "ADP + Pi"]], "atp");
          await verifyModelChoices("#respiration-controls button", "#respiration-output",
            [["glycolysis", "glycolysis"], ["cycle", "citric acid"], ["chain", "electrons"]], "resp");
        }

        if (file.endsWith("/ecology.html")) {
          await verifyModelChoices("#carbon-controls button", "#carbon-output",
            [["photosynthesis", "photosynthesis"], ["respiration", "cellular respiration"],
             ["decomposition", "decomposition"], ["combustion", "combustion"], ["ocean", "ocean"]], "carbon");
          await verifyModelChoices("#nitrogen-controls button", "#nitrogen-output",
            [["fixation", "nitrogen fixation"], ["ammonification", "ammonification"],
             ["nitrification", "nitrification"], ["assimilation", "assimilation"],
             ["denitrification", "denitrification"]], "nitrogen");
          await verifyModelChoices("#pressure-controls button", "#pressure-output",
            [["drought", "drought"], ["pollution", "pollut"], ["invasive", "invasive"], ["protection", "habitat restoration"]], "pressure");
          for (const organism of ["grass", "grasshopper", "frog", "snake", "hawk"]) {
            await page.locator('#chain-controls [data-chain="' + organism + '"]').click();
          }
          const completedChain = await page.locator("#chain-output").innerText();
          if (!completedChain.includes("Grass") || !completedChain.includes("Grasshopper") ||
              !completedChain.includes("Frog") || !completedChain.includes("Snake") ||
              !completedChain.includes("Hawk") || !completedChain.includes("Complete")) {
            errors.push(file + ": food-chain model did not complete the expected five-organism sequence: " + completedChain);
          }
        }

        if (file.endsWith("/systematics.html")) {
          await verifyModelChoices("#rank-controls button", "#rank-output",
            [["domain", "domain"], ["kingdom", "kingdom"], ["phylum", "phylum"],
             ["class", "class"], ["order", "order"], ["family", "family"],
             ["genus", "genus"], ["species", "species"]], "rank");
          await verifyModelChoices("#domain-controls button", "#domain-output",
            [["bacteria", "bacteria"], ["archaea", "archaea"], ["eukarya", "eukarya"]], "domain");
          await verifyModelChoices("#name-controls button", "#name-output",
            [["wolf", "Canis lupus"], ["human", "Homo sapiens"], ["oak", "Quercus robur"]], "name");
          await page.locator('#key-controls [data-key="backbone"]').click();
          await page.locator('#trait-controls [data-trait="feathers"]').click();
          if (!(await page.locator("#key-output").innerText()).toLowerCase().includes("birds")) {
            errors.push(file + ": classification key did not identify the feathered group as birds");
          }
          await page.locator('#key-controls [data-key="no-backbone"]').click();
          const visibleTraits = await page.locator("#trait-controls [data-trait]:visible").evaluateAll(elements =>
            elements.map(el => el.dataset.trait));
          if (visibleTraits.length !== 1 || visibleTraits[0] !== "shell") {
            errors.push(file + ": invertebrate branch should expose only the exoskeleton trait: " + JSON.stringify(visibleTraits));
          }
          await page.locator('#trait-controls [data-trait="shell"]').click();
          if (!(await page.locator("#key-output").innerText()).toLowerCase().includes("arthropod")) {
            errors.push(file + ": exoskeleton branch did not identify the likely arthropod group");
          }
        }

        // Check that interactive model outputs are localised, not just their labels.
        if (file.endsWith("/genetics.html")) {
          await lang.click();
          await page.locator('#template-controls [data-template="GGA"]').click();
          const output = await page.locator("#rna-output").innerText();
          if (!output.includes("Транскрипт РНК") || !output.includes("CCU")) {
            errors.push(file + ": DNA-template model output is not correctly localised in Russian: " + output);
          }
          await lang.click();
        }
        if (file.endsWith("/biochemistry.html")) {
          await lang.click();
          await page.locator('#atp-controls [data-atp="hydrolysis"]').click();
          const output = await page.locator("#atp-output").innerText();
          if (!output.includes("АТФ + H₂O") || !output.includes("стандартных биохимических")) {
            errors.push(file + ": ATP hydrolysis model output is not correctly localised in Russian: " + output);
          }
          await lang.click();
        }
        if (file.endsWith("/ecology.html")) {
          await lang.click();
          await page.locator('#nitrogen-controls [data-nitrogen="denitrification"]').click();
          const output = await page.locator("#nitrogen-output").innerText();
          if (!output.includes("Денитрификация") || !output.includes("N₂O")) {
            errors.push(file + ": nitrogen-cycle model output is not correctly localised in Russian: " + output);
          }
          await lang.click();
        }
        if (file.endsWith("/systematics.html")) {
          await lang.click();
          await page.locator('#domain-controls [data-domain="archaea"]').click();
          const output = await page.locator("#domain-output").innerText();
          if (!output.includes("Археи") || !output.includes("прокариоты")) {
            errors.push(file + ": domain model output is not correctly localised in Russian: " + output);
          }
          await lang.click();
        }

        if (file.endsWith("/systematics.html")) {
          const nameControl = page.locator('#name-controls [data-name="human"]');
          const nameOutput = page.locator("#name-output");
          if (await nameOutput.getAttribute("aria-live") !== "polite") {
            errors.push(file + ": dynamic species-name output is not announced through a polite live region");
          }
          const beforeName = await nameOutput.innerText();
          await nameControl.focus();
          await page.keyboard.press("Enter");
          const afterName = await nameOutput.innerText();
          if (await nameControl.getAttribute("aria-pressed") !== "true" ||
              !afterName || afterName === beforeName) {
            errors.push(file + ": keyboard selection did not update the species-name example");
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

        // Exercise every chapter quiz: lock one answer, preserve feedback across
        // language changes, then confirm that advancing unlocks the next question.
        const quizNext = page.locator("#quiz-next");
        const quizAnswers = page.locator("#answers button");
        if (await quizNext.count() && await quizAnswers.count()) {
          if (!(await quizAnswers.first().isDisabled())) await quizAnswers.first().click();
          const answeredStates = await quizAnswers.evaluateAll(elements => elements.map(el => ({
            disabled: el.disabled,
            pressed: el.getAttribute("aria-pressed")
          })));
          if (answeredStates.some(x => !x.disabled) ||
              answeredStates.filter(x => x.pressed === "true").length !== 1) {
            errors.push(file + ": quiz choices must lock after one answer and expose exactly one selected choice");
          }
          const feedbackBeforeSwitch = (await page.locator("#result").innerText()).trim();
          await lang.click();
          const feedbackAfterSwitch = (await page.locator("#result").innerText()).trim();
          const translatedStates = await page.locator("#answers button").evaluateAll(elements => elements.map(el => ({
            disabled: el.disabled,
            pressed: el.getAttribute("aria-pressed")
          })));
          if (!feedbackAfterSwitch || feedbackAfterSwitch === feedbackBeforeSwitch ||
              translatedStates.some(x => !x.disabled) ||
              translatedStates.filter(x => x.pressed === "true").length !== 1) {
            errors.push(file + ": quiz feedback or selected-answer lock was not preserved in the alternate language");
          }
          await lang.click();
          await quizNext.click();
          const nextQuestionStates = await page.locator("#answers button").evaluateAll(elements => elements.map(el => ({
            disabled: el.disabled,
            pressed: el.getAttribute("aria-pressed")
          })));
          if (nextQuestionStates.some(x => x.disabled || x.pressed !== null)) {
            errors.push(file + ": advancing the quiz must unlock all choices and clear the previous selection");
          }
        }
        languageChecks++;

        if (file.endsWith("/index.html")) {
          const verifyOrganelleKeyboard = async (language) => {
            const controls = page.locator("#cell-diagram [data-org]");
            const count = await controls.count();
            if (count !== 6) {
              errors.push(file + ": expected 6 keyboard-accessible organelle controls, found " + count);
              return;
            }
            for (let i = 0; i < count; i++) {
              const control = controls.nth(i);
              const semantics = await control.evaluate(el => ({
                role: el.getAttribute("role"),
                tabIndex: el.tabIndex,
                label: (el.getAttribute("aria-label") || "").trim(),
                describedBy: el.getAttribute("aria-describedby"),
                descriptionExists: !!document.getElementById(el.getAttribute("aria-describedby") || "")
              }));
              if (semantics.role !== "button" || semantics.tabIndex < 0 || !semantics.label ||
                  semantics.describedBy !== "org-info" || !semantics.descriptionExists) {
                errors.push(file + ": organelle control " + i + " has incomplete accessible semantics in " +
                  language + ": " + JSON.stringify(semantics));
                continue;
              }
              await control.focus();
              const focusState = await control.evaluate(el => {
                const style = getComputedStyle(el);
                return (style.outlineStyle !== "none" && Number.parseFloat(style.outlineWidth) > 0) ||
                  style.boxShadow !== "none" || style.filter !== "none";
              });
              if (!focusState) {
                errors.push(file + ": organelle control " + semantics.label +
                  " has no detectable keyboard focus indicator in " + language + " mode");
              }
              for (const key of ["Enter", "Space"]) {
                await control.focus();
                await page.keyboard.press(key);
                const info = await page.locator("#org-info").innerText();
                if (!info.includes(semantics.label)) {
                  errors.push(file + ": " + key + " did not activate " + semantics.label +
                    " in " + language + " mode; live-region text was: " + info);
                }
              }
            }
          };

          // Test the complete organelle set with both language labels and both activation keys.
          await verifyOrganelleKeyboard("English");
          await lang.click();
          languageChecks++;
          await verifyOrganelleKeyboard("Russian");
          await lang.click();
          languageChecks++;
        }
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

      // Dynamic model outputs and quiz feedback must expose an announcement mechanism.
      const dynamicOutputIssues = await page.locator(
        '[id$="-output"], #result, #feedback, #org-info, #photo-status'
      ).evaluateAll(elements => elements.filter(el => {
        const live = (el.getAttribute("aria-live") || "").toLowerCase();
        const role = (el.getAttribute("role") || "").toLowerCase();
        return !["polite", "assertive"].includes(live) && !["status", "alert"].includes(role);
      }).map(el => ({
        id: el.id || "",
        role: el.getAttribute("role") || "",
        ariaLive: el.getAttribute("aria-live") || "",
        tag: el.tagName.toLowerCase()
      })));
      if (dynamicOutputIssues.length) {
        errors.push(file + ": dynamic output/feedback regions lack aria-live or status semantics: " +
          JSON.stringify(dynamicOutputIssues));
      }

      // Horizontally scrollable data tables must be named, focusable regions and respond to arrow keys.
      const tableCount = await page.locator(".table-wrap").count();
      for (let tableIndex = 0; tableIndex < tableCount; tableIndex++) {
        const table = page.locator(".table-wrap").nth(tableIndex);
        const details = await table.evaluate(el => ({
          visible: el.getClientRects().length > 0,
          scrollable: el.scrollWidth > el.clientWidth + 1 &&
            ["auto", "scroll"].includes(getComputedStyle(el).overflowX),
          tabIndex: el.tabIndex,
          role: el.getAttribute("role"),
          label: (el.getAttribute("aria-label") || "").trim()
        }));
        if (!details.visible || !details.scrollable) continue;
        if (details.tabIndex < 0 || details.role !== "region" || !details.label) {
          errors.push(file + ": horizontally scrollable table " + tableIndex +
            " lacks a named keyboard-focusable region: " + JSON.stringify(details));
          continue;
        }
        await table.evaluate(el => { el.scrollLeft = 0; });
        await table.focus();
        for (let keyStep = 0; keyStep < 3; keyStep++) await page.keyboard.press("ArrowRight");
        const finalScroll = await table.evaluate(el => el.scrollLeft);
        if (finalScroll <= 0) {
          errors.push(file + ": ArrowRight did not scroll horizontally overflowed table " + tableIndex);
        }
      }

      // Toggle buttons must expose a valid, machine-readable pressed state when they use aria-pressed.
      const pressedStateIssues = await page.locator("button[aria-pressed]").evaluateAll(elements =>
        elements.filter(el => !["true", "false"].includes(el.getAttribute("aria-pressed")))
          .map(el => ({ id: el.id || "", text: (el.innerText || "").trim().slice(0, 100),
            ariaPressed: el.getAttribute("aria-pressed") }))
      );
      if (pressedStateIssues.length) {
        errors.push(file + ": toggle button(s) expose invalid aria-pressed values: " +
          JSON.stringify(pressedStateIssues));
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

      // Every visible native/custom interactive control must be keyboard focusable,
      // and Tab / Shift+Tab must be able to leave and return to it (no local keyboard trap).
      const keyboardTargets = page.locator("button, a[href], input, select, textarea, [role='button'], [tabindex]:not([tabindex='-1'])");
      const keyboardTargetCount = await keyboardTargets.count();
      let keyboardTargetsChecked = 0;
      for (let targetIndex = 0; targetIndex < keyboardTargetCount; targetIndex++) {
        const target = keyboardTargets.nth(targetIndex);
        const targetState = await target.evaluate(el => {
          const style = getComputedStyle(el);
          return {
            visible: style.display !== "none" && style.visibility !== "hidden" &&
              style.visibility !== "collapse" && el.getClientRects().length > 0,
            enabled: !el.disabled && el.getAttribute("aria-disabled") !== "true",
            tabIndex: el.tabIndex
          };
        });
        if (!targetState.visible || !targetState.enabled || targetState.tabIndex < 0) continue;
        await target.focus();
        const receivedFocus = await target.evaluate(el => document.activeElement === el);
        if (!receivedFocus) {
          errors.push(file + ": visible interactive control " + targetIndex +
            " cannot receive keyboard focus (tabIndex " + targetState.tabIndex + ")");
          continue;
        }
        await page.keyboard.press("Tab");
        const movedForward = await target.evaluate(el => document.activeElement !== el);
        if (!movedForward) {
          errors.push(file + ": Tab could not move away from interactive control " + targetIndex);
          continue;
        }
        await page.keyboard.press("Shift+Tab");
        const returned = await target.evaluate(el => document.activeElement === el);
        if (!returned) {
          errors.push(file + ": Shift+Tab did not return to interactive control " + targetIndex);
        }
        keyboardTargetsChecked++;
      }
      if (!keyboardTargetsChecked) {
        errors.push(file + ": no visible keyboard targets were exercised");
      }

      // Start document-level traversal from a clean page with no scripted focus history.
      await page.goto("http://127.0.0.1:4173/" + file, { waitUntil: "domcontentloaded" });
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
