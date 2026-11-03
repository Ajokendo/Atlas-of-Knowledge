#!/usr/bin/env python3
"""Acquire and verify the selected Arslanbob walnut-forest photograph."""
from __future__ import annotations
import hashlib, json, pathlib, time, urllib.error, urllib.request
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "biology" / "images" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
ITEM = {
    "commons_title": "File:Walnut forest Arslanbob.jpg",
    "output": "flora-jalalabad.webp",
    "subject": "Arslanbob walnut-fruit forest landscape",
    "author": "Ekrem Canli",
    "date": "2012-07-13",
    "location": "Arslanbob, Jalal-Abad Region, Kyrgyzstan",
    "license": "CC BY-SA 3.0",
    "page": "https://commons.wikimedia.org/wiki/File:Walnut_forest_Arslanbob.jpg",
    "direct_url": "https://upload.wikimedia.org/wikipedia/commons/4/48/Walnut_forest_Arslanbob.jpg",
    "expected_sha1": "b44ca13fcd8e9359bef518c0fbaa604797d7117d",
    "expected_bytes": 10193195,
    "expected_dimensions": [3888, 2592],
}
UA = "AtlasOfKnowledge-BiologyAssetBuilder/1.0 (educational project; source attribution in manifest)"
TARGET = OUT / ITEM["output"]
MANIFEST = OUT / "flora-jalalabad-asset-manifest.json"

def download(url: str) -> bytes:
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
cached = previous.get("asset", {})
if TARGET.exists() and cached:
    digest = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    if digest == cached.get("webp_sha256"):
        print("Reusing previously verified WebP:", ITEM["output"])
        raise SystemExit(0)

original = download(ITEM["direct_url"])
sha1 = hashlib.sha1(original).hexdigest()
if sha1 != ITEM["expected_sha1"]:
    raise RuntimeError(f"Commons SHA-1 mismatch: {sha1}")
if len(original) != ITEM["expected_bytes"]:
    raise RuntimeError(f"Original byte-size mismatch: {len(original)}")
source = OUT / (ITEM["output"] + ".source.jpg")
source.write_bytes(original)
with Image.open(source) as image:
    image.verify()
with Image.open(source) as image:
    dimensions = list(image.size)
    if dimensions != ITEM["expected_dimensions"]:
        raise RuntimeError(f"Unexpected source dimensions: {dimensions}")
    image.convert("RGB").save(TARGET, "WEBP", quality=88, method=6)
source.unlink()
webp = TARGET.read_bytes()
record = {
    **{k: v for k, v in ITEM.items() if k not in {"direct_url", "expected_sha1", "expected_bytes", "expected_dimensions"}},
    "original_filename": "Walnut_forest_Arslanbob.jpg",
    "original_sha1_commons": ITEM["expected_sha1"],
    "original_sha1_downloaded": sha1,
    "original_bytes": len(original),
    "original_dimensions": dimensions,
    "webp_file": str(TARGET.relative_to(ROOT)).replace("\\\\", "/"),
    "webp_bytes": len(webp),
    "webp_sha256": hashlib.sha256(webp).hexdigest(),
    "webp_dimensions": dimensions,
    "conversion": "JPEG to WebP, RGB, quality=88, method=6",
}
MANIFEST.write_text(json.dumps({"generated_by": "biology/scripts/build_jalalabad_flora_asset.py", "asset": record}, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=False, indent=2))
