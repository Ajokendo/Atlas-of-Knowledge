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
    if (!/^(?:\d+(?:\.\d+)?|\[\d+\]|\d+(?:\.\d+)?[–-]\d+(?:\.\d+)?)$/.test(row[4] || "")) errors.push("periodic-table.html: invalid atomic-mass, interval or mass-number notation for record " + (i + 1));
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
const staticAssetRegister = imageSources.split("## Asset register")[1]?.split("## Non-file interactive visuals")[0] || "";
const provenanceMapping = imageSources.split("## Retrospective provenance and Category C mapping")[1] || "";
if (!provenanceMapping.includes("The current 24 files form 12 bilingual visual families")) {
  errors.push("IMAGE_SOURCES.md: current file-level provenance mapping for all 12 bilingual SVG families is missing");
}
if (!imageSources.includes("rights fields remain **PENDING**") ||
    !imageSources.includes("rightsholder, licensing authority and licence not established")) {
  errors.push("IMAGE_SOURCES.md: Category C classification must not be treated as automatic rights clearance");
}
for (const id of ["CH-V01","CH-V02","CH-V03","CH-V04","CH-V05","CH-V06","CH-V07","CH-V08","CH-V09","CH-V10","CH-V11","CH-V12"]) {
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
  ["Russian dilute ideal-solution assumption", "разбавленные идеальные растворы"],
  ["English dilute ideal-solution assumption", "dilute ideal solutions"],
  ["Russian additive-volume assumption", "аддитивность объёмов"],
  ["English additive-volume assumption", "additive volumes"],
  ["Russian activity limitation", "активности ионов"],
  ["English activity limitation", "ion activities"]
]) {
  if (!virtualLabPage.includes(evidence)) errors.push("virtual-lab.html: missing model-scope qualification: " + label);
}

if (!virtualLabPage.includes('id="beakerWrap" role="img" aria-label="Виртуальный сосуд') ||
    !virtualLabPage.includes('setAttribute("aria-label",t.beakerVisualAlt)')) {
  errors.push("virtual-lab.html: beaker visual needs a bilingual accessible name linked to dynamic text");
}

