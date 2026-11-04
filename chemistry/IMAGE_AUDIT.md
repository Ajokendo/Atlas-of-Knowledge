# Chemistry Atlas — Image and visual audit

**Canonical standard:** [IMAGE-FIRST POLICY v1.1](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/atlas-of-knowledge-integration/IMAGE_FIRST_POLICY.md)  
**Branch:** `workspace/chemistry`  
**Audit date:** 2026-11-05  
**Policy version:** IMAGE-FIRST POLICY v1.1  
**Scope of this checkpoint:** all 22 static SVG files (11 RU/EN pairs), seven interactive visual systems across chapter pages and standalone tools, their learner-facing language/accessibility metadata, and the unintegrated Chapter 03 candidate. This is an inventory and first-pass source-code review, not a complete independent scientific or legal certification. The repository does not contain a historical search log proving that ready-made licensed sources were considered before these project SVGs were created; compliance with the search-first sequence for past assets remains PENDING.

## Audit method

Use the canonical policy for status definitions, audit result values, evidence requirements, and verification rules. This file contains only Chemistry-specific findings and metrics; it does not redefine the universal standard.

## Summary metrics — historical checkpoint (superseded by the 2026-11-05 policy re-audit below)

| Metric | Current result | Interpretation |
|---|---:|---|
| Static visual topics inventoried | 11 | Each topic has RU and EN SVG variants |
| Static SVG files inventoried | 22 | 11 English + 11 Russian |
| Interactive visual systems inventoried | 4 | Atomic model, subatomic-particle comparison, bonding models, periodic table |
| Static visuals integrated | 11 / 11 | All inventoried static visual pairs are used on the landing page or in a chapter |
| Provisional static Image Coverage | 11 / 11 = 100% | **Only for the 11 currently inventoried static visual topics; not a claim that every chapter has all required visuals** |
| Static Image Verification | 0 / 11 = 0% VERIFIED | All 11 pairs still lack file-specific creator/rightsholder and licence confirmation |
| Static Image Gaps | Not yet fully determined | Chapter 01 now includes the electron-cloud figure alongside the interactive shell model; chapter 03 still needs a documented decision on whether a static periodic-trends visual adds learning value. The complete visual-need matrix is still pending |
| Category A — external original reuse | 0 | No external image-source records established |
| Category B — adapted external reuse | 0 | No external adapted image-source records established |
| Unclassified local SVG pairs | 11 | Project-local files exist, but creation method, creator/rightsholder and rights basis are not established; do not classify as C until evidenced |
| Search-first evidence | 15 / 15 records searched | No contemporaneous historical log exists. Retrospective searches cover all 15 records. These searches do not prove the original creation process followed image-first |
| Search candidates | 3 FOUND / 15 searched | OpenStax titration curve, OpenStax Daniell-cell figure, and PubChem interactive periodic table identified as candidates; none adopted pending suitability and item-level rights review |
| Rights / licence checks | 0 PASS / 15 PENDING | File-specific creator/rightsholder and licence evidence is not recorded for the 11 SVG pairs or four interactive systems |
| Scientific first-pass checks | 10 PASS / 1 PENDING | See detailed table; first-pass source-code review only |
| RU/EN metadata presence | 11 PASS / 0 FAIL | Paired SVG files and localized title/description elements exist; this is not a complete translation-quality or manual accessibility review |
| Technical source checks | 22 PASS for basic SVG metadata | CI checks viewBox, role, title, description and local asset paths; responsive/device review remains pending. Four interactive systems still need manual keyboard, zoom and screen-reader checks |

**Important:** the 11/11 ratio measures only whether the currently inventoried static topics exist and are integrated. It is not a measure of curriculum visual coverage or readiness. A learning-purpose and visual-need decision is still required for every chapter. Retrospective searches cover 15/15 records; the original search-first sequence cannot be proven retrospectively. Rights verification is 0/15; none of the visual records may be described as VERIFIED or publication-ready.

## Latest policy-readiness checkpoint — 2026-11-05

This checkpoint supersedes the earlier provisional 11/11 static-only coverage figure. It uses the chapter-level visual plan, counts the unintegrated Chapter 03 trend diagram as a required gap, and keeps image readiness separate from editorial and general website readiness.

