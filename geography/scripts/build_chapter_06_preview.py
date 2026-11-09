#!/usr/bin/env python3
"""Build an isolated Chapter 06 visual gallery from the bilingual Markdown source."""
from __future__ import annotations
import html, re, sys
from pathlib import Path
from urllib.parse import urlparse

CHAPTER = Path("geography/chapters/06-hydrosphere-and-world-ocean.md")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
BASE = "https://raw.githubusercontent.com/Ajokendo/Atlas-of-Knowledge/workspace/geography/geography/"

def main() -> int:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/geography-chapter-06-preview.html")
    source = CHAPTER.read_text(encoding="utf-8")
    seen = set()
    cards = []
    embeds = IMAGE.findall(source)
    for alt, target in embeds:
        seen.add(target)
        if target.startswith("../assets/"):
            src = BASE + "assets/" + Path(urlparse(target).path).name
        elif target.startswith("http://") or target.startswith("https://"):
            src = target
        else:
            raise SystemExit(f"Unsupported Chapter 06 image target: {target}")
        cards.append(f'<figure><img src="{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}" loading="eager"><figcaption>{html.escape(alt)}</figcaption></figure>')
    if len(embeds) != 32 or len(seen) != 16 or len(cards) != 32:
        raise SystemExit(f"Expected 32 bilingual embeds and 16 unique targets; got {len(embeds)}, {len(seen)} and {len(cards)}")
    document = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Geography Chapter 06 visual QA</title><style>
*{box-sizing:border-box}body{font:16px/1.5 system-ui,sans-serif;margin:0;padding:1rem;color:#17212b;background:#fff}a:focus,img:focus{outline:3px solid #1459a6;outline-offset:3px}.skip{display:inline-block;padding:.6rem 1rem}main{max-width:1200px;margin:auto}h1{font-size:1.5rem}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:1rem}figure{margin:0;border:1px solid #9aa6b2;padding:.75rem;border-radius:.5rem;min-width:0}img{display:block;width:100%;height:auto;max-height:560px;object-fit:contain}figcaption{font-size:.9rem;margin-top:.5rem;overflow-wrap:anywhere}</style></head><body><a class="skip" href="#visuals">Skip to visuals</a><main><h1>Chapter 06 — unique visual targets</h1><p>Isolated source-image gallery for automated visual QA. It is not the production chapter layout.</p><section id="visuals" class="gallery" aria-label="Chapter 06 visual assets">""" + "".join(cards) + """</section></main></body></html>"""
    output.write_text(document, encoding="utf-8")
    print(f"Built {output}: {len(cards)} bilingual image embeds, {len(seen)} unique targets.")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
