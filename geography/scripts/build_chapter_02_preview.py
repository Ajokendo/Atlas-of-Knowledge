#!/usr/bin/env python3
"""Build an isolated visual QA page from every Chapter 02 Markdown image embed."""
from __future__ import annotations
import html
import re
import sys
from collections import Counter
from pathlib import Path

SOURCE = Path("geography/chapters/02-geographic-envelope.md")
IMAGE = re.compile(r"!\[([^\]]*)\]\((https://[^)\s]+)\)")

def main() -> int:
    if not SOURCE.is_file():
        print("FAIL: missing source:", SOURCE); return 1
    source = SOURCE.read_text(encoding="utf-8")
    blocks = []
    for match in IMAGE.finditer(source):
        alt, url = match.groups()
        if not alt.strip():
            print("FAIL: empty alt text for", url); return 1
        before = source[:match.start()].splitlines()
        heading = ""
        for previous in reversed(before[-5:]):
            if previous.startswith("**Иллюстрация") or previous.startswith("**Figure"):
                heading = re.sub(r"^\*\*|\*\*$", "", previous.strip())
                break
        after = source[match.end():].lstrip().splitlines()
        credit = after[0].strip().strip("*") if after and after[0].lstrip().startswith("*Источник") else ""
        blocks.append(
            '<figure><img loading="lazy" decoding="async" src="' + html.escape(url, quote=True) +
            '" alt="' + html.escape(alt, quote=True) + '" data-source="' + html.escape(url, quote=True) +
            '"><figcaption>' + ('<strong>' + html.escape(heading) + '</strong>' if heading else '') +
            ('<p>' + html.escape(credit) + '</p>' if credit else '') + '</figcaption></figure>'
        )
    counts = Counter(url for _, url in IMAGE.findall(source))
    if len(blocks) != 56 or len(counts) != 28 or any(n != 2 for n in counts.values()):
        print(f"FAIL: embeds={len(blocks)}, unique URLs={len(counts)}, frequencies={sorted(Counter(counts.values()).items())}")
        return 1
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
figcaption p{margin:.4rem 0}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:white;padding:12px;outline:3px solid #287f91}
@media(max-width:650px){header,main{padding:14px}.gallery{grid-template-columns:minmax(0,1fr)}figure{padding:9px}}
</style></head><body><a class="skip" href="#visuals">Перейти к визуалам / Skip to visuals</a>
<header><p>Atlas of Knowledge · Geography · QA only</p></header>
<main><h1>Глава 2 — проверка визуалов / Chapter 2 — visual QA</h1>
<p>Isolated QA harness generated from the source Markdown. It displays all bilingual image embeds together; it is not the production chapter renderer.</p>
<section id="visuals" aria-labelledby="visuals-title"><h2 id="visuals-title">Иллюстрации главы 2 / Chapter 2 figures</h2>
<div class="gallery">""" + "".join(blocks) + """</div></section></main></body></html>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(f"PASS: generated {output}; {len(blocks)} embeds, {len(counts)} unique assets, every URL appears twice.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
