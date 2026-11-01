# Full repeat audit — Atlas of Biology

**Audit start:** 1 November 2026  
**Canonical branch:** `workspace/biology`  
**Scope:** all Biology HTML pages, scientific/editorial content, interactive tools, technical checks, vector and raster visuals, image placeholders, bilingual parity, links and release controls.  
**Audit completion:** **70%** — species-checklist currency and bird-list scope audit completed.  
**Controlled editorial readiness:** **95/100** (separate metric; unchanged).

## Audit method and boundaries

The audit is conducted in the Biology working area only. It does not modify other Atlas disciplines, the portal, publication settings or historical branches. Confirmed defects may be corrected in place after the current blob SHA is fetched; every saved change must be read back and verified. Ambiguous scientific claims are recorded for qualified review rather than silently rewritten.

The audit separates:
1. Editorial quality and bilingual equivalence.
2. Scientific accuracy, source traceability, taxonomy and evidence scope.
3. Technical structure, local links, scripts, controls and regression checks.
4. Visual quality, SVG accessibility, image briefs, raster provenance and insertion-marker integrity.
5. Cross-page navigation, responsive behaviour and release readiness.

## 5% milestone — repository inventory

### Pages inventoried

- Landing page: `index.html`.
- Ten core chapters: Botany, Zoology, Cell Biology, Anatomy and Physiology, Genetics, Microbiology, Ecology, Evolutionary Biology, Biochemistry, Systematics.
- Two regional chapters: Flora of Kyrgyzstan and Fauna of Kyrgyzstan.
- Total: **13 HTML pages**.

### Baseline source scan

A source-level scan of all 13 pages found:
- Russian and English content markers are present in balanced counts on every page.
- No duplicate HTML `id` values were found in the scanned pages.
- Inline SVG illustrations are present across the course; the scan counted 22 SVG elements in total.
- No raster `<img>` elements are currently integrated in the 13 pages, consistent with the existing deferral decision.
- All 52 planned `image-brief-*` anchors remain represented in the production map and page content according to the existing committed regression assertions. Actual end-to-end execution of the Node/Chromium suites has not yet been performed in this audit.
- The regional chapters contain substantially larger source/reference footprints than the core teaching chapters; a bibliography entry alone is not treated as proof for every nearby species claim.

### Existing controls and gates confirmed

- The image insertion map contains 52 planned assets; the disposition register records all 52 as Deferred.
- No raster image is approved, committed or integrated under `biology/images/generated/`.
- G4 independent scientific review and G5 independent bilingual/editorial release review remain open.
- The existing 95/100 controlled editorial-readiness score is not changed by this inventory milestone.

## Initial audit observations

1. **Source traceability remains a known substantive gap.** The regional species audit explicitly notes that a chapter-wide bibliography does not prove every adjacent species statement. High-priority claims need claim-level source linkage.
2. **Independent review is still required.** The existing external-review packet is prepared but has no completed sign-off.
3. **Visual publication is deliberately incomplete.** SVG learning diagrams exist, but all 52 planned raster assets remain deferred. This is a recorded release choice, not a hidden completed state.
4. **Automated checks are extensive but not yet freshly executed against the current branch head.** The committed `checks.mjs` covers document metadata, duplicate IDs, bilingual marker and numeric parity, scientific-name parity, local paths/fragments, inline JavaScript syntax, SVG naming, button types, reference sections and specialised regional evidence assertions. Actual runtime/browser behaviour still needs a fresh run.
5. **A source-level pass cannot certify visual appearance or keyboard/mobile behaviour.** These require browser rendering and manual interaction checks in addition to static assertions, consistent with WCAG 2.2's testable accessibility requirements.

## Next audit block

Proceed to the technical baseline: inspect the complete regression script and workflow configuration, run the available checks against this exact branch head, classify failures, then correct confirmed issues and record the results. In parallel, begin claim-to-source sampling in the two regional chapters.

## Change log

- 1 November 2026: audit initiated; 13-page inventory and source-level baseline completed. No chapter content, tool logic, visual asset or image marker modified in this milestone.


## 10% milestone — technical and accessibility source review

### Completed checks

A second source-level pass was completed across all 13 HTML pages. It sampled heading hierarchy, interactive controls, SVG naming, input labels, external new-tab links and the structure of the committed regression suite.

