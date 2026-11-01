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
