# Biology branch audit — 1 November 2026

Repository: `Ajokendo/Atlas-of-Knowledge`  
Canonical Biology workspace: `workspace/biology`  
Discipline path: `biology/`  
Audit base: `workspace/biology` HEAD `96729b39f459245009a52adaa35465e9f3fc41dd`  
Main at audit: `67dc12b7d5793e1d73c5f58047027c6a707fef07`

## Branch inventory

The repository branch search returned five Biology-named branches:

| Branch | Comparison against main | Audit classification |
|---|---:|---|
| `workspace/biology` | 408 ahead, 0 behind | Canonical active workspace; retain as the sole Biology development branch |
| `biology-atlas` | 225 ahead, 300 behind | Historical source branch; substantially diverged and overlaps the existing Biology tree |
| `biology-deep-editorial-pass-1` | 13 ahead, 9 behind | Candidate source of editorial deltas in 12 chapter files; requires selective review |
| `biology-learning-experience-pass` | 1 ahead, 10 behind | Candidate source of a small learning-experience delta in README, 12 chapters and landing page |
| `biology-release-integration` | 29 ahead, 36 behind | Historical release staging branch; not a second active workspace |

The branch comparisons show that these are whole-repository snapshots, not isolated Biology repositories. The canonical workspace is 408 commits ahead of main and contains work outside Biology as well. Its Biology path includes the expanded chapter set, quality-assurance scripts, regional biodiversity dossiers, image briefs and review registers.

## Merge decision

Do not perform a blind branch merge or delete any source branch.

The project registry requires discipline changes to remain within the assigned folder and says branch consolidation is coordinated through `atlas-of-knowledge-integration`; assistants must not independently merge source branches. This is especially important because `biology-atlas` is 225 commits ahead and 300 behind main, while the two small pass branches diverged from older common ancestors and touch the same chapter files that have since evolved in the canonical workspace.

Recommended consolidation:
1. Keep `workspace/biology` as the single active Biology workspace.
2. Review the 13-commit editorial pass and the one-commit learning-experience pass as targeted diffs against the current workspace; selectively port only changes that are demonstrably absent and still scientifically/editorially valid.
3. Treat `biology-atlas` and `biology-release-integration` as historical checkpoints, not merge targets.
4. Preserve all historical branches until the coordinator confirms the canonical integration and retention plan.

## Image and validation checkpoint

The current workspace contains `IMAGE_DISPOSITION_REGISTER.md`, which records 52 illustration placements as deferred, with the in-page anchors retained and no unverified or unlicensed image assets claimed as generated. Continue preserving those exact placeholders and their target filenames until approved assets can be integrated.

## Audit conclusion

Five Biology-related branches exist. There is one designated active workspace and four historical/source/staging branches. No destructive merge or branch deletion was made during this audit. Selective consolidation of the two small pass branches remains the next coordinator-reviewed task; the old `biology-atlas` branch should not be merged wholesale.


## Follow-up review — 1 November 2026

The mandatory registry and editorial standard were re-read from `atlas-of-knowledge-integration` before continuing. The standard requires clear first-use definitions, staged explanations, scientific accuracy, RU/EN parity, accessible interaction, mobile checks and a documented final review. The registry confirms that `workspace/biology` is the assigned branch, work must stay inside `biology/`, and assistants must not merge branches independently or delete historical source branches.

The current canonical workspace HEAD is `fe2cc66833ff8923128ad88893fa16586e35224c` (the audit-record commit).

### Targeted review of the two small pass branches

- `biology-learning-experience-pass`: its single unique commit is `b1e388bb71f8408fdf9b535d26c760702c96635f` (“Enrich Biology atlas for an engaging learner experience”). It adds learner objectives/glossaries and learner-facing introductions in a set of Biology pages. The canonical workspace already contains the corresponding bilingual “wonder” introductions and learning blocks, while its chapter files are substantially more developed than the pass-branch snapshots (for example, anatomy and biochemistry). The pass branch is 419 commits behind the workspace. **Decision: do not port or merge this branch as-is; the educational concepts are already represented in the canonical workspace, and its older page snapshots would risk replacing richer content.** A future content-only comparison may still identify a small wording improvement, but no such missing improvement has yet been demonstrated.
- `biology-deep-editorial-pass-1`: the branch is 418 commits behind the workspace and has 13 commits ahead, touching 12 chapter files. The inspected tip commit `83b476acf0f1a67da515c8138fc89c5389aaa97b` clarifies habitat connectivity, wildlife explanations and taxonomy/context in the Kyrgyzstan chapters. These are relevant editorial themes, but the branch's broad chapter snapshots are not safe merge candidates. The current workspace already contains expanded Kyrgyzstan flora/fauna dossiers and explicit caveats about evidence, taxonomic uncertainty and dated Red Data Book figures. **Decision: no wholesale merge; continue commit-by-commit review and only transfer a demonstrably absent, fact-checked sentence or correction.** The remaining 12 commits have not yet been individually certified as redundant or fully reviewed.

### Historical branches

- `biology-atlas` is 225 commits ahead and 709 behind `workspace/biology` in the direct comparison. Its diff also includes Chemistry and portal files, so it is a repository-wide historical snapshot, not a clean Biology-only source.
- `biology-release-integration` is 29 commits ahead and 445 behind `workspace/biology`; its diff includes the old Biology release tree and shared portal content. Treat it as a historical checkpoint only.

### Current decision and remaining work

There is one canonical Biology development branch: `workspace/biology`. The learning-experience branch is not a useful merge candidate because its educational elements are already present in a more developed form. The editorial-pass branch remains under selective review; no unique, missing change has yet been approved for transfer. The old atlas and release branches must remain untouched as historical sources. No branch was merged, rewritten or deleted.

The 52 deferred illustration placements remain governed by `biology/IMAGE_DISPOSITION_REGISTER.md`; preserve the existing anchors and filenames. Before any later release handoff, complete the remaining editorial-pass commit review, verify the current QA scripts, and record actual test results. This audit is a branch-consolidation review, not a claim that the entire Biology Atlas has passed its final scientific/editorial audit.


## Biology quality pass — Biochemistry language controls — 1 November 2026

A source-level review of `chapters/biochemistry.html` found a real RU/EN usability defect: all 11 controls across the enzyme, enzyme-factor, ATP and cellular-respiration models displayed Russian-only labels even when the page language was English. Their explanatory output was localized, but the control labels were not.

Corrected all 11 controls with paired `.ru` and `.en` labels (the pH abbreviation is intentionally identical in both languages). Added regression coverage:
- `checks.mjs` now requires bilingual labels in all four Biochemistry control groups.
- `browser-smoke.mjs` now checks that English labels are visible and Russian labels are hidden after switching the Biochemistry page to English.
- `BILINGUAL_PARITY_AUDIT.md` now records the additional 11 RU/EN pairs: Biochemistry 55/55; total 1,147/1,147 paired blocks.

