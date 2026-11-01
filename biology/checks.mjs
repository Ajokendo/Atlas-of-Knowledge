import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const pages = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.isFile() && entry.name.endsWith(".html")) pages.push(full);
  }
}
walk(root);
const errors = [];
let links = 0, scripts = 0, buttons = 0;
for (const file of pages) {
  const html = fs.readFileSync(file, "utf8");
  const rel = path.relative(root, file);
  if (!/<html\b[^>]*lang=["'][^"']+["']/i.test(html)) errors.push(rel + ": missing html lang");
  if (!/<meta\s+name=["']viewport["']/i.test(html)) errors.push(rel + ": missing viewport");
  const ids = [...html.matchAll(/\bid=["']([^"']+)["']/gi)].map(m => m[1]);
  if (new Set(ids).size !== ids.length) errors.push(rel + ": duplicate HTML id");
  const ruMarkers = [...html.matchAll(/class=["'][^"']*\bru\b[^"']*["']/gi)].length;
  const enMarkers = [...html.matchAll(/class=["'][^"']*\ben\b[^"']*["']/gi)].length;
  if (ruMarkers === 0 || enMarkers === 0 || ruMarkers !== enMarkers) {
    errors.push(rel + ": Russian and English content markers must be present in balanced pairs");
  }
  if (!/(?:document\.documentElement\.lang|setAttribute\(["']lang["'])/.test(html)) {
    errors.push(rel + ": missing document-language update for the RU/EN switch");
  }
  for (const svg of html.matchAll(/<svg\b([^>]*)>/gi)) {
    if (!/\baria-label\s*=|\baria-labelledby\s*=|\brole=["']img["']/.test(svg[1])) {
      errors.push(rel + ": SVG must expose an accessible name");
    }
  }
  for (const anchor of html.matchAll(/<a\b([^>]*\bhref=["']https?:\/\/[^"']+["'][^>]*)>/gi)) {
    if (/\btarget=["']_blank["']/i.test(anchor[1]) && !/\brel=["'][^"']*noopener/i.test(anchor[1])) {
      errors.push(rel + ": external link opening a new tab must include rel=noopener");
    }
  }
  for (const m of html.matchAll(/<button\b([^>]*)>/gi)) {
    buttons++;
    if (!/\btype=["']button["']/i.test(m[1])) errors.push(rel + ": button without explicit type=button");
  }
  for (const m of html.matchAll(/<(?:a|img|script|link|source)[^>]*?\b(href|src)=["']([^"']+)["'][^>]*>/gi)) {
    const value = m[2].trim();
    if (!value || /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(value)) continue;
    const target = path.resolve(path.dirname(file), decodeURIComponent(value.split("#")[0].split("?")[0]));
    links++;
    if (!fs.existsSync(target)) errors.push(rel + ": broken local path " + value);
  }
  for (const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (!m[2].trim() || /\bsrc=/i.test(m[1])) continue;
    try { new vm.Script(m[2], { filename: rel + ":inline-script" }); scripts++; }
    catch (e) { errors.push(rel + ": JS syntax " + e.message); }
  }
}

// Check bilingual block alignment, numeric parity and scientific-name parity.
const plainText = value => value.replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
const numericTokens = value => [...plainText(value).matchAll(/\d{1,3}(?:[ ,\u00a0]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?/g)]
  .map(m => m[0].replace(/[^\d]/g, "")).sort();
const latinNameSet = blocks => [...new Set([...blocks.join(" ").matchAll(/<i class=["']latin["']>([^<]+)<\/i>/gi)].map(m => m[1].trim()))].sort();
for (const file of pages) {
  const html = fs.readFileSync(file, "utf8");
  const rel = path.relative(root, file);
  const ruBlocks = [...html.matchAll(/<span class=["']ru["']>([\s\S]*?)<\/span>/gi)].map(m => m[1]);
  const enBlocks = [...html.matchAll(/<span class=["']en["']>([\s\S]*?)<\/span>/gi)].map(m => m[1]);
  if (ruBlocks.length !== enBlocks.length) errors.push(rel + ": RU/EN block counts differ");
  for (let i = 0; i < Math.min(ruBlocks.length, enBlocks.length); i++) {
    if (numericTokens(ruBlocks[i]).join("|") !== numericTokens(enBlocks[i]).join("|")) {
      errors.push(rel + ": numeric evidence differs between RU/EN block pair " + i);
    }
  }
  if (latinNameSet(ruBlocks).join("|") !== latinNameSet(enBlocks).join("|")) {
    errors.push(rel + ": scientific-name sets differ between Russian and English content");
  }
}
// Validate local HTML fragments as well as local file paths.
for (const file of pages) {
  const html = fs.readFileSync(file, "utf8");
  for (const anchor of html.matchAll(/<a\b[^>]*\bhref=["']([^"']+)["'][^>]*>/gi)) {
    const href = anchor[1].trim();
    if (!href || /^(?:https?:|mailto:|tel:|data:|javascript:)/i.test(href)) continue;
    const [rawPath, rawFragment] = href.split("#", 2);
    if (!rawFragment) continue;
    const localPath = decodeURIComponent((rawPath || "").split("?")[0] || path.basename(file));
    const target = path.resolve(path.dirname(file), localPath);
    if (!target.endsWith(".html") || !fs.existsSync(target)) continue;
    const targetHtml = fs.readFileSync(target, "utf8");
    const targetIds = new Set([...targetHtml.matchAll(/\bid=["']([^"']+)["']/gi)].map(m => m[1]));
    if (!targetIds.has(decodeURIComponent(rawFragment))) {
      errors.push(path.relative(root, file) + ": broken local HTML fragment " + href);
    }
  }
}
if (pages.length !== 13) errors.push("Expected 13 Biology HTML pages; found " + pages.length);

// Keep the 52 planned image anchors and their central production map in sync.
const imageMapPath = path.join(root, "IMAGE_INSERTION_MAP.md");
if (!fs.existsSync(imageMapPath)) {
  errors.push("Missing Biology IMAGE_INSERTION_MAP.md");
} else {
  const imageMap = fs.readFileSync(imageMapPath, "utf8");
  const mappedRows = [...imageMap.matchAll(/^[|] `(image-brief-[^`]+)` [|] `([^`]+)` [|] [^|]*[|] `([^`]+)` [|]/gm)];
  const mappedIds = mappedRows.map(m => m[1]);
  const mappedFiles = mappedRows.map(m => m[3]);
  const pageIds = pages.flatMap(file => {
    const html = fs.readFileSync(file, "utf8");
    return [...html.matchAll(/id=["'](image-brief-[^"']+)["']/gi)].map(m => m[1]);
  });
  const mappedSet = new Set(mappedIds);
  const pageSet = new Set(pageIds);
  if (mappedRows.length !== 52) errors.push("Expected 52 image insertion-map rows; found " + mappedRows.length);
  if (mappedSet.size !== mappedIds.length) errors.push("Image insertion map contains duplicate anchor IDs");
  if (new Set(mappedFiles).size !== mappedFiles.length) errors.push("Image insertion map contains duplicate target filenames");
  if (pageSet.size !== pageIds.length) errors.push("Biology pages contain duplicate image placeholder IDs");
  for (const id of mappedIds) if (!pageSet.has(id)) errors.push("Image map anchor is missing from Biology pages: " + id);
  for (const id of pageIds) if (!mappedSet.has(id)) errors.push("Biology page image placeholder is missing from insertion map: " + id);
}
const coreChapters = [
  "botany.html", "zoology.html", "cell-biology.html", "anatomy.html",
  "genetics.html", "microbiology.html", "ecology.html", "evolution.html",
  "biochemistry.html", "systematics.html"
];
for (const chapter of coreChapters) {
  const file = path.join(root, "chapters", chapter);
  const html = fs.readFileSync(file, "utf8");
  if (!html.includes('document.getElementById("quiz-next").hidden=!quizAnswered;') ||
      !html.includes('quizAnswered=false;renderQuiz()});')) {
    errors.push("chapters/" + chapter + ": quiz answer state must persist across language switches and reset only when advancing");
  }
}
for (const chapter of coreChapters) {
  const file = path.join(root, "chapters", chapter);
  const html = fs.readFileSync(file, "utf8");
  const match = html.match(/<section\b[^>]*class=["'][^"']*\breferences\b[^"']*["'][^>]*>([\s\S]*?)<\/section>/i);
  if (!match) {
    errors.push("chapters/" + chapter + ": missing selected references section");
    continue;
  }
  const sourceLinks = [...match[1].matchAll(/<a\b[^>]*href=["']https?:/gi)];
  if (sourceLinks.length < 2) errors.push("chapters/" + chapter + ": fewer than two external references");
  if (!/<span\s+class=["'][^"']*\bru\b/i.test(match[1])) errors.push("chapters/" + chapter + ": references missing Russian description");
  if (!/<span\s+class=["'][^"']*\ben\b/i.test(match[1])) errors.push("chapters/" + chapter + ": references missing English description");
}
const floraKyrgyzstanFile = fs.readFileSync(path.join(root, "chapters", "flora-kyrgyzstan.html"), "utf8");
if (!floraKyrgyzstanFile.includes("4 043 видов") || !floraKyrgyzstanFile.includes("4,043 species")) errors.push("chapters/flora-kyrgyzstan.html: the 2025 national vascular-plant total must be stated bilingually and with its scope");
if (!floraKyrgyzstanFile.includes("Sennikov и соавторов (2025)") || !floraKyrgyzstanFile.includes("Sennikov and colleagues (2025)") || !floraKyrgyzstanFile.includes("doi.org/10.1002/njb.04731")) errors.push("chapters/flora-kyrgyzstan.html: the dated 2025 peer-reviewed vascular-flora checklist must be attributed and linked");
if (!floraKyrgyzstanFile.includes("не число всех организмов") || !floraKyrgyzstanFile.includes("not a count of all organisms") || !floraKyrgyzstanFile.includes("гербарные находки") || !floraKyrgyzstanFile.includes("herbarium records")) errors.push("chapters/flora-kyrgyzstan.html: the vascular-plant count must retain its scope and revision caveats");

if (!floraKyrgyzstanFile.includes("10.1016/j.japb.2023.09.002") || !floraKyrgyzstanFile.includes("Utricularia macrorhiza") || !floraKyrgyzstanFile.includes("Stuckenia amblyphylla")) errors.push("chapters/flora-kyrgyzstan.html: aquatic-plant field study must retain its DOI and key taxonomic findings");
if (!floraKyrgyzstanFile.includes("MW0896287") || !floraKyrgyzstanFile.includes("Allium filifolium") || !floraKyrgyzstanFile.includes("taxonomic issue is fully settled")) errors.push("chapters/flora-kyrgyzstan.html: Besh-Tash Allium record must retain its voucher and taxonomic caveat");
if (!floraKyrgyzstanFile.includes("10.5281/zenodo.15253859") || !floraKyrgyzstanFile.includes("31 региональная запись") || !floraKyrgyzstanFile.includes("31 regional records") || !floraKyrgyzstanFile.includes("не тождественны административным областям") || !floraKyrgyzstanFile.includes("not equivalent to administrative oblasts")) errors.push("chapters/flora-kyrgyzstan.html: the 2025 regional-plant source must retain its DOI, record count and floristic-region/oblast distinction");
if (!floraKyrgyzstanFile.includes("северо-восточного Кыргызстана") || !floraKyrgyzstanFile.includes("north-eastern Kyrgyzstan") || !floraKyrgyzstanFile.includes("не является полной инвентаризацией") || !floraKyrgyzstanFile.includes("not a complete inventory")) errors.push("chapters/flora-kyrgyzstan.html: aquatic-plant findings must retain geographic and inventory-scope caveats");

const ecologyFile = fs.readFileSync(path.join(root, "chapters", "ecology.html"), "utf8");
const chainButtons = [...ecologyFile.matchAll(/<button\b[^>]*data-chain="[^"]+"[^>]*>/gi)];
if (chainButtons.length !== 5) errors.push("chapters/ecology.html: expected five food-chain controls");
if ((ecologyFile.match(/data-chain="[^"]+" aria-pressed="false"><span class="ru">/g) || []).length !== 5) {
  errors.push("chapters/ecology.html: food-chain controls must have bilingual labels and initial pressed state");
}
if (!ecologyFile.includes("else if(i===selected.length)") || !ecologyFile.includes("const next=chainOrder[selected.length]")) {
  errors.push("chapters/ecology.html: food-chain builder must enforce sequential trophic choices");
}
if (!ecologyFile.includes('role="status" aria-live="polite"')) errors.push("chapters/ecology.html: food-chain feedback must be announced accessibly");
if (!/data-nitrogen="ammonification"/.test(ecologyFile) || !ecologyFile.includes("Аммонификация") || !ecologyFile.includes("Ammonification")) errors.push("chapters/ecology.html: nitrogen cycle must include bilingual ammonification control");
if (!ecologyFile.includes("NH₄⁺") || !ecologyFile.includes("N₂O и N₂") || !ecologyFile.includes("N₂O and N₂")) errors.push("chapters/ecology.html: nitrogen-cycle explanations must identify ammonium and gaseous denitrification products");
if ((ecologyFile.match(/data-nitrogen="[^"]+" aria-pressed="(?:true|false)"/g) || []).length !== 5) errors.push("chapters/ecology.html: all five nitrogen-cycle controls must expose initial pressed states");
const ecologyControlCounts = {
  "carbon-controls": { attribute: "carbon", count: 5 },
  "pressure-controls": { attribute: "pressure", count: 4 }
};
for (const [group, config] of Object.entries(ecologyControlCounts)) {
  const section = ecologyFile.match(new RegExp('<div class="controls" id="' + group + '">([\\s\\S]*?)<\\/div>'));
  if (!section) {
    errors.push("chapters/ecology.html: missing " + group);
    continue;
  }
  const buttons = [...section[1].matchAll(/<button\b([^>]*)>([\s\S]*?)<\/button>/gi)].filter(m => m[1].includes('data-' + config.attribute + '="'));
  if (buttons.length !== config.count) {
    errors.push("chapters/ecology.html: expected " + config.count + " controls in " + group + ", found " + buttons.length);
  }
  if (buttons.some(m => !/<span class=["']ru["']>/.test(m[2]) || !/<span class=["']en["']>/.test(m[2]))) {
    errors.push("chapters/ecology.html: every " + group + " control must have paired Russian and English labels");
  }
  const pressed = [...section[1].matchAll(/aria-pressed="(?:true|false)"/g)];
  if (pressed.length !== config.count || (section[1].match(/aria-pressed="true"/g) || []).length !== 1) {
    errors.push("chapters/ecology.html: " + group + " must expose one initial pressed selection and pressed state on every control");
  }
}


const biochemistryFile = fs.readFileSync(path.join(root, "chapters", "biochemistry.html"), "utf8");
const biochemistryControlCounts = {
  "enzyme-controls": 3,
  "factor-controls": 3,
  "atp-controls": 2,
  "respiration-controls": 3
};
for (const [group, expectedCount] of Object.entries(biochemistryControlCounts)) {
  const section = biochemistryFile.match(new RegExp('<div class="controls" id="' + group + '">([\\s\\S]*?)<\\/div>'));
  if (!section) {
    errors.push("chapters/biochemistry.html: missing " + group);
    continue;
  }
  const labels = [...section[1].matchAll(/<button\b[^>]*>([\s\S]*?)<\/button>/gi)];
  if (labels.length !== expectedCount) {
    errors.push("chapters/biochemistry.html: expected " + expectedCount + " controls in " + group + ", found " + labels.length);
  }
  if (labels.some(m => !/<span class=["']ru["']>/.test(m[1]) || !/<span class=["']en["']>/.test(m[1]))) {
    errors.push("chapters/biochemistry.html: every " + group + " control must have paired Russian and English labels");
  }
}
if (!biochemistryFile.includes("does not shift the equilibrium position") || !biochemistryFile.includes("не меняет его положение")) {
  errors.push("chapters/biochemistry.html: enzyme explanation must state that enzymes do not shift equilibrium");
}
if (!biochemistryFile.includes("actual ΔG in a cell depends") || !biochemistryFile.includes("Фактическое значение ΔG в клетке зависит")) {
  errors.push("chapters/biochemistry.html: ATP hydrolysis explanation must qualify cellular ΔG");
}

for (const url of ["7-1-energy-in-living-systems", "7-3-oxidation-of-pyruvate-and-the-citric-acid-cycle", "7-4-oxidative-phosphorylation"]) {
  if (!biochemistryFile.includes("openstax.org/books/biology-2e/pages/" + url)) errors.push("chapters/biochemistry.html: missing topic-matched OpenStax reference " + url);
}
for (const phrase of ["протонный градиент", "proton gradient", "хемиосмос", "chemiosmosis"]) {
  if (!biochemistryFile.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/biochemistry.html: oxidative-phosphorylation explanation must cover " + phrase);
}

const botanyFile = fs.readFileSync(path.join(root, "chapters", "botany.html"), "utf8");
if (!botanyFile.includes("function updateOrgan()") || !botanyFile.includes("updateOrgan();updatePhoto();updateConditionLabels()")) {
  errors.push("chapters/botany.html: language switching must refresh organ and photosynthesis model outputs");
}
if (!botanyFile.includes('b.setAttribute("aria-pressed",String(b.dataset.organ===selectedOrgan))')) {
  errors.push("chapters/botany.html: organ selector must expose its selected state");
}
if (!botanyFile.includes("32-2-pollination-and-fertilization") || !botanyFile.includes("развитие семени из семязачатка") || !botanyFile.includes("seed development from the ovule")) {
  errors.push("chapters/botany.html: seed and fruit development require a topic-matched bilingual reference");
}
if (!botanyFile.includes("устьица часто закрываются") || !botanyFile.includes("stomata often close")) {
  errors.push("chapters/botany.html: water-stress explanation must connect stomatal closure with reduced CO₂ uptake");
}
const cellBiologyFile = fs.readFileSync(path.join(root, "chapters", "cell-biology.html"), "utf8");
const cellSignalingStart = cellBiologyFile.indexOf('id="cell-signaling-pathways"');
const cellMembraneStart = cellBiologyFile.indexOf('<section class="detail"><h2 id="detail-title">Клеточная мембрана</h2>');
const cellSignalingBlock = cellBiologyFile.slice(cellSignalingStart, cellMembraneStart);
if (cellSignalingStart < 0 || cellMembraneStart <= cellSignalingStart) errors.push("chapters/cell-biology.html: cell-signalling lesson must precede the membrane detail");
for (const phrase of ["contact-dependent", "paracrine", "endocrine", "synaptic", "receptor", "second messengers", "feedback", "cross-talk"]) {
  if (!cellSignalingBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/cell-biology.html: cell-signalling lesson missing pathway concept: " + phrase);
}
if (!/<span class="ru">/.test(cellSignalingBlock) || !/<span class="en">/.test(cellSignalingBlock)) errors.push("chapters/cell-biology.html: cell-signalling lesson must be bilingual");
if (!cellSignalingBlock.includes('role="img"') || !cellSignalingBlock.includes('aria-labelledby="cell-signal-svg-title cell-signal-svg-desc"') || !cellSignalingBlock.includes("<title") || !cellSignalingBlock.includes("<desc")) errors.push("chapters/cell-biology.html: signalling diagram must have accessible SVG title and description");

const cellCycleControlStart = cellBiologyFile.indexOf('id="cell-cycle-checkpoints-apoptosis"');

const cellCycleControlBlock = cellBiologyFile.slice(cellCycleControlStart, cellSignalingStart);
if (cellCycleControlStart < 0 || cellSignalingStart <= cellCycleControlStart) errors.push("chapters/cell-biology.html: cell-cycle control lesson must precede cell signalling");
for (const phrase of ["G1/S", "G2/M", "spindle-assembly checkpoint", "cyclin", "cyclin-dependent kinase", "apoptosis", "necrosis", "DNA repair"]) {
  if (!cellCycleControlBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/cell-biology.html: cell-cycle control lesson missing mechanism or distinction: " + phrase);
}
if (!/<span class="ru">/.test(cellCycleControlBlock) || !/<span class="en">/.test(cellCycleControlBlock)) errors.push("chapters/cell-biology.html: cell-cycle control lesson must be bilingual");


const anatomyFile = fs.readFileSync(path.join(root, "chapters", "anatomy.html"), "utf8");
const homeostasisControlStart = anatomyFile.indexOf('id="homeostatic-control-loops"');
const anatomyLearningStart = anatomyFile.indexOf('<section class="learning-block"><div class="learning-grid">');
const homeostasisControlBlock = anatomyFile.slice(homeostasisControlStart, anatomyLearningStart);
if (homeostasisControlStart < 0 || anatomyLearningStart <= homeostasisControlStart) errors.push("chapters/anatomy.html: expanded homeostasis lesson must precede the learning objectives");
for (const phrase of ["negative feedback", "positive feedback", "insulin", "glucagon", "vasopressin", "oxytocin", "osmoreceptors", "thermoregulation"]) {
  if (!homeostasisControlBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/anatomy.html: homeostasis lesson missing mechanism or example: " + phrase);
}
if (!/<span class="ru">/.test(homeostasisControlBlock) || !/<span class="en">/.test(homeostasisControlBlock)) errors.push("chapters/anatomy.html: homeostasis lesson must be bilingual");
if (!homeostasisControlBlock.includes('role="img"') || !homeostasisControlBlock.includes('aria-labelledby="homeostasis-svg-title homeostasis-svg-desc"') || !homeostasisControlBlock.includes("<title") || !homeostasisControlBlock.includes("<desc")) errors.push("chapters/anatomy.html: homeostasis diagram must have accessible SVG title and description");

const renalStart = anatomyFile.indexOf('id="renal-physiology"');
const objectivesStart = anatomyFile.indexOf('<section class="learning-block"><div class="learning-grid">');
const renalBlock = anatomyFile.slice(renalStart, objectivesStart);
if (renalStart < 0 || objectivesStart <= renalStart) errors.push("chapters/anatomy.html: renal physiology lesson must precede the learning objectives");
for (const phrase of ["glomerulus", "Bowman's capsule", "filtration", "reabsorption", "secretion", "aldosterone", "vasopressin", "renin", "angiotensin", "extracellular-fluid volume", "selective and regulated"]) {
  if (!renalBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/anatomy.html: renal physiology lesson missing mechanism or scientific qualification: " + phrase);
}
if (!/<span class="ru">/.test(renalBlock) || !/<span class="en">/.test(renalBlock)) errors.push("chapters/anatomy.html: renal physiology lesson must be bilingual");
if (!renalBlock.includes('role="img"') || !renalBlock.includes('aria-labelledby="nephron-svg-title nephron-svg-desc"') || !renalBlock.includes('id="nephron-svg-title"') || !renalBlock.includes('id="nephron-svg-desc"')) errors.push("chapters/anatomy.html: nephron diagram must have accessible SVG title and description");
if (!anatomyFile.includes("Healthy kidneys do not maintain a fixed filtration rate or urine volume under all conditions.") || !renalBlock.includes("не означает, что скорость фильтрации и объём мочи постоянны")) errors.push("chapters/anatomy.html: renal lesson must explain physiological variation in filtration and urine output");

const cardiovascularStart = anatomyFile.indexOf('id="cardiovascular-physiology"');
const cardiovascularObjectivesStart = anatomyFile.indexOf('<section class="learning-block"><div class="learning-grid">', cardiovascularStart);
const cardiovascularBlock = anatomyFile.slice(cardiovascularStart, cardiovascularObjectivesStart);
if (cardiovascularStart < 0 || cardiovascularObjectivesStart <= cardiovascularStart) errors.push("chapters/anatomy.html: cardiovascular physiology lesson must precede the learning objectives");
if (renalStart < 0 || renalStart >= cardiovascularObjectivesStart) errors.push("chapters/anatomy.html: renal physiology lesson must also precede the learning objectives");
for (const phrase of ["diastole", "ventricular systole", "stroke volume", "cardiac output", "heart rate", "sinoatrial", "atrioventricular", "Purkinje", "baroreceptors", "carotid sinus", "aortic arch", "total peripheral resistance", "angiotensin II", "aldosterone", "vasopressin", "short-term regulatory mechanism"]) {
  if (!cardiovascularBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/anatomy.html: cardiovascular lesson missing mechanism or scientific distinction: " + phrase);
}
if (!/<span class="ru">/.test(cardiovascularBlock) || !/<span class="en">/.test(cardiovascularBlock)) errors.push("chapters/anatomy.html: cardiovascular lesson must be bilingual");
if (!cardiovascularBlock.includes('role="img"') || !cardiovascularBlock.includes('aria-labelledby="conduction-svg-title conduction-svg-desc"') || !cardiovascularBlock.includes('id="conduction-svg-title"') || !cardiovascularBlock.includes('id="conduction-svg-desc"')) errors.push("chapters/anatomy.html: cardiac conduction diagram must have accessible SVG title and description");
if (!cardiovascularBlock.includes("Cardiac output = heart rate × stroke volume") || !cardiovascularBlock.includes("не являются одним и тем же показателем")) errors.push("chapters/anatomy.html: cardiovascular lesson must distinguish cardiac output, heart rate and blood pressure");

const geneticsFile = fs.readFileSync(path.join(root, "chapters", "genetics.html"), "utf8");
if (!geneticsFile.includes("let selectedMutation=null") || !geneticsFile.includes("updateDynamic();updateMutation()")) {
  errors.push("chapters/genetics.html: mutation model must preserve and translate selection on language switch");
}
const mendelianStart = geneticsFile.indexOf('id="mendelian-inheritance"');
const geneRegulationStart = geneticsFile.indexOf('id="gene-expression-regulation"');
const mendelianBlock = geneticsFile.slice(mendelianStart, geneRegulationStart);
if (mendelianStart < 0 || geneRegulationStart <= mendelianStart) errors.push("chapters/genetics.html: Mendelian inheritance lesson must precede gene regulation");
for (const phrase of ["Punnett square", "Aa × Aa", "1 AA : 2 Aa : 1 aa", "complete dominance", "incomplete dominance", "codominance", "many human traits are polygenic"]) {
  if (!mendelianBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/genetics.html: inheritance lesson missing model or qualification: " + phrase);
}
if (!/<span class="ru">/.test(mendelianBlock) || !/<span class="en">/.test(mendelianBlock)) errors.push("chapters/genetics.html: inheritance lesson must be bilingual");
if (!mendelianBlock.includes('<table class="inheritance-table">') || !mendelianBlock.includes('scope="row"') || !mendelianBlock.includes('<caption>')) errors.push("chapters/genetics.html: Punnett square must use an accessible semantic table");
if (!geneticsFile.includes(".inheritance-table{width:100%") || !geneticsFile.includes("@media(max-width:420px){.inheritance-table")) errors.push("chapters/genetics.html: Punnett square must remain readable on narrow screens");

const geneticCodeStart = geneticsFile.indexOf('<section class="detail"><h2 id="detail-title">');
const geneRegulationBlock = geneticsFile.slice(geneRegulationStart, geneticCodeStart);
if (geneRegulationStart < 0 || geneticCodeStart <= geneRegulationStart) errors.push("chapters/genetics.html: gene-regulation lesson must appear before the genetic-code detail");
for (const phrase of ["Регуляция экспрессии генов", "Regulation of gene expression", "транскрипционные факторы", "transcription factors", "Эпигенетические изменения", "Epigenetic changes", "not automatic"]) {
  if (!geneRegulationBlock.includes(phrase)) errors.push("chapters/genetics.html: gene-regulation lesson missing bilingual concept or qualification: " + phrase);
}

const evolutionFile = fs.readFileSync(path.join(root, "chapters", "evolution.html"), "utf8");
for (const url of ["19-2-population-genetics", "19-3-adaptive-evolution"]) {
  if (!evolutionFile.includes("openstax.org/books/biology-2e/pages/" + url)) errors.push("chapters/evolution.html: missing topic-matched OpenStax reference " + url);
}
if (!evolutionFile.includes("Illustrative frequencies after several generations") || !evolutionFile.includes("not a prediction for a real population")) errors.push("chapters/evolution.html: selection model must be labelled illustrative, not predictive");
if (!evolutionFile.includes("function localizeControls()") || !evolutionFile.includes("localizeControls();updateModules()")) errors.push("chapters/evolution.html: interactive controls must relabel when the language changes");
if (!/data-selection="high" aria-pressed="false"/.test(evolutionFile) || !/data-era="human" aria-pressed="false"/.test(evolutionFile)) errors.push("chapters/evolution.html: toggle controls must expose initial pressed states");

const ecologyProductivityStart = ecologyFile.indexOf('id="ecosystem-productivity"');
const ecologyPopulationStart = ecologyFile.indexOf('id="population-dynamics"');
const ecologyProductivity = ecologyFile.slice(ecologyProductivityStart, ecologyPopulationStart);
if (ecologyProductivityStart < 0 || ecologyPopulationStart <= ecologyProductivityStart) errors.push("chapters/ecology.html: ecosystem-productivity lesson must precede population dynamics");
for (const phrase of ["npp = gpp − r", "transfer efficiency", "10% rule", "rough teaching approximation", "biomass pyramid can be inverted", "aria-labelledby=\"trophic-pyramid-title trophic-pyramid-desc\""]) {
  if (!ecologyProductivity.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/ecology.html: productivity lesson missing scientific concept or qualification: " + phrase);
}
if (!/<span class="ru">/.test(ecologyProductivity) || !/<span class="en">/.test(ecologyProductivity)) errors.push("chapters/ecology.html: productivity lesson must be bilingual");


const speciationStart = evolutionFile.indexOf('id="speciation-processes"');
const selectionStart = evolutionFile.indexOf('<section class="lab">', speciationStart);
const speciationBlock = evolutionFile.slice(speciationStart, selectionStart);
if (speciationStart < 0 || selectionStart <= speciationStart) errors.push("chapters/evolution.html: speciation lesson must precede the natural-selection interactive");
for (const phrase of ["allopatric speciation", "sympatric speciation", "prezygotic", "postzygotic", "polyploidy", "not a ladder"]) {
  if (!speciationBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/evolution.html: speciation lesson missing mechanism or qualification: " + phrase);
}
if (!/<span class="ru">/.test(speciationBlock) || !/<span class="en">/.test(speciationBlock)) errors.push("chapters/evolution.html: speciation lesson must be bilingual");

const microbiologyFile = fs.readFileSync(path.join(root, "chapters", "microbiology.html"), "utf8");
const hgtStart = microbiologyFile.indexOf('id="horizontal-gene-transfer"');
const microbiologyDetailStart = microbiologyFile.indexOf('<section class="detail">', hgtStart);
const hgtBlock = microbiologyFile.slice(hgtStart, microbiologyDetailStart);
if (hgtStart < 0 || microbiologyDetailStart <= hgtStart) errors.push("chapters/microbiology.html: horizontal gene transfer lesson must precede the detail section");
for (const phrase of ["horizontal gene transfer", "transformation", "transduction", "conjugation", "does not occur automatically"]) {
  if (!hgtBlock.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/microbiology.html: HGT lesson missing mechanism or qualification: " + phrase);
}
if (!/<span class="ru">/.test(hgtBlock) || !/<span class="en">/.test(hgtBlock)) errors.push("chapters/microbiology.html: HGT lesson must be bilingual");
if (!microbiologyFile.includes("function localizeControls()") || !microbiologyFile.includes("localizeControls();updateModules()")) errors.push("chapters/microbiology.html: group, shape and growth-phase controls must relabel when the language changes");
if (!/data-group="viruses" aria-pressed="false"/.test(microbiologyFile) || !/data-phase="death" aria-pressed="false"/.test(microbiologyFile)) errors.push("chapters/microbiology.html: toggle controls must expose initial pressed states");
for (const url of ["6-1-viruses", "6-2-the-viral-life-cycle", "14-5-drug-resistance"]) {
  if (!microbiologyFile.includes("openstax.org/books/microbiology/pages/" + url)) errors.push("chapters/microbiology.html: missing topic-matched OpenStax reference " + url);
}
for (const phrase of ["Как вирус создаёт новые частицы", "How a virus makes new particles", "литический цикл", "лизогенный цикл", "lytic cycle", "lysogenic cycle", "Почему микробы становятся устойчивыми", "Why microbes become resistant", "естественный отбор", "natural selection", "не лечат вирусные инфекции", "not viral infections"]) {
  if (!microbiologyFile.toLowerCase().includes(phrase.toLowerCase())) errors.push("chapters/microbiology.html: missing bilingual virus/resistance learning content: " + phrase);
}
const systematicsFile = fs.readFileSync(path.join(root, "chapters", "systematics.html"), "utf8");
if (!systematicsFile.includes("function localizeControls()") || !systematicsFile.includes("localizeControls();updateAll()")) errors.push("chapters/systematics.html: rank, domain and identification controls must relabel when the language changes");
if (!systematicsFile.includes("когда одного признака недостаточно") || !systematicsFile.includes("when one trait is not enough")) errors.push("chapters/systematics.html: identification-key wording must explain the limit of a single trait");
if (!systematicsFile.includes('const allowed=base==="backbone"?["feathers","fur","scales"]:["shell"]') || !systematicsFile.includes('if(id==="key-controls")document.querySelectorAll("#trait-controls [data-trait]").forEach(x=>x.setAttribute("aria-pressed","false"))')) errors.push("chapters/systematics.html: identification key must clear incompatible traits when its first branch changes");
const faunaKyrgyzstanFile = fs.readFileSync(path.join(root, "chapters", "fauna-kyrgyzstan.html"), "utf8");
if (!faunaKyrgyzstanFile.includes("нельзя автоматически переносить на каждую соседнюю долину") || !faunaKyrgyzstanFile.includes("national occurrence should not automatically be extended")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Menzbier marmot range must distinguish national occurrence from uncertain local records");
}
if (!faunaKyrgyzstanFile.includes("mammaldiversity.org/taxon/1001733") || !faunaKyrgyzstanFile.includes("moip-bio.msu.ru")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Menzbier marmot taxonomic and regional evidence sources are required");
}
if (!faunaKyrgyzstanFile.includes("publicera.kb.se/slr/article/view/63883") || !faunaKyrgyzstanFile.includes("en.kabar.kg/news/snow-leopard-argali-and-mountain-goats-caught-on-video-at-issyk-kul/")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 snow leopard national assessment and dated Issyk-Kul field record sources are required");
}
if (!faunaKyrgyzstanFile.includes("450–550 особей") || !faunaKyrgyzstanFile.includes("450–550 animals") || !faunaKyrgyzstanFile.includes("29 октября 2026 года") || !faunaKyrgyzstanFile.includes("29 October 2026") || !faunaKyrgyzstanFile.includes("не разрешено") || !faunaKyrgyzstanFile.includes("remains unresolved") || !faunaKyrgyzstanFile.includes("v-dzeti-oguzskom-raione-na-video-zapecatleli-snezhnogo-barsa")) errors.push("chapters/fauna-kyrgyzstan.html: PASK adult estimate and Ministry 2026 range must remain separately dated and explicitly unreconciled");
if (!faunaKyrgyzstanFile.includes("20821615") || !faunaKyrgyzstanFile.includes("98 ячеек") || !faunaKyrgyzstanFile.includes("98 sampling cells") || !faunaKyrgyzstanFile.includes("93% ячеек") || !faunaKyrgyzstanFile.includes("93% of cells") || !faunaKyrgyzstanFile.includes("Из девяти предположительно барсовых экскрементов ДНК-анализ подтвердил пять") || !faunaKyrgyzstanFile.includes("five of nine") || !faunaKyrgyzstanFile.includes("112 снимков") || !faunaKyrgyzstanFile.includes("112 images") || !faunaKyrgyzstanFile.includes("не менее пяти индивидуальных барсов") || !faunaKyrgyzstanFile.includes("at least five individual snow leopards") || !faunaKyrgyzstanFile.includes("не должны суммироваться") || !faunaKyrgyzstanFile.includes("must not be added") || !faunaKyrgyzstanFile.includes("не всей популяции Кыргызстана") || !faunaKyrgyzstanFile.includes("not the national population") || !faunaKyrgyzstanFile.includes("двух ячейках") || !faunaKyrgyzstanFile.includes("two cells") || !faunaKyrgyzstanFile.includes("Otolobus manul") || !faunaKyrgyzstanFile.includes("Otocolobus manul")) errors.push("chapters/fauna-kyrgyzstan.html: Terskey Ala-Too expedition records must retain sampling effort, method-specific counts, local scope and the Pallas's cat spelling caveat");

if (!faunaKyrgyzstanFile.includes("10.3390/d18030194") || !faunaKyrgyzstanFile.includes("10.5061/dryad.76hdr7t7t") || !faunaKyrgyzstanFile.includes("расхождение следует считать нерешённым")) {
  errors.push("chapters/fauna-kyrgyzstan.html: argali genomic study must cite the correct article and dataset and preserve the unresolved provenance discrepancy");
}
if (!faunaKyrgyzstanFile.includes("конкретном эпизоде наблюдения") || !faunaKyrgyzstanFile.includes("specific observation event")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Issyk-Kul field observation must not be presented as an abundance estimate");
}
if (!faunaKyrgyzstanFile.includes("narynskii-gosudarstvennyi-prirodnyi-zapovednik") || !faunaKyrgyzstanFile.includes("v-narynskoi-oblasti-na-video-snyaty-stado-gornyx-kozlov-i-sneznyi-bars")) {
  errors.push("chapters/fauna-kyrgyzstan.html: dated Naryn camera-trap and patrol records are required");
}
if (!faunaKyrgyzstanFile.includes("не приводит число индивидуально распознанных животных") || !faunaKyrgyzstanFile.includes("does not provide the number of individually identified animals")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Naryn camera-trap notice must retain sampling and density caveat");
}
if (!faunaKyrgyzstanFile.includes("нельзя автоматически относить к территории Нарынского заповедника") || !faunaKyrgyzstanFile.includes("should not automatically be assigned to Naryn Nature Reserve")) {
  errors.push("chapters/fauna-kyrgyzstan.html: unnamed Naryn valley record must not be assigned to the reserve");
}
if (faunaKyrgyzstanFile.includes("Караatal-Жапырыкского")) {
  errors.push("chapters/fauna-kyrgyzstan.html: mixed-script spelling of Karatal-Japyryk reserve name remains");
}
if (!faunaKyrgyzstanFile.includes("Подвидовое деление архаров остаётся дискуссионным") || !faunaKyrgyzstanFile.includes("Subspecies taxonomy within argali remains debated")) {
  errors.push("chapters/fauna-kyrgyzstan.html: argali must retain the subspecies-taxonomy caveat");
}
if (!faunaKyrgyzstanFile.includes("450–500") || !faunaKyrgyzstanFile.includes("около 900") || !faunaKyrgyzstanFile.includes("не численность архара в Кыргызстане") || !faunaKyrgyzstanFile.includes("not the national argali total")) {
  errors.push("chapters/fauna-kyrgyzstan.html: December 2025 argali records must retain site and non-national-estimate caveats");
}
if (!faunaKyrgyzstanFile.includes("7–12 октября 2024 года") || !faunaKyrgyzstanFile.includes("160 животных") || !faunaKyrgyzstanFile.includes("не публикует итоговое число") || !faunaKyrgyzstanFile.includes("did not publish a final total")) {
  errors.push("chapters/fauna-kyrgyzstan.html: maral 400–600 estimate must be attributed to 2024, not the 2025 census");
}
if (!faunaKyrgyzstanFile.includes("35 животных были завезены из Алтая в 2022 году") || !faunaKyrgyzstanFile.includes("отличать от естественных популяций")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Besh-Tash introduced maral group must be distinguished from natural populations");
}
if (!faunaKyrgyzstanFile.includes("135 242 SNP-маркера") || !faunaKyrgyzstanFile.includes("88 образцов архара") || !faunaKyrgyzstanFile.includes("O. a. polii") || !faunaKyrgyzstanFile.includes("Pamir Plateau")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 argali genetics evidence must retain initial and analysed sample sizes, named subspecies and Pamir scope caveat");
}
if (!faunaKyrgyzstanFile.includes("135 242 SNP-маркера") || !faunaKyrgyzstanFile.includes("72 individuals") || !faunaKyrgyzstanFile.includes("not extended to the full Marco Polo argali range")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 argali genetics evidence must retain sample size and scope caveat");
}
if (!faunaKyrgyzstanFile.includes("689 маралов") || !faunaKyrgyzstanFile.includes("нельзя складывать, усреднять или выдавать за одну согласованную оценку") || !faunaKyrgyzstanFile.includes("these figures must not be added, averaged or presented as one reconciled estimate")) {
  errors.push("chapters/fauna-kyrgyzstan.html: distinct 2024 CAMCA maral estimate must be disclosed with comparability caveat");
}
if (!faunaKyrgyzstanFile.includes("689 маралов для Кыргызстана за 2024 год") || !faunaKyrgyzstanFile.includes("47 голов за 2024 год") || !faunaKyrgyzstanFile.includes("must not be added, averaged")) {
  errors.push("chapters/fauna-kyrgyzstan.html: conflicting 2024 maral counts must remain explicitly unreconciled");
}
if (!faunaKyrgyzstanFile.includes("stat.gov.kg/kg/opendata/category/138/") || !faunaKyrgyzstanFile.includes("47 маралов за 2024 год") || !faunaKyrgyzstanFile.includes("61 за 2023 год") || !faunaKyrgyzstanFile.includes("should not be directly combined")) {
  errors.push("chapters/fauna-kyrgyzstan.html: official maral statistical series must remain distinct from CAMCA Naryn estimate");
}
if (!faunaKyrgyzstanFile.includes("четыре полевых сезона 2016–2019 годов") || !faunaKyrgyzstanFile.includes("пяти взрослых барсов") || !faunaKyrgyzstanFile.includes("five cubs or subadults") || !faunaKyrgyzstanFile.includes("cannot be directly compared with CAMCA")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Naryn snow leopard local camera-trap study must remain distinct from wider regional estimate");
}
if (!faunaKyrgyzstanFile.includes("Ursus arctos isabellinus") || !faunaKyrgyzstanFile.includes("Mammal Diversity Database") || !faunaKyrgyzstanFile.includes("not treat Central Asian brown bear forms uniformly")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Tian Shan brown bear subspecies designation must remain qualified");
}
if (/<a\b[^>]*>\s*<a\b/i.test(faunaKyrgyzstanFile)) errors.push("chapters/fauna-kyrgyzstan.html: nested anchors must be repaired so catalogue citations remain accessible");
if (!faunaKyrgyzstanFile.includes("Coregonus lavaretus") || !faunaKyrgyzstanFile.includes("Coregonus peled") || !faunaKyrgyzstanFile.includes("Triplophysa stoliczkae")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Son-Kul fish account must retain the 2021–2023 field-study taxa");
}
if (!faunaKyrgyzstanFile.includes("Из них 14 отнесены") ||
    !faunaKyrgyzstanFile.includes("14 were classified as wildlife-related violations") ||
    !faunaKyrgyzstanFile.includes("112 363,5 га") ||
    !faunaKyrgyzstanFile.includes("112,363.5 ha")) {
  errors.push("chapters/fauna-kyrgyzstan.html: paired Russian/English wildlife statistics and reserve-area values must match");
}
if (!faunaKyrgyzstanFile.includes("Список OSME v10.1") ||
    !faunaKyrgyzstanFile.includes("OSME Region List v10.1") ||
    !faunaKyrgyzstanFile.includes("ITIS признаёт") ||
    !faunaKyrgyzstanFile.includes("ITIS treats both")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Himalayan Snowcock occurrence caveat must be equivalent in Russian and English");
}
if (!faunaKyrgyzstanFile.includes("This disagreement reflects different taxonomic concepts") ||
    !faunaKyrgyzstanFile.includes("fishcatget.asp?spid=53209") ||
    !faunaKyrgyzstanFile.includes("T. stoliczkae") ||
    !faunaKyrgyzstanFile.includes("T. stolickai") ||
    !faunaKyrgyzstanFile.includes("Gymnodiptychus dybowskii") ||
    !faunaKyrgyzstanFile.includes("Diptychus dybowskii micromakulatus") ||
    !faunaKyrgyzstanFile.includes("fishcatget.asp?spid=55960") ||
    !faunaKyrgyzstanFile.includes("search_value=689192") ||
    !faunaKyrgyzstanFile.includes("Diptychus gymnogaster micromakulatus") ||
    !faunaKyrgyzstanFile.includes("fao.org/docrep/018/i3268e/i3268e.pdf") ||
    faunaKyrgyzstanFile.includes("опубликованное в 2023 году исследование") ||
    faunaKyrgyzstanFile.includes("published in 2023; its abstract")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Son-Kul Triplophysa determination must retain the IUCN/Catalogue taxonomic-concept conflict");
}
if (!faunaKyrgyzstanFile.includes("2004–2005 годов") || !faunaKyrgyzstanFile.includes("описан как озеро без рыб") || !faunaKyrgyzstanFile.includes("described as fishless")) {
  errors.push("chapters/fauna-kyrgyzstan.html: fishless Chatyr-Kul and fish-bearing Son-Kul distinction must remain explicit");
}
if (!faunaKyrgyzstanFile.includes("их нельзя превращать в актуальную оценку численности всех рыб озера") || !faunaKyrgyzstanFile.includes("must not be converted into a current abundance estimate")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Son-Kul fish-stock findings must retain their historical monitoring scope");
}
if (!faunaKyrgyzstanFile.includes("105 519 га") || !faunaKyrgyzstanFile.includes("4 вида пресмыкающихся") || !faunaKyrgyzstanFile.includes("1 вид земноводных") || !faunaKyrgyzstanFile.includes("not as a complete inventory newly verified in 2026")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Naryn reserve taxonomic inventory must retain its source date and completeness caveat");
}
if (!faunaKyrgyzstanFile.includes("14 июля 2026 года") || !faunaKyrgyzstanFile.includes("21 сентября 2026 года") || !faunaKyrgyzstanFile.includes("not evidence of an increase in bird numbers")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 Karatal-Japyryk bird expedition and Son-Kul observation structure must be accurately qualified");
}
if (!faunaKyrgyzstanFile.includes("Cervus canadensis songaricus") || !faunaKyrgyzstanFile.includes("Cervus elaphus songaricus") || !faunaKyrgyzstanFile.includes("C. c. sibiricus") || !faunaKyrgyzstanFile.includes("NCBI Taxonomy")) {
  errors.push("chapters/fauna-kyrgyzstan.html: maral nomenclature must document the NCBI synonym and the competing IUCN/CAMCA subspecies treatment");
}


if (!faunaKyrgyzstanFile.includes("04B · TERRESTRIAL INVERTEBRATES") || !faunaKyrgyzstanFile.includes("Hidden diversity: insects and other arthropods")) {
  errors.push("chapters/fauna-kyrgyzstan.html: terrestrial invertebrates require a bilingual dedicated section");
}
if (!faunaKyrgyzstanFile.includes("14 600 видов насекомых") || !faunaKyrgyzstanFile.includes("30 000 видов членистоногих") || !faunaKyrgyzstanFile.includes("must not be added, directly compared")) {
  errors.push("chapters/fauna-kyrgyzstan.html: insect and arthropod estimates must retain their different scopes and non-comparability caveat");
}
if (!faunaKyrgyzstanFile.includes("около 150 видов насекомых") || !faunaKyrgyzstanFile.includes("более 30 других видов беспозвоночных") || !faunaKyrgyzstanFile.includes("два вида, подтверждённо исчезнувшие") || !faunaKyrgyzstanFile.includes("not equivalent to the number of taxa")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2025 national threat estimates must be distinguished from the 18-species official arthropod list");
}
if (!faunaKyrgyzstanFile.includes("Kyrgyzstancampa") || !faunaKyrgyzstanFile.includes("47 видов дневных бабочек") || !faunaKyrgyzstanFile.includes("no local or regional endemics")) {
  errors.push("chapters/fauna-kyrgyzstan.html: cave discoveries and the bounded Naryn badlands butterfly survey require accurate scope");
}
if (!faunaKyrgyzstanFile.includes("2026–2028") || !faunaKyrgyzstanFile.includes("voucher specimen or photograph") || !faunaKyrgyzstanFile.includes("date, and a description of the habitat")) {
  errors.push("chapters/fauna-kyrgyzstan.html: invertebrate conservation accounts must include Red Data Book revision context and field-record metadata");
}
if (!faunaKyrgyzstanFile.includes("ibnaskr.org/laboratoriya-entomologii-i-parazitologii/") || !faunaKyrgyzstanFile.includes("VNR%202025%20Kyrgyz%20Republic%20Report%20EN.pdf") || !faunaKyrgyzstanFile.includes("KG-CARs3-Draft-ESIA-May-16-Final.pdf") || !faunaKyrgyzstanFile.includes("16%282%29_22_Korb.pdf") || !faunaKyrgyzstanFile.includes("red-data-book-kyrgyzstan-project-2026-2028/")) {
  errors.push("chapters/fauna-kyrgyzstan.html: primary institutional, national review, World Bank, peer-reviewed and Red Data Book project sources are required");
}


if (!faunaKyrgyzstanFile.includes("Why there is no single uncontested fish-species total") || !faunaKyrgyzstanFile.includes("Почему нельзя назвать одно бесспорное число видов рыб")) {
  errors.push("chapters/fauna-kyrgyzstan.html: freshwater fish inventory must explain dated, non-final species totals in both languages");
}
if (!faunaKyrgyzstanFile.includes("73 fish species") || !faunaKyrgyzstanFile.includes("49 аборигенных и 24 интродуцированных") || !faunaKyrgyzstanFile.includes("not as a definitive national checklist")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2013 FAO fish inventory must retain native/introduced breakdown and historical scope");
}
if (!faunaKyrgyzstanFile.includes("seven major zoogeographic basins") || !faunaKyrgyzstanFile.includes("Балхашского, Чуйского, Иссык-Кульского") || !faunaKyrgyzstanFile.includes("Talas-Ters")) {
  errors.push("chapters/fauna-kyrgyzstan.html: fish distribution must be explained through the seven zoogeographic basins");
}
if (!faunaKyrgyzstanFile.includes("72 экземпляра трёх видов") || !faunaKyrgyzstanFile.includes("55 Issyk-Kul chebak") || !faunaKyrgyzstanFile.includes("not a complete inventory of the lake fauna")) {
  errors.push("chapters/fauna-kyrgyzstan.html: FAO 2024 Issyk-Kul sample must not be misrepresented as a full species inventory");
}
if (!faunaKyrgyzstanFile.includes("Toru-Aygyr") || !faunaKyrgyzstanFile.includes("Chok-Tal") || !faunaKyrgyzstanFile.includes("Cholpon-Ata")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Issyk-Kul survey locations must be retained accurately");
}
if (!faunaKyrgyzstanFile.includes("American Museum of Natural History") || !faunaKyrgyzstanFile.includes("preliminary fish identification") || !faunaKyrgyzstanFile.includes("laboratory processing and analysis were continuing")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 NAS KR–AMNH fieldwork must be described as ongoing, not as a final checklist");
}
if (!faunaKyrgyzstanFile.includes("FAO Fisheries and Aquaculture Technical Paper No. 584") || !faunaKyrgyzstanFile.includes("fao.org/countryprofiles/news-archive/detail-news/en/c/1730494/") || !faunaKyrgyzstanFile.includes("amnh-fish-research-kyrgyzstan-2026/") || !faunaKyrgyzstanFile.includes("10.1080/14634988.2015.1028309")) {
  errors.push("chapters/fauna-kyrgyzstan.html: FAO, NAS KR–AMNH and peer-reviewed basin review sources are required");
}

const cellBiologyAuditFile = fs.readFileSync(path.join(root, "chapters/cell-biology.html"), "utf8");
if (!cellBiologyAuditFile.includes("Клеточный цикл и митоз: последовательность") || !cellBiologyAuditFile.includes("The cell cycle and mitosis: sequence of events")) errors.push("chapters/cell-biology.html: cell-cycle heading must not label interphase as mitosis");
if ((cellBiologyAuditFile.match(/data-stage="[^"]+"/g) || []).length !== 6 || !cellBiologyAuditFile.includes('data-stage="cytokinesis" aria-pressed="false"')) errors.push("chapters/cell-biology.html: cell-cycle explorer must include a separate cytokinesis control");
if (!cellBiologyAuditFile.includes("клеточная пластинка") || !cellBiologyAuditFile.includes("cell plate") || !cellBiologyAuditFile.includes("cleavage furrow")) errors.push("chapters/cell-biology.html: cytokinesis must distinguish plant cell plate from animal cleavage furrow");
if (!cellBiologyAuditFile.includes("10-3-control-of-the-cell-cycle")) errors.push("chapters/cell-biology.html: cell-cycle checkpoint explanation requires a topic-matched reference");

const zoologyAuditFile = fs.readFileSync(path.join(root, "chapters/zoology.html"), "utf8");
if (!zoologyAuditFile.includes("«Рыбы» — общее название нескольких линий позвоночных") || !zoologyAuditFile.includes("“Fish” is a collective label for several vertebrate lineages")) errors.push("chapters/zoology.html: fish must not be presented as a single monophyletic clade");
if (!zoologyAuditFile.includes("Птицы, в свою очередь, произошли от тероподовых динозавров") || !zoologyAuditFile.includes("are included within reptiles in modern phylogenetic classification")) errors.push("chapters/zoology.html: phylogenetic classification must place birds within reptiles");
if (!zoologyAuditFile.includes("29-4-reptiles") || !zoologyAuditFile.includes("29-1-chordates")) errors.push("chapters/zoology.html: chordate and reptile evolution references are required");

if (!anatomyFile.includes("pages/19-introduction") || !anatomyFile.includes("pages/20-5-circulatory-pathways") || !anatomyFile.includes("pages/22-introduction")) errors.push("chapters/anatomy.html: heart, circulatory pathways and respiratory-system references are required");
if (!anatomyFile.includes("артерии определяются направлением кровотока от сердца") || !anatomyFile.includes("arteries are defined by blood flow away from the heart")) errors.push("chapters/anatomy.html: artery definition must distinguish direction of flow from oxygen content");
if (!anatomyFile.includes("лёгочные артерии проводят бедную кислородом кровь от правого желудочка к лёгким") || !anatomyFile.includes("лёгочные вены возвращают богатую кислородом кровь к левому предсердию")) errors.push("chapters/anatomy.html: pulmonary circuit must correctly identify oxygen-poor arterial and oxygen-rich venous blood");
if (!anatomyFile.includes("pulmonary arteries carry oxygen-poor blood from the right ventricle to the lungs") || !anatomyFile.includes("pulmonary veins return oxygen-rich blood to the left atrium")) errors.push("chapters/anatomy.html: English pulmonary-circuit explanation must match the Russian account");
const geneticsAuditFile = fs.readFileSync(path.join(root, "chapters/genetics.html"), "utf8");
if (!/data-template="TAC" aria-pressed="true"/.test(geneticsAuditFile) || !geneticsAuditFile.includes('x.setAttribute("aria-pressed",String(x.dataset.template===t))')) errors.push("chapters/genetics.html: transcription-template controls must expose and update selected state");
if (!/data-mutation="insertion" aria-pressed="false"/.test(geneticsAuditFile) || !geneticsAuditFile.includes('b.setAttribute("aria-pressed",String(b.dataset.mutation===selectedMutation))')) errors.push("chapters/genetics.html: mutation controls must expose selected state to assistive technology");
if (!geneticsAuditFile.includes("AUG · AGC · UUU · UGG · A…")) errors.push("chapters/genetics.html: insertion example must display the shifted reading frame accurately");
if (!geneticsAuditFile.includes("ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi") || !geneticsAuditFile.includes("ncbi.nlm.nih.gov/books/NBK9849/")) errors.push("chapters/genetics.html: authoritative genetic-code and translation references are required");


// Planned scientific-illustration markers: keep the in-page briefs and the
// central production checklist in sync. This is a static integrity check;
// it does not claim that any planned artwork has been generated.
const imagePlanFile = fs.readFileSync(path.join(root, "IMAGE_GENERATION_PLAN.md"), "utf8");
const imagePages = [
  "index.html",
  "chapters/anatomy.html",
  "chapters/biochemistry.html",
  "chapters/botany.html",
  "chapters/cell-biology.html",
  "chapters/ecology.html",
  "chapters/evolution.html",
  "chapters/genetics.html",
  "chapters/microbiology.html",
  "chapters/systematics.html",
  "chapters/zoology.html",
  "chapters/flora-kyrgyzstan.html",
  "chapters/fauna-kyrgyzstan.html"
];
const imageBriefIds = [];
let imageBriefCount = 0;
for (const rel of imagePages) {
  const html = fs.readFileSync(path.join(root, rel), "utf8");
  const briefs = [...html.matchAll(/<aside class="image-generation-note" id="image-brief-([^"]+)" data-image-status="planned"[\s\S]*?<\/aside>/g)];
  imageBriefCount += briefs.length;
  for (const brief of briefs) {
    const id = brief[1], markup = brief[0];
    imageBriefIds.push(id);
    if (!markup.includes('class="image-note-insert"') || !/images\/generated\/[a-z0-9-]+\.webp/.test(markup) || !/WebP · (?:4:3|16:9)/.test(markup)) {
      errors.push(rel + ": image brief " + id + " must specify a WebP asset path and aspect ratio");
    }
    if (!/data-image-priority="P[123]"/.test(markup)) errors.push(rel + ": image brief " + id + " is missing its visible production priority");
    if (!markup.includes('class="ru"') || !markup.includes('class="en"') || !markup.includes("IMAGE TO GENERATE")) {
      errors.push(rel + ": image brief " + id + " must contain bilingual title/description and a visible planning label");
    }
    if (!/<strong>[\s\S]*?<\/strong>/.test(markup) || !/<p class="ru">[\s\S]*?<\/p>/.test(markup) || !/<p class="en">[\s\S]*?<\/p>/.test(markup)) {
      errors.push(rel + ": image brief " + id + " is missing its title or bilingual brief");
    }
    const title = (markup.match(/<span class="ru">([\s\S]*?)<\/span>/) || [])[1];
    if (title && !imagePlanFile.includes(title)) errors.push(rel + ": image brief " + id + " is absent from IMAGE_GENERATION_PLAN.md");
  }
  if (briefs.length === 0) errors.push(rel + ": expected planned image-generation markers");
}
if (new Set(imageBriefIds).size !== imageBriefIds.length) errors.push("Image-generation brief IDs must be unique across all Biology pages");
if (imageBriefCount !== 52) errors.push("Expected 52 in-page image-generation briefs, found " + imageBriefCount);
const geneticsImageBriefFile = fs.readFileSync(path.join(root, "chapters/genetics.html"), "utf8");
if (!geneticsImageBriefFile.includes('id="image-brief-genetics-dna-packaging"') || !geneticsImageBriefFile.includes("genetics-dna-packaging.webp") || geneticsImageBriefFile.includes("genetics-central-dogma.webp")) {
  errors.push("chapters/genetics.html: DNA-packaging image brief ID and target filename must match its actual subject");
}
const imageInsertionMap = fs.readFileSync(path.join(root, "IMAGE_INSERTION_MAP.md"), "utf8");
const insertionMapIds = [...imageInsertionMap.matchAll(/^\| `image-brief-([^ `]+)`/gm)].map(m => m[1]);
if (insertionMapIds.length !== 52 || new Set(insertionMapIds).size !== 52) errors.push("IMAGE_INSERTION_MAP.md must contain 52 unique insertion anchors; found " + insertionMapIds.length);
const imageDispositionRegister = fs.readFileSync(path.join(root, "IMAGE_DISPOSITION_REGISTER.md"), "utf8");
const imageDispositionRows = [...imageDispositionRegister.matchAll(/^\| `image-brief-([^ `]+)` \| `([^ `]+)` \| P[123] \| [^|]+ \| Deferred \| No asset selected; no third-party image used\./gm)];
const imageDispositionIds = imageDispositionRows.map(m => m[1]);
if (imageDispositionRows.length !== 52 || new Set(imageDispositionIds).size !== 52) {
  errors.push("IMAGE_DISPOSITION_REGISTER.md must contain 52 unique deferred image decisions; found " + imageDispositionRows.length);
}
for (const id of insertionMapIds) if (!imageDispositionIds.includes(id)) errors.push("IMAGE_DISPOSITION_REGISTER.md is missing deferred disposition for " + id);
const dispositionTableRows = imageDispositionRegister.split("\n").filter(line => line.startsWith("| `image-brief-"));
const p1DispositionRows = dispositionTableRows.filter(line => line.includes("| P1 |"));
const p2p3DispositionRows = dispositionTableRows.filter(line => line.includes("| P2 |") || line.includes("| P3 |"));
if (p1DispositionRows.length !== 13 || p1DispositionRows.some(line => !line.includes("IMAGE_SCIENTIFIC_REVIEW.md"))) {
  errors.push("IMAGE_DISPOSITION_REGISTER.md: all 13 P1 assets must link to the detailed scientific review");
}
if (p2p3DispositionRows.length !== 39 || p2p3DispositionRows.some(line => !line.includes("IMAGE_BRIEF_REVIEW.md"))) {
  errors.push("IMAGE_DISPOSITION_REGISTER.md: all 39 P2/P3 assets must link to the individual brief review");
}
const imageBriefReview = fs.readFileSync(path.join(root, "IMAGE_BRIEF_REVIEW.md"), "utf8");
const imageBriefReviewIds = [...imageBriefReview.matchAll(/^\| `(image-brief-[^ `]+)` \| P[23] \|/gm)].map(m => m[1]);
if (imageBriefReviewIds.length !== 39 || new Set(imageBriefReviewIds).size !== 39) {
  errors.push("IMAGE_BRIEF_REVIEW.md must individually review 39 unique P2/P3 briefs; found " + imageBriefReviewIds.length);
}
for (const line of p2p3DispositionRows) {
  const id = (line.match(/^\| `(image-brief-[^ `]+)`/) || [])[1];
  if (id && !imageBriefReviewIds.includes(id)) errors.push("IMAGE_BRIEF_REVIEW.md is missing P2/P3 brief " + id);
}

if (!imageDispositionRegister.includes("G6 disposition:** complete as an explicit, documented deferral") ||
    !imageDispositionRegister.includes("actual image QA is pending") ||
    fs.existsSync(path.join(root, "images/generated"))) {
  errors.push("IMAGE_DISPOSITION_REGISTER.md must document the no-asset deferral and be revised if image assets are added");
}
for (const id of imageBriefIds) if (!insertionMapIds.includes(id)) errors.push("IMAGE_INSERTION_MAP.md is missing insertion anchor " + id);
const imageChecklistCount = (imagePlanFile.match(/^- \[~\] \*\*/gm) || []).length;
const priorityCounts = {
  P1: (imagePlanFile.match(/^- \[~\] \*\*\[P1\]/gm) || []).length,
  P2: (imagePlanFile.match(/^- \[~\] \*\*\[P2\]/gm) || []).length,
  P3: (imagePlanFile.match(/^- \[~\] \*\*\[P3\]/gm) || []).length
};
if (priorityCounts.P1 !== 13 || priorityCounts.P2 !== 26 || priorityCounts.P3 !== 13) {
  errors.push("IMAGE_GENERATION_PLAN.md priority allocation must remain 13 P1, 26 P2 and 13 P3; found " + JSON.stringify(priorityCounts));
}
if (!imagePlanFile.includes("P1 — highest value") || !imagePlanFile.includes("P2 — useful complement") || !imagePlanFile.includes("P3 — lower priority")) {
  errors.push("IMAGE_GENERATION_PLAN.md must define all three image-production priority levels");
}
if (imageChecklistCount !== 52) errors.push("IMAGE_GENERATION_PLAN.md must contain 52 explicitly deferred checklist items, found " + imageChecklistCount);
if (!imagePlanFile.includes("Change `[~]` to `[x]` only after the exact asset exists") || !imagePlanFile.includes("Do not ask the image model to invent species")) {
  errors.push("IMAGE_GENERATION_PLAN.md must retain the scientific-review and no-invented-species production rules");
}

const floraKyrgyzstanAuditFile = fs.readFileSync(path.join(root, "chapters/flora-kyrgyzstan.html"), "utf8");
const faunaKyrgyzstanAuditFile = fs.readFileSync(path.join(root, "chapters/fauna-kyrgyzstan.html"), "utf8");
// Shared editorial standard and visible evidence-status key in both regional chapters.
const kyrgyzBiodiversityStandardFile = fs.readFileSync(path.join(root, "KYRGYZSTAN_BIODIVERSITY_DATA_STANDARD.md"), "utf8");
if (!kyrgyzBiodiversityStandardFile.includes("Confirmed local record") || !kyrgyzBiodiversityStandardFile.includes("National checklist record") || !kyrgyzBiodiversityStandardFile.includes("Historical record")) errors.push("Kyrgyzstan biodiversity data standard must distinguish local, national-checklist and historical evidence");
if (!kyrgyzBiodiversityStandardFile.includes("sampling effort") || !kyrgyzBiodiversityStandardFile.includes("coordinate uncertainty") || !kyrgyzBiodiversityStandardFile.includes("population estimate")) errors.push("Kyrgyzstan biodiversity data standard must define survey effort, spatial uncertainty and abundance evidence");
for (const [label, html] of [["flora", floraKyrgyzstanAuditFile], ["fauna", faunaKyrgyzstanAuditFile]]) {
  if (!html.includes('id="evidence-status-key"')) errors.push(label + " chapter must display the shared evidence-status key");
  if (!html.includes("Confirmed local record") || !html.includes("Historical record") || !html.includes("National checklist record")) errors.push(label + " chapter evidence key must distinguish record scopes");
  if (!html.includes("../KYRGYZSTAN_BIODIVERSITY_DATA_STANDARD.md")) errors.push(label + " chapter must link to the shared biodiversity data standard");
  if (!html.includes("Data quality requirements: occurrence datasets") || !html.includes("Guidelines for Using the Red List Categories and Criteria")) errors.push(label + " chapter must cite GBIF occurrence guidance and IUCN assessment guidance");
}

// Ethical, bilingual field-record protocols for the two Kyrgyzstan biodiversity chapters.
for (const [label, html, id] of [
  ["flora", floraKyrgyzstanAuditFile, "flora-field-record-protocol"],
  ["fauna", faunaKyrgyzstanAuditFile, "fauna-field-record-protocol"]
]) {
  if (!html.includes('id="' + id + '"')) errors.push(label + " Kyrgyzstan chapter must include its field-record protocol");
  if (!html.includes("Minimum field record") || !html.includes("Минимум полевой записи")) errors.push(label + " field protocol must be bilingual and provide a minimum record");
  if (!html.includes("Example of a well-documented record") || !html.includes("Пример корректной записи")) errors.push(label + " field protocol must include a worked example");
}
if (!floraKyrgyzstanAuditFile.includes("herbarium voucher") || !floraKyrgyzstanAuditFile.includes("требуемых разрешений") || !floraKyrgyzstanAuditFile.includes("rare or protected species")) errors.push("flora field protocol must require lawful voucher collection and protect rare plants");
if (!faunaKyrgyzstanAuditFile.includes("camera-days") || !faunaKyrgyzstanAuditFile.includes("eDNA") || !faunaKyrgyzstanAuditFile.includes("repeat images as new animals")) errors.push("fauna field protocol must distinguish survey effort, eDNA and repeat detections");
if (!faunaKyrgyzstanAuditFile.includes("precise locations of rare species") || !faunaKyrgyzstanAuditFile.includes("population estimates")) errors.push("fauna field protocol must protect sensitive localities and distinguish detections from abundance");

// Scientific constraints for the first-priority Kyrgyzstan illustration set.
const imageScientificReview = fs.readFileSync(path.join(root, "IMAGE_SCIENTIFIC_REVIEW.md"), "utf8");
for (const row of p1DispositionRows) {
  const target = (row.match(/^\| `image-brief-[^ `]+` \| `([^ `]+)`/) || [])[1];
  const filename = target ? target.split("/").pop() : "";
  if (filename && !imageScientificReview.includes(filename)) errors.push("IMAGE_SCIENTIFIC_REVIEW.md is missing P1 asset " + filename);
}
if (!imageScientificReview.includes("13 P1") && !imageScientificReview.includes("13-item P1")) errors.push("IMAGE_SCIENTIFIC_REVIEW.md must document the complete P1 review scope");
if ((imageScientificReview.match(/\b(?:flora|fauna)-[a-z-]+\.webp\b/g) || []).length !== 13) errors.push("IMAGE_SCIENTIFIC_REVIEW.md must review all 13 P1 assets");
if (!imageScientificReview.includes("Fritillaria eduardii") || !imageScientificReview.includes("Petilium eduardii")) errors.push("IMAGE_SCIENTIFIC_REVIEW.md must preserve accepted Aygul name and synonym");
if (!imageScientificReview.includes("Panthera uncia") || !imageScientificReview.includes("Uncia uncia")) errors.push("IMAGE_SCIENTIFIC_REVIEW.md must explain current and historical snow-leopard nomenclature");
if (!imageScientificReview.includes("country-level presence is not") && !imageScientificReview.includes("country-level presence")) errors.push("IMAGE_SCIENTIFIC_REVIEW.md must prohibit unsupported oblast/locality inference");
if (!imageInsertionMap.includes("Fritillaria eduardii") || !imageInsertionMap.includes("синоним") || !imageInsertionMap.includes("вытаптывание")) errors.push("IMAGE_INSERTION_MAP.md must carry the corrected, conservation-safe Aygul illustration brief");
if (!imageScientificReview.includes("does not publish the full taxon list") ||
    !imageScientificReview.includes("disputed Suusamyr") ||
    !imageScientificReview.includes("Son-Kul paper") ||
    !imageScientificReview.includes("Triplophysa stoliczkae") ||
    !imageScientificReview.includes("unpublished 14-taxon Kempir-Abad list") ||
    !imageScientificReview.includes("not as an additional species") ||
    !imageScientificReview.includes("Gymnodiptychus dybowskii") ||
    !imageScientificReview.includes("D. dybowskii micromakulatus") ||
    !imageScientificReview.includes("D. gymnogaster micromakulatus") ||
    !imageScientificReview.includes("FAO 2013") ||
    !imageScientificReview.includes("Diptychus gymnogaster") ||
    !imageScientificReview.includes("Diptychus maculatus")) {
  errors.push("IMAGE_SCIENTIFIC_REVIEW.md: freshwater illustration constraints must not invent or prematurely label new fish records or duplicate synonym taxa");
}


// Seven-oblast species-evidence audit: enforce coverage and conservative interpretation.
const regionalSpeciesAudit = fs.readFileSync(path.join(root, "KYRGYZSTAN_SPECIES_AUDIT.md"), "utf8");
if (!regionalSpeciesAudit.includes("Son-Kul fish survey (sampling in 2020, 2021 and 2023; published 2023)") ||
    !regionalSpeciesAudit.includes("abstract/methods date discrepancy") ||
    !regionalSpeciesAudit.includes("Gymnodiptychus dybowskii") ||
    !regionalSpeciesAudit.includes("D. dybowskii micromakulatus") ||
    !regionalSpeciesAudit.includes("D. gymnogaster micromakulatus") ||
    !regionalSpeciesAudit.includes("voucher/genetic review")) {
  errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: Son-Kul fish survey must retain its sampling-date discrepancy and taxonomic evidence limits");
}
if (!regionalSpeciesAudit.includes("10.5281/zenodo.15253859") || !regionalSpeciesAudit.includes("seven floristic/biogeographical provinces, not the seven administrative oblasts") || !regionalSpeciesAudit.includes("397 specimens (37%) remained unidentified")) errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: 2025 regional flora paper must retain its expedition scope and unresolved-identification caveat");
if (!regionalSpeciesAudit.includes("Terskey Ala-Too expedition report") || !regionalSpeciesAudit.includes("10.5281/zenodo.20821615") || !regionalSpeciesAudit.includes("not a nationally representative inventory")) errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: Terskey Ala-Too report must retain its source and site-level scope limitation");

if (!faunaKyrgyzstanFile.includes("около 16 145 сурков") || !faunaKyrgyzstanFile.includes("about 16,145 marmots") || !faunaKyrgyzstanFile.includes("июне 2021 и июне 2022") || !faunaKyrgyzstanFile.includes("June 2021 and June 2022") || !faunaKyrgyzstanFile.includes("не полностью сопоставимы") || !faunaKyrgyzstanFile.includes("not fully comparable") || !faunaKyrgyzstanFile.includes("Vulnerable (VU)") || !faunaKyrgyzstanFile.includes("Critically Depleted") || !faunaKyrgyzstanFile.includes("13%") || !faunaKyrgyzstanFile.includes("final-project-report-2747") || !faunaKyrgyzstanFile.includes("10.2305/IUCN.UK.2023-1.RLTS.T12827A229617076.en") || !faunaKyrgyzstanFile.includes("small-mammals.org/2025/03/28/green-status-update-2025/")) errors.push("chapters/fauna-kyrgyzstan.html: Menzbier's marmot estimate and Red List / Green Status distinctions must remain sourced and separate");
if (!regionalSpeciesAudit.includes("Menzbier's marmot — survey estimate and two IUCN assessment frameworks") || !regionalSpeciesAudit.includes("16,145 animals") || !regionalSpeciesAudit.includes("recovery score of 13%")) errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: Menzbier's marmot estimate and IUCN framework distinction must remain documented");

const requiredOblasts = ["Jalal-Abad", "Issyk-Kul", "Naryn", "Osh", "Batken", "Talas", "Chuy"];
for (const oblast of requiredOblasts) {
  if (!regionalSpeciesAudit.includes("| " + oblast + " |")) errors.push("KYRGYZSTAN_SPECIES_AUDIT.md is missing the " + oblast + " oblast row");
}
if (!regionalSpeciesAudit.includes("not a national checklist") || !regionalSpeciesAudit.includes("does **not** certify every regional occurrence claim")) errors.push("Regional species audit must state its scope and avoid claiming a verified national checklist");
if (!regionalSpeciesAudit.includes("national checklist") || !regionalSpeciesAudit.includes("population estimate") || !regionalSpeciesAudit.includes("camera-trap")) errors.push("Regional species audit must distinguish evidence scope, abundance estimates and detection methods");
if (!regionalSpeciesAudit.includes("Red Data Book") || !regionalSpeciesAudit.includes("IUCN")) errors.push("Regional species audit must keep national and IUCN conservation systems distinct");
if (!regionalSpeciesAudit.includes("GBIF") || !regionalSpeciesAudit.includes("Occurrence data quality requirements")) errors.push("Regional species audit must retain authoritative occurrence-data methodology links");
for (const [label, html] of [["flora", floraKyrgyzstanAuditFile], ["fauna", faunaKyrgyzstanAuditFile]]) {
  const oblastHeadings = [...html.matchAll(/<h[23]\b[^>]*>([\s\S]*?)<\/h[23]>/gi)].map(m => m[1]);
  const expected = ["Jalal-Abad", "Issyk-Kul", "Naryn", "Osh", "Batken", "Talas", "Chuy"];
  for (const oblast of expected) {
    if (!oblastHeadings.some(h => h.includes(oblast))) errors.push(label + " regional chapter is missing the " + oblast + " oblast section heading");
  }
}


for (const [label, html] of [["flora", floraKyrgyzstanAuditFile], ["fauna", faunaKyrgyzstanAuditFile]]) {
  if (!html.includes('id="regional-evidence-reading-guide"')) errors.push(label + " regional chapter must explain how to interpret local, historical and national evidence");
  if (!html.includes("../KYRGYZSTAN_SPECIES_AUDIT.md")) errors.push(label + " regional chapter must link to the seven-oblast species-evidence audit");
  if (!html.includes("Suitable habitat is ecological context") || !html.includes("not population estimates")) errors.push(label + " regional evidence guide must distinguish habitat, detections and population estimates");
}


const requiredRegionalClaimSources = [
  "https://mnr.gov.kg/ru/posts/news/bes-aralskii-zapovednik-unikalnaya-prirodnaya-zona",
  "https://camcaproject.org/study-in-tien-shan-maral-in-kyrgyzstan/",
  "https://www.camp.kg/news/krasnoknizhnye-i-pereletnye.-posmotrite-kakih-ptic-zametili-na-issyk-kule?lang=en",
  "https://www.mnr.gov.kg/ru/posts/news/v-bes-tasskom-gosudarstvennom-prirodnom-parke-zafiksirovany-dikie-zivotnye",
  "https://www.mnr.gov.kg/en/posts/news/v-batkenskoi-oblasti-zaversen-vesennii-ucet-surkov-v-regione-nascityvaetsya-bolee-4-tysyac-osobei",
  "https://www.mnr.gov.kg/ru/posts/news/egeri-i-naucnye-sotrudniki-gosudarstvennogo-prirodnogo-parka-con-kemin-pri-ministerstve-prirodnyx-resursov-ekologii-i-texniceskogo-nadzora-kyrgyzskoi-respubliki-sobrali-dannye-s-fotolovusek-ustanovlennyx-na-territorii-zapovednogo-ucastka-kok-oirok"
];
for (const url of requiredRegionalClaimSources) {
  if (!faunaKyrgyzstanAuditFile.includes(url)) errors.push("Fauna regional claim is missing its direct source link: " + url);
}
if (!floraKyrgyzstanAuditFile.includes("https://scientificjournal.ru/a/107-bio/2480-current-state.html")) errors.push("Aygul-Tash flora profile must link directly to its supporting study");


if (!regionalSpeciesAudit.includes("Primary-source spot-check") || !regionalSpeciesAudit.includes("page metadata labels the region as Chuy")) errors.push("Regional species audit must record bounded primary-source checks and the Besh-Tash metadata anomaly");
for (const required of ["400–600", "4,146", "Nearly 7,000", "Menzbier", "Kök-Oyrok", "Petilium eduardii"]) {
  if (!regionalSpeciesAudit.includes(required)) errors.push("Regional species audit is missing the primary-source spot-check for " + required);
}

if (!floraKyrgyzstanAuditFile.includes("https://mnr.gov.kg/ru/posts/news/v-bes-tasskom-prirodnom-parke-uvelicivaetsya-cislennost-maralov")) errors.push("Besh-Tash flora richness claim must link to the Ministry's park profile");
if (!regionalSpeciesAudit.includes("separate Ministry notice dated 19 September 2025 explicitly places Besh-Tash in Talas Region")) errors.push("Regional audit must resolve the Besh-Tash administrative metadata discrepancy with corroborating evidence");

if (!faunaKyrgyzstanFile.includes("resource?r=central_asia_amphibians&amp;v=1.18") || !faunaKyrgyzstanFile.includes("version 1.18 of the GBIF regional checklist") || !faunaKyrgyzstanFile.includes("Bufotes") || !faunaKyrgyzstanFile.includes("does not replace current surveys in each oblast")) {
  errors.push("chapters/fauna-kyrgyzstan.html: latest GBIF Central Asian amphibian checklist must be linked, dated and scoped as a regional compilation");
}
if (!regionalSpeciesAudit.includes("Central Asian amphibian checklist (GBIF dataset, version 1.18, 26 October 2026)") || !regionalSpeciesAudit.includes("not a new Kyrgyz field survey")) {
  errors.push("Regional species audit must record the 2026 amphibian checklist and its non-fieldwork scope");
}
if (!regionalSpeciesAudit.includes("Argali genomic sample provenance") || !regionalSpeciesAudit.includes("Kyrgyzstan and Tajikistan") || !regionalSpeciesAudit.includes("author/supplementary-table resolution")) {
  errors.push("Regional species audit must flag the unresolved geographic-provenance discrepancy in the 2026 argali article and Dryad dataset");
}

if (!faunaKyrgyzstanFile.includes("wingeds.world/species/amphibia/kg") || !faunaKyrgyzstanFile.includes("30 September 2026") || !faunaKyrgyzstanFile.includes("Hynobius turkestanicus") || !faunaKyrgyzstanFile.includes("B. oblongus") || !faunaKyrgyzstanFile.includes("B. viridis")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Kyrgyz amphibian country snapshot must be dated and preserve the three unconfirmed taxa");
}
if (!faunaKyrgyzstanFile.includes("209 adult male green toads") || !faunaKyrgyzstanFile.includes("14 localities") || !faunaKyrgyzstanFile.includes("10.20363/BZB-2021.70.2.361") || !faunaKyrgyzstanFile.includes("triploid hybrids")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2021 peer-reviewed Bufotes study must retain sample scope, direct DOI and hybridization caveat");
}

if (!faunaKyrgyzstanFile.includes("B. viridis") || !faunaKyrgyzstanFile.includes("presence as unconfirmed") || !faunaKyrgyzstanFile.includes("A conservation listing and evidence of current occurrence are different things")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Red Data Book inclusion must not be presented as proof of current amphibian occurrence");
}

if (!faunaKyrgyzstanFile.includes("ORL_10.1-A-Non-Passerines.pdf") || !faunaKyrgyzstanFile.includes("possibly reaching just into southern Kyrgyzstan") || !faunaKyrgyzstanFile.includes("not a complete country-by-country occurrence list")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Tibetan Snowcock must remain a possible range-edge claim, not a confirmed Kyrgyzstan occurrence");
}
if (!faunaKyrgyzstanFile.includes("search_value=175953") || !faunaKyrgyzstanFile.includes("search_value=175954") || !faunaKyrgyzstanFile.includes("nomenclatural validity does not establish occurrence")) {
  errors.push("chapters/fauna-kyrgyzstan.html: both snowcock names must be taxonomically cross-referenced without conflating validity and locality evidence");
}
if (!regionalSpeciesAudit.includes("Snowcock taxonomy and Kyrgyzstan occurrence scope") || !regionalSpeciesAudit.includes("mapped possible range edge") || !regionalSpeciesAudit.includes("primary Kyrgyz locality record")) {
  errors.push("Regional species audit must preserve the distinction between snowcock taxonomy, possible range edge and documented Kyrgyz occurrence");
}

if (!faunaKyrgyzstanFile.includes("wingeds.world/species/reptile/kg") || !faunaKyrgyzstanFile.includes("19 October 2026") || !faunaKyrgyzstanFile.includes("43 species") || !faunaKyrgyzstanFile.includes("19 subspecies")) {
  errors.push("chapters/fauna-kyrgyzstan.html: dated Kyrgyz reptile list must retain its species and subspecies totals");
}
if (!faunaKyrgyzstanFile.includes("Tenuidactylus fedtschenkoi") || !faunaKyrgyzstanFile.includes("Varanus griseus") || !faunaKyrgyzstanFile.includes("page header says 44") || !faunaKyrgyzstanFile.includes("summary line reports 43")) {
  errors.push("chapters/fauna-kyrgyzstan.html: reptile account must distinguish introduced/absent taxa and flag the 44-versus-43 count discrepancy");
}
if (!faunaKyrgyzstanFile.includes("central_asia_reptile&amp;v=1.15") || !faunaKyrgyzstanFile.includes("26 October 2026") || !faunaKyrgyzstanFile.includes("including within <i class=\"latin\">Varanus</i>")) {
  errors.push("chapters/fauna-kyrgyzstan.html: latest GBIF Central Asian reptile checklist must be linked, dated and scoped");
}
if (!regionalSpeciesAudit.includes("Kyrgyzstan reptile country list (page checked 1 November 2026; source export labelled 19 October 2026)") || !regionalSpeciesAudit.includes("44-versus-43 discrepancy")) {
  errors.push("Regional species audit must record the dated reptile snapshot and unresolved count discrepancy");
}
if (!regionalSpeciesAudit.includes("Central Asian reptile checklist (GBIF dataset, version 1.15; published 26 October 2026, accessed 29 October 2026)") ||
    !regionalSpeciesAudit.includes("systematic literature review, prioritising official national Red Data Book editions") ||
    !regionalSpeciesAudit.includes("not based on field sampling")) {
  errors.push("Regional species audit must preserve the latest reptile checklist version, source hierarchy and non-field methodology");
}
if (!regionalSpeciesAudit.includes("44-versus-43") ||
    !regionalSpeciesAudit.includes("8 national Red Data Book entries (6 species and 2 subspecies)") ||
    !regionalSpeciesAudit.includes("not a fresh legal review of the decree annex")) {
  errors.push("Regional species audit must preserve reptile count discrepancy and distinguish compiled Red Book mapping from legal verification");
}
if (!faunaKyrgyzstanFile.includes("precise position is intentionally not reproduced in the atlas") ||
    !faunaKyrgyzstanFile.includes("one pair in Boom Gorge near Kok-Moynok village")) {
  errors.push("Black Stork breeding account must retain the dated single-pair evidence and avoid publishing the precise nest location");
}
if (!regionalSpeciesAudit.includes("Black Stork breeding record at Boom Gorge (Romanovskaya, 2015;") ||
    !regionalSpeciesAudit.includes("four downy chicks on 24 May") ||
    !regionalSpeciesAudit.includes("do not reproduce the paper's road-kilometre marker")) {
  errors.push("Regional species audit must preserve Black Stork breeding chronology and sensitive-locality handling");
}

if (!faunaKyrgyzstanFile.includes("fishbase.se/country/CountryChecklist.php?c_code=417") || !faunaKyrgyzstanFile.includes("31 species currently present") || !faunaKyrgyzstanFile.includes("explicitly labelled the list incomplete") || !faunaKyrgyzstanFile.includes("73 fish species")) {
  errors.push("chapters/fauna-kyrgyzstan.html: fish totals must distinguish the 2013 FAO synthesis from the incomplete current FishBase list");
}
if (!faunaKyrgyzstanFile.includes("do not demonstrate a sharp decline") || !faunaKyrgyzstanFile.includes("not as a definitive national checklist")) {
  errors.push("chapters/fauna-kyrgyzstan.html: incompatible fish totals must not be interpreted as a population trend or definitive national inventory");
}
if (!regionalSpeciesAudit.includes("National fish totals: FAO 2013 versus FishBase (checked 1 November 2026)") || !regionalSpeciesAudit.includes("31 currently present but explicitly labels its country list incomplete")) {
  errors.push("Regional species audit must retain FishBase incompleteness and the non-comparable FAO/FishBase fish totals");
}
if (!regionalSpeciesAudit.includes("Issyk-Kul fish survey reported by FAO (December 2024)") || !regionalSpeciesAudit.includes("72 specimens of three species")) {
  errors.push("Regional species audit must preserve the bounded 2024 Issyk-Kul fish sample and distinguish it from a full inventory");
}

if (!faunaKyrgyzstanFile.includes("ibnaskr.org/amnh-fish-research-kyrgyzstan-2026/") || !faunaKyrgyzstanFile.includes("ibnaskr.org/laboratoriya-ikhtiologii-i-gidrobiologii/")) {
  errors.push("chapters/fauna-kyrgyzstan.html: current fish research sources must be linked");
}
if (!regionalSpeciesAudit.includes("Institute of Biology NAS KR fish research with AMNH (14 October 2026)")) {
  errors.push("Regional species audit must record the current Institute and AMNH fish research");
}
if (!regionalSpeciesAudit.includes("Kyrgyzstan amphibian country list (page snapshot generated 12 October 2026; regional dataset version 1.18 published 26 October 2026)") || !regionalSpeciesAudit.includes("4 resident, 3 unconfirmed") || !regionalSpeciesAudit.includes("33 core taxon records") || !regionalSpeciesAudit.includes("must not be quoted as a Kyrgyzstan species total")) {
  errors.push("Regional species audit must retain the corrected amphibian snapshot date, five-country dataset scope and country presence categories");
}
if (!regionalSpeciesAudit.includes("Green-toad morphology and locality study (Litvinchuk, Svinin & Dujsebayeva, 2021; DOI 10.20363/BZB-2021.70.2.361)") || !regionalSpeciesAudit.includes("209 adult males from 14 localities across Kazakhstan and Kyrgyzstan combined") || !regionalSpeciesAudit.includes("six Kyrgyzstan localities and 117 specimens") || !regionalSpeciesAudit.includes("not all in Kyrgyzstan")) {
  errors.push("Regional species audit must retain the primary 2021 Bufotes paper's two-country sample scope and Kyrgyzstan subset");
}

if (!faunaKyrgyzstanAuditFile.includes("https://mnr.gov.kg/ru/posts/news/sotrudnikami-talasskogo-regionalnogo-upravleniya-ministerstva-prirodnyx-resursov-ekologii-i-texniceskogo-nadzora-provedeny-raboty-po-ucyotu-cislennosti-obektov-zivotnogo-mira")) errors.push("Talas multi-site marmot survey must link to its Ministry source");

if (!faunaKyrgyzstanAuditFile.includes("https://mnr.gov.kg/ru/posts/news/osskim-regionalnym-upravleniem-ministerstva-prirodnyx-resursov-ekologii-i-texniceskogo-nadzora-na-territorii-gosudarstvennogo-prirodnogo-zapovednika-kulun-ata-uspesno-provedyon-ocerednoi-kompleks-meropriyatii-po-monitoringu-bioraznoobraziya")) errors.push("Osh Region Kulun-Ata detections must link to the Ministry source");

// The 2026 Kempir-Abad expedition is a dated institutional report, not a complete local checklist.
if (!faunaKyrgyzstanFile.includes("https://oshsu.kg/public/en/news/4569") ||
    !faunaKyrgyzstanFile.includes("14 видов рыб") ||
    !faunaKyrgyzstanFile.includes("14 fish species") ||
    !faunaKyrgyzstanFile.includes("Diptychus maculatus") ||
    !faunaKyrgyzstanFile.includes("not a completed reservoir checklist")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Kempir-Abad fish expedition must retain its source, taxonomic follow-up and checklist-scope caveat");
}
if (!regionalSpeciesAudit.includes("Kempir-Abad basin fish expedition (30 July–4 August 2026)") ||
    !regionalSpeciesAudit.includes("not a completed reservoir/oblast checklist") ||
    !regionalSpeciesAudit.includes("molecular-genetic analysis")) {
  errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: Kempir-Abad fish expedition must retain its date, unresolved analysis and evidence limits");
}

// Preserve the Suusamyr paper's internally inconsistent total and unresolved Triplophysa identification.
if (!faunaKyrgyzstanFile.includes("10.36979/1694-500X-2025-25-12-159-166") ||
    !faunaKyrgyzstanFile.includes("Triplophysa stoliczkai") ||
    !faunaKyrgyzstanFile.includes("Triplophysa elegans") ||
    !faunaKyrgyzstanFile.includes("Diptychus gymnogaster") ||
    !faunaKyrgyzstanFile.includes("should not be counted as separate species") ||
    !faunaKyrgyzstanFile.includes("fishcatget.asp?spid=31906") ||
    !faunaKyrgyzstanFile.includes("not be used as a settled total")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Suusamyr fish study must retain its DOI, author-reported names, synonymy and unresolved count/taxonomy caveats");
}

if (!faunaKyrgyzstanFile.includes("central_asia_mammals&amp;v=1.12") ||
    !faunaKyrgyzstanFile.includes("version 1.12, GBIF") ||
    !faunaKyrgyzstanFile.includes("published 26 October 2026") ||
    !faunaKyrgyzstanFile.includes("not based on field sampling") ||
    !faunaKyrgyzstanFile.includes("lists 407 species") ||
    !faunaKyrgyzstanFile.includes("country profile 327") ||
    !faunaKyrgyzstanFile.includes("database 380") ||
    !faunaKyrgyzstanFile.includes("133 species regularly represented in open observation data") ||
    !faunaKyrgyzstanFile.includes("its list is incomplete")) {
  errors.push("chapters/fauna-kyrgyzstan.html: mammal checklist v1.12 and non-comparable bird checklist totals must retain date, source scope and non-field / incomplete-list caveats");
}
if (!regionalSpeciesAudit.includes("Mammal checklist version 1.12 and bird-list scope comparison") ||
    !regionalSpeciesAudit.includes("not based on field sampling") ||
    !regionalSpeciesAudit.includes("not a national checklist")) {
  errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: current mammal checklist version and bird-list scope comparison must be documented");
}

if (!faunaKyrgyzstanFile.includes("ZHETIM-BEL AND KARAKOL · CAMERA-TRAP MONITORING · 2025–2026") ||
    !faunaKyrgyzstanFile.includes("22–28 June 2026") ||
    !faunaKyrgyzstanFile.includes("still being processed") ||
    !faunaKyrgyzstanFile.includes("no count of independent detections") ||
    !faunaKyrgyzstanFile.includes("BISHKEK · IMPORTANT BIRD AREA") ||
    !faunaKyrgyzstanFile.includes("only confirmed nesting location") ||
    !faunaKyrgyzstanFile.includes("about 40 species") ||
    !faunaKyrgyzstanFile.includes("more than 200 bird species")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Zhetim-Bel camera-trap evidence and Bishkek IBA bird observations must retain dates, source scope and abundance / nesting-claim caveats");
}
if (!faunaKyrgyzstanFile.includes("v-fotolovuski-ustanovlennye-na-xrebte-zetim-bel") ||
    !faunaKyrgyzstanFile.includes("discover-bishkeks-wintering-bird-hotspot-field-visit-important-bird-area-global-significance")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Zhetim-Bel and Bishkek IBA primary institutional sources must remain linked");
}
if (!regionalSpeciesAudit.includes("Local bird and mammal evidence update — 1 November 2026") ||
    !regionalSpeciesAudit.includes("not a published survey dataset") ||
    !regionalSpeciesAudit.includes("only confirmed nesting site")) {
  errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: local 2025–2026 evidence and source attribution caveats must be documented");
}

// Preserve the June 2026 ministry-reported Common Crane breeding record and its historical qualification.
if (!faunaKyrgyzstanFile.includes("ISSYK-KUL · JETY-OGUZ · COMMON CRANE BREEDING RECORD · 2026") ||
    !faunaKyrgyzstanFile.includes("Grus grus") ||
    !faunaKyrgyzstanFile.includes("19 April") ||
    !faunaKyrgyzstanFile.includes("24 May") ||
    !faunaKyrgyzstanFile.includes("second known national record") ||
    !faunaKyrgyzstanFile.includes("pervoe-gnezdovanie-serogo-zuravlya-na-vostocnom-pobereze-ozera-issyk-kul") ||
    !regionalSpeciesAudit.includes("Common Crane breeding record on Issyk-Kul — 2026") ||
    !regionalSpeciesAudit.includes("Do not infer range expansion")) {
  errors.push("2026 Issyk-Kul Common Crane breeding record must retain dates, primary source and cautious national-history interpretation");
}

// Preserve the August 2026 institutional record of a Demoiselle Crane migration aggregation.
if (!faunaKyrgyzstanFile.includes("ISSYK-KUL · DEMOISELLE CRANE MIGRATION · AUGUST 2026") ||
    !faunaKyrgyzstanFile.includes("approximately 2,000 Demoiselle Cranes") ||
    !faunaKyrgyzstanFile.includes("must not be automatically combined") ||
    !faunaKyrgyzstanFile.includes("zhuravl-krasavka-issyk-kul-2026") ||
    !regionalSpeciesAudit.includes("Issyk-Kul: Demoiselle Crane migration aggregation — August 2026") ||
    !regionalSpeciesAudit.includes("do not treat it as a national population estimate or trend")) {
  errors.push("2026 Issyk-Kul Demoiselle Crane aggregation must retain its source, approximate count and non-population scope");
}

const externalReviewPacket = fs.readFileSync(path.join(root, "EXTERNAL_REVIEW_PACKET.md"), "utf8");
for (const phrase of [
  "### G4 — Scientific review",
  "### G5 — Bilingual editorial and release review",
  "Son-Kul fish survey (Sarieva, Konurbaev & Osmonov, 2023)",
  "Kempir-Abad basin expedition",
  "Argali genomic study and Dryad metadata",
  "Tibetan Snowcock occurrence",
  "Black-necked Crane candidate near Soek Pass",
  "G4 and G5 remain **open**"
]) {
  if (!externalReviewPacket.includes(phrase)) errors.push("EXTERNAL_REVIEW_PACKET.md: missing independent-review scope or sign-off requirement: " + phrase);
}

if (!regionalSpeciesAudit.includes("Suusamyr Valley fish survey (fieldwork 2024; published 2025)") ||
    !regionalSpeciesAudit.includes("not infer a settled 4+1 total") ||
    !regionalSpeciesAudit.includes("Diptychus gymnogaster` as a synonym of `D. maculatus") ||
    !regionalSpeciesAudit.includes("voucher/specimen review") ||
    !regionalSpeciesAudit.includes("fishcatget.asp?spid=31906")) {
  errors.push("KYRGYZSTAN_SPECIES_AUDIT.md: Suusamyr fish evidence must retain its count discrepancy, osman synonym and specimen-review requirement");
}

if (errors.length) {
  console.error("Biology checks failed:\n" + errors.map(x => " - " + x).join("\n"));
  process.exit(1);
}
console.log("Biology checks passed: " + pages.length + " HTML pages, " + links + " local paths, " + scripts + " inline scripts, " + buttons + " typed buttons.");
