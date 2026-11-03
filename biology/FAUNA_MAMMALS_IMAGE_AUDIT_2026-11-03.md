# Mountain mammals illustration audit — 3 November 2026

**Branch:** `workspace/biology`  
**Chapter:** `chapters/fauna-kyrgyzstan.html`  
**Anchor:** `image-brief-fauna-mammals`  
**Target:** `images/generated/fauna-mammals.webp`  
**Priority:** P1  
**Disposition:** Candidate generated and visually screened; repository integration and browser QA pending. The brief remains Deferred.

## Evidence and taxonomic scope

The chapter's three intended subjects are:
- Snow leopard — `Panthera uncia`. The 2026 country status paper describes its distribution across Kyrgyz Tian Shan and Pamir–Alai ranges and gives a primary elevational range of 3,000–4,000 m, with camera-trap records lower and field evidence higher. It is a country-level synthesis, not a claim about one exact valley.
- Argali — `Ovis ammon`. The chapter and Kyrgyzstan country material support its presence in high-mountain landscapes. Subspecies should not be assigned in the illustration without locality-specific confirmation.
- Siberian ibex — `Capra sibirica`. The chapter describes this wild mountain goat as characteristic of rocky high-mountain terrain. Keep it distinct from argali by its long backward-curving, ridged horns and beard.

## Visual inspection

A new 16:9 naturalistic landscape candidate was generated. It depicts:
- a snow leopard on a rocky ledge, with pale coat, dark rosettes and long thick tail;
- an argali on a more open grassy slope, with massive curled horns;
- a Siberian ibex on a separate higher rocky outcrop, with long swept-back horns and beard.

The animals are spatially separated and are not shown fighting, hunting or forming an artificial group. The scene is an **illustrative habitat reconstruction**, not documentary evidence that all three individuals occupy the same site or were observed together. It contains no scientific labels, population counts, range boundaries or conservation-status symbols.

## Provenance and integration gate

This is original AI-generated artwork, not a third-party photograph. It requires no external photo attribution; the atlas should identify it as an illustrative generated reconstruction in its bilingual caption. The generated candidate is currently stored in the working session only and has **not** yet been committed to the repository or inserted into the chapter.

Before the brief can be marked Produced:
1. copy the optimized WebP to `biology/images/generated/fauna-mammals.webp`;
2. replace the existing marker at `image-brief-fauna-mammals` without changing its anchor;
3. add concise Russian and English alt text and captions;
4. verify image dimensions, decoding, visible rendering and local path;
5. run the full Biology static checks and Chromium smoke tests.

## Sources

- Kubanychbekov et al. (2026), *Snow Leopard (Panthera uncia) Status in Kyrgyzstan*, Snow Leopard Reports 5(1), DOI: https://doi.org/10.56510/slr.v5.63883 (CC BY 4.0).
- CMS / CAMI, Kyrgyzstan country profile: https://cami.cms.int/country/kyrgyzstan
- Kyrgyz Republic Ministry of Natural Resources, 14 October 2026 field notice reporting snow leopard, argali and mountain goats in their natural mountain habitat in Issyk-Kul Region: https://www.mnr.gov.kg/ru/posts/news/v-issyk-kule-na-video-zapecatleny-sneznyi-bars-arxary-i-gornye-kozly

**Decision:** Candidate visually acceptable as a broad educational habitat reconstruction, subject to repository integration and Chromium QA. Not counted as a completed visual brief yet.
