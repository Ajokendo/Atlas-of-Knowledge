# Issyk-Kul flora image audit — 3 November 2026

## Decision and scope

The P1 brief `image-brief-flora-issyk` is produced with four locally packaged documentary photographs. The panel keeps four distinct settings visually separate: a Tamchy Bay wetland, a dry gully above Tamchy, a sea-buckthorn shrub on the lake shore, and the spruce-forested Karakol Valley.

These are dated photographic examples from 2007–2008, not a complete, current or georeferenced vegetation map of the Issyk-Kul basin. The dry-gully image documents terrain and a dry setting; it does not establish a named plant community. Species identification is limited to the source-supported *Hippophae rhamnoides* and *Picea schrenkiana* captions.

## Sources, licences and binary verification

All originals were retrieved by the GitHub Actions builder. The workflow queried Wikimedia Commons image metadata at build time and verified each downloaded original's byte count, dimensions and SHA-1 against the live Commons API values before converting it to WebP.

### 1. Tamchy Bay wetland

- Commons file: https://commons.wikimedia.org/wiki/File:E8288-Tamchy-Bay-wetland.jpg
- Author: Vmenkov; own work.
- Date: 16 September 2007.
- Location: Tamchy Bay between Tamchy and Kosh Köl, Issyk-Kul Region.
- Licence: CC BY-SA 4.0.
- Original JPEG: 2,048 × 1,536 px; 1,179,469 bytes.
- Commons API SHA-1 and downloaded SHA-1: `c233acf00a5d28c06fe6ab36b2533850eca15149`.
- Local output: `biology/images/generated/flora-issyk-wetland.webp`.
- WebP: 597,392 bytes; SHA-256 `80e82b191baa37120ac5662bd61f60034dcfd7f45113a68de5188692e3ff0588`.

### 2. Dry gully above Tamchy

- Commons file: https://commons.wikimedia.org/wiki/File:E8221-Tamchy-dry-gulch.jpg
- Author: Vmenkov; own work.
- Date: 15 September 2007.
- Location: dry hills above Tamchy, Issyk-Kul Region.
- Licence: CC BY-SA 3.0.
- Original JPEG: 2,048 × 1,536 px; 1,206,027 bytes.
- Commons API SHA-1 and downloaded SHA-1: `a9d86c598db9c3709c6406a83b26de8cc680ae5f`.
- Local output: `biology/images/generated/flora-issyk-dry-foothills.webp`.
- WebP: 714,808 bytes; SHA-256 `c2b810e0d119c3cbadf4595893d7c8ffa35d837d9a1daa962224292981d8a913`.

### 3. Sea-buckthorn on the Issyk-Kul shore

- Commons file: https://commons.wikimedia.org/wiki/File:E8306-Kosh-Kol-sea-buckthorn.jpg
- Author: Vmenkov; own work.
- Date: 16 September 2007.
- Location: shore between Tamchy and Kosh Köl, Issyk-Kul Region.
- Source-supported taxon: *Hippophae rhamnoides*.
- Licence: CC BY-SA 4.0.
- Original JPEG: 2,560 × 1,920 px; 1,745,803 bytes.
- Commons API SHA-1 and downloaded SHA-1: `436ec4c8caffc3b4b95a5e4b39fa4eb170b88ee5`.
- Local output: `biology/images/generated/flora-issyk-sea-buckthorn.webp`.
- WebP: 1,116,186 bytes; SHA-256 `3d5fcd6791139c108e00ae44042b0608a6c4182ad42a6025a1cf67c6812e08f1`.

### 4. Karakol Valley spruce forest

- Commons file: https://commons.wikimedia.org/wiki/File:Karakol_Valley.jpg
- Author: Ondřej Žváček; own work.
- Date: 19 August 2008.
- Location: Karakol Valley, Issyk-Kul Region.
- Source description identifies the trees as *Picea schrenkiana*.
- Licence used: CC BY-SA 3.0 (the file page also offers CC BY 2.5).
- Original JPEG: 3,072 × 2,304 px; 5,126,254 bytes.
- Commons API SHA-1 and downloaded SHA-1: `8abf0b8afa14a954bdc40f9616ea5d47b348d011`.
- Local output: `biology/images/generated/flora-issyk-karakol-spruce.webp`.
- WebP: 1,194,038 bytes; SHA-256 `719fc93ed1247e129974c963e6c44b25fb1be0cd89b59adb97010e8a74fcae0a`.

## Integration and QA

- Replaced the exact planned note at `figure#image-brief-flora-issyk` in `chapters/flora-kyrgyzstan.html`.
- Preserved four native 4:3 image proportions in a responsive four-panel grid; no panorama or map is implied.
- Added Russian and English alt text and captions for every photograph, with an individual Commons source link and licence attribution.
- Updated `IMAGE_INSERTION_MAP.md`, `IMAGE_DISPOSITION_REGISTER.md`, `IMAGE_GENERATION_PLAN.md` and `IMAGE_SCIENTIFIC_REVIEW.md`.
- The original downloads, live Commons SHA-1 checks, dimensions/byte-size validation and WebP conversion passed.
- Focused Chromium chapter QA passed in https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41608849568. The test opened the actual bilingual flora chapter and decoded all four local images, checking dimensions, visibility, bilingual alt text and the exact attribution links.

## Progress accounting

Three of 52 unique visual briefs are complete: Chüy fauna (six photographs), Jalal-Abad flora (one photograph) and Issyk-Kul flora (four photographs). Visual-brief production is **3/52 = 5.8%**. Eleven photographs are contained in those three completed briefs. The other 49 briefs remain pending or deferred. Do not count individual photographs as separate briefs.

This figure is independent of the controlled editorial-readiness score. Offline caching remains unimplemented and unverified; browser image decode QA does not establish offline availability.