| Metric | Current result | Scope / interpretation |
|---|---:|---|
| Required static visual units / SVG pairs | 12 | 11 integrated bilingual SVG pairs plus the missing Chapter 03 periodic-trends pair. Chapter 12 has two static figures; Chapter 04 is covered by an interactive model rather than a static pair. |
| Static Image Coverage | 11 / 12 = 91.7% | 11 static bilingual pairs are integrated; the Chapter 03 periodic-trends visual is found as a candidate but not integrated. Provisional chapter-plan coverage. |
| Interactive visual systems | 7 / 7 integrated | Four chapter-level systems plus molecular geometry, gas-particle count and the acid–base virtual beaker. Presence does not imply verification. |
| Chapter-level visual plan | 15 / 16 = 93.75% integrated | 12 static topics + 4 chapter-level interactive systems; 15 are present and one required static topic remains missing. Provisional. |
| Supplemental interactive tools | 3 / 3 integrated | Molecular laboratory, gas-laws particle-count visual and acid–base virtual beaker; all remain unverified. |
| Atlas-wide visual plan | 18 / 19 = 94.74% integrated | 12 static topics + 7 interactive systems; 18 are present and the Chapter 03 static trend visual remains the only identified gap. Provisional. |
| Image Verification | 0 / 18 = 0% VERIFIED | None of the 18 integrated visual records meets every applicable science, rights, language, accessibility and technical criterion. |
| Image Gaps | 1 required visual | Chapter 03 periodic trends: candidate found; local integration and review pending. No other missing chapter-level visual identified in the current 12-chapter plan. |
| Category A — external original reuse | 0 assigned | Existing local assets have not been proven to be unmodified external reuse. |
| Category B — adapted external reuse | 0 assigned | No existing local asset has a verified external source/adaptation trail. |
| Category C — created | 0 assigned | Local presence alone does not prove project authorship or method. |
| Category / method pending | 18 / 18 integrated records | 11 static pairs + 7 interactive visual systems; provenance and creator/rightsholder evidence still needed. |
| Rights on integrated records | 0 PASS / 18 PENDING / 0 FAIL | All 18 integrated records remain unverified. Candidate source rights are tracked separately and do not count as integrated assets. |
| AI-assisted first-pass scientific review | 13 PASS / 5 PENDING / 0 FAIL | Source-level first pass: 10 static visuals and three supplemental interactive systems reviewed PASS; CH-V01 and four earlier interactive systems remain PENDING. This is not independent expert sign-off. |
| Independent scientific/factual review | 0 PASS / 18 PENDING / 0 FAIL | A competent independent subject-matter reviewer has not signed off any integrated visual; all 18 remain PENDING for this formal policy dimension. |
| Language and accessibility status | 0 PASS / 18 PENDING / 0 FAIL | Automated bilingual metadata, 42 axe scans and language toggles pass; full translation-quality, keyboard, screen-reader and device review remains PENDING for every integrated visual. |
| Technical status | 0 full PASS / 18 PENDING / 0 FAIL | Automated CI passed on commit 7a4d60c: 22 HTML pages, 90 local links/assets, 21 inline scripts, 21 Chromium pages, 42 RU/EN axe scans, 21 language toggles and overflow checks at 390/768/1280 px. Full per-visual technical sign-off still awaits manual zoom/reflow, device and assistive-technology review. |
| Retrospective search evidence | 19 / 19 records have dated search notes | The 18 integrated records plus the Chapter 03 candidate. This does not prove the original pre-creation search-first sequence. |
| Search candidates | 10 FOUND / 19 searched | Earlier candidates plus PhET Molecule Shapes, Gas Properties and Acid-Base Solutions/pH Scale resources. None has been adopted; exact reuse terms and pedagogical fit are recorded in IMAGE_SOURCES.md. |

### Chapter-level visual metrics

| Chapter | Required visuals | Integrated | Image Coverage | Image Verification | Image Gaps |
|---|---:|---:|---:|---:|---|
| 01 Atomic structure | 3 | 3 | 100% | 0 / 3 VERIFIED | None identified; rights and manual checks remain open |
| 02 Chemical elements and isotopes | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 03 Periodic system | 2 | 1 | 50% | 0 / 1 VERIFIED | Periodic-trends diagram: candidate FOUND, not integrated |
| 04 Chemical bonding | 1 system (3 models) | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 05 Amount of substance | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 06 Chemical formulae | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 07 Solutions | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 08 Acids and bases | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 09 Chemical reactions | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 10 Redox | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 11 Organic chemistry | 1 | 1 | 100% | 0 / 1 VERIFIED | None identified; rights and manual checks remain open |
| 12 Chemistry of life and environment | 2 | 2 | 100% | 0 / 2 VERIFIED | None identified; rights and manual checks remain open |

**Totals:** 16 required visual units, 15 integrated, 93.75% provisional Image Coverage; 0/15 integrated visuals VERIFIED; one known gap in Chapter 03. A chapter showing 100% coverage is not thereby verified: the rights, provenance, scientific, language, accessibility and technical checks may still be pending.

### Chapter-level policy-dimension status

Counts below are for integrated visual units only; each cell uses PASS / PENDING / FAIL. A missing visual is reported separately in Image Gaps. No integrated visual is yet VERIFIED because rights and independent/manual checks remain open.

| Chapter | Integrated units | Rights P/P/F | Independent science P/P/F | Language/accessibility P/P/F | Technical P/P/F | Category A/B/C/PENDING |
|---|---:|---:|---:|---:|---:|---:|
| 01 Atomic structure | 3 | 0/3/0 | 0/3/0 | 0/3/0 | 0/3/0 | 0/0/0/3 |
| 02 Chemical elements and isotopes | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 03 Periodic system | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 04 Chemical bonding | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 05 Amount of substance | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 06 Chemical formulae | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 07 Solutions | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 08 Acids and bases | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 09 Chemical reactions | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 10 Redox | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 11 Organic chemistry | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| 12 Chemistry of life and environment | 2 | 0/2/0 | 0/2/0 | 0/2/0 | 0/2/0 | 0/0/0/2 |

