import { chromium } from "playwright";
import path from "node:path";

const base = "http://127.0.0.1:4173/chemistry/";
const pages = [
  "index.html",
  "chapters/atomic-structure.html",
  "chapters/chemical-elements.html",
  "periodic-table.html",
  "chapters/chemical-bonding.html",
  "chapters/amount-of-substance.html",
  "chapters/chemical-formulae.html",
  "chapters/solutions.html",
  "chapters/acids-and-bases.html",
  "chapters/chemical-reactions.html",
  "chapters/redox.html",
  "chapters/organic-chemistry.html",
  "chapters/chemistry-of-life.html",
  "molecule-lab.html",
  "virtual-lab.html",
  "reaction-trainer.html",
  "stoichiometry.html",
  "gas-laws.html",
  "chemistry-constants.html",
  "glossary.html",
  "knowledge-check.html"
];

const browser = await chromium.launch({ headless: true });
const errors = [];
let languageChecks = 0;
const checkedInternalLinks = new Set();
const localOrigin = new URL(base).origin;
try {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  let current = "";
  page.on("pageerror", error => errors.push(current + ": " + error.message));

  for (const file of pages) {
    current = file;
    const response = await page.goto(base + file, { waitUntil: "domcontentloaded" });
    if (!response || !response.ok()) {
      errors.push(file + ": HTTP " + (response?.status() ?? "no response"));
      continue;
    }

    const hrefs = await page.locator("a[href]").evaluateAll(items => items.map(a => a.getAttribute("href")).filter(Boolean));
    for (const href of hrefs) {
      let target;
      try { target = new URL(href, page.url()); } catch { continue; }
      if (target.origin !== localOrigin || target.protocol !== "http:" && target.protocol !== "https:") continue;
      target.hash = "";
      if (checkedInternalLinks.has(target.href)) continue;
      checkedInternalLinks.add(target.href);
      const linkResponse = await page.request.get(target.href);
      if (!linkResponse.ok()) errors.push(file + ": internal link returned HTTP " + linkResponse.status() + " (" + target.pathname + ")");
    }

    for (const width of [390, 768, 1280]) {
      await page.setViewportSize({ width, height: 844 });
      const dimensions = await page.evaluate(() => ({ document: document.documentElement.scrollWidth, viewport: document.documentElement.clientWidth }));
      if (dimensions.document > dimensions.viewport + 1) {
        errors.push(file + ": horizontal page overflow at " + width + "px (" + dimensions.document + "px > " + dimensions.viewport + "px)");
      }
    }
    await page.setViewportSize({ width: 390, height: 844 });
    const unlabeledControls = await page.locator("input:not([type=hidden]), select, textarea").evaluateAll(items => items.filter(el => !(el.labels && el.labels.length) && !el.getAttribute("aria-label") && !el.getAttribute("aria-labelledby")).map(el => el.id || el.outerHTML.slice(0, 80)));
    if (unlabeledControls.length) errors.push(file + ": form controls lack accessible labels: " + unlabeledControls.join(", "));

    const imagesWithoutAlt = await page.locator("img:not([alt])").count();
    if (imagesWithoutAlt) errors.push(file + ": " + imagesWithoutAlt + " image(s) lack an alt attribute");

    const unnamedActions = await page.locator("a, button").evaluateAll(items => items.filter(el => !el.innerText.trim() && !el.getAttribute("aria-label") && !el.getAttribute("title") && !el.querySelector("[aria-label], title, img[alt]")).map(el => el.outerHTML.slice(0, 100)));
    if (unnamedActions.length) errors.push(file + ": links or buttons lack an accessible name: " + unnamedActions.join(" | "));

    if (file === "index.html") {
      const chapterCount = await page.locator(".chapter").count();
      if (chapterCount !== 12) errors.push(file + ": expected 12 visible chapter cards, found " + chapterCount);
      const widths = await page.evaluate(() => ({
        document: document.documentElement.scrollWidth,
        viewport: document.documentElement.clientWidth
      }));
      if (widths.document > widths.viewport + 1) {
        errors.push(file + ": horizontal overflow at 390px (" + widths.document + "px > " + widths.viewport + "px)");
      }
    }

    const lang = page.locator("#lang, #language").first();
    if (await lang.count()) {
      const before = (await lang.innerText()).trim();
      const originalDocumentLanguage = await page.locator("html").getAttribute("lang");
      await lang.click();
      const after = (await lang.innerText()).trim();
      const switchedDocumentLanguage = await page.locator("html").getAttribute("lang");
      if (before === after) errors.push(file + ": language toggle did not change");
      if (originalDocumentLanguage === "ru" && switchedDocumentLanguage !== "en") {
        errors.push(file + ": document language was not updated to English after switching");
      }
      await lang.click();
      const restoredDocumentLanguage = await page.locator("html").getAttribute("lang");
      if (restoredDocumentLanguage !== originalDocumentLanguage) {
        errors.push(file + ": document language was not restored after switching back");
      }
      languageChecks++;
    }

    if (await page.locator("button").evaluateAll(items => items.some(button => button.type !== "button"))) {
      errors.push(file + ": a button is missing an explicit button type");
    }

    if (file === "chapters/atomic-structure.html") {
      const stats = page.locator(".atom-stats");
      if (await stats.getAttribute("aria-live") !== "polite") {
        errors.push(file + ": changing atom statistics are not announced to assistive technology");
      }
      const expectedAtoms = { H: ["1", "0", "1"], C: ["6", "6", "6"], O: ["8", "8", "8"], Na: ["11", "12", "11"], Cl: ["17", "18", "17"] };
      for (const [symbol, expected] of Object.entries(expectedAtoms)) {
        await page.locator("#element").selectOption(symbol);
        const actual = await Promise.all(["#p", "#n", "#e"].map(selector => page.locator(selector).innerText().then(value => value.trim())));
        if (JSON.stringify(actual) !== JSON.stringify(expected)) {
          errors.push(file + ": incorrect proton, neutron or electron count for " + symbol + " (got " + actual.join("/") + ")");
        }
      }
      if (!(await page.locator("[data-t=ionNote]").innerText()).includes("одинаковое число протонов") ||
          !(await page.locator("[data-t=ionNote]").innerText()).includes("теряет либо присоединяет электроны")) {
        errors.push(file + ": Russian note must distinguish isotopes from ions");
      }
      if (!(await page.locator("[data-t=modelLimit]").innerText()).includes("круговым дорожкам")) {
        errors.push(file + ": simplified shell diagram does not explain that electrons do not follow fixed circular paths");
      }
      await page.locator("#element").selectOption("O");
      await page.locator("#lang").click();
      if (!(await page.locator("[data-t=ionNote]").innerText()).includes("same number of protons") ||
          !(await page.locator("[data-t=ionNote]").innerText()).includes("loses or gains electrons")) {
        errors.push(file + ": English note must distinguish isotopes from ions");
      }
      if (!(await page.locator("[data-t=modelLimit]").innerText()).includes("fixed circular tracks")) {
        errors.push(file + ": atomic model limitation is missing in English");
      }
      if (await page.locator("#element").inputValue() !== "O" ||
          (await page.locator("#p").innerText()).trim() !== "8" ||
          (await page.locator("#e").innerText()).trim() !== "8") {
        errors.push(file + ": changing language reset the selected atom or its statistics");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/chemical-bonding.html") {
      if (!(await page.locator("[data-i=polarityNote]").innerText()).includes("частичные заряды") ||
          !(await page.locator("[data-i=polarityNote]").innerText()).includes("полного переноса электрона")) {
        errors.push(file + ": Russian polarity note must distinguish partial charges from full electron transfer");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=polarityNote]").innerText()).includes("partial charges") ||
          !(await page.locator("[data-i=polarityNote]").innerText()).includes("complete electron transfer")) {
        errors.push(file + ": English polarity note must distinguish partial charges from full electron transfer");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=lead]").innerText()).includes("энергия системы") || !(await page.locator("[data-i=lead]").innerText()).includes("атомы или ионы")) {
        errors.push(file + ": Russian introduction should explain bonds between atoms or ions through system energy");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=lead]").innerText()).includes("system's energy") || !(await page.locator("[data-i=lead]").innerText()).includes("atoms or ions")) {
        errors.push(file + ": English introduction should explain bonds between atoms or ions through system energy");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=molecularPolarityNote]").innerText()).includes("CO₂") ||
          !(await page.locator("[data-i=molecularPolarityNote]").innerText()).includes("H₂O") ||
          !(await page.locator("[data-i=molecularPolarityNote]").innerText()).includes("не задаёт универсальную")) {
        errors.push(file + ": Russian explanation must distinguish bond and molecular polarity and avoid a rigid electronegativity cutoff");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=molecularPolarityNote]").innerText()).includes("linear CO₂") ||
          !(await page.locator("[data-i=molecularPolarityNote]").innerText()).includes("bent H₂O") ||
          !(await page.locator("[data-i=molecularPolarityNote]").innerText()).includes("universal sharp boundary")) {
        errors.push(file + ": English explanation must distinguish bond and molecular polarity and avoid a rigid electronegativity cutoff");
      }
      await page.locator("#lang").click();
      const detail = page.locator(".detail");
      if (await detail.getAttribute("aria-live") !== "polite") {
        errors.push(file + ": dynamic bond explanation is not announced to assistive technology");
      }
      await page.locator('[data-type="ionic"]').click();
      if (!(await page.locator("#detailText").innerText()).includes("кристаллическую решётку")) {
        errors.push(file + ": ionic bonding explanation does not distinguish a crystal lattice from an isolated ion pair");
      }
      const ruConductivity = await page.locator('[data-i="ionicFeature"]').innerText();
      if (!ruConductivity.includes("твёрдом состоянии") || !ruConductivity.includes("подвижными ионами")) {
        errors.push(file + ": Russian ionic conductivity explanation is incomplete");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("#detailText").innerText()).includes("crystal lattice")) {
        errors.push(file + ": ionic bonding clarification is missing in English");
      }
      const enConductivity = await page.locator('[data-i="ionicFeature"]').innerText();
      if (!enConductivity.includes("solid state") || !enConductivity.includes("mobile ions")) {
        errors.push(file + ": English ionic conductivity explanation is incomplete");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/chemical-reactions.html") {
      if (!(await page.locator("[data-i=exoText]").innerText()).includes("тепло передаётся") ||
          !(await page.locator("[data-i=endoText]").innerText()).includes("поглощает тепло")) {
        errors.push(file + ": Russian exothermic/endothermic definitions are incomplete");
      }
      if (!(await page.locator("[data-i=hessNote]").innerText()).includes("начального и конечного состояний") ||
          !(await page.locator("[data-i=thermoCaution]").innerText()).includes("не определяет скорость")) {
        errors.push(file + ": Russian Hess's law or enthalpy limitation is missing");
      }
      if (!(await page.locator("[data-i=methaneEnthalpy]").innerText()).includes("−890,3")) {
        errors.push(file + ": methane combustion enthalpy example is missing");
      }
      if (!(await page.locator("[data-i=thermoIntro]").innerText()).includes("работа расширения") ||
          !(await page.locator(".formula").filter({ hasText: "qₚ = ΔH" }).count())) {
        errors.push(file + ": constant-pressure heat/enthalpy condition or relation is missing in Russian");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=hessNote]").innerText()).includes("initial and final states") ||
          !(await page.locator("[data-i=thermoCaution]").innerText()).includes("does not determine reaction rate")) {
        errors.push(file + ": English Hess's law or enthalpy limitation is missing");
      }
      if (!(await page.locator("[data-i=methaneEnthalpy]").innerText()).includes("−890.3")) {
        errors.push(file + ": English methane combustion enthalpy example is missing");
      }
      if (!(await page.locator("[data-i=thermoIntro]").innerText()).includes("pressure–volume work")) {
        errors.push(file + ": English constant-pressure heat/enthalpy condition is missing");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/organic-chemistry.html") {
      for (const key of ["ketonesText", "estersText", "ethersText", "arenesText", "carbonylNote"]) {
        if (!(await page.locator('[data-i="' + key + '"]').count())) errors.push(file + ": missing organic chemistry topic " + key);
      }
      if (!(await page.locator("[data-i=carbonylNote]").innerText()).includes("на конце цепи") ||
          !(await page.locator("[data-i=carbonylNote]").innerText()).includes("внутри цепи")) {
        errors.push(file + ": Russian explanation does not distinguish aldehydes from ketones");
      }
      if (!(await page.locator("[data-i=aromaticityNote]").innerText()).includes("4n + 2 π-электронов") || !(await page.locator("[data-i=aromaticityNote]").innerText()).includes("антиароматичны")) {
        errors.push(file + ": Russian aromaticity note must state the Hückel electron-count rule and its antiaromatic counterpart");
      }
      if (!(await page.locator("[data-i=isomerismNote]").innerText()).includes("одинаковую молекулярную формулу") || !(await page.locator("[data-i=isomerismNote]").innerText()).includes("C₂H₆O")) errors.push(file + ": Russian note must explain structural isomerism with an example");
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=carbonylNote]").innerText()).includes("at the end of the chain") ||
          !(await page.locator("[data-i=carbonylNote]").innerText()).includes("within the chain")) {
        errors.push(file + ": English explanation does not distinguish aldehydes from ketones");
      }
      if (!(await page.locator("[data-i=isomerismNote]").innerText()).includes("same molecular formula") || !(await page.locator("[data-i=isomerismNote]").innerText()).includes("C₂H₆O")) errors.push(file + ": English note must explain structural isomerism with an example");
      if (!(await page.locator("[data-i=aromaticityNote]").innerText()).includes("4n + 2 π electrons") || !(await page.locator("[data-i=aromaticityNote]").innerText()).includes("antiaromatic")) {
        errors.push(file + ": English aromaticity note must state the Hückel electron-count rule and its antiaromatic counterpart");
      }
      if (!(await page.locator("[data-i=arenesText]").innerText()).includes("delocalised")) {
        errors.push(file + ": English aromaticity note must refer to a delocalised pi system");
      }
      if (await page.locator(".tile").count() !== 10) errors.push(file + ": expected ten organic-compound family cards");
      await page.locator("#lang").click();
    }

    if (file === "chapters/redox.html") {
      if (!(await page.locator("[data-i=electronBalanceNote]").innerText()).includes("число отданных электронов должно равняться числу принятых") || !(await page.locator("[data-i=electronBalanceNote]").innerText()).includes("суммарного заряда")) errors.push(file + ": Russian redox balancing note must conserve electrons, atoms and charge");
      if (!(await page.locator("[data-i=electronFlow]").innerText()).includes("одна вертикальная черта") || !(await page.locator("[data-i=electronFlow]").innerText()).includes("двойная") ||
          !(await page.locator("[data-i=anodeText]").innerText()).includes("анод отрицателен") ||
          !(await page.locator("[data-i=cathodeText]").innerText()).includes("катод положителен")) {
        errors.push(file + ": Russian galvanic-cell electrode signs are incorrect or missing");
      }
      if (!(await page.locator("[data-i=electrodeRule]").innerText()).includes("электролизёре анод положителен") ||
          !(await page.locator("[data-i=electrodeRule]").innerText()).includes("внешнее напряжение") ||
          !(await page.locator("[data-i=gibbsPotential]").innerText()).includes("ΔᵣG° = −nFE°cell")) {
        errors.push(file + ": Russian electrolytic-cell sign distinction or Gibbs relation is missing");
      }
      if (!(await page.locator("[data-i=cellPotential]").innerText()).includes("+1,10 В") || !(await page.locator("[data-i=cellPotential]").innerText()).includes("активность растворённых ионов равна 1")) {
        errors.push(file + ": Daniell-cell standard potential is missing in Russian");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=electronBalanceNote]").innerText()).includes("number of electrons lost must equal the number gained") || !(await page.locator("[data-i=electronBalanceNote]").innerText()).includes("total charge")) errors.push(file + ": English redox balancing note must conserve electrons, atoms and charge");
      if (!(await page.locator("[data-i=electronFlow]").innerText()).includes("single vertical line") || !(await page.locator("[data-i=electronFlow]").innerText()).includes("double line") ||
          !(await page.locator("[data-i=anodeText]").innerText()).includes("anode is negative") ||
          !(await page.locator("[data-i=cathodeText]").innerText()).includes("cathode is positive")) {
        errors.push(file + ": English galvanic-cell electrode signs are incorrect or missing");
      }
      if (!(await page.locator("[data-i=electrodeRule]").innerText()).includes("anode is positive") ||
          !(await page.locator("[data-i=electrodeRule]").innerText()).includes("external voltage") ||
          !(await page.locator("[data-i=gibbsPotential]").innerText()).includes("Faraday constant")) {
        errors.push(file + ": English electrolytic-cell sign distinction or Gibbs relation is missing");
      }
      if (!(await page.locator("[data-i=cellPotential]").innerText()).includes("+1.10 V") || !(await page.locator("[data-i=cellPotential]").innerText()).includes("unit activity for dissolved ions")) {
        errors.push(file + ": Daniell-cell standard potential is missing in English");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/chemistry-of-life.html") {
      if (!(await page.locator("[data-i=carbonNote]").innerText()).includes("снижает pH морской воды") || !(await page.locator("[data-i=carbonNote]").innerText()).includes("парниковый эффект")) errors.push(file + ": Russian environment note must connect carbon emissions, greenhouse effect and ocean acidification");
      if (!(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("полимеры нуклеотидов") ||
          !(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("пентозу") ||
          !(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("дезоксирибоза") ||
          !(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("синтезе белка")) {
        errors.push(file + ": Russian nucleic-acid explanation is incomplete");
      }
      if (!(await page.locator("[data-i=enzymesText]").innerText()).includes("энергию активации") ||
          !(await page.locator("[data-i=enzymeNote]").innerText()).includes("температуру и pH")) {
        errors.push(file + ": Russian enzyme explanation lacks catalytic mechanism or condition caveat");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=carbonNote]").innerText()).includes("seawater pH decreases") || !(await page.locator("[data-i=carbonNote]").innerText()).includes("greenhouse effect")) errors.push(file + ": English environment note must connect carbon emissions, greenhouse effect and ocean acidification");
      if (!(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("nucleotide polymers") ||
          !(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("pentose sugar") ||
          !(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("deoxyribose") ||
          !(await page.locator("[data-i=nucleicAcidsText]").innerText()).includes("protein synthesis")) {
        errors.push(file + ": English nucleic-acid explanation is incomplete");
      }
      if (!(await page.locator("[data-i=enzymesText]").innerText()).includes("activation energy") ||
          !(await page.locator("[data-i=enzymeNote]").innerText()).includes("temperature and pH")) {
        errors.push(file + ": English enzyme explanation lacks catalytic mechanism or condition caveat");
      }
      if (await page.locator(".tile").count() !== 6) errors.push(file + ": expected six biomolecule/water/enzyme topic cards");
      if (!(await page.locator("[data-i=proteinNote]").innerText()).includes("peptide bonds") || !(await page.locator("[data-i=proteinNote]").innerText()).includes("primary structure")) errors.push(file + ": English protein note must explain peptide bonds and primary structure");
      if (!(await page.locator("[data-i=waterNote]").innerText()).includes("covalent O–H bonds")) errors.push(file + ": English water note must distinguish hydrogen bonds from covalent O-H bonds");
      if (!(await page.locator("[data-i=waterText]").innerText()).includes("molecule is bent") || !(await page.locator("[data-i=waterText]").innerText()).includes("dipole moments do not cancel")) errors.push(file + ": English water explanation must connect bent geometry with molecular polarity");
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=proteinNote]").innerText()).includes("пептидными связями") || !(await page.locator("[data-i=proteinNote]").innerText()).includes("первичная структура")) errors.push(file + ": Russian protein note must explain peptide bonds and primary structure");
      if (!(await page.locator("[data-i=waterNote]").innerText()).includes("ковалентными связями O–H")) errors.push(file + ": Russian water note must distinguish hydrogen bonds from covalent O-H bonds");
      if (!(await page.locator("[data-i=waterText]").innerText()).includes("угловой формы") || !(await page.locator("[data-i=waterText]").innerText()).includes("дипольные моменты не компенсируются")) errors.push(file + ": Russian water explanation must connect bent geometry with molecular polarity");
    }

    if (file === "chapters/redox.html") {
      const rules = page.locator(".panel li");
      if (await rules.count() !== 5) errors.push(file + ": expected five oxidation-state assignment rules");
      if (!(await page.locator("[data-i=workedConclusion]").innerText()).includes("не утверждение о заряде")) {
        errors.push(file + ": Russian worked example must distinguish formal oxidation state from actual atomic charge");
      }
      if (!(await page.locator(".formula").filter({ hasText: "2(+1)" }).count())) {
        errors.push(file + ": sulfur oxidation-state calculation is missing");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=workedConclusion]").innerText()).includes("not a claim")) {
        errors.push(file + ": English worked example must distinguish formal oxidation state from actual atomic charge");
      }
      if (!(await page.locator("[data-i=ruleOH]").innerText()).includes("peroxides") ||
          !(await page.locator("[data-i=ruleOH]").innerText()).includes("metal hydrides")) {
        errors.push(file + ": English oxidation-state exceptions are incomplete");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=ruleOH]").innerText()).includes("пероксидах") ||
          !(await page.locator("[data-i=ruleOH]").innerText()).includes("гидридах металлов")) {
        errors.push(file + ": Russian oxidation-state exceptions are incomplete");
      }
    }

    if (file === "chapters/chemical-formulae.html") {
      if (!(await page.locator("[data-i=formulaTypes]").innerText()).includes("простейшее целочисленное соотношение") ||
          !(await page.locator("[data-i=formulaTypes]").innerText()).includes("формульной единице")) {
        errors.push(file + ": Russian note must distinguish empirical, molecular and ionic formula representations");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=formulaTypes]").innerText()).includes("simplest whole-number ratio") ||
          !(await page.locator("[data-i=formulaTypes]").innerText()).includes("formula unit")) {
        errors.push(file + ": English note must distinguish empirical, molecular and ionic formula representations");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/chemical-formulae.html") {
      const formula = page.locator("#formula");
      const calculate = page.locator("#calc");
      const rows = page.locator("#rows tr");
      const total = page.locator("#total");

      await formula.fill("H2O");
      await calculate.click();
      let values = await rows.evaluateAll(items => items.map(row => [row.cells[0].textContent.trim(), row.cells[1].textContent.trim()]));
      if ((await total.innerText()).trim() !== "Всего атомов: 3" ||
          JSON.stringify(values) !== JSON.stringify([["H", "2"], ["O", "1"]])) {
        errors.push(file + ": H2O was not parsed into 2 H and 1 O atoms");
      }

      await formula.fill("2H2O");
      await calculate.click();
      values = await rows.evaluateAll(items => items.map(row => [row.cells[0].textContent.trim(), row.cells[1].textContent.trim()]));
      if ((await total.innerText()).trim() !== "Всего атомов: 6" ||
          JSON.stringify(values) !== JSON.stringify([["H", "4"], ["O", "2"]])) {
        errors.push(file + ": leading coefficient 2H2O was not applied to the whole formula");
      }

      await formula.fill("0H2O");
      await calculate.click();
      if ((await page.locator("#feedback").innerText()).trim() === "Формула разобрана успешно.") {
        errors.push(file + ": zero leading coefficient was incorrectly accepted");
      }

      await formula.fill("999999999999999999999999H2O");
      await calculate.click();
      if ((await page.locator("#feedback").innerText()).trim() === "Формула разобрана успешно.") {
        errors.push(file + ": unsafe leading coefficient overflow was incorrectly accepted");
      }

      await formula.fill("Ca(OH)2");
      await calculate.click();
      values = await rows.evaluateAll(items => items.map(row => [row.cells[0].textContent.trim(), row.cells[1].textContent.trim()]));
      if ((await total.innerText()).trim() !== "Всего атомов: 5" ||
          JSON.stringify(values) !== JSON.stringify([["Ca", "1"], ["O", "2"], ["H", "2"]])) {
        errors.push(file + ": Ca(OH)2 or group multipliers were calculated incorrectly");
      }

      await formula.fill("Al2(SO4)3");
      await calculate.click();
      values = await rows.evaluateAll(items => items.map(row => [row.cells[0].textContent.trim(), row.cells[1].textContent.trim()]));
      if ((await total.innerText()).trim() !== "Всего атомов: 17" ||
          JSON.stringify(values) !== JSON.stringify([["Al", "2"], ["S", "3"], ["O", "12"]])) {
        errors.push(file + ": nested-group formula Al2(SO4)3 was calculated incorrectly");
      }

      await formula.fill("H 2 O");
      await calculate.click();
      if ((await total.innerText()).trim() !== "Всего атомов: 3") {
        errors.push(file + ": harmless spaces in a formula were not ignored");
      }

      await formula.fill("Ca()2");
      await calculate.click();
      if ((await page.locator("#feedback").innerText()).trim() === "Формула разобрана успешно.") {
        errors.push(file + ": empty brackets were incorrectly accepted");
      }

      await formula.fill("Xx2");
      await calculate.click();
      if ((await page.locator("#feedback").innerText()).trim() === "Формула разобрана успешно.") {
        errors.push(file + ": unknown element symbol was incorrectly accepted");
      }
    }

    if (file === "chapters/chemical-elements.html") {
      const isotopeButtons = page.locator("[data-iso]");
      const russianLabels = await isotopeButtons.allInnerTexts();
      if (JSON.stringify(russianLabels) !== JSON.stringify(["Углерод-12", "Углерод-13", "Углерод-14"])) {
        errors.push(file + ": isotope selector labels are not localized in Russian");
      }
      if (!(await page.locator("[data-i=isotopicAverage]").innerText()).includes("взвешенное среднее") || !(await page.locator("[data-i=isotopicAverage]").innerText()).includes("сумма всех долей равна 1")) errors.push(file + ": Russian isotope-abundance note must describe a weighted mean");
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=isotopicAverage]").innerText()).includes("weighted mean") || !(await page.locator("[data-i=isotopicAverage]").innerText()).includes("sum to 1")) errors.push(file + ": English isotope-abundance note must describe a weighted mean");
      const englishLabels = await isotopeButtons.allInnerTexts();
      if (JSON.stringify(englishLabels) !== JSON.stringify(["Carbon-12", "Carbon-13", "Carbon-14"])) {
        errors.push(file + ": isotope selector labels are not localized in English");
      }
      if (await page.locator(".stats").getAttribute("aria-live") !== "polite" ||
          await isotopeButtons.nth(0).getAttribute("aria-pressed") !== "true") {
        errors.push(file + ": isotope statistics or selected state are not exposed to assistive technology");
      }
      await isotopeButtons.nth(2).click();
      if ((await page.locator("#neutrons").innerText()).trim() !== "8" ||
          (await page.locator("#mass").innerText()).trim() !== "14" ||
          await isotopeButtons.nth(2).getAttribute("aria-pressed") !== "true" ||
          await isotopeButtons.nth(0).getAttribute("aria-pressed") !== "false") {
        errors.push(file + ": Carbon-14 model did not show 8 neutrons, mass number 14 and an announced selected state");
      }
      await isotopeButtons.nth(0).click();
      await page.locator("#lang").click();
      if (await isotopeButtons.evaluateAll(items => items.some(button => button.type !== "button"))) {
        errors.push(file + ": isotope selector contains a button without explicit button type");
      }
    }

    if (file === "chapters/acids-and-bases.html") {
      if (!(await page.locator("[data-i=note]").innerText()).includes("при 25 °C") || !(await page.locator("[data-i=note]").innerText()).includes("другой температуре") || !(await page.locator("[data-i=note]").innerText()).includes("не ограничены строго интервалом 0–14")) {
        errors.push(file + ": Russian pH note must qualify the neutral point by temperature");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=note]").innerText()).includes("at 25 °C") || !(await page.locator("[data-i=note]").innerText()).includes("other temperatures") || !(await page.locator("[data-i=note]").innerText()).includes("not strictly limited to the 0–14 interval")) {
        errors.push(file + ": English pH note must qualify the neutral point by temperature");
      }
      if (!(await page.locator("[data-i=strengthNote]").innerText()).includes("не то же самое, что концентрация") ||
          !(await page.locator("[data-i=pairNote]").innerText()).includes("сопряжённое основание") ||
          !(await page.locator("[data-i=kaNote]").innerText()).includes("Константа кислотности")) {
        errors.push(file + ": Russian acid-base section must distinguish strength from concentration and explain conjugate pairs and Ka");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=strengthNote]").innerText()).includes("not the same as concentration") ||
          !(await page.locator("[data-i=pairNote]").innerText()).includes("conjugate base") ||
          !(await page.locator("[data-i=kaNote]").innerText()).includes("acid-dissociation constant")) {
        errors.push(file + ": English acid-base section must distinguish strength from concentration and explain conjugate pairs and Ka");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=bufferIntro]").innerText()).includes("сопряжённое основание") ||
          !(await page.locator("[data-i=bufferCapacity]").innerText()).includes("конечна") ||
          !(await page.locator("[data-i=bufferFormulaNote]").innerText()).includes("разбавленных растворов")) {
        errors.push(file + ": Russian buffer definition, approximation conditions or finite capacity is missing");
      }
      if (!(await page.locator(".formula").filter({ hasText: "pH ≈ pKₐ" }).count())) {
        errors.push(file + ": Henderson–Hasselbalch relation is missing");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=bufferIntro]").innerText()).includes("conjugate base") ||
          !(await page.locator("[data-i=bufferCapacity]").innerText()).includes("finite") ||
          !(await page.locator("[data-i=bufferFormulaNote]").innerText()).includes("dilute solutions")) {
        errors.push(file + ": English buffer definition, approximation conditions or finite capacity is missing");
      }
      await page.locator("#lang").click();
      const ph = page.locator("#ph");
      const value = page.locator("#value");
      if (await ph.getAttribute("min") !== "0" || await ph.getAttribute("max") !== "14" ||
          await value.getAttribute("aria-live") !== "polite" ||
          !(await ph.getAttribute("aria-valuetext")).includes("нейтральная среда")) {
        errors.push(file + ": pH slider bounds, localized accessible value or live result announcement are missing");
      }
      await ph.fill("0");
      if (!(await value.innerText()).includes("кислая среда")) {
        errors.push(file + ": pH 0 was not classified as acidic");
      }
      await ph.fill("7");
      if (!(await value.innerText()).includes("нейтральная среда")) {
        errors.push(file + ": pH 7 was not classified as neutral");
      }
      await ph.fill("14");
      if (!(await value.innerText()).includes("щелочная среда")) {
        errors.push(file + ": pH 14 was not classified as alkaline");
      }
      await page.locator("#lang").click();
      if (!(await value.innerText()).includes("alkaline solution") ||
          !(await ph.getAttribute("aria-valuetext")).includes("alkaline solution") ||
          await page.locator("html").getAttribute("lang") !== "en") {
        errors.push(file + ": pH result, accessible slider value or document language did not switch to English");
      }
      await page.locator("#lang").click();
      await ph.fill("7");
      await page.locator("#lang").click();
    }

    if (file === "chapters/solutions.html") {
      if (!(await page.locator("[data-i=solubilityIntro]").innerText()).includes("не равна скорости растворения") ||
          !(await page.locator("[data-i=saturatedText]").innerText()).includes("скорости растворения и кристаллизации равны") ||
          !(await page.locator("[data-i=kspCaution]").innerText()).includes("Qₛₚ < Kₛₚ")) {
        errors.push(file + ": Russian solution section must distinguish solubility from rate and explain saturation and Qsp/Ksp");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=solubilityIntro]").innerText()).includes("not the same as the rate") ||
          !(await page.locator("[data-i=saturatedText]").innerText()).includes("rates of dissolution and crystallisation are equal") ||
          !(await page.locator("[data-i=kspCaution]").innerText()).includes("Qₛₚ < Kₛₚ")) {
        errors.push(file + ": English solution section must distinguish solubility from rate and explain saturation and Qsp/Ksp");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=pressurep]").innerText()).includes("парциального давления") ||
          !(await page.locator("[data-i=pressurep]").innerText()).includes("закон Генри")) {
        errors.push(file + ": Russian gas-solubility statement must specify partial pressure and Henry's law");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=pressurep]").innerText()).includes("partial pressure") ||
          !(await page.locator("[data-i=pressurep]").innerText()).includes("Henry")) {
        errors.push(file + ": English gas-solubility statement must specify partial pressure and Henry's law");
      }
      await page.locator("#lang").click();
      await page.locator("#n").fill("1");
      await page.locator("#v").fill("2");
      await page.locator("#n").fill("0");
      if (!(await page.locator("#result").innerText()).includes("0") ||
          !(await page.locator("#feedback").innerText()).includes("Расчёт выполнен")) {
        errors.push(file + ": zero solute amount was not handled as a valid zero concentration");
      }
      await page.locator("#v").fill("0");
      if ((await page.locator("#result").innerText()).trim() !== "c = —") {
        errors.push(file + ": zero solution volume was accepted");
      }
      await page.locator("#n").fill("1");
      await page.locator("#v").fill("2");
      let result = (await page.locator("#result").innerText()).trim();
      if (!result.endsWith("моль/л")) {
        errors.push(file + ": Russian molar-concentration unit is not localized");
      }
      await page.locator("#lang").click();
      result = (await page.locator("#result").innerText()).trim();
      if (!result.endsWith("mol/L")) {
        errors.push(file + ": English molar-concentration unit is incorrect");
      }
      await page.locator("#lang").click();
      await page.locator("#n").fill("1");
      await page.locator("#v").fill("1e-323");
      if ((await page.locator("#result").innerText()).trim() !== "c = —" ||
          !(await page.locator("#feedback").innerText()).includes("числовой диапазон")) {
        errors.push(file + ": numeric overflow was displayed as a valid molar concentration");
      }
      await page.locator("#v").fill("2");
    }

    if (file === "chapters/amount-of-substance.html") {
      await page.locator("#mass").fill("18.015");
      if (!(await page.locator("#moles").innerText()).startsWith("1")) {
        errors.push(file + ": one mole of water was not calculated correctly");
      }
      if (!(await page.locator("[data-i=note]").innerText()).includes("m — масса образца") || !(await page.locator("[data-i=note]").innerText()).includes("ровно Nₐ")) {
        errors.push(file + ": Russian note must distinguish mass, molar mass, amount and exact entities per mole");
      }
      if (await page.locator(".result").getAttribute("aria-live") !== "polite") {
        errors.push(file + ": dynamic amount results are not announced to assistive technology");
      }
      await page.locator("#substance").selectOption("custom");
      await page.locator("#molar").fill("10");
      await page.locator("#mass").fill("20");
      if (!(await page.locator("#moles").innerText()).startsWith("2")) {
        errors.push(file + ": custom molar-mass calculation is incorrect");
      }
      await page.locator("#mass").fill("1e300");
      await page.locator("#molar").fill("1");
      if ((await page.locator("#moles").innerText()).trim() !== "—" || (await page.locator("#count").innerText()).trim() !== "—" || !(await page.locator("#calcFeedback").innerText()).includes("диапазон")) {
        errors.push(file + ": particle-count overflow was not rejected with a clear message");
      }
      await page.locator("#mass").fill("1e-100");
      await page.locator("#molar").fill("1e308");
      if ((await page.locator("#moles").innerText()).trim() !== "—" || !(await page.locator("#calcFeedback").innerText()).includes("диапазон")) {
        errors.push(file + ": underflowed amount-of-substance result was not rejected");
      }
      await page.locator("#molar").fill("10");
      await page.locator("#mass").fill("");
      if ((await page.locator("#moles").innerText()).trim() !== "—" || !(await page.locator("#calcFeedback").innerText()).includes("Введите")) {
        errors.push(file + ": empty mass input retained or displayed a misleading result");
      }
      await page.locator("#mass").fill("20");
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=note]").innerText()).includes("m is sample mass") || !(await page.locator("[data-i=note]").innerText()).includes("exactly Nₐ")) {
        errors.push(file + ": English note must distinguish mass, molar mass, amount and exact entities per mole");
      }
      if (!(await page.locator("#moles").innerText()).endsWith("mol")) {
        errors.push(file + ": amount-of-substance unit did not switch to English");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/organic-chemistry.html") {
      if (!(await page.locator("[data-i=familyNote]").innerText()).includes("фенолы") || !(await page.locator("[data-i=alcp]").innerText()).includes("насыщенным атомом углерода")) {
        errors.push(file + ": Russian alcohol definition must distinguish phenols and carboxylic acids");
      }
      for (const [key, term] of [["acidp","карбоксильную группу"],["aldehydp","альдегидную группу"],["aminep","Производные аммиака"]]) {
        if (!(await page.locator("[data-i="+key+"]").innerText()).toLowerCase().includes(term.toLowerCase())) errors.push(file + ": Russian functional-group definition missing for " + key);
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=familyNote]").innerText()).includes("phenols") || !(await page.locator("[data-i=alcp]").innerText()).includes("saturated carbon atom")) {
        errors.push(file + ": English alcohol definition must distinguish phenols and carboxylic acids");
      }
      for (const [key, term] of [["acidp","carboxyl group"],["aldehydp","aldehyde group"],["aminep","Derivatives of ammonia"]]) {
        if (!(await page.locator("[data-i="+key+"]").innerText()).includes(term)) errors.push(file + ": English functional-group definition missing for " + key);
      }
      await page.locator("#lang").click();
      const organicFamilies = ["Карбоновые кислоты","Альдегиды","Амины","карбоксильную группу","альдегидную группу","метиламин"];
      const organicText = await page.locator("main").innerText();
      if (!organicFamilies.every(term => organicText.includes(term))) {
        errors.push(file + ": Russian functional-group overview is missing an organic family or defining group");
      }
      await page.locator("#lang").click();
      const organicEnglish = await page.locator("main").innerText();
      if (!["Carboxylic acids","Aldehydes","Amines","carboxyl group","aldehyde group","methylamine"].every(term => organicEnglish.includes(term))) {
        errors.push(file + ": English functional-group overview is missing an organic family or defining group");
      }
      await page.locator("#lang").click();
      await page.locator("#n").fill("0");
      await page.locator("#calc").click();
      if ((await page.locator("#result").innerText()).trim() !== "—" || !(await page.locator("#feedback").innerText()).includes("от 1 до 20")) {
        errors.push(file + ": invalid alkane carbon count left a stale formula visible");
      }
      await page.locator("#n").fill("4");
      await page.locator("#calc").click();
      if ((await page.locator("#result").innerText()).trim() !== "C₄H₁₀") {
        errors.push(file + ": valid butane formula was not restored after invalid input");
      }
      await page.locator("#lang").click();
      await page.locator("#n").fill("");
      await page.locator("#calc").click();
      if (!(await page.locator("#feedback").innerText()).includes("Enter an integer")) {
        errors.push(file + ": empty alkane input did not receive English validation feedback");
      }
      await page.locator("#lang").click();
    }

    if (file === "chapters/chemical-reactions.html") {
      if (!(await page.locator("[data-i=classificationNote]").innerText()).includes("не полный перечень") || !(await page.locator("[data-i=chargeNote]").innerText()).includes("электрический заряд")) {
        errors.push(file + ": Russian notes must explain overlapping reaction classes and charge conservation");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=classificationNote]").innerText()).includes("not an exhaustive list") || !(await page.locator("[data-i=chargeNote]").innerText()).includes("total electric charge")) {
        errors.push(file + ": English notes must explain overlapping reaction classes and charge conservation");
      }
      await page.locator("#lang").click();
      await page.locator("#answer").selectOption("2,1,2");
      await page.locator("#check").click();
      if (!(await page.locator("#feedback").innerText()).includes("Верно")) {
        errors.push(file + ": balanced water equation was not accepted");
      }
    }

    if (file === "chapters/chemical-reactions.html") {
      const kineticText = page.locator("main");
      if (!(await page.locator(".formula").filter({hasText:"Δ[A]"}).count())) {
        errors.push(file + ": reaction-rate formula must account for stoichiometric coefficients");
      }
      if (!(await page.locator("[data-i=rateText]").innerText()).includes("стехиометрическими коэффициентами")) {
        errors.push(file + ": Russian reaction-rate definition must account for stoichiometric coefficients");
      }
      for (const phrase of ["Скорость реакции", "Динамическое равновесие", "энергией активации"]) {
        if (!(await kineticText.innerText()).includes(phrase)) {
          errors.push(file + ": Russian kinetics/equilibrium explanation is missing: " + phrase);
        }
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=rateText]").innerText()).includes("stoichiometric coefficients")) {
        errors.push(file + ": English reaction-rate definition must account for stoichiometric coefficients");
      }
      for (const phrase of ["Reaction rate", "Dynamic equilibrium", "activation energy"]) {
        if (!(await kineticText.innerText()).includes(phrase)) {
          errors.push(file + ": English kinetics/equilibrium explanation is missing: " + phrase);
        }
      }
      if (!(await page.locator('[data-i="catalystNote"]').innerText()).includes("equilibrium constant")) {
        errors.push(file + ": English catalyst note must state that a catalyst does not change the equilibrium constant");
      }
      if (!(await page.locator('[data-i="quotientNote"]').innerText()).includes("Q < K") ||
          !(await page.locator('[data-i="leChatelierNote"]').innerText()).includes("partly opposes")) {
        errors.push(file + ": English equilibrium notes must explain Q versus K and the qualitative nature of Le Chatelier's principle");
      }
      await page.locator("#lang").click();
      if (!(await page.locator('[data-i="quotientNote"]').innerText()).includes("Q < K") ||
          !(await page.locator('[data-i="leChatelierNote"]').innerText()).includes("частично ослабить")) {
        errors.push(file + ": Russian equilibrium notes must explain Q versus K and the qualitative nature of Le Chatelier's principle");
      }
    }

    if (file === "chapters/redox.html") {
      if (!(await page.locator("[data-i=lead]").innerText()).includes("перераспределение электронной плотности")) {
        errors.push(file + ": Russian redox introduction must distinguish ionic electron transfer from covalent electron-density redistribution");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=lead]").innerText()).includes("redistribution of electron density")) {
        errors.push(file + ": English redox introduction must distinguish ionic electron transfer from covalent electron-density redistribution");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=stateNote]").innerText()).includes("условный заряд") || !(await page.locator("[data-i=stateNote]").innerText()).includes("реальному электрическому заряду")) {
        errors.push(file + ": Russian explanation must distinguish oxidation state from actual charge");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=stateNote]").innerText()).includes("formal charge") || !(await page.locator("[data-i=stateNote]").innerText()).includes("actual electrical charge")) {
        errors.push(file + ": English explanation must distinguish oxidation state from actual charge");
      }
      await page.locator("#lang").click();
      await page.locator("#ans").selectOption("zn");
      await page.locator("#check").click();
      if (!(await page.locator("#feedback").innerText()).includes("Верно")) {
        errors.push(file + ": zinc was not accepted as the reducing agent");
      }
    }

    if (file === "chapters/organic-chemistry.html") {
      await page.locator("#n").fill("4");
      await page.locator("#calc").click();
      if ((await page.locator("#result").innerText()).trim() !== "C₄H₁₀") {
        errors.push(file + ": alkane formula for n=4 is incorrect");
      }
      await page.locator("#n").fill("0");
      await page.locator("#calc").click();
      if (!(await page.locator("#feedback").innerText()).includes("от 1 до 20")) {
        errors.push(file + ": invalid alkane input was not rejected clearly");
      }
    }

    if (["chapters/amount-of-substance.html", "chapters/chemical-reactions.html", "chapters/redox.html", "chapters/organic-chemistry.html", "chapters/chemistry-of-life.html"].includes(file)) {
      if (await page.locator("button").evaluateAll(items => items.some(button => button.type !== "button"))) {
        errors.push(file + ": a button is missing an explicit button type");
      }
    }

    if (file === "periodic-table.html") {
      const elementButtons = page.locator("#table button[data-id], #lanth button[data-id], #act button[data-id]");
      const elementIds = await elementButtons.evaluateAll(items => items.map(button => Number(button.dataset.id)));
      if (elementIds.length !== 118 || new Set(elementIds).size !== 118 || Array.from({length:118}, (_, index) => index + 1).some(id => !elementIds.includes(id))) {
        errors.push(file + ": periodic table must render each atomic number 1–118 exactly once across all blocks");
      }
      if (await page.locator("#table button[data-id]").evaluateAll(items => items.some(button => !button.querySelector(".sym")?.textContent.trim() || !button.querySelector(".mass")?.textContent.trim()))) {
        errors.push(file + ": a main-table element is missing its symbol or atomic-mass display");
      }
      if (!(await page.locator("[data-t=classificationNote]").innerText()).includes("границы классификации")) {
        errors.push(file + ": Russian periodic-table category note is missing");
      }
      if (!(await page.locator("[data-t=massNote]").innerText()).includes("массовое число") ||
          !(await page.locator("[data-t=massNote]").innerText()).includes("не средняя относительная атомная масса")) {
        errors.push(file + ": Russian periodic-table note must explain bracketed isotope mass numbers");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-t=classificationNote]").innerText()).includes("metalloid")) {
        errors.push(file + ": English periodic-table category note is missing");
      }
      if (!(await page.locator("[data-t=massNote]").innerText()).includes("mass number") ||
          !(await page.locator("[data-t=massNote]").innerText()).includes("not average relative atomic masses")) {
        errors.push(file + ": English periodic-table note must explain bracketed isotope mass numbers");
      }
      await page.locator("#lang").click();
      if (!await page.locator("#search").getAttribute("aria-label") ||
          !await page.locator("#category").getAttribute("aria-label") ||
          !await page.locator("#group").getAttribute("aria-label")) {
        errors.push(file + ": search and filters need accessible names");
      }
      await page.locator("#search").fill("oxygen");
      if (await page.locator("#table button[data-id]").count() !== 1) {
        errors.push(file + ": element search did not narrow results to oxygen");
      }
      await page.locator("#search").fill("");
      if (await page.locator("#table button[data-id]").evaluateAll(items => items.some(button => button.type !== "button"))) {
        errors.push(file + ": generated element buttons need explicit button type");
      }
      if (await page.locator('#table button[data-id="1"]').getAttribute("aria-pressed") !== "true") {
        errors.push(file + ": initial hydrogen selection is not exposed to assistive technology");
      }
      await page.locator('#table button[data-id="8"]').click();
      if (!(await page.locator("#detail").innerText()).toLowerCase().includes("oxygen") ||
          await page.locator('#table button[data-id="8"]').getAttribute("aria-pressed") !== "true" ||
          await page.locator('#table button[data-id="1"]').getAttribute("aria-pressed") !== "false") {
        errors.push(file + ": selecting oxygen must update details and the accessible selected state");
      }
      await page.locator('#lanth button[data-id="58"]').click();
      if (!(await page.locator("#detail").innerText()).includes("f-блок")) {
        errors.push(file + ": cerium must be identified as an f-block element, not assigned a misleading group number");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("#detail").innerText()).includes("f-block")) {
        errors.push(file + ": f-block designation is missing in English");
      }
      await page.locator("#lang").click();
      await page.locator("#group").selectOption("4");
      if (await page.locator("#lanth button[data-id]").count() !== 0 || await page.locator("#act button[data-id]").count() !== 0) {
        errors.push(file + ": group filter incorrectly assigns f-block elements to numbered groups");
      }
      await page.locator("#group").selectOption("all");
      await page.locator('#lanth button[data-id="58"]').click();
      if (!(await page.locator("#detail").innerText()).includes("наиболее долгоживущего известного изотопа")) {
        errors.push(file + ": bracketed isotope mass-number explanation is missing");
      }
    }

    if (file === "molecule-lab.html") {
      await page.locator("#choose").selectOption("co2");
      if (!(await page.locator("#formula").innerText()).includes("CO₂")) errors.push(file + ": molecule selector failed");
      await page.locator("#reset").click();
      await page.locator("#spin").click();
      await page.locator("#spin").click();
    }

    if (file === "molecule-lab.html") {
      const canvas = page.locator("#molecule");
      if (await canvas.getAttribute("tabindex") !== "0" || await canvas.getAttribute("role") !== "img") {
        errors.push(file + ": molecule canvas is not keyboard-focusable and exposed as a graphic");
      }
      if (!(await canvas.getAttribute("aria-label")).includes("стрелками")) {
        errors.push(file + ": Russian screen-reader label omits keyboard rotation instructions");
      }
      await page.locator("#lang").click();
      if (!(await canvas.getAttribute("aria-label")).includes("arrow keys")) {
        errors.push(file + ": English screen-reader label omits keyboard rotation instructions");
      }
      await page.locator("#lang").click();
      await canvas.focus();
      await page.keyboard.press("ArrowRight");
      if (!(await canvas.evaluate(el => el.matches(":focus")))) {
        errors.push(file + ": molecule canvas loses keyboard focus during rotation");
      }
    }

    if (file === "virtual-lab.html") {
      await page.locator("#add").click();
      if (!(await page.locator("#status").innerText()).trim()) errors.push(file + ": experiment did not report a result");
      if (!(await page.locator("#baseOut").innerText()).trim().endsWith("мл") ||
          !(await page.locator("#status").innerText()).trim().endsWith("5 мл")) {
        errors.push(file + ": Russian volume units are not localized consistently");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("#baseOut").innerText()).trim().endsWith("mL") ||
          !(await page.locator("#status").innerText()).trim().endsWith("5 mL")) {
        errors.push(file + ": English volume units are not localized consistently");
      }
      await page.locator("#lang").click();
      await page.locator("#reset").click();
      await page.locator("#acidC").fill("0");
      await page.locator("#acidC").dispatchEvent("input");
      if (!(await page.locator("#ph").innerText()).includes("—") ||
          (await page.locator("#pin").evaluate(el => el.style.left)) !== "50%" ||
          (await page.locator("#beakerLabel").innerText()).trim() !== "—") {
        errors.push(file + ": invalid input left stale visual results in the beaker");
      }
      await page.locator("#acidC").fill("0.1");
      await page.locator("#acidC").dispatchEvent("input");
      await page.locator("#baseV").fill("100");
      await page.locator("#baseV").dispatchEvent("input");
      if ((await page.locator("#ph").innerText()).trim() !== "pH = 7.00") {
        errors.push(file + ": exact strong acid/base equivalence did not produce pH 7");
      }
      await page.locator("#baseC").fill("0.100000000001");
      await page.locator("#baseC").dispatchEvent("input");
      const nearEquivalencePH = Number((await page.locator("#ph").innerText()).replace("pH = ", ""));
      if (!Number.isFinite(nearEquivalencePH) || nearEquivalencePH < 6.9 || nearEquivalencePH > 7.1) {
        errors.push(file + ": pH is discontinuous near equivalence because water autoionisation is not represented");
      }
      await page.locator("#reset").click();
    }

    if (file === "reaction-trainer.html") {
      const fields = page.locator('#equation input[type="number"]');
      if (await fields.count() < 2) errors.push(file + ": coefficient inputs were not rendered");
      else {
        if (await fields.first().getAttribute("aria-label") !== "Коэффициент 1" || await page.locator("#progress").getAttribute("role") !== "progressbar" || await page.locator("#progress").getAttribute("aria-valuenow") !== "0") {
          errors.push(file + ": Russian coefficient labels or progressbar semantics are missing");
        }
        await page.locator("#lang").click();
        if (await page.locator('#equation input[type="number"]').first().getAttribute("aria-label") !== "Coefficient 1" || await page.locator("#progress").getAttribute("aria-label") !== "Tasks completed") {
          errors.push(file + ": English coefficient labels or progressbar label are missing");
        }
        await page.locator("#lang").click();
        await fields.first().fill("1");
        await page.locator("#check").click();
        if (!(await page.locator("#feedback").innerText()).trim()) errors.push(file + ": answer feedback was not shown");

        const solutions = [[2, 1, 2], [1, 3, 2], [4, 3, 2], [2, 6, 2, 3], [2, 1, 1, 2], [1, 5, 3, 4]];
        for (let i = 0; i < solutions.length; i++) {
          if (i > 0) await page.locator("#next").click();
          const currentFields = page.locator('#equation input[type="number"]');
          if (await currentFields.count() !== solutions[i].length) {
            errors.push(file + ": unexpected coefficient count in task " + (i + 1));
            break;
          }
          for (let j = 0; j < solutions[i].length; j++) {
            await currentFields.nth(j).fill(String(solutions[i][j]));
          }
          await page.locator("#check").click();
          if (await page.locator("#progress").getAttribute("aria-valuenow") !== String(i+1)) {
            errors.push(file + ": progressbar did not advance after task " + (i + 1));
          }
          if (!(await page.locator("#feedback").innerText()).includes("Верно")) {
            errors.push(file + ": correct solution was rejected in task " + (i + 1));
            break;
          }
        }
        await page.locator("#next").click();
        const history = await page.evaluate(() => JSON.parse(localStorage.getItem("atlas-chemistry-trainer-v1-history-v1") || "[]"));
        if (!Array.isArray(history) || history.length !== 1 || history[0].total !== 6) {
          errors.push(file + ": completed trainer attempt was not saved exactly once");
        }
      }
    }

    if (file === "stoichiometry.html") {
      const before = (await page.locator("#theory").innerText()).trim();
      await page.locator("#na").fill("1");
      await page.locator("#na").dispatchEvent("input");
      const after = (await page.locator("#theory").innerText()).trim();
      if (before === after) errors.push(file + ": changing amount did not update calculation");

      await page.locator("#a").fill("1");
      await page.locator("#b").fill("1");
      await page.locator("#c").fill("1");
      await page.locator("#na").fill("1");
      await page.locator("#nb").fill("1");
      await page.locator("#actual").fill("");
      await page.locator("#na").dispatchEvent("input");
      if (!(await page.locator("#left").innerText()).includes("Избытка реагента нет")) {
        errors.push(file + ": exact stoichiometric proportions must report that no excess reactant remains");
      }

      await page.locator("#a").fill("1");
      await page.locator("#b").fill("1");
      await page.locator("#c").fill("1");
      await page.locator("#na").fill("0.000000000001");
      await page.locator("#nb").fill("0.000000001");
      await page.locator("#actual").fill("");
      await page.locator("#na").dispatchEvent("input");
      const traceLimit = (await page.locator("#limit").innerText()).trim();
      const traceRemainder = (await page.locator("#left").innerText()).trim();
      if (traceLimit !== "A" || !traceRemainder.replace(",", ".").includes("0.000000000999")) {
        errors.push(file + ": trace quantities expected limiting A and 9.99e-10 mol B remaining; got " + traceLimit + " / " + traceRemainder);
      }

      await page.locator("#na").fill("");
      await page.locator("#na").dispatchEvent("input");
      if (!(await page.locator("#explain").innerText()).includes("количества")) {
        errors.push(file + ": empty reactant amount was silently treated as zero");
      }
      await page.locator("#na").fill("0");
      await page.locator("#nb").fill("2");
      await page.locator("#na").dispatchEvent("input");
      if ((await page.locator("#limit").innerText()).trim() !== "A" ||
          !(await page.locator("#left").innerText()).includes("2 mol")) {
        errors.push(file + ": zero amount of one reactant did not identify it as limiting");
      }

      await page.locator("#na").fill("0");
      await page.locator("#nb").fill("0");
      await page.locator("#actual").fill("0");
      await page.locator("#na").dispatchEvent("input");
      if (!(await page.locator("#yield").innerText()).includes("нулю")) {
        errors.push(file + ": zero theoretical product amount was reported as a numeric percentage");
      }

      await page.locator("#na").fill("1");
      await page.locator("#nb").fill("1");
      await page.locator("#actual").fill("1.01");
      await page.locator("#na").dispatchEvent("input");
      if (!(await page.locator("#yield").innerText()).includes("превышает")) {
        errors.push(file + ": actual yield above theoretical yield was not rejected");
      }

      await page.locator("#a").fill("0");
      await page.locator("#a").dispatchEvent("input");
      if (!(await page.locator("#explain").innerText()).includes("коэффициенты")) {
        errors.push(file + ": zero stoichiometric coefficient was not rejected");
      }
      await page.locator("#a").fill("1001");
      await page.locator("#a").dispatchEvent("input");
      if (!(await page.locator("#explain").innerText()).includes("коэффициенты")) {
        errors.push(file + ": coefficient above the supported maximum was not rejected");
      }
      await page.locator("#a").fill("1");
      await page.locator("#na").fill("1e308");
      await page.locator("#b").fill("1");
      await page.locator("#c").fill("1000");
      await page.locator("#nb").fill("1e308");
      await page.locator("#na").dispatchEvent("input");
      if ((await page.locator("#theory").innerText()).trim() !== "—" || !(await page.locator("#explain").innerText()).includes("числовой диапазон")) {
        errors.push(file + ": overflowed theoretical yield was not rejected");
      }
      await page.locator("#a").fill("1");
      await page.locator("#c").fill("1");
      await page.locator("#na").fill("1e-300");
      await page.locator("#nb").fill("1e300");
      await page.locator("#actual").fill("1e-10");
      await page.locator("#na").dispatchEvent("input");
      if (!(await page.locator("#yield").innerText()).includes("превышает")) {
        errors.push(file + ": actual yield far above a tiny theoretical yield was not rejected using a product-scaled tolerance");
      }
      await page.locator("#a").fill("1000");
      await page.locator("#na").fill("1e-323");
      await page.locator("#actual").fill("");
      await page.locator("#na").dispatchEvent("input");
      if ((await page.locator("#theory").innerText()).trim() !== "—" || !(await page.locator("#explain").innerText()).includes("числовой диапазон")) {
        errors.push(file + ": underflowed reactant ratio was not rejected");
      }
    }

    if (file === "chapters/chemistry-of-life.html") {
      if (!(await page.locator("[data-i=lipidNote]").innerText()).includes("не образуют единого класса полимеров")) {
        errors.push(file + ": Russian lipid note must distinguish lipids from polymer classes");
      }
      await page.locator("#lang").click();
      if (!(await page.locator("[data-i=lipidNote]").innerText()).includes("not one class of polymers")) {
        errors.push(file + ": English lipid note must distinguish lipids from polymer classes");
      }
      await page.locator("#lang").click();
      await page.locator("#fraction").fill("0.042");
      await page.locator("#fraction").dispatchEvent("input");
      if ((await page.locator("#ppm").innerText()).replace(/\s/g, "") !== "420ppm" || !(await page.locator("[data-i=modelNote]").innerText()).includes("не текущие измерения")) {
        errors.push(file + ": initial CO2 output=" + (await page.locator("#ppm").innerText()) + "; disclaimer=" + (await page.locator("[data-i=modelNote]").innerText()));
      }
      await page.locator("#fraction").fill("1");
      await page.locator("#fraction").dispatchEvent("input");
      if ((await page.locator("#ppm").innerText()).replace(/\s/g, "") !== "10000ppm") {
        errors.push(file + ": 1 percent CO2 fraction should convert to 10,000 ppm in Russian");
      }
      await page.locator("#lang").click();
      await page.locator("#fraction").fill("0.5");
      await page.locator("#fraction").dispatchEvent("input");
      if ((await page.locator("#ppm").innerText()).replace(/\s/g, "") !== "5,000ppm" || !(await page.locator("[data-i=modelNote]").innerText()).includes("not a live atmospheric measurement")) {
        errors.push(file + ": English CO2 fraction conversion or disclaimer is incorrect");
      }
      await page.locator("#lang").click();
      await page.locator("#fraction").fill("0.05");
      await page.locator("#fraction").dispatchEvent("input");
      if ((await page.locator("#ppm").innerText()).replace(/\s/g, "") !== "500ppm" ||
          await page.locator("#ppm").getAttribute("aria-live") !== "polite") {
        errors.push(file + ": 0.05 percent must produce an accessible 500 ppm result; got " + (await page.locator("#ppm").innerText()) + "; aria-live=" + (await page.locator("#ppm").getAttribute("aria-live")) + "; language=" + (await page.locator("html").getAttribute("lang")));
      }
    }

    if (file === "gas-laws.html") {
      const before = (await page.locator("#pressureValue").innerText()).trim();
      if (Math.abs(parseFloat(before.replace(",", ".")) - 101.56) > 0.01) {
        errors.push(file + ": default pressure must match PV=nRT at 1.00 mol, 24.0 L and 20 °C");
      }
      const particle = page.locator(".particle").first();
      const initialParticleTransform = await particle.evaluate(el => getComputedStyle(el).transform);
      await page.locator("#t").fill("100");
      await page.locator("#t").dispatchEvent("input");
      const after = (await page.locator("#pressureValue").innerText()).trim();
      const expectedHeatedPressure = 8.314462618 * 373.15 / 24;
      if (Math.abs(parseFloat(after.replace(",", ".")) - expectedHeatedPressure) > 0.01) {
        errors.push(file + ": pressure at 100 °C must use absolute temperature in kelvin");
      }
      const heatedParticleTransform = await particle.evaluate(el => getComputedStyle(el).transform);
      if (before === after) errors.push(file + ": temperature change did not update pressure");
      if (initialParticleTransform !== heatedParticleTransform) {
        errors.push(file + ": particle size appears to change with temperature, suggesting molecules expand when heated");
      }
    }

    if (file === "chemistry-constants.html") {
      const regions = page.locator(".panel[role=region]");
      if (await regions.count() !== 3 || await regions.first().getAttribute("tabindex") !== "0" || !(await regions.first().getAttribute("aria-label")).includes("Прокручиваемая")) {
        errors.push(file + ": reference tables are not keyboard-scrollable labeled regions in Russian");
      }
      await page.locator("#lang").click();
      if (!(await regions.first().getAttribute("aria-label")).includes("Scrollable")) {
        errors.push(file + ": reference-table region label did not switch to English");
      }
      await page.locator("#lang").click();
    }

    if (file === "glossary.html") {
      if (await page.locator(".term").count() !== 99) {
        errors.push(file + ": expected 99 bilingual chemistry glossary entries");
      }
      if (await page.locator("#category").getAttribute("aria-label") !== "Категория") {
        errors.push(file + ": Russian glossary category selector needs a localized accessible name");
      }
      await page.locator("#search").fill("лимитирующий реагент");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Реагент")) {
        errors.push(file + ": Russian glossary search did not find the limiting-reactant definition");
      }
      await page.locator("#lang").click();
      if (await page.locator("#category").getAttribute("aria-label") !== "Category") {
        errors.push(file + ": English glossary category selector needs a localized accessible name");
      }
      await page.locator("#search").fill("equivalence point");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Equivalence point")) {
        errors.push(file + ": English glossary search did not find the equivalence-point definition");
      }
      await page.locator("#category").selectOption("solution");
      if (await page.locator(".term").count() !== 1) {
        errors.push(file + ": glossary topic filter did not isolate the equivalence-point entry");
      }
      await page.locator("#lang").click();
      await page.locator("#category").selectOption("all");
      await page.locator("#lang").click();
      await page.locator("#search").fill("Henderson–Hasselbalch");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Henderson")) {
        errors.push(file + ": glossary search did not find the Henderson–Hasselbalch equation");
      }
      await page.locator("#search").fill("galvanic cell");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Galvanic cell")) {
        errors.push(file + ": glossary search did not find the galvanic-cell definition");
      }
      await page.locator("#search").fill("enzyme");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Enzyme")) {
        errors.push(file + ": glossary search did not find the enzyme definition");
      }
      await page.locator("#search").fill("electrolysis");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Electrolysis")) {
        errors.push(file + ": glossary search did not find the electrolysis definition");
      }
      await page.locator("#search").fill("solubility product");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Solubility product")) {
        errors.push(file + ": glossary search did not find the solubility-product definition");
      }
      await page.locator("#search").fill("hydrogen bond");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Hydrogen bond")) {
        errors.push(file + ": glossary search did not find the hydrogen-bond definition");
      }
      await page.locator("#search").fill("dipole moment");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Dipole moment")) {
        errors.push(file + ": glossary search did not find the dipole-moment definition");
      }
      await page.locator("#search").fill("nucleotide");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Nucleotide")) {
        errors.push(file + ": glossary search did not find the nucleotide definition");
      }
      await page.locator("#search").fill("carbonyl group");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Carbonyl group")) {
        errors.push(file + ": glossary search did not find the carbonyl-group definition");
      }
      await page.locator("#search").fill("amount of substance");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Amount of substance")) {
        errors.push(file + ": glossary search did not find the amount-of-substance definition");
      }
      await page.locator("#search").fill("formula unit");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Formula unit")) {
        errors.push(file + ": glossary search did not find the formula-unit definition");
      }
      await page.locator("#search").fill("peptide bond");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Peptide bond")) {
        errors.push(file + ": glossary search did not find the peptide-bond definition");
      }
      await page.locator("#search").fill("electron balance");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Electron balance")) {
        errors.push(file + ": glossary search did not find the electron-balance definition");
      }
      await page.locator("#search").fill("Hückel rule");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Hückel rule")) {
        errors.push(file + ": glossary search did not find the Hückel-rule definition");
      }
      await page.locator("#search").fill("homologous series");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Homologous series")) {
        errors.push(file + ": glossary search did not find the homologous-series definition");
      }
      await page.locator("#search").fill("ocean acidification");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Ocean acidification")) {
        errors.push(file + ": glossary search did not find the ocean-acidification definition");
      }
      await page.locator("#search").fill("reaction quotient");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Reaction quotient")) {
        errors.push(file + ": glossary search did not find the reaction-quotient definition");
      }
      await page.locator("#search").fill("standard state");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Standard state")) {
        errors.push(file + ": glossary search did not find the standard-state definition");
      }
      await page.locator("#search").fill("supersaturated solution");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Supersaturated solution")) {
        errors.push(file + ": glossary search did not find the supersaturated-solution definition");
      }
      await page.locator("#search").fill("relative atomic mass");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Relative atomic mass")) {
        errors.push(file + ": English glossary is missing the relative atomic mass definition");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("буферный раствор");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("изменению pH")) {
        errors.push(file + ": Russian glossary is missing the buffer-solution definition");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("energy barrier");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("energy barrier")) {
        errors.push(file + ": English glossary is missing the activation-energy definition");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("энергетический барьер");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("Энергетический барьер")) {
        errors.push(file + ": Russian glossary is missing the activation-energy definition");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("empirical formula");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("simplest whole-number ratio")) {
        errors.push(file + ": English glossary is missing the empirical-formula definition");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("массовое число");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("протонов и нейтронов")) {
        errors.push(file + ": Russian glossary is missing the mass-number definition");
      }
      await page.locator("#search").fill("catalyst");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("альтернативный путь")) {
        errors.push(file + ": Russian catalyst definition does not explain its alternative reaction pathway");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("catalyst");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("lower activation energy")) {
        errors.push(file + ": English catalyst definition does not explain its alternative reaction pathway");
      }
      await page.locator("#search").fill("energy barrier");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("energy barrier")) {
        errors.push(file + ": English glossary is missing the activation-energy definition");
      }
      await page.locator("#search").fill("chemical equilibrium");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("forward and reverse reaction rates are equal")) {
        errors.push(file + ": English glossary is missing the dynamic-equilibrium definition");
      }
      await page.locator("#search").fill("electron density away");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("electron density away")) {
        errors.push(file + ": English oxidation definition must cover covalent electron-density shifts");
      }
      await page.locator("#search").fill("electron density towards");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("electron density towards")) {
        errors.push(file + ": English reduction definition must cover covalent electron-density shifts");
      }
      await page.locator("#lang").click();
      await page.locator("#search").fill("окисление");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("смещение электронной плотности от атома")) {
        errors.push(file + ": Russian oxidation definition must cover covalent electron-density shifts");
      }
      await page.locator("#search").fill("восстановление");
      if (await page.locator(".term").count() !== 1 || !(await page.locator(".term").first().innerText()).includes("смещение электронной плотности к атому")) {
        errors.push(file + ": Russian reduction definition must cover covalent electron-density shifts");
      }
    }

    if (file === "knowledge-check.html") {
      const questionCount = await page.locator("#quiz .question").count();
      if (questionCount !== 15) {
        errors.push(file + ": expected 15 quiz questions, found " + questionCount);
      } else {
        const newRussianQuestions = [
          ["#q10 h2", "Q < K"],
          ["#q11 h2", "Qₛₚ > Kₛₚ"],
          ["#q12 h2", "правилу Хюккеля"],
          ["#q13 h2", "структурных изомеров"],
          ["#q14 h2", "поглощение CO₂ океаном"]
        ];
        for (const [selector, phrase] of newRussianQuestions) {
          if (!(await page.locator(selector).innerText()).includes(phrase)) errors.push(file + ": missing Russian advanced topic " + phrase);
        }
        await page.locator("#lang").click();
        const newEnglishQuestions = [
          ["#q10 h2", "Q < K"],
          ["#q11 h2", "Qₛₚ > Kₛₚ"],
          ["#q12 h2", "Hückel’s rule"],
          ["#q13 h2", "structural isomers"],
          ["#q14 h2", "ocean uptake of CO₂"]
        ];
        for (const [selector, phrase] of newEnglishQuestions) {
          if (!(await page.locator(selector).innerText()).includes(phrase)) errors.push(file + ": missing English advanced topic " + phrase);
        }
        await page.locator("#lang").click();
        for (let i = 0; i < questionCount; i++) {
          await page.locator("#q" + i + ' input[type="radio"]').first().check();
        }
        await page.locator("#finish").click();
        if (!(await page.locator("#score").innerText()).trim()) errors.push(file + ": quiz score was not produced");
        if (!(await page.locator("#finish").isDisabled())) errors.push(file + ": completed quiz finish button was not locked");
        const history = await page.evaluate(() => JSON.parse(localStorage.getItem("atlas-chemistry-quiz-v1-history-v1") || "[]"));
        if (!Array.isArray(history) || history.length !== 1 || history[0].total !== 15) {
          errors.push(file + ": completed quiz attempt was not saved exactly once");
        }
        await page.locator("#reset").click();
      }
    }
  }
} finally {
  await browser.close();
}

if (errors.length) {
  console.error("Chemistry browser smoke checks failed:");
  for (const error of errors) console.error(" - " + error);
  process.exit(1);
}
console.log("Chemistry browser smoke checks passed: " + pages.length + " pages loaded at 390px; " + languageChecks + " language toggles and key interactive workflows checked; no uncaught page errors.");
