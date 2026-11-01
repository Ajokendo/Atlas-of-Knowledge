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
