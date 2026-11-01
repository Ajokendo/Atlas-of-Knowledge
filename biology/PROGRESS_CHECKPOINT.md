# Biology development checkpoint

**Date:** 1 November 2026  
**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Canonical branch:** `workspace/biology`  
**Working area:** `biology/` only  
**Controlled editorial readiness:** **95/100** (not publication approval)

## Gate status

- **G1–G3:** closed; the recorded GitHub Actions run #41275274366 passed the static and Chromium checks for its tested commit. The bilingual structural parity audit was also covered by run #41275876545.
- **G4:** open — independent scientific review and qualified sign-off are still required.
- **G5:** open — independent bilingual/editorial and release review are still required.
- **G6:** closed as an explicit deferral decision only. All 52 visual assets remain deferred; no image is represented as generated or integrated.

## Latest saved development

- Ecology productivity and trophic efficiency: `e2cb743769ec6f30c1c82633f6b2e8e58ade1e29`.
- Evolution speciation and reproductive isolation: `1124de622af9878799cbddeaebe7cc0038894580`.
- Microbiology horizontal gene transfer: `f183a91c8e90dfb32f29edca02f4f73e90fe783d`.
- Genetics gene regulation and epigenetics: `a53317046d14b6d939de0e295732e4404d44bc6c`.
- Regression assertions for these four sections in `checks.mjs`: `6fede848c410135dccd164f87aabf6f682f7227b`.
- Development record in `README.md`: `48efd57ec0a90fef832924ca9e368ee03820c38e`.

## Preservation and verification

- The 52 exact `image-brief-*` insertion anchors remain in the chapters and match the 52 rows in `IMAGE_INSERTION_MAP.md` and the 52 Deferred rows in `IMAGE_DISPOSITION_REGISTER.md`.
- Focused source-level verification passed for all four new lessons, their bilingual blocks, key scientific distinctions and section ordering.
- The regression assertions are committed. The full Node suite, Chromium smoke suite and CI have **not** yet been rerun against these latest commits.
- No branch merge, deletion, or change outside `biology/` was made.

**Next milestone:** raise the controlled score only when evidence closes the outstanding gates; do not increase the percentage merely because additional content or commits were added.

## Subsequent genetics extension

- Added a bilingual Mendelian inheritance lesson with genotype/phenotype, allele segregation, a semantic Punnett square for `Aa × Aa`, and explicit limits of simple dominance models.
- Chapter commits: `58fb4df00485a74db502973bb29b5a4481710fc2`, `ac6f6a937e5dfc8f76b3f96453167d1869e6e5e4`.
- Regression assertion commit: `0947593055409086a77245a376b5f2302767c665`.
- Development log updated in README commit: `cd773c5c7ff380cd581aaeab233ccaf6583e936b`.
- Image anchors remain preserved: 52 mapped, 52 deferred. The controlled score remains 95/100 until G4/G5 independent review is completed.

## Cell biology extension

- Added bilingual cell communication and signal-transduction content: four major signalling modes, receptor activation, relay proteins, second messengers, amplification, feedback and cross-talk.
- Added an accessible SVG pathway overview with `title`, `desc` and `aria-labelledby`.
- Chapter commit: `d7c3c181dc3c5f486d3cabf78ce2fb0da9c496b9`.
- Regression checks commit: `bd0009d56bace3c1b20f11012ed5d6e61151d6e6`.
- README record commit: `f8d2c893afc4dc31adddd24a330926b8b9b0bc1f`.
- Focused source-level verification is pending final read-back; full Node.js, Chromium and CI suites have not been rerun. Readiness remains 95/100; G4/G5 are open.

## Further cell-biology coverage

- Added bilingual material on cell-cycle checkpoints (G1/S, G2/M and spindle assembly), cyclin–CDK control, DNA-damage responses, apoptosis and necrosis, and the multifactorial nature of tumour development.
- Chapter commit: `f96f28c4386afca6e23437d0aedc14bc49233323`.
- Regression test commit: `6d680c4e08ea76372b9232bd2b00c6eb58622707`.
- README log commit: `4d02c2b3ba0133f9ebd35b2647de336623582f4f`.
- Focused source read-back and full test execution are pending. No readiness increase is claimed; G4/G5 remain open.

## Anatomy and physiology extension

