import { chromium } from "playwright";
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage();
  const response = await page.goto("http://127.0.0.1:4173/biology/images/generated/flora-jalalabad.webp", { waitUntil: "load" });
  if (!response?.ok()) throw new Error("Generated Arslanbob WebP did not load");
  const result = await page.evaluate(async () => {
    const image = new Image();
    image.src = location.href;
    await image.decode();
    return { width: image.naturalWidth, height: image.naturalHeight, complete: image.complete };
  });
  if (!result.complete || result.width !== 3888 || result.height !== 2592) {
    throw new Error("Unexpected WebP decode result: " + JSON.stringify(result));
  }
  console.log("PASS Arslanbob WebP decode", JSON.stringify(result));
} finally {
  await browser.close();
}
