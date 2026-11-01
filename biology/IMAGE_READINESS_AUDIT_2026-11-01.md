# Biology illustration-marker readiness audit — 1 November 2026

Repository: `Ajokendo/Atlas-of-Knowledge`  
Canonical branch: `workspace/biology`  
Scope: all 52 planned illustration markers, their page anchors, briefs, target paths and production status.

## Executive result

The marker system is structurally intact and the briefs have all received their documented brief-level review. The project is **not yet at the stage where any of the 52 raster illustrations can be represented as generated or publication-ready assets**: the generated-image directory does not exist, no raster image files are present in the Biology page set, and all 52 assets remain deferred.

This is not a reason to discard or rewrite the markers. Keep their exact IDs, positions, target filenames and priorities.

## Marker integrity

| Check | Result |
|---|---:|
| Insertion-map rows | 52 |
| Unique marker IDs | 52 |
| Unique target filenames | 52 |
| Matching rows in disposition register | 52/52 |
| Matching page anchors found | 52/52 |
| Markers with Russian and English brief text | 52/52 |
| Markers with non-empty descriptions | 52/52 |
| Marker HTML status | `planned`: 52 |
| Disposition register status | `Deferred`: 52 |
| Generation-plan status | `[~]`: 52 |

All 52 markers were checked in their actual page files. No missing, duplicate or orphaned marker was found. All 52 IDs match the insertion map and the disposition register.

## Review coverage and priorities

| Priority | Count | Review coverage | Production note |
|---|---:|---|---|
| P1 | 13 | 13/13 have a detailed entry in `IMAGE_SCIENTIFIC_REVIEW.md` | Highest value, but each rendered image still needs visual scientific and locality review |
| P2 | 26 | Included in the individual brief review | Produce after P1; follow each topic-specific scientific constraint |
| P3 | 13 | Included in the individual brief review | Lowest priority; generate only when it adds value beyond existing diagrams or interactive models |
| **Total** | **52** | **52/52 briefs reviewed at brief level** | No rendered asset is approved by this review |

The 39 P2/P3 IDs all have matching individual entries in `IMAGE_BRIEF_REVIEW.md`. The 13 P1 target filenames all have matching detailed entries in `IMAGE_SCIENTIFIC_REVIEW.md`. These are reviews of the *briefs and intended visual scope*, not approvals of images that do not yet exist.

## Actual asset inventory

- The Biology root currently contains the `chapters/` directory; no `biology/images/` directory has been committed.
- `biology/images/generated/` is absent. One local-only 1280×720 Batken flora concept preview was created in the working session; it is not in the repository and is not approved.
- Across the 13 pages carrying markers, the audit found 22 inline SVG elements and zero HTML `<img>` elements.
- The 22 SVGs are existing diagrams/visual models, not substitutes for all 52 planned assets.
- The image plan's previous count of 16 inline SVG elements was stale; it has been corrected to 22.
- No target WebP file exists in the generated-image directory because that directory is not present.

## Scientific holds and production cautions

1. **Freshwater fauna of Kyrgyzstan** (`fauna-freshwater.webp`): retain a strict taxonomic hold on disputed `Triplophysa` identifications and unresolved `Diptychus` combinations. Do not add a species count, use the unpublished Kempir-Abad list, or imply that sampled fish records form a complete national checklist.
2. **Batken Aygul / wild tulips** (`flora-batken.webp`): show `Fritillaria eduardii` accurately and separately from wild tulips; do not depict picking, trampling or unsupported public access.
3. **Regional fauna scenes**: a country-level species record is not enough to label a specific oblast or protected area. Follow the locality and habitat constraints in the P1 scientific review.
4. **P3 conceptual assets**: avoid duplicating existing SVG explanations without a clear additional learning benefit.

## Safe next production sequence

1. Verify a complete asset-ingestion route that can place actual binary image bytes at the exact repository target paths, then validate format, dimensions and file integrity.
2. Start with a small P1 pilot whose source constraints are explicit (for example, the regional flora landscapes and the reviewed mountain-mammal/bird compositions). Review each rendered image before committing it.
3. Keep the freshwater-fauna and Batken-plant constraints visible during production; do not bypass the listed scientific holds.
4. For every accepted image, record creator/provenance and licence, exact target path, actual dimensions, Russian and English alt text, caption, reviewer and commit SHA.
5. Replace only the matching `<aside id="image-brief-…">` with a semantic `<figure>` after review. Then update the matching row in the disposition register and generation plan. Never mark a marker complete merely because an image was rendered in a chat.

## Files and preservation

No page marker, anchor ID, target filename, priority or brief was changed. One local draft concept was generated, but it is not a publication asset and no marker was marked complete. Its scientific cautions and integration decision are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`. The exact 52-marker set remains available for production.
