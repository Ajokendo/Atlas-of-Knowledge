# Chemistry Atlas — Image and visual audit

**Standard:** IMAGE-FIRST POLICY v1.0  
**Branch:** `workspace/chemistry`  
**Audit date:** 2026-11-05  
**Scope of this checkpoint:** all 22 existing static SVG files (11 RU/EN pairs), their chapter integrations, and three identified interactive visual systems. This is an inventory and first-pass source-code review, not a complete independent scientific or legal certification.

## Status vocabulary

- **MISSING** — required visual not yet available.
- **FOUND** — candidate visual located, not yet checked.
- **LICENSE_CHECK** — file-specific rights evidence is being checked.
- **SCIENTIFIC_CHECK** — scientific content requires review.
- **ADAPTED** — source visual has been modified; adaptation details must be recorded.
- **INTEGRATED** — visual is present in the subject atlas.
- **VERIFIED** — all applicable scientific, rights, bilingual and technical checks pass.
- **REJECTED** — visual must not be published.

Audit result values: **PASS**, **FAIL**, **PENDING**, **NOT APPLICABLE** (with reason). A visual is not VERIFIED if any applicable check is pending.

## Summary metrics — current checkpoint

| Metric | Current result | Interpretation |
|---|---:|---|
| Static visual topics inventoried | 11 | Each topic has RU and EN SVG variants |
| Static SVG files inventoried | 22 | 11 English + 11 Russian |
| Interactive visual systems inventoried | 3 | Atomic model, bonding models, periodic table |
| Static visuals integrated | 11 / 11 | All inventoried static visual pairs are used on the landing page or in a chapter |
| Provisional static Image Coverage | 11 / 11 = 100% | **Only for the 11 currently inventoried static visual topics; not a claim that every chapter has all required visuals** |
| Static Image Verification | 0 / 11 = 0% VERIFIED | All 11 pairs still lack file-specific creator/rightsholder and licence confirmation |
| Static Image Gaps | 2 provisional chapter-placement/content gaps | Dedicated chapter 01 placement for the electron-cloud illustration; a chapter 03 explanatory visual beyond the interactive periodic table may be required after curriculum review |
| Category A — external original reuse | 0 | No external image-source records established |
| Category B — adapted external reuse | 0 | No external adapted image-source records established |
| Category C — project-created SVG pairs | 11 | Provenance method and rightsholder still need confirmation |
| Licence checks | 0 PASS / 11 PENDING | No file-specific licence evidence currently recorded |
| Scientific first-pass checks | 9 PASS / 2 PENDING | See detailed table; first-pass source-code review only |
| RU/EN technical content checks | 11 PASS / 0 FAIL | Paired files and localized titles/descriptions exist; independent translation review remains pending |
| Technical source checks | 22 PASS for basic SVG metadata | CI checks viewBox, role, title, description and local asset paths; responsive/device review remains pending |

**Important:** the provisional 100% static coverage ratio uses only the 11 static visual topics already present in the repository. It must not be reported as 100% chapter visual readiness. The atlas has 12 curriculum chapters; the full required-visual plan needs a chapter-by-chapter editorial decision. Licence verification is currently 0%, so the static set is **not publication-verified**.

## Static visual audit register

| ID / visual | Files | Science | Licence / provenance | RU/EN | Technical | Integration | Result / findings |
|---|---|---|---|---|---|---|---|
| CH-V01 Electron probability cloud | EN + RU | PENDING | PENDING | PASS — paired title/description | PASS — viewBox, role, title, desc | PASS — landing page | PENDING. Descriptive illustration; ensure text makes clear that the cloud represents probability distribution, not a literal orbit or solid shell. Chapter 01 placement not confirmed. |
| CH-V02 Carbon isotopes | EN + RU | PASS — 6 p⁺/6 n⁰ for C-12; 6 p⁺/7 n⁰ for C-13; abundance-weighted mean ≈12.011 | PENDING | PASS — paired title/description and labels | PASS — existing CI also checks nucleus counts | PASS — chapter 02 | PENDING due rights evidence. Natural abundance values are rounded approximations, as labelled. |
| CH-V03 One mole | EN + RU | PASS — Avogadro constant exact; water molar mass shown approximately | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 05 | PENDING due rights evidence. Russian label should use “элементарных сущностей” rather than the narrower “частиц” for the SI definition; fix is queued in this checkpoint. |
| CH-V04 Reading chemical formulae | EN + RU | PASS — subscripts, bracket multiplier and coefficient are distinguished | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 06 | PENDING due rights evidence. |
| CH-V05 Solution saturation | EN + RU | PASS — distinguishes unsaturated, saturated equilibrium and metastable supersaturated solution | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 07 | PENDING due rights evidence. Keep same-temperature condition visible. |
| CH-V06 Acid–base neutralisation | EN + RU | PASS — net ionic reaction and qualified equivalence pH for strong acid/strong base at 25 °C | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 08 | PENDING due rights evidence. Existing CI checks the equivalence-curve marker. |
| CH-V07 Reaction atom rearrangement | EN + RU | PASS — conveys conservation of atoms and bond rearrangement | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 09 | PENDING due rights evidence. |
| CH-V08 Daniell cell | EN + RU | PASS — Zn oxidation, Cu²⁺ reduction, electron direction and salt-bridge ion migration | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 10 | PENDING due rights evidence. |
| CH-V09 Organic functional groups | EN + RU | PENDING — R–NH₂ represents a primary amine, not the whole amine class | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 11 | PENDING. Clarify the primary-amine label in both languages before scientific PASS. |
| CH-V10 Biomolecule overview | EN + RU | PASS — explicitly avoids treating all lipids as repeating-monomer polymers | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 12 | PENDING due rights evidence. |
| CH-V11 Carbon cycle | EN + RU | PASS — major reservoirs and exchanges shown; omissions explicitly acknowledged | PENDING | PASS — paired files | PASS — SVG metadata and local reference | PASS — chapter 12 | PENDING due rights evidence. This is a simplified conceptual diagram, not a quantitative flux diagram. |

