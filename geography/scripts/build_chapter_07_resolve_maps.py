#!/usr/bin/env python3
"""Build bilingual Chapter 07 biome and biogeographical-realm maps from RESOLVE 2017.

The source is fetched from the public ArcGIS FeatureServer. Geometry is simplified
by the service for legibility; all category attributes are retained. Outputs are
original SVG renderings of CC BY 4.0 source geometry and carry attribution.
"""
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import json, html, math, sys

ENDPOINT = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/Resolve_Ecoregions/FeatureServer/0/query"
OUT = Path("geography/assets/diagrams")
W, H = 1800, 1080
MAP = (55, 55, 1260, 760)
LEGEND_X, LEGEND_Y = 1350, 105
BIOMES = [
 ("Tropical & Subtropical Moist Broadleaf Forests","Влажные тропические и субтропические широколиственные леса","#167a45"),
 ("Tropical & Subtropical Dry Broadleaf Forests","Сухие тропические и субтропические широколиственные леса","#a6a63c"),
 ("Tropical & Subtropical Coniferous Forests","Тропические и субтропические хвойные леса","#69a85c"),
 ("Temperate Broadleaf & Mixed Forests","Умеренные широколиственные и смешанные леса","#26734d"),
 ("Temperate Conifer Forests","Умеренные хвойные леса","#7b9b72"),
 ("Boreal Forests/Taiga","Бореальные леса / тайга","#4f7f9d"),
 ("Tropical & Subtropical Grasslands, Savannas & Shrublands","Тропические и субтропические луга, саванны и кустарники","#d58a32"),
 ("Temperate Grasslands, Savannas & Shrublands","Умеренные луга, саванны и кустарники","#d6bd58"),
 ("Flooded Grasslands & Savannas","Затопляемые луга и саванны","#7bb7c8"),
 ("Montane Grasslands & Shrublands","Горные луга и кустарники","#b59b70"),
 ("Tundra","Тундра","#9bb7ad"),
 ("Mediterranean Forests, Woodlands & Scrub","Средиземноморские леса, редколесья и кустарники","#b66a58"),
 ("Deserts & Xeric Shrublands","Пустыни и ксерофитные кустарники","#c58a57"),
 ("Mangroves","Мангровые леса","#55a9a0"),
]
REALMS = [
 ("Afrotropic","Афротропическая область","#d77a52"),
 ("Antarctic","Антарктическая область","#d8e6ed"),
 ("Australasia","Австралазийская область","#7d9c63"),
 ("Indomalayan","Индомалайская область","#c2a44b"),
 ("Nearctic","Неарктическая область","#6596b5"),
 ("Neotropic","Неотропическая область","#8e75ad"),
 ("Oceania","Океанийская область","#d48bb0"),
 ("Palearctic","Палеарктическая область","#70a58c"),
]
def fetch():
    params = {
      "where":"1=1", "outFields":"BIOME_NAME,REALM", "returnGeometry":"true",
      "geometryPrecision":"2", "maxAllowableOffset":"0.12", "outSR":"4326",
      "returnTrueCurves":"false", "f":"geojson", "resultRecordCount":"2000"
    }
    url = ENDPOINT + "?" + urlencode(params)
    with urlopen(url, timeout=90) as response:
        data=json.loads(response.read().decode("utf-8"))
    if data.get("error"): raise RuntimeError(data["error"])
    features=data.get("features",[])
    if len(features)<800: raise RuntimeError(f"Expected ~846 RESOLVE ecoregions; received {len(features)}")
    return features

def path_for_ring(ring, box):
    x0,y0,w,h=box
    points=[]
    for lon,lat,*_ in ring:
        # Equirectangular world view. Source coordinates are WGS84 lon/lat.
        x=x0+(lon+180)/360*w
        y=y0+(90-lat)/180*h
        points.append((x,y))
    if len(points)<3: return ""
    return "M"+" L".join(f"{x:.1f},{y:.1f}" for x,y in points)+" Z"