- All 13 pages have one `h1`; each page has a populated `h2` structure.
- The sampled pages contain no `input` elements requiring an associated label.
- All 22 inline SVGs exposed an accessible name through `aria-label` / `aria-labelledby` or the required SVG image role; no SVG in the sampled source lacked a title/name.
- No external link using `target="_blank"` was found without `rel="noopener"`.
- Interactive pages use native `button` elements with explicit `type="button"`; the language-switch button's visible text (EN/RU) supplies its name. A first-pass regex flagged this control as potentially unnamed, but manual inspection confirmed it is visibly named; this was classified as a false positive, not a defect.
- The existing regression script includes checks for duplicate IDs, RU/EN block counts, numeric-token parity, scientific-name parity, local paths and fragments, inline JavaScript syntax, SVG accessible names, button types and the 52 image-anchor map.
- The existing bilingual parity report records 1,147 Russian and 1,147 English blocks, with no numeric-token or scientific-name-set differences in its measured scope. This remains an author-side structural parity check, not professional translation approval.

### Accessibility standard applied

The source review uses WCAG 2.2 as a reference, particularly text alternatives for non-text content, keyboard operation, focus visibility, language identification, contrast and minimum target size. Static source inspection cannot establish contrast ratios, responsive reflow, real keyboard behaviour or assistive-technology output; those remain browser/manual test items.

### Findings / limitations

1. No confirmed source-level defect requiring a code edit was found in this technical/accessibility sample. Therefore no speculative HTML or JS change was made.
2. The 81 KB `checks.mjs` suite was inspected but not executed: the repository checkout/runtime and its installed Node/Chromium dependencies are not available through the current GitHub file-reading connection. No claim of a passing test run is made.
3. Workflow configuration and latest CI run still require direct retrieval/verification; they are not inferred from the presence of a test script.
4. Browser-based mobile/desktop rendering, keyboard-only interaction, contrast measurement, reduced-motion behaviour and screen-reader checks remain open.

### Next block

Continue technical review by examining each interactive model's state transitions, calculations, boundary cases and language-switch behaviour; then perform targeted scientific claim-to-source review in the two Kyrgyzstan regional chapters.

### Change log

- 1 November 2026: completed source-level technical/accessibility review of all 13 pages and inspected the committed regression script. No code change made because no confirmed defect was established. Audit completion advanced to 10%; controlled editorial readiness remains 95/100.


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

## 30% milestone — regional flora primary-source and voucher pass — 1 November 2026

### Completed source checks

- Reviewed Seregin, Lyskov & German (2025), *Acta Biologica Sibirica* 11:551–579, DOI 10.5281/zenodo.15253859, against the full article. The publication reports a 2016 expedition across 90 sites over 28 days; it records 945 numbered gatherings / 963 physical specimens, three taxa new to Kyrgyzstan, 31 new records for one of seven floristic provinces and 12 supplementary records. The paper notes that 397 specimens (37%) remained unidentified to species level at the stated processing date.
- Confirmed a key scale distinction: the seven floristic provinces used by the national vascular-plant checklist are not the seven administrative oblasts used in the regional atlas. The chapter bibliography and the species-evidence audit now state this explicitly; the source is not presented as a seven-oblast checklist.
- Verified the Talas/Besh-Tash record of *Allium filifolium*: Besh-Tash Gorge, 23 July 2016, 2,170 m, specimen MW0896287. The source discusses the complex taxonomic history of the *A. kokanicum* group. The chapter now reports the name as the 2025 paper's identification and retains that taxonomic caveat, rather than asserting a fully settled taxonomic treatment.

### Saved changes and regression protection

- Added the 2025 regional-record paper to `chapters/flora-kyrgyzstan.html` bibliography in Russian and English, with its expedition date, record counts and explicit floristic-region / administrative-oblast distinction.
- Added the voucher-backed Besh-Tash *Allium filifolium* record to the Talas dossier in both languages, including date, herbarium accession and taxonomic qualification.
- Expanded `KYRGYZSTAN_SPECIES_AUDIT.md` with the source's scope, identification limitations and the specific Besh-Tash voucher evidence.
- Added regression assertions in `checks.mjs` for the source DOI, regional-framework caveat, unresolved-identification caveat and Besh-Tash voucher/taxonomic qualification.
- Read-back confirmed the edited chapter, audit and regression script contain the new evidence. The image insertion map and disposition register each still contain 52 unique anchor IDs.

### Verification limits

- Source-level verification and GitHub read-back were completed. `checks.mjs`, browser tests and CI were **not** executed in this pass; the new assertions are committed but not reported as passing.
- No new image was generated or integrated. All 52 illustration anchors and Deferred dispositions remain unchanged.
- This remains a bounded claim-to-source pass, not a complete verification of all species accounts or locality records.
- G4 independent scientific review and G5 independent bilingual/editorial review remain open. Controlled editorial readiness remains **95/100**; no publication approval is implied.

### Change log

- 1 November 2026: advanced repeat-audit coverage to 30%; added and checked a primary regional-flora source and a voucher-backed Besh-Tash record, with bilingual caveats and regression guards. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.

## 40% milestone — fauna abundance, field-record and conservation-status audit — 1 November 2026

### Completed source checks and corrections