const gasLawsPage = fs.readFileSync(path.join(root, "gas-laws.html"), "utf8");
if (!gasLawsPage.includes('particleNote:"Визуализация показывает только условное число частиц') ||
    !gasLawsPage.includes('id="particleVisual" role="img" aria-label="Схема условного числа частиц') ||
    !gasLawsPage.includes('setAttribute("aria-label",w.particleVisualAlt)') ||
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
for (const key of ["trendTitle", "trendBody", "trendEyebrow", "trendCaption"]) {
  if (!periodicPage.includes(key + ':"') || !periodicPage.includes('data-t="' + key + '"')) {
    errors.push("periodic-table.html: Chapter 03 periodic-trends visual must be bilingual: " + key);
  }
}
if (!periodicPage.includes("atomic radius generally increases down and to the left") ||
    !periodicPage.includes("first ionisation energy and electronegativity generally increase up and to the right") ||
    !periodicPage.includes("not exception-free rules") || !periodicPage.includes("electron configuration")) {
  errors.push("periodic-table.html: periodic-trends alt text must preserve qualified scientific direction statements");
}
if (!fs.existsSync(path.join(root, "periodic-table.html"))) errors.push("periodic-table.html: interactive periodic table visual is missing");

const isotopeSvgPath = path.join(assetRoot, "isotope-abundance.svg");
if (fs.existsSync(isotopeSvgPath)) {
  const isotopeSvg = fs.readFileSync(isotopeSvgPath, "utf8");
  for (const [x, expectedNeutrons] of [[205, 6], [470, 7]]) {
    const start = isotopeSvg.indexOf('<g transform="translate(' + x + ' 185)">');
    const end = start < 0 ? -1 : isotopeSvg.indexOf("</text></g>", start);
    const nucleus = start < 0 || end < 0 ? "" : isotopeSvg.slice(start, end);
    const protons = (nucleus.match(/fill="#238b70"/g) || []).length;
    const neutrons = (nucleus.match(/fill="#e0a64d"/g) || []).length;
    if (protons !== 6 || neutrons !== expectedNeutrons) {
      errors.push("assets/isotope-abundance.svg: expected 6 protons and " + expectedNeutrons + " neutrons in nucleus at x=" + x);
    }
  }
}
const isotopeSvgRuPath = path.join(assetRoot, "isotope-abundance-ru.svg");
if (fs.existsSync(isotopeSvgRuPath)) {
  const isotopeSvgRu = fs.readFileSync(isotopeSvgRuPath, "utf8");
  for (const [x, expectedNeutrons] of [[205, 6], [470, 7]]) {
    const start = isotopeSvgRu.indexOf('<g transform="translate(' + x + ' 185)">');
    const end = start < 0 ? -1 : isotopeSvgRu.indexOf("</text></g>", start);
    const nucleus = start < 0 || end < 0 ? "" : isotopeSvgRu.slice(start, end);
    const protons = (nucleus.match(/fill="#238b70"/g) || []).length;
    const neutrons = (nucleus.match(/fill="#e0a64d"/g) || []).length;
    if (protons !== 6 || neutrons !== expectedNeutrons) {
      errors.push("assets/isotope-abundance-ru.svg: expected 6 protons and " + expectedNeutrons + " neutrons in nucleus at x=" + x);
    }
  }
  for (const phrase of ["≈ 98,9%", "≈ 1,1%", "0,989 × 12 +", "0,011 × 13", "≈ 12,011"]) {
    if (!isotopeSvgRu.includes(phrase)) errors.push("assets/isotope-abundance-ru.svg: missing bilingual isotope data or weighted-mean detail: " + phrase);
  }
}
if (fs.existsSync(isotopeSvgPath)) {
  const isotopeSvg = fs.readFileSync(isotopeSvgPath, "utf8");
  for (const phrase of ["98.9% natural abundance", "1.1% natural abundance", "0.989 × 12 + 0.011 × 13 ≈ 12.011 u"]) {
    if (!isotopeSvg.includes(phrase)) errors.push("assets/isotope-abundance.svg: missing English isotope data or weighted-mean detail: " + phrase);
  }
}
for (const [file, phrases] of [
  ["one-mole-scale.svg", ["6.02214076 times 10 to the 23", "seven dots shown are illustrative symbols only", "not a literal particle count"]],
  ["one-mole-scale-ru.svg", ["6,022 140 76 × 10²³", "Семь точек на рисунке — условные символы", "не буквальное число частиц"]]
]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) {
    errors.push("CH-V03: missing mole visual " + file);
    continue;
  }
  const svg = fs.readFileSync(fullPath, "utf8");
  for (const phrase of phrases) {
    if (!svg.includes(phrase)) errors.push("CH-V03: " + file + " must clarify exact Avogadro count and illustrative particle symbols");
  }
}
for (const [file, required] of [
  ["formula-reading.svg", ["Al₂(SO₄)₃", "2 × (2 H + 1 O)", "4 H atoms + 2 O atoms", "Coefficient ≠ subscript"]],
  ["formula-reading-ru.svg", ["Al₂(SO₄)₃", "2H₂O", "4 атома H + 2 атома O", "Коэффициент и индекс"]]
]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) {
    errors.push("CH-V04: missing formula-reading visual " + file);
    continue;
  }
  const svg = fs.readFileSync(fullPath, "utf8");
  for (const phrase of required) {
    if (!svg.includes(phrase)) errors.push("CH-V04: " + file + " is missing the bilingual formula/coefficient explanation: " + phrase);
  }
}
for (const [file, required] of [
  ["solution-saturation-particles.svg", ["same temperature and amount of solvent", "dynamic equilibrium with undissolved solute", "metastable", "crystallise when seeded", "Dynamic equilibrium with solid"]],
  ["solution-saturation-particles-ru.svg", ["при одинаковой температуре и количестве растворителя", "в равновесии с нерастворённым веществом", "метастабилен", "после внесения затравки", "Динамическое равновесие"]]
]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) {
    errors.push("CH-V05: missing saturation-state visual " + file);
    continue;
  }
  const svg = fs.readFileSync(fullPath, "utf8");
  for (const phrase of required) {
    if (!svg.toLowerCase().includes(phrase.toLowerCase())) errors.push("CH-V05: " + file + " is missing scientific state distinction: " + phrase);
  }
}
for (const [file, required] of [
  ["acid-base-neutralisation.svg", ["Brønsted–Lowry model", "Acid: proton donor", "Base: proton acceptor", "Base added →", "equivalence point near pH 7"]],
  ["acid-base-neutralisation-ru.svg", ["Модель Бренстеда — Лоури", "Кислота: донор протона", "Основание: акцептор протона", "Добавление основания", "около pH 7"]]
]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) {
    errors.push("CH-V06: missing neutralisation visual " + file);
    continue;
  }
  const svg = fs.readFileSync(fullPath, "utf8");
  for (const phrase of required) {
    if (!svg.toLowerCase().includes(phrase.toLowerCase())) errors.push("CH-V06: " + file + " is missing the bilingual acid-base/titration explanation: " + phrase);
  }
}
const acidBaseChapterPath = path.join(root, "chapters", "acids-and-bases.html");
if (fs.existsSync(acidBaseChapterPath)) {
  const acidBaseChapter = fs.readFileSync(acidBaseChapterPath, "utf8");
  for (const required of [
    'class="neutralisation-mobile"',
    'data-i="mobileDiagramTitle"',
    'data-i="mobileCurveTitle"',
    'data-i="mobileQualification"',
    'mobileDiagramAlt:',
    '.chemistry-illustration>img{display:none!important}',
    '.neutralisation-mobile{display:grid;gap:10px}',
    'setAttribute("aria-label",copy[lang].mobileDiagramAlt)'
  ]) {
    if (!acidBaseChapter.includes(required)) errors.push("chapters/acids-and-bases.html: responsive bilingual mobile neutralisation diagram is incomplete: " + required);
  }
} else {
  errors.push("chapters/acids-and-bases.html: responsive acid-base chapter is missing");
}

