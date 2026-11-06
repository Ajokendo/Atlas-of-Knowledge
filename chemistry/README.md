> **Project review boundary (current instruction, 6 November 2026):** External expert/teacher assessment is **not part of the Chemistry Atlas development or internal acceptance workflow**. Any external assessment will be organised separately after this project stage. Older dated checkpoints below that list independent chemistry-teacher or subject-matter review as a pending “external gate” are historical wording and are superseded by this instruction; they must not be treated as active Atlas tasks or blockers. Internal source review, bilingual consistency checks, automated tests, accessibility checks, provenance and rights documentation, and the project's own final editorial decision remain in scope. Physical-device and assistive-technology checks are distinct operational checks; they are not external subject-matter certification.



### Tablet-width periodic table follow-up — 6 November 2026

- [x] 768 px scan found that the periodic table needed horizontal scrolling but did not show its instruction at tablet widths.
- [x] Hint now remains visible up to 1050 px; Chromium tests cover the 768 px scroll state and 1280 px fit state. Run [42171810358](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42171810358) passed on `e3c3579`.
- [x] Exact Russian wording assertion passed in run [42172003249](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42172003249) on `2dfc46e`; updated 768 px screenshot confirms the tablet hint.

### Bilingual rendered screenshots

- [x] Expanded the screenshot artifact to include both Russian and English baselines for all 12 selected pages at 390, 768 and 1280 CSS-pixel widths (72 images per successful run).
- [x] Refined periodic-trend arrowhead scale and hid the mobile scroll hint at desktop widths; branch-head CI and artifact review are pending.

### Mobile-first acid–base diagram — 6 November 2026

- [x] Added a vertically stacked mobile version of the neutralisation visual so reaction labels, titration curve and model notes remain readable on narrow screens.
- [x] Kept the wide RU/EN SVG pair for desktop and synchronised mobile labels/accessible name with the language toggle.
- [x] Added static and browser assertions for the responsive layout and bilingual content; fresh CI is pending.

### Acid–base visual correction — 6 November 2026

- [x] Repaired the Russian titration-curve note overlapping the x-axis caption.
- [x] Rebuilt the English SVG's Brønsted–Lowry explanation panel, which was positioned outside the SVG viewBox.
- [x] Added static regression checks for both language variants; fresh branch-head CI is pending.

### First rendered screenshot review — 6 November 2026

- [x] Inspected the first retained screenshot artifact from run [42158701555](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42158701555).
- [x] Corrected the periodic-table mobile horizontal-scroll affordance and keyboard accessibility in both language modes; browser regression run [42170499572](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42170499572) passed.
- [x] Corrected arrow/label overlap in the Russian and English periodic-trends SVGs and added a source regression guard.
- [ ] Re-inspect the next screenshot artifact after these changes; review of all 36 baseline images and all interactive states remains incomplete.

### Rendered visual evidence in CI — 6 November 2026

- [x] Added full-page baseline screenshots for 12 key Chemistry visual pages at 390, 768 and 1280 CSS-pixel widths (72 captures per successful run (RU + EN × 12 pages × 3 widths)).
- [x] GitHub Actions now uploads the screenshots as the `chemistry-rendered-review` artifact for 7 days.
- [x] Run [42171472363](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42171472363) passed on `cf15ec1`; the artifact contains 72 RU/EN screenshots across 390/768/1280 px.
- [x] Contact-sheet scan of all 390 px and 1280 px captures completed; focused full-size review corrected periodic-trend arrow overlap and acid/base mobile readability/contrast.
- [ ] Scan the 768 px captures and continue manual review of the remaining page-specific visuals and interactive states; screenshot generation is evidence capture, not full visual approval.

### Reproducible browser-audit toolchain

The Chemistry CI workflow installs exact versions of its browser-audit dependencies rather than floating npm tags: Playwright `1.64.1` and axe-core `4.14.0`. It prints the resolved top-level dependency tree with `npm ls --depth=0` before installing Chromium, so CI logs retain evidence of the tool versions used for each run. These are test-only dependencies; the static Chemistry Atlas remains dependency-free for visitors. Update either pinned version deliberately, then review the release notes and require a fresh full CI run before accepting the change.


