#!/usr/bin/env python3
"""Build a local, full-size gallery for the seven integrated Chapter 07 SVGs."""
from pathlib import Path
import html, re, sys
ROOT=Path(".")
CHAPTER=ROOT/"geography/chapters/07-biosphere-and-natural-biomes.md"
ASSETS=ROOT/"geography/assets/diagrams"
NAMES=[
"07-A-biosphere-earth-spheres-bilingual.svg",
"07-B-food-web-energy-pyramid-bilingual.svg",
"07-D-shelford-tolerance-curve-bilingual.svg",
"07-F-terrestrial-biome-panorama-bilingual.svg",
"07-G-lake-ocean-zonation-bilingual.svg",
"07-H-habitat-connectivity-bilingual.svg",
"07-I-carbon-nitrogen-cycles-bilingual.svg",
]
def main():
    output=Path(sys.argv[1]) if len(sys.argv)>1 else Path("/tmp/geography-chapter-07-preview.html")
    chapter=CHAPTER.read_text(encoding="utf-8")
    embeds=re.findall(r"!\\[([^\\]]*)\\]\\(([^)\\s]+)\\)",chapter)
    alts={}
    for alt,target in embeds:
        alts.setdefault(Path(target).name,[]).append(alt)
    cards=[]
    for name in NAMES:
        path=ASSETS/name
        if not path.is_file(): raise SystemExit(f"Missing SVG: {name}")
        uri=path.resolve().as_uri()
        alt=alts.get(name,["Chapter 07 visual "+name])[0]
        label=name.split("-")[0]+" — "+name.split("-")[1]
        cards.append(f'<article><h2>{html.escape(label)}</h2><p>{html.escape(name)}</p><img src="{uri}" alt="{html.escape(alt, quote=True)}"></article>')
    output.write_text("""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Chapter 07 visual QA</title><style>
body{font:16px/1.45 system-ui,sans-serif;margin:0;padding:16px;background:#f3f5f7;color:#17212b}
main{max-width:1200px;margin:auto}h1{font-size:1.6rem}article{background:white;border:1px solid #ccd3da;border-radius:10px;padding:14px;margin:18px 0;overflow:hidden}
article img{display:block;width:100%;height:auto;object-fit:contain}article h2{font-size:1.1rem;margin:0 0 4px}article p{font-size:.8rem;color:#46515c;margin:0 0 10px}
</style><main><h1>Chapter 07 — full-size visual review</h1>"""+"".join(cards)+"</main></html>",encoding="utf-8")
    print(f"Built {output} with {len(cards)} full-size SVGs.")
if __name__=="__main__": main()
