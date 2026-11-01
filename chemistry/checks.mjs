import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const htmlFiles = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.isFile() && entry.name.endsWith(".html")) htmlFiles.push(full);
  }
}
walk(root);

const errors = [];
let checkedLinks = 0;
let checkedScripts = 0;

let checkedBilingualPages = 0;

function objectLiteralAt(source, start) {
  let depth = 0, quote = null, escaped = false;
  for (let i = start; i < source.length; i++) {
    const char = source[i];
    if (quote) {
      if (escaped) escaped = false;
      else if (char === "\\") escaped = true;
      else if (char === quote) quote = null;
      continue;
    }
    if (char === '"' || char === "'" || char === "\`") { quote = char; continue; }
    if (char === "{") depth++;
    if (char === "}" && --depth === 0) return source.slice(start, i + 1);
  }
  return null;
}


function arrayLiteralAt(source, start) {
  let depth = 0, quote = null, escaped = false;
  for (let i = start; i < source.length; i++) {
    const char = source[i];
    if (quote) {
      if (escaped) escaped = false;
      else if (char === "\\") escaped = true;
      else if (char === quote) quote = null;
      continue;
    }
    if (char === '"' || char === "'" || char === "\`") { quote = char; continue; }
    if (char === "[") depth++;
    if (char === "]" && --depth === 0) return source.slice(start, i + 1);
  }
  return null;
}

function plainText(markup) {
  return markup
    .replace(/<\/?[a-zA-Z][^>]*>/g, "")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)))
    .replace(/&#x([\da-f]+);/gi, (_, code) => String.fromCodePoint(parseInt(code, 16)))
    .trim()
    .replace(/\s+/g, " ");
}


