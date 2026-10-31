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
if (pages.length !== 13) errors.push("Expected 13 Biology HTML pages; found " + pages.length);
const coreChapters = [
  "botany.html", "zoology.html", "cell-biology.html", "anatomy.html",
  "genetics.html", "microbiology.html", "ecology.html", "evolution.html",
  "biochemistry.html", "systematics.html"
];
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

const biochemistryFile = fs.readFileSync(path.join(root, "chapters", "biochemistry.html"), "utf8");
if (!biochemistryFile.includes("does not shift the equilibrium position") || !biochemistryFile.includes("не меняет его положение")) {
  errors.push("chapters/biochemistry.html: enzyme explanation must state that enzymes do not shift equilibrium");
}
if (!biochemistryFile.includes("actual ΔG in a cell depends") || !biochemistryFile.includes("Фактическое значение ΔG в клетке зависит")) {
  errors.push("chapters/biochemistry.html: ATP hydrolysis explanation must qualify cellular ΔG");
}

const botanyFile = fs.readFileSync(path.join(root, "chapters", "botany.html"), "utf8");
if (!botanyFile.includes("function updateOrgan()") || !botanyFile.includes("updateOrgan();updatePhoto();updateConditionLabels()")) {
  errors.push("chapters/botany.html: language switching must refresh organ and photosynthesis model outputs");
}
if (!botanyFile.includes('b.setAttribute("aria-pressed",String(b.dataset.organ===selectedOrgan))')) {
  errors.push("chapters/botany.html: organ selector must expose its selected state");
}
const geneticsFile = fs.readFileSync(path.join(root, "chapters", "genetics.html"), "utf8");
if (!geneticsFile.includes("let selectedMutation=null") || !geneticsFile.includes("updateDynamic();updateMutation()")) {
  errors.push("chapters/genetics.html: mutation model must preserve and translate selection on language switch");
}

const evolutionFile = fs.readFileSync(path.join(root, "chapters", "evolution.html"), "utf8");
for (const url of ["19-2-population-genetics", "19-3-adaptive-evolution"]) {
  if (!evolutionFile.includes("openstax.org/books/biology-2e/pages/" + url)) errors.push("chapters/evolution.html: missing topic-matched OpenStax reference " + url);
}
if (!evolutionFile.includes("Illustrative frequencies after several generations") || !evolutionFile.includes("not a prediction for a real population")) errors.push("chapters/evolution.html: selection model must be labelled illustrative, not predictive");
if (!evolutionFile.includes("function localizeControls()") || !evolutionFile.includes("localizeControls();updateModules()")) errors.push("chapters/evolution.html: interactive controls must relabel when the language changes");
if (!/data-selection="high" aria-pressed="false"/.test(evolutionFile) || !/data-era="human" aria-pressed="false"/.test(evolutionFile)) errors.push("chapters/evolution.html: toggle controls must expose initial pressed states");
const microbiologyFile = fs.readFileSync(path.join(root, "chapters", "microbiology.html"), "utf8");
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
if (!faunaKyrgyzstanFile.includes("135 242 SNP-маркеров") || !faunaKyrgyzstanFile.includes("88 образцов архара") || !faunaKyrgyzstanFile.includes("O. a. polii") || !faunaKyrgyzstanFile.includes("Pamir Plateau")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 argali genetics evidence must retain initial and analysed sample sizes, named subspecies and Pamir scope caveat");
}
if (!faunaKyrgyzstanFile.includes("135 242 SNP-маркеров") || !faunaKyrgyzstanFile.includes("72 образца архара") || !faunaKyrgyzstanFile.includes("does not cover every population")) {
  errors.push("chapters/fauna-kyrgyzstan.html: 2026 argali genetics evidence must retain sample size and scope caveat");
}
if (!faunaKyrgyzstanFile.includes("689 маралов") || !faunaKyrgyzstanFile.includes("нельзя напрямую приравнивать") || !faunaKyrgyzstanFile.includes("cannot be directly equated")) {
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
if (!faunaKyrgyzstanFile.includes("Coregonus lavaretus") || !faunaKyrgyzstanFile.includes("Coregonus peled") || !faunaKyrgyzstanFile.includes("Triplophysa stoliczkae")) {
  errors.push("chapters/fauna-kyrgyzstan.html: Son-Kul fish account must retain the 2021–2023 field-study taxa");
}
if (!faunaKyrgyzstanFile.includes("2004–2005 годов") || !faunaKyrgyzstanFile.includes("описан как озеро без рыб") || !faunaKyrgyzstanFile.includes("described as fishless")) {
  errors.push("chapters/fauna-kyrgyzstan.html: fishless Chatyr-Kul and fish-bearing Son-Kul distinction must remain explicit");
}
if (!faunaKyrgyzstanFile.includes("не превращать в актуальную оценку численности") || !faunaKyrgyzstanFile.includes("must not be converted into a current abundance estimate")) {
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

const anatomyFile = fs.readFileSync(path.join(root, "chapters/anatomy.html"), "utf8");
if (!anatomyFile.includes("pages/19-introduction") || !anatomyFile.includes("pages/20-5-circulatory-pathways") || !anatomyFile.includes("pages/22-introduction")) errors.push("chapters/anatomy.html: heart, circulatory pathways and respiratory-system references are required");
if (!anatomyFile.includes("артерии определяются направлением кровотока от сердца") || !anatomyFile.includes("arteries are defined by blood flow away from the heart")) errors.push("chapters/anatomy.html: artery definition must distinguish direction of flow from oxygen content");
if (!anatomyFile.includes("лёгочные артерии проводят бедную кислородом кровь от правого желудочка к лёгким") || !anatomyFile.includes("лёгочные вены возвращают богатую кислородом кровь к левому предсердию")) errors.push("chapters/anatomy.html: pulmonary circuit must correctly identify oxygen-poor arterial and oxygen-rich venous blood");
if (!anatomyFile.includes("pulmonary arteries carry oxygen-poor blood from the right ventricle to the lungs") || !anatomyFile.includes("pulmonary veins return oxygen-rich blood to the left atrium")) errors.push("chapters/anatomy.html: English pulmonary-circuit explanation must match the Russian account");
const geneticsAuditFile = fs.readFileSync(path.join(root, "chapters/genetics.html"), "utf8");
if (!/data-template="TAC" aria-pressed="true"/.test(geneticsAuditFile) || !geneticsAuditFile.includes('x.setAttribute("aria-pressed",String(x.dataset.template===t))')) errors.push("chapters/genetics.html: transcription-template controls must expose and update selected state");
if (!/data-mutation="insertion" aria-pressed="false"/.test(geneticsAuditFile) || !geneticsAuditFile.includes('b.setAttribute("aria-pressed",String(b.dataset.mutation===selectedMutation))')) errors.push("chapters/genetics.html: mutation controls must expose selected state to assistive technology");
if (!geneticsAuditFile.includes("AUG · AGC · UUU · UGG · A…")) errors.push("chapters/genetics.html: insertion example must display the shifted reading frame accurately");
if (!geneticsAuditFile.includes("ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi") || !geneticsAuditFile.includes("ncbi.nlm.nih.gov/books/NBK9849/")) errors.push("chapters/genetics.html: authoritative genetic-code and translation references are required");

if (errors.length) {
  console.error("Biology checks failed:\n" + errors.map(x => " - " + x).join("\n"));
  process.exit(1);
}
console.log("Biology checks passed: " + pages.length + " HTML pages, " + links + " local paths, " + scripts + " inline scripts, " + buttons + " typed buttons.");
