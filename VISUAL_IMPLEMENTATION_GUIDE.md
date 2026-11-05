# VISUAL IMPLEMENTATION GUIDE
## Practical workflow for visual content across Atlas of Knowledge

**Document ID:** AOK-IMG-GUIDE-001  
**Version:** 1.0  
**Status:** Mandatory implementation guide  
**Applies to:** Every current and future subject atlas, chapter, language edition, interactive lesson, and visual learning component in Atlas of Knowledge  
**Governing standard:** `IMAGE_FIRST_POLICY.md` (currently v1.1)  
**Canonical location:** Repository root — `VISUAL_IMPLEMENTATION_GUIDE.md`

---

## 1. Purpose and relationship to the universal policy

This guide explains how development teams implement the visual requirements of the universal `IMAGE_FIRST_POLICY.md`. It applies to all disciplines, not to any one subject.

The three canonical documents have different roles:

- **`IMAGE_FIRST_POLICY.md`** defines the universal mandatory rules for all visuals.
- **`AUTHOR_CREATED_VISUALS_STANDARD.md`** adds the mandatory authorship, provenance, licensing, and verification gates for Category C — Created assets.
- **`VISUAL_IMPLEMENTATION_GUIDE.md`** explains the practical workflow for finding, assessing, creating, adapting, integrating, and verifying all visual categories.

Read the applicable standards before work begins. The universal policy takes precedence over this guide; the author-created standard supplements the policy and is mandatory for Category C. Subject-level procedures may add stricter checks but must not weaken these canonical requirements.

## 2. Start with the learning need

Before searching for or creating an asset, identify:

1. Subject, chapter, page, and learning objective.
2. What the learner must understand from the visual.
3. The required visual type: photograph, illustration, diagram, map, chart, graph, timeline, model, animation, or interactive component.
4. Required languages and display contexts (phone, tablet, desktop, and print where applicable).
5. Whether the visual is essential, helpful, or decorative.

Do not add visuals merely to fill space. Each visual must have a clear educational purpose.

## 3. Use the image-first decision sequence

For each missing, outdated, inaccurate, inaccessible, or otherwise unsuitable visual, follow this order:

### Step 1 — Inspect what already exists

- Check the current page, asset folders, source register, and visual audit.
- Confirm whether an existing asset is already suitable and verified.
- Avoid creating a duplicate or replacing a working asset without a clear reason.
- For inherited or derivative material, identify the original source and distinguish unchanged assets from adaptations.

### Step 2 — Search for a suitable reusable visual

Search appropriate authoritative sources before creating a replacement. Depending on the discipline, these may include scientific and educational institutions, universities, museums, government agencies, public data portals, and recognised open-content repositories.

A website or search result is not proof of permission. Verify the licence or permission for the exact asset in accordance with `IMAGE_FIRST_POLICY.md`.

Record the search date, search terms or collections, candidates considered, and the reason for selecting or rejecting them. If no suitable rights-cleared visual is found, record that result rather than implying that a search was successful.

### Step 3 — Choose the implementation route

Use one of the standard categories:

- **A — Original reuse:** use a suitable existing visual without substantive content changes.
- **B — Adapted:** translate embedded labels, annotate, crop, recolour, simplify, combine, or otherwise modify an existing visual. Confirm adaptation rights first and document all material changes.
- **C — Created:** produce a new project-specific visual. Record the actual method, such as original SVG, hand-drawn illustration, code-generated chart, GIS map, 3D render, photography, or AI-assisted generation.

Do not choose category C simply because it is faster than checking whether a suitable reusable visual exists. Do not describe an illustrative or AI-generated image as a real photograph, observation, specimen, or measurement.

### Step 4 — Validate before integration

Check the visual's factual or scientific accuracy, educational suitability, source and rights, language requirements, accessibility, and technical quality. Apply the discipline-specific checks in section 6.

If a required internal check is incomplete, keep it **PENDING**. Do not mark the asset verified based on appearance, filename, or successful upload alone. The scientific/factual reviewer must be competent and distinct from the creator, but may be an internal project reviewer. External specialist review is an additional assurance level, not a publication prerequisite.