### Verification checkpoint — 2026-11-01

- [x] Pinned-toolchain commit `d203edc1e79207df727b480a199fbb747225e2f0`: Chemistry Actions run [41321214353](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41321214353) completed successfully.
- [x] Documentation commit `f3fe2b96c0a0f7db25ce6f2408116c9403a279e9`: Chemistry Actions run [41321221712](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41321221712) completed successfully.
- [x] Both runs completed the repository validation, pinned browser-tool installation, local server startup, and Chromium tests across the Chemistry pages.
- [x] The latest recorded automated accessibility gate covers all 21 Chemistry pages in Russian and English (42 axe-core scans), with no serious or critical findings in the final CI run.
- [ ] Physical-device, screen-reader, and independent scientific reviews remain external pending gates; CI success does not satisfy them.

- [x] Checkpoint commit `e244cb8c894eb5cb1ab1aa8a48615cd26b3d17f4`: full Chemistry CI run [41326918004](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41326918004) completed successfully, including repository checks and the Chromium browser suite.


### Internal audit progress — 80% (2026-11-01)

This percentage refers only to the current internal automated/technical audit stage. It is not a publication-readiness percentage and does not include the outstanding external reviews.

- [x] Re-ran the full repository and browser validation after the checkpoint documentation changes. Both resulting CI runs completed successfully: [README evidence run 41327013009](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41327013009) and [publication-checklist evidence run 41327016326](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41327016326).
- [x] Reviewed browser-suite coverage: 21 pages at 390, 768 and 1280 CSS-pixel widths; Russian/English switching; 42 axe-core scans; page errors, images, internal links, keyboard entry focus, labels and selected contrast pairs.
- [x] Confirmed targeted interaction tests for formula parsing (including grouped formulas and invalid/overflow inputs), pH classification, Nernst calculation, gas-law temperature conversion, limiting-reactant calculations and numeric boundaries, all six reaction-trainer tasks, and the bilingual knowledge check.
- [x] Confirmed automated source checks for 118 periodic-table records, bilingual glossary and quiz data, SVG accessibility metadata, local assets and script syntax.
- [ ] Remaining internal work: inspect uncovered interaction states and edge cases, reconcile any test gaps, and complete a final regression run.
- [ ] External gates remain pending: physical Android/iOS devices, NVDA/TalkBack/VoiceOver screen-reader testing, full keyboard/zoom review by a human tester, and independent chemistry subject-matter review/sign-off.

Do not mark any external gate complete based on CI. The successful runs above are browser automation on GitHub-hosted Chromium, not testing on physical devices or assistive technologies.

### Internal audit progress — 85% (2026-11-02)

This is the internal audit milestone only. It is not a publication-readiness percentage and does not imply completion of independent or real-device testing.

- [x] Full Chemistry CI run [41335696007](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41335696007) completed with `status=completed` and `conclusion=success` on branch `workspace/chemistry`, commit `fa90e1a3cf83a173049e635f1b7ee467b4ccfd35`.
- [x] Repository validation, pinned browser-audit tool installation, local site server startup, and the Chromium suite for every Chemistry Atlas page all completed successfully.
- [x] The keyboard-sequence assertion now uses the same focusable-element selector for its expected sequence and active-focus lookup, including explicit `[tabindex]` targets; the resulting full CI run passed.
- [ ] Remaining internal work: inspect uncovered interaction states and edge cases, reconcile any remaining test gaps, and complete a final regression run.
- [ ] External gates remain pending: physical Android/iOS device testing, manual keyboard/zoom review, NVDA/TalkBack/VoiceOver testing, independent scientific review, and any outstanding independent RU/EN editorial review.

The successful CI run is automated testing on GitHub-hosted Chromium. It is not evidence of testing on physical devices, assistive technologies, or independent expert sign-off.

### Teacher feedback preparation — Chemistry (2026-11-02)