const neutralisationSvgPath = path.join(assetRoot, "acid-base-neutralisation.svg");
if (fs.existsSync(neutralisationSvgPath)) {
  const neutralisationSvg = fs.readFileSync(neutralisationSvgPath, "utf8");
  if (!/d="M20 132 C90 132 120 130 145 112 C160 100 164 75 185 75 C206 75 210 50 225 35 C250 18 300 20 350 20"/.test(neutralisationSvg)) {
    errors.push("assets/acid-base-neutralisation.svg: expected rising curve crossing pH 7 at the equivalence marker (x=185, y=75)");
  }
}


for (const [file, required] of [
  ["reaction-schematic.svg", ["M112 150L168 150M224 150L224 100", "M650 150L650 100M762 150L706 150", "atoms are conserved"]],
  ["reaction-schematic-ru.svg", ["M112 150L168 150M224 150L224 100", "M650 150L650 100M762 150L706 150", "атомы сохраняются"]]
]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) { errors.push("CH-V07: missing reaction schematic " + file); continue; }
  const svg = fs.readFileSync(fullPath, "utf8");
  for (const phrase of required) if (!svg.toLowerCase().includes(phrase.toLowerCase())) {
    errors.push("CH-V07: " + file + " must show conserved atoms and changed bond connectivity: " + phrase);
  }
  if (/M168 150L224 150|M762 150L762 100/.test(svg)) {
    errors.push("CH-V07: " + file + " still contains the old misleading bond topology");
  }
}
for (const file of ["biomolecule-overview.svg", "biomolecule-overview-ru.svg"]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) { errors.push("CH-V10: missing biomolecule overview " + file); continue; }
  const svg = fs.readFileSync(fullPath, "utf8");
  if (!svg.includes("M100 330 V390 M130 330 V390") ||
      svg.includes("M95 330 V390 M115 330 V390 M135 330 V390")) {
    errors.push("CH-V10: " + file + " must depict a phospholipid with two hydrocarbon tails, not three");
  }
}
const functionalGroupsEn = fs.readFileSync(path.join(assetRoot, "organic-functional-groups.svg"), "utf8");
for (const phrase of ["carbon–carbon double bond", "hydroxyl group", "carboxyl group", "amino group", "aromatic ring"]) {
  if (!functionalGroupsEn.includes(phrase)) errors.push("CH-V09: English functional-group visual is missing explanatory label: " + phrase);
}
const carbonCycleRu = fs.readFileSync(path.join(assetRoot, "carbon-cycle-ru.svg"), "utf8");
if (!carbonCycleRu.includes("M560 430 V185") ||
    !carbonCycleRu.includes("Вулканический возврат CO₂")) {
  errors.push("CH-V11: Russian carbon-cycle visual must show the geological-to-atmosphere volcanic carbon return");
}
for (const [file, required] of [
  ["periodic-trends.svg", ["atomic radius generally increases down and to the left", "first ionisation energy", "electronegativity", "not exception-free rules", "noble gases"]],
  ["periodic-trends-ru.svg", ["атомный радиус обычно увеличивается вниз и влево", "Энергия первой ионизации", "Электроотрицательность", "Есть исключения", "благородных газов"]]
]) {
  const fullPath = path.join(assetRoot, file);
  if (!fs.existsSync(fullPath)) { errors.push("CH-V12: missing periodic-trends visual " + file); continue; }
  const svg = fs.readFileSync(fullPath, "utf8");
  for (const phrase of required) if (!svg.toLowerCase().includes(phrase.toLowerCase())) {
    errors.push("CH-V12: " + file + " is missing a qualified periodic-trend statement: " + phrase);
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


const canonicalImagePolicyUrl = "https://github.com/Ajokendo/Atlas-of-Knowledge/blob/main/IMAGE_FIRST_POLICY.md";
if (!imageSources.includes(canonicalImagePolicyUrl) || !imageAudit.includes(canonicalImagePolicyUrl)) {
  errors.push("IMAGE-FIRST POLICY: both Chemistry visual records must link to the canonical root policy");
}
if (!imageSources.includes("## Learning purpose and retrospective search record") ||
    !imageSources.includes("| Learning purpose |") ||
    !imageSources.includes("| Search date and outcome |")) {
  errors.push("IMAGE_SOURCES.md: canonical-policy learning-purpose and search-evidence fields are missing");
}
const imageSearchRegister = (imageSources.split("## Learning purpose and retrospective search record")[1] || "").split("## Targeted follow-up search outcomes")[0];
for (const id of ["CH-V01","CH-V02","CH-V03","CH-V04","CH-V05","CH-V06","CH-V07","CH-V08","CH-V09","CH-V10","CH-V11","CH-IV01","CH-IV02","CH-IV03","CH-IV04","CH-IV05","CH-IV06","CH-IV07","CH-V12"]) {
  const lines = imageSearchRegister.split(/\r?\n/).filter(line => line.startsWith("| " + id + " |"));
  if (lines.length !== 1) errors.push("IMAGE_SOURCES.md: expected exactly one learning-purpose/search record for " + id);
  else if (!lines[0].includes("2026-11-05")) errors.push("IMAGE_SOURCES.md: dated search record is missing for " + id);
}


if (!imageSources.includes("IMAGE-FIRST POLICY v1.2") ||
    !imageAudit.includes("IMAGE-FIRST POLICY v1.2") ||
    !imageSources.includes("## IMAGE-FIRST POLICY v1.1 — per-ID metadata completeness supplement") ||
    !imageSources.includes("### Derivative / inherited-atlas protocol") ||
    !imageSources.includes("Not applicable at atlas level")) {
  errors.push("IMAGE-FIRST POLICY v1.2: Chemistry source register must expose current policy version, required metadata and derivative-atlas applicability");
}

const periodicTrendCandidate = imageSources.split("## Chapter 03 image-first candidate review — found, not adopted")[1]?.split("## Non-file interactive visuals")[0] || "";
for (const [label, evidence] of [
  ["English Commons source page", "https://commons.wikimedia.org/wiki/File:Periodic_trends.svg"],
  ["English direct SVG", "https://upload.wikimedia.org/wikipedia/commons/f/fe/Periodic_trends.svg"],
  ["English CC0 licence", "https://creativecommons.org/publicdomain/zero/1.0/"],
  ["English creator", "Mirek2"],
  ["Russian Commons source page", "https://commons.wikimedia.org/wiki/File:Periodic_trends-rus.svg"],
  ["Russian direct SVG", "https://upload.wikimedia.org/wikipedia/commons/e/e8/Periodic_trends-rus.svg"],
  ["Russian CC BY-SA licence", "https://creativecommons.org/licenses/by-sa/4.0/"],
  ["Russian creator", "Донор"],
  ["candidate considered but not adopted", "FOUND — item-specific licence and creator record checked"]
]) {
  if (!periodicTrendCandidate.includes(evidence)) errors.push("IMAGE_SOURCES.md: Chapter 03 periodic-trends candidate missing " + label);
}
if (!imageAudit.includes("## Latest visual checkpoint — 2026-11-05 (after CH-V12 integration)") ||
    !imageAudit.includes("12 / 12 = 100%") ||
    !imageAudit.includes("0 / 19 = 0% VERIFIED") ||
    !imageAudit.includes("19 / 19 = 100%") ||
    !imageAudit.includes("7 / 7 integrated") ||
    !imageAudit.includes("14 PASS / 5 PENDING / 0 FAIL") ||
    !imageAudit.includes("## Interactive visual audit by ID") ||
    !imageAudit.includes("### Chapter-level visual metrics") ||
    !imageAudit.includes("Chapter 03 — periodic system: updated visual status")) {
  errors.push("IMAGE_AUDIT.md: current policy metrics or per-ID interactive visual audit is missing");
}

if (!imageAudit.includes("## Chapter-level learning-need sign-off")) {
  errors.push("IMAGE_AUDIT.md: chapter-level learning-need sign-off is missing");
}


if (!imageSources.includes("## Targeted follow-up search outcomes — 2026-11-05") ||
    !imageSources.includes("CH-V09") ||
    !imageSources.includes("NASA SVS item 10494") ||
    !imageSources.includes("CH-IV02")) {
  errors.push("IMAGE_SOURCES.md: targeted image-first search outcomes are incomplete");
}
if (!imageAudit.includes("10 FOUND / 19 searched") ||
    !imageAudit.includes("19 / 19 = 100%") ||
    !imageAudit.includes("0 identified in current plan")) {
  errors.push("IMAGE_AUDIT.md: current search and coverage metrics are inconsistent or missing");
}


const captionAtomic = fs.readFileSync(path.join(root, 'chapters', 'atomic-structure.html'), 'utf8');
const captionReactions = fs.readFileSync(path.join(root, 'chapters', 'chemical-reactions.html'), 'utf8');
const captionLife = fs.readFileSync(path.join(root, 'chapters', 'chemistry-of-life.html'), 'utf8');
const captionHome = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
if (!captionAtomic.includes('id="electronCloudCaption" class="caption" data-t="electronCloudCaption"') ||
    !captionReactions.includes('data-i="reactionImageCaption"') ||
    !captionReactions.includes('"reactionImageCaption":"Schematic atom rearrangement:') ||
    !captionLife.includes('data-i="carbonCycleCaption"') ||
    !captionHome.includes('data-i18n="heroImageCaption"') ||
    !captionHome.includes('heroImageCaption:"Schematic probability cloud')) {
  errors.push('IMAGE-FIRST: meaningful static and hero visuals need bilingual learner-facing captions');
}

const periodicTablePath = path.join(root, "periodic-table.html");
if (fs.existsSync(periodicTablePath)) {
  const periodicTableSource = fs.readFileSync(periodicTablePath, "utf8");
  if (periodicTableSource.includes("aria-label=\"'+e.n+' '+name(e)+' ('+e.sym+'), '+e.mass+' u\"") ||
      !periodicTableSource.includes("<strong class=\"sym\">'+e.sym+'</strong><span class=\"ename\">'+name(e)+'</span>")) {
    errors.push("periodic-table.html: visible atomic number, symbol, localized name and mass must provide the element button's accessible name without overriding visible text");
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


const periodicTrendEn = path.join(assetRoot, "periodic-trends.svg");
const periodicTrendRu = path.join(assetRoot, "periodic-trends-ru.svg");
if (!fs.existsSync(periodicTrendEn) || !fs.existsSync(periodicTrendRu)) {
  errors.push("CH-V12: bilingual periodic-trends SVG assets must both exist");
}
const periodicTrendPage = fs.readFileSync(periodicTablePath, "utf8");
for (const required of [
  'id="trendImage"',
  'data-svg-ru="assets/periodic-trends-ru.svg"',
  'data-svg-en="assets/periodic-trends.svg"',
  'data-alt-ru=',
  'data-alt-en=',
  '$("trendImage").alt=names[lang].trendAlt',
  '$("trendImage").src=lang==="ru"',
  'data-t="trendCaption"',
  'data-t="trendBody"'
]) {
  if (!periodicTrendPage.includes(required)) errors.push("CH-V12: periodic-table.html is missing " + required);
}
for (const [file, language] of [[periodicTrendEn,"en"],[periodicTrendRu,"ru"]]) {
  if (fs.existsSync(file)) {
    const svg = fs.readFileSync(file,"utf8");
    if (!svg.includes("<title") || !svg.includes("<desc") || !svg.includes("viewBox=") ||
        !svg.includes("atomic radius") && language==="en" ||
        !svg.includes("Атомный радиус") && language==="ru") {
      errors.push("CH-V12: SVG title, description, geometry or language-specific trend labels are missing in " + path.basename(file));
    }
  }
}
if (!imageSources.includes("CH-V12 | Chapter 03") ||
    !imageSources.includes("Category C") ||
    !imageAudit.includes("CH-V12 review record")) {
  errors.push("CH-V12: source register and audit must document category, method and review status");
}

const electronCloudEnPath = path.join(assetRoot, "electron-cloud.svg");
if (fs.existsSync(electronCloudEnPath)) {
  const electronCloudEn = fs.readFileSync(electronCloudEnPath, "utf8");
  const description = electronCloudEn.split("<desc")[1]?.split("</desc>")[0] || "";
  if (!/probability-density cloud/i.test(description) ||
      !/not electron trajectories/i.test(description) ||
      !/not to scale/i.test(description)) {
    errors.push("assets/electron-cloud.svg: English description must identify a probability cloud, reject trajectory/orbit interpretation and state scale limitation");
  }
  if (electronCloudEn.includes('<g fill="none" stroke="#6f9e92"')) {
    errors.push("assets/electron-cloud.svg: remove orbit-like elliptical path outlines from the probability-cloud illustration");
  }
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


// CH-IV04: validate the periodic-table dataset as a complete, internally consistent 118-element sequence.
const periodicTableDataPath = path.join(root, "periodic-table.html");
if (fs.existsSync(periodicTableDataPath)) {
  const periodicSource = fs.readFileSync(periodicTableDataPath, "utf8");
  const rawMatch = periodicSource.match(/const raw=\x60([\s\S]*?)\x60\.trim\(\);/);
  if (!rawMatch) {
    errors.push("periodic-table.html: embedded element dataset could not be parsed");
  } else {
    const rows = rawMatch[1].trim().split(/\r?\n/).map(line => line.split("|"));
    const symbols = new Set();
    const categories = new Set(["nonmetal","noble","alkali","alkaline","metalloid","halogen","transition","post","lanthanide","actinide"]);
    if (rows.length !== 118) errors.push("periodic-table.html: dataset must contain exactly 118 element records");
    rows.forEach((r, i) => {
      const [number, symbol, ruName, enName, mass, category, group, period] = r;
      if (+number !== i + 1) errors.push("periodic-table.html: atomic numbers must be consecutive at record " + (i + 1));
      if (!/^[A-Z][a-z]?$/.test(symbol || "") || symbols.has(symbol)) errors.push("periodic-table.html: invalid or duplicate element symbol at record " + (i + 1));
      symbols.add(symbol);
      if (!ruName || !enName) errors.push("periodic-table.html: bilingual element names missing for atomic number " + number);
      if (!/^(?:\d+(?:\.\d+)?|\[\d+\]|\d+(?:\.\d+)?[–-]\d+(?:\.\d+)?)$/.test(mass || "")) errors.push("periodic-table.html: invalid atomic-mass, interval or mass-number format for " + symbol);
      if (!categories.has(category)) errors.push("periodic-table.html: unknown element category for " + symbol);
      if (!Number.isInteger(+group) || +group < 1 || +group > 18 || !Number.isInteger(+period) || +period < 1 || +period > 7) errors.push("periodic-table.html: invalid group or period for " + symbol);
      if (["lanthanide","actinide"].includes(category) && ![6,7].includes(+period)) errors.push("periodic-table.html: f-block element assigned outside periods 6–7: " + symbol);
    });
    if (symbols.size !== rows.length) errors.push("periodic-table.html: element symbols are not unique");
  }
  for (const required of ['aria-live="polite" aria-atomic="true"', 'button.setAttribute("aria-pressed",String(active))', '$("search").setAttribute("aria-label",names[lang].searchLabel)']) {
    if (!periodicSource.includes(required)) errors.push("periodic-table.html: required accessible interaction pattern missing: " + required);
  }
} else {
  errors.push("periodic-table.html: interactive periodic table is missing");
}

// CH-IV05: the molecular canvas should not run a permanent animation-frame loop while idle.
const moleculeLabPath = path.join(root, "molecule-lab.html");
if (fs.existsSync(moleculeLabPath)) {
  const moleculeLabSource = fs.readFileSync(moleculeLabPath, "utf8");
  if (!moleculeLabSource.includes('function animate(time){if(!spinning)return;') &&
      !moleculeLabSource.includes('function animate(time){if(!spinning){lastFrame=0;return}')) {
    errors.push("molecule-lab.html: animation loop must stop scheduling frames while auto-rotation is off");
  }
  if (!moleculeLabSource.includes('if(spinning){lastFrame=0;requestAnimationFrame(animate)}') ||
      moleculeLabSource.includes('render();requestAnimationFrame(animate);')) {
    errors.push("molecule-lab.html: animation frames should start only when the learner enables auto-rotation");
  }
} else {
  errors.push("molecule-lab.html: molecular geometry interactive is missing");
}


 // CH-IV06: guard the ideal-gas calculation's units, Kelvin conversion and learner input domain.
const gasLawPath = path.join(root, "gas-laws.html");
if (fs.existsSync(gasLawPath)) {
  const gasSource = fs.readFileSync(gasLawPath, "utf8");
  for (const required of [
    'min="-100" max="300"',
    'min=".1" max="3"',
    'min="5" max="60"',
    'const $=id=>document.getElementById(id);let lang="ru";',
    'k=c+273.15',
    'p=n*8.314462618*k/v',
    'p.toFixed(2)',
    'kPa·L·mol⁻¹·K⁻¹',
    'кПа·л·моль⁻¹·К⁻¹'
  ]) {
    if (!gasSource.includes(required)) errors.push("gas-laws.html: ideal-gas calculation or stated input/unit contract changed or is missing: " + required);
  }
  if (!gasSource.includes('id="particleNote"') ||
      !gasSource.includes('does not model density, speed, trajectories or collisions') ||
      !gasSource.includes('не моделирует плотность, скорость, траектории или столкновения')) {
    errors.push("gas-laws.html: schematic particle visual must retain its bilingual limitation note");
  }
} else {
  errors.push("gas-laws.html: ideal-gas interactive is missing");
}

// CH-IV07: guard the strong monoprotic-acid / monobasic-base model and its numerical edge handling.
const virtualLabPath = path.join(root, "virtual-lab.html");
if (fs.existsSync(virtualLabPath)) {
  const labSource = fs.readFileSync(virtualLabPath, "utf8");
  for (const required of [
    'ac>=.01&&ac<=2',
    'av>=10&&av<=500',
    'bc>=.01&&bc<=2',
    'bv>=0&&bv<=200',
    'acidMol=s.ac*s.av/1000',
    'baseMol=s.bc*s.bv/1000',
    'volume=(s.av+s.bv)/1000',
    'Math.hypot(excess,2e-7)',
    'if(diff>eps)p=-Math.log10(dominantIon)',
    'else if(diff< -eps)p=14+Math.log10(dominantIon)',
    'else p=7',
    '25 °C',
    'strong monoprotic acid'
  ]) {
    if (!labSource.includes(required)) errors.push("virtual-lab.html: neutralisation assumptions, input bounds or pH calculation guard missing: " + required);
  }
} else {
  errors.push("virtual-lab.html: acid-base neutralisation interactive is missing");
}

// Periodic-trend diagrams: arrows must remain in the right-hand lane, clear of bilingual labels.
for (const [file, oldPath] of [
  ["periodic-trends-ru.svg", "M 1040 204 L 900 278"],
  ["periodic-trends.svg", "M 1040 204 L 900 278"]
]) {
  const svgPath = path.join(root, "assets", file);
  if (!fs.existsSync(svgPath)) {
    errors.push("assets/" + file + ": periodic-trend visual is missing");
    continue;
  }
  const svg = fs.readFileSync(svgPath, "utf8");
  if (svg.includes(oldPath) ||
      (svg.match(/markerUnits="userSpaceOnUse"/g) || []).length !== 3 ||
      !svg.includes("M 1090 184 L 1055 244") ||
      !svg.includes("M 1055 374 L 1090 314") ||
      !svg.includes("M 1055 484 L 1090 424")) {
    errors.push("assets/" + file + ": trend arrows must stay in the right-hand lane and not cross labels");
  }
}

// Acid-base neutralisation figures: graph captions and model panel must be separate and visible in both languages.
const acidBaseDiagramRequirements = [
  ["acid-base-neutralisation-ru.svg", ["точка эквивалентности", "pH эквивалентности ≈ 7", "translate(550 260)", "Добавление основания"], ["y=\"435\""]],
  ["acid-base-neutralisation.svg", ["Idealised titration curve", "Brønsted–Lowry model", "Ideal model: equivalence pH ≈ 7.", "translate(550 260)", "Base added"], ["x=\"535\" y=\"430\""]]
];
for (const [file, required, forbidden] of acidBaseDiagramRequirements) {
  const diagramPath = path.join(root, "assets", file);
  if (!fs.existsSync(diagramPath)) {
    errors.push("assets/" + file + ": acid-base neutralisation visual is missing");
    continue;
  }
  const svg = fs.readFileSync(diagramPath, "utf8");
  for (const phrase of required) {
    if (!svg.includes(phrase)) errors.push("assets/" + file + ": required diagram label or model panel missing: " + phrase);
  }
  for (const phrase of forbidden) {
    if (svg.includes(phrase)) errors.push("assets/" + file + ": obsolete overlapping/off-canvas annotation remains: " + phrase);
  }
  if (!svg.includes("</g></svg>")) errors.push("assets/" + file + ": diagram groups must close before the SVG ends");
}

if (errors.length) {
  console.error("Chemistry atlas checks failed:");
  for (const error of errors) console.error(" - " + error);
  process.exit(1);
}
console.log("Chemistry atlas checks passed: " + htmlFiles.length + " HTML pages, " + checkedLinks + " local links/assets, " + checkedScripts + " inline scripts.");
console.log("Bilingual dictionaries checked: " + checkedBilingualPages + " pages.");