## Interactive visual audit

| ID | Visual | Scientific review | Rights/provenance | Bilingual / accessibility | Technical | Result |
|---|---|---|---|---|---|---|
| CH-IV01 | Atomic structure interactive model | PENDING — verify shell/orbital language and model limitations against chapter text | PENDING — creator and code licence not evidenced in this register | PASS — language-dependent accessible label found in source; manual screen-reader review pending | PENDING — needs responsive and keyboard/manual review | PENDING |
| CH-IV02 | Ionic, covalent and metallic inline SVG models | PENDING — simplified models need contextual qualifications | PENDING — creator and code licence not evidenced in this register | PASS — generated SVG receives localized accessible name/description in source | PENDING — manual keyboard, zoom and screen-reader review | PENDING |
| CH-IV03 | Interactive periodic table | PENDING — independent element-data review remains separate | PENDING — data/code provenance to be reconciled with relevant notices | PENDING — full data-table and screen-reader review | PENDING — device and keyboard review | PENDING |

## Chapter-level visual gap register

| Chapter | Existing visual evidence | Current assessment | Next action |
|---|---|---|---|
| 01 Atomic structure | Electron-cloud image on landing page; interactive atom model in chapter page | INTEGRATED at atlas level; chapter figure placement and scientific wording require confirmation | Decide whether the electron-cloud figure should also be embedded in chapter 01; avoid implying electron paths are classical orbits |
| 02 Chemical elements | Isotope abundance figure | INTEGRATED | Keep |
| 03 Periodic system | Interactive periodic table | INTEGRATED as an interactive visual, not a static figure | Decide whether a separate periodic-trend diagram is pedagogically required |
| 04 Chemical bonding | Three interactive inline SVG models | INTEGRATED as interactive visual | Review model limitations and add static fallback only if needed |
| 05 Amount of substance | One-mole figure | INTEGRATED | Correct Russian “particles” wording to “elementary entities” |
| 06 Chemical formulae | Formula-reading figure | INTEGRATED | Keep |
| 07 Solutions | Saturation particle models | INTEGRATED | Keep |
| 08 Acids and bases | Neutralisation / titration figure | INTEGRATED | Keep |
| 09 Chemical reactions | Atom-rearrangement figure | INTEGRATED | Keep |
| 10 Redox | Daniell cell figure | INTEGRATED | Keep |
| 11 Organic chemistry | Functional-group figure | INTEGRATED | Specify primary amine for R–NH₂ |
| 12 Chemistry of life and environment | Biomolecule overview and carbon-cycle figures | INTEGRATED | Keep |

## Required follow-up before VERIFIED / publication-ready

1. Confirm creator, authoring method and rightsholder for every project-created SVG and interactive visual.
2. Establish the explicit licence for these assets and add the actual licence link/text. Do not infer permission from repository presence.
3. Complete chapter-by-chapter visual-need sign-off; decide on the two provisional gaps above.
4. Resolve the scientific wording items in CH-V03 and CH-V09.
5. Perform manual visual inspection at phone/tablet/desktop widths, zoom/reflow, keyboard and screen-reader checks. CI does not establish these.
6. Re-run the full Chemistry CI after the fixes and update the metrics with actual results.

## Automation boundary

CI can validate file existence, SVG metadata, local references, bilingual pairing, non-empty alt text and registry/audit presence. CI cannot certify scientific correctness, ownership, legal rights, the quality of translation, or actual assistive-technology/device behaviour.