- [x] Added the subject-adapted standard: `FEEDBACK_SYSTEM_STANDARD.md`.
- [x] Added the private moderation and issue-processing procedure: `FEEDBACK_PROCESSING_GUIDE.md`.
- [x] Added the bilingual Chemistry questionnaire template: `FEEDBACK_WIDGET_TEMPLATE.html`. It includes nine shared 1–5 / Cannot assess criteria, chemistry-specific prompts for formulae, equations, coefficients, subscripts, units, calculations, models and virtual labs, targeted location, priority, optional evidence/contact, and a separate voluntary publication choice.
- [x] Submission is intentionally unavailable: the button is disabled, the control is non-submitting (`type=button`), and the template has no endpoint, submit handler, network request or browser storage logic. It must not be enabled before portal completion, a separate security/technical review, and explicit project-owner approval.
- [x] Added automated safeguards in `checks.mjs` to prevent accidental activation or addition of client-side collection/storage logic and to verify all nine “Cannot assess” choices.
- [ ] This is preparation only, not a live feedback channel. No real responses have been collected or stored. The portal-wide feedback entry point and shared backend remain outside this subject branch's scope.


### Reference provenance and regression checkpoint — 2026-11-02

- [x] Added bilingual source links for fundamental constants to NIST/CODATA 2022.
- [x] Added IUPAC Gold Book references for standard pressure, standard gas conditions, standard thermodynamic quantities, and the autoprotolysis constant of water.
- [x] Clarified that IUPAC standard conditions for gases are 273.15 K and 100 kPa, while 298.15 K is a commonly used separately stated temperature for thermodynamic data.
- [x] Added automated checks for the displayed constants, authoritative source URLs, bilingual qualifications, and the standard-condition distinction.
- [x] Added browser assertions for all five external source links, safe new-tab attributes, RU/EN labels, and unchanged numerical values after language switching.
- [x] Full Chemistry CI run [41341078589](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41341078589) completed with `status=completed` and `conclusion=success` on commit `51b373ce6eeccd5ff5f0aac2ddf95547aa170b19`.
- [ ] Physical-device, assistive-technology, manual zoom/reflow, and independent scientific reviews remain external pending gates. This checkpoint does not change the recorded 85% internal audit milestone.

- [x] Expanded the molecular-laboratory browser checks to exercise arrow-key rotation, pointer dragging, reset to the default orientation, and preservation of the selected molecule plus its accessible name across RU/EN switching.
- [x] Full Chemistry CI run [41341324210](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41341324210) completed with `status=completed` and `conclusion=success` on commit `76d4899c3da587dbae516f66ebcf199cb22bc0dc`.

- [x] Expanded ideal-gas regression coverage for all three slider bounds/steps, pressure response to amount and volume, and particle-count scaling. Full Chemistry CI run [41341571748](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41341571748) completed with `status=completed` and `conclusion=success` on commit `0f2ab4010ac27389fe573697c57a31105f2ee1e6`.

### Acid–base virtual laboratory regression checkpoint — 2026-11-02

- [x] Extended Chromium checks for the initial 0.10 mol/L strong-acid pH, strong-base excess, equivalence-volume scaling when acid volume is doubled, and equivalence-volume scaling when base concentration is doubled.
- [x] Checked bilingual equivalence status and volume units, plus rejection of an acid concentration above the model's declared range without leaving stale visual output.
- [x] The first run exposed an incorrect expected volume in the newly added test (the test used 100 mL where 200 mL was required after doubling the acid volume). The test scenario was corrected; no chemistry-model code change was needed.
- [x] Full Chemistry CI run [41342268215](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41342268215) completed with `status=completed` and `conclusion=success` on commit `bd2cf5322ced0019128c1c71e3b35e633e0b0496`.

- [x] Extended reaction-trainer browser checks to reject decimal and zero coefficients without locking the task or advancing progress. Full Chemistry CI run [41342407125](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41342407125) completed with `status=completed` and `conclusion=success` on commit `b77394eaa4eed665e72dafef4356cf26c39c6da5`.


