import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const preview=pathToFileURL(resolve("/tmp/geography-chapter-05-preview.html")).href;
const liveUrl="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/workspace/geography/geography/chapters/05-atmosphere-and-climatology.md";
const browser=await chromium.launch({headless:true});
const errors=[],reports=[];
let expectedAlts=[];
try {
 for(const viewport of [{width:390,height:844},{width:1365,height:900}]){
  const page=await browser.newPage({viewport,deviceScaleFactor:1});
  page.on("pageerror",e=>errors.push("preview JS: "+e.message));
  page.on("requestfailed",r=>errors.push("preview request failed: "+r.url()+" — "+r.failure()?.errorText));
  await page.goto(preview,{waitUntil:"domcontentloaded"});
  await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
  const images=page.locator("#visuals img"),count=await images.count();
  if(viewport.width===390) expectedAlts=await images.evaluateAll(nodes=>nodes.map(img=>img.alt));
  if(count!==46) errors.push(viewport.width+"px preview: expected 46 images, found "+count);
  const decoded=await images.evaluateAll(async nodes=>{
   await Promise.all(nodes.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
   return nodes.filter(img=>img.complete&&img.naturalWidth>0).length;
  });
  if(decoded!==46) errors.push(viewport.width+"px preview: only "+decoded+"/46 images decoded");
  const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(dims.scroll>dims.client+1) errors.push(viewport.width+"px preview: horizontal overflow");
  await page.keyboard.press("Tab");
  const focus=await page.evaluate(()=>({tag:document.activeElement?.tagName,href:document.activeElement?.getAttribute("href")}));
  if(focus.tag!=="A"||focus.href!=="#visuals") errors.push(viewport.width+"px preview: keyboard skip link failed");
  await page.keyboard.press("Enter");
  if(await page.evaluate(()=>location.hash)!=="#visuals") errors.push(viewport.width+"px preview: skip link did not navigate");
  const axe=await page.evaluate(async()=>await window.axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa"]}}));
  if(axe.violations.length) errors.push(viewport.width+"px preview: axe violations "+axe.violations.map(v=>v.id).join(", "));
  await page.screenshot({path:"/tmp/chapter-05-preview-"+viewport.width+".png",fullPage:true});
  reports.push(viewport.width+"px isolated preview: "+decoded+"/46 decoded; axe violations="+axe.violations.length);
  await page.close();

  const live=await browser.newPage({viewport,deviceScaleFactor:1});
  const imageResponses=[];
  live.on("response",response=>{if(response.url().includes("camo.githubusercontent.com")) imageResponses.push({url:response.url(),status:response.status()})});
  await live.goto(liveUrl,{waitUntil:"domcontentloaded",timeout:60000});
  await live.locator(".markdown-body").first().waitFor({state:"visible",timeout:60000});
  const allImages=live.locator(".markdown-body img");
  const liveData=await allImages.evaluateAll((nodes,alts)=>nodes.filter(img=>alts.includes(img.alt)).map(img=>({alt:img.alt,src:img.src})),expectedAlts);
  if(liveData.length!==46) errors.push(viewport.width+"px GitHub Markdown: expected 46 chapter images, found "+liveData.length+"; all markdown-body imgs="+await allImages.count());
  const liveDecoded=await allImages.evaluateAll(async (nodes,alts)=>{
   const selected=nodes.filter(img=>alts.includes(img.alt));
   await Promise.all(selected.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
   return selected.filter(img=>img.complete&&img.naturalWidth>0).length;
  },expectedAlts);
  if(liveDecoded!==46){
   const broken=await allImages.evaluateAll((nodes,alts)=>nodes.filter(img=>alts.includes(img.alt)&&(!img.complete||img.naturalWidth===0)).map(img=>({alt:img.alt,src:img.src})),expectedAlts);
   errors.push(viewport.width+"px GitHub Markdown: "+liveDecoded+"/46 decoded; broken="+JSON.stringify(broken)+"; Camo errors="+JSON.stringify(imageResponses.filter(x=>x.status>=400)));
  }
  const liveDims=await live.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(liveDims.scroll>liveDims.client+1) errors.push(viewport.width+"px GitHub Markdown: horizontal overflow "+liveDims.scroll+">"+liveDims.client);
  await live.screenshot({path:"/tmp/chapter-05-github-"+viewport.width+".png",fullPage:true});
  reports.push(viewport.width+"px GitHub Markdown: "+liveDecoded+"/46 chapter images decoded; Camo HTTP errors="+imageResponses.filter(x=>x.status>=400).length);
  await live.close();
 }
} finally {await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 05 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: isolated preview and live GitHub Markdown at mobile/desktop; all chapter images decoded; axe WCAG scan clean; keyboard navigation passed.");
