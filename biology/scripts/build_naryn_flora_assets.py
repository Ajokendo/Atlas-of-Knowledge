#!/usr/bin/env python3
"""Acquire and verify three selected Naryn flora and habitat photographs."""
from __future__ import annotations
import hashlib, json, pathlib, time, urllib.error, urllib.parse, urllib.request
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "biology" / "images" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
UA = "AtlasOfKnowledge-BiologyAssetBuilder/1.0 (educational project; source attribution in manifest)"
ITEMS = [
 {"commons_title":"Chatyr kul lake.JPG","output":"flora-naryn-chatyr.webp","subject":"Chatyr-Kul high-altitude lake shore","author":"Nurdjen","date":"2006-07","location":"Chatyr-Kul, Naryn Region, Kyrgyzstan","license":"Public domain dedication (PD-self)","page":"https://commons.wikimedia.org/wiki/File:Chatyr_kul_lake.JPG","dimensions":[2816,2120]},
 {"commons_title":"Son-Kul, Kyrgyzstan (44623421951).jpg","output":"flora-naryn-songkul.webp","subject":"Son-Kul lakeshore meadow","author":"Ninara","date":"2018-07-16","location":"Son-Kul, Naryn Region, Kyrgyzstan","license":"CC BY 2.0","page":"https://commons.wikimedia.org/wiki/File:Son-Kul,_Kyrgyzstan_(44623421951).jpg","dimensions":[3240,2160]},
 {"commons_title":"Clematis songorica.jpg","output":"flora-naryn-clematis.webp","subject":"Flowering Clematis songorica in a rocky-clay floodplain","taxon":"Clematis songorica","author":"Alexey Yakovlev","date":"2026-07-11","location":"Tributary of the Alabuga River, 4 km south of Dzherge-Tal, Ak-Tala District, Naryn Region, Kyrgyzstan; 2,400 m a.s.l.","license":"CC0 1.0","page":"https://commons.wikimedia.org/wiki/File:Clematis_songorica.jpg","dimensions":[1400,933]},
]
MANIFEST = OUT / "flora-naryn-assets-manifest.json"
def request_bytes(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA})
 for attempt in range(6):
  try:
   with urllib.request.urlopen(req,timeout=90) as response: return response.read()
  except (urllib.error.HTTPError,urllib.error.URLError) as exc:
   if isinstance(exc,urllib.error.HTTPError) and exc.code not in (429,500,502,503,504): raise
   if attempt==5: raise
   time.sleep(min(3*(2**attempt),45))
 raise RuntimeError("Download retries exhausted")
previous=json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
old_assets={x.get("output"):x for x in previous.get("assets",[])}
records=[]
for item in ITEMS:
 target=OUT/item["output"]; old=old_assets.get(item["output"],{})
 if target.exists() and old and hashlib.sha256(target.read_bytes()).hexdigest()==old.get("webp_sha256"):
  records.append(old); print("Reusing verified WebP:",item["output"]); continue
 api="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","format":"json","formatversion":2,"titles":"File:"+item["commons_title"],"prop":"imageinfo","iiprop":"url|size|sha1"})
 metadata=json.loads(request_bytes(api)); page=metadata["query"]["pages"][0]
 if page.get("missing"): raise RuntimeError("Commons file missing: "+item["commons_title"])
 info=page["imageinfo"][0]; dims=[info["width"],info["height"]]
 if dims!=item["dimensions"]: raise RuntimeError(f"Unexpected dimensions for {item['commons_title']}: {dims}")
 original=request_bytes(info["url"]); sha1=hashlib.sha1(original).hexdigest()
 if sha1!=info["sha1"]: raise RuntimeError(f"Commons SHA-1 mismatch for {item['commons_title']}: {sha1} != {info['sha1']}")
 if len(original)!=info["size"]: raise RuntimeError("Original byte-size mismatch: "+item["commons_title"])
 source=OUT/(item["output"]+".source.jpg"); source.write_bytes(original)
 with Image.open(source) as image: image.verify()
 with Image.open(source) as image: image.convert("RGB").save(target,"WEBP",quality=88,method=6)
 source.unlink(); webp=target.read_bytes()
 record={**item,"original_filename":item["commons_title"],"original_sha1_commons_api":info["sha1"],"original_sha1_downloaded":sha1,"original_bytes":len(original),"original_dimensions":dims,"webp_file":target.relative_to(ROOT).as_posix(),"webp_bytes":len(webp),"webp_sha256":hashlib.sha256(webp).hexdigest(),"webp_dimensions":dims,"conversion":"JPEG to WebP, RGB, quality=88, method=6"}
 records.append(record); print("Built and verified:",item["output"],"SHA-1",sha1)
MANIFEST.write_text(json.dumps({"generated_by":"biology/scripts/build_naryn_flora_assets.py","assets":records},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Manifest written:",MANIFEST)
