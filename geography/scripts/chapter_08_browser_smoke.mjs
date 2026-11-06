import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
import { readFileSync } from "node:fs";

const preview = pathToFileURL(resolve("/tmp/geography-chapter-08-preview.html")).href;
const liveUrl = "https://github.com/Ajokendo/Atlas-of-Knowledge/blob/workspace/geography/geography/chapters/08-soils-and-landscape-geography.md";
const chapter = readFileSync(resolve("geography/chapters/08-soils-and-landscape-geography.md"), "utf8");
const embeds = [...chapter.matchAll(/!\[([^\]]*)\]\(([^)\s]+)\)/g)].map(m => ({alt:m[1],src:m[2]}));
const errors = [], reports = [];
const ids = ["08-A","08-B","08-C","08-D","08-E","08-F","08-G"];
const localSvgNames = [
 "08-A-soil-profile-horizons-bilingual.svg",
 "08-C-soil-degradation-processes-bilingual.svg",
 "08-D-soil-earth-spheres-interface-bilingual.svg",
 "08-E-soil-forming-factors-bilingual.svg",
 "08-F-landscape-morphology-block-bilingual.svg",
 "08-G-landscape-mosaic-patches-corridors-matrix-bilingual.svg"
];
if (embeds.length !== 14) errors.push("Chapter Markdown: expected 14 image embeds, found " + embeds.length);
for (const id of ids) {
 const occurrences = (chapter.match(new RegExp(id,"g")) || []).length;
 if (!occurrences) errors.push("Missing visual ID " + id);
}
if (!chapter.includes("https://files.isric.org/public/WRB/wrb2014.png")) errors.push("08-B ISRIC map source missing");
const svgD = readFileSync(resolve("geography/assets/diagrams/08-D-soil-earth-spheres-interface-bilingual.svg"),"utf8");
const svgG = readFileSync(resolve("geography/assets/diagrams/08-G-landscape-mosaic-patches-corridors-matrix-bilingual.svg"),"utf8");
if (!svgD.includes('fill="#c3a27e"')) errors.push("08-D central soil panel must retain mobile-safe text contrast background #c3a27e");
if (!svgG.includes('fill="#a3c19a"')) errors.push("08-G habitat patches must retain mobile-safe text contrast background #a3c19a");
for (const name of localSvgNames) {
 if (!readFileSync(resolve("geography/assets/diagrams/" + name),"utf8").includes("<svg")) errors.push("Invalid/missing SVG root: " + name);
}

