# Osh flora visual brief — source, licence and integration audit

**Date:** 3 November 2026  
**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Branch:** `workspace/biology`  
**Brief:** `image-brief-flora-osh`  
**Status:** Produced — one locally packaged WebP photograph; focused bilingual Chromium QA passed.

## Accepted image and provenance

- Commons file: [Inbound1554290775583060652.jpg](https://commons.wikimedia.org/wiki/File:Inbound1554290775583060652.jpg)
- Author: Talantbekkyzymalika; own work.
- Capture date: 12 June 2024.
- Location: Kulun-Ata State Nature Reserve, Kara-Kulja District, Osh Region, Kyrgyzstan.
- Licence: CC BY-SA 4.0.
- Original JPEG: 4,640 × 3,472 px; 10,395,588 bytes.
- Commons SHA-1: `faddae3b639dacafb1002b04b75ecb0c1c1060d1`.
- Downloaded-original SHA-1: `faddae3b639dacafb1002b04b75ecb0c1c1060d1`.
- Local output: `biology/images/generated/flora-osh.webp`.
- WebP: 4,640 × 3,472 px; 4,093,228 bytes.
- SHA-256: `30cc8f67c2c0f631a06cb4f51e79179c023af253f6ff2bd7d6c5be15a1835f63`.
- Manifest: `biology/images/generated/flora-osh-asset-manifest.json`.

The Commons page identifies the location, creator, capture date, dimensions, checksum and CC BY-SA 4.0 licence. The downloaded original's SHA-1 matched the Commons value exactly. The derivative is an RGB JPEG-to-WebP conversion (quality 88, method 6); no crop or content alteration was made.

## Scientific and editorial scope

The photograph visibly shows a mountain river corridor with woody riparian vegetation in Kulun-Ata State Nature Reserve. The caption intentionally does not identify individual trees or claim that the visible vegetation is juniper or spruce. It is one local river-habitat example, not a complete inventory of Osh Region flora, a map of the reserve, or a representation of all its forest and altitudinal zones.

## Integration and QA

- Replaced the planned marker at the original `image-brief-flora-osh` anchor in `chapters/flora-kyrgyzstan.html` with a semantic figure.
- Preserved the original image dimensions and near-4:3 aspect ratio.
- Added bilingual alt text/captions, author credit and direct source/licence links.
- Focused Chromium image decode and chapter-integration QA passed in [workflow run 41611930095](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41611930095). The test checked the local image, native dimensions, visibility, bilingual alt text, caption credit, licence and source link.
- Generated asset commit: `42b46a9ea95c6ffa9478a7d0233dcc8c90f1efa5`.

## Progress accounting

This completes one visual brief. The atlas now has **5 of 52 mapped visual briefs produced (9.6%)**: Chüy fauna (six photographs), Jalal-Abad flora (one), Issyk-Kul flora (four), Naryn flora (three) and Osh flora (one). The other 47 briefs remain pending or deferred. The controlled editorial-readiness score remains 95/100 and is not increased by image production.

Offline caching remains unimplemented and unverified; browser decode QA does not establish offline availability.
