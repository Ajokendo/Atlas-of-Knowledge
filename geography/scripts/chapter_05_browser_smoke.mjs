import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const file=pathToFileURL(resolve("/tmp/geography-chapter-05-preview.html")).href;
const browser=await chromium.launch({headless:true});
const errors=[],reports=[];
try {
  for (const viewport of [{width:390,height:844},{width:1365,height:900}]) {
    const page=await browser.newPage({viewport,deviceScaleFactor:1});
    page.on("pageerror",e=>errors.push(e.message));
    page.on("requestfailed",r=>errors.push("request failed: "+r.url()+" — "+r.failure()?.errorText));
    await page.goto(file,{waitUntil:"domcontentloaded"});
    const images=page.locator("#visuals img"),count=await images.count();
    if(count!==46) errors.push(viewport.width+"px: expected 46 images, found "+count);
    const missing=await page.locator("#visuals img:not([alt]), #visuals img[alt='']").count();
    if(missing) errors.push(viewport.width+"px: "+missing+" images lack alt text");
    const decoded=await images.evaluateAll(async nodes=>{
      await Promise.all(nodes.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
      return nodes.filter(img=>img.complete&&img.naturalWidth>0).length;
    });
    if(decoded!==46){
      const broken=await images.evaluateAll(nodes=>nodes.filter(img=>!img.complete||img.naturalWidth===0).map(img=>({alt:img.alt,src:img.src})));
      errors.push(viewport.width+"px: only "+decoded+"/46 images decoded: "+JSON.stringify(broken));
    }
    const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
    if(dims.scroll>dims.client+1) errors.push(viewport.width+"px: horizontal overflow "+dims.scroll+">"+dims.client);
    const clipped=await images.evaluateAll(nodes=>nodes.filter(img=>{const r=img.getBoundingClientRect();return r.width>innerWidth+1||r.left < -1||r.right>innerWidth+1}).length);
    if(clipped) errors.push(viewport.width+"px: "+clipped+" images outside viewport");
    await page.keyboard.press("Tab");
    const focus=await page.evaluate(()=>({tag:document.activeElement?.tagName,href:document.activeElement?.getAttribute("href")}));
    if(focus.tag!=="A"||focus.href!=="#visuals") errors.push(viewport.width+"px: skip link is not first keyboard focus target");
    await page.keyboard.press("Enter");
    if(await page.evaluate(()=>location.hash)!=="#visuals") errors.push(viewport.width+"px: skip link navigation failed");
    const title=await page.title();
    if(!title.includes("Chapter 05")) errors.push(viewport.width+"px: document title missing");
    await page.screenshot({path:"/tmp/chapter-05-"+viewport.width+".png",fullPage:true});
    reports.push(viewport.width+"px: "+decoded+"/46 images decoded; no horizontal overflow; keyboard skip link passed");
    await page.close();
  }
} finally {await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 05 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: mobile/desktop Chromium preview, image decoding, alt text, viewport fit and keyboard skip navigation.");
