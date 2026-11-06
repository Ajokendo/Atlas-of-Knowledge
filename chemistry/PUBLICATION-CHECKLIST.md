# Chemistry Atlas — internal publication checklist

**Current project decision (6 November 2026):** the Chemistry Atlas is being prepared for publication using internal editorial, scientific-source, bilingual, visual, accessibility and technical checks. Documentary confirmation of rights/licensing authority and independent scientific review by another competent person are separate follow-up activities; neither is a prerequisite that blocks this project's publication milestone. This decision does not claim that the Atlas is legally cleared or independently certified. We must still identify sources, preserve attribution, respect known licence restrictions, and replace or obtain permission for any material known to be impermissible to publish.

## Publication-readiness checks

- [x] Chemistry pages, local links, assets and scripts pass `chemistry/checks.mjs`.
- [x] All 21 configured Chemistry pages load in Chromium.
- [x] RU/EN language switching and key interactive workflows pass.
- [x] 42 axe-core WCAG 2.1 A/AA scans (RU + EN across 21 pages) pass without serious/critical findings.
- [x] Automated responsive overflow checks at 390, 768 and 1280 CSS px pass.
- [x] No uncaught browser page errors in the recorded branch-head run.
- [x] All 12 bilingual static visual topics (24 SVG files) are integrated.
- [x] Retrospective production-lineage reconstruction is recorded for all 12 bilingual static visual families (24 SVG files), preserving filenames and page references. Category C is a production-lineage classification only; it does not establish a named human author, legal rightsholder, licensing authority or approved licence.
- [x] Localized title/description metadata is present in replacement SVGs.
- [x] All seven interactive visual systems were inspected; no third-party visualization-library imports or external image-asset references were identified.
- [x] Replacement commits, source references and known provenance limitations are documented in `IMAGE_SOURCES.md` and `IMAGE_AUDIT.md`.
- [x] Expanded visual capture to all 21 Chemistry pages (the three previously omitted pages were chemistry constants, glossary and knowledge check).
- [x] Captured and scanned 126 screenshots: 21 pages × RU/EN × 390/768/1280 px. Contact-sheet review found no obvious page-level clipping or overlap.
- [x] Scanned all six RU/EN × 390/768/1280 px contact sheets from the latest 126-image artifact; no new page-level clipping, overlap or missing-page issue was identified. This remains a contact-sheet pass, not a full-size review of every image.
- [x] Expanded the knowledge-check regression: incomplete submission is blocked; 15/15 and 0/15 outcomes, feedback, explanation visibility, answer locking, reset behaviour, RU/EN result translation and single-entry history persistence are checked in Chromium.
- [x] Performed focused full-size checks of acid–base, chemical reactions, periodic table, molecular laboratory, stoichiometry, chemistry constants, glossary and knowledge check. The periodic-table horizontal scroll is intentional and explained.
- [ ] Complete the remaining detailed page-by-page full-size review and manual review of interactive states.
- [ ] Resolve any remaining content, bilingual-parity, visual, usability or accessibility defects found during that review.
- [ ] Record the final internal editorial decision after the remaining in-scope checks and final regression run.

## Automated evidence

**Latest recorded branch-head GitHub Actions run:** [42210374860](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42210374860)  
**Branch:** `workspace/chemistry`  
**Commit:** `e59dcc73bebc978ff7dbc731162b902ec3bc24ca`  
**Result:** SUCCESS

The run captured artifact [13497179956](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/42210374860/artifacts/13497179956), containing 126 rendered screenshots (21 pages × RU/EN × 390/768/1280 px).

Automated results establish only the checks actually run. They do not establish identical behaviour on every physical device or assistive technology.

## Visual inventory

| Area | Result | Qualification |
|---|---:|---|
| Static visual coverage | 12/12 topics — 100% | All planned bilingual topics are integrated |
| Replacement of previously unresolved static SVGs | 12/12 | New project-specific SVG sources and commits are documented |
| Earlier SVGs with AI-generation evidence | 10 files | Evidence is recorded individually; not blanket legal clearance |
| Interactive visual systems | 7/7 inspected | Local implementations; historical author attribution remains incompletely documented |
| Automated branch-head CI | PASS | Run 42210374860 |
| Rendered screenshot coverage | 21/21 pages — 100% | 126 images across both languages and three viewport widths |

## Separate follow-up activities — not publication blockers

These activities are tracked separately from the current publication-readiness work:

- **Rights and licensing documentation:** further identify rightsholders/licensing authorities and collect documentary confirmation where possible. Existing source/attribution records and known restrictions remain visible; do not describe the Atlas as legally cleared or imply that missing documentation has been obtained.
- **Independent scientific review:** arrange a review by another competent person, distinct from the creator, and record findings. This is a separate expert-assurance activity, not a condition for completing this project's publication milestone.

The fact that these activities are deferred does not authorise knowingly impermissible use. If a specific asset is found to be restricted or clearly unsuitable for publication, replace it or obtain the necessary permission before release.

## Optional technical enhancements

The following are not prerequisites for the current internal publication milestone unless a concrete defect is discovered:
- manual NVDA, TalkBack or VoiceOver testing;
- physical Android/iOS device checks;
- expanded manual 200%/400% zoom and reflow checks.

Any discovered defect that materially prevents access or correct use remains an in-scope issue regardless of the testing method.

## Current completion decision

**Automated technical checks and documented static-visual production-lineage remediation are complete for the recorded inventory. The remaining in-scope work is the manual review of uncovered page-specific visuals and interactive states, correction of any findings, and a final internal editorial decision.**

Do not describe documentary rights confirmation or independent second-person scientific review as mandatory publication gates. Track them as separate follow-up activities. Do not claim legal clearance or independent scientific certification unless those activities are actually completed and documented.
