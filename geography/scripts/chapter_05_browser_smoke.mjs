import { chromium } from "playwright";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";

const preview=pathToFileURL(resolve("/tmp/geography-chapter-05-preview.html")).href;
const liveUrl="https://github.com/Ajokendo/Atlas-of-Knowledge/blob/workspace/geography/geography/chapters/05-atmosphere-and-climatology.md";
const browser=await chromium.launch({headless:true});
const errors=[],reports=[];
try {
  for (const viewport of [{width:390,height:844},{width:1365,height:900}]) {
    const page=await browser.newPage({viewport,deviceScaleFactor:1});
    page.on("pageerror",e=>errors.push("preview JS: "+e.message));
    page.on("requestfailed",r=>errors.push("preview request failed: "+r.url()+" — "+r.failure()?.errorText));
    await page.goto(preview,{waitUntil:"domcontentloaded"});
    await page.addScriptTag({path:resolve("node_modules/axe-core/axe.min.js")});
    const images=page.locator("#visuals img"),count=await images.count();
    if(count!==46) errors.push(viewport.width+"px preview: expected 46 images, found "+count);
    const missing=await page.locator("#visuals img:not([alt]), #visuals img[alt='']").count();
    if(missing) errors.push(viewport.width+"px preview: "+missing+" images lack alt text");
    const decoded=await images.evaluateAll(async nodes=>{
      await Promise.all(nodes.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
      return nodes.filter(img=>img.complete&&img.naturalWidth>0).length;
    });
    if(decoded!==46){
      const broken=await images.evaluateAll(nodes=>nodes.filter(img=>!img.complete||img.naturalWidth===0).map(img=>({alt:img.alt,src:img.src})));
      errors.push(viewport.width+"px preview: only "+decoded+"/46 images decoded: "+JSON.stringify(broken));
    }
    const dims=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
    if(dims.scroll>dims.client+1) errors.push(viewport.width+"px preview: horizontal overflow "+dims.scroll+">"+dims.client);
    const clipped=await images.evaluateAll(nodes=>nodes.filter(img=>{const r=img.getBoundingClientRect();return r.width>innerWidth+1||r.left < -1||r.right>innerWidth+1}).length);
    if(clipped) errors.push(viewport.width+"px preview: "+clipped+" images outside viewport");
    await page.keyboard.press("Tab");
    const focus=await page.evaluate(()=>({tag:document.activeElement?.tagName,href:document.activeElement?.getAttribute("href")}));
    if(focus.tag!=="A"||focus.href!=="#visuals") errors.push(viewport.width+"px preview: skip link is not first keyboard focus target");
    await page.keyboard.press("Enter");
    if(await page.evaluate(()=>location.hash)!=="#visuals") errors.push(viewport.width+"px preview: skip link navigation failed");
    const axe=await page.evaluate(async()=>await window.axe.run(document,{runOnly:{type:"tag",values:["wcag2a","wcag2aa","wcag21a","wcag21aa"]}}));
    if(axe.violations.length) errors.push(viewport.width+"px preview: axe WCAG violations: "+axe.violations.map(v=>v.id+" ("+v.nodes.length+")").join(", "));
    await page.screenshot({path:"/tmp/chapter-05-preview-"+viewport.width+".png",fullPage:true});
    reports.push(viewport.width+"px isolated preview: "+decoded+"/46 decoded; no overflow; skip link; axe violations="+axe.violations.length);
    await page.close();

    const live=await browser.newPage({viewport,deviceScaleFactor:1});
    await live.goto(liveUrl,{waitUntil:"domcontentloaded",timeout:60000});
    await live.locator(".markdown-body").first().waitFor({state:"visible",timeout:60000});
    const liveImages=live.locator(".markdown-body img");
    const liveCount=await liveImages.count();
    if(liveCount!==46) errors.push(viewport.width+"px GitHub Markdown: expected 46 images, found "+liveCount);
    const liveMissing=await live.locator(".markdown-body img:not([alt]), .markdown-body img[alt='']").count();
    if(liveMissing) errors.push(viewport.width+"px GitHub Markdown: "+liveMissing+" images lack alt text");
    const liveDecoded=await liveImages.evaluateAll(async nodes=>{
      await Promise.all(nodes.map(img=>{img.loading="eager";return img.decode().catch(()=>null)}));
      return nodes.filter(img=>img.complete&&img.naturalWidth>0).length;
    });
    if(liveDecoded!==46){
      const broken=await liveImages.evaluateAll(nodes=>nodes.filter(img=>!img.complete||img.naturalWidth===0).map(img=>({alt:img.alt,src:img.src})));
      errors.push(viewport.width+"px GitHub Markdown: only "+liveDecoded+"/46 images decoded: "+JSON.stringify(broken));
    }
    const liveDims=await live.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));
    if(liveDims.scroll>liveDims.client+1) errors.push(viewport.width+"px GitHub Markdown: horizontal overflow "+liveDims.scroll+">"+liveDims.client);
    await live.screenshot({path:"/tmp/chapter-05-github-"+viewport.width+".png",fullPage:true});
    reports.push(viewport.width+"px GitHub Markdown: "+liveDecoded+"/46 images decoded; alt attributes; no horizontal overflow");
    await live.close();
  }
} finally {await browser.close()}
console.log(reports.join("\n"));
if(errors.length){console.error("Chapter 05 browser QA failed:\n"+errors.join("\n"));process.exit(1)}
console.log("PASS: isolated preview and actual GitHub Markdown rendering at mobile/desktop; all images decoded; axe WCAG scan clean; keyboard skip navigation passed.");
