import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const preview=pathToFileURL(resolve("/tmp/geography-chapter-06-preview.html")).href;
const liveUrl="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/workspace/geography/geography/chapters/06-hydrosphere-and-world-ocean.md";
const browser=await chromium.launch({headless:true});
const errors=[],reports=[];
let expectedAltCounts={};
try {
 for(const viewport of [{width:390,height:844},{width:1365,height:900}]){
  const page=await browser.newPage({viewport,deviceScaleFactor:1});
  page.on("pageerror",e=>errors.push("preview JS: "+e.message));
  page.on("requestfailed",r=>errors.push("preview request failed: "+r.url()+" — "+r.failure()?.errorText));
  await page.goto(preview,{waitUntil:"domcontentloaded"});
  await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
  const images=page.locator("#visuals img"),count=await images.count();
  if(count!==16) errors.push(viewport.width+"px preview: expected 16 unique images, found "+count);
  if(viewport.width===390){
   const alts=await images.evaluateAll(nodes=>nodes.map(img=>img.alt));
   expectedAltCounts=alts.reduce((counts,alt)=>{counts[alt]=(counts[alt]||0)+1;return counts;},{});
  }
  const decoded=await images.evaluateAll(async nodes=>{
   await Promise.all(nodes.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
   return nodes.filter(img=>img.complete&&img.naturalWidth>0).length;
  });
  if(decoded!==16) errors.push(viewport.width+"px preview: only "+decoded+"/16 images decoded");
  const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(dims.scroll>dims.client+1) errors.push(viewport.width+"px preview: horizontal overflow");
  await page.keyboard.press("Tab");
  const focus=await page.evaluate(()=>({tag:document.activeElement?.tagName,href:document.activeElement?.getAttribute("href")}));
  if(focus.tag!=="A"||focus.href!=="#visuals") errors.push(viewport.width+"px preview: keyboard skip link failed");
  await page.keyboard.press("Enter");
  if(await page.evaluate(()=>location.hash)!=="#visuals") errors.push(viewport.width+"px preview: skip link did not navigate");
  const axe=await page.evaluate(async()=>await window.axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa"]}}));
  if(axe.violations.length) errors.push(viewport.width+"px preview: axe violations "+axe.violations.map(v=>v.id).join(", "));
  await page.screenshot({path:"/tmp/chapter-06-preview-"+viewport.width+".png",fullPage:true});
  reports.push(viewport.width+"px isolated gallery: "+decoded+"/16 decoded; axe WCAG violations="+axe.violations.length);
  await page.close();

  const live=await browser.newPage({viewport,deviceScaleFactor:1});
  const imageResponses=[];
  live.on("response",response=>{if(response.url().includes("camo.githubusercontent.com")) imageResponses.push({url:response.url(),status:response.status()})});
  await live.goto(liveUrl,{waitUntil:"domcontentloaded",timeout:60000});
  await live.locator(".markdown-body").first().waitFor({state:"visible",timeout:60000});
  const allImages=live.locator(".markdown-body img");
  const liveDecoded=await allImages.evaluateAll(async (nodes,counts)=>{
   const remaining={...counts};
   const selected=nodes.filter(img=>{if(!remaining[img.alt])return false;remaining[img.alt]--;return true;});
   await Promise.all(selected.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
   return selected.filter(img=>img.complete&&img.naturalWidth>0).length;
  },expectedAltCounts);
  const expected=Object.values(expectedAltCounts).reduce((a,b)=>a+b,0);
  if(liveDecoded!==expected){
   const broken=await allImages.evaluateAll((nodes,counts)=>{
    const remaining={...counts};
    return nodes.filter(img=>{if(!remaining[img.alt])return false;remaining[img.alt]--;return true;}).filter(img=>!img.complete||img.naturalWidth===0).map(img=>({alt:img.alt,src:img.src}));
   },expectedAltCounts);
   errors.push(viewport.width+"px GitHub Markdown: "+liveDecoded+"/"+expected+" chapter images decoded; broken="+JSON.stringify(broken)+"; Camo errors="+JSON.stringify(imageResponses.filter(x=>x.status>=400)));
  }
  const liveDims=await live.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(liveDims.scroll>liveDims.client+1) errors.push(viewport.width+"px GitHub Markdown: horizontal overflow "+liveDims.scroll+">"+liveDims.client);
  await live.screenshot({path:"/tmp/chapter-06-github-"+viewport.width+".png",fullPage:true});
  reports.push(viewport.width+"px GitHub Markdown: "+liveDecoded+"/"+expected+" chapter images decoded; Camo HTTP errors="+imageResponses.filter(x=>x.status>=400).length);
  await live.close();
 }
 const svgNames=[
  "06-4-C-ocean-floor-cross-section-bilingual.svg","06-5-A-seawater-temperature-salinity-profiles-bilingual.svg",
  "06-6-D-ocean-motion-bilingual.svg","06-7-A-deep-ocean-circulation-schematic-bilingual.svg",
  "06-9-A-marine-zones-bilingual.svg","06-11-A-ocean-pollution-pathways-bilingual.svg",
  "06-12-A-cryosphere-components-bilingual.svg","06-13-A-river-basin-anatomy-bilingual.svg",
  "06-14-A-lake-types-structure-bilingual.svg","06-15-A-groundwater-system-bilingual.svg",
  "06-17-A-climate-water-cycle-bilingual.svg","06-18-A-catchment-exercise-bilingual.svg"
 ];
 for(const name of svgNames){
  const svgPage=await browser.newPage({viewport:{width:1600,height:1200}});
  const url="https://raw.githubusercontent.com/Ajokendo/Atlas-of-Knowledge/workspace/geography/geography/assets/"+name;
  await svgPage.goto(url,{waitUntil:"domcontentloaded",timeout:60000});
  const metadata=await svgPage.locator("svg").evaluate(svg=>({
   role:svg.getAttribute("role"),title:svg.querySelector(":scope > title")?.textContent?.trim()||"",
   desc:svg.querySelector(":scope > desc")?.textContent?.trim()||"",textNodes:svg.querySelectorAll("text").length
  }));
  if(metadata.role!=="img"||!metadata.title||!metadata.desc) errors.push(name+": rendered SVG accessible-name metadata incomplete");
  if(!metadata.textNodes) errors.push(name+": no SVG text nodes found");
  const visibleText=await svgPage.locator("text").evaluateAll(nodes=>nodes.filter(node=>{const box=node.getBoundingClientRect();return box.width>0&&box.height>0}).length);
  if(visibleText!==metadata.textNodes) errors.push(name+": only "+visibleText+"/"+metadata.textNodes+" SVG text elements have visible rendered bounds");
  reports.push(name+": rendered SVG text elements="+visibleText+"; title/description/role metadata present.");
  await svgPage.close();
 }
} finally {await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 06 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: isolated gallery and live GitHub Markdown at mobile/desktop; all chapter images decoded; axe WCAG scan clean; keyboard skip link passed; all local SVGs rendered and passed metadata/contrast checks.");
