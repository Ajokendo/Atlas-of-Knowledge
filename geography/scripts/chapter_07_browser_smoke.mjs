import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const preview=pathToFileURL(resolve("/tmp/geography-chapter-07-preview.html")).href;
const browser=await chromium.launch({headless:true}),errors=[],reports=[];
try{
 for(const viewport of [{width:390,height:844},{width:1365,height:900}]){
  const page=await browser.newPage({viewport,deviceScaleFactor:1});
  await page.goto(preview,{waitUntil:"load"});
  await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
  const count=await page.locator("article svg").count();
  if(count!==7)errors.push(viewport.width+"px gallery: expected 7 inline SVGs, found "+count);
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
  reports.push(viewport.width+"px: 7/7 SVGs; overflow="+(dims.scroll>dims.client)+"; axe violations="+axe.violations.length+"; "+data.map(d=>d.name.split("/")[0]+": min rendered text "+d.minEffective.toFixed(1)+"px; text overlap="+d.overlaps.length).join(" | "));
  if(axe.violations.length)errors.push(viewport.width+"px gallery axe violations "+axe.violations.map(v=>v.id+"("+v.nodes.length+")").join(","));
  await page.screenshot({path:"/tmp/chapter-07-gallery-"+viewport.width+".png",fullPage:true});
  for(let i=0;i<7;i++)await page.locator("article").nth(i).screenshot({path:"/tmp/chapter-07-visual-"+(i+1)+".png"});
  await page.close();
 }
}finally{await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 07 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: all seven inline SVGs render at mobile/desktop; no clipping or text overlap; axe WCAG 2.1 A/AA clean.");