for (const file of htmlFiles) {
  const source = fs.readFileSync(file, "utf8");
  const relativeFile = path.relative(root, file);

  const localizedKeys = [...new Set([...source.matchAll(/data-(?:i|alt-i)=["']([^"']+)["']/g)].map(match => match[1]))];
  if (localizedKeys.length) {
    let dictionary = null;
    let dictionaryScore = -1;
    for (const match of source.matchAll(/\b(?:const|let|var)\s+[\w$]+\s*=\s*\{/g)) {
      const literal = objectLiteralAt(source, match.index + match[0].lastIndexOf("{"));
      if (!literal) continue;
      try {
        const candidate = vm.runInNewContext("(" + literal + ")");
        if (candidate && candidate.ru && candidate.en &&
            typeof candidate.ru === "object" && typeof candidate.en === "object" &&
            !Array.isArray(candidate.ru) && !Array.isArray(candidate.en)) {
          const score = localizedKeys.filter(key => key in candidate.ru && key in candidate.en).length;
          if (score > dictionaryScore) {
            dictionary = candidate;
            dictionaryScore = score;
          }
        }
      } catch { /* Not a standalone translation dictionary. */ }
    }
    if (!dictionary) {
      errors.push(relativeFile + ": data-i elements have no detectable RU/EN translation dictionary");
    } else {
      checkedBilingualPages++;
      for (const key of localizedKeys) {
        if (!(key in dictionary.ru)) errors.push(relativeFile + ": missing Russian translation key " + key);
        if (!(key in dictionary.en)) errors.push(relativeFile + ": missing English translation key " + key);
      }
      for (const match of source.matchAll(/<([a-z][\w-]*)\b([^>]*\bdata-i=["']([^"']+)["'][^>]*)>([\s\S]*?)<\/\1>/gi)) {
        const key = match[3];
        if (key in dictionary.ru) {
          const initialText = plainText(match[4]);
          const russianText = plainText(dictionary.ru[key]);
          if (initialText !== russianText) {
            errors.push(relativeFile + ": initial Russian text differs from translation dictionary for " + key);
          }
        }
      }
    }
  }

  if (!/<html\b[^>]*lang=["'][^"']+["']/i.test(source)) errors.push(relativeFile + ": missing html lang attribute");
  if (!/<meta\s+name=["']viewport["']/i.test(source)) errors.push(relativeFile + ": missing viewport meta tag");
  if (!/<title>\s*[^<]+<\/title>/i.test(source)) errors.push(relativeFile + ": missing or empty document title");
  if (!/<h1\b[^>]*>[\s\S]*?<\/h1>/i.test(source)) errors.push(relativeFile + ": missing primary page heading");

  for (const match of source.matchAll(/<img\b([^>]*)>/gi)) {
    if (!/\balt\s*=\s*(?:[\"'][^\"']*[\"']|[^\s>]+)/i.test(match[1])) {
      errors.push(relativeFile + ": image missing alt attribute");
    }
  }

  const idValues = [...source.matchAll(/\bid=["']([^"']+)["']/gi)].map(m => m[1]);
  const ids = new Set(idValues);
  if (ids.size !== idValues.length) errors.push(relativeFile + ": duplicate id attributes found");
  for (const match of source.matchAll(/<(?:a|img|script|link|source)[^>]*?\b(href|src)=["']([^"']+)["'][^>]*>/gi)) {
    const attribute = match[1].toLowerCase();
    const value = match[2].trim();
    if (!value || /^(?:https?:|mailto:|tel:|data:|javascript:|#)/i.test(value)) {
      if (value.startsWith("#") && value.length > 1 && !ids.has(decodeURIComponent(value.slice(1)))) errors.push(relativeFile + ": missing in-page anchor " + value);
      continue;
    }
    const parts = value.split("#", 2);
    const cleanPath = decodeURIComponent(parts[0].split("?")[0]);
    const fragment = parts[1];
    const target = path.resolve(path.dirname(file), cleanPath);
    checkedLinks++;
    if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
      errors.push(relativeFile + ': broken ' + attribute + ' path "' + value + '"');
      continue;
    }
    if (fragment && target.endsWith(".html")) {
      const targetSource = fs.readFileSync(target, "utf8");
      const targetIds = new Set([...targetSource.matchAll(/\bid=["']([^"']+)["']/gi)].map(m => m[1]));
      if (!targetIds.has(decodeURIComponent(fragment))) errors.push(relativeFile + ': missing anchor "' + fragment + '" in ' + path.relative(root, target));
    }
  }

  for (const match of source.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    const attrs = match[1];
    const code = match[2].trim();
    if (!code || /\bsrc=/i.test(attrs)) continue;
    try {
      new vm.Script(code, { filename: relativeFile + ":inline-script" });
      checkedScripts++;
    } catch (error) {
      errors.push(relativeFile + ": JavaScript syntax error: " + error.message);
    }
  }
}

const redoxSource = fs.readFileSync(path.join(root, "chapters/redox.html"), "utf8");
for (const [label, evidence] of [
  ["oxygen difluoride exception", "OF₂"],
  ["peroxide oxygen state", "H₂O₂"],
  ["superoxide average oxygen state", "KO₂"],
  ["Russian oxidation-state exception note", "Важные исключения:"],
  ["English oxidation-state exception translation", "Important exceptions:"],
  ["calculated oxygen state in OF₂", "x(O) = +2"],
  ["peroxide oxidation state", "кислород −1"],
  ["superoxide average oxidation state", "кислорода −½"]
]) {
  if (!redoxSource.includes(evidence)) errors.push("chapters/redox.html: missing or incomplete " + label);
}

const lifeSource = fs.readFileSync(path.join(root, "chapters/chemistry-of-life.html"), "utf8");
for (const [label, evidence] of [
  ["carbohydrate classification in Russian", "моносахариды, дисахариды и полисахариды"],
  ["storage polysaccharides", "Крахмал и гликоген"],
  ["cellulose structural role", "целлюлоза выполняет структурную функцию"],
  ["carbohydrate classification in English", "Carbohydrates are classified by the number of sugar units"],
  ["storage polysaccharides in English", "Starch and glycogen are storage polysaccharides"],
  ["carbohydrate formula caveat", "Not all carbohydrates follow the formula"],
  ["phospholipid amphiphilicity in Russian", "Фосфолипиды амфифильны"],
  ["phospholipid bilayer in Russian", "липидного бислоя клеточных мембран"],
  ["phospholipid amphiphilicity in English", "Phospholipids are amphiphilic"],
  ["phospholipid bilayer in English", "lipid bilayer in cell membranes"]
]) {
  if (!lifeSource.includes(evidence)) errors.push("chapters/chemistry-of-life.html: missing or incomplete " + label);
}


for (const [label, evidence] of [
  ["amino acid functional groups in Russian", "Аминокислоты содержат аминогруппу и карбоксильную группу"],
  ["zwitterion and pH in Russian", "цвиттерионная форма"],
  ["amino acid amphoterism in Russian", "аминокислоты амфотерны"],
  ["ribosomal peptide synthesis in Russian", "рибосома формирует пептидную связь"],
  ["protein secondary structure in Russian", "α-спирали и β-слои"],
  ["protein quaternary structure caveat in Russian", "не у всех белков"],
  ["protein denaturation and primary structure in Russian", "без обычного разрыва пептидных связей первичной структуры"],
  ["protein denaturation and function in Russian", "белок теряет часть своей функции"],
  ["protein refolding caveat in Russian", "обратное сворачивание возможно не всегда"],
  ["disulfide bridges in Russian", "дисульфидные мостики"],
  ["enzyme activation energy and Gibbs energy in Russian", "не изменяют суммарное изменение энергии Гиббса ΔG"],
  ["enzyme active site and substrate complex in Russian", "Субстрат связывается с активным центром фермента"],
  ["enzyme specificity in Russian", "обеспечивают специфичность"],
  ["amino acid functional groups in English", "Amino acids contain an amino group and a carboxyl group"],
  ["zwitterion and pH in English", "is called a zwitterion"],
  ["ribosomal peptide synthesis in English", "the ribosome forms peptide bonds"],
  ["protein secondary structure in English", "α-helices and β-sheets"],
  ["protein quaternary structure caveat in English", "is not present in every protein"],
  ["protein denaturation and primary structure in English", "without normally breaking the peptide bonds of the primary structure"],
  ["protein denaturation and function in English", "protein may lose some or all of its function"],
  ["protein refolding caveat in English", "refolding is not always possible"],
  ["disulfide bridges in English", "disulfide bridges"],
  ["enzyme activation energy and equilibrium in English", "do not change the overall Gibbs energy change ΔG or the position of chemical equilibrium"],
  ["enzyme active site and substrate complex in English", "A substrate binds at an enzyme's active site"],
  ["enzyme specificity in English", "provide specificity, although it is not always absolute"]
]) {
  if (!lifeSource.includes(evidence)) errors.push("chapters/chemistry-of-life.html: missing or incomplete " + label);
}


for (const [label, evidence] of [
  ["DNA antiparallel orientation in Russian", "Две цепи ДНК ориентированы антипараллельно"],
  ["polymerase synthesis direction in Russian", "присоединяя нуклеотид к свободной 3′-OH-группе"],
  ["ATP hydrolysis coupling in Russian", "гидролиз до АДФ и неорганического фосфата"],
  ["ATP is not energy itself in Russian", "АТФ не является «энергией» сама по себе"],
  ["DNA antiparallel orientation in English", "The two DNA strands are antiparallel"],
  ["polymerase synthesis direction in English", "only in the 5′→3′ direction"],
  ["ATP hydrolysis coupling in English", "hydrolysis to ADP and inorganic phosphate"],
  ["ATP is not energy itself in English", "ATP is not energy itself"]
]) {
  if (!lifeSource.includes(evidence)) errors.push("chapters/chemistry-of-life.html: missing or incomplete " + label);
}


for (const [label, evidence] of [
  ["carbon fixation into biomass", "органические вещества биомассы"],
  ["bidirectional ocean carbon exchange", "поглощает CO₂ из атмосферы и отдаёт его обратно"],
  ["geological carbon storage", "длительные геологические сроки"],
  ["carbon cycle in English", "Photosynthesis transfers carbon from atmospheric CO₂"],
  ["bidirectional ocean exchange in English", "both absorbs CO₂ from the atmosphere and releases it back"],
  ["geological carbon storage in English", "long geological timescales"]
]) {
  if (!lifeSource.includes(evidence)) errors.push("chapters/chemistry-of-life.html: missing or incomplete " + label);
}

const periodicSource = fs.readFileSync(path.join(root, "periodic-table.html"), "utf8");
const periodicData = periodicSource.match(/const raw=\`([\s\S]*?)\`\.trim\(\);/);
if (!periodicData) {
  errors.push("periodic-table.html: element data block not found");
} else {
  const rows = periodicData[1].trim().split(/\r?\n/).map(line => line.split("|"));
  const symbols = rows.map(row => row[1]);
  const categories = new Set(["nonmetal", "noble", "alkali", "alkaline", "metalloid", "halogen", "post", "transition", "lanthanide", "actinide"]);
  if (rows.length !== 118) errors.push("periodic-table.html: expected 118 element records, found " + rows.length);
  if (new Set(symbols).size !== rows.length) errors.push("periodic-table.html: duplicate element symbols");
  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    if (row.length !== 8) errors.push("periodic-table.html: element record " + (i + 1) + " must have 8 fields");
    if (Number(row[0]) !== i + 1) errors.push("periodic-table.html: atomic numbers must form the sequence 1–118");
    if (!/^\[?\d+(?:\.\d+)?\]?$/.test(row[4] || "")) errors.push("periodic-table.html: invalid atomic-mass notation for record " + (i + 1));
    if (!categories.has(row[5])) errors.push("periodic-table.html: unknown element category for record " + (i + 1));
    if (!Number.isInteger(Number(row[6])) || !Number.isInteger(Number(row[7])) ||
        Number(row[6]) < 1 || Number(row[6]) > 18 || Number(row[7]) < 1 || Number(row[7]) > 7) {
      errors.push("periodic-table.html: invalid group or period for record " + (i + 1));
    }
    if (!row[2] || !row[3]) errors.push("periodic-table.html: missing bilingual element name for record " + (i + 1));
  }
}

const trainerSource = fs.readFileSync(path.join(root, "reaction-trainer.html"), "utf8");
const trainerTaskStart = trainerSource.indexOf("const tasks=");
if (trainerTaskStart < 0) {
  errors.push("reaction-trainer.html: reaction task bank not found");
} else {
  try {
    const literal = arrayLiteralAt(trainerSource, trainerTaskStart + "const tasks=".length);
    const tasks = vm.runInNewContext("(" + literal + ")");
    const subscriptDigits = { "₀":"0", "₁":"1", "₂":"2", "₃":"3", "₄":"4", "₅":"5", "₆":"6", "₇":"7", "₈":"8", "₉":"9" };
    const parseTrainerFormula = formula => {
      const counts = {};
      const tokens = [...formula.matchAll(/([A-Z][a-z]?)([₀-₉]*)/g)];
      if (!tokens.length || tokens.map(token => token[0]).join("") !== formula) throw new Error("unsupported formula " + formula);
      for (const token of tokens) {
        const countText = [...token[2]].map(digit => subscriptDigits[digit]).join("");
        const count = countText ? Number(countText) : 1;
        if (!Number.isSafeInteger(count) || count < 1) throw new Error("invalid subscript in " + formula);
        counts[token[1]] = (counts[token[1]] || 0) + count;
      }
      return counts;
    };
    const gcd = (a, b) => b ? gcd(b, a % b) : a;
    if (!Array.isArray(tasks) || tasks.length !== 6) {
      errors.push("reaction-trainer.html: expected 6 balancing tasks");
    } else tasks.forEach((task, index) => {
      const label = "reaction-trainer.html: task " + (index + 1);
      if (!Array.isArray(task.f) || !Array.isArray(task.c) || task.f.length !== task.c.length || task.f.length < 3) {
        errors.push(label + " has mismatched formulas and coefficients");
        return;
      }
      if (task.c.some(value => !Number.isSafeInteger(value) || value < 1)) {
        errors.push(label + " must use positive integer coefficients");
        return;
      }
      const totals = [{}, {}];
      task.f.forEach((formula, formulaIndex) => {
        const split = task.split || task.f.length - 1;
        if (!Number.isInteger(split) || split < 1 || split >= task.f.length) errors.push(label + " has an invalid reactant/product split");
        const side = formulaIndex < split ? 0 : 1;
        const atoms = parseTrainerFormula(formula);
        for (const [element, count] of Object.entries(atoms)) {
          totals[side][element] = (totals[side][element] || 0) + count * task.c[formulaIndex];
        }
      });
      if (JSON.stringify(Object.entries(totals[0]).sort()) !== JSON.stringify(Object.entries(totals[1]).sort())) {
        errors.push(label + " is not atom-balanced for its stored answer");
      }
      if (task.c.reduce((value, coefficient) => gcd(value, coefficient), 0) !== 1) {
        errors.push(label + " coefficients are not in the smallest whole-number ratio");
      }
      if (!Array.isArray(task.hint) || task.hint.length !== 2 || !Array.isArray(task.why) || task.why.length !== 2 ||
          [...task.hint, ...task.why].some(value => typeof value !== "string" || !value.trim())) {
        errors.push(label + " is missing Russian or English hints/explanations");
      }
    });
  } catch (error) {
    errors.push("reaction-trainer.html: could not validate reaction tasks: " + error.message);
  }
}

const glossarySource = fs.readFileSync(path.join(root, "glossary.html"), "utf8");
const glossaryMatch = glossarySource.match(/\bconst entries\s*=\s*\[/);
if (!glossaryMatch) {
  errors.push("glossary.html: term data array not found");
} else {
  try {
    const literal = arrayLiteralAt(glossarySource, glossaryMatch.index + glossaryMatch[0].lastIndexOf("["));
    const entries = vm.runInNewContext("(" + literal + ")");
    const categories = new Set(["matter", "reaction", "solution", "organic", "environment"]);
    if (!Array.isArray(entries) || entries.length !== 102) {
      errors.push("glossary.html: expected 102 bilingual terms");
    } else {
      if (new Set(entries.map(entry => entry[0])).size !== entries.length) errors.push("glossary.html: duplicate Russian term titles");
      if (new Set(entries.map(entry => entry[1])).size !== entries.length) errors.push("glossary.html: duplicate English term titles");
      entries.forEach((entry, index) => {
        if (!Array.isArray(entry) || entry.length !== 5 ||
            entry.some(value => typeof value !== "string" || !value.trim()) ||
            !categories.has(entry[4])) {
          errors.push("glossary.html: malformed bilingual glossary record " + (index + 1));
        }
      });
    }
  } catch (error) {
    errors.push("glossary.html: could not parse term data: " + error.message);
  }
}

const quizSource = fs.readFileSync(path.join(root, "knowledge-check.html"), "utf8");
const quizMatch = quizSource.match(/\bconst questions\s*=\s*\{/);
if (!quizMatch) {
  errors.push("knowledge-check.html: bilingual question bank not found");
} else {
  const literal = objectLiteralAt(quizSource, quizMatch.index + quizMatch[0].lastIndexOf("{"));
  try {
    const questions = vm.runInNewContext("(" + literal + ")");
    for (const language of ["ru", "en"]) {
      const items = questions[language];
      if (!Array.isArray(items) || items.length !== 15) {
        errors.push("knowledge-check.html: expected 15 " + language + " questions");
        continue;
      }
      items.forEach((question, index) => {
        if (!question.q || !question.e || !Array.isArray(question.a) || question.a.length !== 4 ||
            !Number.isInteger(question.c) || question.c < 0 || question.c > 3) {
          errors.push("knowledge-check.html: malformed " + language + " question " + (index + 1));
        }
      });
    }
    if (Array.isArray(questions.ru) && Array.isArray(questions.en) &&
        questions.ru.length === questions.en.length) {
      questions.ru.forEach((question, index) => {
        if (question.c !== questions.en[index].c) {
          errors.push("knowledge-check.html: RU/EN answer key mismatch at question " + (index + 1));
        }
      });
    }
  } catch (error) {
    errors.push("knowledge-check.html: could not parse bilingual question bank: " + error.message);
  }
}

const assetRoot = path.join(root, "assets");
const svgFiles = [];
function walkSvg(dir) {
  if (!fs.existsSync(dir)) return;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walkSvg(full);
    else if (entry.isFile() && entry.name.toLowerCase().endsWith(".svg")) svgFiles.push(full);
  }
}
walkSvg(assetRoot);
for (const file of svgFiles) {
  const source = fs.readFileSync(file, "utf8");
  const relative = path.relative(root, file);
  if (!/<svg\b[^>]*\bviewBox=/i.test(source)) errors.push(relative + ": SVG missing viewBox");
  if (!/<svg\b[^>]*\brole=["']img["']/i.test(source)) errors.push(relative + ": SVG missing role=img");
  if (!/<title\b[^>]*>[\s\S]*?<\/title>/i.test(source)) errors.push(relative + ": SVG missing accessible title");
  if (!/<desc\b[^>]*>[\s\S]*?<\/desc>/i.test(source)) errors.push(relative + ": SVG missing accessible description");
}

const lowContrastSvgTextFills = ["#8c8c90", "#64766f", "#9a6a22", "#888", "#999"];
for (const file of svgFiles) {
  const source = fs.readFileSync(file, "utf8");
  const relative = path.relative(root, file);
  for (const color of lowContrastSvgTextFills) {
    if (source.toLowerCase().includes('fill="' + color + '"')) {
      errors.push(relative + ": replace low-contrast SVG text colour " + color);
    }
  }
}

const russianSvgFiles = svgFiles.filter(file => file.toLowerCase().endsWith("-ru.svg"));
for (const file of russianSvgFiles) {
  const source = fs.readFileSync(file, "utf8");
  const relative = path.relative(root, file);
  const title = source.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i)?.[1] || "";
  const description = source.match(/<desc\b[^>]*>([\s\S]*?)<\/desc>/i)?.[1] || "";
  if (!/[А-Яа-яЁё]/.test(title)) errors.push(relative + ": Russian SVG title must contain Cyrillic text");
  if (!/[А-Яа-яЁё]/.test(description)) errors.push(relative + ": Russian SVG description must contain Cyrillic text");
  const englishPath = file.replace(/-ru\.svg$/i, ".svg");
  if (!fs.existsSync(englishPath)) errors.push(relative + ": matching English SVG is missing");
}

const isotopeSvgPath = path.join(assetRoot, "isotope-abundance.svg");
if (fs.existsSync(isotopeSvgPath)) {
  const isotopeSvg = fs.readFileSync(isotopeSvgPath, "utf8");
  for (const [x, expectedNeutrons] of [[205, 6], [470, 7]]) {
    const start = isotopeSvg.indexOf('<g transform="translate(' + x + ' 185)">');
    const end = start < 0 ? -1 : isotopeSvg.indexOf("</g>", start);
    const nucleus = start < 0 || end < 0 ? "" : isotopeSvg.slice(start, end);
    const protons = (nucleus.match(/fill="#238b70"/g) || []).length;
    const neutrons = (nucleus.match(/fill="#e0a64d"/g) || []).length;
    if (protons !== 6 || neutrons !== expectedNeutrons) {
      errors.push("assets/isotope-abundance.svg: expected 6 protons and " + expectedNeutrons + " neutrons in nucleus at x=" + x);
    }
  }
}
const neutralisationSvgPath = path.join(assetRoot, "acid-base-neutralisation.svg");
if (fs.existsSync(neutralisationSvgPath)) {
  const neutralisationSvg = fs.readFileSync(neutralisationSvgPath, "utf8");
  if (!neutralisationSvg.includes('d="M20 132 C90 132 120 130 145 112 C160 100 164 75 185 75 C206 75 210 50 225 35 C250 18 300 20 350 20"')) {
    errors.push("assets/acid-base-neutralisation.svg: expected rising curve crossing pH 7 at the equivalence marker (x=185, y=75)");
  }
}

const homepage = fs.readFileSync(path.join(root, "index.html"), "utf8");
const chapterIds = [...homepage.matchAll(/["'](0[1-9]|1[0-2])["']/g)].map(m => m[1]);
if (new Set(chapterIds).size < 12) errors.push("index.html: expected all 12 chapter identifiers");

if (errors.length) {
  console.error("Chemistry atlas checks failed:");
  for (const error of errors) console.error(" - " + error);
  process.exit(1);
}
console.log("Chemistry atlas checks passed: " + htmlFiles.length + " HTML pages, " + checkedLinks + " local links/assets, " + checkedScripts + " inline scripts.");
console.log("Bilingual dictionaries checked: " + checkedBilingualPages + " pages.");
