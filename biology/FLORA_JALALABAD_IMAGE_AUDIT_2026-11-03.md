# Jalal-Abad flora image audit — 3 November 2026

## Decision and scope

The P1 brief `image-brief-flora-jalalabad` is produced with one documentary photograph of the Arslanbob walnut-fruit forest and its surrounding wooded slopes. The image is a local example of a characteristic habitat, not a complete regional flora panorama. It does not depict or claim to represent Sary-Chelek, Besh-Aral, moist ravines or every vegetation community in Jalal-Abad Region.

## Source and licence

- Commons file: [Walnut forest Arslanbob.jpg](https://commons.wikimedia.org/wiki/File:Walnut_forest_Arslanbob.jpg)
- Author: Ekrem Canli; own work.
- Capture date: 13 July 2012.
- Location described by source: Arslanbob, Kyrgyzstan.
- Licence: CC BY-SA 3.0.
- Original: JPEG, 3,888 × 2,592 px, 10,193,195 bytes.
- Commons SHA-1: `b44ca13fcd8e9359bef518c0fbaa604797d7117d`.
- Downloaded original SHA-1: `b44ca13fcd8e9359bef518c0fbaa604797d7117d`.
- Local output: `biology/images/generated/flora-jalalabad.webp`.
- WebP: 3,888 × 2,592 px, 3,111,310 bytes.
- SHA-256: `a2be8bc5bbef030df622a8a40af342f1ac646ec0dc17e8674cdc2e143644331e`.
- Manifest: `biology/images/generated/flora-jalalabad-asset-manifest.json`.

The Commons page identifies the author, own-work status, capture date, source dimensions and CC BY-SA 3.0 licence. Its structured data identifies *Juglans regia*. The figure caption credits Ekrem Canli and links to the source and licence. The image is not modified beyond JPEG-to-WebP conversion.

## Integration and QA

- Replaced the exact planned marker in `chapters/flora-kyrgyzstan.html` with a semantic `figure` at the same anchor.
- Added Russian and English alt text and captions.
- Preserved native 3:2 aspect ratio rather than cropping the source into the former 16:9 placeholder.
- Updated `IMAGE_INSERTION_MAP.md`, `IMAGE_DISPOSITION_REGISTER.md`, `IMAGE_GENERATION_PLAN.md` and `IMAGE_SCIENTIFIC_REVIEW.md`.
- Source acquisition, SHA-1 validation, WebP conversion and standalone Chromium image decode passed in workflow https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41598920898.
- A second focused Chromium run passed against the actual bilingual chapter, including decode, native dimensions, visibility, bilingual alt text, caption and attribution link: https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41599165657.

## Progress accounting

Two of 52 unique visual briefs are complete: Chüy fauna (six photographs) and Jalal-Abad flora (one photograph). Visual-brief production is therefore **2/52 = 3.8%**. Do not count individual photographs as separate briefs. This figure is independent of the editorial-readiness score.

Offline caching remains unimplemented and unverified; browser decode QA does not establish offline availability.
