#!/usr/bin/env python3
"""Chapter 07 bilingual image inventory and SVG structural acceptance."""
from collections import Counter, defaultdict
from pathlib import Path
import re, sys, xml.etree.ElementTree as ET
CHAPTER=Path("geography/chapters/07-biosphere-and-natural-biomes.md")
ASSETS=Path("geography/assets/diagrams")
EXPECTED={
"07-A-biosphere-earth-spheres-bilingual.svg",
"07-B-food-web-energy-pyramid-bilingual.svg",
"07-D-shelford-tolerance-curve-bilingual.svg",
"07-F-terrestrial-biome-panorama-bilingual.svg",
"07-G-lake-ocean-zonation-bilingual.svg",
"07-H-habitat-connectivity-bilingual.svg",
"07-I-carbon-nitrogen-cycles-bilingual.svg",
}
IMAGE=re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
def main():
 errors=[]
 if not CHAPTER.is_file(): print("FAIL: Chapter 07 file missing"); return 1
 source=CHAPTER.read_text(encoding="utf-8")
 embeds=IMAGE.findall(source)
 counts=Counter(Path(target).name for _,target in embeds)
 if len(embeds)!=14 or set(counts)!=EXPECTED or any(v!=2 for v in counts.values()):
  errors.append(f"expected 14 RU/EN embeds across 7 paired SVGs; found {len(embeds)} embeds and {len(counts)} targets")
 if any(not alt.strip() for alt,_ in embeds): errors.append("empty Markdown alt text")
 by_target=defaultdict(list)
 for alt,target in embeds: by_target[Path(target).name].append(alt)
 for name,alts in by_target.items():
  if len(alts)==2 and not (any(re.search(r"[А-Яа-яЁё]",a) for a in alts) and any(re.search(r"[A-Za-z]",a) for a in alts)):
   errors.append(name+": Russian/English alt-text pair not evident")
 for ident in ["07-A","07-B","07-D","07-F","07-G","07-H","07-I"]:
  if f"IMAGE PLACEHOLDER {ident}" in source or f"МЕТКА ИЛЛЮСТРАЦИИ {ident}" in source:
   errors.append(ident+": integrated visual still has a placeholder marker")
 for ident in ["07-C","07-E"]:
  if f"IMAGE PLACEHOLDER {ident}" not in source and f"МЕТКА ИЛЛЮСТРАЦИИ {ident}" not in source:
   errors.append(ident+": planned map gap marker unexpectedly missing")
 chapter_lines=source.splitlines()
 for figure in ["7.1","7.3","7.6","7.7","7.8","7.9"]:
  idx=next((i for i,line in enumerate(chapter_lines) if line.startswith(f"**Рисунок {figure} / Figure")),None)
  if idx is not None:
   following=chapter_lines[idx+1:idx+4]
   if any(line.startswith("Техническое задание:") or line.startswith("**EN production brief:**") for line in following):
    errors.append(f"Figure {figure}: stale production brief remains after integration")
 ns="{http://www.w3.org/2000/svg}"
 for name in sorted(EXPECTED):
  path=ASSETS/name
  if not path.is_file(): errors.append(f"missing SVG: {name}"); continue
  try: root=ET.parse(path).getroot()
  except ET.ParseError as exc: errors.append(f"{name}: invalid XML: {exc}"); continue
  children=list(root)
  ids=[node.attrib["id"] for node in root.iter() if "id" in node.attrib]
  title=next((n for n in children if n.tag==ns+"title"),None)
  desc=next((n for n in children if n.tag==ns+"desc"),None)
  if root.tag!=ns+"svg": errors.append(f"{name}: wrong root")
  if title is None or not (title.text or "").strip(): errors.append(f"{name}: title missing")
  if desc is None or not (desc.text or "").strip(): errors.append(f"{name}: description missing")
  if root.attrib.get("role")!="img": errors.append(f"{name}: role=img missing")
  if len(ids)!=len(set(ids)): errors.append(f"{name}: duplicate IDs")
  refs=root.attrib.get("aria-labelledby","").split()
  if not refs or any(x not in set(ids) for x in refs): errors.append(f"{name}: aria-labelledby broken")
  if any(n.tag in (ns+"script",ns+"foreignObject") for n in root.iter()): errors.append(f"{name}: script/foreignObject found")
 if errors:
  for e in errors: print("FAIL:",e)
  return 1
 print("PASS: 14 RU/EN image embeds; 7 SVG targets paired exactly twice; bilingual alt text; 7 valid SVGs with title/description/ARIA and unique IDs; 07-C and 07-E remain explicit map gaps; no stale briefs for integrated figures.")
 print("NOTE: rendered layout, screen-reader experience, project licensing and deployed-site QA are separate.")
 return 0
if __name__=="__main__": sys.exit(main())