**Chapter-level totals:** 15 integrated visual units; for each formal policy dimension, 0 PASS / 15 PENDING / 0 FAIL. The only missing chapter visual is the Chapter 03 periodic-trends pair.

### Supplemental interactive-tool visual metrics

| Tool / visual | Required | Integrated | Image Coverage | Image Verification | Image Gaps |
|---|---:|---:|---:|---:|---|
| Molecular laboratory — four 3D molecule models | 1 system | 1 | 100% | 0 / 1 VERIFIED | None identified; creator/code rights and manual checks pending |
| Gas laws — schematic particle-count visual | 1 system | 1 | 100% | 0 / 1 VERIFIED | None identified; creator/code rights and manual checks pending |
| Acid–base virtual laboratory — beaker and pH indicator | 1 system | 1 | 100% | 0 / 1 VERIFIED | None identified; creator/code rights and manual checks pending |

**Supplemental tools total:** 3 / 3 integrated (100% provisional coverage), 0 / 3 VERIFIED. Combined with the chapter-level plan, the whole atlas has 18 / 19 integrated visual units (94.74% provisional coverage) and 0 / 18 VERIFIED.


### Supplemental-tool policy-dimension status

| Tool | Integrated | Rights P/P/F | Independent science P/P/F | Language/accessibility P/P/F | Technical P/P/F | Category A/B/C/PENDING |
|---|---:|---:|---:|---:|---:|---:|
| Molecular laboratory | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| Gas-laws particle visual | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |
| Acid–base virtual beaker | 1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1/0 | 0/0/0/1 |

**Whole-atlas policy-dimension totals:** 0 PASS / 18 PENDING / 0 FAIL for rights, independent scientific review, full language/accessibility review and full technical sign-off. Category counts: A = 0, B = 0, C = 0, category/method PENDING = 18. Automated CI PASS is reported separately and does not change these full-review counts.

### Chapter 03 candidate rights finding

A suitable bilingual candidate was located on Wikimedia Commons on 2026-11-05. The English original by Mirek2 is dedicated under CC0 1.0. The Russian derivative by Донор is licensed CC BY-SA 4.0 and identifies the English source; its file history records a later edit by Землеройкин. The exact source pages and licence deeds are recorded in IMAGE_SOURCES.md. These item-level source/licence checks are complete for the candidate files, but the candidate is not integrated and does not increase Image Coverage or Image Verification. Scientific, language, accessibility and local-file integration checks remain PENDING.

### Interactive visual audit by ID

| ID | Visual | Scientific / factual | Rights / provenance | Language / accessibility | Technical / integration | Overall |
|---|---|---|---|---|---|---|
| CH-IV01 | Interactive atom and electron-shell model | PENDING — teaching-model simplifications need final manual sign-off | PENDING — source-code creator, authoring method and code rights Unknown | PENDING — localized accessible name exists; manual screen-reader check outstanding | Source present; manual keyboard, zoom and device review pending | INTEGRATED, not VERIFIED |
| CH-IV02 | Inline proton, neutron and electron comparison | PENDING — visual proportions/model limits need final manual sign-off | PENDING — source-code creator, authoring method and code rights Unknown | PENDING — accessible label exists; manual RU/EN and screen-reader review outstanding | Source present; manual display and keyboard review pending | INTEGRATED, not VERIFIED |
| CH-IV03 | Ionic, covalent and metallic bonding models | PENDING — conceptual-model limitations need final manual sign-off | PENDING — source-code creator, authoring method and code rights Unknown | PENDING — localized names/live-region description exist; manual assistive-technology review outstanding | Three inline SVG models present; manual responsive/keyboard review pending | INTEGRATED, not VERIFIED |
| CH-IV04 | Interactive periodic table | PENDING — element data provenance and property conventions need final expert review | PENDING — source-code/data creator, provenance and reuse rights Unknown | PENDING — visible atomic number, symbol, localized element name and mass now form the button's computed accessible name; complete polite live region exists; manual AT review outstanding | Keyboard focus is preserved in place; visible-text naming is source-guarded; manual device/zoom review pending | INTEGRATED, not VERIFIED |
| CH-IV05 | Molecular laboratory — water, carbon dioxide, methane and ammonia 3D canvas models | PASS — source-level geometry check: water ≈104.6°, methane tetrahedral ≈109.5°, ammonia trigonal-pyramidal ≈107°, CO₂ linear; scale limitations are stated | PENDING — project code creator/rightsholder and code rights Unknown | PENDING — localized canvas accessible name and molecule descriptions exist; manual screen-reader review outstanding | Canvas and keyboard rotation present; responsive/device/zoom review pending | INTEGRATED, not VERIFIED |
| CH-IV06 | Gas laws — schematic particle-count visual | PASS — count changes with amount of substance only; nearby note explicitly excludes density, speed, trajectories and collisions and states pressure is calculated separately | PENDING — project code creator/rightsholder and code rights Unknown | PENDING — new localized accessible name is linked to the bilingual explanatory note; manual screen-reader review outstanding | Source-level description added; browser/device/zoom review pending | INTEGRATED, not VERIFIED |
| CH-IV07 | Acid–base virtual laboratory — beaker/liquid state and pH indicator | PASS — strong monoprotic/monobasic model, 25 °C, ideal dilute solution and additive-volume assumptions are stated; pH model includes water autoionisation approximation | PENDING — project code creator/rightsholder and code rights Unknown | PENDING — pH/status text is announced; new localized beaker name is linked to dynamic text; manual screen-reader review outstanding | Source-level accessibility improvement added; browser/device/zoom review pending | INTEGRATED, not VERIFIED |
## Static visual audit register

