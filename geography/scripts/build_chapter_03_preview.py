#!/usr/bin/env python3
"""Build an isolated visual QA page from every Chapter 03 Markdown image embed."""
from __future__ import annotations
import html, re, sys
from collections import Counter
from pathlib import Path
SOURCE=Path("geography/chapters/03-lithosphere-and-geological-processes.md")
IMAGE=re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")

def main():
    if not SOURCE.is_file(): print("FAIL: missing",SOURCE); return 1
    source=SOURCE.read_text(encoding="utf-8"); blocks=[]
    for match in IMAGE.finditer(source):
        alt,target=match.groups()
        if not alt.strip(): print("FAIL: empty alt",target); return 1
        if target.startswith("https://"): src=target
        else:
            local=(SOURCE.parent/target).resolve()
            if not local.is_file(): print("FAIL: missing local asset",target); return 1
            src=local.as_uri()
        before=source[:match.start()].splitlines(); heading=""
        for line in reversed(before[-5:]):
            if line.startswith("**Иллюстрация") or line.startswith("**Illustration"):
                heading=re.sub(r"^\*\*|\*\*$","",line.strip()); break
        blocks.append('<figure><img loading="lazy" decoding="async" src="'+html.escape(src,quote=True)+'" alt="'+html.escape(alt,quote=True)+'"><figcaption>'+html.escape(heading)+'</figcaption></figure>')
    counts=Counter(m.group(2) for m in IMAGE.finditer(source))
    if len(blocks)!=26 or len(counts)!=13 or any(n!=2 for n in counts.values()):
        print(f"FAIL: embeds={len(blocks)}, unique={len(counts)}, frequencies={Counter(counts.values())}"); return 1
    output=Path(sys.argv[1] if len(sys.argv)>1 else "/tmp/geography-chapter-03-preview.html")
    document='''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Chapter 03 visual QA</title><style>
*{box-sizing:border-box}body{margin:0;background:#f2f2ef;color:#18181a;font:16px/1.55 system-ui,sans-serif}header,main{max-width:1100px;margin:auto;padding:20px}h1{font:400 clamp(2rem,5vw,3.5rem) Georgia,serif}.gallery{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}figure{margin:0;padding:12px;background:#fff;border:1px solid #ddd;min-width:0}img{display:block;width:100%;height:auto;max-height:520px;object-fit:contain;background:#f7f7f5}figcaption{font-size:.9rem;color:#444;overflow-wrap:anywhere}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:white;padding:12px;outline:3px solid #287f91}@media(max-width:650px){header,main{padding:14px}.gallery{grid-template-columns:minmax(0,1fr)}}
</style></head><body><a class="skip" href="#visuals">Перейти к визуалам / Skip to visuals</a><header>Atlas of Knowledge · Geography · isolated QA only</header><main><h1>Глава 3 — визуальная проверка / Chapter 3 — visual QA</h1><p>Generated from the bilingual Markdown source; not the production chapter reader.</p><section id="visuals"><div class="gallery">'''+''.join(blocks)+'''</div></section></main></body></html>'''
    output.parent.mkdir(parents=True,exist_ok=True); output.write_text(document,encoding="utf-8")
    print(f"PASS: generated {output}; 26 embeds, 13 unique assets.")
    return 0
if __name__=="__main__": raise SystemExit(main())
