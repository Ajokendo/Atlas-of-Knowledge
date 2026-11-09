import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const file=pathToFileURL(resolve("/tmp/geography-chapter-03-preview.html")).href;
const browser=await chromium.launch({headless:true}),errors=[],results=[];
try{
 for(const viewport of [{width:390,height:844},{width:1365,height:900}]){
  const page=await browser.newPage({viewport}); page.on("pageerror",e=>errors.push(e.message));
  await page.goto(file,{waitUntil:"domcontentloaded"});
  const images=page.locator("#visuals img"),count=await images.count();
  if(count!==26) errors.push(`${viewport.width}px: expected 26 embeds, found ${count}`);
  const missingAlt=await page.locator("#visuals img:not([alt]), #visuals img[alt='']").count();
  if(missingAlt) errors.push(`${viewport.width}px: ${missingAlt} images lack alt text`);
  const decoded=await images.evaluateAll(async nodes=>{await Promise.all(nodes.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));return nodes.filter(img=>img.complete&&img.naturalWidth>0).length});
  if(decoded!==26) errors.push(`${viewport.width}px: only ${decoded}/26 images decoded`);
  const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(dims.scroll>dims.client+1) errors.push(`${viewport.width}px: horizontal overflow ${dims.scroll}>${dims.client}`);
  await page.keyboard.press("Tab"); const focus=await page.evaluate(()=>({tag:document.activeElement?.tagName,href:document.activeElement?.getAttribute("href")}));
  if(focus.tag!=="A"||focus.href!=="#visuals") errors.push(`${viewport.width}px: skip link is not first focus target`);
  await page.keyboard.press("Enter"); if(await page.evaluate(()=>location.hash)!=="#visuals") errors.push(`${viewport.width}px: skip link failed`);
  results.push(`${viewport.width}px: 26 embeds; ${decoded}/26 decoded; no overflow; keyboard skip link passed`); await page.close();
 }
}finally{await browser.close()}
console.log(results.join("\n"));
if(errors.length){console.error("Browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: responsive preview, all 26 image decodes, alt attributes and keyboard skip navigation.");
