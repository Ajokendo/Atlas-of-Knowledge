import { chromium } from "playwright";
const browser = await chromium.launch({headless:true});
try {
 const page=await browser.newPage({viewport:{width:1365,height:900}}); const errors=[];
 page.on("pageerror",e=>errors.push(e.message));
 const response=await page.goto("http://127.0.0.1:4173/biology/chapters/flora-kyrgyzstan.html",{waitUntil:"networkidle"});
 if(!response?.ok()) throw new Error("Flora chapter HTTP response was not successful");
 const figure=page.locator('figure#image-brief-flora-naryn');
 if(await figure.count()!==1) throw new Error("Expected Naryn flora figure at original anchor");
 const expected=[
  ["flora-naryn-chatyr.webp",2816,2120,"https://commons.wikimedia.org/wiki/File:Chatyr_kul_lake.JPG","общественное достояние"],
  ["flora-naryn-songkul.webp",3240,2160,"https://commons.wikimedia.org/wiki/File:Son-Kul,_Kyrgyzstan_(44623421951).jpg","CC BY 2.0"],
  ["flora-naryn-clematis.webp",1400,933,"https://commons.wikimedia.org/wiki/File:Clematis_songorica.jpg","CC0"],
 ];
 const images=figure.locator("img");
 if(await images.count()!==expected.length) throw new Error("Expected three Naryn habitat/species photographs");
 for(let i=0;i<expected.length;i++){
  const [filename,width,height,sourceUrl,licence]=expected[i]; const img=images.nth(i);
  await img.evaluate(el=>{el.loading="eager";el.scrollIntoView();}); await img.evaluate(el=>el.decode());
  const state=await img.evaluate(el=>({src:el.getAttribute("src"),width:el.naturalWidth,height:el.naturalHeight,alt:el.alt,visible:!!(el.offsetWidth||el.offsetHeight||el.getClientRects().length),caption:el.parentElement?.innerText||"",attribution:el.parentElement?.querySelector("a")?.href||""}));
  if(!state.src?.endsWith(filename)||state.width!==width||state.height!==height||!state.alt.includes("/")||!state.visible||state.attribution!==sourceUrl||!state.caption.includes(licence)) throw new Error("Naryn image failed browser validation: "+JSON.stringify(state));
 }
 if(errors.length) throw new Error("Browser page errors: "+errors.join("; "));
 console.log("PASS Naryn flora integration: three locally decoded images at the original bilingual anchor");
} finally { await browser.close(); }
