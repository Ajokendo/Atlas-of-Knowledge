# Chemistry Atlas — external release acceptance checklist

This checklist separates repository automation from checks that require human reviewers and physical devices. Automated CI success is not evidence that these manual checks have been completed.

## Release status

- [x] Repository structure, local assets, scripts and internal links checked by `chemistry/checks.mjs`.
- [x] All 21 Chemistry pages exercised by Chromium smoke tests at 390, 768 and 1280 CSS px.
- [x] RU/EN language switching, selected interactive workflows and known calculation edge cases covered by browser tests.
- [x] axe-core WCAG 2.1 A/AA audit: passed in RU and EN on all 21 pages (42 scans); no serious/critical findings in the final CI run. Confirmed again in successful CI run [41326918004](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41326918004), commit `e244cb8c894eb5cb1ab1aa8a48615cd26b3d17f4`.
- [ ] Physical Android phone/tablet check.
- [ ] Physical iPhone/iPad check, including Safari where available.
- [ ] Keyboard-only review of every page and interactive tool.
- [ ] Screen-reader review: NVDA + Firefox/Chrome on desktop; TalkBack + Chrome on Android; VoiceOver + Safari on iOS.
- [ ] Browser zoom/reflow review at 200% and 400% (where applicable).
- [ ] Independent chemistry subject-matter review and sign-off.
- [ ] Final publication approval.

## Manual test protocol

### Devices and browsers
Record device model, OS version, browser/version, date, tester and result. At minimum test:
- Android phone: current Chrome; TalkBack enabled.
- iPhone: current Safari; VoiceOver enabled.
- Desktop: Chrome or Edge with NVDA, plus Firefox if available.
- Tablet: portrait and landscape orientation.

### Keyboard and assistive technology
For every page and each interactive tool:
- Navigate from the address bar using Tab and Shift+Tab only; verify logical order and a clearly visible focus indicator.
- Operate language switches, selectors, calculators, quizzes, tabs and dialogs without a pointer.
- Confirm dynamic results and quiz feedback are announced once, in a useful order, without focus being lost.
- Verify headings, landmarks, labels, instructions, error messages and image alternatives with a screen reader.
- Confirm decorative images are ignored and informative diagrams have meaningful localized alternatives.
- Confirm there are no keyboard traps and that focus returns sensibly after dismissing overlays.

### Visual and responsive checks
- Test portrait and landscape; inspect at 200% and 400% zoom.
- Check clipping, overlap, tiny text, touch target spacing and horizontal scrolling.
- Recheck text, controls, focus indicators, chart labels and SVG annotations in both Russian and English.
- Confirm browser text scaling does not hide essential content or controls.

### Scientific review
An independent reviewer should verify:
- Definitions, equations, units, significant figures and stated approximations.
- Worked examples and all calculator assumptions, input limits and outputs.
- Periodic-table values and isotope/atomic-mass explanations.
- Reaction balancing, oxidation states, acid–base and equilibrium explanations.
- Diagram labels and alt text in both languages.
Record reviewer name/qualification, date, chapters reviewed, findings, corrections and approval.

## Sign-off record

| Check | Reviewer / device | Date | Result / evidence |
|---|---|---|---|
| Android + TalkBack | Pending | — | — |
| iOS + VoiceOver | Pending | — | — |
| Desktop keyboard + NVDA | Pending | — | — |
| 200% / 400% zoom and reflow | Pending | — | — |
| Independent chemistry review | Pending | — | — |
| Release approval | Pending | — | — |

## Release gate

Do not describe the atlas as fully publication-ready until all pending items above are completed, serious/critical automated accessibility findings are resolved, and the independent scientific reviewer has signed off. Keep the repository's internal audit result distinct from external publication acceptance.


## Internal audit checkpoint — 80% (2026-11-01)

This is an internal audit milestone only; it is not external release acceptance.

- [x] Full CI rerun after recording the previous verification evidence: [README run 41327013009](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41327013009) and [checklist run 41327016326](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41327016326) both succeeded.
- [x] Reviewed targeted browser coverage for chemistry formula parsing, pH, Nernst equation, ideal-gas pressure, limiting reagent, reaction balancing and quiz workflows.
- [x] Confirmed automated coverage for bilingual page rendering/accessibility scans, responsive widths, local assets, glossary, periodic-table data and SVG descriptions.
- [ ] Remaining external device, assistive-technology and independent scientific checks are still pending and require human evidence/sign-off.


## Latest automated evidence — 2026-11-04