| ID / visual | Files | Science | Licence / provenance | RU/EN | Technical | Integration | Result / findings |
|---|---|---|---|---|---|---|---|
| CH-V01 Electron probability cloud | `electron-cloud.svg` + `electron-cloud-ru.svg` | PENDING | PENDING | PASS — paired title/description | PASS — viewBox, role, title, desc | PASS — landing page | PENDING. Descriptive illustration; ensure text makes clear that the cloud represents probability distribution, not a literal orbit or solid shell. Chapter 01 placement not confirmed. |
| CH-V02 Carbon isotopes | `isotope-abundance.svg` + `isotope-abundance-ru.svg` | PASS — 6 p⁺/6 n⁰ for C-12; 6 p⁺/7 n⁰ for C-13; abundance-weighted mean ≈12.011 | PENDING | PASS — paired title/description and labels | PASS — existing CI also checks nucleus counts | PASS — chapter 02 | PENDING due rights evidence. Natural abundance values are rounded approximations, as labelled. |
| CH-V03 One mole | `one-mole-scale.svg` + `one-mole-scale-ru.svg` | PASS — Avogadro constant exact; Russian label says “elementary entities”; water molar mass shown approximately | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 05 | PENDING due rights evidence. Russian wording now uses “элементарных сущностей” and the unit label “моль”. |
| CH-V04 Reading chemical formulae | `formula-reading.svg` + `formula-reading-ru.svg` | PASS — subscripts, bracket multiplier and coefficient are distinguished | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 06 | PENDING due rights evidence. |
| CH-V05 Solution saturation | `solution-saturation-particles.svg` + `solution-saturation-particles-ru.svg` | PASS — distinguishes unsaturated, saturated equilibrium and metastable supersaturated solution | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 07 | PENDING due rights evidence. Keep same-temperature condition visible. |
| CH-V06 Acid–base neutralisation | `acid-base-neutralisation.svg` + `acid-base-neutralisation-ru.svg` | PASS — net ionic reaction and qualified equivalence pH for strong acid/strong base at 25 °C | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 08 | PENDING due rights evidence. Search candidate: OpenStax Chemistry: Atoms First, Figure 14.21; image-specific credit and rights remain unchecked. |
| CH-V07 Reaction atom rearrangement | `reaction-schematic.svg` + `reaction-schematic-ru.svg` | PASS — conveys conservation of atoms and bond rearrangement | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 09 | PENDING due rights evidence. |
| CH-V08 Daniell cell | `daniell-cell.svg` + `daniell-cell-ru.svg` | PASS — Zn oxidation, Cu²⁺ reduction, electron direction and salt-bridge ion migration | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 10 | PENDING due rights evidence. Search candidate: OpenStax Chemistry 2e, Figure 17.8; composite historical and modern components require separate rights review. |
| CH-V09 Organic functional groups | `organic-functional-groups.svg` + `organic-functional-groups-ru.svg` | PASS — R–NH₂ and both language labels now identify a primary amine | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 11 | PENDING. Corrected in both SVG labels/descriptions and bilingual page alt text; keep primary-amine qualification. |
| CH-V10 Biomolecule overview | `biomolecule-overview.svg` + `biomolecule-overview-ru.svg` | PASS — explicitly avoids treating all lipids as repeating-monomer polymers | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 12 | PENDING due rights evidence. |
| CH-V11 Carbon cycle | `carbon-cycle.svg` + `carbon-cycle-ru.svg` | PASS — major reservoirs and exchanges shown; omissions explicitly acknowledged | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 12 | PENDING due rights evidence. This is a simplified conceptual diagram, not a quantitative flux diagram. |

## Interactive visual audit

