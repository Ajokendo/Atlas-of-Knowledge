#!/usr/bin/env python3
"""Build an isolated browser QA gallery from all Chapter 05 Markdown image embeds."""
from __future__ import annotations
import html, re, sys
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin
SOURCE=Path("geography/chapters/05-atmosphere-and-climatology.md")
BASE_URL="https://raw.githubusercontent.com/Ajokendo/Atlas-of-Knowledge/workspace/geography/geography/chapters/05-atmosphere-and-climatology.md"
IMAGE=re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
def main():
    if not SOURCE.is_file(): print("FAIL: missing chapter source"); return 1
    source=SOURCE.read_text(encoding="utf-8"); matches=list(IMAGE.finditer(source)); blocks=[]; urls=[]
    for i,m in enumerate(matches,1):
        alt,target=m.groups()
        if not alt.strip(): print(f"FAIL: empty alt text at embed {i}"); return 1
        url=urljoin(BASE_URL,target)
        if not url.startswith("https://"): print("FAIL: non-HTTPS source",url); return 1
        urls.append(url)
        before=source[:m.start()].splitlines(); heading=""
        for line in reversed(before[-6:]):
            if line.startswith(("**Иллюстрация","**Illustration","**Figure")):
                heading=re.sub(r"^\*\*|\*\*$","",line.strip()); break
        blocks.append('<figure><img loading="lazy" decoding="async" src="'+html.escape(url,quote=True)+'" alt="'+html.escape(alt,quote=True)+'" data-embed="'+str(i)+'"><figcaption>'+html.escape(heading)+'</figcaption></figure>')
    counts=Counter(urls)
    if len(matches)!=46 or len(counts)!=23 or any(n!=2 for n in counts.values()):
        print(f"FAIL: expected 46 embeds/23 unique paired assets; got {len(matches)}/{len(counts)}")
        for url,n in counts.items():
            if n!=2: print(n,url)
        return 1
    out=Path(sys.argv[1] if len(sys.argv)>1 else "/tmp/geography-chapter-05-preview.html")
    doc="""<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Chapter 05 visual QA</title><style>
:root{color-scheme:light;background:#f2f2ef;color:#18181a;font:16px/1.55 system-ui,sans-serif}*{box-sizing:border-box}body{margin:0}header,main{max-width:1160px;margin:auto;padding:20px}h1{font:400 clamp(2rem,5vw,3.4rem)/1.1 Georgia,serif}.lead{max-width:760px;color:#4b4b4b}.gallery{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}figure{margin:0;padding:12px;min-width:0;background:#fff;border:1px solid #c9c9c4;border-radius:8px}img{display:block;width:100%;height:auto;max-height:560px;object-fit:contain;background:#fff}figcaption{font-size:.88rem;color:#333;overflow-wrap:anywhere;margin-top:8px}.skip{position:absolute;left:-9999px;top:8px}.skip:focus{left:12px;background:#fff;color:#111;padding:12px;outline:3px solid #165d75;z-index:10}@media(max-width:680px){header,main{padding:14px}.gallery{grid-template-columns:minmax(0,1fr)}figure{padding:9px}}
</style></head><body><a class="skip" href="#visuals">Перейти к иллюстрациям / Skip to figures</a><header>Atlas of Knowledge · Geography · Chapter 05 · isolated QA harness</header><main><h1>Атмосфера и климатология / Atmosphere and Climatology</h1><p class="lead">All RU/EN image embeds extracted from the chapter. This isolated gallery is for asset rendering and responsive checks; it is not the production chapter reader.</p><section id="visuals" aria-label="Chapter 05 visual assets"><div class="gallery">"""+"".join(blocks)+"""</div></section></main></body></html>"""
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(doc,encoding="utf-8")
    print(f"PASS: generated {out}; {len(matches)} embeds, {len(counts)} unique bilingual assets.")
    return 0
if __name__=="__main__": raise SystemExit(main())