### Calculation-tool regression checkpoint — 2026-11-02

- [x] Added browser-level calculation checks for the amount-of-substance tool: 36.03 g H₂O at 18.015 g/mol gives 2 mol; a custom 25 g / 10 g·mol⁻¹ case gives 2.5 mol and the corresponding Avogadro particle count; zero sample mass gives zero entities; zero molar mass is rejected; particle-count overflow is rejected.
- [x] Added browser-level checks for the solution-concentration tool: 0.5 mol in 1 L gives 0.5 mol/L; doubling final solution volume halves concentration; zero solute amount is valid; zero volume and numeric overflow are rejected; English/Russian output and validation messages are checked.
- [x] The new checks explicitly reset calculator inputs because earlier checks on the same page intentionally leave non-default values. Decimal parsing accepts both RU and EN number formats.
- [x] No production calculator formula change was indicated by this review: the inspected calculations use n = m/M, N = n·Nₐ and c = n/V with input/range guards. This is a code review plus automated Chromium regression, not independent chemistry sign-off.
- [x] Full Chemistry CI run [41343565722](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41343565722) completed with `status=completed` and `conclusion=success` on commit `5a3e952b536b779aa671379fec48e1e425b536e0`.
- [ ] Physical-device, assistive-technology, manual zoom/reflow, independent scientific review, and independent RU/EN editorial sign-off remain external pending gates.


### Electrochemistry and biochemical-energy checkpoint — 2026-11-02

- [x] Reviewed the Daniell-cell model: oxidation at the zinc anode, reduction at the copper cathode, electron direction, galvanic/electrolytic electrode signs, standard cell potential, Gibbs-energy relation, and the reaction quotient used in the Nernst equation.
- [x] Extended the Nernst calculator's Chromium regression coverage with blank input and an extreme finite activity ratio, in addition to the existing standard-state, direction-of-change, zero-activity, and RU/EN checks.
- [x] Improved the bilingual ATP explanation: added the schematic hydrolysis equation `ATP + H₂O → ADP + Pᵢ` and clarified that `ΔG°′ ≈ −30.5 kJ/mol` applies to biochemical standard conditions near pH 7, while the actual cellular value depends on concentrations and conditions.
- [x] Added bilingual browser assertions for the ATP equation and thermodynamic qualification.
- [x] Full Chemistry CI run [41344361142](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41344361142) completed successfully on commit `9be0bc14bc8cb22e555e84f5a39f244e290256b8`.
- [ ] External chemistry-teacher review, physical-device checks, screen-reader checks, and independent editorial sign-off remain pending. This checkpoint is an internal content review plus automated browser verification, not external scientific certification.


### Organic chemistry coverage checkpoint — 2026-11-02

- [x] Expanded the bilingual organic-family overview to include alkynes, alongside alkanes and alkenes. The new definition limits the formula CₙH₂ₙ₋₂ to acyclic monoalkynes and gives ethyne (acetylene), C₂H₂, as an example.
- [x] Added Chromium regression assertions for the C≡C triple bond, the stated formula, and the ethyne example in both Russian and English.
- [ ] This is an internal content/automated-browser checkpoint only. Independent chemistry-teacher review, manual device checks, screen-reader checks, and independent RU/EN editorial sign-off remain pending.

- [x] Follow-up CI caught a stale browser assertion that still expected ten organic-family cards after adding alkynes. Updated the expected count to eleven; the failure was in the regression assertion, not the chemistry content.

- [x] Scientific wording review of the arene family: narrowed the definition from the overly broad “aromatic compounds” to aromatic hydrocarbons containing one or more benzene rings, in both languages. Added matching RU/EN browser assertions.

- [x] The first follow-up CI run caught a bilingual synchronization issue: the Russian translation dictionary had the corrected arene definition, but the page's initial HTML text still contained the older wording. Synchronized the initial markup; the repository's translation-consistency check covers this mismatch.


### Solution-equilibrium and calculator validation checkpoint — 2026-11-02

