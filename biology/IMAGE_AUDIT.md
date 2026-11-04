# Biology image audit

**Policy:** Atlas of Knowledge IMAGE-FIRST POLICY v1.0  
**Branch:** `workspace/biology`  
**Audit baseline:** 5 November 2026  
**Scope:** all 53 mapped visual briefs and the currently integrated image assets.

This is the consolidated audit and remediation tracker. It separates asset production from scientific, legal, bilingual and technical verification. The per-asset `IMAGE_DISPOSITION_REGISTER.md` remains the authoritative 53-row inventory.

## 1. Executive status

| Measure | Current evidence-based status |
|---|---|
| Mapped visual briefs | 53 |
| Produced or integrated | 53/53 (100% production/integration coverage only) |
| Register disposition | 47 labelled Produced; 6 labelled Integrated |
| Deferred production briefs | 0 in the current disposition register |
| Documentary third-party photographs | 15 across five regional briefs |
| Original project SVG artwork | Recorded throughout the disposition register |
| Full 13-page Chromium/axe CI | Passed in run [41822905607](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41822905607) |
| Detailed visual review | Not complete for all assets; individual register rows retain pending notes |
| Hands-on physical-device / screen-reader testing | Not performed; tracked separately in `SCREEN_READER_AND_DEVICE_TEST_PLAN.md` |
| Independent specialist review | Not commissioned; do not describe author-side review as independent certification |

**Important:** 53/53 means every mapped brief has a produced or integrated asset. It does not mean 53/53 assets have passed every IMAGE-FIRST acceptance gate. Do not report Image Verification as 100% on the basis of production coverage or CI alone.

## 2. Image categories

- **A — Original:** an unmodified third-party original. The accepted Commons photographs are category A at source level.
- **B — Adapted:** a third-party image that has been cropped, translated, retouched, annotated or otherwise modified. JPEG-to-WebP format conversion without content changes is recorded as a technical derivative; preserve the source identity and document the conversion.
- **C — Created:** original Atlas of Knowledge artwork, including authored SVG teaching diagrams. Historical AI concept drafts are not approved production assets.

The register and source audits identify 15 source-backed documentary photographs and original SVG diagrams. If a third-party image is materially cropped, relabelled or annotated in a future change, update its category and modification record.

## 3. Scientific audit

### Existing evidence

- `IMAGE_SCIENTIFIC_REVIEW.md` contains the 13 P1 Kyrgyzstan flora/fauna visual constraints.
- `IMAGE_BRIEF_REVIEW.md` records brief-level constraints for all 53 mapped anchors and explicitly distinguishes brief review from actual rendered-asset review.
- Regional photo audits restrict captions to what the source image and locality evidence support.
- The image register records known limitations, including schematic/not-to-scale labels, generic species silhouettes, habitat separation and unsupported range claims.

### Required remediation

For every individual asset, confirm the actual rendered image against the relevant brief and chapter, not only the text prompt or planned composition. Explicitly inspect:

- morphology and taxonomic diagnostic features where a species is named;
- scale, proportions and spatial relationships;
- process, force, flow and movement direction;
- time/season and geographic scope;
- legends, symbols, colour scales and units;
- whether the image could imply unsupported abundance, continuous distribution or a false real-world observation.

**Current result:** author-side brief/scientific constraints are documented; this consolidated pass does not claim independent expert validation of all 53 final rendered assets. Rows with pending visual/morphology notes remain open for focused human review.

## 4. Legal and provenance audit

### Evidence found

The five documentary-photo briefs have dedicated source audits and local asset manifests:

- Chüy fauna: six photos; `FAUNA_CHUY_SOURCE_AUDIT_2026-11-03.md`, `images/generated/fauna-chuy-assets-manifest.json`.
- Jalal-Abad flora: one photo; `FLORA_JALALABAD_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-jalalabad-asset-manifest.json`.
- Issyk-Kul flora: four photos; `FLORA_ISSYK_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-issyk-assets-manifest.json`.
- Naryn flora: three photos; `FLORA_NARYN_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-naryn-assets-manifest.json`.
- Osh flora: one photo; `FLORA_OSH_IMAGE_AUDIT_2026-11-03.md`, `images/generated/flora-osh-asset-manifest.json`.

The source audits record individual file pages, creators, licence choices, dates/locations, dimensions and original-file checksum comparisons. The local derivative checksums are also recorded in manifests.

### Required remediation

- Keep the source file page and exact licence version for every third-party file.
- Confirm that each live figure's attribution is visible or reachable from the caption and includes all required elements.
- Preserve modification notes, especially if a future crop, translation or annotation changes the source image.
- Do not infer rights from the host website or from search-result availability.
- Resolve any mismatch between the live caption and source record before marking the asset VERIFIED.

**Current result:** source and licence evidence is documented for the 15 accepted documentary photographs. Original SVG artwork is project-authored according to the disposition register. This audit does not assert that every caption has been re-opened and compared against the current live source page on 5 November; revalidation is required when a source or asset changes.

## 5. Bilingual and accessibility audit

The image programme uses bilingual captions and alt text in the chapter figures. The full browser suite has checked alt-attribute presence and image loading, but presence alone does not prove that alt text is useful or semantically equivalent.