- Compared the 2026 Snow Leopard Reports synthesis of the 2020–2024 PASK assessment with the Ministry's 29 October 2026 estimate. PASK reports approximately 300 adult snow leopards (95% CI 246–366), based on spatial capture–recapture modelling; the Ministry notice gives 450–550 animals but does not state its method, confidence interval or age structure. The chapter now keeps both figures separate, dates and attributes them, and explicitly records the discrepancy as unresolved rather than averaging or conflating them.
- Added the 2025 Terskey Ala-Too expedition report (Burkhan and Archaly valleys; published on Zenodo in June 2026) to the Issyk-Kul dossier. The bilingual account preserves survey effort (98 cells, 40 days, 93% visited once), separates DNA scat results from camera-trap identifications, limits argali observations to the sampled site, and corrects the report's misspelling Otolobus manul to the current genus spelling Otocolobus manul while retaining the source typo as a note.
- Expanded the Besh-Aral Menzbier's marmot account using the 2023 FFI/CEPF final report: surveys in June 2021 and June 2022, project estimate of about 16,145 animals (reported by the project as the Kyrgyzstan total), and the warning that the earlier 2002 estimate of about 12,000 is not fully comparable. Added the 2023 IUCN Red List category Vulnerable (VU) and distinguished it from the separate IUCN Green Status result, Critically Depleted / 13% recovery score.
- Updated KYRGYZSTAN_SPECIES_AUDIT.md with the source scope, methodological limits and status-framework distinctions.
- Added regression assertions in checks.mjs for the separate snow-leopard estimates, Terskey sampling and method-specific evidence, the Pallas's cat spelling caveat, and the Menzbier abundance / Red List / Green Status distinctions.

### Saved-state and verification limits

- Read-back verified the fauna chapter, species audit and regression script after updates. The audit-script checks were inspected for source strings and initialization order; the Node.js script itself was not executed.
- No browser, mobile, accessibility or CI tests were run in this pass. No automated test success is claimed.
- The image insertion map and disposition register still each contain 52 unique illustration anchors. All remain Deferred; no image asset was generated or integrated.
- This is a bounded primary-source claim audit, not a complete verification of every species, locality or conservation category. G4 independent scientific review and G5 independent bilingual/editorial review remain open. Controlled editorial readiness remains 95/100; no publication approval is implied.

### Change log

- 1 November 2026: advanced repeat-audit coverage to 40%; documented the snow-leopard estimate discrepancy, added scoped Terskey Ala-Too field evidence, and updated Menzbier's marmot population and conservation-status evidence. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.



## 50% milestone — amphibian checklist and locality-evidence audit — 1 November 2026

### Completed source checks and corrections

- Rechecked the Central Asian amphibian checklist at GBIF IPT version 1.18 (published 26 October 2026). It is a five-country literature compilation, not a Kyrgyzstan field survey; its 33 core taxon records cover the region and must not be mistaken for a Kyrgyzstan-only species total.
- Corrected the Kyrgyzstan amphibian country-page snapshot date: the page itself states that its displayed export was generated on 12 October 2026, not 30 September. It lists 7 species (4 resident, 3 unconfirmed) and 2 subspecies (1 unconfirmed). The resident / unconfirmed categories remain distinct from taxonomy and conservation status.
- Re-examined Litvinchuk, Svinin & Dujsebayeva (2021), DOI 10.20363/BZB-2021.70.2.361, against the full paper and Table 1. The reported 209 adult males from 14 localities are a combined Kazakhstan–Kyrgyzstan sample collected during 1994–2001. The table contains six Kyrgyzstan localities and 117 specimens; the 14 localities are not all Kyrgyzstan. The audit now states this explicitly and prohibits interpreting the sample as a current population estimate.
- Updated `KYRGYZSTAN_SPECIES_AUDIT.md` and strengthened `checks.mjs` assertions for the corrected page date, five-country dataset scope, two-country Bufotes sample provenance and Kyrgyzstan subset.
- Static GitHub read-back verified the updated audit and regression-script text, including assertion placement after `regionalSpeciesAudit` initialization.

### Saved-state and verification limits

- The image insertion map and disposition register still contain 52 unique anchors each; all 52 remain Deferred. No image asset was generated or integrated.
- `checks.mjs` was not executed. No test pass is claimed; browser, mobile, accessibility and CI checks remain pending.
- This remains a bounded evidence audit, not a complete verification of every amphibian, reptile, fish or locality record. G4 independent scientific review and G5 independent bilingual/editorial review remain open.
- Repeat-audit coverage: **50%**. Controlled editorial readiness remains **95/100**; this is not publication approval.

### Change log

- 1 November 2026: advanced repeat-audit coverage to 50%; corrected the amphibian snapshot date, clarified the scope of the five-country checklist, and quantified the Kyrgyzstan subset of the 2021 green-toad sample. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.