- [x] Reviewed the solution chapter's equilibrium-solubility distinction, saturation states, Henry's-law wording, and ionic-product comparison against Kₛₚ in both languages. No production formula correction was indicated in the reviewed passages.
- [x] Expanded Chromium regression coverage for the concentration calculator to reject negative solute amount, negative final solution volume, and an empty amount field; these cases must not be silently interpreted as valid zero concentration.
- [ ] Independent chemistry-teacher review and manual device/accessibility checks remain pending.

- [x] Added RU/EN Chromium assertions for ΔᵣG° = −RT ln K, the signs associated with K above/below 1, the standard-state qualification, the qualitative Le Chatelier wording, and the fact that a catalyst changes the rate of reaching equilibrium but not its position or K at fixed temperature.


### Bilingual chemistry review checkpoint — 2026-11-02

- [x] Fixed a real RU/EN defect in the chemical-formula calculator: parser validation errors were previously emitted in English regardless of the selected language. Added localized messages for invalid coefficients/subscripts, empty or missing brackets, unexpected characters, unknown element symbols, and atom-count overflow.
- [x] Expanded Chromium regression coverage for coefficient formulae (`2H2O`), grouped formulae (`Al2(SO4)3`), nested groups (`K4(ON(SO3)2)2`), unknown symbols, missing brackets, empty input, and zero coefficients/subscripts in Russian; added English invalid-input and successful-parse checks.
- [x] Expanded bilingual acid–base regression checks for the distinction between acid strength and concentration, conjugate acid–base pairs, Kₐ, the approximate nature and conditions of the Henderson–Hasselbalch equation, and finite buffer capacity.
- [x] Chromium CI passed for the localized formula parser and initial regression additions (commit `f7f379d`); the expanded acid–base checks passed with commit `fe282de`.
- [ ] Continue scientific review of remaining chapter content and calculation tools; continue editorial RU/EN parity review. This checkpoint does not represent external scientific certification or manual device testing.


### Core-chapter science and bilingual audit checkpoint — 2026-11-02

- [x] Added static regression evidence checks for atomic structure, the limits of shell/orbital diagrams, ionic lattices, bond versus molecular polarity, acid strength versus concentration, temperature-dependent neutral pH, buffer approximation/capacity limits, Henry's law, equilibrium solubility versus dissolution rate, Qₛₚ/Kₛₚ and nucleation, and the mole/entity distinction.
- [x] Corrected two test expectations to match the published Russian wording in the amount-of-substance chapter; no content defect was found there.
- [x] Re-ran full CI after correcting the two assertion expectations; the latest branch-head run completed successfully, including Chromium checks for all 21 pages.

- [x] Expanded Chromium regression coverage for all three carbon isotope model states (C-12/C-13/C-14), live-region announcements, and the weighted-average explanation in RU/EN.
- [x] Added RU/EN formula-theory assertions distinguishing empirical formulae, molecular formulae, ionic formula units, and the limits of structural information in a molecular formula.
- [x] Added RU/EN chemistry-of-life checks for carbohydrate classification, zwitterionic/amphoteric amino acids, ribosomal peptide-bond formation, protein structural levels/denaturation, lipid classification, antiparallel DNA and 5′→3′ polymerase extension, ATP thermodynamic qualifications, and base pairing.
- [x] Added bilingual redox exception checks for oxygen in OF₂, peroxides, and superoxides.
- [ ] Await the complete Chromium and static-validation run for this expanded suite; continue remaining chapters and formula/calculator checks.
- [x] Chromium exposed a test-order dependency: the new C-12/C-13/C-14 sequence left C-14 selected before an older accessibility assertion that expected the default C-12 state. The test now explicitly restores C-12 between scenarios; the chemistry content and isotope model were not defective.
- [x] Expanded Chromium suite passed on commit `db6f971d50a85b6e55e726079be45efc7155c64c`: all 21 Chemistry Atlas pages loaded; 42 axe-core RU/EN scans completed; isotope states, formula theory, biomolecule explanations and redox exceptions passed the new bilingual assertions.

