# Chemistry Atlas — Image and visual audit

**Canonical standard:** [IMAGE-FIRST POLICY v1.0](https://github.com/Ajokendo/Atlas-of-Knowledge/blob/atlas-of-knowledge-integration/IMAGE_FIRST_POLICY.md)  
**Branch:** `workspace/chemistry`  
**Audit date:** 2026-11-05  
**Policy version:** IMAGE-FIRST POLICY v1.0  
**Scope of this checkpoint:** all 22 existing static SVG files (11 RU/EN pairs), their chapter integrations, and four identified interactive visual systems. This is an inventory and first-pass source-code review, not a complete independent scientific or legal certification. The repository does not contain a historical search log proving that ready-made licensed sources were considered before these project SVGs were created; compliance with the search-first sequence for past assets remains PENDING.

## Audit method

Use the canonical policy for status definitions, audit result values, evidence requirements, and verification rules. This file contains only Chemistry-specific findings and metrics; it does not redefine the universal standard.

## Summary metrics — current checkpoint

| Metric | Current result | Interpretation |
|---|---:|---|
| Static visual topics inventoried | 11 | Each topic has RU and EN SVG variants |
| Static SVG files inventoried | 22 | 11 English + 11 Russian |
| Interactive visual systems inventoried | 4 | Atomic model, subatomic-particle comparison, bonding models, periodic table |
| Static visuals integrated | 11 / 11 | All inventoried static visual pairs are used on the landing page or in a chapter |
| Provisional static Image Coverage | 11 / 11 = 100% | **Only for the 11 currently inventoried static visual topics; not a claim that every chapter has all required visuals** |
| Static Image Verification | 0 / 11 = 0% VERIFIED | All 11 pairs still lack file-specific creator/rightsholder and licence confirmation |
| Static Image Gaps | Not yet fully determined | Chapter 01 electron-cloud figure is on the landing page, not confirmed in the chapter; chapter 03 needs a documented decision on whether a static periodic-trends visual adds learning value. The complete visual-need matrix is still pending |
| Category A — external original reuse | 0 | No external image-source records established |
| Category B — adapted external reuse | 0 | No external adapted image-source records established |
| Category C — project-created SVG pairs | 11 | Provenance method and rightsholder still need confirmation |
| Search-first evidence | 15 / 15 records searched | No contemporaneous historical log exists. Retrospective searches cover all 15 records. These searches do not prove the original creation process followed image-first |
| Search candidates | 3 FOUND / 15 searched | OpenStax titration curve, OpenStax Daniell-cell figure, and PubChem interactive periodic table identified as candidates; none adopted pending suitability and item-level rights review |
| Rights / licence checks | 0 PASS / 15 PENDING | File-specific creator/rightsholder and licence evidence is not recorded for the 11 SVG pairs or four interactive systems |
| Scientific first-pass checks | 10 PASS / 1 PENDING | See detailed table; first-pass source-code review only |
| RU/EN metadata presence | 11 PASS / 0 FAIL | Paired SVG files and localized title/description elements exist; this is not a complete translation-quality or manual accessibility review |
| Technical source checks | 22 PASS for basic SVG metadata | CI checks viewBox, role, title, description and local asset paths; responsive/device review remains pending. Four interactive systems still need manual keyboard, zoom and screen-reader checks |

**Important:** the 11/11 ratio measures only whether the currently inventoried static topics exist and are integrated. It is not a measure of curriculum visual coverage or readiness. A learning-purpose and visual-need decision is still required for every chapter. Retrospective searches cover 14/15 records; the original search-first sequence cannot be proven retrospectively. Rights verification is 0/15; none of the visual records may be described as VERIFIED or publication-ready.

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
| CH-IV04 | Interactive periodic table | PENDING — independent element-data review remains separate | PENDING — data/code provenance to be reconciled with relevant notices | PENDING — full data-table and screen-reader review | PENDING — device and keyboard review | PENDING |

## Chapter-level visual gap register

| Chapter | Existing visual evidence | Current assessment | Next action |
|---|---|---|---|
| 01 Atomic structure | Two inline SVG models in the chapter (atom/electron-shell model and subatomic-particle comparison); electron-cloud image on landing page | INTEGRATED with two chapter-level models; no confirmed missing figure | Verify model limitations and accessible labels; avoid implying electron paths are classical orbits |
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
| 01 Atomic structure | Distinguish nucleus, electron probability distribution and subatomic particles; explain model limits | Two inline interactive SVGs; electron-cloud SVG currently on landing page | PENDING — confirm whether the electron-cloud figure should also appear in the chapter; review shell model wording and scale claims |
| 02 Chemical elements | Compare isotopes and explain weighted atomic mass | Carbon isotope SVG pair | INTEGRATED — science first-pass PASS; search and rights PENDING |
| 03 Periodic system | Relate element position to groups, periods and periodic trends | Interactive periodic table | PENDING — decide whether a dedicated trend diagram is needed; PubChem interactive table is a candidate reference for trend functionality, but reuse terms and data provenance require review |
| 04 Chemical bonding | Compare ionic, covalent and metallic bonding without presenting models as literal structure | Three inline interactive SVG models | INTEGRATED — model limitations are described in page text; manual accessibility and rights review PENDING |
| 05 Amount of substance | Connect mole, Avogadro constant and molar mass | One-mole SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 06 Chemical formulae | Read subscripts, brackets and coefficients | Formula-reading SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 07 Solutions | Compare unsaturated, saturated and metastable supersaturated states | Solution saturation SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 08 Acids and bases | Explain neutralisation and titration equivalence | Neutralisation SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 09 Chemical reactions | Show atom conservation and bond rearrangement | Reaction schematic SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 10 Redox | Trace oxidation, reduction and electron/ion movement in a galvanic cell | Daniell cell SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 11 Organic chemistry | Recognise major functional groups and avoid overgeneralising R–NH₂ | Functional-groups SVG pair | INTEGRATED — first-pass science PASS; search and rights PENDING |
| 12 Chemistry of life and environment | Compare biomolecule classes and explain major carbon reservoirs/flows | Biomolecule and carbon-cycle SVG pairs | INTEGRATED — first-pass science PASS; search and rights PENDING |

## Required follow-up before VERIFIED / publication-ready

1. Complete the remaining targeted search for CH-IV02 and improve the coverage of the other searches where no suitable candidate surfaced; record exact source pages and candidate/rejection decisions.
2. Confirm creator, authoring method, rightsholder and explicit licence or code/data rights basis for every project-created visual.
3. Complete the chapter-level learning-need sign-off, especially the Chapter 01 electron-cloud placement and Chapter 03 periodic-trend visual decision.
4. Perform manual inspection at phone/tablet/desktop widths, zoom/reflow, keyboard and screen-reader checks. CI does not establish these.
5. Re-run Chemistry CI after the register and checks changes; update metrics only from actual results.

## Automation boundary

CI can validate file existence, SVG metadata, local references, bilingual pairing, non-empty alt text and registry/audit presence. CI cannot certify scientific correctness, ownership, legal rights, the quality of translation, or actual assistive-technology/device behaviour.
