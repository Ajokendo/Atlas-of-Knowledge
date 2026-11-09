# Geography branch inventory and source-history reconciliation
**Audit date:** 1 November 2026  
**Repository:** `Ajokendo/Atlas-of-Knowledge`  
**Canonical development branch:** `workspace/geography`

## Executive finding

There is **one dedicated active Geography development branch**: `workspace/geography`. No second branch named `geography`, `geography-atlas` or another dedicated Geography workspace was present in the repository's branch inventory.

A legacy mixed-discipline branch, `portal-foundation`, contains the original Geography source chapters 02–26 alongside Chemistry and portal work. It is not a second active Geography workspace. It is retained as a historical source/backup branch and must not receive new Geography development.

The umbrella branch `atlas-of-knowledge-integration` is a platform-wide integration branch, not a Geography workspace. Its two commits ahead of `workspace/geography` concern the shared editorial standard and project registry, not Geography chapter content. Draft PR #6 uses this umbrella branch as its head and targets `main`.

**Operating rule:** all new Geography work, edits, audits and checkpoints go only to `workspace/geography`.

## Repository branch inventory

The repository returned 12 branches:

- `workspace/geography` — canonical Geography development branch.
- `portal-foundation` — legacy mixed-discipline source branch; archive/reference only.
- `atlas-of-knowledge-integration` — umbrella integration branch; not a Geography work branch.
- `main` — repository default branch; not the active Geography development branch.
- `workspace/biology`, `biology-atlas`, `biology-deep-editorial-pass-1`, `biology-learning-experience-pass`, `biology-release-integration` — Biology work/integration branches.
- `workspace/chemistry`, `chemistry-atlas-integration` — Chemistry work/integration branches.
- `workspace/physics` — Physics work branch.

No additional dedicated Geography branch appeared in this inventory.

## Commit-history comparison

The comparison was made against the checked-out branch heads on 1 November 2026.

| Comparison | Result | Interpretation |
|---|---:|---|
| `workspace/geography` vs `portal-foundation` | `portal-foundation` ahead by 80 commits; behind by 715; diverged | The legacy branch has a distinct source history, not a second current workspace. |
| `workspace/geography` vs `atlas-of-knowledge-integration` | Integration branch ahead by 2 commits; behind by 411; diverged | The two unique commits are platform-wide editorial-standard changes. |
| `workspace/geography` vs `main` | `main` behind by 415 commits; no commits ahead | `main` is not a parallel Geography source. |

The 80 commits unique to `portal-foundation` include 25 Geography chapter-introduction commits (chapters 02–26) and 55 commits concerning Chemistry and shared portal/platform work. The 25 Geography commit objects are not ancestors of the current canonical branch. They are preserved in the legacy branch listed above.

### The 25 unique Geography source commits

| Chapter | Source commit |
|---:|---|
| 02 | `7e3e3530600b729db2010490d64b93130486b11a` |
| 03 | `36767a090759fac83cc997cba3312d5769427c22` |
| 04 | `72ad9873c247624ea30fcef035639861b786d63c` |
| 05 | `4ed3823ac27ec692fce118a595bfb562edcbeb52` |
| 06 | `158cca609b7f2bba34f83d86347440245d0904e9` |
| 07 | `06e04086681243b8f33ba7f37276a311f46051ed` |
| 08 | `38c46e2954a0e95d7c964c6287b589580de1aeca` |
| 09 | `0c31570c867125d59954369e6d41d2618744ce94` |
| 10 | `45af85914a57d68012762f8c4479f29c1d114df2` |
| 11 | `316a28bb003e7359425a006484a5cff7885b4655` |
| 12 | `1cc02090168de6478e666201d908a20208358d65` |
| 13 | `1acfc51ed7a1a0404214cd67f9dc2d742aad8a0e` |
| 14 | `d82d2346cb54c2423cb4f1c8e51c648817e11ecc` |
| 15 | `aa43a575a7cacca97b9d48d634838fcaef8093d8` |
| 16 | `05c5de8b61d781986baf66d5413bac9aed738ea1` |
| 17 | `a3af8f4bf28c7f3e0a3734caad9486916480df75` |
| 18 | `20f993670a3e29e0ba88dd4432076936212b26e0` |
| 19 | `6ae3c96e3532405a472c57b650b71da3bd06d406` |
| 20 | `32d15e793a22df32895b4cfc9e7d639a10d66ff0` |
| 21 | `4a891753c739ccb4f46d8681d59111826e8f1fbf` |
| 22 | `2bde7edf7f3c758244b5e80d290fc39d5197a866` |
| 23 | `ce1d5c4d4add77b7ec51e5454050e48aef0f19cf` |
| 24 | `09f2a69d0c26998032282ec584e0b47c2dcea014` |
| 25 | `7b6b05fd5ecfae741c06a8190046a528976fc280` |
| 26 | `582608fc771935f9f350ff03c3945c14ec9f300e` |

