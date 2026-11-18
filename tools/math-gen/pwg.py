import sys, json
from playwright.sync_api import sync_playwright
slug=sys.argv[1]; actions=json.loads(sys.argv[2]) if len(sys.argv)>2 else []
url="file:///home/claude/atlas-of-knowledge/math/chapters/"+slug
errs=[]
def setv(pg,i,v): pg.evaluate("(a)=>{const e=document.getElementById(a[0]);e.value=a[1];e.dispatchEvent(new Event('input'));e.dispatchEvent(new Event('change'))}",[i,str(v)])
def dump(pg,tag):
    print(tag, "|".join(pg.eval_on_selector_all(".stat strong","els=>els.map(e=>e.textContent)")), "||", " ## ".join(pg.eval_on_selector_all(".lab .fb","els=>els.map(e=>e.textContent)"))[:300])
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,vw,vh in [("desk",1200,900),("mob",390,800)]:
        pg=b.new_page(viewport={"width":vw,"height":vh})
        pg.on("console",lambda m:errs.append((name,m.type,m.text)) if m.type in("error","warning") else None)
        pg.on("pageerror",lambda e:errs.append((name,"pageerror",str(e))))
        pg.goto(url); pg.wait_for_timeout(400)
        if name=="desk":
            dump(pg,"default")
            for act in actions:
                for k,v in act.items():
                    if k=="click": pg.click("#"+v); pg.wait_for_timeout(int(act.get("wait",300)))
                    elif k!="wait": setv(pg,k,v)
                dump(pg,"after "+json.dumps(act,ensure_ascii=False))
        n=pg.locator(".lab").count()
        for i in range(n):
            pg.locator(".lab").nth(i).screenshot(path=f"/home/claude/shots/{slug[:2]}_{name}_lab{i+1}.png")
        qn=pg.locator("#quizBox .q").count()
        for i in range(qn): pg.locator("#quizBox .q").nth(i).locator("button.opt").first.click()
        if name=="desk": print("quiz:",pg.inner_text("#score"),pg.evaluate("localStorage.getItem('atlas-math-quiz-v1')"))
        print(name,"overflow:",pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth"),"labs",n,"q",qn)
        pg.click("#lang"); pg.wait_for_timeout(200)
        if name=="desk": dump(pg,"EN"); print(pg.title())
        pg.close()
    b.close()
print("ERRORS:",errs)