- [x] Corrected a genuine dimensional-precision issue in the bilingual glossary: pH is now defined through dimensionless hydronium activity, with the dilute-solution approximation written as a logarithm of the dimensionless concentration ratio [H₃O⁺]/(1 mol/L), rather than taking the logarithm of a dimensional concentration.
- [x] Added RU/EN browser assertions for the pH definition and the reference-page qualifications for K_w activities, concentration-form units, IUPAC standard pressure, standard gas conditions and the separate 298.15 K thermodynamic-data temperature.
- [ ] Re-run static validation and full Chromium suite on the latest saved commit.
- [x] Corrected a second test-only wording mismatch in the Russian reference-data assertion: the page says «произведение безразмерно», not «безразмерным». The reference text was already scientifically correct; the assertion now matches it exactly.
- [x] The glossary pH correction and the new reference-data RU/EN assertions passed the full Chromium run on commit `de99c192092796d32bc1b4ced377af1734cf1ff8`; the latest branch SHA matched the successful run SHA. The test wording was corrected to match the exact Russian adjective in the existing reference note.

- [x] Refined two glossary entries during bilingual editorial review: the periodic law now describes the periodic variation of element properties with increasing atomic number (without overgeneralising compound properties), and the English molar-concentration definition now states the SI unit mol/m³ as well as the commonly used mol/L.
- [x] Added RU/EN glossary browser assertions for both entries; CI pending for this latest glossary refinement.


### Latest internal audit checkpoint — 90% (2026-11-04)

This percentage refers to the internal automated/technical audit stage only. It is not publication readiness and does not include external human reviews or physical-device testing.

- [x] Corrected the two Russian amount-of-substance test expectations to match the existing chapter wording; the scientifically correct learning text was not changed for the sake of the assertions.
- [x] Completed the follow-up bilingual glossary refinements: the periodic-law entry now describes periodic variation in element properties with increasing atomic number, and the molar-concentration entry states SI mol/m³ alongside commonly used mol/L.
- [x] Full latest branch-head CI run [41889220939](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41889220939) completed successfully on commit `73affc2476dc4f14d6f8b6bf569d8b546df57868`.
- [x] Static validation passed: 22 HTML pages, 89 local links/assets, 21 inline scripts, and RU/EN dictionaries on 18 pages.
- [x] Chromium smoke suite passed on all 21 Chemistry pages; all 42 axe-core RU/EN scans completed, language switching and key interactive workflows passed, and no uncaught page errors were reported.
- [x] Responsive horizontal-overflow checks ran at 390, 768 and 1280 CSS-pixel widths. This is an automated layout-overflow check, not a substitute for manual visual inspection or browser zoom testing.
- [ ] Remaining internal work: continue targeted scientific and bilingual review of any not-yet-audited passages and interactive edge cases; record only verified corrections and rerun CI after changes.
- [ ] External gates remain pending: physical Android/iOS checks, manual keyboard and 200%/400% zoom/reflow review, NVDA/TalkBack/VoiceOver testing, independent chemistry subject-matter review, and final publication approval.

The successful CI run is evidence of repository validation and automated GitHub-hosted Chromium testing only. It is not independent scientific certification, physical-device testing, or final release approval.


- [x] Revalidated the saved audit report and publication checklist themselves: full CI run [41891315678](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41891315678) completed successfully on commit `f0d862a82893ba3caa0eb946bd216b815b620825`; static validation and the complete Chromium job both passed.

### Internal technical audit completion — 100% (2026-11-05)

This closes the defined internal automated/technical audit scope. It is not external publication acceptance and does not include physical-device testing, assistive-technology testing by human users, or independent chemistry-teacher sign-off.

