#!/usr/bin/env python3
"""Static Chapter 06 bilingual image inventory and SVG XML/ARIA validation."""
from __future__ import annotations
import re, sys, xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

CHAPTER = Path("geography/chapters/06-hydrosphere-and-world-ocean.md")
ASSETS = Path("geography/assets")
LICENSE_NOTICE = ASSETS / "CHAPTER_06_ASSET_LICENSE.md"
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
EXPECTED_SVG = {
    "06-4-C-ocean-floor-cross-section-bilingual.svg",
    "06-5-A-seawater-temperature-salinity-profiles-bilingual.svg",
    "06-6-D-ocean-motion-bilingual.svg",
    "06-7-A-deep-ocean-circulation-schematic-bilingual.svg",
    "06-9-A-marine-zones-bilingual.svg",
    "06-11-A-ocean-pollution-pathways-bilingual.svg",
    "06-12-A-cryosphere-components-bilingual.svg",
    "06-13-A-river-basin-anatomy-bilingual.svg",
    "06-14-A-lake-types-structure-bilingual.svg",
    "06-15-A-groundwater-system-bilingual.svg",
    "06-17-A-climate-water-cycle-bilingual.svg",
    "06-18-A-catchment-exercise-bilingual.svg",
}
def main() -> int:
    errors=[]
    if not CHAPTER.is_file():
        print("FAIL: chapter file missing"); return 1
    source=CHAPTER.read_text(encoding="utf-8")
    embeds=IMAGE.findall(source)
    counts=Counter(target for _,target in embeds)
    print(f"Markdown embeds={len(embeds)}; unique targets={len(counts)}")
    if len(embeds)!=32 or len(counts)!=16 or any(n!=2 for n in counts.values()):
        errors.append("expected 32 bilingual embeds / 16 unique targets, each target paired exactly twice")
    if any(not alt.strip() for alt,_ in embeds):
        errors.append("empty alt text found")
    local={Path(urlparse(target).path).name for _,target in embeds if target.startswith("../assets/")}
    if local!=EXPECTED_SVG:
        errors.append(f"local SVG inventory mismatch; expected {len(EXPECTED_SVG)}, found {len(local)}")
    if not LICENSE_NOTICE.is_file():
        errors.append("Chapter 06 local-SVG licence notice missing")
    else:
        notice=LICENSE_NOTICE.read_text(encoding="utf-8")
        if "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)" not in notice:
            errors.append("Chapter 06 licence notice does not declare CC BY-NC 4.0")
        missing=[name for name in EXPECTED_SVG if f"`{name}`" not in notice]
        if missing:
            errors.append("Chapter 06 licence notice omits scoped SVGs: "+", ".join(sorted(missing)))
        if "6-B" not in notice or "CC BY-SA 3.0" not in notice or "NOAA/AOML" not in notice:
            errors.append("Chapter 06 licence notice must preserve separate third-party rights")
    for name in sorted(EXPECTED_SVG):
        path=ASSETS/name
        if not path.is_file():
            errors.append(f"missing SVG: {name}"); continue
        try:
            root=ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{name}: invalid XML: {exc}"); continue
        ns="{http://www.w3.org/2000/svg}"
        children=list(root)
        ids=[node.attrib["id"] for node in root.iter() if "id" in node.attrib]
        title=next((node for node in children if node.tag==ns+"title"),None)
        desc=next((node for node in children if node.tag==ns+"desc"),None)
        if root.tag!=ns+"svg": errors.append(f"{name}: root is not SVG")
        if title is None or not (title.text or "").strip(): errors.append(f"{name}: missing title")
        elif children and children[0] is not title: errors.append(f"{name}: title is not first child")
        if desc is None or not (desc.text or "").strip(): errors.append(f"{name}: missing description")
        if root.attrib.get("role")!="img": errors.append(f"{name}: role=img missing")
        if len(ids)!=len(set(ids)): errors.append(f"{name}: duplicate IDs")
        refs=root.attrib.get("aria-labelledby","").split()
        if not refs or any(ref not in set(ids) for ref in refs): errors.append(f"{name}: broken aria-labelledby")
        if any(node.tag in (ns+"script",ns+"foreignObject") for node in root.iter()):
            errors.append(f"{name}: script/foreignObject element found")
    if errors:
        for error in errors: print("FAIL:",error)
        return 1
    print(f"PASS: 32 bilingual embeds; 16 paired targets; all {len(EXPECTED_SVG)} SVG files parse as XML and pass title/description/ARIA/ID checks; all alt text non-empty; exact CC BY-NC 4.0 licence scope covers all 12 local SVGs and excludes third-party assets.")
    print("NOTE: this is static QA only; rendered contrast, screen-reader output, browser/mobile and deployed-site checks are separate.")
    return 0
if __name__=="__main__":
    sys.exit(main())
