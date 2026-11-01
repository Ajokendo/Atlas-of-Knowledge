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

function plainText(markup) {
  return markup
    .replace(/<[^>]*>/g, "")
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

  const localizedKeys = [...new Set([...source.matchAll(/data-i=["']([^"']+)["']/g)].map(match => match[1]))];
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
