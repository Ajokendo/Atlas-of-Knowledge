# Full repeat audit — Atlas of Biology

**Audit start:** 1 November 2026  
**Canonical branch:** `workspace/biology`  
**Scope:** all Biology HTML pages, scientific/editorial content, interactive tools, technical checks, vector and raster visuals, image placeholders, bilingual parity, links and release controls.  
**Audit completion:** **5%** — repository inventory and baseline structure pass completed.  
**Controlled editorial readiness:** **95/100** (separate metric; unchanged).

## Audit method and boundaries

The audit is conducted in the Biology working area only. It does not modify other Atlas disciplines, the portal, publication settings or historical branches. Confirmed defects may be corrected in place after the current blob SHA is fetched; every saved change must be read back and verified. Ambiguous scientific claims are recorded for qualified review rather than silently rewritten.

The audit separates:
1. Editorial quality and bilingual equivalence.
2. Scientific accuracy, source traceability, taxonomy and evidence scope.
3. Technical structure, local links, scripts, controls and regression checks.
4. Visual quality, SVG accessibility, image briefs, raster provenance and insertion-marker integrity.
5. Cross-page navigation, responsive behaviour and release readiness.

## 5% milestone — repository inventory

### Pages inventoried

- Landing page: `index.html`.
- Ten core chapters: Botany, Zoology, Cell Biology, Anatomy and Physiology, Genetics, Microbiology, Ecology, Evolutionary Biology, Biochemistry, Systematics.
- Two regional chapters: Flora of Kyrgyzstan and Fauna of Kyrgyzstan.
- Total: **13 HTML pages**.

### Baseline source scan

A source-level scan of all 13 pages found:
- Russian and English content markers are present in balanced counts on every page.
- No duplicate HTML `id` values were found in the scanned pages.
- Inline SVG illustrations are present across the course; the scan counted 22 SVG elements in total.
- No raster `<img>` elements are currently integrated in the 13 pages, consistent with the existing deferral decision.
- All 52 planned `image-brief-*` anchors remain represented in the production map and page content according to the existing committed regression assertions. Actual end-to-end execution of the Node/Chromium suites has not yet been performed in this audit.
- The regional chapters contain substantially larger source/reference footprints than the core teaching chapters; a bibliography entry alone is not treated as proof for every nearby species claim.

### Existing controls and gates confirmed

- The image insertion map contains 52 planned assets; the disposition register records all 52 as Deferred.
- No raster image is approved, committed or integrated under `biology/images/generated/`.
- G4 independent scientific review and G5 independent bilingual/editorial release review remain open.
- The existing 95/100 controlled editorial-readiness score is not changed by this inventory milestone.

## Initial audit observations

1. **Source traceability remains a known substantive gap.** The regional species audit explicitly notes that a chapter-wide bibliography does not prove every adjacent species statement. High-priority claims need claim-level source linkage.
2. **Independent review is still required.** The existing external-review packet is prepared but has no completed sign-off.
3. **Visual publication is deliberately incomplete.** SVG learning diagrams exist, but all 52 planned raster assets remain deferred. This is a recorded release choice, not a hidden completed state.
4. **Automated checks are extensive but not yet freshly executed against the current branch head.** The committed `checks.mjs` covers document metadata, duplicate IDs, bilingual marker and numeric parity, scientific-name parity, local paths/fragments, inline JavaScript syntax, SVG naming, button types, reference sections and specialised regional evidence assertions. Actual runtime/browser behaviour still needs a fresh run.
5. **A source-level pass cannot certify visual appearance or keyboard/mobile behaviour.** These require browser rendering and manual interaction checks in addition to static assertions, consistent with WCAG 2.2's testable accessibility requirements.

## Next audit block

Proceed to the technical baseline: inspect the complete regression script and workflow configuration, run the available checks against this exact branch head, classify failures, then correct confirmed issues and record the results. In parallel, begin claim-to-source sampling in the two regional chapters.

## Change log

- 1 November 2026: audit initiated; 13-page inventory and source-level baseline completed. No chapter content, tool logic, visual asset or image marker modified in this milestone.


## 10% milestone — technical and accessibility source review

### Completed checks

A second source-level pass was completed across all 13 HTML pages. It sampled heading hierarchy, interactive controls, SVG naming, input labels, external new-tab links and the structure of the committed regression suite.

- All 13 pages have one `h1`; each page has a populated `h2` structure.
- The sampled pages contain no `input` elements requiring an associated label.
- All 22 inline SVGs exposed an accessible name through `aria-label` / `aria-labelledby` or the required SVG image role; no SVG in the sampled source lacked a title/name.
- No external link using `target="_blank"` was found without `rel="noopener"`.
- Interactive pages use native `button` elements with explicit `type="button"`; the language-switch button's visible text (EN/RU) supplies its name. A first-pass regex flagged this control as potentially unnamed, but manual inspection confirmed it is visibly named; this was classified as a false positive, not a defect.
- The existing regression script includes checks for duplicate IDs, RU/EN block counts, numeric-token parity, scientific-name parity, local paths and fragments, inline JavaScript syntax, SVG accessible names, button types and the 52 image-anchor map.
- The existing bilingual parity report records 1,147 Russian and 1,147 English blocks, with no numeric-token or scientific-name-set differences in its measured scope. This remains an author-side structural parity check, not professional translation approval.

### Accessibility standard applied

The source review uses WCAG 2.2 as a reference, particularly text alternatives for non-text content, keyboard operation, focus visibility, language identification, contrast and minimum target size. Static source inspection cannot establish contrast ratios, responsive reflow, real keyboard behaviour or assistive-technology output; those remain browser/manual test items.

### Findings / limitations

1. No confirmed source-level defect requiring a code edit was found in this technical/accessibility sample. Therefore no speculative HTML or JS change was made.
2. The 81 KB `checks.mjs` suite was inspected but not executed: the repository checkout/runtime and its installed Node/Chromium dependencies are not available through the current GitHub file-reading connection. No claim of a passing test run is made.
3. Workflow configuration and latest CI run still require direct retrieval/verification; they are not inferred from the presence of a test script.
4. Browser-based mobile/desktop rendering, keyboard-only interaction, contrast measurement, reduced-motion behaviour and screen-reader checks remain open.

### Next block

Continue technical review by examining each interactive model's state transitions, calculations, boundary cases and language-switch behaviour; then perform targeted scientific claim-to-source review in the two Kyrgyzstan regional chapters.

### Change log

- 1 November 2026: completed source-level technical/accessibility review of all 13 pages and inspected the committed regression script. No code change made because no confirmed defect was established. Audit completion advanced to 10%; controlled editorial readiness remains 95/100.