Commits:
- `57bda10a4529ec305d718e15c539b45aeda5dbc9` — localized the main Biochemistry controls.
- `801dc4445144dda4b114a09a2887e31559b7b5ef` — paired the pH label explicitly.
- `49a21532ea945f243ef429f822122ae4409030e7` — added static regression checks.
- `9f3ca32a52d918155162eedc65d2c60fe8708134` — added browser smoke coverage.
- `9cf723bd6ac2077d8dc3ea3a9db074587dac2767` — updated the parity audit.

Static source inspection confirms 58 RU and 58 EN markers on the Biochemistry page, and every one of the 11 model controls now has both language labels. The checks and browser test have been updated but were not executed in this session; do not report them as passing until a GitHub Actions run or local execution confirms the result.


## Follow-up QA checkpoint — biochemistry controls and image planning — 1 November 2026

A source-level inspection found that the targeted biochemistry control-label check used an over-escaped regular expression for HTML button tags. The pattern could not reliably match the actual `<button>` elements, so the previous check did not provide the intended coverage.

Corrected `biology/checks.mjs` and strengthened the assertion to require the expected control count in each interactive group:

| Control group | Expected | Source-level result |
|---|---:|---|
| `enzyme-controls` | 3 | 3 found; RU/EN labels present |
| `factor-controls` | 3 | 3 found; RU/EN labels present |
| `atp-controls` | 2 | 2 found; RU/EN labels present |
| `respiration-controls` | 3 | 3 found; RU/EN labels present |
| **Total** | **11** | **11 found and bilingual** |

The corrected pattern was checked against the current chapter source in the connector runtime. This is a focused source-level verification, **not** a claim that the full Node.js test suite or Playwright browser suite was executed.

Image-planning integrity was also rechecked against the current repository files:
- `IMAGE_INSERTION_MAP.md`: 52 rows, 52 unique anchors.
- `IMAGE_DISPOSITION_REGISTER.md`: 52 deferred rows, 52 unique anchors.
- Priority split: 13 P1 and 39 P2/P3.
- `IMAGE_BRIEF_REVIEW.md`: 39 individually reviewed P2/P3 briefs.
- `IMAGE_GENERATION_PLAN.md`: 52 planned entries (13 P1, 26 P2, 13 P3).
- `IMAGE_SCIENTIFIC_REVIEW.md` retains its approval checklist for the P1 assets.

No illustration asset was generated or marked complete. All 52 page anchors, target filenames, priorities and future-artwork descriptions remain deferred pending actual asset creation, provenance/licence review and scientific/editorial approval.

No other discipline folder or historical branch was changed. No merge or branch deletion was performed.

Code checkpoint: `10c8765bc7ab9ee1afcebb84b67d9790b8f198dc`.


## Ecology interactive controls QA checkpoint — 1 November 2026

A chapter-level review found that the carbon-cycle and ecosystem-pressure controls in `chapters/ecology.html` were Russian-only, unlike the surrounding bilingual chapter. These controls also lacked explicit initial `aria-pressed` states even though the interaction code reads and updates that state.

Corrected the five carbon-cycle controls and four ecosystem-pressure controls:
- Carbon cycle: Photosynthesis, Cellular respiration, Decomposition, Combustion, Ocean exchange.
- Ecosystem pressures: Drought, Pollution, Invasive species, Conservation.
- Each control now has paired Russian/English labels and an explicit initial pressed state; exactly one control per group is initially selected.
- The existing update handler continues to switch the explanatory output according to the selected page language.

Added regression coverage in `checks.mjs` for exact group counts, bilingual labels and initial pressed-state consistency. Added Playwright smoke assertions in `browser-smoke.mjs` for language visibility, accessible pressed states, selection changes and the English cellular-respiration output.

Focused source-level verification against the current repository files:
- Carbon controls: 5/5, bilingual, 5 pressed-state attributes, one initial selection.
- Pressure controls: 4/4, bilingual, 4 pressed-state attributes, one initial selection.
- Static assertion logic matches the actual chapter markup.
- Browser smoke coverage is present in source.

**Execution limitation:** the connector returned no workflow runs for this commit. The Playwright and Node.js suites have not been executed in a local runtime; this checkpoint is not a CI pass.

Illustration planning remains unchanged and intact:
- `IMAGE_INSERTION_MAP.md`: 52 rows.
- `IMAGE_DISPOSITION_REGISTER.md`: 52 deferred rows.
- Ecology image anchors `image-brief-ecology-cycles` and `image-brief-ecology-mountain` remain in the chapter with bilingual descriptions and planned target assets. No image was generated or marked complete.

Code checkpoints:
- Ecology chapter: `dd54adaffed4f03289ad3e1d351d38373e9ee045`.
- Static checks: `c8dce8ff328b7515f488fc4854eb36bec97f92df`.
- Browser smoke: `da05d8e111da2a024806eea0c34a54a1610f860e`.


## Population ecology content-development checkpoint — 1 November 2026

Expanded `chapters/ecology.html` with a new bilingual learning section, **“How population size changes / Как меняется численность популяции”**. This is substantive chapter development, not branch-only auditing.

The new section explains:
- the four demographic processes that change population size: births, deaths, immigration and emigration;
- idealised exponential growth (`dN/dt = rN`) and logistic growth (`dN/dt = rN(1 − N/K)`);
- environmental carrying capacity and why it is not a fixed universal constant;
- density-dependent and density-independent limiting factors;
- why model curves are explanatory simplifications and not automatic forecasts for real populations.

Added an accessible SVG comparison of J-shaped exponential and S-shaped logistic curves, with a labelled carrying-capacity line and bilingual visible labels. The section uses the chapter's existing RU/EN language-switch convention and responsive learning-block layout.

Focused source verification after the commit confirmed:
- section anchor `population-dynamics` exists;
- both growth-model equations and both limiting-factor categories are present;
- bilingual label spans are present;
- the SVG has an accessible title/description association.

**Execution limitation:** this was source-level inspection only. No browser, Node.js, or full project test suite was executed in this checkpoint. The chart and explanatory copy still warrant a visual/browser review.

Image-planning registers were not changed; the existing 52 planned/deferred image placements remain untouched. No image asset was generated or marked complete.

Code commit: `108b94c5394f06f6f1a5d36b7f78ad3c2b4fd462`.

Progress reporting note: overall Atlas completion remains a provisional project estimate until a chapter-by-chapter rubric is recalculated. This content checkpoint is complete at source level; visual and automated test verification remain open.



## Branch consolidation recheck — 1 November 2026

Rechecked the repository branch inventory and pull-request history against the current canonical workspace.

### Current branch inventory

