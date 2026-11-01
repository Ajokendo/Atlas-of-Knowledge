import { existsSync, readFileSync } from "node:fs";

const root = "original-engine";
const chapters = [
  "kinematics", "newton", "circular", "energy", "momentum",
  "oscillations", "rotation", "fluids", "electrostatics", "gauss",
  "potential", "capacitors", "circuits", "magnetism", "induction",
];
const requiredEngineFiles = [
  "engine/book.js", "engine/book.css", "engine/cover.js",
  "engine/parts.js", "engine/render.js", "engine/xrefs.js",
  "equations/index.html",
];
const requiredLabFiles = [
  "index.html", "main.js", "model.js", "pages.js",
  "practice.js", "world.js", "checks.mjs",
];
const errors = [];
let checked = 0;

function requireFile(path) {
  checked += 1;
  if (!existsSync(path)) errors.push("Missing required file: " + path);
}

for (const file of requiredEngineFiles) requireFile(root + "/" + file);
for (const chapter of chapters) {
  for (const file of requiredLabFiles) requireFile(root + "/" + chapter + "/" + file);
  const htmlPath = root + "/" + chapter + "/index.html";
  if (existsSync(htmlPath)) {
    const html = readFileSync(htmlPath, "utf8");
    for (const marker of [
      'href="../atlas.css"',
      'href="../engine/book.css"',
      'src="../engine/cover.js"',
      'src="main.js"',
    ]) {
      if (!html.includes(marker)) errors.push(htmlPath + ": missing expected resource reference " + marker);
    }
  }
}

const book = readFileSync(root + "/engine/book.js", "utf8");
if (!book.includes("from './xrefs.js'")) errors.push("engine/book.js does not import the cross-reference data");
if (!book.includes('href="../equations/"')) errors.push("engine/book.js does not expose the formula reference link");

const xrefsPath = root + "/engine/xrefs.js";
const xrefs = readFileSync(xrefsPath, "utf8");
const refs = [...xrefs.matchAll(/['"]([a-z-]+)\/(\d+)['"]/g)].map((match) => ({
  chapter: match[1],
  page: Number(match[2]),
}));
if (refs.length < 2 || refs.length % 2 !== 0) errors.push("Cross-reference table is empty or has an incomplete pair");
for (const ref of refs) {
  if (!chapters.includes(ref.chapter)) errors.push("Unknown cross-reference chapter: " + ref.chapter);
  requireFile(root + "/" + ref.chapter + "/index.html");
  if (!Number.isInteger(ref.page) || ref.page < 0) errors.push("Invalid cross-reference page index: " + ref.chapter + "/" + ref.page);
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode = 1;
} else {
  console.log("Checked " + checked + " required lab resources and " + refs.length + " cross-reference endpoints across " + chapters.length + " laboratories.");
}