- Expanded the homeostasis section with bilingual explanations of negative-feedback control loops, receptor/integrator/effector roles and normal physiological ranges.
- Added thermoregulation, insulin/glucagon blood-glucose regulation, vasopressin-mediated water balance, and bounded positive-feedback examples (labour and clotting).
- Added an accessible SVG control-loop diagram with bilingual labels, title and description.
- Chapter commit: `851d39f57321940c90562b681fd59b7578b2895e`.
- Regression checks commit: `4cc01025f6066befd783b9b745747392ae14cbab`.
- README log commit: `05f553bdb0cff315e0695bbdfd337f28b81b5abd`.
- Focused source read-back is pending. Full Node.js, Chromium and CI suites have not yet been rerun. Readiness remains 95/100; G4/G5 remain open.


## Renal physiology extension

- Added a bilingual nephron and renal-regulation lesson covering filtration, selective reabsorption, secretion, aldosterone, vasopressin and RAAS.
- Added an accessible nephron SVG with bilingual title/description and regression assertions for placement, mechanisms, bilingual content and scientific caveats.
- Chapter commit: `029a51f04974c6e6c1a06065bdec60c8bd1f09c5`. Nephron flow-arrow refinement: `a85f987c716a5d71cda01a11bdc99a5b80e53de8`.
- Regression-check commit: `c3a24ceae7d3b933118ab5f9cdd9a5bb7de7d99c`.
- README log commit: `9becc8851d4792dbe368e367ad867fb489a012af`.
- Full Node.js, Chromium and CI checks have not yet been run on these latest commits. Controlled readiness remains 95/100; G4/G5 remain open. Existing 52 image anchors and their Deferred dispositions are unchanged.


## Cardiovascular physiology extension

- Added bilingual coverage of the cardiac cycle, stroke volume, cardiac output, electrical conduction, baroreceptor reflex and the interaction of cardiovascular regulation with renal RAAS and vasopressin mechanisms.
- Added an accessible bilingual SVG diagram of the cardiac conduction pathway.
- Chapter commit: `af8a0108af71f0c93d10ff2b70dddb1be04cacd1`.
- Regression-check commit: `55a7262c61db31b4d6d6ea3d5dc14bfe8a30b0dd`. Boundary correction in regression assertions: `3ca37b077b4cd0ab829394e1b562843f6f495b48`.
- README log commit: `14ec92f2f088447a0383991f59432cb40ab45e7d`.
- Full Node.js, Chromium and CI checks have not yet been run on these latest commits. Controlled readiness remains 95/100; G4/G5 remain open. Existing 52 image anchors and Deferred dispositions are unchanged.


## Illustration production pilot — 1 November 2026

- Began the P1 image pilot with a local Batken flora concept preview (1280×720, WebP). The image pairs an Aygul-like fritillary with an unlabeled generic wild tulip; generated labels were removed.
- The candidate is not committed to the repository, not integrated into the chapter and not approved. The wild-tulip morphology is unverified against the Batken taxa listed in the chapter; Aygul nomenclature must follow `Petilium eduardii`.
- See `IMAGE_DRAFT_REVIEW_2026-11-01.md`. The `image-brief-flora-batken` anchor and all 52 Deferred statuses remain unchanged.
- No publication gate is closed; controlled readiness remains 95/100, G4/G5 remain open.


## Second illustration production attempt — 1 November 2026

- Generated a mountain biodiversity concept collage (ImageGen generation ID `decb1eeb-b86a-4b4c-abc7-9d6e5efcdd66`) and cropped three local WebP review candidates: snow-leopard-like cat (500×500), golden-eagle-like raptor (496×500), and unidentified horned mountain ram (498×500).
- All three remain local-only drafts. They are not field photographs, do not establish a Kyrgyzstan locality, and have not passed zoological review. The ram is not identified as argali or any subspecies.
- Updated `IMAGE_DRAFT_REVIEW_2026-11-01.md` with generation provenance, exact local filenames/dimensions and scientific holds. README records the pilot.
- No raster image has been added to GitHub or inserted into a chapter. All 52 markers remain Deferred; no marker, target filename or anchor changed.
- Controlled editorial readiness remains **95/100**. G4 and G5 remain open. No new test or CI success is claimed.


## Third illustration production attempt — 1 November 2026