## 4. Integrate the visual correctly

For every selected or created asset:

1. Store it in the relevant subject's established asset directory. Do not place subject-owned assets in another discipline's folder.
2. Use a descriptive, stable filename and follow the subject's existing naming convention.
3. Connect the actual file to the intended page or component. A placeholder or empty visual container is not an implementation.
4. Add an accurate caption and meaningful alternative text in every supported language.
5. Translate embedded labels, legends, annotations, and controls where required.
6. Add attribution in the location and wording required by the applicable licence.
7. Preserve source notices and identify material adaptations.
8. Ensure that the visual remains legible and functional on supported screen sizes.
9. Provide a text explanation, long description, or equivalent data/table representation when a complex visual cannot be understood through alternative text alone.

For interactive visuals, also check keyboard operation, visible focus, accessible names, instructions, feedback, and a useful non-interactive alternative where appropriate.

## 5. Keep the audit record up to date

Every subject atlas must maintain its own `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md`, following the universal policy.

For each visual, keep the following information aligned between the asset, source register, and audit:

- stable visual ID, subject, chapter, learning purpose, and exact file path;
- category A/B/C and actual creation or adaptation method;
- original source, creator/rightsholder, exact licence or permission, evidence link, and check date;
- attribution wording and all material changes;
- captions and alternative text for each supported language;
- scientific/factual, rights, language, accessibility, and technical review results;
- reviewer, date, evidence, current status, and unresolved issues.

Use only the lifecycle status vocabulary defined in `IMAGE_FIRST_POLICY.md`: `MISSING`, `FOUND`, `LICENSE_CHECK`, `SCIENTIFIC_CHECK`, `ADAPTED`, `INTEGRATED`, `VERIFIED`, and `REJECTED`.

In reports, describe `VERIFIED` as **INTERNALLY VERIFIED**. Record external specialist review separately; use **EXTERNALLY VERIFIED** only when that independent review has passed and is evidenced. External review is optional and does not block publication of an internally verified visual.

Use `PASS`, `FAIL`, `PENDING`, or justified `NOT APPLICABLE` for individual audit dimensions. Never change a status to `VERIFIED` until every applicable internal check has passed and evidence is recorded.

## 6. Apply discipline-specific checks

The universal workflow is the same for every subject. The expert checks depend on the type of visual.

Examples:

- **Physics:** correct physical model, symbols, formulae, units, axes, scales, vector directions, experimental conditions, and stated limitations. For inherited or derivative atlases, preserve source authorship and do not rewrite protected original content outside the authorised scope.
- **Geography:** projection, coordinate reference system, scale, orientation, boundaries and their dates, data provenance, classification method, units, and satellite/GIS resolution and acquisition date where applicable.
- **Biology:** correct organism identification, anatomy, life stage, taxonomic naming, habitat and location/date where relevant, and responsible handling of sensitive species-location information.
- **Chemistry:** correct molecular structure, bonds, charges, stereochemistry where relevant, reaction conditions, formulae, coefficients, symbols, and units.
- **History and social sciences:** date, place, creator, archive provenance, source context, and clear distinction between primary evidence, reconstruction, interpretation, and illustration.
- **Mathematics and data-focused subjects:** correct calculations, definitions, scales, axes, units, notation, data provenance, and reproducibility.

These examples are not an exhaustive checklist. Each discipline must apply competent subject-matter review. Local supplements may add stricter requirements but may not weaken the universal policy.

## 7. Verify in efficient batches

To reduce repeated work and shorten the validation cycle, work chapter by chapter:

1. Inventory all visual needs in the chapter.
2. Group similar needs (for example, maps, diagrams, charts, photographs, or interactive models).
3. Inspect existing assets and source records before searching for replacements.
4. Search and assess suitable reusable candidates in one batch.
5. Create or adapt only the remaining visuals.
6. Integrate all selected assets and complete their source-register entries.
7. Review all language variants together.
8. Run automated checks for paths, missing files, formats, dimensions, required metadata, and page behaviour.
9. Perform manual checks for accuracy, rights, translation quality, accessibility, and visual comprehension.
10. Update the audit and close the chapter only when its acceptance criteria are met.

