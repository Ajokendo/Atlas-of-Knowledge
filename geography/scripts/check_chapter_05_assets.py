#!/usr/bin/env python3
"""Static Chapter 05 image inventory, SVG structure, and licence-scope checks."""
from __future__ import annotations
import re, sys, xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
BS=chr(92)
CHAPTER=Path("geography/chapters/05-atmosphere-and-climatology.md")
LICENSE=Path("geography/assets/CHAPTER_05_ASSET_LICENSE.md")
VISUALS=Path("geography/visuals")
IMAGE=re.compile("!"+BS+"[([^]]*)"+BS+"]"+BS+"(([^)"+BS+"s]+)"+BS+")")
SVG_NAMES=[
"chapter-05-dry-air-composition.svg","chapter-05-atmosphere-layers-bilingual.svg",
"chapter-05-weather-vs-climate.svg","chapter-05-climate-controls.svg",
"chapter-05-global-climate-belts.svg","chapter-05-urban-microclimate-heat-island.svg",
"chapter-05-atmospheric-hazards.svg","chapter-05-climate-change-drivers-evidence-responses.svg",
"chapter-05-weather-observations-to-forecast.svg","chapter-05-climate-diagram-exercise.svg",
"chapter-05-synoptic-map-climate-analysis.svg","chapter-05-cloud-formation-processes.svg"]
ORIGINALS=set(SVG_NAMES)-{"chapter-05-cloud-formation-processes.svg"}
NOAA_NAMES=["noaa-global-atmospheric-circulation.jpg","noaa-hydrologic-cycle.jpg","noaa-cold-front-symbol.png","noaa-warm-front-symbol.png","noaa-stationary-front-symbol.png","noaa-occluded-front-symbol.png","noaa-cold-occlusion-cross-section.png"]
def main():
    errors=[]
    if not CHAPTER.is_file() or not LICENSE.is_file():
        print("FAIL: chapter or licence notice missing"); return 1
    source=CHAPTER.read_text(encoding="utf-8")
    embeds=IMAGE.findall(source); counts=Counter(target for _,target in embeds)
    print(f"Embeds={len(embeds)}; unique targets={len(counts)}")
    if len(embeds)!=46 or len(counts)!=23 or any(n!=2 for n in counts.values()):
        errors.append("expected 46 bilingual embeds, 23 unique targets, each paired twice")
    if any(not alt.strip() for alt,_ in embeds): errors.append("empty alt text found")
    if any(not target.startswith(("https://","../visuals/","../assets/chapter-05-noaa/")) for _,target in embeds): errors.append("unexpected image URL/path")
    local={Path(urlparse(target).path).name for _,target in embeds if target.startswith("../visuals/") or "/geography/visuals/" in target}
    if local!=set(SVG_NAMES): errors.append(f"local SVG inventory mismatch: expected {len(SVG_NAMES)}, found {len(local)}")
    local_noaa={Path(urlparse(target).path).name for _,target in embeds if target.startswith("../assets/chapter-05-noaa/")}
    if local_noaa!=set(NOAA_NAMES): errors.append(f"local NOAA mirror inventory mismatch: expected {len(NOAA_NAMES)}, found {len(local_noaa)}")
    for name in NOAA_NAMES:
        asset=Path("geography/assets/chapter-05-noaa")/name
        if not asset.is_file(): errors.append(f"missing local NOAA mirror: {name}")
        elif asset.stat().st_size==0: errors.append(f"empty local NOAA mirror: {name}")
    for name in SVG_NAMES:
        path=VISUALS/name
        if not path.is_file(): errors.append(f"missing SVG {name}"); continue
        try:
            root=ET.parse(path).getroot(); ns="{http://www.w3.org/2000/svg}"; children=list(root)
            ids=[node.attrib["id"] for node in root.iter() if "id" in node.attrib]
            title=next((x for x in children if x.tag==ns+"title"),None)
            desc=next((x for x in children if x.tag==ns+"desc"),None)
            if root.tag!=ns+"svg": errors.append(f"{name}: root is not SVG")
            if title is None or not (title.text or "").strip(): errors.append(f"{name}: missing title")
            elif children and children[0] is not title: errors.append(f"{name}: title not first child")
            if desc is None or not (desc.text or "").strip(): errors.append(f"{name}: missing description")
            if root.attrib.get("role")!="img": errors.append(f"{name}: role=img missing")
            if len(ids)!=len(set(ids)): errors.append(f"{name}: duplicate IDs")
            refs=root.attrib.get("aria-labelledby","").split()
            if not refs or any(ref not in set(ids) for ref in refs): errors.append(f"{name}: broken aria-labelledby")
            if any(node.tag in (ns+"script",ns+"foreignObject") for node in root.iter()): errors.append(f"{name}: script/foreignObject found")
        except ET.ParseError as exc: errors.append(f"{name}: invalid XML: {exc}")
    licence=LICENSE.read_text(encoding="utf-8")
    listed=set()
    for line in licence.splitlines():
        if line[:1].isdigit() and ". " in line:
            listed.update(name for name in ORIGINALS if name in line)
    if listed!=ORIGINALS: errors.append(f"licence list is not exactly 11 originals (found {len(listed)})")
    if "chapter-05-cloud-formation-processes.svg" in listed: errors.append("adapted 5.7-B incorrectly included in CC BY-NC list")
    if "CC BY-SA 4.0" not in licence or "5.7-B" not in licence: errors.append("5.7-B CC BY-SA exclusion missing")
    if errors:
        for item in errors: print("FAIL:",item)
        return 1
    print(f"PASS: 46 embeds; 23 paired targets; {len(SVG_NAMES)}/12 SVG XML/ARIA checks; {len(NOAA_NAMES)}/7 unchanged NOAA mirrors present; exact 11-original CC BY-NC scope; 5.7-B excluded.")
    return 0
if __name__=="__main__": sys.exit(main())
