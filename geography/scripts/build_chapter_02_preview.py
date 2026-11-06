#!/usr/bin/env python3
"""Build a temporary, isolated browser-QA preview of Chapter 02 figures."""
from __future__ import annotations
import html
import re
import sys
from pathlib import Path

SOURCE = Path("geography/chapters/02-geographic-envelope.md")
IMAGE = re.compile(r"!\[([^\]]*)\]\((https://[^)\s]+)\)")
SPLIT = "# Chapter 2. Earth's Geographic Envelope"

def section(title: str, source: str) -> str:
    blocks = []
    lines = source.splitlines()
    for i, line in enumerate(lines):
        match = IMAGE.search(line)
        if not match:
            continue
        alt, url = match.groups()
        heading = ""
        for previous in reversed(lines[max(0, i-4):i]):
            if previous.startswith("**Иллюстрация") or previous.startswith("**Figure"):
                heading = re.sub(r"^\*\*|\*\*$", "", previous.strip())
                break
        credit = ""
        if i + 1 < len(lines) and lines[i+1].lstrip().startswith("*Источник"):
            credit = lines[i+1].strip().strip("*")
        blocks.append(
            '<figure><img loading="lazy" decoding="async" src="' + html.escape(url, quote=True) +
            '" alt="' + html.escape(alt, quote=True) + '"><figcaption>' +
            ('<strong>' + html.escape(heading) + '</strong>' if heading else '') +
            ('<p>' + html.escape(credit) + '</p>' if credit else '') +
            '</figcaption></figure>'
        )
    return '<section><h2>' + html.escape(title) + '</h2><div class="gallery">' + "".join(blocks) + '</div></section>'

def main() -> int:
    if not SOURCE.is_file():
        print("Missing source:", SOURCE); return 1
    text = SOURCE.read_text(encoding="utf-8")
    if SPLIT not in text:
        print("Could not locate English section marker"); return 1
    ru, en = text.split(SPLIT, 1)
    ru_html = section("Русская версия · визуалы главы 2", ru)
    en_html = section("English version · Chapter 2 visuals", en)
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/geography-chapter-02-preview.html")
    document = """<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chapter 02 — isolated visual QA preview</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f2f2ef;color:#18181a;font:16px/1.55 system-ui,sans-serif}
header,main{max-width:1100px;margin:auto;padding:20px}header{border-bottom:1px solid #ccc}
h1,h2{font-family:Georgia,serif;font-weight:400}h1{font-size:clamp(2rem,5vw,3.5rem)}
.gallery{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
figure{margin:0;padding:12px;background:#fff;border:1px solid #ddd;min-width:0}
img{display:block;width:100%;height:auto;max-height:520px;object-fit:contain;background:#f7f7f5}
figcaption{font-size:.88rem;color:#555;overflow-wrap:anywhere}figcaption strong{display:block;color:#222;margin:.6rem 0}
figcaption p{margin:.4rem 0}
a:focus-visible,button:focus-visible{outline:3px solid #287f91;outline-offset:3px}
button{padding:9px 14px;font:inherit}
@media(max-width:650px){header,main{padding:14px}.gallery{grid-template-columns:minmax(0,1fr)}figure{padding:9px}}
</style></head><body><header><p>Atlas of Knowledge · Geography · QA only</p>
<button id="lang" type="button" aria-pressed="false">Показать English</button></header>
<main><h1>Глава 2 — проверка визуалов / Chapter 2 — visual QA</h1>
<p>Temporary test harness generated from the source Markdown. This is not the production chapter renderer.</p>
<div id="ru">""" + ru_html + """</div><div id="en" hidden>""" + en_html + """</div></main>
<script>
const b=document.querySelector('#lang'),ru=document.querySelector('#ru'),en=document.querySelector('#en');
b.addEventListener('click',()=>{const show=en.hidden;en.hidden=!show;ru.hidden=show;
document.documentElement.lang=show?'en':'ru';b.setAttribute('aria-pressed',String(show));
b.textContent=show?'Показать русский':'Показать English';});
</script></body></html>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(f"Preview generated: {output}; RU images={len(IMAGE.findall(ru))}; EN images={len(IMAGE.findall(en))}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
