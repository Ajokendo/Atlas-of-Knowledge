import sys, json, re
from playwright.sync_api import sync_playwright
args=[a for a in sys.argv[1:] if not a.startswith('-')]; verbose='-v' in sys.argv; shots='-s' in sys.argv
BAD=re.compile(r'NaN|undefined|Infinity|\[object|null')
base="file:///home/claude/atlas-of-knowledge/math/chapters/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for slug in args:
        errs=[]; probs=[]
        for name,vw,vh in [("desk",1200,900),("mob",390,800)]:
            pg=b.new_page(viewport={"width":vw,"height":vh})
            pg.on("console",lambda m:errs.append((name,m.text)) if m.type in("error","warning") else None)
            pg.on("pageerror",lambda e:errs.append((name,"pageerror "+str(e))))
            pg.goto(base+slug); pg.wait_for_timeout(300)
            if name=="desk":
                if verbose:
                    for i,t in enumerate(pg.eval_on_selector_all(".lab",'ls=>ls.map(l=>[...l.querySelectorAll(".stat strong")].map(e=>e.textContent).join(" | ")+" || "+l.querySelector(".fb").textContent)')): print("  M%d: %s"%(i+1,t))
                rng=pg.eval_on_selector_all('.lab input[type=range]','es=>es.map(e=>[e.id,e.min,e.max,e.value])')
                sels=pg.eval_on_selector_all('.lab select','es=>es.map(e=>[e.id,e.options.length,e.value])')
                def scan(tag):
                    t=pg.inner_text(".lab") if False else " ".join(pg.eval_on_selector_all(".lab","ls=>ls.map(l=>l.innerText+' '+l.querySelector('svg').innerHTML.replace(/<[^>]*>/g,' '))"))
                    m=BAD.search(t)
                    if m: probs.append(tag+": "+m.group(0)+" ..."+t[max(0,m.start()-40):m.end()+20].replace("\n"," "))
                scan("default")
                for (i,mn,mx,val) in rng:
                    for v in (mn,mx):
                        pg.evaluate("a=>{const e=document.getElementById(a[0]);e.value=a[1];e.dispatchEvent(new Event('input'))}",[i,v]); scan("%s=%s"%(i,v))
                    pg.evaluate("a=>{const e=document.getElementById(a[0]);e.value=a[1];e.dispatchEvent(new Event('input'))}",[i,val])
                for (i,cnt,val) in sels:
                    for k in range(cnt):
                        pg.evaluate("a=>{const e=document.getElementById(a[0]);e.value=a[1];e.dispatchEvent(new Event('input'))}",[i,str(k)]); scan("%s#%d"%(i,k))
                    pg.evaluate("a=>{const e=document.getElementById(a[0]);e.value=a[1];e.dispatchEvent(new Event('input'))}",[i,val])
                for i in range(pg.locator("#quizBox .q").count()): pg.locator("#quizBox .q").nth(i).locator("button.opt").first.click()
                pg.click("#lang"); pg.wait_for_timeout(150); scan("EN")
            ov=pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
            if ov>0: probs.append("overflow %s %d"%(name,ov))
            if shots and name=="desk":
                pg.click("#lang")
                for i in range(pg.locator(".lab").count()): pg.locator(".lab").nth(i).screenshot(path="/home/claude/shots/%s_lab%d.png"%(slug[:2],i+1))
            pg.close()
        print(slug, "OK" if not errs and not probs else "PROBLEMS", errs[:3], probs[:6])
    b.close()
