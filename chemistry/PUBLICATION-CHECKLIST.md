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
