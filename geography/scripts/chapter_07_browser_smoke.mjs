import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
import { readFileSync } from "node:fs";
const preview=pathToFileURL(resolve("/tmp/geography-chapter-07-preview.html")).href;
const liveUrl="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/workspace/geography/geography/chapters/07-biosphere-and-natural-biomes.md";
const chapter=readFileSync(resolve("geography/chapters/07-biosphere-and-natural-biomes.md"),"utf8");
const embeds=[...chapter.matchAll(/!\[([^\]]*)\]\(([^)\s]+)\)/g)].map(m=>m[1]);
const expectedAltCounts=embeds.reduce((counts,alt)=>{counts[alt]=(counts[alt]||0)+1;return counts;},{});
const browser=await chromium.launch({headless:true}),errors=[],reports=[];
try{
 for(const viewport of [{width:390,height:844},{width:1365,height:900}]){
  const page=await browser.newPage({viewport,deviceScaleFactor:1});
  await page.goto(preview,{waitUntil:"load"});
  await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
  const count=await page.locator("article svg").count();
  if(count!==9)errors.push(viewport.width+"px gallery: expected 9 inline SVGs, found "+count);
  const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(dims.scroll>dims.client+1)errors.push(viewport.width+"px gallery horizontal overflow "+dims.scroll+">"+dims.client);
  const data=await page.evaluate(()=>{
   const svgs=[...document.querySelectorAll("article svg")];
   return svgs.map(svg=>{
    const vb=svg.viewBox.baseVal,rect=svg.getBoundingClientRect();
    const texts=[...svg.querySelectorAll("text")].map((node,i)=>{
     const b=node.getBBox(),cs=getComputedStyle(node),font=parseFloat(cs.fontSize),m=node.getScreenCTM(),inv=svg.getScreenCTM().inverse();
     const corners=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m).matrixTransform(inv));
     const xs=corners.map(p=>p.x),ys=corners.map(p=>p.y),x=Math.min(...xs),y=Math.min(...ys),w=Math.max(...xs)-x,h=Math.max(...ys)-y;
     return {i,text:(node.textContent||"").replace(/\s+/g," ").trim().slice(0,80),x,y,w,h,font,effective:font*rect.width/vb.width};
    });
    const outside=texts.filter(t=>t.x<vb.x-1||t.y<vb.y-1||t.x+t.w>vb.x+vb.width+1||t.y+t.h>vb.y+vb.height+1);
    const overlaps=[];
    for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){
     const a=texts[i],b=texts[j],dx=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x),dy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
     if(dx>2&&dy>2)overlaps.push({a:a.text,b:b.text});
    }
    return {name:svg.querySelector(":scope > title")?.textContent||"untitled",role:svg.getAttribute("role"),desc:!!svg.querySelector(":scope > desc"),textCount:texts.length,outside,overlaps,minEffective:Math.min(...texts.map(t=>t.effective)),minFont:Math.min(...texts.map(t=>t.font))};
   });
  });
  for(const d of data){
   if(d.role!=="img"||!d.desc||!d.textCount)errors.push(viewport.width+"px "+d.name+": title/description/role/text missing");
   if(d.outside.length)errors.push(viewport.width+"px "+d.name+": text outside viewBox "+JSON.stringify(d.outside));
   if(d.overlaps.length)errors.push(viewport.width+"px "+d.name+": text-to-text overlaps "+JSON.stringify(d.overlaps));
  }
  const axe=await page.evaluate(async()=>await window.axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa"]}}));
  reports.push(viewport.width+"px: 9/9 SVGs; overflow="+(dims.scroll>dims.client)+"; axe violations="+axe.violations.length+"; "+data.map(d=>d.name.split("/")[0]+": min rendered text "+d.minEffective.toFixed(1)+"px; text overlap="+d.overlaps.length).join(" | "));
  if(axe.violations.length)errors.push(viewport.width+"px gallery axe violations "+axe.violations.map(v=>v.id+"("+v.nodes.length+")").join(","));
  await page.screenshot({path:"/tmp/chapter-07-gallery-"+viewport.width+".png",fullPage:true});
  for(let i=0;i<9;i++)await page.locator("article").nth(i).screenshot({path:"/tmp/chapter-07-visual-"+(i+1)+".png"});
  await page.close();

  const live=await browser.newPage({viewport,deviceScaleFactor:1});
  await live.goto(liveUrl,{waitUntil:"domcontentloaded",timeout:60000});
  await live.locator(".markdown-body").first().waitFor({state:"visible",timeout:60000});
  const allImages=live.locator(".markdown-body img");
  const liveData=await allImages.evaluateAll((nodes,counts)=>{
   const remaining={...counts};
   return nodes.filter(img=>{if(!remaining[img.alt])return false;remaining[img.alt]--;return true;}).map(img=>({alt:img.alt,src:img.src}));
  },expectedAltCounts);
  if(liveData.length!==18)errors.push(viewport.width+"px GitHub Markdown: expected 18 Chapter 07 images, found "+liveData.length);
  const liveDecoded=await allImages.evaluateAll(async(nodes,counts)=>{
   const remaining={...counts};
   const selected=nodes.filter(img=>{if(!remaining[img.alt])return false;remaining[img.alt]--;return true;});
   await Promise.all(selected.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
   return selected.filter(img=>img.complete&&img.naturalWidth>0).length;
  },expectedAltCounts);
  if(liveDecoded!==14)errors.push(viewport.width+"px GitHub Markdown: only "+liveDecoded+"/14 images decoded");
  const liveDims=await live.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
  if(liveDims.scroll>liveDims.client+1)errors.push(viewport.width+"px GitHub Markdown horizontal overflow");
  reports.push(viewport.width+"px GitHub Markdown: "+liveDecoded+"/18 images decoded; overflow="+(liveDims.scroll>liveDims.client));
  await live.close();
 }
}finally{await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 07 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: all nine inline SVGs render at mobile/desktop; all 18 live GitHub Markdown embeds decode; no clipping or text overlap; axe WCAG 2.1 A/AA clean.");
