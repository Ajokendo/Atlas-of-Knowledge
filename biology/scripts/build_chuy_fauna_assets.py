#!/usr/bin/env python3
"""Download and verify selected Chüy fauna and habitat originals, then create WebP assets."""
from __future__ import annotations
import hashlib, json, pathlib, time, urllib.error, urllib.parse, urllib.request
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "biology" / "images" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
UA = "AtlasOfKnowledge-BiologyAssetBuilder/1.0 (educational project; source attribution in manifest)"
FILES = [
    {
        "commons_title": "File:Ала-Арча, белка.jpg",
        "output": "fauna-chuy-squirrel.webp",
        "subject": "Red squirrel (Sciurus vulgaris)",
        "author": "Nikolai Bulykin",
        "date": "2023-08-25",
        "location": "Ala-Archa National Park, Chüy Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:Ала-Арча,_белка.jpg",
    },
    {
        "commons_title": "File:Ала-Арча, обыкновенный щитомордник (1).jpg",
        "output": "fauna-chuy-pit-viper.webp",
        "subject": "Halys pit viper (Gloydius halys)",
        "author": "Nikolai Bulykin",
        "date": "2023-08-25",
        "location": "Ala-Archa National Park, Chüy Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:Ала-Арча,_обыкновенный_щитомордник_(1).jpg",
    },
    {
        "commons_title": "File:Ak Suu Gorge, Chuy region, Kyrgyzstan.jpg",
        "output": "habitat-chuy-ak-suu.webp",
        "subject": "Ak-Suu gorge and river habitat",
        "author": "Vilya Shoni",
        "date": "2022-06-18",
        "location": "Ak-Suu Complex Sanctuary, Moskovsky District, Chüy Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:Ak_Suu_Gorge,_Chuy_region,_Kyrgyzstan.jpg",
    },
    {
        "commons_title": "File:Landscape view, Ala Archa National Park, Chuy region, Kyrgyzstan 02.jpg",
        "output": "habitat-chuy-ala-archa.webp",
        "subject": "Ala-Archa mountain forest and alpine habitat",
        "author": "Vilya Shoni",
        "date": "2024-05-17",
        "location": "Ala-Archa National Park, Chüy Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:Landscape_view,_Ala_Archa_National_Park,_Chuy_region,_Kyrgyzstan_02.jpg",
    },
    {
        "commons_title": "File:Chong Kemin National Park, Kemin district, Chuy Region, Kyrgyzstan 01.jpg",
        "output": "habitat-chuy-chon-kemin.webp",
        "subject": "Chong-Kemin rocky stream, meadow and conifer-forest habitat",
        "author": "Vilya Shoni",
        "date": "2024-06-07",
        "location": "Chong-Kemin State Nature Park, Kemin District, Chüy Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:Chong_Kemin_National_Park,_Kemin_district,_Chuy_Region,_Kyrgyzstan_01.jpg",
    },
    {
        "commons_title": "File:Canyon, Chunkurchak sanctuary, Chuy region, Kyrgyzstan.jpg",
        "output": "habitat-chuy-chunkurchak-canyon.webp",
        "subject": "Chunkurchak red sandstone canyon and shrub habitat",
        "author": "Vilya Shoni",
        "date": "2020-06-07",
        "location": "Chong-Kuurchak Botanical Reserve, Alamudun District, Chüy Region, Kyrgyzstan",
        "license": "CC BY-SA 4.0",
        "page": "https://commons.wikimedia.org/wiki/File:Canyon,_Chunkurchak_sanctuary,_Chuy_region,_Kyrgyzstan.jpg",
    },
]

def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 5:
                raise
            retry_after = exc.headers.get("Retry-After")
            delay = int(retry_after) if retry_after and retry_after.isdigit() else min(3 * (2 ** attempt), 45)
            time.sleep(delay)
        except urllib.error.URLError:
            if attempt == 5:
                raise
            time.sleep(min(3 * (2 ** attempt), 45))
    raise RuntimeError("Download retry loop exhausted: " + url)

manifest = {"generated_by": "biology/scripts/build_chuy_fauna_assets.py", "assets": []}
for item in FILES:
    query = urllib.parse.urlencode({
        "action": "query", "format": "json", "titles": item["commons_title"],
        "prop": "imageinfo", "iiprop": "url|sha1|size|mime"
    })
    payload = json.loads(get("https://commons.wikimedia.org/w/api.php?" + query))
    page = next(iter(payload["query"]["pages"].values()))
    info = page["imageinfo"][0]
    if info["mime"] != "image/jpeg":
        raise RuntimeError(f"Unexpected source MIME for {item['commons_title']}: {info['mime']}")
    original = get(info["url"])
    actual_sha1 = hashlib.sha1(original).hexdigest()
    if actual_sha1 != info["sha1"]:
        raise RuntimeError(f"SHA-1 mismatch for {item['commons_title']}: {actual_sha1} != {info['sha1']}")
    if len(original) != int(info["size"]):
        raise RuntimeError(f"Byte-size mismatch for {item['commons_title']}")
    temp = OUT / (item["output"] + ".source.jpg")
    temp.write_bytes(original)
    with Image.open(temp) as im:
        im.verify()
    with Image.open(temp) as im:
        dimensions = list(im.size)
        im = im.convert("RGB")
        target = OUT / item["output"]
        im.save(target, "WEBP", quality=88, method=6)
    temp.unlink()
    webp_bytes = target.read_bytes()
    manifest["assets"].append({
        **item,
        "original_filename": pathlib.PurePosixPath(urllib.parse.urlparse(info["url"]).path).name,
        "original_sha1_commons": info["sha1"],
        "original_sha1_downloaded": actual_sha1,
        "original_bytes": len(original),
        "original_dimensions": dimensions,
        "webp_file": str(target.relative_to(ROOT)).replace("\\", "/"),
        "webp_bytes": len(webp_bytes),
        "webp_sha256": hashlib.sha256(webp_bytes).hexdigest(),
        "webp_dimensions": dimensions,
        "conversion": "JPEG to WebP, RGB, quality=88, method=6",
    })
(OUT / "fauna-chuy-assets-manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(manifest, ensure_ascii=False, indent=2))
