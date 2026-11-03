# Naryn flora visual brief — source, licence and integration audit

**Date:** 3 November 2026  
**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Branch:** `workspace/biology`  
**Brief:** `image-brief-flora-naryn`  
**Status:** Produced — three locally packaged WebP photographs; focused bilingual Chromium QA passed.

## Accepted images and provenance

1. **Chatyr-Kul shoreline**
   - Commons file: [Chatyr kul lake.JPG](https://commons.wikimedia.org/wiki/File:Chatyr_kul_lake.JPG)
   - Author: Nurdjen; date: July 2006; location: Chatyr-Kul, Naryn Region, Kyrgyzstan.
   - Rights: public-domain dedication (PD-self).
   - Original JPEG: 2,816 × 2,120 px; 1,569,099 bytes.
   - Commons API SHA-1 and downloaded-original SHA-1: `c26860e9b01d7b06bfc8684bbd33f96cb73bf615`.
   - WebP: `biology/images/generated/flora-naryn-chatyr.webp`; 496,772 bytes; SHA-256 `bcf1fc200eb6a9534a4f85f3e1ccb758be61d8cd3d63df9d1734b6bdac74b200`.

2. **Son-Kul lakeshore meadow**
   - Commons file: [Son-Kul, Kyrgyzstan (44623421951).jpg](https://commons.wikimedia.org/wiki/File:Son-Kul,_Kyrgyzstan_(44623421951).jpg)
   - Author: Ninara; date: 16 July 2018; location: Son-Kul, Naryn Region, Kyrgyzstan.
   - Licence: CC BY 2.0.
   - Original JPEG: 3,240 × 2,160 px; 5,113,942 bytes.
   - Commons API SHA-1 and downloaded-original SHA-1: `d633442f141d97a1db60affb53068450afbea4b7`.
   - WebP: `biology/images/generated/flora-naryn-songkul.webp`; 1,061,080 bytes; SHA-256 `5cb5829525dd5d427fccc8a687dbd02131f0c00fe87738c790b62ebc3f8ec76f`.

3. **Songorica clematis (*Clematis songorica*)**
   - Commons file: [Clematis songorica.jpg](https://commons.wikimedia.org/wiki/File:Clematis_songorica.jpg)
   - Author: Alexey Yakovlev; date: 11 July 2026.
   - Location: tributary of the Alabuga River, 4 km south of Dzherge-Tal, Ak-Tala District, Naryn Region, Kyrgyzstan; 2,400 m a.s.l.
   - Licence: CC0 1.0.
   - Original JPEG: 1,400 × 933 px; 450,948 bytes.
   - Commons API SHA-1 and downloaded-original SHA-1: `dc3fe6c40900b70292db502ed9b75af322cd2198`.
   - WebP: `biology/images/generated/flora-naryn-clematis.webp`; 272,820 bytes; SHA-256 `16333088149f22584564ade575a7a9e4a0ebce954b377da343f2cf11e8eb3d51`.

All three source originals were retrieved by the dedicated GitHub Actions builder from current Wikimedia Commons file metadata. Each downloaded SHA-1, byte count and dimension set matched the live Commons API metadata. Derivatives are RGB WebP conversions at quality 88, method 6. Complete machine-readable provenance is in `images/generated/flora-naryn-assets-manifest.json`.

## Scientific and editorial scope

The figure presents two high-altitude lake shoreline settings and one geographically documented plant record. It does not claim that *Clematis songorica* is restricted to the photographed point, nor that the three panels form a complete vegetation survey or map of Naryn Region. The taxon caption is limited to the source-identified *Clematis songorica* and its recorded Naryn locality.

## Integration and QA

- Replaced the planned marker at the original `image-brief-flora-naryn` anchor in `chapters/flora-kyrgyzstan.html` with a semantic three-panel figure.
- Preserved native image aspect ratios and used bilingual alt text/captions with source and licence attribution.
- Focused Chromium chapter QA passed in [workflow run 41611003785](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41611003785). It decoded all three local WebP files, checked dimensions, visibility, bilingual alt text and source links. The public-domain panel check was corrected to match the exact Russian wording of the caption; this did not change the image or its rights status.
- Generated asset commit: `811fb5ea4194da34bf1c86b7fd1d4cfa930cd0a5` (`Add verified Naryn flora WebP assets`).

## Progress accounting

This completes one visual brief, not three. The atlas now has **4 of 52 mapped visual briefs produced (7.7%)**: Chüy fauna (six photographs), Jalal-Abad flora (one), Issyk-Kul flora (four) and Naryn flora (three). The other 48 briefs remain pending or deferred. The controlled editorial-readiness score remains 95/100 and is not increased by image production.

Offline caching remains unimplemented and unverified; browser decode QA does not establish offline availability.