## 60% milestone — reptile checklist and sensitive breeding-locality audit — 1 November 2026

### Completed source checks and corrections

- Rechecked the Kyrgyzstan reptile country list against its visible page table. The country selector displays 44, while the numbered species table and summary both report 43 species; the summary separately lists 19 subspecies, including 12 unconfirmed. The discrepancy remains explicit and unresolved. The page separately identifies four unconfirmed species, the introduced/resident status of `Tenuidactylus fedtschenkoi`, and `Varanus griseus` as absent. The compiler's eight Red Data Book entries (six species and two subspecies) are recorded as its mapping to the cited 2006 edition, not as an independent legal verification.
- Rechecked the GBIF Central Asian reptile checklist, version 1.15 (published 26 October 2026; accessed 29 October). Its metadata confirms a five-country scope and a systematic literature-review method, with official national Red Data Book editions prioritized before monographs, specialist taxonomic papers and institutional checklists. It explicitly states that the checklist is not based on field sampling; GBIF, IUCN and Catalogue of Life are cross-checks.
- Rechecked Romanovskaya (2015) on Black Stork breeding in Boom Gorge. The primary paper documents one pair and a 2015 nest chronology: four downy chicks on 24 May, three live chicks plus one dead chick on 17 June, and three older chicks on 27 June. The chapter retains this as dated local breeding evidence, not a current population estimate.
- Generalized the Black Stork nest description in the bilingual chapter to the Boom Gorge / Kok-Moynok area. The paper's road-kilometre marker and precise nest position are deliberately not reproduced, given the species' sensitivity and disturbance documented by the author.
- Updated `KYRGYZSTAN_SPECIES_AUDIT.md` and strengthened `checks.mjs` guards for reptile count / legal-status limitations, the latest checklist's non-field methodology, the Black Stork chronology and sensitive locality handling.

### Saved-state and verification limits

- GitHub read-back is required for all changed files before this checkpoint is treated as saved.
- The image insertion map and disposition register remain at 52 unique anchors each; all remain Deferred. No visual asset was generated or integrated.
- `checks.mjs` was not executed. No test pass is claimed; browser, mobile, accessibility and CI checks remain pending.
- G4 independent scientific review and G5 independent bilingual/editorial review remain open.
- Repeat-audit coverage: **60%**. Controlled editorial readiness remains **95/100**; this is not publication approval.

### Change log

- 1 November 2026: advanced repeat-audit coverage to 60%; expanded the reptile checklist's method and count caveats, verified the 2015 Black Stork breeding record, and generalized the sensitive nest locality. No test pass or publication approval is claimed.


## 70% milestone — mammal checklist currency and bird-list comparability — 1 November 2026

### Completed source checks and corrections

- Reopened the GBIF record for the Central Asian mammal checklist. Its current published release is version 1.12 (26 October 2026; DOI 10.15468/hmrvjn), not the previously cited version 1.11. Updated the fauna chapter's bilingual bibliography link and description.
- Verified the dataset's five-country scope, country-specific presence categories, species/subspecies coverage and explicit separation of global IUCN status from national Red Data Book entries.
- Verified the checklist's method: systematic review of published literature, prioritising national Red Data Book editions, systematic monographs, specialist taxonomic papers and institutional checklists. The dataset explicitly says it is not based on field sampling; it is not new local survey evidence.
- Compared four public bird-list sources: Birds of Kyrgyzstan (407), OSME (327), The Ornithology (380), and Limosa (133 regular open-data species; explicitly incomplete). These are different reference products with different scope and inclusion criteria, not evidence of a biological change in national richness.
- Added a bilingual chapter note explaining why the bird totals must not be merged or represented as one definitive total. Locality claims remain dependent on dated site-level evidence.
- Expanded `KYRGYZSTAN_SPECIES_AUDIT.md` with the version 1.12 source/method record and the bird-list scope comparison. Added regression guards for the updated version, publication date, non-field method and bird-list caveats.

### Saved-state and verification limits

- GitHub read-back verified the changed fauna chapter, species audit and `checks.mjs`; milestone documents are being synchronized and read back in this save cycle.
- The 52 image insertion anchors and 52 Deferred disposition entries remain unchanged; no new image is claimed as generated or integrated.
- `checks.mjs` was not executed. No test pass is claimed; browser, mobile, accessibility and CI checks remain pending.
- G4 independent scientific review and G5 independent bilingual/editorial review remain open.
- Repeat-audit coverage: **70%**. Controlled editorial readiness remains **95/100**; this is not publication approval.

### Change log

- 1 November 2026: advanced repeat-audit coverage to 70%; updated the mammal checklist from GBIF v1.11 to v1.12 and documented why public Kyrgyzstan bird-list totals are not directly comparable. No test pass or publication approval is claimed.