- Generated one six-panel alpine biodiversity concept collage (ImageGen generation ID `d34da22d-d7e5-4247-9be9-e2f29d102e1a`) and split it into six local WebP review candidates: snow-leopard-like cat, eagle-like raptor, argali-like ram, partridge-like bird, unidentified marmot and unidentified butterfly.
- Exact filenames and pixel dimensions, plus taxonomic cautions, are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`. These are generated concepts, not field records or verified locality evidence.
- No raster asset was added to GitHub or integrated into a chapter. All 52 markers remain Deferred; no marker or target path changed.
- Controlled readiness remains **95/100**. G4/G5 remain open. No test or CI success is claimed.


## Fourth illustration production attempt — 1 November 2026

- Produced one new local WebP candidate from the fourth generated collage: an unidentified edelweiss-like alpine flower (503×507). Its morphology requires botanical review; no genus, species or Kyrgyzstan locality is asserted.
- Provenance and scientific hold are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`. Repeated wildlife panels were not treated as new assets.
- No image was committed or integrated. All 52 markers remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No new tests or CI runs are claimed.


## Fifth illustration production attempt — 1 November 2026

- One new local candidate extracted: `biology-red-bell-alpine-flower-candidate.webp` (505×504). It is an unidentified red bell-shaped alpine flower concept; species/genus attribution is withheld pending botanical review.
- Provenance and scientific caveats recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`. No asset committed or inserted; no marker changed.
- Controlled readiness remains **95/100**. G4 independent scientific review and G5 independent bilingual/editorial/release review remain open. All 52 image dispositions remain Deferred. No tests/CI were run or claimed in this stage.


## Sixth illustration production attempt — 1 November 2026

- Added one standalone local WebP botanical candidate (1254×1254), a red-orange crown-like alpine flower. It remains taxonomically unidentified pending botanical review; the setting is illustrative.
- Generation provenance, filename, size and caveats are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- No raster was committed or inserted; no marker changed. All 52 dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests or CI were run in this stage.


## Seventh illustration production attempt — 1 November 2026

- Added one distinct standalone local WebP wildlife candidate: snow-leopard-like large cat, 1254×1254. Generation provenance and scientific caveats are in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- Candidate is not a field record and is not committed or inserted. A repeated flower motif from the preceding generation was excluded from the candidate count.
- No insertion marker changed; all 52 dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run in this stage.


## Illustration quality-control audit — 1 November 2026

- Three additional generation attempts repeated the existing snow-leopard scene and were rejected as duplicates; they are not counted as new assets.
- Audited the P1 `fauna-birds.webp` insertion brief against the actual fauna chapter. The named examples include golden eagle (`Aquila chrysaetos`), bearded vulture (`Gypaetus barbatus`), Himalayan snowcock (`Tetraogallus himalayensis`) and black stork (`Ciconia nigra`), plus separately described wetland birds. The intended plate must preserve distinct cliff, alpine and wetland settings.
- This was a quality-control/documentation checkpoint, not a completed illustration. No image was committed or inserted. All 52 markers remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests or CI were run.


## Eighth illustration production attempt — 1 November 2026

- Produced one distinct local horizontal WebP candidate: a large eagle in flight over alpine mountains (1536×1024). It is intended as a golden-eagle concept, but requires ornithological review before taxonomic labelling.
- Generation provenance and caveats are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`. The asset is local-only, not committed or inserted.
- No marker changed; all 52 image dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## Ninth illustration production attempt — 1 November 2026