- [x] Reviewed remaining high-value interaction gaps and extended `browser-smoke.mjs` with regression checks for periodic-table category/group filter combinations, empty search results and RU/EN state preservation.
- [x] Added a completed reaction-trainer restart check: first task restored, controls unlocked, progress reset, and no duplicate completed attempt stored.
- [x] Added exact-stoichiometric-state bilingual regression: equal reactant ratios, no excess reagent, unchanged theoretical yield and translated explanation after switching language.
- [x] Added ideal-gas maximum-boundary regression: n = 3 mol, V = 5 L, t = 300 °C; pressure checked against PV = nRT using T = 573.15 K, then verified unchanged under RU/EN switching with localized units.
- [x] Full branch-head CI run [41894536945](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41894536945) completed successfully on commit `51fa0dcf9f66a256900c34d793e5e3d4e34bfac6`.
- [x] Static validation passed: 22 HTML pages, 89 local links/assets, 21 inline scripts, and 18 bilingual dictionaries.
- [x] Chromium suite passed on all 21 pages; 42 RU/EN axe-core scans completed; all 21 language toggles and key interactive workflows passed; no uncaught page errors.
- [x] Responsive overflow checks at 390, 768 and 1280 CSS-pixel widths remained green.
- [x] No production chemistry calculation or learning content change was required by this final edge-case pass; the changes strengthened regression coverage and verified existing behavior.
- [ ] External release gates remain open: physical Android/iOS testing; manual keyboard-only and 200%/400% zoom/reflow review; NVDA/TalkBack/VoiceOver testing; independent chemistry subject-matter review; final publication approval.

The 100% result applies only to the defined internal technical audit. It must not be presented as a claim that the atlas is fully externally validated or publication-approved.

### Image-first visual governance checkpoint — 2026-11-05

- [x] Added `IMAGE_SOURCES.md`: source register for all 22 existing static SVG files (11 English/Russian pairs), plus the identified inline and interactive visual systems.
- [x] Added `IMAGE_AUDIT.md`: first-pass scientific, bilingual, accessibility and technical audit; chapter-level visual inventory; coverage/verification metrics; and unresolved publication gates.
- [x] Registered all 12 curriculum chapters and distinguished static illustrations from inline SVG models and the interactive periodic table.
- [x] Extended `checks.mjs` to require source/audit records for every SVG file, enforce RU/EN SVG pairing, check non-empty image alt text and localized SVG references, and ensure the inline Chemistry visual systems remain inventoried.
- [x] Corrected the Russian one-mole illustration to use “элементарные сущности” and “моль”.
- [x] Clarified that the `R–NH₂` example in the organic functional-groups illustration is a **primary amine**, in both SVG languages and bilingual alternative text.
- [x] Fixed the mobile horizontal overflow in the chemical-bonding comparison table found during the Chromium regression run.
- [ ] Rights gate remains open: creator/rightsholder and explicit licence evidence for project-created SVGs and inline models are not established in repository metadata. These assets are therefore not marked VERIFIED.
- [ ] Independent scientific/editorial sign-off, manual responsive/zoom review, and physical-device / assistive-technology testing remain external gates.

**Checkpoint metrics (static SVG inventory only):** 11 visual topics / 22 files; 11 of 11 static topics integrated (100% provisional static coverage); 0 of 11 VERIFIED (0% image verification); 0 confirmed missing static assets; 1 chapter-level visual-need decision remains pending. Category C: 11 project SVG pairs; categories A/B: 0 evidenced assets. All 11 licence checks remain PENDING. The provisional static coverage figure does not mean the atlas is publication-ready or that every possible chapter visual need has been approved.


### Chemistry continuation checkpoint — 2026-11-05

- [x] Reconciled the automated provenance assertions with the current file-level Category C mapping for the 12 bilingual static SVG families. The checks now require documented provenance mapping while keeping rightsholder, licensing authority and licence evidence explicitly PENDING; Category C is not treated as automatic rights clearance.
- [x] Full branch-head CI run [42034196615](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42034196615) passed on commit `03497d8ed64dd5e9891639c8c9808979a823afcf`.
- [x] Static validation passed; Chromium smoke checks loaded all 21 Chemistry pages at 390 CSS px, completed 42 axe-core scans (RU + EN), checked 21 language toggles and key interactive workflows, and reported no uncaught page errors.
- [x] Current visual inventory: 12 bilingual static families / 24 SVG files and 7 interactive visual systems. Coverage/integration is recorded separately from verification; no static family or interactive system is labelled `VERIFIED` while applicable rights and review gates remain open.
- [ ] Continue the targeted bilingual and scientific source review, starting with the carbon-isotope SVG pair. The English figure has been updated with natural-abundance values and the weighted-mean expression; complete manual semantic/rendered pair review remains open.
- [ ] Rights/licence records remain PENDING. Internal second-person scientific review and manual visual/accessibility review are not yet recorded as complete. External specialist review is optional and is not a project blocker.

