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
  if (!Number.isInteger(ref.page) || ref.page < 0) {
    errors.push("Invalid cross-reference page index: " + ref.chapter + "/" + ref.page);
    continue;
  }
  const pagesPath = root + "/" + ref.chapter + "/pages.js";
  const pageSource = readFileSync(pagesPath, "utf8");
  const pageCount = [...pageSource.matchAll(/\bkicker:\s*['"`]/g)].length;
  if (ref.page >= pageCount) {
    errors.push("Cross-reference page is out of range: " + ref.chapter + "/" + ref.page + " (page count " + pageCount + ")");
  }
}

const app = readFileSync("app.js", "utf8");
const chapterPages = {
  kinematics: "chapters/kinematics.html", newton: "chapters/newton-laws.html",
  circular: "chapters/circular-motion.html", energy: "chapters/work-energy.html",
  momentum: "chapters/momentum.html", oscillations: "chapters/oscillations.html",
  rotation: "chapters/rotation.html", fluids: "chapters/fluids.html",
  electrostatics: "chapters/electrostatics.html", gauss: "chapters/gauss-law.html",
  potential: "chapters/electric-potential.html", capacitors: "chapters/capacitors.html",
  circuits: "chapters/circuits.html", magnetism: "chapters/magnetism.html",
  induction: "chapters/induction.html",
};
for (const chapter of chapters) {
  if (!app.includes("original-engine/" + chapter + "/index.html")) {
    errors.push("Main catalog does not link to the " + chapter + " laboratory");
  }
  if (!app.includes(chapterPages[chapter])) {
    errors.push("Main catalog does not link to the " + chapter + " theory chapter");
  }
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode = 1;
} else {
  console.log("Checked " + checked + " required lab resources and " + refs.length + " cross-reference endpoints across " + chapters.length + " laboratories.");
}
