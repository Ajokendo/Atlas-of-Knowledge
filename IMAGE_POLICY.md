# IMAGE-FIRST POLICY — Atlas of Knowledge: Physics

**Status:** mandatory editorial and technical quality-control standard  
**Scope:** this Physics branch only  
**Applies to:** every chapter, the catalogue, interactive laboratories and supporting learning materials

## Core rule

Search for an existing scientific image before creating a new one. Verify scientific accuracy and reuse rights before integration. Create a new visual only when a suitable, legally reusable and scientifically reliable asset cannot be found, or when the learning objective requires a genuinely original composition.

A freely accessible image is not automatically free to reuse. The fact that Atlas of Knowledge is free to access does not remove licence conditions.

## Required workflow

1. **Define the visual requirement.** Record the chapter, learning objective, objects/processes to show, required labels, viewpoint, level of detail, language and mobile-display needs.
2. **Search trusted collections.** Prioritise scientific museums, universities, peer-reviewed publications with reusable figures, open educational resources and established public image libraries. Search for the original asset page, not merely a search-engine thumbnail.
3. **Review scientific accuracy.** Check object identity, proportions, direction of processes, scale, terminology, units, labels and consistency with the chapter text. For diagrams, verify the underlying scientific model, not just visual appearance.
4. **Review the exact licence.** Confirm the licence on the individual asset page and retain evidence of the source and conditions. Check whether online redistribution, modification, cropping, translation and commercial reuse are allowed or restricted.
5. **Check technical suitability.** Prefer the original downloadable file, adequate resolution, readable labels, accessible contrast, no watermark, and responsive display. Do not remove watermarks or creator credits.
6. **Integrate and attribute.** Store the asset in the Physics subject area, preserve the original where practical, add bilingual captions and alt text, and record all required attribution and licence information in `IMAGE_SOURCES.md`.
7. **Validate in context.** Check that the image loads, remains legible on narrow screens, has meaningful alt text, and is placed next to the correct explanation.
8. **Create only if needed.** If no suitable asset passes the scientific, rights and technical checks, document the search/disposition decision. Prefer a hand-authored SVG or HTML/CSS diagram for precise educational schematics. Use image generation only for a justified original composition and scientifically review the result before publication.

## Licence decision guide

| Licence / status | Default handling |
|---|---|
| Public Domain / CC0 | Usually reusable; still record source and creator when known. Check for third-party elements. |
| CC BY | Reuse and adaptation generally permitted with required attribution and licence notice. |
| CC BY-SA | Reuse/adaptation generally permitted; comply with ShareAlike conditions for adaptations. |
| CC BY-NC | Do not use unless the project has confirmed that the specific use qualifies as non-commercial under the licence. |
| CC BY-ND | Do not crop, translate, remix or otherwise distribute an adapted version without permission. Use unchanged only where the licence permits the intended redistribution. |
| All Rights Reserved / unclear terms | Do not integrate without explicit permission. Find an alternative. |

This table is a screening guide, not a substitute for checking the exact licence and any third-party rights on the original asset page. When uncertain, do not use the asset.

## Preferred source families

- Wikimedia Commons — inspect the individual file page and licence, not only the collection.
- NASA Image and Video Library — check the item page, credits and any third-party copyright notices.
- OpenStax — check the licence of the specific book/edition and any excluded third-party figures.
- USGS Multimedia — check item-specific public-use and credit conditions.
- NOAA Multimedia — check item-specific credits and third-party restrictions.
- University, museum and journal repositories — use only where the individual asset's reuse terms are explicit.

These are discovery starting points, not blanket permissions.

## Physics-specific selection guidance

| Visual type | Preferred approach |
|---|---|
| Real experiments and apparatus | Existing photographs from a reliable scientific or educational source, with licence review. |
| Historical instruments | Museum collection images with item-level credit and rights information. |
| Physical phenomena in nature | Original scientific photographs or institutional archives. |
| Force diagrams, vectors and free-body diagrams | Accurate hand-authored SVG/HTML where this gives clearer labels and controllable geometry. |
| Graphs, plots and quantitative relationships | Generate from verified data or equations in code; label axes, units and assumptions. |
| Three-dimensional interactive scenes | Use the existing validated interactive model where appropriate; do not add a decorative image as a substitute for a functioning model. |
| Bilingual educational infographics | Compose with SVG/HTML/CSS using verified content; generate an image only if the required composition cannot be built reliably. |

Never present a generated image as evidence of a real experiment, apparatus, physical structure or measured result. Clearly distinguish illustrative models from real photographs and measured data.

## Required asset metadata

Every integrated asset must have an entry in `IMAGE_SOURCES.md` containing:

- chapter and learning objective;
- local file path and original source URL;
- creator/author, if stated;
- exact licence and licence URL;
- access date (ISO format);
- Russian and English captions;
- Russian and English alt text;
- whether and how the asset was modified;
- scientific review status and reviewer/check notes.

Do not invent missing authors, dates, licences or permissions. Mark a field as unknown and keep the asset out of publication until its rights are resolved.

## Quality-control metrics

Report these three counts separately for each subject and reporting period:

1. **Found and integrated** — external assets with completed scientific and licence review, integrated into the atlas.
2. **Independently created** — report subcategories separately: authored SVG/HTML/CSS diagrams, code-generated plots, and AI-generated images.
3. **Outstanding** — visual requirements not yet resolved and integrated.

Do not count search results, unverified candidates, placeholders or merely planned images as integrated assets. Do not count one asset more than once. An asset is complete only when its source/rights record and on-page integration are both present.

## Completion checklist

- [ ] Requirement and chapter recorded.
- [ ] Original source page located.
- [ ] Scientific accuracy reviewed.
- [ ] Exact licence and permitted use verified.
- [ ] Original file obtained without removing credits or watermarks.
- [ ] Bilingual caption and alt text added.
- [ ] Entry added to `IMAGE_SOURCES.md`.
- [ ] Asset stored in the Physics area.
- [ ] Desktop and mobile rendering checked.
- [ ] Three quality-control metrics updated.

**Branch isolation:** make Physics changes only in `workspace/physics`. Do not modify the English source project, other subject branches, the common portal, or publishing settings as part of this policy work.
