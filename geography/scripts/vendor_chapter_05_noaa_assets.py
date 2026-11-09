#!/usr/bin/env python3
"""Download unchanged NOAA educational images into a local mirror for GitHub Markdown."""
from __future__ import annotations
import hashlib
import urllib.request
from pathlib import Path

OUT=Path("geography/assets/chapter-05-noaa")
SOURCES=[
("noaa-global-atmospheric-circulation","https://www.noaa.gov/sites/default/files/2022-05/circ.jpg","https://www.noaa.gov/jetstream/global/global-atmospheric-circulations"),
("noaa-hydrologic-cycle","https://www.noaa.gov/media/image_download/72476931-c7f9-4606-a1d8-61f4703d806e","https://www.noaa.gov/jetstream/atmosphere/hydro"),
("noaa-cold-front-symbol","https://www.noaa.gov/sites/default/files/2022-06/cold_front_sym.png","https://www.noaa.gov/jetstream/wxmaps"),
("noaa-warm-front-symbol","https://www.noaa.gov/sites/default/files/2022-06/warm_front_sym.png","https://www.noaa.gov/jetstream/wxmaps"),
("noaa-stationary-front-symbol","https://www.noaa.gov/sites/default/files/2022-06/stationary_front_sym.png","https://www.noaa.gov/jetstream/wxmaps"),
("noaa-occluded-front-symbol","https://www.noaa.gov/sites/default/files/2022-06/occ_front_sym.png","https://www.noaa.gov/jetstream/wxmaps"),
("noaa-cold-occlusion-cross-section","https://www.noaa.gov/sites/default/files/2022-06/cold_occ.png","https://www.noaa.gov/jetstream/wxmaps"),
]
def extension(data:bytes)->str:
    if data.startswith(bytes([137,80,78,71,13,10,26,10])): return ".png"
    if data.startswith(bytes([255,216,255])): return ".jpg"
    if data.startswith((b"GIF87a",b"GIF89a")): return ".gif"
    if data.startswith(b"RIFF") and data[8:12]==b"WEBP": return ".webp"
    if data.startswith(b"BM"): return ".bmp"
    raise ValueError("response is not a recognised raster image")
def main()->int:
    OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    for stem,url,context in SOURCES:
        req=urllib.request.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (compatible; AtlasOfKnowledgeAssetMirror/1.0)",
            "Accept":"image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
            "Referer":context,
        })
        with urllib.request.urlopen(req,timeout=45) as response:
            data=response.read(25*1024*1024+1)
            ctype=response.headers.get("Content-Type","").split(";")[0].lower()
            if len(data)>25*1024*1024: raise ValueError(stem+": response exceeds 25 MiB")
            ext=extension(data)
            if ctype and not (ctype.startswith("image/") or ctype=="application/octet-stream"):
                raise ValueError(stem+": unexpected content type "+ctype)
        path=OUT/(stem+ext)
        path.write_bytes(data)
        digest=hashlib.sha256(data).hexdigest()
        rows.append((path,len(data),digest,url,context))
        print("MIRRORED",path,"bytes="+str(len(data)),"sha256="+digest)
    readme=["# NOAA educational image mirror — Chapter 05","","These files are byte-for-byte local copies of the official NOAA image endpoints listed below. They are mirrored unchanged solely to avoid failures of GitHub's external-image proxy in the Chapter 05 Markdown view.","","Credit: NOAA. No NOAA endorsement is implied. The Chapter 05 source register records the specific NOAA reuse guidance and scope for each image. These third-party images are not included in the project's separate CC BY-NC 4.0 designation for 11 original project SVGs.",""]
    for path,size,digest,url,context in rows:
        readme.append("- **"+path.name+"** — original image: "+url+"; context: "+context+"; unchanged copy; "+str(size)+" bytes; SHA-256: "+digest+".")
    (OUT/"README.md").write_text("\n".join(readme)+"\n",encoding="utf-8")
    print("PASS:",len(rows),"unchanged NOAA image copies mirrored.")
    return 0
if __name__=="__main__": raise SystemExit(main())
