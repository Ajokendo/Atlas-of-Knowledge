#!/usr/bin/env python3
"""Build a full-size Chapter 08 gallery with six inline SVGs and the ISRIC map."""
from pathlib import Path
import html
import sys

ASSETS = Path("geography/assets/diagrams")
NAMES = [
    ("08-A", "08-A-soil-profile-horizons-bilingual.svg", "Original SVG"),
    ("08-C", "08-C-soil-degradation-processes-bilingual.svg", "Original SVG"),
    ("08-D", "08-D-soil-earth-spheres-interface-bilingual.svg", "Original SVG"),
    ("08-E", "08-E-soil-forming-factors-bilingual.svg", "Original SVG"),
    ("08-F", "08-F-landscape-morphology-block-bilingual.svg", "Original SVG"),
    ("08-G", "08-G-landscape-mosaic-patches-corridors-matrix-bilingual.svg", "Original SVG"),
]
MAP_URL = "https://files.isric.org/public/WRB/wrb2014.png"

def main():
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/geography-chapter-08-preview.html")
    cards = []
    for visual_id, filename, kind in NAMES:
        path = ASSETS / filename
        if not path.is_file():
            raise SystemExit(f"Missing SVG: {filename}")
        svg = path.read_text(encoding="utf-8")
        cards.append(
            f'<article data-visual="{visual_id}"><h2>{visual_id}</h2>'
            f'<p>{html.escape(filename)} · {kind}</p>{svg}</article>'
        )
    cards.insert(1,
        '<article data-visual="08-B"><h2>08-B — ISRIC WRB 2014 map</h2>'
        '<p>Third-party raster map, reproduced unchanged; open the full poster for the small legend.</p>'
        f'<img class="map" src="{MAP_URL}" alt="ISRIC global soil map according to WRB 2014"></article>'
    )
    output.write_text("""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chapter 08 visual QA</title><style>
*{box-sizing:border-box}body{font:16px/1.45 system-ui,sans-serif;margin:0;padding:16px;background:#f3f5f7;color:#17212b}
main{max-width:1200px;margin:auto}h1{font-size:1.6rem}article{background:white;border:1px solid #ccd3da;border-radius:10px;padding:14px;margin:18px 0;overflow:hidden}
article svg,article img{display:block;width:100%;height:auto}article svg{overflow:visible}article h2{font-size:1.1rem;margin:0 0 4px}article p{font-size:.8rem;color:#46515c;margin:0 0 10px}
.note{background:#fff4d6;padding:10px;border-radius:6px}
</style></head><body><main><h1>Chapter 08 — full-size visual review</h1>
<p class="note">The ISRIC map is a WRB 2014 overview, not a WRB 2022 map. Its legend is too small for comfortable reading at phone width; use the linked full poster.</p>"""+"".join(cards)+"</main></body></html>", encoding="utf-8")
    print(f"Built {output} with {len(cards)} visual assets (6 SVGs + 1 raster map).")

if __name__ == "__main__":
    main()
