

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