Chapter 01 is present in `workspace/geography` and was not present in `portal-foundation`.

## File-level and unique-content review

All 25 chapter files (02–26) were compared between `portal-foundation` and `workspace/geography`. The blob SHAs differ for all 25 files. The canonical versions are substantially expanded; the legacy branch therefore represents older snapshots, not files that should replace the current versions.

A line-level set comparison identified 55 nonblank legacy lines not reproduced verbatim in the canonical files. Each was reviewed for content, not blindly copied:

- **Chapter 02:** the unmatched line was an obsolete language-status note. The canonical header now correctly describes the bilingual teaching text.
- **Chapter 06:** the legacy exercise included catchment delineation, tributary mapping and land-use impacts on floods and water quality. These useful tasks were added to the existing Russian and English practical assignment in the canonical chapter. Verified in commit `978befef9149cbd2178b331244c3734d96be03d0`.
- **Chapter 17:** the older source's mineral-resource examples and evaluation cautions are covered by the expanded canonical sections distinguishing occurrence, resource, reserve, actual extraction, economic viability and environmental constraints.
- **Chapter 22:** the older statistical figures and protected-area caveats are present in the canonical chapter.
- **Chapter 23:** the unmatched older city reference used the former name Jalal-Abad; the canonical text uses the updated name Manas where applicable.
- **Chapter 24:** the administrative-reform caution, legal references and glossary terms are represented in the current chapter.
- **Chapter 25:** the transport-network indicators and 2026 electricity-balance estimates are present in the canonical version.
- **Chapter 26:** the old rounded water figures are superseded by the more precise NSC 2025 series in the canonical text: 8,938.4 million m³ abstraction, 6,224.9 million m³ consumption and 5,821.1 million m³ for irrigation/agricultural water supply. The NDC, pasture, forest-cover and wastewater material is also represented in the expanded current chapter.

No legacy chapter file was copied over a canonical chapter. No older version was allowed to overwrite later bilingual, scientific or editorial corrections.

## Consolidation decision

1. Keep `workspace/geography` as the sole active Geography development branch.
2. Treat `portal-foundation` as read-only historical source material; do not create new Geography commits there.
3. Do not cherry-pick the 25 old chapter-creation commits into the active branch: their chapter content has already been carried forward and substantially revised, while the same legacy history also contains unrelated Chemistry and portal commits. The unique commit SHAs are recorded above and remain reachable through the preserved source branch.
4. Do not merge `atlas-of-knowledge-integration` into the Geography branch. Its two unique commits establish shared platform-wide standards; PR #6 remains an umbrella integration item.
5. Do not delete `portal-foundation`. The shared project registry explicitly requires old source branches to be retained as source and backup checkpoints. Keeping this historical reference does not create a second active Geography workspace.
6. All future Geography development must use `workspace/geography` only.

## Verification and resulting commits

- README branch policy updated and re-fetched successfully: commit `f9ac0d82c863b55b8d77378cb4642cacb6db974d`, blob `ba6edfb694018c81a93ceee3c2838292fcd7d342`.
- Chapter 06 bilingual practical assignment updated and re-fetched successfully: commit `978befef9149cbd2178b331244c3734d96be03d0`, blob `a7e006f9ee0fa86cb7233fc9e5e9e8050537f1c7`.
- This report records the full branch and commit review. The branch head and report will be re-fetched after the audit-log update.