| ID | Visual | Scientific review | Rights/provenance | Bilingual / accessibility | Technical | Result |
|---|---|---|---|---|---|---|
| CH-IV01 | Atomic structure interactive model | PENDING — verify shell/orbital language and model limitations against chapter text | PENDING — creator and code licence not evidenced in this register | PASS — language-dependent accessible label found in source; manual screen-reader review pending | PENDING — needs responsive and keyboard/manual review | PENDING |
| CH-IV02 | Proton, neutron and electron comparison inline SVG | PENDING — verify relative scale and explanatory labels | PENDING — creator and code licence not evidenced in this register | PASS — accessible label found in source; manual screen-reader review pending | PENDING — responsive and keyboard/manual review | PENDING |
| CH-IV03 | Ionic, covalent and metallic inline SVG models | PENDING — simplified models need contextual qualifications | PENDING — creator and code licence not evidenced in this register | PASS — generated SVG receives localized accessible name/description in source | PENDING — manual keyboard, zoom and screen-reader review | PENDING |
| CH-IV04 | Interactive periodic table | PENDING — independent element-data review remains separate | PENDING — data/code provenance to be reconciled with relevant notices | IMPROVED — each element button now has a name with atomic number, localized name, symbol and mass; selected-element details use a polite live region. Manual screen-reader review pending | PENDING — device and keyboard review | PENDING |

## Chapter-level visual gap register

| Chapter | Existing visual evidence | Current assessment | Next action |
|---|---|---|---|
| 01 Atomic structure | Interactive atom/shell model, subatomic-particle comparison, and bilingual electron-probability-cloud SVG in the chapter | INTEGRATED — three complementary representations now distinguish shell-level teaching model from probability-cloud illustration | Verify model limitations and accessible labels; manual assistive-technology review and rights evidence remain pending |
| 02 Chemical elements | Isotope abundance figure | INTEGRATED | Keep |
| 03 Periodic system | Interactive periodic table | INTEGRATED as an interactive visual, not a static figure | Editorial decision: determine whether a separate periodic-trend diagram is pedagogically required |
| 04 Chemical bonding | Three interactive inline SVG models | INTEGRATED as interactive visual | Review model limitations and add static fallback only if needed |
| 05 Amount of substance | One-mole figure | INTEGRATED | Correct Russian “particles” wording to “elementary entities” |
| 06 Chemical formulae | Formula-reading figure | INTEGRATED | Keep |
| 07 Solutions | Saturation particle models | INTEGRATED | Keep |
| 08 Acids and bases | Neutralisation / titration figure | INTEGRATED | Keep |
| 09 Chemical reactions | Atom-rearrangement figure | INTEGRATED | Keep |
| 10 Redox | Daniell cell figure | INTEGRATED | Keep |
| 11 Organic chemistry | Functional-group figure | INTEGRATED | Specify primary amine for R–NH₂ |
| 12 Chemistry of life and environment | Biomolecule overview and carbon-cycle figures | INTEGRATED | Keep |

## Chapter-level learning-need sign-off

This is a first-pass map of the currently identified visual need, not a final declaration that the chapter has every visual it requires. “Present” means a visual exists in the source; it does not mean it has passed rights, science, accessibility or manual display checks.

| Chapter | Learning need / visual role | Existing evidence | Decision / status |
|---|---|---|---|
| 01 Atomic structure | Distinguish nucleus, electron probability distribution and subatomic particles; explain model limits | Interactive atom and particle SVGs; bilingual electron-cloud SVG embedded in chapter and landing page; particle names and SVG accessible labels switch RU/EN | INTEGRATED — complementary visual roles covered; scientific wording, rights and manual screen-reader/device review remain pending |
| 02 Chemical elements | Compare isotopes and explain weighted atomic mass | Carbon isotope SVG pair | INTEGRATED — science first-pass PASS; search and rights PENDING |
| 03 Periodic system | Relate element position to groups, periods and periodic trends | Interactive periodic table displays position, group, period, symbol and mass; selected-element updates preserve keyboard focus and are announced in a complete polite live region. Wikimedia Commons bilingual trend-diagram candidate located; exact creator and licence records are documented in IMAGE_SOURCES.md | PENDING — candidate is FOUND, not integrated. English original: Mirek2, CC0 1.0; Russian derivative: Донор, CC BY-SA 4.0. Scientific, RU/EN, accessibility and local integration checks remain pending; placeholder stays until these checks pass |
| 04 Chemical bonding | Compare ionic, covalent and metallic bonding without presenting models as literal structure | Three inline SVG models; each receives a language-dependent accessible name; model explanation is announced through an atomic polite live region | INTEGRATED — model limitations are described in page text; manual keyboard/screen-reader and rights review PENDING |
| 05 Amount of substance | Connect mole, Avogadro constant and molar mass | One-mole SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 06 Chemical formulae | Read subscripts, brackets and coefficients | Formula-reading SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 07 Solutions | Compare unsaturated, saturated and metastable supersaturated states | Solution saturation SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 08 Acids and bases | Explain neutralisation and titration equivalence | Neutralisation SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 09 Chemical reactions | Show atom conservation and bond rearrangement | Reaction schematic SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 10 Redox | Trace oxidation, reduction and electron/ion movement in a galvanic cell | Daniell cell SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 11 Organic chemistry | Recognise major functional groups and avoid overgeneralising R–NH₂ | Functional-groups SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 12 Chemistry of life and environment | Compare biomolecule classes and explain major carbon reservoirs/flows | Biomolecule and carbon-cycle SVG pairs | INTEGRATED — first-pass science PASS; search and rights PENDING |

