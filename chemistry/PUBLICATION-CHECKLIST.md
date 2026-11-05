# Chemistry Atlas — internal publication checklist

**Current decision (2026-11-05):** this is a community-built, no-budget project. External scientific/legal reviewers, physical-device labs and dedicated screen-reader testers are not available. Their absence is explicitly **out of scope and non-blocking**. This checklist records the feasible internal release checks; it does not claim legal clearance or independent certification.

## Internal release checks

- [x] Chemistry pages, local links, assets and scripts pass `chemistry/checks.mjs`.
- [x] All 21 configured Chemistry pages load in Chromium.
- [x] RU/EN language switching and key interactive workflows pass.
- [x] 42 axe-core WCAG 2.1 A/AA scans (RU + EN across 21 pages) pass without serious/critical findings.
- [x] Automated responsive overflow checks at 390, 768 and 1280 CSS px pass.
- [x] No uncaught browser page errors in the final branch-head run.
- [x] All 12 bilingual static visual topics (24 SVG files) are integrated.
- [x] Replaced all 12 static SVG files whose creator/source provenance could not be established; preserved filenames and page references.
- [x] Localized title/description metadata is present in replacement SVGs.
- [x] Inspected all seven interactive visual systems; no third-party visualization-library imports or external image-asset references were identified.
- [x] Documented replacement commits, remaining provenance limitations and the interactive-system disposition in `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md`.
- [x] Recorded the project's scope decision: independent external review and manual assistive-technology/device testing are not release blockers.

## Final automated evidence

**GitHub Actions:** [run 41968413926](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41968413926)  
**Branch:** `workspace/chemistry`  
**Commit:** `113985acda1b23e2fc27b4ca446a8eede881ba9f`  
**Result:** SUCCESS

The completed browser job reports:
- 21 pages loaded at 390 px;
- 42 axe-core scans (Russian and English);
- 21 language toggles;
- key interactive workflows checked;
- no uncaught page errors.

Automated results are evidence of the checks listed above only. They do not establish that every assistive technology or physical device behaves identically.

## Visual status

| Area | Result | Qualification |
|---|---:|---|
| Static visual coverage | 12/12 topics — 100% | All planned bilingual topics are integrated |
| Previously unresolved static SVGs | 12/12 replaced | New project-specific SVG source and commits documented |
| Earlier SVGs with AI-generation evidence | 10 files | Evidence is recorded individually; not blanket legal clearance |
| Interactive visual systems | 7/7 inspected | Local code implementations; historical author attribution remains undocumented |
| Automated branch-head CI | PASS | Run 41968413926 |

## Disclosed limitations (not blockers for this project's internal release)

- The seven interactive systems are retained as self-contained local HTML/SVG/CSS/JavaScript/Canvas code. Their repository introduction history and absence of third-party visualization dependencies are documented, but original human/AI authoring attribution and a separate legal opinion are not established.
- Earlier AI-generation evidence for ten SVG files does not by itself establish a comprehensive rights basis or exclusive ownership.
- Internal scientific review is not independent expert certification.
- Automated axe-core scans do not replace manual NVDA, TalkBack or VoiceOver testing.
- No physical Android/iOS device certification or external 200%/400% zoom/reflow certification is claimed.
- Do not describe the atlas as legally cleared or independently scientifically certified.

## Optional future improvements

These may be completed if resources become available, but they do not block the internal audit:
- independent chemistry educator review;
- manual keyboard and screen-reader testing (NVDA, TalkBack, VoiceOver);
- physical Android/iOS device checks;
- manual 200%/400% zoom and reflow review;
- additional rights-holder research for older project assets and interactive-code history.

## Internal completion decision

**The feasible internal technical and static-visual provenance remediation scope is complete.** The remaining items above are explicitly optional external-resource checks or disclosed historical attribution limitations, not unfinished tasks silently presented as passed.
