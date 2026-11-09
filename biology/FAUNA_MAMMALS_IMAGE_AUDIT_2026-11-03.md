# Mountain mammals illustration audit — updated 6 November 2026

**Branch:** `workspace/biology`  
**Chapter:** `chapters/fauna-kyrgyzstan.html`  
**Anchor:** `image-brief-fauna-mammals`  
**Active asset:** `images/generated/fauna-mammals-habitat-reconstruction.svg`  
**Priority:** P1  
**Current disposition:** Original bilingual-context SVG habitat reconstruction is integrated. The former photorealistic WebP candidate is not used and is not the active page asset.

## Evidence and taxonomic scope

The three subjects named in the illustration are:
- Snow leopard — *Panthera uncia*. The 2026 country status paper describes its distribution across the Kyrgyz Tian Shan and Pamir–Alai ranges and gives a primary elevational range of 3,000–4,000 m, while noting records outside that band. This is country-level evidence, not a claim about one exact valley.
- Argali — *Ovis ammon*. The chapter and Kyrgyzstan country material support its presence in high-mountain landscapes. The illustration does not assign a subspecies because argali subspecies treatment remains disputed and requires a stated taxonomic framework.
- Siberian ibex — *Capra sibirica*. The chapter describes this wild mountain goat as characteristic of rocky high-mountain terrain. The drawing distinguishes it from argali through the long swept-back horns and beard rather than the argali's heavy curled horns.

A spatial-modelling study in a specific Kyrgyzstan–Tajikistan study landscape reported local absence of argali from its Kyrgyz portion. This local finding must not be generalized to the whole country. The illustration is not captioned as a record from that landscape or as proof that all three animals were observed together.

## Current SVG and content inspection

The active vector plate is an original, unlabelled educational reconstruction. It shows:
- a snow leopard on a separate rocky ledge, with a pale coat, dark rosette markings and a long thick tail;
- an argali on an open grassy slope, with massive curled horns;
- a Siberian ibex on a distinct steep crag, with swept-back ridged horns and a beard.

The three animals occupy visibly separate habitat sections. The image contains no map pins, range boundaries, counts, conservation symbols or claims of co-occurrence. Its bilingual alt text names the three subjects and explicitly says they occupy separate parts of a mountain landscape. Its bilingual caption says this is a schematic habitat reconstruction, not evidence of observation together at one site.

## Rendered-page QA — 6 November 2026

The current page was inspected in the successful full Biology Chromium screenshot artifact from run #1575:
- **Desktop (1365 px):** the figure loads in the snow-leopard species card; the image and caption remain within the card, with no broken-media or page-overflow defect in the inspected rendering.
- **Mobile (390 px):** the diagram is presented in a horizontally scrollable viewport; the bilingual scroll hint is visible, and the surrounding species card remains within the page column. The initial viewport shows the left portion of the wide diagram, as intended for this scrollable presentation.
- The full Biology workflow completed successfully, including static validation, Chromium tests for every Biology page and screenshot upload.

**Rendered layout disposition: PASS for the inspected desktop and mobile page screenshots.** This is not a certification of every pixel or physical-device behavior.

## Remaining internal checks

- Compare the fine anatomical details of each animal silhouette with the cited species references; the broad distinguishing traits are present, but this audit does not claim exhaustive morphological verification.
- Confirm semantic bilingual equivalence of the caption/alt text as part of the chapter-level language pass.
- Retain the explicit habitat-reconstruction caveat; do not present the composition as a documentary photograph, distribution map, census or co-occurrence record.

## Sources

- Kubanychbekov et al. (2026), *Snow Leopard (Panthera uncia) Status in Kyrgyzstan*, Snow Leopard Reports 5(1), DOI: https://doi.org/10.56510/slr.v5.63883 (CC BY 4.0).
- CMS / CAMI, Kyrgyzstan country profile: https://cami.cms.int/country/kyrgyzstan
- Kyrgyz Republic Ministry of Natural Resources, 14 October 2026 field notice reporting snow leopard, argali and mountain goats in their natural mountain habitat in Issyk-Kul Region: https://www.mnr.gov.kg/ru/posts/news/v-issyk-kule-na-video-zapecatleny-sneznyi-bars-arxary-i-gornye-kozly

**Decision:** Production/integration and inspected responsive layout are complete for this asset. Fine-grained morphology and chapter-level bilingual semantic checks remain internal open items. No external review or sign-off is part of the project.