## Additional interactive-tool review

- `periodic-table.html`: a visible bilingual Chapter 03 placeholder now marks the missing periodic-trends illustration. The illustration itself is NOT integrated; image generation is deferred. The placeholder records the broad directions and explicitly qualifies them as trends with exceptions.
- `molecule-lab.html`: molecule selector option names and the workspace accessible name now switch with RU/EN. The canvas has keyboard rotation and a language-dependent accessible name; manual assistive-technology review remains pending.
- `gas-laws.html`: added a bilingual limitation note clarifying that particle dots only represent a schematic count based on amount of gas; they do not simulate density, speed, trajectories or collisions. Pressure remains calculated separately from the ideal-gas equation.

## Required follow-up before VERIFIED / publication-ready

1. Improve targeted searches for records where the first retrospective search did not surface a suitable candidate; retain the exact queries and dated outcomes already recorded. The original pre-creation search sequence remains historically unverifiable.
2. Confirm creator, authoring method, rightsholder and explicit licence or code/data rights basis for every project-created visual.
3. Complete the chapter-level learning-need sign-off. Chapter 01 electron-cloud placement is integrated but still needs manual checks. Chapter 03 has a visible bilingual placeholder in `periodic-table.html`; the actual periodic-trends illustration remains PENDING due to the image-generation limit. It must cover atomic radius, first ionisation energy and electronegativity, with explicit scope/exception notes. The static visual coverage ratio is inventory-only, not curriculum completeness.
4. Perform manual inspection at phone/tablet/desktop widths, zoom/reflow, keyboard and screen-reader checks. CI does not establish these.
5. Re-run Chemistry CI after the register and checks changes; update metrics only from actual results.

## Automation boundary

CI can validate file existence, SVG metadata, local references, bilingual pairing, non-empty alt text and registry/audit presence. CI cannot certify scientific correctness, ownership, legal rights, the quality of translation, or actual assistive-technology/device behaviour.
### Acid–base virtual laboratory — model scope clarified (2026-11-05)

The neutralisation simulator uses a 1:1 molar reaction model. Its bilingual warning now explicitly limits the model to a strong monoprotic acid and a strong monobasic base (example: NaOH) at 25 °C. It also states the dilute/ideal-solution and additive-volume assumptions, and notes that ion activities and experimental effects are not modelled. This prevents the generic phrase “strong base” from implying that dibasic or polybasic bases are covered. Automated regression checks require these qualifications in both languages. This is a source-level correction; a manual browser/device review remains outstanding.
### Reaction-balancing trainer — restart interaction corrected (2026-11-05)

A source-code review found that the completion screen assigned a second onclick handler to the Next button while the original addEventListener handler remained attached. After restarting, one click could therefore advance two tasks and skip an exercise. The restart path now lives in the single existing next() handler; the localized Next label is restored when a new task renders. A regression guard checks that the competing handler is absent. Manual browser testing of the full six-task cycle remains pending.
### Stoichiometry calculator — scale-sensitive edge cases corrected (2026-11-05)

The limiting-reactant comparison previously used an absolute tolerance with a floor of 1 mol, which could classify very small but materially different reactant amounts as stoichiometrically equal. The comparison now scales its floating-point tolerance to the actual reaction extents, and residual checks use amount-specific tolerances. Optional actual-yield input trims whitespace, and non-finite percentage results are rejected rather than displayed. Regression guards cover the scale-relative tolerance and yield-input safeguards. Manual browser tests and execution of the repository checks remain outstanding.


## 2026-11-05 follow-up: amount-of-substance terminology

A focused review of the bilingual amount-of-substance calculator found that its explanatory note correctly defined the Avogadro count as a number of specified elementary entities, but the result label and figure caption still used the less precise generic word “particles”. Updated the Russian and English calculator copy, result label, caption and image alternative text to consistently refer to specified entities / элементарные сущности. This avoids implying that every mole count necessarily refers to molecules: depending on the substance, the counted entities may be atoms, ions or formula units.

The numerical model remains (n=m/M) and (N=nN_A), with the Avogadro constant exact. Existing checks continue to assert the definition and examples of entity identity. The change is source-reviewed only; no browser or screen-reader test is claimed here.


## 2026-11-05 follow-up: virtual-lab bilingual model scope

A bilingual parity review found that the English virtual-lab warning stated the full mathematical assumptions (dilute ideal solutions, additive volumes, and omission of ion activities and experimental effects), while the Russian warning only named the strong-acid/strong-base model and temperature. Expanded the Russian warning to match the English scientific scope and explicitly identify a strong monobasic base (for example, NaOH). The existing source-level regression checks already require the key assumptions in both languages. This is a copy correction; browser interaction and assistive-technology testing remain outstanding.


## 2026-11-05: full atlas visual-marker sweep

