#!/usr/bin/env python3
"""Acquire and verify the four selected Issyk-Kul vegetation/habitat photographs."""
from __future__ import annotations
import hashlib, json, pathlib, time, urllib.error, urllib.parse, urllib.request
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "biology" / "images" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
UA = "AtlasOfKnowledge-BiologyAssetBuilder/1.0 (educational project; source attribution in manifest)"
ITEMS = [
    {
        "commons_title": "E8288-Tamchy-Bay-wetland.jpg",
        "output": "flora-issyk-wetland.webp",
        "subject": "Tamchy Bay lakeshore wetland",
        "author": "Vmenkov",
        "date": "2007-09-16",
        "location": "Tamchy Bay between Tamchy and Kosh Köl, Issyk-Kul Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:E8288-Tamchy-Bay-wetland.jpg",
        "dimensions": [2048, 1536],
    },
    {
        "commons_title": "E8221-Tamchy-dry-gulch.jpg",
        "output": "flora-issyk-dry-foothills.webp",
        "subject": "Dry gully and foothill terrain above Tamchy",
        "author": "Vmenkov",
        "date": "2007-09-15",
        "location": "Dry hills above Tamchy, Issyk-Kul Region, Kyrgyzstan",
        "license": "CC BY-SA 3.0",
        "page": "https://commons.wikimedia.org/wiki/File:E8221-Tamchy-dry-gulch.jpg",
        "dimensions": [2048, 1536],
    },
    {
        "commons_title": "E8306-Kosh-Kol-sea-buckthorn.jpg",
        "output": "flora-issyk-sea-buckthorn.webp",
        "subject": "Sea-buckthorn shrub on the Issyk-Kul shore",
        "taxon": "Hippophae rhamnoides",
        "author": "Vmenkov",
        "date": "2007-09-16",
        "location": "Shore of Issyk-Kul between Tamchy and Kosh Köl, Issyk-Kul Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:E8306-Kosh-Kol-sea-buckthorn.jpg",
        "dimensions": [2560, 1920],
    },
    {
        "commons_title": "Karakol Valley.jpg",
        "output": "flora-issyk-karakol-spruce.webp",
        "subject": "Karakol Valley with Schrenk spruce forest",
        "taxon": "Picea schrenkiana",
        "author": "Ondřej Žváček",
        "date": "2008-08-19",
        "location": "Karakol Valley, Issyk-Kul Region, Kyrgyzstan",
        "license": "CC BY-SA 3.0",
        "page": "https://commons.wikimedia.org/wiki/File:Karakol_Valley.jpg",
        "dimensions": [3072, 2304],
    },
]
MANIFEST = OUT / "flora-issyk-assets-manifest.json"

def request_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                return response.read()
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            if isinstance(exc, urllib.error.HTTPError) and exc.code not in (429, 500, 502, 503, 504):
                raise
            if attempt == 5:
                raise
            time.sleep(min(3 * (2 ** attempt), 45))
    raise RuntimeError("Download retries exhausted")

previous = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
old_assets = {x.get("output"): x for x in previous.get("assets", [])}
records = []
for item in ITEMS:
    target = OUT / item["output"]
    old = old_assets.get(item["output"], {})
    if target.exists() and old:
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        if digest == old.get("webp_sha256"):
            records.append(old)
            print("Reusing verified WebP:", item["output"])
            continue

    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "formatversion": 2,
        "titles": "File:" + item["commons_title"],
        "prop": "imageinfo", "iiprop": "url|size|sha1",
    })
    metadata = json.loads(request_bytes(api))
    page = metadata["query"]["pages"][0]
    if page.get("missing"):
        raise RuntimeError("Commons file missing: " + item["commons_title"])
    info = page["imageinfo"][0]
    dimensions = [info["width"], info["height"]]
    if dimensions != item["dimensions"]:
        raise RuntimeError(f"Unexpected dimensions for {item['commons_title']}: {dimensions}")
    original = request_bytes(info["url"])
    sha1 = hashlib.sha1(original).hexdigest()
    if sha1 != info["sha1"]:
        raise RuntimeError(f"Commons SHA-1 mismatch for {item['commons_title']}: {sha1} != {info['sha1']}")
    if len(original) != info["size"]:
        raise RuntimeError(f"Original byte-size mismatch for {item['commons_title']}")
    source = OUT / (item["output"] + ".source.jpg")
    source.write_bytes(original)
    with Image.open(source) as image:
        image.verify()
    with Image.open(source) as image:
        image.convert("RGB").save(target, "WEBP", quality=88, method=6)
    source.unlink()
    webp = target.read_bytes()
    record = {
        **item,
        "original_filename": item["commons_title"],
        "original_sha1_commons_api": info["sha1"],
        "original_sha1_downloaded": sha1,
        "original_bytes": len(original),
        "original_dimensions": dimensions,
        "webp_file": str(target.relative_to(ROOT)).replace("\\\\", "/"),
        "webp_bytes": len(webp),
        "webp_sha256": hashlib.sha256(webp).hexdigest(),
        "webp_dimensions": dimensions,
        "conversion": "JPEG to WebP, RGB, quality=88, method=6",
    }
    records.append(record)
    print("Built and verified:", item["output"], "SHA-1", sha1)

MANIFEST.write_text(json.dumps({
    "generated_by": "biology/scripts/build_issyk_flora_assets.py",
    "assets": records,
}, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
print("Manifest written:", MANIFEST)