For each figure, verify:
- RU and EN captions communicate the same scientific claim and qualification;
- RU and EN alt text describe the same essential visual information;
- species names, units, symbols and formulae are consistent;
- text inside SVG remains legible at narrow viewport sizes and 200%/400% zoom;
- colour is not the only way to distinguish categories or processes;
- decorative artwork has empty alt text where appropriate, rather than redundant prose.

**Current result:** bilingual content and structural checks exist; full semantic pair-by-pair human review of all captions and alt descriptions remains a focused audit item. Do not mark all images bilingual-verified based solely on the existence of both language blocks.

## 6. Technical audit

### Automated evidence

Full browser/axe/Chromium CI run [41822905607](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41822905607) passed for all 13 Biology HTML pages. It included 390×844 and 1365×900 viewport checks, bilingual switching, keyboard checks, axe accessibility checks, contrast sampling, raster decode/dimensions/alt-attribute checks and non-zero inline-SVG geometry.

### Limits

- This is headless browser evidence, not physical-device testing.
- A decoded raster or non-zero SVG box does not prove that text is readable or that the scientific artwork looks correct.
- It does not establish offline caching.
- It does not replace NVDA, TalkBack or VoiceOver testing.
- It does not verify every source link's current legal metadata.

**Current result:** automated loading and basic rendered-geometry checks passed on the tested revision. Detailed visual review, physical-device testing and screen-reader sessions remain separate.

## 7. Current gaps and remediation queue

| Gap | Scope | Required action | Closure evidence |
|---|---|---|---|
| Focused final-art visual inspection | Assets with pending notes in `IMAGE_DISPOSITION_REGISTER.md` (33 rows explicitly retain pending visual/morphology/browser notes at this baseline) | Inspect actual rendered asset at desktop and narrow mobile widths; compare with approved scientific brief | Dated pass/fail entry per asset |
| Scientific morphology / scene review | Species-specific and regional wildlife/plant visuals | Verify diagnostic features, locality claims and ecological relationships; keep generic labels where identification is uncertain | Reviewer, evidence/source and decision |
| Bilingual semantic equivalence | All figures with RU/EN text | Compare caption, alt text, embedded labels, units and scientific names | RU/EN audit result per asset |
| Live attribution comparison | Third-party photo figures | Compare visible credit/source/licence links with the individual source page and licence terms | Dated rights check per source |
| Physical-device / assistive technology | 13 pages | Execute the separate manual test plan in the actual environments | Completed test record; never infer from CI |
| Offline availability | Local images and any future remote assets | Test offline behaviour only if offline support is an intended feature | Explicit result; currently not tested |

The count of 33 is derived from rows that explicitly retain pending visual, morphology or browser-validation notes in the current register. It is a triage count, not a claim that the remaining 20 have passed every manual gate.

## 8. Status vocabulary and acceptance rule

Use these statuses in future asset records:

- `FOUND` — candidate located; not approved.
- `LICENSE_CHECK` — rights evidence is being checked.
- `SCIENTIFIC_CHECK` — scientific content is being checked.
- `ADAPTED` — adaptation completed and documented.
- `INTEGRATED` — file inserted at the intended chapter anchor.
- `VERIFIED` — scientific, legal, bilingual and technical checks all passed.
- `REJECTED` — candidate must not be used.
- `MISSING` — required visual remains absent.

The existing legacy terms Produced/Integrated are retained in the historical register for continuity. Do not silently translate Produced or Integrated into VERIFIED. As assets are rechecked, add the new status and evidence without deleting historical production records.

### Check-result vocabulary required by IMAGE-FIRST v1.0

For each applicable scientific, legal, bilingual and technical check, record one of these explicit results:

- `PASS` — the check was performed and passed.
- `FAIL` — the check was performed and a blocking issue was found.
- `PENDING` — the check has not yet been completed.
- `NOT APPLICABLE` — the check does not apply; give a short reason.

Do not infer PASS from the absence of a reported defect. The asset lifecycle status `VERIFIED` may be assigned only when all applicable checks are PASS and each NOT APPLICABLE result is justified. The current 53/53 production/integration count is not an Image Verification score.

## 9. Chapter-level metrics

Report these separately:

- **Image Coverage:** integrated required visual briefs / all required visual briefs × 100%.
- **Image Verification:** assets marked VERIFIED / integrated assets × 100%.
- **Image Gaps:** number of required briefs still missing or requiring replacement.

**Current measured values (5 November 2026):**

- **Image Coverage: 100% (53/53).** A direct scan of all 13 Biology HTML pages found 53 semantic `<figure>` elements at the mapped image anchors and zero remaining image placeholders.
- **Image Verification: Pending audit (percentage not yet defensible).** The register still contains 33 rows with explicit pending final visual, morphology or browser-review notes. No 100% verification claim is permitted until every applicable per-asset human check is recorded.
- **Image Gaps: 0 confirmed missing required briefs/assets.** This is a production-gap count only; an asset may still require correction or replacement if its pending scientific or visual review fails.

These three measures are deliberately separate. The 53/53 figure count establishes integration coverage, not scientific/legal/bilingual verification.

## 10. Audit history and scope boundary

This audit is an author-side project audit, not independent specialist certification. It does not alter the scientific content or claim new expert review. All changes in this pass are confined to `biology/` on `workspace/biology`; no main branch, other subject, shared portal or publishing configuration is changed.

**Next action:** close the focused per-asset review queue in batches, updating the source register and this audit with dated evidence. Do not generate replacement images merely to clear a pending status; reuse suitable existing assets or correct the record where appropriate.