Reviewed all 12 instructional chapter pages, the Chemistry landing page, and the standalone interactive tools on `workspace/chemistry`. This sweep checks whether intended visuals are already embedded or whether an explicit deferred-visual marker is present; it does not certify image rights or final visual quality.

| Chapter / page | Intended visual and current state | Marker action |
|---|---|---|
| 01 Atomic structure | Two inline explanatory SVG diagrams (atom and subatomic particles) plus the bilingual electron-probability-cloud SVG pair | Integrated; no missing-visual marker needed |
| 02 Chemical elements and isotopes | Bilingual isotope-abundance SVG pair | Integrated; no missing-visual marker needed |
| 03 Periodic system | Interactive periodic table plus a separate periodic-trends infographic (atomic radius, first ionisation energy, electronegativity) | **Deferred-visual marker already present** in `periodic-table.html`; bilingual copy explains placement and scientific caveats |
| 04 Chemical bonding | Three inline SVG models for ionic, covalent and metallic bonding | Integrated; no missing-visual marker needed |
| 05 Amount of substance | Bilingual one-mole scale SVG pair | Integrated; no missing-visual marker needed |
| 06 Chemical formulae | Bilingual formula-reading SVG pair | Integrated; no missing-visual marker needed |
| 07 Solutions | Bilingual saturation-state particle-model SVG pair | Integrated; no missing-visual marker needed |
| 08 Acids and bases | Bilingual neutralisation SVG pair | Integrated; no missing-visual marker needed |
| 09 Chemical reactions | Bilingual reaction-rearrangement SVG pair | Integrated; no missing-visual marker needed |
| 10 Redox | Bilingual Daniell-cell SVG pair | Integrated; no missing-visual marker needed |
| 11 Organic chemistry | Bilingual functional-groups SVG pair | Integrated; no missing-visual marker needed |
| 12 Chemistry of life and environment | Bilingual biomolecule-overview and carbon-cycle SVG pairs | Integrated; no missing-visual marker needed |

### Additional pages and interactive tools

- `index.html`: the electron-cloud SVG is used as the landing-page hero visual.
- `molecule-lab.html`: the molecular workspace is rendered interactively on a canvas; this is an interactive model, not a missing static illustration.
- `gas-laws.html`: the particle representation is intentionally schematic and is accompanied by a bilingual limitation note. No separate deferred illustration is currently declared in the page or the existing visual plan.
- `stoichiometry.html`, `chemistry-constants.html`, `virtual-lab.html`, `reaction-trainer.html`, `knowledge-check.html` and `glossary.html`: these are calculation, reference, simulation or assessment interfaces. Their inspected markup contains no unlabelled deferred-illustration slot; generic input placeholders are not visual markers.

### Sweep result

**No additional missing marker was found in the existing visual plan.** Chapter 03 remains the one explicitly deferred chapter illustration, and its marker is visible in both Russian and English. All chapter image references inspected in this sweep resolve to SVG filenames present in `chemistry/assets/`; the asset directory contains 11 bilingual SVG pairs. The interactive and inline-SVG visuals in Chapters 01 and 04 are accounted for separately.

This is a source/asset-reference audit only. It does not mean that the Chapter 03 illustration has been generated, that the SVG pairs have completed legal-rights verification, or that every visual has passed manual rendering, responsive-layout and assistive-technology review.

## 2026-11-05 follow-up: policy metrics corrected and candidate search completed

The earlier 11/11 static-only Image Coverage figure is retained above as historical evidence but is superseded for current readiness reporting. The chapter-level plan contains 12 static visual topics; 11 are integrated and Chapter 03 remains one required gap. Current provisional static coverage is therefore 11/12 (91.7%), not 100%. With four integrated interactive systems, the combined visual plan is 15/16 (93.75%). Image Verification remains 0/15 because no integrated record has passed all applicable dimensions.

A targeted image-first search located a bilingual periodic-trends candidate on Wikimedia Commons. The English file is attributed to Mirek2 and dedicated under CC0 1.0. The Russian derivative is attributed to Донор, is derived from the English work, and is licensed CC BY-SA 4.0; a later edit by Землеройкин is recorded in its file history. Exact source URLs, direct asset URLs, licence deeds, dates and conditional attribution are now recorded in IMAGE_SOURCES.md. The candidate is FOUND, not integrated. It does not close the Chapter 03 gap.

The four interactive visual systems now have explicit per-ID audit rows. All remain INTEGRATED, not VERIFIED, because creator/code rights and manual accessibility/device evidence are incomplete.

CI evidence in the publication checklist predates the latest Chemistry branch commits. A fresh CI run is required before current technical status can be reported as PASS. No new CI success is claimed by this documentation update.
## 2026-11-05 follow-up: targeted image-first search