const browser = await chromium.launch({headless:true});
try {
 for (const viewport of [{width:390,height:844},{width:1365,height:900}]) {
  const page = await browser.newPage({viewport,deviceScaleFactor:1});
  await page.goto(preview,{waitUntil:"load"});
  await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
  const count = await page.locator("article[data-visual]").count();
  if (count !== 7) errors.push(viewport.width+"px gallery: expected 7 assets, found "+count);
  const dims = await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if (dims.scroll > dims.client + 1) errors.push(viewport.width+"px gallery horizontal overflow");
  const data = await page.evaluate(()=>{
   const svgs=[...document.querySelectorAll("article svg")];
   return svgs.map(svg=>{
    const vb=svg.viewBox.baseVal, rect=svg.getBoundingClientRect();
    const title=svg.querySelector(":scope > title"), desc=svg.querySelector(":scope > desc");
    const texts=[...svg.querySelectorAll("text")].map(node=>{
     const b=node.getBBox(), font=parseFloat(getComputedStyle(node).fontSize);
     const m=node.getScreenCTM(), inv=svg.getScreenCTM().inverse();
     const corners=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m).matrixTransform(inv));
     const xs=corners.map(p=>p.x), ys=corners.map(p=>p.y), x=Math.min(...xs), y=Math.min(...ys);
     return {text:(node.textContent||"").replace(/\s+/g," ").trim().slice(0,70),x,y,w:Math.max(...xs)-x,h:Math.max(...ys)-y,effective:font*rect.width/vb.width};
    });
    const outside=texts.filter(t=>t.x<vb.x-1||t.y<vb.y-1||t.x+t.w>vb.x+vb.width+1||t.y+t.h>vb.y+vb.height+1);
    const overlaps=[];
    for(let i=0;i<texts.length;i++) for(let j=i+1;j<texts.length;j++){
     const a=texts[i],b=texts[j],dx=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x),dy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
     if(dx>2&&dy>2) overlaps.push({a:a.text,b:b.text});
    }
    return {name:title?.textContent||"untitled",role:svg.getAttribute("role"),desc:!!desc?.textContent?.trim(),textCount:texts.length,outside,overlaps,minEffective:Math.min(...texts.map(t=>t.effective))};
   });
  });
  for(const d of data){
   if(d.role!=="img"||!d.desc||!d.textCount) errors.push(viewport.width+"px "+d.name+": title/description/role/text missing");
   if(d.outside.length) errors.push(viewport.width+"px "+d.name+": text outside viewBox "+JSON.stringify(d.outside));
   if(d.overlaps.length) errors.push(viewport.width+"px "+d.name+": text-to-text overlap "+JSON.stringify(d.overlaps));
  }
  const axe=await page.evaluate(async()=>await window.axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa"]}}));
  if(axe.violations.length) errors.push(viewport.width+"px gallery axe violations "+axe.violations.map(v=>v.id+"("+v.nodes.length+")").join(","));
  const map=await page.locator('article[data-visual="08-B"] img').evaluate(img=>({complete:img.complete,naturalWidth:img.naturalWidth,naturalHeight:img.naturalHeight,displayWidth:img.getBoundingClientRect().width}));
  if(!map.complete||!map.naturalWidth) errors.push(viewport.width+"px ISRIC map failed to decode");
  reports.push(viewport.width+"px gallery: 6/6 SVGs; ISRIC PNG "+map.naturalWidth+"x"+map.naturalHeight+" displayed at "+Math.round(map.displayWidth)+"px; overflow="+(dims.scroll>dims.client)+"; axe="+axe.violations.length+"; "+data.map(d=>d.name+": smallest rendered text "+d.minEffective.toFixed(1)+"px; overlap="+d.overlaps.length).join(" | "));
  await page.screenshot({path:"/tmp/chapter-08-gallery-"+viewport.width+".png",fullPage:true});
  for(let i=0;i<7;i++) await page.locator("article").nth(i).screenshot({path:"/tmp/chapter-08-visual-"+(i+1)+".png"});
  await page.close();

  const live=await browser.newPage({viewport,deviceScaleFactor:1});
  await live.goto(liveUrl,{waitUntil:"domcontentloaded",timeout:60000});
  await live.locator(".markdown-body").first().waitFor({state:"visible",timeout:60000});
  const images=live.locator(".markdown-body img");
  const chapterImages=await images.evaluateAll((nodes,expected)=>{
   const remaining=[...expected]; const selected=[];
   for(const img of nodes){const i=remaining.findIndex(x=>x.alt===img.alt);if(i>=0){selected.push(img);remaining.splice(i,1);}}
   return {selected:selected.length,missing:remaining.map(x=>x.alt)};
  },embeds);
  if(chapterImages.selected!==14) errors.push(viewport.width+"px GitHub Markdown: expected 14 Chapter 08 images, found "+chapterImages.selected);
  const decoded=await images.evaluateAll(async(nodes,expected)=>{
   const remaining=[...expected],selected=[];
   for(const img of nodes){const i=remaining.findIndex(x=>x.alt===img.alt);if(i>=0){selected.push(img);remaining.splice(i,1);}}
   await Promise.all(selected.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
   return selected.filter(img=>img.complete&&img.naturalWidth>0).length;
  },embeds);
  if(decoded!==14) errors.push(viewport.width+"px GitHub Markdown: only "+decoded+"/14 images decoded");
  const liveDims=await live.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(liveDims.scroll>liveDims.client+1) errors.push(viewport.width+"px GitHub Markdown horizontal overflow");
  reports.push(viewport.width+"px live GitHub Markdown: "+decoded+"/14 images decoded; overflow="+(liveDims.scroll>liveDims.client));
  await live.close();
 }
} finally { await browser.close(); }

console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 08 browser QA failed:\n"+errors.join("\n"));process.exit(1);}
console.log("PASS: six original SVGs render without viewBox clipping or text overlap; ISRIC PNG decodes; all 14 RU/EN chapter embeds decode at 390px and 1365px; no horizontal overflow; axe WCAG 2.1 A/AA clean.");