| Branch | Current relationship to `workspace/biology` | Decision |
|---|---|---|
| `workspace/biology` | Canonical active Biology workspace | **Retain** |
| `biology-learning-experience-pass` | 1 branch-only commit; its PR #4 is closed and merged to `main`; workspace is substantially ahead | Historical source; do not merge or delete until its unique commit is explicitly reconciled |
| `biology-deep-editorial-pass-1` | 13 branch-only commits; PR #5 is closed and merged to `main`; workspace is substantially ahead | Historical editorial source; do not merge wholesale or delete before commit-level reconciliation |
| `biology-release-integration` | 29 branch-only commits; PR #3 is closed and merged to `main`; includes release/portal/shared files | Historical release staging; retain pending repository-owner cleanup |
| `biology-atlas` | 225 branch-only commits; broad mixed-discipline snapshot, not Biology-only | Historical source snapshot; retain pending owner cleanup |

Pull-request history confirms that PR #3 (release integration), PR #4 (learning experience) and PR #5 (editorial pass) were merged into `main` on 31 October 2026. The current `workspace/biology` has since advanced independently and contains the latest audit, chapter and QA work. Branch comparisons are diverged because these refs preserve earlier histories; a branch's ahead count is not by itself proof that its content is missing from the canonical workspace.

### Cleanup decision

- There is exactly one active Biology development branch: `workspace/biology`.
- The four other Biology-named branches are historical/source/staging branches, not parallel active workspaces.
- No branch was deleted or force-moved. The available GitHub connection in this session exposes branch listing/comparison and branch creation/update, but no branch-delete operation. The read-only fetch endpoint cannot delete refs.
- It would be unsafe to simulate deletion by force-moving old branch refs to the current workspace SHA: that would rewrite historical references and could discard unreviewed branch-only commits.
- Therefore the repository is logically consolidated (one active workspace), but physical deletion of the four historical refs remains an owner/admin action. Before deletion, retain an archive tag or verify the merged PRs and preserve any required source snapshots.

This is a verified inventory and safe-cleanup boundary, not a claim that branch refs have already been deleted.


## Owner cleanup verification — 1 November 2026

A fresh GitHub REST branch-list read was performed after the repository owner cleanup. The following five historical Biology refs are now absent from the live branch list:
- `biology-learning-experience-pass`
- `biology-deep-editorial-pass-1`
- `biology-release-integration`
- `biology-atlas`
- `workspace/biology` remains present and is the sole active Biology development branch.

The live repository now lists exactly these seven branches: `atlas-of-knowledge-integration`, `main`, `portal-foundation`, `workspace/biology`, `workspace/chemistry`, `workspace/geography`, and `workspace/physics`. Thus the four historical refs previously identified plus `biology-atlas` have been physically removed; no non-Biology workspace branch was removed. This is confirmed from the current remote branch enumeration, not inferred from the earlier recommendation.


## Deleted-branch commit recovery audit — 1 November 2026

### Graph-level result

- Historical tip remains resolvable by SHA: `98ec95abfbce011f78fa96d8b6c813dc1b43fe29`.
- GitHub compare `workspace/biology...${sha}` reports `diverged`, **225 commits ahead** on the historical tip and 934 commits ahead on the current workspace; merge base: `20a69a14886131e50f7cb3e785103a741af670d4`.
- Querying the historical tip's commit history with path filter `biology` returns **180 commits that touched the Biology directory**. The remaining **45 of the 225 branch-only commits** did not touch `biology/` and belong to other discipline/shared repository work. The 180 are unique Git-history commits relative to the current branch's merge base; this does **not** mean their content is absent from the current atlas.

### Content reconciliation

- Compared the historical and current versions of all 14 Biology page files present in the historical diff: README, landing page, ten core chapters, and the Kyrgyzstan flora/fauna chapters.
- Current Biology README is substantially expanded (historical 21,331 characters; current 184,077). The current chapter files are also larger and more developed than the historical snapshots.
- Text-block comparison found the historical learning objectives, glossaries, quiz material, navigation, interactive modules and scientific plate concepts represented in the current chapter versions. Several short overview paragraphs differ in wording, but their subject matter is covered by the newer explanatory sections.
- The old flora and fauna regional dossiers were checked against the current versions. Distinctive legacy topics including Besh-Aral marmot, CAMCA maral estimate in the Naryn valley, Son-Kul and Chatyr-Kul Ramsar bird records, the Ministry's dated maral figure and the October 2026 fish-research memorandum are present in the current fauna chapter. The current chapter also contains later evidence additions (including the 2026 Common Crane record) not present in the historical snapshot.
- No confirmed scientifically useful Biology passage or interactive feature was identified as missing from `workspace/biology`. No cherry-pick or file overwrite was made. This is a source/content reconciliation, not independent scientific sign-off or browser test execution.

### Inventory of all 180 Biology-path commits

The following commits are unique in the historical branch's Git ancestry relative to the current workspace merge base and touch `biology/`. Their content is retained here as an audit index; do not interpret this list as a set of 180 missing changes.

