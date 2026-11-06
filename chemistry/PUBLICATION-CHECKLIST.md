# Chemistry Atlas — internal publication checklist

**Current decision (2026-11-06):** this is a community-built, no-budget project. External specialist scientific review, external legal opinion, physical-device labs and dedicated screen-reader testers are not available; those additional services are out of scope and are not universal prerequisites for internal verification. This does **not** waive the mandatory internal gates in the root `AUTHOR_CREATED_VISUALS_STANDARD.md` and `IMAGE_FIRST_POLICY.md`: actual rights/licensing authority and an explicit licence or permission must be evidenced, and scientific review must be documented by a competent second reviewer distinct from the creator. This checklist records technical remediation separately from permission to publicly release the visuals.

## Internal release checks

- [x] Chemistry pages, local links, assets and scripts pass `chemistry/checks.mjs`.
- [x] All 21 configured Chemistry pages load in Chromium.
- [x] RU/EN language switching and key interactive workflows pass.
- [x] 42 axe-core WCAG 2.1 A/AA scans (RU + EN across 21 pages) pass without serious/critical findings.
- [x] Automated responsive overflow checks at 390, 768 and 1280 CSS px pass.
- [x] No uncaught browser page errors in the final branch-head run.
- [x] All 12 bilingual static visual topics (24 SVG files) are integrated.
- [x] Completed the documented retrospective provenance reconstruction for all 12 bilingual static visual families (24 SVG files), preserving filenames and page references. All families are classified Category C for production-lineage tracking; this does not establish a named human author, legal rightsholder, licensing authority or approved licence. Rights remain PENDING.
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

## Disclosed resource limitations

These limitations are reported transparently and do not, by themselves, prevent an internal review:

- No external legal opinion or independent specialist chemistry review is claimed. External counsel and external subject-matter review are not universal prerequisites under the project standard; a competent internal second reviewer may satisfy the scientific-review gate.
- The seven interactive systems are self-contained local HTML/SVG/CSS/JavaScript/Canvas implementations. Their repository history and lack of third-party visualization dependencies are documented, but this does not establish the original author, rightsholder or authority to license the code.
- AI-generation evidence for ten earlier SVG files does not by itself establish a comprehensive rights basis or exclusive ownership.
- Automated axe-core scans do not replace manual NVDA, TalkBack or VoiceOver testing.
- No physical Android/iOS device certification or external 200%/400% zoom/reflow certification is claimed.
- Do not describe the atlas as legally cleared or independently scientifically certified.

## Optional accessibility and specialist enhancements

These may be completed if resources become available; they are not substitutes for the mandatory rights/licence and competent internal second-review gates:
- external chemistry educator review;
- manual keyboard and screen-reader testing (NVDA, TalkBack, VoiceOver);
- physical Android/iOS device checks;
- manual 200%/400% zoom and reflow review.

Rights-holder research, confirmation of licensing authority and the explicit licence/permission decision are **mandatory open gates**, not optional future improvements.

## Internal completion decision

**The automated technical checks and the documented static-visual provenance remediation are complete for the current inventory. This is not a complete visual verification or public-release approval.**

The following mandatory gates remain open under the root policy and must not be described as optional:

- **Rights and licence:** all 12 static visual families and all 7 interactive systems still have unresolved rightsholder/licensing-authority and/or explicit project-licence evidence. Keep the rights result `PENDING`; do not publicly release these assets or mark them `VERIFIED` until the authority and exact licence/permission are documented for every covered file/system.
- **Scientific/factual review:** the first-pass source audit is recorded, but the required competent second reviewer distinct from the creator has not yet been documented for every visual family/system. External specialist review is optional; a qualified internal reviewer is sufficient.
- **Per-asset visual/accessibility evidence and final approval:** automated scans and selected rendered screenshots do not replace the remaining manual checks and a recorded final approval under the seven-gate standard.

The absence of external counsel, external subject-matter experts, physical-device labs or dedicated screen-reader testers is disclosed and non-blocking as a resource limitation. It must not be confused with the unresolved documentary rights gate or the mandatory internal second-review gate. Do not claim legal clearance, `VERIFIED` status, or publication readiness while those gates remain pending.


## Latest branch-head evidence — 6 November 2026

- [x] Branch-head CI run [42197379151](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42197379151) completed successfully on commit `3f0b4a45da54b41ea9f55670f5f092809ed54f54`.
- [x] Repository validation, pinned browser-audit tool installation, local server startup, Chromium tests for all configured Chemistry pages, and rendered screenshot upload all succeeded.
- [x] The `chemistry-rendered-review` artifact [13492128627](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42197379151/artifacts/13492128627) was uploaded successfully.
- [ ] This CI run does not close rights/licence evidence, competent second-person review, complete per-asset/manual state review, or final approval.
