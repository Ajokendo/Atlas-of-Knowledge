#!/usr/bin/env python3
"""Static and best-effort remote availability audit for Geography Chapter 03."""
from __future__ import annotations
import concurrent.futures, re, sys, urllib.error, urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

CHAPTER = Path("geography/chapters/03-lithosphere-and-geological-processes.md")
EXPECTED_EMBEDS, EXPECTED_UNIQUE = 26, 13
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
NS = {"svg": "http://www.w3.org/2000/svg"}

def probe(url):
    req=urllib.request.Request(url,headers={"User-Agent":"AtlasOfKnowledge-GeographyImageAudit/1.0","Range":"bytes=0-0"})
    try:
        with urllib.request.urlopen(req,timeout=15) as response:
            status=response.status; kind=response.headers.get("Content-Type","").split(";")[0].lower(); response.read(1)
            return (url,"PASS" if 200<=status<300 and kind.startswith("image/") else "WARN",f"HTTP {status}; {kind or 'missing content type'}")
    except urllib.error.HTTPError as exc:
        return url,("FAIL" if exc.code in (404,410) else "WARN"),f"HTTP {exc.code}"
    except Exception as exc:
        return url,"WARN",f"{type(exc).__name__}: {exc}"

def main():
    if not CHAPTER.is_file(): print("FAIL: missing",CHAPTER); return 1
    source=CHAPTER.read_text(encoding="utf-8"); matches=IMAGE_RE.findall(source)
    counts=Counter(target for _,target in matches); errors=[]
    print(f"Embeds: {len(matches)} (expected 26); unique assets: {len(counts)} (expected 13)")
    if len(matches)!=EXPECTED_EMBEDS: errors.append(f"expected 26 embeds, found {len(matches)}")
    if len(counts)!=EXPECTED_UNIQUE: errors.append(f"expected 13 unique assets, found {len(counts)}")
    if any(n!=2 for n in counts.values()): errors.append("every asset must appear once in each language section")
    if any(not alt.strip() or "/" not in alt for alt,_ in matches): errors.append("all alt text must be non-empty and bilingual")
    remote=[u for u in counts if u.startswith("https://")]; local=[u for u in counts if not u.startswith("https://")]
    if len(remote)!=3 or len(local)!=10: errors.append(f"expected 3 remote and 10 local assets; found {len(remote)} and {len(local)}")
    for rel in local:
        target=(CHAPTER.parent/rel).resolve()
        if not target.is_file(): errors.append(f"missing local asset: {rel}"); continue
        try:
            root=ET.parse(target).getroot()
            if root.tag.split("}")[-1]!="svg" or not root.get("viewBox") or root.get("role")!="img": errors.append(f"invalid SVG root/viewBox/role: {rel}")
            if root.find("svg:title",NS) is None or root.find("svg:desc",NS) is None: errors.append(f"missing SVG title/desc: {rel}")
            visible=" ".join(t.strip() for t in root.itertext() if t.strip())
            if not re.search(r"[А-Яа-яЁё]",visible) or not re.search(r"[A-Za-z]",visible): errors.append(f"SVG does not contain both RU and EN text: {rel}")
        except ET.ParseError as exc: errors.append(f"invalid SVG XML {rel}: {exc}")
    if errors:
        for error in errors: print("FAIL:",error)
        return 1
    print("PASS: all 26 bilingual embeds; 10 local SVGs resolve and pass XML, title, description and RU/EN checks.")
    print("Probing 3 external images; network blocks/rate limits are warnings, confirmed 404/410 is failure.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(probe,remote))
    tally=Counter(state for _,state,_ in results)
    for url,state,detail in results: print(f"{state}: {detail} — {url}")
    print(f"Remote endpoint summary: {tally['PASS']} PASS, {tally['WARN']} WARN, {tally['FAIL']} FAIL")
    if tally["FAIL"]: return 1
    print("PASS: no confirmed 404/410 remote endpoints; manually review any WARN.")
    return 0
if __name__=="__main__": sys.exit(main())