Targeted searches were added for the existing chapter visuals and interactive models. Additional candidate findings are recorded in IMAGE_SOURCES.md: OpenStax Organic Chemistry section 3.1 / Table 3.1 is a functional-groups reference under the book's CC BY-NC-SA 4.0 terms, subject to item-level image-credit checks; NASA SVS carbon-cycle animation 10494 is a conceptual candidate with NASA/GSFC/UMBC and creator credits, subject to the NASA third-party-content caveat; Wikimedia Commons particle-comparison diagrams were found but not selected because one uses equal-density sphere assumptions and the other includes antiparticles beyond the learning objective. OpenStax reference sections for isotopes, mole concept, chemical formulas, solubility and balancing equations were also checked; the surfaced examples did not match the local figure's precise teaching purpose closely enough to replace it.

These targeted searches improve retrospective evidence but cannot prove that the search-first sequence occurred before the existing project-local visuals were authored. The original 11 SVG pairs and four interactive systems remain unclassified with rights PENDING until their actual creation history and project rights basis are confirmed.
## 2026-11-05 follow-up: standalone interactive visuals added to scope

A deeper page-by-page audit found three existing visual learning components that were not present in the original four-system inventory: the 3D molecular-geometry canvas, the gas-laws schematic particle-count display, and the acid–base virtual-lab beaker/pH indicator. They are now registered as CH-IV05 through CH-IV07, with per-ID audit rows, learning purposes and targeted image-first candidate searches. The whole-atlas denominator is therefore 19 visual units (12 chapter-level static topics + 7 interactive systems), of which 18 are integrated; the Chapter 03 periodic-trends diagram remains the only identified gap.

Source-level science review found the molecular geometry coordinates consistent with the displayed approximate geometries: H₂O ≈104.6°, CH₄ ≈109.5°, NH₃ ≈107° and linear CO₂. The gas-laws dots are explicitly a schematic count tied only to amount of substance, not a kinetic-theory simulation. The virtual neutralisation model states its strong monoprotic/monobasic, 25 °C, dilute/ideal and additive-volume assumptions and uses a water-autoionisation approximation near equivalence. These are first-pass source reviews, not independent expert certification.

Two accessibility improvements were made: the gas-laws particle visual now has a bilingual accessible name linked to its explanatory limitation note; the virtual beaker now has a bilingual accessible name linked to the live pH/status text. Manual screen-reader, keyboard, device and zoom checks remain pending.

PhET alternatives were located for molecule geometry, gas properties and acid/base solutions. The official PhET licensing page states regular HTML simulations are CC BY-NC 4.0 and requires attribution; these are candidates only, not adopted assets. The exact fit and non-commercial condition must be assessed before any future embedding.
## 2026-11-05 follow-up: periodic-table visible-label accessibility

Chromium/axe identified a serious label-content-name-mismatch on all 118 periodic-table element buttons in both languages. The buttons had an aria-label override that did not satisfy axe's visible-label-in-accessible-name check. Removed the redundant aria-label from the element buttons so the visible atomic number, chemical symbol, localized element name and mass provide the computed accessible name directly. The selected state remains exposed through aria-pressed, and selection updates in place to preserve keyboard focus. Static source validation passes after the correction; the updated Chromium/axe run is pending. Manual screen-reader testing remains outstanding.
## 2026-11-05 follow-up: current branch-head automated validation PASS

GitHub Actions run 41911003011 passed on branch workspace/chemistry at commit 7a4d60cca9407e059be913cd390e4ea89ced8c41. Static validation checked 22 HTML pages, 90 local links/assets, 21 inline scripts and 18 bilingual pages. Chromium smoke checks loaded all 21 configured pages, ran 42 axe-core WCAG 2.1 A/AA audits in Russian and English, toggled language on 21 pages, exercised key interactive workflows, and found no uncaught page errors. Responsive overflow checks at 390, 768 and 1280 CSS px passed.

This CI PASS includes the periodic-table accessible-name correction: element buttons now use their visible atomic number, symbol, localized name and mass as the computed accessible name rather than overriding it with aria-label. It also includes the bilingual accessible names added to the gas-laws particle visual and acid–base beaker.

Automated CI does not close the remaining manual screen-reader/device/zoom checks, independent scientific review, creator/rightsholder confirmation or licence verification. Therefore the whole-atlas Image Verification metric remains 0/18 despite the technical CI PASS.
## 2026-11-05 follow-up: learner-facing visual captions

A targeted caption audit found three actual omissions/defects and one false alarm. In Chapter 01, the electron-cloud caption existed but was not connected to the RU/EN language dictionary; it now switches in both languages. The reaction-rearrangement visual in Chapter 09 had alt text but no separate learner-facing caption; a bilingual caption was added. The Chemistry landing-page hero electron-cloud image had alt text but no caption; a bilingual caption was added. The Chapter 12 carbon-cycle image already had a separate bilingual `image-caption` paragraph keyed to `carbonCycleCaption`; an earlier scan that searched only for `figcaption` missed it, so no change was needed there.

The 10 chapter image pairs now have a caption or equivalent explanatory text in both languages; the landing-page hero visual also has a bilingual caption. The static regression checks now guard the three corrected caption cases and preserve the existing carbon-cycle caption.