- [`98ec95abfbce011f78fa96d8b6c813dc1b43fe29`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/98ec95abfbce011f78fa96d8b6c813dc1b43fe29) — Record explicit button type accessibility hardening
- [`8becb857fb3fbf2d449d366e04c5d18890493530`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8becb857fb3fbf2d449d366e04c5d18890493530) — Set explicit button types for safe interaction
- [`64159738da118641aad4e7ccd2a70a72212c0b9d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/64159738da118641aad4e7ccd2a70a72212c0b9d) — Set explicit button types for safe interaction
- [`e378fdde37a4b0530b3041ed28f92af669dca5b0`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e378fdde37a4b0530b3041ed28f92af669dca5b0) — Set explicit button types for safe interaction
- [`11d0a35f05a82a528f696af0970cdc3478763fc5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/11d0a35f05a82a528f696af0970cdc3478763fc5) — Set explicit button types for safe interaction
- [`3100d6909237175d6da3a02ca6ab9a3dff733426`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/3100d6909237175d6da3a02ca6ab9a3dff733426) — Set explicit button types for safe interaction
- [`5105d10bc3425473d167656d9393fdf302f1922c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5105d10bc3425473d167656d9393fdf302f1922c) — Set explicit button types for safe interaction
- [`b842060a15e836eeb22d732392900b67e366e037`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b842060a15e836eeb22d732392900b67e366e037) — Set explicit button types for safe interaction
- [`4c1a11cc604e1a78edce39420887f1408bba1260`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4c1a11cc604e1a78edce39420887f1408bba1260) — Set explicit button types for safe interaction
- [`d1f7031d9d80852c85fe54fb53fceb3efc6a02c3`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/d1f7031d9d80852c85fe54fb53fceb3efc6a02c3) — Set explicit button types for safe interaction
- [`f75ebeb974a8bf3399a94d82bcc2b4a53edc3eaa`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f75ebeb974a8bf3399a94d82bcc2b4a53edc3eaa) — Set explicit button types for safe interaction
- [`17ee028cd4655496ec693b6227d278baad6dc325`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/17ee028cd4655496ec693b6227d278baad6dc325) — Set explicit button types for safe interaction
- [`6a9db6470e3a0207a7c80db966e7962f9f82a3f5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/6a9db6470e3a0207a7c80db966e7962f9f82a3f5) — Document final static validation of Biology atlas
- [`0a9e42b4fe9186f614b31d9e466cbda514ada2ef`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0a9e42b4fe9186f614b31d9e466cbda514ada2ef) — Add 2026 fish biodiversity research update
- [`50eb654b6413ffb1bb44c70689e70da38a468cfd`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/50eb654b6413ffb1bb44c70689e70da38a468cfd) — Add 2026 biodiversity research methods update
- [`f7027baffa5338d2f8ba116ff3197b46e357a96f`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f7027baffa5338d2f8ba116ff3197b46e357a96f) — Add 2026 biodiversity research methods update
- [`1f7de80d1e1e04d6c17af864d06246a7e8c3765b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/1f7de80d1e1e04d6c17af864d06246a7e8c3765b) — Add NAS Biology Institute Red Data Book project reference
- [`03392558bf48b540e9a0c8800152e56420604fb6`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/03392558bf48b540e9a0c8800152e56420604fb6) — Add NAS Biology Institute Red Data Book project reference
- [`d75586bda3b3fd4809281b23eaadeb4844fe983d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/d75586bda3b3fd4809281b23eaadeb4844fe983d) — Add Kyrgyzstan regional biodiversity chapters to Biology landing page
- [`715e196e2c71474b465b765e9582e861600888a9`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/715e196e2c71474b465b765e9582e861600888a9) — Complete regional biodiversity documentation for seven oblasts
- [`1b999c83e9c36a08c42e447a77d5155f8b3785f5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/1b999c83e9c36a08c42e447a77d5155f8b3785f5) — Document Chuy regional biodiversity dossiers
- [`b0fc4fffd056df25626ce105e021120672bd365a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b0fc4fffd056df25626ce105e021120672bd365a) — Add Chuy Region fauna dossier
- [`8e47633cced74160df8fed606152d40f5730ce54`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8e47633cced74160df8fed606152d40f5730ce54) — Add Chuy Region flora dossier
- [`5dc9f2fef57fca1773df12ba15e657415ca16ac5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5dc9f2fef57fca1773df12ba15e657415ca16ac5) — Fix paragraph markup in Kyrgyzstan fauna chapter
- [`466c0ad9177eafb1fd6c15730afff46e3b6b0fbe`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/466c0ad9177eafb1fd6c15730afff46e3b6b0fbe) — Document Talas regional biodiversity dossiers
- [`7ef948a23ce9564a5510a57d108d393df540be2f`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7ef948a23ce9564a5510a57d108d393df540be2f) — Add Talas Region fauna dossier
- [`1d53ae8726ba5031d46fb6d7033ace2c60fb1052`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/1d53ae8726ba5031d46fb6d7033ace2c60fb1052) — Add Talas Region flora dossier
- [`b081dc5ae8e63d3646e792624c10ddfedde52b4d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b081dc5ae8e63d3646e792624c10ddfedde52b4d) — Add Batken primary and scientific sources
- [`b76a161b875f6e8a2c2664ff6aa33eeccfa7ad96`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b76a161b875f6e8a2c2664ff6aa33eeccfa7ad96) — Add Batken regional biodiversity field dossier
- [`5cd16ea7a0c1a32bd0b3f849befc60165ec5d8d2`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5cd16ea7a0c1a32bd0b3f849befc60165ec5d8d2) — Add Batken regional biodiversity field dossier
- [`f515da408b7b0b6ad52352c5768bdecee37b443a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f515da408b7b0b6ad52352c5768bdecee37b443a) — Document Osh biodiversity field dossiers
- [`dbc2bcc4bbcefe022d5d616c8a7a95c14be2621e`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/dbc2bcc4bbcefe022d5d616c8a7a95c14be2621e) — Add primary research sources for Osh regional dossiers
- [`424b7789d2d23298d9b9390c1c1e8413c951504c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/424b7789d2d23298d9b9390c1c1e8413c951504c) — Add primary research sources for Osh regional dossiers
- [`0df69ed1ccb54504eecb34239763d54f71948125`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0df69ed1ccb54504eecb34239763d54f71948125) — Add Osh regional biodiversity field dossier
- [`c322fee78c477dca20c773557c52d18f5035a059`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c322fee78c477dca20c773557c52d18f5035a059) — Add Osh regional biodiversity field dossier
- [`047ded9537618c8436bd44ac2f2d9c9bb394418c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/047ded9537618c8436bd44ac2f2d9c9bb394418c) — Document Naryn biodiversity field dossiers
- [`a53b903912cf92fb9ce0d213759b0a50776ea940`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a53b903912cf92fb9ce0d213759b0a50776ea940) — Cite Naryn regional biodiversity dossier sources
- [`3f37dd2dfcbe920a1e9b404ffa280d6274f2241c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/3f37dd2dfcbe920a1e9b404ffa280d6274f2241c) — Cite Naryn regional biodiversity dossier sources
- [`2248edef4a66fb68ff9fa4463f3bf143a97aa28f`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/2248edef4a66fb68ff9fa4463f3bf143a97aa28f) — Add Naryn regional biodiversity field dossier
- [`58f63290b531eaba9eeb1a81600ddcfaf0a80422`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/58f63290b531eaba9eeb1a81600ddcfaf0a80422) — Add Naryn regional biodiversity field dossier
- [`0597f60d165a8dc5b3e33dbd6c210a3be169b4a3`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0597f60d165a8dc5b3e33dbd6c210a3be169b4a3) — Document Issyk-Kul biodiversity field dossiers
- [`70a3d1523d862b9cd13cedfbaac60230cc1817ba`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/70a3d1523d862b9cd13cedfbaac60230cc1817ba) — Correct markup and source URL in Issyk-Kul fauna dossier
- [`4f2ea0435c6f2990c2f6e1ebd745d81643244264`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4f2ea0435c6f2990c2f6e1ebd745d81643244264) — Cite Issyk-Kul biodiversity field dossier sources
- [`33cedda0490f97ef52c8c07ea8879e7a9a696e1c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/33cedda0490f97ef52c8c07ea8879e7a9a696e1c) — Cite Issyk-Kul biodiversity field dossier sources
- [`54f68ab549ef9193bde8b15617bc28d45601f326`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/54f68ab549ef9193bde8b15617bc28d45601f326) — Add Issyk-Kul regional biodiversity field dossier
- [`5dc437c2f865391688cce11c6dc70ce9b1d28f0a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5dc437c2f865391688cce11c6dc70ce9b1d28f0a) — Add Issyk-Kul regional biodiversity field dossier
- [`f352f0165be956cc0c1fa9c7f8b8a3e4909b6d39`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f352f0165be956cc0c1fa9c7f8b8a3e4909b6d39) — Document Jalal-Abad biodiversity field dossiers
- [`acaeaf73c68e19790ad1e78aef1a6f734ba2467d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/acaeaf73c68e19790ad1e78aef1a6f734ba2467d) — Add verified regional biodiversity references
- [`78e95e9fd87bf7f3edcc4e3325da449baceb3ecd`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/78e95e9fd87bf7f3edcc4e3325da449baceb3ecd) — Add verified regional biodiversity references
- [`3a764d5e7ec58e4e78df65d08d20b49785bfb77b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/3a764d5e7ec58e4e78df65d08d20b49785bfb77b) — Add Jalal-Abad regional biodiversity field dossier
- [`180642e6e1be1bf63d1a51d9f1630e09dfda71ed`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/180642e6e1be1bf63d1a51d9f1630e09dfda71ed) — Add Jalal-Abad regional biodiversity field dossier
- [`a802ccc40805914f20e55714c956a764f7be34a6`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a802ccc40805914f20e55714c956a764f7be34a6) — Document seven-oblast biodiversity framework and source basis
- [`7945ceebe34b138b414d925e511389212509f6fc`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7945ceebe34b138b414d925e511389212509f6fc) — Polish bilingual oblast labels in regional biodiversity tables
- [`2ff5ab1ddd7a9c0d5d66e2f0b379ac4671a7811a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/2ff5ab1ddd7a9c0d5d66e2f0b379ac4671a7811a) — Polish bilingual oblast labels in regional biodiversity tables
- [`59faa9565efcd14671785821982d6552ad870048`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/59faa9565efcd14671785821982d6552ad870048) — Add coordinated seven-oblast regional biodiversity framework
- [`a8aaa97dc1306733a733b02e0a0d408bc729d500`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a8aaa97dc1306733a733b02e0a0d408bc729d500) — Add coordinated seven-oblast regional biodiversity framework
- [`b8c32f5e5aec0a3185e1083fc1b86806cf06df85`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b8c32f5e5aec0a3185e1083fc1b86806cf06df85) — Document regional biodiversity chapter QA and 2026 Red Data Book update
- [`3f55e2234a49066bc51852416351bc6adf199dbb`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/3f55e2234a49066bc51852416351bc6adf199dbb) — Improve regional chapter navigation and Red Data Book currency note
- [`ea5da88191523f8692f28674a0a5ec6a57222824`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/ea5da88191523f8692f28674a0a5ec6a57222824) — Improve regional chapter navigation and Red Data Book currency note
- [`a0d4ebe127386d07b601974a96339ec10ed153c5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a0d4ebe127386d07b601974a96339ec10ed153c5) — Document Kyrgyzstan fauna regional chapter
- [`4d89ff87d569bad9a32f3487b15ea262d20f4941`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4d89ff87d569bad9a32f3487b15ea262d20f4941) — Link zoology chapter to Kyrgyzstan regional fauna
- [`681c07e98a7a9eb721dfef1facd442a7c6e230d0`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/681c07e98a7a9eb721dfef1facd442a7c6e230d0) — Create bilingual regional fauna of Kyrgyzstan chapter
- [`29fac75c0c066f5e3f9d1086c92969f0973e5ba2`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/29fac75c0c066f5e3f9d1086c92969f0973e5ba2) — Document Kyrgyzstan flora regional chapter
- [`47abb5bbb779b06f97752ca87fb38d02d81954c9`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/47abb5bbb779b06f97752ca87fb38d02d81954c9) — Link botany chapter to Kyrgyzstan regional flora
- [`4cab9dc495ab09c7b6c1faeba19a346a56243ae3`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4cab9dc495ab09c7b6c1faeba19a346a56243ae3) — Create bilingual regional flora of Kyrgyzstan chapter
- [`535db27b5f4afb9a2cc3c24c3e2d60e1476a34ae`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/535db27b5f4afb9a2cc3c24c3e2d60e1476a34ae) — Polish quiz navigation and keyboard focus styling
- [`6357a1b5c7cdf4e4267fa5eb110c220d8f90cd06`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/6357a1b5c7cdf4e4267fa5eb110c220d8f90cd06) — Polish quiz navigation and keyboard focus styling
- [`001f532d4f21051dc92879be6279659c3ac32070`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/001f532d4f21051dc92879be6279659c3ac32070) — Polish quiz navigation and keyboard focus styling
- [`50aebee3b8c54eb9930ead0ebabaf67dc7496cbe`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/50aebee3b8c54eb9930ead0ebabaf67dc7496cbe) — Polish quiz navigation and keyboard focus styling
- [`0bf0234ff9a514ea9d4c13f4c8d97d876d9e1125`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0bf0234ff9a514ea9d4c13f4c8d97d876d9e1125) — Polish quiz navigation and keyboard focus styling
- [`115320a9c168691703114807588de4aa293c9ce8`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/115320a9c168691703114807588de4aa293c9ce8) — Polish quiz navigation and keyboard focus styling
- [`f2ad6d195711475f370b5b6d302f96026e1ca20f`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f2ad6d195711475f370b5b6d302f96026e1ca20f) — Polish quiz navigation and keyboard focus styling
- [`ef73ab24be0bdce5172ac9dffae96189aec90242`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/ef73ab24be0bdce5172ac9dffae96189aec90242) — Polish quiz navigation and keyboard focus styling
- [`a4f14536e8780c0f814292831ac7fa7a5bf812e5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a4f14536e8780c0f814292831ac7fa7a5bf812e5) — Polish quiz navigation and keyboard focus styling
- [`b5b2ffca25a95c369187e90077a5a491f53e27ad`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b5b2ffca25a95c369187e90077a5a491f53e27ad) — Polish quiz navigation and keyboard focus styling
- [`e9ad7d17934d94c8b6838f4cd7fb15ec7667dfd0`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e9ad7d17934d94c8b6838f4cd7fb15ec7667dfd0) — Make quiz answer controls explicit non-submit buttons
- [`94cbb7ae5504a2211862005d0dda08d77db31da7`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/94cbb7ae5504a2211862005d0dda08d77db31da7) — Make quiz answer controls explicit non-submit buttons
- [`e15a78c50ae24b916e91f3d2759c77e85bb0c901`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e15a78c50ae24b916e91f3d2759c77e85bb0c901) — Make quiz answer controls explicit non-submit buttons
- [`7f81fca464a7a6da751c23e19975c30721208359`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7f81fca464a7a6da751c23e19975c30721208359) — Make quiz answer controls explicit non-submit buttons
- [`8ac3c54aaae8626d39ca0b0c8bad29472078d233`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8ac3c54aaae8626d39ca0b0c8bad29472078d233) — Make quiz answer controls explicit non-submit buttons
- [`2ab8fe807b231f6b2ef30067b2375e9c1c1d2a73`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/2ab8fe807b231f6b2ef30067b2375e9c1c1d2a73) — Make quiz answer controls explicit non-submit buttons
- [`4f1e3e3c34db055d7760131caeefba49ba3f4d27`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4f1e3e3c34db055d7760131caeefba49ba3f4d27) — Make quiz answer controls explicit non-submit buttons
- [`7a63930d89f7413eceecd9013774af8c1aaee3ac`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7a63930d89f7413eceecd9013774af8c1aaee3ac) — Make quiz answer controls explicit non-submit buttons
- [`aa9682faf8672579e83ca17f9dcb8a9fa1b9fca4`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/aa9682faf8672579e83ca17f9dcb8a9fa1b9fca4) — Make quiz answer controls explicit non-submit buttons
- [`af5f9409a7400895b6479f5708cb88fe6c32df75`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/af5f9409a7400895b6479f5708cb88fe6c32df75) — Make quiz answer controls explicit non-submit buttons
- [`d335ded9a133cc049d8eacbdee27c989e9ec3476`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/d335ded9a133cc049d8eacbdee27c989e9ec3476) — Document five-question bilingual knowledge checks
- [`7956a967638a828ddd50c66862e5fa9d59165f4b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7956a967638a828ddd50c66862e5fa9d59165f4b) — Expand bilingual chapter knowledge check to five questions
- [`010192e8852190babd4c2b489e0e6d759c97c217`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/010192e8852190babd4c2b489e0e6d759c97c217) — Expand bilingual chapter knowledge check to five questions
- [`979ee90cb2a3c256123380c4476ed4439989e746`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/979ee90cb2a3c256123380c4476ed4439989e746) — Expand bilingual chapter knowledge check to five questions
- [`0b2e0ae352786ee8b82c437675b2dbbfc8aa3533`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0b2e0ae352786ee8b82c437675b2dbbfc8aa3533) — Expand bilingual chapter knowledge check to five questions
- [`8ed5aa286c0f3e56c978eb10072a24aaca5d8b46`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8ed5aa286c0f3e56c978eb10072a24aaca5d8b46) — Expand bilingual chapter knowledge check to five questions
- [`36ffa3cff24540dfeb430557dd676f0725444b1d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/36ffa3cff24540dfeb430557dd676f0725444b1d) — Expand bilingual chapter knowledge check to five questions
- [`0c45cb73604826446cb489cf6c65cd3133eeb9b0`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0c45cb73604826446cb489cf6c65cd3133eeb9b0) — Expand bilingual chapter knowledge check to five questions
- [`f80a1d1b21c6502aab30411a5bcf826d3a042d47`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f80a1d1b21c6502aab30411a5bcf826d3a042d47) — Expand bilingual chapter knowledge check to five questions
- [`4743e432fd33f7e28b6b2ccdfaae90c0b82303bc`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4743e432fd33f7e28b6b2ccdfaae90c0b82303bc) — Add question navigation to botany knowledge check
- [`3dc0603099b7725a9301d8694d96bc220d320f5b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/3dc0603099b7725a9301d8694d96bc220d320f5b) — Correct zoology quiz explanation
- [`d2e9b1bdb7c4b0787d62f911045f8890f35f3ed1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/d2e9b1bdb7c4b0787d62f911045f8890f35f3ed1) — Expand bilingual chapter knowledge check to five questions
- [`b295c945a8e4a050d8356bbf8650936a6f9f6f2a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b295c945a8e4a050d8356bbf8650936a6f9f6f2a) — Expand bilingual chapter knowledge check to five questions
- [`8e9474df2f33492d89323ff28471b09082eaeab1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8e9474df2f33492d89323ff28471b09082eaeab1) — Document learning objectives and glossaries across all biology chapters
- [`7a5efec7eb710a6b0f9da67569706a63b51f4403`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7a5efec7eb710a6b0f9da67569706a63b51f4403) — Add systematics learning objectives and bilingual glossary
- [`0dc843961d190aed3ba5b91a3e40353b7792916d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0dc843961d190aed3ba5b91a3e40353b7792916d) — Add biochemistry learning objectives and bilingual glossary
- [`10b7f08c84b059513e7cb18f1884b5a77c6bf211`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/10b7f08c84b059513e7cb18f1884b5a77c6bf211) — Add evolution learning objectives and bilingual glossary
- [`9bc071d9c6e2a022b50b17872e83eb095c478045`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/9bc071d9c6e2a022b50b17872e83eb095c478045) — Add ecology learning objectives and bilingual glossary
- [`c022e4d0706da150ecf0d4e7beb764c994e06a49`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c022e4d0706da150ecf0d4e7beb764c994e06a49) — Add microbiology learning objectives and bilingual glossary
- [`f7a8c54e3fabd4daf633a1bae08a53ca5b85343c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f7a8c54e3fabd4daf633a1bae08a53ca5b85343c) — Add genetics learning objectives and bilingual glossary
- [`18a62db096d5d43404a2650cdf94b8a3612fc825`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/18a62db096d5d43404a2650cdf94b8a3612fc825) — Add anatomy learning objectives and bilingual glossary
- [`a03e820b0dd61d7ef8ae5d6b8029d2dfe5498a6b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a03e820b0dd61d7ef8ae5d6b8029d2dfe5498a6b) — Add cell biology learning objectives and bilingual glossary
- [`77270f16121b888011207d96374d537828f69f08`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/77270f16121b888011207d96374d537828f69f08) — Document bilingual learning sections and Kyrgyzstan biodiversity plan
- [`c02abca10b66df779edb8705bb7635fba51724d5`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c02abca10b66df779edb8705bb7635fba51724d5) — Add zoology learning objectives and bilingual glossary
- [`2c7838cd4098e1528932a7bb9d923851f89df91f`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/2c7838cd4098e1528932a7bb9d923851f89df91f) — Add botany learning objectives and bilingual glossary
- [`1e8d936445867f949bf50f13b09b9f6e5d0de4aa`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/1e8d936445867f949bf50f13b09b9f6e5d0de4aa) — Improve keyboard accessibility with skip links
- [`f5b42927952ed9d871435888b0075afdfadad241`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f5b42927952ed9d871435888b0075afdfadad241) — Improve keyboard accessibility with skip links
- [`b0dcec99db27f322057db51392794767162afe45`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b0dcec99db27f322057db51392794767162afe45) — Improve keyboard accessibility with skip links
- [`c606d8575523e1c6954530551b4ca1ac6fc263f9`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c606d8575523e1c6954530551b4ca1ac6fc263f9) — Improve keyboard accessibility with skip links
- [`8ede4d650680e71053ea3031a69bc7edf2ec0ac1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8ede4d650680e71053ea3031a69bc7edf2ec0ac1) — Improve keyboard accessibility with skip links
- [`9e7da612b187d30b40d99eb0ed81e598bceae622`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/9e7da612b187d30b40d99eb0ed81e598bceae622) — Improve keyboard accessibility with skip links
- [`6264145c3c0a03ba6d10ac1ecf9759b08c98721a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/6264145c3c0a03ba6d10ac1ecf9759b08c98721a) — Improve keyboard accessibility with skip links
- [`b09643520d704bf6848113b433c4a2a17f2311da`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b09643520d704bf6848113b433c4a2a17f2311da) — Improve keyboard accessibility with skip links
- [`fc32d572e7e35cf44f29f938f227b601a9ef18e7`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/fc32d572e7e35cf44f29f938f227b601a9ef18e7) — Improve keyboard accessibility with skip links
- [`e2c847f3d5bb954f6ae9e70d5fa297d03e34af98`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e2c847f3d5bb954f6ae9e70d5fa297d03e34af98) — Improve keyboard accessibility with skip links
- [`03225d0959cffb793879a7d44e9cd12e370d6940`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/03225d0959cffb793879a7d44e9cd12e370d6940) — Improve keyboard accessibility with skip links
- [`e3e65a2573cdbf59266b94c9e82f36f380bb4e69`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e3e65a2573cdbf59266b94c9e82f36f380bb4e69) — Document bilingual sequential navigation and QA roadmap
- [`f64c6385e662e2547d7d9c4ff6e4403f56f642eb`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f64c6385e662e2547d7d9c4ff6e4403f56f642eb) — Add sequential bilingual navigation across Biology chapters
- [`f8074ed8049e193f7ab0acb8e72b32e4fe7f54ac`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f8074ed8049e193f7ab0acb8e72b32e4fe7f54ac) — Add sequential bilingual navigation across Biology chapters
- [`6048c5aa65be6869ea1287128a95bda333097c17`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/6048c5aa65be6869ea1287128a95bda333097c17) — Add sequential bilingual navigation across Biology chapters
- [`dd1526273c3638307656f6e7d36440f548026858`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/dd1526273c3638307656f6e7d36440f548026858) — Add sequential bilingual navigation across Biology chapters
- [`c6e7f915197a94eb55aa1877d603585befc1a158`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c6e7f915197a94eb55aa1877d603585befc1a158) — Add sequential bilingual navigation across Biology chapters
- [`c3d7fbf9344f69ddde62d97647753b500e65f1a8`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c3d7fbf9344f69ddde62d97647753b500e65f1a8) — Add sequential bilingual navigation across Biology chapters
- [`d856fc8a524983151312c84767eedb35b67cfda1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/d856fc8a524983151312c84767eedb35b67cfda1) — Add sequential bilingual navigation across Biology chapters
- [`25d50ccd859cffbc9c28147b8b73d231a15b4511`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/25d50ccd859cffbc9c28147b8b73d231a15b4511) — Add sequential bilingual navigation across Biology chapters
- [`e20de592bf2a958511c808e2e1485379faa8060e`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e20de592bf2a958511c808e2e1485379faa8060e) — Add sequential bilingual navigation across Biology chapters
- [`60744e7f8a61695b20a5b73b13ec9980fa4c5e85`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/60744e7f8a61695b20a5b73b13ec9980fa4c5e85) — Add sequential bilingual navigation across Biology chapters
- [`8586fa4cd92eb69f9bbcabaa764c4fc386286fbc`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8586fa4cd92eb69f9bbcabaa764c4fc386286fbc) — Document expanded systematics chapter
- [`7f292da1b3343cc153ba8412d9b8af53f48ee7cc`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7f292da1b3343cc153ba8412d9b8af53f48ee7cc) — Expand systematics chapter with taxonomy and identification interactives
- [`7465860a67d808b3956e3b01d0df906f83fe6bb3`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/7465860a67d808b3956e3b01d0df906f83fe6bb3) — Document expanded biochemistry chapter
- [`4d6b5d2a0a2bd28f051bdd565252e2d82746e264`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4d6b5d2a0a2bd28f051bdd565252e2d82746e264) — Expand biochemistry chapter with molecular plates and interactive models
- [`56ac4bb79aa3b46bb26c9b3d86d1e78877d48d9e`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/56ac4bb79aa3b46bb26c9b3d86d1e78877d48d9e) — Document expanded evolutionary biology interactives
- [`b4f0d2c2131cb5af398c4ebb5e272390869c720c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b4f0d2c2131cb5af398c4ebb5e272390869c720c) — Expand evolution chapter with phylogeny and interactive selection models
- [`897556e3307a46d93572342bda62299ce87f050c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/897556e3307a46d93572342bda62299ce87f050c) — Document ecology ecosystem diagram and interactive learning tools
- [`6b6cb5cb4905acffc70a2b6a3c450a834ed1aec7`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/6b6cb5cb4905acffc70a2b6a3c450a834ed1aec7) — Expand ecology chapter with ecosystem plate and interactive cycles
- [`9a6798032f4b5615c125cfc48e81bb5929a63bfd`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/9a6798032f4b5615c125cfc48e81bb5929a63bfd) — Document microbiology scientific plate and learning modules
- [`542898bdae053c31abf1407db10532a06ff4c61a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/542898bdae053c31abf1407db10532a06ff4c61a) — Expand microbiology chapter with original plate and interactive modules
- [`5f500c1d677481874aea39d76155f44c025e5345`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5f500c1d677481874aea39d76155f44c025e5345) — Document expanded genetics learning interactives
- [`ffa2832598ee815bf949433b554c870e8f00e0a8`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/ffa2832598ee815bf949433b554c870e8f00e0a8) — Rebuild genetics chapter with transcription translation and mutation interactives
- [`e0a7778ea8b037e2ed1e1253afbdad6ff05a10bb`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e0a7778ea8b037e2ed1e1253afbdad6ff05a10bb) — Document expanded cell biology learning modules
- [`de825c47fc33f12ba2edede01112731abc37bfc4`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/de825c47fc33f12ba2edede01112731abc37bfc4) — Expand cell biology with organelle, membrane transport and mitosis interactives
- [`c2201065aa6b5867e119fb6da6eb50667c874dd4`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c2201065aa6b5867e119fb6da6eb50667c874dd4) — Document anatomy illustration and organ-system explorer
- [`5dcf3be464c0822229787284f61cf3a2d0747c59`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5dcf3be464c0822229787284f61cf3a2d0747c59) — Expand Anatomy chapter with bilingual organ-system explorer
- [`a13ad41041f8e7ddcf9986516e32c533f37b549c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/a13ad41041f8e7ddcf9986516e32c533f37b549c) — Document interactive vertebrate comparison module
- [`e0ff82df330e5451c03f2238c8404d8c142e07da`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e0ff82df330e5451c03f2238c8404d8c142e07da) — Repair Zoology chapter and add bilingual vertebrate explorer
- [`5dbe20c373842497e561cc856b265506ebdfbce1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5dbe20c373842497e561cc856b265506ebdfbce1) — Document interactive photosynthesis learning module
- [`daabc4dc1975215c5eb592732602349a6fbe533e`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/daabc4dc1975215c5eb592732602349a6fbe533e) — Expand Botany with bilingual interactive photosynthesis model
- [`5994ef87c420baee4b4652af4d47798eb672d1cd`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/5994ef87c420baee4b4652af4d47798eb672d1cd) — Update Biology Atlas development progress
- [`bea205de64bb9124b34a7957ead3061594bd645a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/bea205de64bb9124b34a7957ead3061594bd645a) — Add DNA scientific plate and interactive base-pairing model
- [`08fe34a4ef949c0cdd1aabe3fe9cbb8fb9ef974c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/08fe34a4ef949c0cdd1aabe3fe9cbb8fb9ef974c) — Add interactive plant organ learning module
- [`aff0206d977caea7849932a2e90bb67acaa8caee`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/aff0206d977caea7849932a2e90bb67acaa8caee) — Add original bilingual scientific diagram to biology/chapters/cell-biology.html
- [`213cf69953024ab4122ead8e28ac30bc7ff78cb1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/213cf69953024ab4122ead8e28ac30bc7ff78cb1) — Add original bilingual scientific diagram to biology/chapters/zoology.html
- [`0c57214c2a99ef6bea8a4327cdf0a1330c653487`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/0c57214c2a99ef6bea8a4327cdf0a1330c653487) — Add original bilingual scientific diagram to biology/chapters/botany.html
- [`4b862f37d5c16f1170975abed388059dc31b26b0`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4b862f37d5c16f1170975abed388059dc31b26b0) — Document Biology Atlas structure and roadmap
- [`f6527fe275c048c243803a8a126a0942c86e4b4f`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/f6527fe275c048c243803a8a126a0942c86e4b4f) — Correct bilingual quiz answer key
- [`c8d10f1ad1db35005a981cc449e1c3aa7205368a`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c8d10f1ad1db35005a981cc449e1c3aa7205368a) — Correct bilingual quiz answer key
- [`b41c38f78e0c6a5c104b87a40c4ee0acf4d41f0b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/b41c38f78e0c6a5c104b87a40c4ee0acf4d41f0b) — Correct bilingual quiz answer key
- [`9da6f83e0aa2bdf358c40bb0f90a1be90406ee55`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/9da6f83e0aa2bdf358c40bb0f90a1be90406ee55) — Correct bilingual quiz answer key
- [`144056a3aadd0349c1a6ef58a0e3bd6cca7aac65`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/144056a3aadd0349c1a6ef58a0e3bd6cca7aac65) — Correct bilingual quiz answer key
- [`58545edcbb903a879f5f38a96abb88b309277d73`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/58545edcbb903a879f5f38a96abb88b309277d73) — Correct bilingual quiz answer key
- [`3a3e8a00d942c6725db9d079fbbc498e62f982a6`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/3a3e8a00d942c6725db9d079fbbc498e62f982a6) — Correct bilingual quiz answer key
- [`62787b10a11ab4a39edb6d810d349bfb2e50bf76`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/62787b10a11ab4a39edb6d810d349bfb2e50bf76) — Fix bilingual chapter knowledge-check answers
- [`c196d2f30bb84a012866dfa1cf4870584fc870a1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/c196d2f30bb84a012866dfa1cf4870584fc870a1) — Fix bilingual chapter knowledge-check answers
- [`bed4748293c1eae5de3eeda20880e0815be1c21c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/bed4748293c1eae5de3eeda20880e0815be1c21c) — Fix bilingual chapter knowledge-check answers
- [`990c300f7d9c341a43b9ab6df35a23122fdc9084`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/990c300f7d9c341a43b9ab6df35a23122fdc9084) — Add bilingual Biology chapter: Систематика и классификация
- [`eee407e11d9ca0b39f83731f2b07b8e4e1a6cdbe`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/eee407e11d9ca0b39f83731f2b07b8e4e1a6cdbe) — Add bilingual Biology chapter: Биохимия
- [`6a518ded4a21c86c390c31073fb1974a6013f08c`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/6a518ded4a21c86c390c31073fb1974a6013f08c) — Add bilingual Biology chapter: Эволюционная биология
- [`af857d15f2c578e04d295d319b6d44d5fa18f15d`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/af857d15f2c578e04d295d319b6d44d5fa18f15d) — Add bilingual Biology chapter: Экология
- [`cd492ff6120225ab4589ba6133364c2dce6603d1`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/cd492ff6120225ab4589ba6133364c2dce6603d1) — Add bilingual Biology chapter: Микробиология
- [`8b1d16bb5a3567244a305e640eaf1d0a4a36388b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/8b1d16bb5a3567244a305e640eaf1d0a4a36388b) — Add bilingual Biology chapter: Генетика
- [`997b953b68c72f33a3e22a9ff8effd2fe3261b0b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/997b953b68c72f33a3e22a9ff8effd2fe3261b0b) — Add bilingual Biology chapter: Анатомия и физиология
- [`307069f91ee6541d356a197c13b4c7b20d761840`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/307069f91ee6541d356a197c13b4c7b20d761840) — Add bilingual Biology chapter: Цитология и клеточная биология
- [`4ee52c21861e9384dd95613b521b889c06376c42`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/4ee52c21861e9384dd95613b521b889c06376c42) — Add bilingual Biology chapter: Зоология
- [`2f4ae5137824b05d599a8139c45af451dd5db55b`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/2f4ae5137824b05d599a8139c45af451dd5db55b) — Add bilingual Biology chapter: Ботаника
- [`e25aab5b83bdb4a684143abcd89619fbf3f682ff`](https://github.com/Ajokendo/Atlas-of-Knowledge/commit/e25aab5b83bdb4a684143abcd89619fbf3f682ff) — Create bilingual Biology Atlas with interactive cell model

### Decision

Keep `workspace/biology` as the canonical source. Do not recreate or merge `biology-atlas` wholesale. Preserve the historical tip SHA and this inventory in the canonical audit record. No missing Biology content was confirmed in this pass; if a future claim points to a specific legacy change, use its SHA above for targeted review.