Do not postpone source records or audit updates until the end. Record evidence as each visual is processed. This prevents repeated searches and avoids reconstructing provenance later.

## 8. Use automation without overstating its results

Automate repeatable technical checks wherever practical:

- local asset paths resolve and referenced files exist;
- no required asset is missing;
- image and SVG files parse and meet technical requirements;
- source-register and audit records exist and use approved status values;
- required language variants, captions, and alternative text are present;
- pages load without broken images or relevant console errors;
- responsive layouts do not introduce avoidable overflow or clipping;
- interactive visual controls meet applicable keyboard and accessibility checks.

Run the subject's established validation scripts and browser tests after integration. Fix failures or document unresolved blockers explicitly.

Automation can confirm file existence, metadata presence, and many technical behaviours. It cannot, by itself, establish copyright permission, scientific truth, pedagogical quality, translation accuracy, or actual accessibility. Those checks require appropriate human review and evidence.

## 9. Report progress honestly

Report these measures separately for each chapter and for the subject:

- **Image Coverage:** required visuals integrated ÷ all required visuals.
- **Image Verification:** integrated visuals with status `VERIFIED` ÷ all integrated visuals.
- **Image Gaps:** missing visuals, rejected assets awaiting replacement, and other unresolved required visual needs.
- **Review status:** PASS / PENDING / FAIL counts for rights, accuracy, language/accessibility, and technical checks.
- **Asset categories:** counts for A, B, and C.

Do not combine visual readiness with editorial completeness or overall website readiness. Do not report 100% coverage while required visuals are missing or represented by placeholders. Do not report 100% verification while any integrated visual remains unverified. If the visual inventory is incomplete, label the figures provisional and explain the scope.

## 10. Chapter completion checklist

A chapter's visual work is complete only when all applicable items are satisfied:

- [ ] All required visual needs have been identified.
- [ ] Existing suitable assets have been checked before replacements were created.
- [ ] Every required visual is a real, integrated asset; no placeholder is counted as complete.
- [ ] Source, creator/rightsholder, licence or permission, and attribution are documented.
- [ ] Scientific/factual accuracy and educational suitability have been reviewed.
- [ ] All supported language versions, captions, labels, and alternative text have been checked.
- [ ] Accessibility and responsive display have been checked.
- [ ] Automated validation and relevant browser tests pass.
- [ ] Internal subject-matter review is completed by a competent reviewer distinct from the creator, with evidence, role, and date recorded.
- [ ] External expert review, if commissioned, is recorded separately; its absence does not block internal verification or publication.
- [ ] `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md` are up to date.
- [ ] Image Coverage, Image Verification, and Image Gaps are reported separately.

If any applicable item remains open, report the chapter's visual work as incomplete and identify the blocker.

## 11. Onboarding every new discipline

When a new subject atlas is created:

1. Read the current root-level `IMAGE_FIRST_POLICY.md` and this guide before producing or integrating visual assets.
2. Do not copy either canonical document into the subject folder. Link to the root-level documents.
3. Create the subject's own `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md` using the universal requirements.
4. Define the chapter-level visual needs and the discipline-specific expert checks.
5. Establish the asset directory and naming conventions.
6. Add automated checks for the asset types and page structure used by that subject.
7. Apply the workflow from the first visual; do not defer provenance, accessibility, or verification until publication.
8. Record the policy version used in the subject's audit and implementation reports.

The central project team should include this guide and the universal policy in the onboarding instructions for every future discipline. Subject teams may propose improvements through the central integration process; only the canonical root-level documents govern the project.

---

**End of VISUAL IMPLEMENTATION GUIDE v1.1**

This guide describes an implementation workflow. It does not grant rights, prove factual accuracy, or certify any asset. Every visual must be supported by the evidence required in the relevant subject's source register and audit.
