# Biology mobile image review — 6 November 2026

Branch: `workspace/biology`
Evidence: full-page Chromium screenshots, 390 px viewport, successful workflow run [42153779144](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42153779144).

## Sampled opening plates

| Chapter | Observation |
|---|---|
| Anatomy | Organ-systems overview stays within its card; explanatory caption wraps normally. Fine labels inside the plate are too small to read at full-page mobile scale. |
| Biochemistry | Four-biomolecule comparison stays within the card; Russian caption is legible. Embedded bilingual labels are miniature at this scale. |
| Cell Biology | Animal-cell plate, leader lines and labels remain within the card; no visible clipping or overlap. Internal labels are not comfortably readable at full-page scale. |
| Evolution | Phylogenetic tree, branch labels and explanatory text remain within the card. No new clipping or collision was confirmed. |
| Genetics | DNA-packaging plate and central-dogma diagram remain within the mobile column. The previously corrected footer/replication-curve separation is visible; no new collision was found. |
| Microbiology | Bacteria-versus-virus plate remains within the card. Caption distinguishes cellular bacteria from acellular viral particles; fine internal labels remain small. |
| Systematics | Three-domain comparison remains within its card; explanatory caption is legible. Internal panel text is too small for comfortable reading at full-page scale. |
| Zoology | Vertebrate comparison and classification diagram remain within the content column; no new clipping or overlap was confirmed. Internal labels are very small. |

## Result and limits

No new confirmed structural layout defect was established in these sampled opening plates. A recurring mobile legibility limitation is present for dense embedded SVG labels. This is an asset-level readability follow-up, not evidence that the figures are scientifically incorrect or that every label fails. Captions and surrounding prose remain readable but do not replace checking whether essential diagram labels can be read on a phone.

This is a targeted sample, not complete asset-by-asset acceptance. It does not certify every label, caption, source attribution, licence, scientific claim or bilingual string. Global Image Verification remains **Pending audit**; no per-asset VERIFIED status is inferred.

## Follow-up remediation — regional SVG inspection on mobile, 6 November 2026

The full-page 390 px Chromium screenshots exposed a recurring limitation: dense embedded labels in the regional SVG diagrams were too small at their normal responsive fit. The captions remained readable, but that did not make the labels inside the artwork legible.

**Implemented on `workspace/biology`:**
- 12 regional fauna SVGs and 3 regional flora SVGs now use a 720 × 405 px horizontally scrollable inspection viewport at narrow mobile widths.
- Each viewport is keyboard-focusable and exposed as a named region with a bilingual accessible label.
- A visible Russian/English instruction now tells mobile readers to scroll horizontally to inspect the diagram labels.
- Grid items and figure containers are constrained so the enlarged diagram does not widen the page itself.

**Automated evidence:**
- [Run #1528](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42170869929) — completed `success`; the 13-page Chromium smoke suite confirmed no page-level horizontal overflow after the viewport-width correction.
- [Run #1529](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42171194427) — completed `success`; fauna scroll guidance and responsive layout passed.
- [Run #1530](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42171199947) — completed `success`; flora scroll guidance and responsive layout passed.
- [Run #1531](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42171211457) — keyboard/scroll interaction regression test is still in progress at the time of this note.

This closes the specific mobile page-overflow defect and adds enlarged scrollable inspection viewports to 34 regional/core SVG diagrams. It does **not** mark those 15 assets `VERIFIED`: detailed scientific morphology, caption/alt semantic equivalence, and all remaining per-asset checks still require their own evidence. To address the same sampled core-chapter readability limitation, 19 additional SVGs across Anatomy (3), Biochemistry (3), Cell Biology (4), Microbiology (3), Systematics (3) and Zoology (3) now also use enlarged scrollable mobile viewports with bilingual hints. A shared `biology/diagram-scroll.js` handler adds explicit ArrowLeft/ArrowRight operation to all 34 regional/core viewports. The dedicated end-to-end keyboard-scroll test is [run #1554](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42172024322) and remains in progress at this note; no keyboard-scroll pass is claimed until it completes.

Global Image Verification remains **Pending audit**. The 53/53 count remains production/integration coverage only; no per-asset verification percentage or 100% whole-atlas readiness is inferred.

