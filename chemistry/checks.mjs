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

// Scientific and bilingual editorial evidence for foundational chapters.
const chapterEvidence = [
  ["chapters/atomic-structure.html", [
    ["atomic number defines element in Russian", "Число протонов Z определяет порядковый номер элемента"],
    ["atomic number defines element in English", "The number of protons Z defines the element's atomic number"],
    ["atomic diagram limitation in Russian", "Электроны не движутся по таким круговым дорожкам"],
    ["atomic diagram limitation in English", "Electrons do not travel along fixed circular tracks"],
    ["first-20 shell model qualification in Russian", "для первых 20 элементов"],
    ["first-20 shell model qualification in English", "for the first 20 elements"]
  ]],
  ["chapters/chemical-bonding.html", [
    ["ionic lattice is not isolated ion pairs in Russian", "это не отдельная пара ионов"],
    ["ionic lattice is not isolated ion pairs in English", "the ions are not isolated pairs"],
    ["bond and molecular polarity distinction in Russian", "Полярность отдельной связи и полярность всей молекулы"],
    ["bond and molecular polarity distinction in English", "The polarity of an individual bond is not the same as the polarity of an entire molecule"],
    ["CO2 and H2O geometry contrast in Russian", "в линейной молекуле CO₂ они компенсируются"],
    ["CO2 and H2O geometry contrast in English", "in linear CO₂ they cancel"]
  ]],
  ["chapters/acids-and-bases.html", [
    ["pH temperature qualification in Russian", "при другой температуре нейтральное значение pH может отличаться"],
    ["pH temperature qualification in English", "at other temperatures, neutral pH can differ"],
    ["pH outside textbook range in Russian", "могут выходить за его пределы"],
    ["pH outside textbook range in English", "can have values outside it"],
    ["acid strength differs from concentration in Russian", "Сила кислоты не то же самое, что концентрация"],
    ["acid strength differs from concentration in English", "Acid strength is not the same as concentration"],
    ["buffer approximation limits in Russian", "обе формы сопряжённой пары присутствуют в заметных количествах"],
    ["buffer approximation limits in English", "both forms of the conjugate pair are present in appreciable amounts"],
    ["finite buffer capacity in Russian", "буферная ёмкость исчерпывается"],
    ["finite buffer capacity in English", "exhausts the buffer capacity"]
  ]],
  ["chapters/solutions.html", [
    ["final solution volume in Russian", "V — конечный объём раствора"],
    ["final solution volume in English", "V is the final volume of the solution"],
    ["Henry's law partial pressure in Russian", "повышение парциального давления газа"],
    ["Henry's law partial pressure in English", "increasing a gas’s partial pressure"],
    ["dissolution rate differs from solubility in Russian", "Она не равна скорости растворения"],
    ["dissolution rate differs from solubility in English", "It is not the same as the rate of dissolving"],
    ["stirring does not alter equilibrium solubility in Russian", "сами по себе не меняют равновесную растворимость"],
    ["stirring does not alter equilibrium solubility in English", "by themselves do not change equilibrium solubility"],
    ["Qsp versus Ksp and nucleation caveat in Russian", "хотя зародышеобразование может задержать его появление"],
    ["Qsp versus Ksp and nucleation caveat in English", "although nucleation may delay its appearance"]
  ]],
  ["chapters/amount-of-substance.html", [
    ["mole exact entity count in Russian", "Один моль содержит ровно Nₐ заданных элементарных сущностей"],
    ["mole exact entity count in English", "One mole contains exactly Nₐ specified elementary entities"],
    ["particle identity depends on substance in Russian", "молекул, атомов, ионов или формульных единиц"],
    ["particle identity depends on substance in English", "molecules, atoms, ions or formula units"],
    ["precise entity-count result label in Russian", "Число элементарных сущностей"],
    ["precise entity-count figure caption in English", "approximate number of specified entities"]
  ]]
];
for (const [relative, evidenceList] of chapterEvidence) {
  const source = fs.readFileSync(path.join(root, relative), "utf8");
  for (const [label, evidence] of evidenceList) {
    if (!source.includes(evidence)) errors.push(relative + ": missing or changed " + label);
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
if (trainerSource.includes('$("next").onclick=next') ||
    !trainerSource.includes('if(completed){completed=false;index=0;score=0;render(true);return}') ||
    !trainerSource.includes('$("next").textContent=words[lang].next')) {
  errors.push("reaction-trainer.html: restarting must use one click handler and restore the localized Next label without double-advancing");
}
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

const lowContrastHtmlPatterns = [
  /--muted\s*:\s*#(?:888|8c8c90|85858a)\b/i,
  /--accent\s*:\s*#39836f\b/i,
  /#39836f\b/i,
  /#bd7059\b/i,
  /#63756b\b/i,
  /#79a9b0\b/i,
  /color\s*:\s*#77736e\b/i,
  /color\s*:\s*#999\b/i
];
for (const file of htmlFiles) {
  const source = fs.readFileSync(file, "utf8");
  for (const pattern of lowContrastHtmlPatterns) {
    if (pattern.test(source)) errors.push(path.relative(root, file) + ": low-contrast HTML text colour detected (" + pattern + ")");
  }
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


const imageSourcesPath = path.join(root, "IMAGE_SOURCES.md");
const imageAuditPath = path.join(root, "IMAGE_AUDIT.md");
if (!fs.existsSync(imageSourcesPath)) errors.push("IMAGE_SOURCES.md: required image source register is missing");
if (!fs.existsSync(imageAuditPath)) errors.push("IMAGE_AUDIT.md: required image audit is missing");
const imageSources = fs.existsSync(imageSourcesPath) ? fs.readFileSync(imageSourcesPath, "utf8") : "";
const imageAudit = fs.existsSync(imageAuditPath) ? fs.readFileSync(imageAuditPath, "utf8") : "";
for (const file of svgFiles) {
  const basename = path.basename(file);
  if (!imageSources.includes("`" + basename + "`")) errors.push("IMAGE_SOURCES.md: missing source-register record for " + basename);
  if (!imageAudit.includes("`" + basename + "`")) errors.push("IMAGE_AUDIT.md: missing audit record for " + basename);
  const paired = basename.endsWith("-ru.svg") ? basename.replace(/-ru\.svg$/i, ".svg") : basename.replace(/\.svg$/i, "-ru.svg");
  if (!fs.existsSync(path.join(assetRoot, paired))) errors.push("assets/" + basename + ": matching bilingual SVG variant is missing");
}
if (imageSources && /\| C — project SVG/.test(imageSources)) errors.push("IMAGE_SOURCES.md: do not assign category C to local SVGs until creator, authoring method and rights are evidenced");
if (imageSources && !imageSources.includes("Unclassified — project-local SVG")) errors.push("IMAGE_SOURCES.md: local SVG provenance must remain PENDING until evidenced");
const staticAssetRegister = imageSources.split("## Asset register")[1]?.split("## Non-file interactive visuals")[0] || "";
for (const id of ["CH-V01","CH-V02","CH-V03","CH-V04","CH-V05","CH-V06","CH-V07","CH-V08","CH-V09","CH-V10","CH-V11"]) {
  const rows = staticAssetRegister.split(/\r?\n/).filter(line => line.startsWith("| " + id + " |"));
  if (rows.length !== 1) errors.push("IMAGE_SOURCES.md: expected exactly one static asset row for " + id);
  else {
    const cells = rows[0].split("|");
    if (cells.length !== 14) errors.push("IMAGE_SOURCES.md: malformed Markdown columns in " + id);
    const enFile = cells[4]?.trim().replace(/^`|`$/g, "");
    const ruFile = cells[5]?.trim().replace(/^`|`$/g, "");
    if (!enFile || !ruFile || !fs.existsSync(path.join(assetRoot, enFile)) || !fs.existsSync(path.join(assetRoot, ruFile))) {
      errors.push("IMAGE_SOURCES.md: English/Russian asset paths must point to existing SVGs for " + id);
    }
  }
}
if (imageAudit && !/\bPENDING\b/.test(imageAudit)) errors.push("IMAGE_AUDIT.md: unresolved checks must remain explicitly marked PENDING");
for (const file of htmlFiles) {
  const source = fs.readFileSync(file, "utf8");
  const relative = path.relative(root, file);
  for (const match of source.matchAll(/<img\b([^>]*)>/gi)) {
    const attrs = match[1];
    const alt = attrs.match(/\balt\s*=\s*(["'])([\s\S]*?)\1/i)?.[2];
    if (alt === undefined || !alt.trim()) errors.push(relative + ": image alt text must be present and non-empty");
    const ru = attrs.match(/\bdata-svg-ru=["']([^"']+)["']/i)?.[1];
    const en = attrs.match(/\bdata-svg-en=["']([^"']+)["']/i)?.[1];
    if (ru && !en) errors.push(relative + ": localized SVG image is missing data-svg-en");
    if (en && !ru) errors.push(relative + ": localized SVG image is missing data-svg-ru");
    for (const ref of [ru, en].filter(Boolean)) {
      const resolved = path.resolve(path.dirname(file), ref.split("?")[0]);
      if (!fs.existsSync(resolved)) errors.push(relative + ": localized SVG reference does not exist: " + ref);
    }
  }
}


for (const id of ["CH-IV01", "CH-IV02", "CH-IV03", "CH-IV04"]) {
  if (!imageSources.includes(id)) errors.push("IMAGE_SOURCES.md: missing interactive visual record " + id);
  if (!imageAudit.includes(id)) errors.push("IMAGE_AUDIT.md: missing interactive visual audit " + id);
}
for (const [relative, minimum] of [["chapters/atomic-structure.html", 2], ["chapters/chemical-bonding.html", 3]]) {
  const pagePath = path.join(root, relative);
  if (!fs.existsSync(pagePath)) {
    errors.push(relative + ": interactive visual page is missing");
    continue;
  }
  const page = fs.readFileSync(pagePath, "utf8");
  const count = (page.match(/<svg\b/gi) || []).length;
  if (count < minimum) errors.push(relative + ": expected at least " + minimum + " inline SVG visual models; found " + count);
}
const stoichiometryPage = fs.readFileSync(path.join(root, "stoichiometry.html"), "utf8");
if (!stoichiometryPage.includes("Math.max(Math.abs(xa),Math.abs(xb),Number.MIN_VALUE)") ||
    !stoichiometryPage.includes("amountEpsA") ||
    !stoichiometryPage.includes("amountEpsB")) {
  errors.push("stoichiometry.html: limiting-reactant comparisons must use scale-relative tolerances for tiny amounts");
}
if (!stoichiometryPage.includes('raw.trim()!==""') ||
    !stoichiometryPage.includes("Number.isFinite(percent)") ||
    !stoichiometryPage.includes("amountEpsA,amountEpsB")) {
  errors.push("stoichiometry.html: optional yield must trim whitespace and reject non-finite percentage results");
}
const virtualLabPage = fs.readFileSync(path.join(root, "virtual-lab.html"), "utf8");
for (const [label, evidence] of [
  ["Russian monobasic-base scope", "сильного одноосновного основания (например, NaOH)"],
  ["English monobasic-base scope", "strong monobasic base (for example, NaOH)"],
  ["Russian dilute-solution and volume assumptions", "аддитивность объёмов"],
  ["English dilute-solution and volume assumptions", "additive volumes"],
  ["Russian activity limitation", "активность ионов"],
  ["English activity limitation", "ion activities"]
]) {
  if (!virtualLabPage.includes(evidence)) errors.push("virtual-lab.html: missing model-scope qualification: " + label);
}

const gasLawsPage = fs.readFileSync(path.join(root, "gas-laws.html"), "utf8");
if (!gasLawsPage.includes('particleNote:"Визуализация показывает только условное число частиц') ||
    !gasLawsPage.includes('particleNote:"The animation shows only a schematic particle count') ||
    !gasLawsPage.includes('data-i="particleNote"') ||
    !gasLawsPage.includes("does not model density, speed, trajectories or collisions")) {
  errors.push("gas-laws.html: particle illustration must disclose its limits in both languages");
}

const moleculeLabPage = fs.readFileSync(path.join(root, "molecule-lab.html"), "utf8");
for (const [key, ru, en] of [
  ["waterOption", "H₂O · Вода", "H₂O · Water"],
  ["co2Option", "CO₂ · Углекислый газ", "CO₂ · Carbon dioxide"],
  ["methaneOption", "CH₄ · Метан", "CH₄ · Methane"],
  ["ammoniaOption", "NH₃ · Аммиак", "NH₃ · Ammonia"]
]) {
  if (!moleculeLabPage.includes(key + ':"' + ru + '"') || !moleculeLabPage.includes(key + ':"' + en + '"') ||
      !moleculeLabPage.includes('data-i="' + key + '"')) {
    errors.push("molecule-lab.html: molecule selector option must switch RU/EN: " + key);
  }
}
if (!moleculeLabPage.includes('setAttribute("aria-label",t.workspaceLabel)')) {
  errors.push("molecule-lab.html: molecular workspace accessible name must switch RU/EN");
}

const bondingPage = fs.readFileSync(path.join(root, "chapters/chemical-bonding.html"), "utf8");
if (!bondingPage.includes('<div class="detail" aria-live="polite" aria-atomic="true">') ||
    !bondingPage.includes('diagram.setAttribute("role","img")') ||
    !bondingPage.includes('diagram.setAttribute("aria-label",d.title[lang]+". "+d.text[lang])')) {
  errors.push("chapters/chemical-bonding.html: each dynamic bonding model needs a localized accessible name and atomic polite detail announcement");
}

const periodicPage = fs.readFileSync(path.join(root, "periodic-table.html"), "utf8");
for (const key of ["trendTitle", "trendBody", "trendPlaceholder"]) {
  if (!periodicPage.includes(key + ':"') || !periodicPage.includes('data-t="' + key + '"')) {
    errors.push("periodic-table.html: Chapter 03 periodic-trends placeholder must be bilingual: " + key);
  }
}
if (!periodicPage.includes("atomic radius generally increases down and to the left") ||
    !periodicPage.includes("first ionisation energy and electronegativity generally increase up and to the right") ||
    !periodicPage.includes("electron configurations create exceptions")) {
  errors.push("periodic-table.html: periodic-trends placeholder must preserve qualified scientific direction statements");
}
if (!fs.existsSync(path.join(root, "periodic-table.html"))) errors.push("periodic-table.html: interactive periodic table visual is missing");

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

const constantsSource = fs.readFileSync(path.join(root, "chemistry-constants.html"), "utf8");
for (const [label, evidence] of [
  ["Avogadro constant", "6.022 140 76 × 10²³"],
  ["elementary charge", "1.602 176 634 × 10⁻¹⁹"],
  ["Planck constant", "6.626 070 15 × 10⁻³⁴"],
  ["Boltzmann constant", "1.380 649 × 10⁻²³"],
  ["speed of light", "299 792 458"],
  ["Faraday constant", "≈ 96 485.33"],
  ["molar gas constant", "8.314 462 618…"],
  ["standard pressure conversion", "1 bar = 100 kPa"],
  ["standard atmosphere conversion", "1 atm = 101.325 kPa"],
  ["IUPAC standard gas conditions", "273.15 K"],
  ["Russian standard pressure distinction", "Стандартное давление по рекомендации IUPAC — 100 kPa (1 bar)"],
  ["English standard pressure distinction", "IUPAC standard pressure is 100 kPa (1 bar)"],
  ["Russian standard gas conditions definition", "Для стандартных условий газов IUPAC указывает 273.15 K и 100 kPa"],
  ["English standard gas conditions definition", "For standard conditions for gases, IUPAC specifies 273.15 K and 100 kPa"],
  ["separate thermodynamic reference temperature", "The temperature for tabulated thermodynamic data is stated separately"]
]) {
  if (!constantsSource.includes(evidence)) errors.push("chemistry-constants.html: missing or changed " + label);
}
for (const [label, url] of [
  ["NIST/CODATA constants source", "https://physics.nist.gov/cuu/Constants/"],
  ["IUPAC standard pressure source", "https://goldbook.iupac.org/terms/view/S05921"],
  ["IUPAC standard gas conditions source", "https://goldbook.iupac.org/terms/view/S05910"],
  ["IUPAC standard thermodynamic quantities source", "https://goldbook.iupac.org/terms/view/S05927"],
  ["IUPAC water autoprotolysis source", "https://goldbook.iupac.org/terms/view/A00532"]
]) {
  if (!constantsSource.includes(url)) errors.push("chemistry-constants.html: missing authoritative reference link for " + label);
}
for (const [label, evidence] of [
  ["Russian source notes", "Источники и методические примечания"],
  ["English source notes", "Sources and methodological notes"],
  ["Russian temperature qualification", "Величины при 25 °C не следует автоматически переносить"],
  ["English temperature qualification", "Values at 25 °C must not automatically be applied"]
]) {
  if (!constantsSource.includes(evidence)) errors.push("chemistry-constants.html: missing " + label);
}

const homepage = fs.readFileSync(path.join(root, "index.html"), "utf8");
const chapterIds = [...homepage.matchAll(/["'](0[1-9]|1[0-2])["']/g)].map(m => m[1]);
if (new Set(chapterIds).size < 12) errors.push("index.html: expected all 12 chapter identifiers");


const feedbackTemplatePath = path.join(root, "FEEDBACK_WIDGET_TEMPLATE.html");
const feedbackTemplate = fs.existsSync(feedbackTemplatePath) ? fs.readFileSync(feedbackTemplatePath, "utf8") : "";
if (!feedbackTemplate) {
  errors.push("FEEDBACK_WIDGET_TEMPLATE.html: disabled feedback template is missing");
} else {
  if (!/<form\b[^>]*id=["']chemistry-feedback-form["']/i.test(feedbackTemplate)) {
    errors.push("FEEDBACK_WIDGET_TEMPLATE.html: chemistry feedback form is missing");
  }
  if (!/<button\b[^>]*type=["']button["'][^>]*disabled/i.test(feedbackTemplate)) {
    errors.push("FEEDBACK_WIDGET_TEMPLATE.html: submission control must remain disabled");
  }
  if (/\b(?:action|formaction)\s*=/i.test(feedbackTemplate) ||
      /\b(?:fetch|XMLHttpRequest|sendBeacon)\s*\(/i.test(feedbackTemplate) ||
      /\b(?:localStorage|sessionStorage|indexedDB)\b/i.test(feedbackTemplate) ||
      /addEventListener\s*\(\s*["']submit["']/i.test(feedbackTemplate)) {
    errors.push("FEEDBACK_WIDGET_TEMPLATE.html: submission, network or browser storage logic must not be present before approval");
  }
  if (!/ответы не отправляются и не сохраняются/i.test(feedbackTemplate) ||
      !/responses are not submitted or stored/i.test(feedbackTemplate)) {
    errors.push("FEEDBACK_WIDGET_TEMPLATE.html: bilingual non-submission notice is required");
  }
  const ratings = [...feedbackTemplate.matchAll(/name=["']rating_[^"']+["']/g)];
  if (ratings.length !== 9 || (feedbackTemplate.match(/value=["']na["']/g) || []).length !== 9) {
    errors.push("FEEDBACK_WIDGET_TEMPLATE.html: all nine evaluation criteria need a Cannot assess option");
  }
  if (!feedbackTemplate.includes("Критическая ошибка / Critical error") ||
      !feedbackTemplate.includes("Согласен(на) на публикацию текста отзыва") ||
      !feedbackTemplate.includes("Не согласен(на) / I do not consent")) {
    errors.push("FEEDBACK_WIDGET_TEMPLATE.html: priority and explicit optional publication consent fields are required");
  }
}


const canonicalImagePolicyUrl = "https://github.com/Ajokendo/Atlas-of-Knowledge/blob/atlas-of-knowledge-integration/IMAGE_FIRST_POLICY.md";
if (!imageSources.includes(canonicalImagePolicyUrl) || !imageAudit.includes(canonicalImagePolicyUrl)) {
  errors.push("IMAGE-FIRST POLICY: both Chemistry visual records must link to the canonical root policy");
}
if (!imageSources.includes("## Learning purpose and retrospective search record") ||
    !imageSources.includes("| Learning purpose |") ||
    !imageSources.includes("| Search date and outcome |")) {
  errors.push("IMAGE_SOURCES.md: canonical-policy learning-purpose and search-evidence fields are missing");
}
const imageSearchRegister = imageSources.split("## Learning purpose and retrospective search record")[1] || "";
for (const id of ["CH-V01","CH-V02","CH-V03","CH-V04","CH-V05","CH-V06","CH-V07","CH-V08","CH-V09","CH-V10","CH-V11","CH-IV01","CH-IV02","CH-IV03","CH-IV04"]) {
  const lines = imageSearchRegister.split(/\r?\n/).filter(line => line.startsWith("| " + id + " |"));
  if (lines.length !== 1) errors.push("IMAGE_SOURCES.md: expected exactly one learning-purpose/search record for " + id);
  else if (!lines[0].includes("2026-11-05")) errors.push("IMAGE_SOURCES.md: dated search record is missing for " + id);
}
if (!imageAudit.includes("## Chapter-level learning-need sign-off")) {
  errors.push("IMAGE_AUDIT.md: chapter-level learning-need sign-off is missing");
}

const periodicTablePath = path.join(root, "periodic-table.html");
if (fs.existsSync(periodicTablePath)) {
  const periodicTableSource = fs.readFileSync(periodicTablePath, "utf8");
  if (!periodicTableSource.includes(`aria-label="'+e.n+' '+name(e)+' ('+e.sym+'), '+e.mass+' u"`)) {
    errors.push("periodic-table.html: element buttons need an accessible name with atomic number, localized name, symbol and mass");
  }
  if (!periodicTableSource.includes('id="detail" aria-live="polite"')) {
    errors.push("periodic-table.html: selected-element details must be announced through a polite live region");
  }
  if (!periodicTableSource.includes('id="detail" aria-live="polite" aria-atomic="true"')) {
    errors.push("periodic-table.html: selected-element live region must announce the complete updated detail");
  }
  if (!periodicTableSource.includes('button.classList.toggle("selected",active)') ||
      !periodicTableSource.includes('button.setAttribute("aria-pressed",String(active))')) {
    errors.push("periodic-table.html: selection must update in place so keyboard focus is not lost when an element is activated");
  }
} else {
  errors.push("periodic-table.html: interactive periodic table is missing");
}

const atomicStructurePath = path.join(root, "chapters", "atomic-structure.html");
if (fs.existsSync(atomicStructurePath)) {
  const atomicStructureSource = fs.readFileSync(atomicStructurePath, "utf8");
  if (!/<img\b[^>]*id=["']electronCloud["'][^>]*data-svg-ru=["'][^"']+["'][^>]*data-svg-en=["'][^"']+["'][^>]*alt=["'][^"']+["']/i.test(atomicStructureSource)) {
    errors.push("chapters/atomic-structure.html: electron probability cloud needs bilingual SVG paths and non-empty alternative text");
  }
  if (!atomicStructureSource.includes("electronCloudAlt:") ||
      !atomicStructureSource.includes('$("electronCloud").alt=t[lang].electronCloudAlt') ||
      !atomicStructureSource.includes('$("electronCloud").src=lang==="ru"')) {
    errors.push("chapters/atomic-structure.html: electron cloud alt text and source must switch with the page language");
  }
  for (const [key, ru, en] of [["particleProton", "Протон", "Proton"], ["particleNeutron", "Нейтрон", "Neutron"], ["particleElectron", "Электрон", "Electron"]]) {
    if (!atomicStructureSource.includes(key + ':"'+ru+'"') || !atomicStructureSource.includes(key + ':"'+en+'"') ||
        !atomicStructureSource.includes('data-t="'+key+'"')) {
      errors.push("chapters/atomic-structure.html: particle SVG label must be bilingual and switch with the page language: " + key);
    }
  }
  for (const asset of ["electron-cloud-ru.svg","electron-cloud.svg"]) {
    if (!fs.existsSync(path.join(assetRoot, asset))) errors.push("chapters/atomic-structure.html: missing electron-cloud language asset " + asset);
  }
} else {
  errors.push("chapters/atomic-structure.html: atomic structure chapter is missing");
}

if (errors.length) {
  console.error("Chemistry atlas checks failed:");
  for (const error of errors) console.error(" - " + error);
  process.exit(1);
}
console.log("Chemistry atlas checks passed: " + htmlFiles.length + " HTML pages, " + checkedLinks + " local links/assets, " + checkedScripts + " inline scripts.");
console.log("Bilingual dictionaries checked: " + checkedBilingualPages + " pages.");
