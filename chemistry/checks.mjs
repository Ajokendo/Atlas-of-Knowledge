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
  const relative = path.relative(root, file).replace(/\\\\/g, "/");
  if (!/<svg\\b[^>]*\\bviewBox=/i.test(source)) errors.push(relative + ": SVG missing viewBox");
  if (!/<svg\\b[^>]*\\brole=["']img["']/i.test(source)) errors.push(relative + ": SVG missing role=img");
  if (!/<title\\b[^>]*>[\\s\\S]*?<\\/title>/i.test(source)) errors.push(relative + ": SVG missing accessible title");
  if (!/<desc\\b[^>]*>[\\s\\S]*?<\\/desc>/i.test(source)) errors.push(relative + ": SVG missing accessible description");
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
  if (!neutralisationSvg.includes('d="M20 132 C100 132 120 128 150 78 S190 25 210 22 S300 20 350 20"')) {
    errors.push("assets/acid-base-neutralisation.svg: expected rising pH curve when base is added");
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