- Generated a local perched golden-eagle concept variant (1536×1024; ImageGen provenance and review caveats are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`). This is a visual variant of the eagle subject, not a new taxon and not completion of the P1 bird plate.
- The WebP remains local-only, uncommitted and uninserted. No chapter content or image marker was changed.
- All 52 dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## Tenth illustration production attempt — 1 November 2026

- Generated a local bearded-vulture-like alpine bird concept (1536×1024). ImageGen provenance and scientific caveats are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- Candidate remains local-only, uncommitted, uninserted and unapproved. It is not evidence of a Kyrgyzstan field record and does not complete the multi-species P1 bird plate.
- No marker changed; all 52 dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## Illustration duplicate-control checkpoint — 1 November 2026

- Three additional bird-image generations repeated the same perched bearded-vulture motif and were rejected as near-duplicates. No candidate count, filename, insertion anchor or disposition was added or changed.
- Next intended distinct subject: Himalayan snowcock (`Tetraogallus himalayensis`); the generation queue did not yet produce a distinct usable draft.
- All 52 image dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## Gamebird illustration quality-control — 1 November 2026

- Two attempted gamebird illustrations did not produce a reliable Himalayan snowcock depiction: one was monal-like and the other chukar/partridge-like, duplicating an existing concept. Both were rejected and not counted as new assets.
- No raster asset was committed or inserted; no marker changed. All 52 dispositions remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## Image-disposition wording correction — 1 November 2026

- Recorded another rejected monal-like gamebird duplicate in the image review log; no new candidate was accepted.
- Corrected the disposition register to distinguish local-only concept drafts from approved, committed and integrated publication assets. No approved raster image is present in `biology/images/generated/`; all 52 mapped assets remain Deferred.
- Controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## User-provided bird image review — 1 November 2026

- Reviewed a user-provided bird image as a possible Himalayan snowcock visual study. A local WebP review copy was created; it remains uncommitted and uninserted.
- Plumage has some relevant high-altitude gamebird traits, but visible throat/face markings do not clearly match the regional adult description for `Tetraogallus himalayensis`. Species identity, local subspecies context, authorship/licence and provenance require verification. The single-bird image cannot complete the mapped multi-habitat 16:9 plate.
- No marker or disposition changed. All 52 assets remain Deferred; controlled readiness remains **95/100**; G4/G5 remain open. No tests/CI were run.


## Eleventh illustration production attempt — 1 November 2026

- Produced one distinct local horizontal WebP candidate for the wetland component of the P1 bird plate: `biology-black-stork-wetland-candidate.webp` (1672×941), a black-stork-like bird at an alpine lake shore. Generation provenance, visual review and regional habitat references are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- The candidate is generated concept art, not a field photograph; species/anatomical review remains open. It is local-only, uncommitted, uninserted and unapproved. The cliff-raptor and alpine-ground-bird components are still required.
- No image marker, target path or disposition changed. All 52 mapped assets remain Deferred. Controlled readiness remains **95/100**; G4/G5 remain open. No tests or CI were run in this stage.


## Full repeat audit — 5% milestone — 1 November 2026

- Unified editorial, scientific, technical and visual repeat audit started for all 13 Biology HTML pages and the interactive/visual asset system.
- Inventory pass: 13 pages identified (index, ten core chapters, two Kyrgyzstan regional chapters); balanced RU/EN marker counts; no duplicate HTML IDs in source scan; 22 inline SVG elements; no integrated raster `<img>` elements.
- All 52 image markers remain mapped and Deferred. No image asset was approved or integrated. G4/G5 remain open.
- Audit report: `REPEAT_AUDIT_2026-11-01.md`. Audit completion 5%; controlled editorial readiness remains 95/100 and is not recalculated by inventory alone.
- No chapter content or tool logic changed in this milestone. Fresh Node/Chromium execution is pending.


## Full repeat audit — 10% milestone — 1 November 2026

- Completed source-level technical/accessibility review across all 13 HTML pages and inspected the committed `checks.mjs` regression suite.
- One H1 and populated H2 hierarchy per page; all 22 SVGs have accessible names; no unlabeled inputs or external `_blank` links missing `noopener`; buttons have explicit types and visible labels.
- Existing bilingual parity audit: 1,147 RU / 1,147 EN blocks, with numeric and scientific-name parity in its measured scope. Not independent editorial approval.
- No confirmed source defect found; no speculative code edit made. Fresh Node/Chromium tests and browser/manual accessibility tests remain pending; no test pass is claimed.
- Full report: `REPEAT_AUDIT_2026-11-01.md`. Audit completion 10%; controlled readiness remains 95/100; G4/G5 remain open.


## 15% milestone — interactive quiz state audit — 1 November 2026

### Completed checks

- Inspected the quiz state model and language-switch handlers in all ten core chapter scripts: Botany, Zoology, Cell Biology, Anatomy and Physiology, Genetics, Microbiology, Ecology, Evolution, Biochemistry and Systematics.
- Confirmed a repeatable state-transition defect: changing RU/EN after answering a question re-rendered the quiz and cleared `quizAnswered` while retaining the current question index and score. A learner could therefore answer the same question again and potentially score twice before advancing.
- Corrected all ten chapter scripts. The answered state now persists through a language switch; it is cleared when the learner explicitly advances to the next question. The Next control remains available when the current question has already been answered.
- Added a regression assertion to `checks.mjs` for all ten core chapters, checking both preservation across re-render and reset on advancement.
- Read-back of the ten chapter changes and regression assertion is recorded as the source-level verification for this milestone.

### Scientific and model review observations

- The sampled DNA transcription model preserves template direction (3′→5′) and complementary RNA output (5′→3′); the example `TAC` → `AUG` is consistent.
- The ecology food-chain builder enforces sequential trophic choices and allows correction by returning to an earlier choice. The explanatory text correctly cautions that real food webs are more complex than the five-step teaching example.
- The microbiology growth-phase model labels the phases as a simplified closed-system pattern and describes the stationary phase as approximate balance between new-cell formation and cell death.
- The evolution selection visual uses illustrative percentage values (50/50 and 78/22); these are model settings, not measured field data. The text frames the result conditionally and notes drift, mutation and gene flow as additional processes.
- These are source-level plausibility checks, not independent scientific sign-off. Targeted claim-to-source sampling in the regional flora/fauna chapters remains in progress.

### Limitations

- No Node.js suite, browser automation, mobile rendering, keyboard interaction or assistive-technology test was executed in this milestone. The new regression assertion is committed but has not yet been run.
- Calculations and state transitions have been inspected in source; real browser behaviour and visual feedback still require execution.
- G4 independent scientific review and G5 independent bilingual/editorial review remain open. All 52 illustration markers remain unchanged and Deferred.

### Change log

- 1 November 2026: advanced the repeat audit to 15%; corrected the shared quiz answer-state defect in ten core chapters and added a regression assertion. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.

## 20% milestone — regional flora/fauna source-traceability pass — 1 November 2026

### Completed source checks

- Rechecked the high-priority national flora claims against the primary publications: Sennikov et al. (2025), *Nordic Journal of Botany*, DOI 10.1002/njb.04731, supports the dated total of 4,043 vascular-plant species, ten new country records, one confirmed record and two exclusions. The chapter correctly presents this as a 2025 published count rather than an immutable total.
- Rechecked the north-eastern aquatic-plant study (2024), DOI 10.1016/j.japb.2023.09.002. The paper supports seven species newly recorded for Kyrgyzstan, a newly detected hybrid, and the treatment of *Stuckenia amblyphylla* as not a separate species. The chapter correctly limits the study to sampled waterbodies in north-eastern Kyrgyzstan rather than claiming a national wetland inventory.
- Rechecked the Ministry / National Academy announcement of 9 June 2026. The 24-month Red Data Book update is ongoing; the cited 89 higher-plant and fungi figure is a number in the announcement/list being prepared, not a completed new Red Data Book edition. The chapter's caveat is appropriate.
- Rechecked the argali genomic paper (Thomson, Davletbakov & Frisina, 2026; *Diversity* 18(3):194; DOI 10.3390/d18030194) against its linked Dryad dataset (DOI 10.5061/dryad.76hdr7t7t). The paper's Methods section says 88 samples were collected in Kyrgyzstan and 72 retained; the dataset abstract describes the 72 retained samples as collected across Kyrgyzstan and Tajikistan. This is a genuine article–dataset geographic metadata discrepancy and must remain unresolved until the sample-provenance table or authors clarify it.

### Confirmed correction saved

- Updated chapters/fauna-kyrgyzstan.html in Russian and English to describe the argali article–dataset discrepancy explicitly, avoid assigning all 72 retained samples to Kyrgyzstan without provenance reconciliation, and cite the correct article and dataset DOIs. The previous DOI placeholder was replaced with the verified DOI 10.3390/d18030194.
- Added a regression assertion in checks.mjs requiring the correct article DOI, dataset DOI and unresolved-provenance caveat to remain in the fauna chapter.
- Updated KYRGYZSTAN_SPECIES_AUDIT.md with the verified bibliographic identifiers and the chapter correction.
- Read-back verification is still required after the final documentation update; no Node.js or browser test execution is claimed.

### Scope and limitations

- This pass verifies selected high-priority claims, not every species account, oblast record, map point or bibliography entry.
- The source-traceability gap remains for many individual species claims where a chapter-wide bibliography is not a direct claim-level citation.
- The seven-oblast framework remains an editorial structure, not seven complete verified species checklists.
- G4 independent scientific review and G5 independent editorial/language review remain open. All illustration markers are preserved; no image production or publication approval is claimed.
- Fresh execution of checks.mjs, browser/mobile rendering, keyboard-only operation, contrast measurement and assistive-technology review remain pending.

### Change log

- 1 November 2026: advanced the repeat audit to 20%; verified selected national flora and regional biodiversity claims against primary sources; corrected the argali genomic sample-provenance caveat and added a regression guard. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.

## 30% repeat-audit milestone — 1 November 2026

- Primary source reviewed: Seregin, Lyskov & German (2025), *Acta Biologica Sibirica* 11:551–579, DOI 10.5281/zenodo.15253859. Its 2016 expedition covered 90 sites / 28 days; the paper reports 945 numbered gatherings / 963 physical specimens, 31 new records across seven floristic provinces, three new country records and 12 supplementary records. It also states that 397 specimens (37%) remained unidentified to species level at the stated processing date.
- Clarified in the flora chapter and audit that the paper's seven floristic provinces are not the atlas's seven administrative oblasts.
- Added the Besh-Tash *Allium filifolium* herbarium record (23 July 2016, 2,170 m, MW0896287) to the Talas regional dossier, retaining the source's taxonomic caveat concerning the *A. kokanicum* complex.
- Added regression assertions for the source DOI, geographic-framework distinction, unresolved identifications and voucher record. GitHub read-back confirmed the chapter, audit and script updates.
- The image insertion map and disposition register still contain 52 unique anchors each; all remain Deferred. No illustration asset was added.
- `checks.mjs`, browser tests and CI were not run during this pass; no test success is claimed.
- Repeat-audit coverage: **30%**. Controlled editorial readiness: **95/100**. G4 scientific sign-off and G5 editorial/language sign-off remain open.

## 40% repeat-audit milestone — 1 November 2026

- Snow leopard: recorded the difference between PASK's modelled estimate of about 300 adults (95% CI 246–366) and the Ministry's 29 October 2026 indicative range of 450–550 animals. The chapter attributes and dates both and marks the difference unresolved.
- Terskey Ala-Too: added the July–August 2025 Burkhan / Archaly expedition report, preserving the 98-cell survey design, limited sampling effort, DNA versus camera-trap evidence, local argali scope and corrected Otocolobus manul spelling.
- Menzbier's marmot: added FFI/CEPF's 2021–2022 project estimate of about 16,145 animals, with the warning that the 2002 comparison is not fully comparable. Distinguished IUCN Red List Vulnerable (VU) from IUCN Green Status Critically Depleted / 13% recovery score.
- Updated the regional species audit and added regression guards. GitHub read-back verified the edited chapter, audit and checks file.
- The image insertion map and disposition register each retain 52 unique anchors; all remain Deferred. No illustration asset was added.
- checks.mjs, browser tests, mobile checks and CI were not run; no test success is claimed.
- Repeat-audit coverage: 40%. Controlled editorial readiness: 95/100. G4 scientific sign-off and G5 editorial/language sign-off remain open.



## Repeat-audit milestone — 50% — 1 November 2026

- Corrected the Kyrgyzstan amphibian checklist page date to its displayed 12 October 2026 generation date; the current regional GBIF checklist is version 1.18, published 26 October 2026, and covers five Central Asian countries.
- Preserved the Kyrgyzstan page's 7-species / 2-subspecies listing and its 4 resident / 3 unconfirmed species split without conflating country-level presence, taxonomy or conservation status.
- Audited the full 2021 green-toad paper: 209 adult males / 14 localities are shared across Kazakhstan and Kyrgyzstan; six localities and 117 specimens are in Kyrgyzstan. Corrected the scope wording and added regression guards.
- Read-back verified the updated species audit and checks source. `checks.mjs` itself was not run; no test success is claimed.
- The 52 image insertion anchors and 52 Deferred disposition entries remain intact; no visual asset was added.
- Repeat-audit coverage: 50%. Controlled editorial readiness: 95/100. G4 scientific review and G5 editorial/language review remain open.


## Repeat-audit milestone — 60% — 1 November 2026

- Reconciled the reptile country page's 44 country-selector count with its 43 numbered species / summary count; retained the unresolved discrepancy and the separate 19-subspecies count (12 unconfirmed).
- Clarified that the compiler's eight Red Data Book entries (six species, two subspecies) are a secondary mapping to the cited 2006 edition, not an independent legal review.
- Updated the GBIF Central Asian reptile checklist description: version 1.15, five-country scope, literature-review hierarchy and explicit non-field-sampling method.
- Rechecked the 2015 Black Stork breeding account and generalized the nest location in the chapter to avoid exposing a sensitive nest site; preserved the dated chick chronology.
- Updated the regional audit and regression guards. GitHub changes are to be read back; `checks.mjs` was not run and no test success is claimed.
- The 52 image anchors and 52 Deferred disposition entries remain intact; no visual asset was added.
- Repeat-audit coverage: 60%. Controlled editorial readiness: 95/100. G4 and G5 remain open.
