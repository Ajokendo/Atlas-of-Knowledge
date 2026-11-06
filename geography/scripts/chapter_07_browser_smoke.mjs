import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const preview=pathToFileURL(resolve("/tmp/geography-chapter-07-preview.html")).href;
const names=[
"07-A-biosphere-earth-spheres-bilingual.svg","07-B-food-web-energy-pyramid-bilingual.svg",
"07-D-shelford-tolerance-curve-bilingual.svg","07-F-terrestrial-biome-panorama-bilingual.svg",
"07-G-lake-ocean-zonation-bilingual.svg","07-H-habitat-connectivity-bilingual.svg",
"07-I-carbon-nitrogen-cycles-bilingual.svg"];
const browser=await chromium.launch({headless:true}),errors=[],reports=[];
try{
 for(const viewport of [{width:390,height:844},{width:1365,height:900}]){
  const page=await browser.newPage({viewport,deviceScaleFactor:1});
  await page.goto(preview,{waitUntil:"load"});
  const images=page.locator("article img");
  const count=await images.count();
  if(count!==7)errors.push(viewport.width+"px gallery: expected 7 images, found "+count);
  const decoded=await images.evaluateAll(async nodes=>{
   await Promise.all(nodes.map(img=>img.decode().catch(()=>null)));
   return nodes.filter(img=>img.complete&&img.naturalWidth>0&&img.naturalHeight>0).length;
  });
  if(decoded!==7)errors.push(viewport.width+"px gallery: only "+decoded+"/7 SVGs decoded");
  const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(dims.scroll>dims.client+1)errors.push(viewport.width+"px gallery horizontal overflow "+dims.scroll+">"+dims.client);
  await page.screenshot({path:"/tmp/chapter-07-gallery-"+viewport.width+".png",fullPage:true});
  reports.push(viewport.width+"px gallery: "+decoded+"/7 decoded; overflow="+(dims.scroll>dims.client));
  await page.close();
 }
 for(const name of names){
  const page=await browser.newPage({viewport:{width:1600,height:1200},deviceScaleFactor:1});
  const path=resolve("geography/assets/diagrams/"+name);
  await page.goto(pathToFileURL(path).href,{waitUntil:"load"});
  await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
  const data=await page.evaluate(()=>{
   const svg=document.querySelector("svg"),vb=svg?.viewBox?.baseVal;
   if(!svg||!vb)return {error:"SVG or viewBox missing"};
   const title=svg.querySelector(":scope > title")?.textContent?.trim()||"";
   const desc=svg.querySelector(":scope > desc")?.textContent?.trim()||"";
   const texts=[...svg.querySelectorAll("text")].map((node,i)=>{
    const b=node.getBBox(),cs=getComputedStyle(node);
    return {i,text:(node.textContent||"").replace(/\\s+/g," ").trim().slice(0,90),x:b.x,y:b.y,w:b.width,h:b.height,font:parseFloat(cs.fontSize)};
   });
   const outside=texts.filter(t=>t.x<vb.x-1||t.y<vb.y-1||t.x+t.w>vb.x+vb.width+1||t.y+t.h>vb.y+vb.height+1);
   const tiny=texts.filter(t=>t.font<12);
   return {role:svg.getAttribute("role"),title,desc,textCount:texts.length,outside,tiny,fonts:texts.map(t=>t.font).filter(Number.isFinite)};
  });
  if(data.error)errors.push(name+": "+data.error);
  if(data.role!=="img"||!data.title||!data.desc)errors.push(name+": accessible metadata incomplete");
  if(!data.textCount)errors.push(name+": no rendered text labels");
  if(data.outside?.length)errors.push(name+": text outside viewBox "+JSON.stringify(data.outside));
  const axe=await page.evaluate(async()=>await window.axe.run(document,{runOnly:{type:"rule",values:["color-contrast"]}}));
  reports.push(name+": text="+data.textCount+"; font-size range="+Math.min(...data.fonts).toFixed(1)+"–"+Math.max(...data.fonts).toFixed(1)+"px; outside="+(data.outside?.length||0)+"; tiny(<12px)="+(data.tiny?.length||0)+"; contrast violations="+axe.violations.length);
  if(axe.violations.length)errors.push(name+": axe contrast violations "+axe.violations.map(v=>v.id+"("+v.nodes.length+")").join(","));
  await page.screenshot({path:"/tmp/chapter-07-"+name.replace(".svg","")+".png",fullPage:true});
  await page.close();
 }
}finally{await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 07 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: all 7 SVGs render; no text is outside the viewBox; no horizontal overflow; color-contrast scan clean.");