- [x] Latest branch-head CI run [41889220939](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41889220939), commit `73affc2476dc4f14d6f8b6bf569d8b546df57868`, completed successfully.
- [x] Static validation: 22 HTML pages, 89 local links/assets, 21 inline scripts, and 18 bilingual dictionaries.
- [x] Chromium: 21 pages loaded; 42 RU/EN axe-core scans passed without serious/critical findings; language switching and key interactive workflows passed; no uncaught page errors.
- [x] Automated horizontal-overflow checks executed at 390, 768 and 1280 CSS px.
- [ ] Manual physical-device, keyboard, screen-reader and 200%/400% zoom/reflow checks remain pending. Automated CI does not satisfy these gates.
- [ ] Independent chemistry review and final publication approval remain pending.

## Internal technical audit completion — 2026-11-05

The internal technical audit is complete for its defined scope. This does not close the external release gates above.

- [x] Expanded edge-case browser tests for periodic-table filters and empty search, completed trainer restart and progress reset, bilingual exact-stoichiometry state, and ideal-gas maximum slider values plus RU/EN preservation.
- [x] Full CI run [41894536945](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41894536945) passed on commit `51fa0dcf9f66a256900c34d793e5e3d4e34bfac6`.
- [x] Static checks: 22 HTML pages, 89 local links/assets, 21 inline scripts, 18 bilingual dictionaries.
- [x] Chromium checks: all 21 pages; 42 RU/EN axe-core scans; 21 language toggles; key interaction workflows; no uncaught page errors; responsive overflow checks at 390, 768 and 1280 CSS px.
- [ ] External gates remain pending: physical Android/iOS, manual keyboard and 200%/400% zoom/reflow, NVDA/TalkBack/VoiceOver, independent chemistry review, and final publication approval.

Do not interpret internal technical audit completion as external release acceptance.


## Branch-head validation status — 2026-11-05

**Automated CI: PASS.** Current Chemistry branch head at commit `96d4f3a035be77ced650b9c0520d1e3c4ebb27d2` passed GitHub Actions run [41912166802](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41911003011).

- [x] Static Chemistry checks: 22 HTML pages, 90 local links/assets, 21 inline scripts and 18 bilingual pages checked.
- [x] Chromium browser smoke: all 21 configured pages loaded; 42 axe-core WCAG 2.1 A/AA scans (RU + EN); 21 language toggles and key interactive workflows; no uncaught page errors.
- [x] Responsive overflow checks at 390, 768 and 1280 CSS px; keyboard focus, accessible control names, image alt attributes, image decoding and other scripted browser checks passed.
- [ ] Manual Android/iOS, keyboard-only, NVDA/TalkBack/VoiceOver and 200%/400% zoom/reflow checks remain PENDING.
- [ ] Independent chemistry review and final publication approval remain PENDING.
- [ ] Visual rights/provenance verification remains PENDING for all 18 integrated visual records; Image Verification is still 0/18.
- [ ] Chapter 03 periodic-trends candidate still requires local SVG integration and side-by-side scientific/language/accessibility review.

CI PASS is evidence of automated structural and browser checks only. It does not certify legal rights, creator attribution, scientific correctness, translation quality, independent review or manual assistive-technology behaviour.

## Visual inventory update — 2026-11-05

The former statement that the Chapter 03 periodic-trends visual still needed integration is superseded. The current Chemistry visual inventory is:

- [x] 24 static SVG files (12 bilingual pairs) are present in `chemistry/assets/`.
- [x] All 12 planned static visual topics are integrated, including the new Chapter 03 periodic-trends pair (`periodic-trends.svg` / `periodic-trends-ru.svg`).
- [x] Seven interactive visual systems are present in the subject atlas.
- [x] SVG dependency scan: no external `href` / `xlink:href` image dependencies found in the 24 SVG files.
- [x] Chapter 03 periodic-trends visual passes the automated branch-head CI run [41967264963](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41967264963), commit `4fd30ec4133a3cbef848478daa889d3d8cd1f42e`.
- [ ] Creator, source lineage and rights remain Unknown/PENDING for 12 SVG files; Git introduction commits are documented but do not establish authorship or licensing.
- [ ] The remaining seven interactive systems have local implementations and no identified external visualization-library imports, but creator/rightsholder and licence evidence remains PENDING.
- [ ] Independent chemistry educator review, physical-device tests, manual keyboard/screen-reader checks and 200%/400% zoom/reflow remain external release gates.

**Interpretation:** Image Coverage is 12/12 (100%) and all 19 planned visual units are integrated. Image Verification is not complete. Do not describe the atlas as legally cleared, independently scientifically approved or fully publication-ready until the outstanding gates have evidence and sign-off.