This checkpoint records automated CI evidence only. It is not legal clearance, independent scientific certification, physical-device testing, or final publication approval.


### Chemistry visual audit continuation — 5 November 2026

Current focused source-level review has advanced through static visual families CH-V01–CH-V06 (6 of 12 families; 50% of the static-family source-review sequence). This is a work-sequence measure only, not a verification or publication-readiness percentage.

Corrections recorded in `IMAGE_AUDIT.md`:
- CH-V01: clarified the electron probability-cloud meaning in English and removed orbit-like contour strokes; RU/EN alt text updated.
- CH-V02: checked isotope particle counts and abundance-weighted mean in both language variants; regression checks guard the six-proton / six-versus-seven-neutron structure and values.
- CH-V03: clarified that the seven dots are illustrative symbols, not a literal particle count; exact Avogadro count and not-to-scale caveat are explicit in both languages.
- CH-V04: aligned the English worked coefficient example with the Russian version: `2 × (2 H + 1 O) = 4 H atoms + 2 O atoms`.
- CH-V05: aligned the English saturated-state description with dynamic equilibrium and undissolved solute; added a distinct solid-phase symbol and explicit seeding-triggered crystallisation for the metastable supersaturated state.
- CH-V06: added the missing English Brønsted–Lowry donor/acceptor definitions and pH / base-addition graph labels; retained the pH≈7 qualification only for ideal strong-acid/strong-base titration at 25 °C.

Automated regression assertions were added for the corrected bilingual content. The current branch-head run is [42037108063](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42037108063), commit `78538a00195a966a9de3b95979c8540e476d7eb4`: static validation passed; pinned browser-tool installation is still running, so Chromium result is not yet available. Earlier failed runs corresponded to intermediate commits while the new checks were being corrected; do not treat them as the final branch-head result.

Coverage remains 12/12 static families integrated and 7/7 interactive systems integrated. Full seven-gate verification remains 0/12 static families and 0/7 interactive systems; rights/licence evidence and competent second-person scientific review remain PENDING. Manual rendered review and final approval are also open. External specialist review is not an Atlas project requirement.


### Visual audit checkpoint — 2026-11-06

- [x] Completed the source-level first pass for all 12 static bilingual visual families (CH-V01–CH-V12): 12/12 = 100% of the defined source-review sequence.
- [x] Corrected the English landing-page electron-cloud alternative text after the Chromium assertion exposed a wording mismatch.
- [x] Branch-head CI run [42039243308](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42039243308) passed on commit `06999206c3315d7060edfe3a55a68ba2c195c858`: static validation and Chromium page tests passed; 21 pages loaded at 390 CSS px, 42 axe-core scans (RU + EN), 21 language toggles and key interaction checks passed, with no uncaught page errors.
- [ ] Retained per-SVG desktop/mobile screenshot review is still open; the successful browser run did not publish screenshot artifacts.
- [ ] Complete the targeted source-level and manual state review of CH-IV01–CH-IV07, using the interactive audit register in `IMAGE_AUDIT.md`.
- [ ] Seven-gate verification and final approval remain distinct from coverage and automated CI. Do not mark assets VERIFIED based on CI alone.

Static source-review progress: **12/12 (100%)**. Static coverage: **12/12 (100%)**. Automated branch-head CI: **PASS**. Full seven-gate verification: **0/12 static and 0/7 interactive marked VERIFIED**; applicable rights, review and manual-render evidence remain open.