def paths(geometry,box):
    if not geometry: return []
    typ=geometry.get("type"); coords=geometry.get("coordinates",[])
    polys = [coords] if typ=="Polygon" else coords if typ=="MultiPolygon" else []
    out=[]
    for poly in polys:
        if not poly: continue
        # Outer ring only: holes are omitted deliberately at this teaching scale.
        p=path_for_ring(poly[0],box)
        if p: out.append(p)
    return out

def svg_map(features, mode, outpath):
    palette=BIOMES if mode=="biome" else REALMS
    key="BIOME_NAME" if mode=="biome" else "REALM"
    lookup={en:(ru,color) for en,ru,color in palette}
    unknown=Counter((f.get("properties") or {}).get(key,"UNCLASSIFIED") for f in features)
    unknown_names=[n for n in unknown if n not in lookup]
    if unknown_names: raise RuntimeError(f"Unmapped {key} categories: {unknown_names}")
    title_en="World terrestrial biomes — RESOLVE Ecoregions 2017" if mode=="biome" else "World biogeographical realms — RESOLVE Ecoregions 2017"
    title_ru="Наземные биомы мира — RESOLVE Ecoregions 2017" if mode=="biome" else "Биогеографические области мира — RESOLVE Ecoregions 2017"
    desc="Simplified teaching map of 846 terrestrial ecoregions grouped into 14 biomes." if mode=="biome" else "Simplified teaching map of terrestrial ecoregions grouped into eight biogeographical realms."
    x0,y0,mw,mh=MAP
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">']
    parts += [f'<title id="title">{html.escape(title_ru)} / {html.escape(title_en)}</title>',f'<desc id="desc">{html.escape(desc)} Русская и английская легенды приведены справа. Границы являются классификационными, а не политическими.</desc>']
    parts += ['<rect width="100%" height="100%" fill="#f5f8fa"/>',
      '<text x="60" y="38" font-family="Arial,sans-serif" font-size="23" font-weight="bold" fill="#183044">'+html.escape(title_ru)+'</text>',
      '<text x="60" y="68" font-family="Arial,sans-serif" font-size="19" fill="#355166">'+html.escape(title_en)+'</text>',
      f'<rect x="{x0}" y="{y0}" width="{mw}" height="{mh}" fill="#e8f1f4" stroke="#647b87" stroke-width="1.5"/>']
    # Subtle graticule.
    for lon in range(-120,181,60):
        x=x0+(lon+180)/360*mw
        parts.append(f'<path d="M{x:.1f},{y0} V{y0+mh}" stroke="#c8d5da" stroke-width="1" stroke-dasharray="4 6"/>')
    for lat in [-60,-30,0,30,60]:
        y=y0+(90-lat)/180*mh
        parts.append(f'<path d="M{x0},{y:.1f} H{x0+mw}" stroke="#c8d5da" stroke-width="1" stroke-dasharray="4 6"/>')
    for f in features:
        props=f.get("properties") or {}
        name=props.get(key)
        color=lookup[name][1]
        for d in paths(f.get("geometry"),MAP):
            parts.append(f'<path d="{d}" fill="{color}" stroke="#465b62" stroke-width="0.45" stroke-linejoin="round"/>')
    parts += ['<text x="70" y="840" font-family="Arial,sans-serif" font-size="15" fill="#526773">180°W</text>',
      '<text x="650" y="840" font-family="Arial,sans-serif" font-size="15" text-anchor="middle" fill="#526773">0°</text>',
      '<text x="1270" y="840" font-family="Arial,sans-serif" font-size="15" text-anchor="end" fill="#526773">180°E</text>']
    parts.append(f'<text x="{LEGEND_X}" y="58" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="#183044">Легенда / Legend</text>')
    row=42 if len(palette)>9 else 62
    for i,(en,ru,color) in enumerate(palette):
        y=LEGEND_Y+i*row
        parts.append(f'<rect x="{LEGEND_X}" y="{y}" width="24" height="24" rx="3" fill="{color}" stroke="#45545a"/>')
        parts.append(f'<text x="{LEGEND_X+36}" y="{y+11}" font-family="Arial,sans-serif" font-size="15" fill="#183044">{html.escape(ru)}</text>')
        parts.append(f'<text x="{LEGEND_X+36}" y="{y+29}" font-family="Arial,sans-serif" font-size="13" fill="#405966">{html.escape(en)}</text>')
    note_y=LEGEND_Y+len(palette)*row+26
    note_ru="Классификация наземных экорегионов; не карта современного землепользования."
    note_en="A reference classification of terrestrial ecoregions; not a current land-cover map."
    parts += [f'<text x="{LEGEND_X}" y="{note_y}" font-family="Arial,sans-serif" font-size="13" fill="#183044">{html.escape(note_ru)}</text>',
      f'<text x="{LEGEND_X}" y="{note_y+22}" font-family="Arial,sans-serif" font-size="12" fill="#405966">{html.escape(note_en)}</text>',
      '<text x="60" y="900" font-family="Arial,sans-serif" font-size="14" fill="#263e4b">Источник данных / Data: RESOLVE Ecoregions 2017; Dinerstein et al. (2017), BioScience 67(6): 534–545. DOI: 10.1093/biosci/bix014.</text>',
      '<text x="60" y="925" font-family="Arial,sans-serif" font-size="14" fill="#263e4b">Данные / Data licence: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/ . Карта создана Atlas of Knowledge; геометрия упрощена для учебного масштаба.</text>',
      '<text x="60" y="950" font-family="Arial,sans-serif" font-size="14" fill="#263e4b">This derivative map is attributed to RESOLVE / Dinerstein et al. and is distributed under CC BY 4.0.</text>',
      '<text x="60" y="985" font-family="Arial,sans-serif" font-size="13" fill="#526773">Восемь биогеографических областей / Eight realms.</text>' if mode=="realm" else '<text x="60" y="985" font-family="Arial,sans-serif" font-size="13" fill="#526773">Четырнадцать биомов / Fourteen biomes.</text>',
      '</svg>']
    outpath.write_text("\n".join(parts),encoding="utf-8")

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    raw_features=fetch()
    # RESOLVE includes one N/A Rock & Ice record; it is not one of the 14 classified biomes.
    # Exclude records without both classification fields rather than inventing a 15th category.
    biome_names={item[0] for item in BIOMES}
    realm_names={item[0] for item in REALMS}
    features=[f for f in raw_features if (f.get("properties") or {}).get("BIOME_NAME") in biome_names and (f.get("properties") or {}).get("REALM") in realm_names]
    excluded=len(raw_features)-len(features)
    biome_counts=Counter((f.get("properties") or {}).get("BIOME_NAME") for f in features)
    realm_counts=Counter((f.get("properties") or {}).get("REALM") for f in features)
    if len(biome_counts)!=14: raise RuntimeError(f"Expected 14 biome categories, got {len(biome_counts)}: {biome_counts}")
    if len(realm_counts)!=8: raise RuntimeError(f"Expected 8 realm categories, got {len(realm_counts)}: {realm_counts}")
    svg_map(features,"biome",OUT/"07-C-world-terrestrial-biomes-bilingual.svg")
    svg_map(features,"realm",OUT/"07-E-world-biogeographical-realms-bilingual.svg")
    print(f"PASS: generated 07-C and 07-E from {len(features)} classified RESOLVE 2017 ecoregions; 14 biomes and 8 realms; excluded {excluded} unclassified record(s).")
    print("Source geometry simplified by ArcGIS maxAllowableOffset=0.12 degrees; attribution and CC BY 4.0 embedded in both maps.")
if __name__=="__main__": main()
