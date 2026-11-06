#!/usr/bin/env python3
"""Static and best-effort remote availability audit for Geography Chapter 02."""
from __future__ import annotations

import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

CHAPTER = Path("geography/chapters/02-geographic-envelope.md")
EXPECTED_EMBEDS = 56
EXPECTED_UNIQUE = 28
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)")
LOCAL_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((?!https?://)([^)\s]+)\)")


def probe(url: str) -> tuple[str, str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "AtlasOfKnowledge-GeographyImageAudit/1.0",
            "Range": "bytes=0-0",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            status = response.status
            content_type = response.headers.get("Content-Type", "").split(";")[0].lower()
            response.read(1)
            if 200 <= status < 300 and content_type.startswith("image/"):
                return url, "PASS", f"HTTP {status}; {content_type}"
            return url, "WARN", f"HTTP {status}; Content-Type={content_type or 'missing'}"
    except urllib.error.HTTPError as exc:
        state = "FAIL" if exc.code in (404, 410) else "WARN"
        return url, state, f"HTTP {exc.code}"
    except Exception as exc:  # network blocks/timeouts are not proof of a broken asset
        return url, "WARN", f"{type(exc).__name__}: {exc}"


def main() -> int:
    if not CHAPTER.is_file():
        print(f"FAIL: missing chapter file: {CHAPTER}")
        return 1

    text = CHAPTER.read_text(encoding="utf-8")
    matches = IMAGE_RE.findall(text)
    local = LOCAL_IMAGE_RE.findall(text)
    urls = [url for _, url in matches]
    counts = Counter(urls)
    errors: list[str] = []

    print(f"Chapter: {CHAPTER}")
    print(f"Image embeds: {len(matches)} (expected {EXPECTED_EMBEDS})")
    print(f"Unique remote assets: {len(counts)} (expected {EXPECTED_UNIQUE})")
    print(f"Local image references: {len(local)}")

    if len(matches) != EXPECTED_EMBEDS:
        errors.append(f"expected {EXPECTED_EMBEDS} image embeds, found {len(matches)}")
    if len(counts) != EXPECTED_UNIQUE:
        errors.append(f"expected {EXPECTED_UNIQUE} unique URLs, found {len(counts)}")
    if local:
        errors.append("local image references remain: " + ", ".join(path for _, path in local))

    empty_alt = [url for alt, url in matches if not alt.strip()]
    if empty_alt:
        errors.append(f"{len(empty_alt)} image embeds have empty alt text")
    non_https = [url for url in urls if not url.startswith("https://")]
    if non_https:
        errors.append(f"{len(non_https)} image URLs are not HTTPS")

    old_svg_refs = re.findall(r"geography/assets/diagrams/02-[^\s)\]]+\.svg", text)
    if old_svg_refs:
        errors.append("retired Chapter 02 SVG references remain: " + ", ".join(old_svg_refs))

    wrong_frequency = {url: count for url, count in counts.items() if count != 2}
    if wrong_frequency:
        errors.append("URLs must occur once in each language version (2 embeds each): " +
                      "; ".join(f"{url} ×{count}" for url, count in wrong_frequency.items()))

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: all {len(matches)} embeds have non-empty alt text, HTTPS sources, bilingual pairing, and no local image references.")
    print("Checking remote image endpoints (network failures other than 404/410 are warnings, not proof of broken assets)...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(probe, counts.keys()))

    tally = Counter(state for _, state, _ in results)
    for url, state, detail in results:
        print(f"{state}: {detail} — {url}")
    print(f"Remote endpoint summary: {tally['PASS']} PASS, {tally['WARN']} WARN, {tally['FAIL']} FAIL")

    if tally["FAIL"]:
        print("FAIL: one or more source endpoints returned 404/410; replace or repair those URLs.")
        return 1
    print("PASS: no confirmed 404/410 image endpoints. Review WARN entries manually before publication.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
