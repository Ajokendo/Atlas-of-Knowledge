import { chromium } from "playwright";
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1365, height: 900 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const response = await page.goto("http://127.0.0.1:4173/biology/chapters/flora-kyrgyzstan.html", { waitUntil: "networkidle" });
  if (!response?.ok()) throw new Error("Flora chapter HTTP response was not successful");
  const figure = page.locator('figure#image-brief-flora-issyk');
  if (await figure.count() !== 1) throw new Error("Expected one Issyk-Kul flora figure at the original insertion anchor");
  const expected = [
    ["flora-issyk-wetland.webp", 2048, 1536, "E8288-Tamchy-Bay-wetland.jpg"],
    ["flora-issyk-dry-foothills.webp", 2048, 1536, "E8221-Tamchy-dry-gulch.jpg"],
    ["flora-issyk-sea-buckthorn.webp", 2560, 1920, "E8306-Kosh-Kol-sea-buckthorn.jpg"],
    ["flora-issyk-karakol-spruce.webp", 3072, 2304, "Karakol_Valley.jpg"],
  ];
  const images = figure.locator("img");
  if (await images.count() !== expected.length) throw new Error("Expected four separate habitat photographs");
  for (let i = 0; i < expected.length; i++) {
    const [filename, width, height, sourceFile] = expected[i];
    const img = images.nth(i);
    await img.evaluate(el => { el.loading = "eager"; el.scrollIntoView(); });
    await img.evaluate(el => el.decode());
    const state = await img.evaluate(el => ({
      src: el.getAttribute("src"), width: el.naturalWidth, height: el.naturalHeight,
      alt: el.alt, visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length),
      caption: el.parentElement?.innerText || "",
      source: !!el.parentElement?.querySelector('a[href*="' + "commons.wikimedia.org/wiki/File:" + '"]'),
    }));
    if (!state.src?.endsWith(filename) || state.width !== width || state.height !== height ||
        !state.alt.includes("/") || !state.visible || !state.caption.includes(sourceFile) ||
        !state.source || !state.caption.includes("CC BY")) {
      throw new Error("Issyk-Kul image failed browser validation: " + JSON.stringify(state));
    }
  }
  if (errors.length) throw new Error("Browser page errors: " + errors.join("; "));
  console.log("PASS Issyk-Kul flora integration: four locally decoded images at the original bilingual anchor");
} finally {
  await browser.close();
}
