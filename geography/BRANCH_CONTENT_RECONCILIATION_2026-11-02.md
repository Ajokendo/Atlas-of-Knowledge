# Geography Branch Content Reconciliation — 2026-11-02

**Scope:** read-only comparison of `workspace/geography` with `portal-foundation` and `atlas-of-knowledge-integration`.  
**No merge, cherry-pick, deletion, or chapter overwrite was performed.**

## 1. Branch snapshots inspected

- `workspace/geography`: `d0b41f9d14f48c63b1d6b018fd49d0dabf9e04a5` (2026-11-01 18:34:57 UTC)
- `portal-foundation`: `582608fc771935f9f350ff03c3945c14ec9f300e` (2026-10-31 15:31:06 UTC)
- `atlas-of-knowledge-integration`: `aecea18a4a3297d861f9d6bcbd171f3cf1f8d294` (2026-10-31 17:11:49 UTC)

The integration branch and portal-foundation contain the same 25-file geography snapshot: chapters 02–26 plus `geography/index.html`. The active geography branch contains all 25 of those paths, plus chapter 01, supporting documents, the visual asset register, four SVG assets, and the newer geography index: 43 files in total.

**No geography file path present in either older snapshot is absent from `workspace/geography`.** The two older snapshots have matching blobs for their shared geography paths; they are an earlier content snapshot, not an alternate newer copy.

## 2. Chapter-by-chapter comparison

All 25 chapters that existed in the older snapshots (02–26) were compared at file, heading, paragraph and selected key-data level. Every one is larger in the active branch. The active branch also contains chapter 01, which is absent from both older snapshots.

At heading level, no old chapter section heading was found to be wholly absent except an obsolete/changed title in chapter 18:
- older: “Peak Ibn Sina (historically Lenin Peak)”;
- active: “Lenin Peak / Lenin Atyndagy Choku”, with the distinction that Tajikistan uses the official name Abu Ali Ibn Sina Peak.

The active wording distinguishes the names used on the two sides of the state border. The older title should not be restored mechanically; any historical-name note should be based on a checked cartographic or official source.

## 3. Material differences reviewed

The paragraph-level comparison surfaced exact-text differences where the active branch has rewritten, expanded, or updated older text. Selected substantive checks:

- **Chapter 02 and 05 — atmospheric composition:** the principal atmospheric proportions remain in the active text; older explanatory wording and table formatting were revised.
- **Chapter 06 — hydrological exercise:** the older basin exercise is no longer an exact paragraph match; the active chapter contains expanded water-balance and practical-analysis material. This is a wording/structure change, not evidence that the older exercise should be copied verbatim.
- **Chapter 17 — Kyrgyzstan's area and geology:** the older rounded area figure (199.9 thousand km²), named mining areas (including Kumtor, Makmal, Jerooy, Taldy-Bulak, Kadamjay and Haidarkan), and the distinction between occurrence, resource and reserve are retained and expanded. The active text adds the more precise 199,951 km² figure and an access date. Its source list is expanded.
- **Chapter 20 — Issyk-Kul:** older morphometric figures (about 1,607 m, 6,200 km² and 178 km) were replaced by figures attributed to the National Water Resources Management Plan (about 1,609 m, 6,280 km² and 177 km). Maximum depth (about 668 m) remains. This is an update, not a missing-data case.
- **Chapter 21 — biodiversity:** the 2025 national biodiversity programme to 2040 (NBSAP) and relevant international conservation references remain represented in the active chapter.
- **Chapter 22 — protected areas:** the active chapter retains and refines the older statistics: 23 state reserves and nature parks; 1,305.5 thousand ha in 2025; and the reported increase from 3.8% (2010) to 7.4% (2025). It adds a separate 2024 figure and explains why categories and dates must not be mixed.
- **Chapter 23 — settlements:** the older city examples (including Tokmok, Kara-Balta, Kyzyl-Kiya and others) remain represented in the expanded active chapter. Administrative and rural-settlement material has been reorganised.
- **Chapter 24 — seven regions:** the older caution about proposed administrative reform and the need to date boundaries remains part of the active chapter's treatment. Older visual-production briefs were reorganised into the newer in-text visual-placeholder and register system.
- **Chapter 25 — transport and energy:** the active text retains the older road-network and transport-share context but distinguishes ministry estimates (up to 96% freight / 98% passenger) from the National Statistical Committee's 2025 transport statistics (over 80% freight and over 90% passenger). It retains the October 2026 electricity-plan figures (19.6 / 15.5 / 4.1 billion kWh) and explicitly notes the later 4.999 billion kWh import-plan figure and 2.922 billion kWh imported by 15 October; it warns against treating the inconsistent plans as a final balance.
- **Chapter 26 — environment and water:** the active text retains the NDC 3.0 targets and the 2025 water-use data, with more precise figures: abstraction 8,938.4 million m³, consumption 6,224.9 million m³ and irrigation/agricultural supply 5,821.1 million m³. The 21.9% safe-treatment figure for domestic wastewater is retained with its UN SDG 6.3.1 scope explained. National wastewater volumes are separately qualified.

The active chapter text also contains additional English-language sections, worked examples, explanations, caveats and sources. This audit compared repository text; it does not constitute a fresh scientific verification of every external source or a live validation of every URL.

## 4. Older branch-only commit history

Comparing `portal-foundation` with `workspace/geography` shows 80 commits unique to the older branch. The commit list up to the merge base was inspected:
- 25 of those commits created geography chapters 02–26;
- the remaining 55 concern Chemistry, Physics, Biology or shared portal work;
- the 25 geography chapter commits are represented by the corresponding paths and later expanded versions in `workspace/geography`.

No additional geography-only asset, dataset or chapter file was found in the older branch trees beyond those 25 chapters and the old index.

## 5. Important shared-document gap

The integration branch has two commits not present in `workspace/geography`:
- `28aea99dfe4786a2b35f79a63448cffae5c43ca6` — adds root-level `EDITORIAL_STANDARD.md`;
- `aecea18a4a3297d861f9d6bcbd171f3cf1f8d294` — updates root-level `PROJECT_REGISTRY.md` to require that standard before discipline work.

`EDITORIAL_STANDARD.md` is absent from the active geography branch, and its root `PROJECT_REGISTRY.md` is an earlier revision. These are project-wide files, not geography-specific assets. They were **not copied or modified** during this audit. They should be resolved through the project's integration process; meanwhile the standard should be consulted from `atlas-of-knowledge-integration` as the authoritative shared reference.

## 6. Conclusion and disposition

- `workspace/geography` is the most complete geography content snapshot among the branches compared.
- No old geography chapter or geography file needs to be restored from `portal-foundation` or `atlas-of-knowledge-integration`.
- Do not merge either older branch wholesale.
- Do not restore the old chapter 18 peak title without authoritative naming verification.
- Resolve the missing shared editorial standard and newer project registry at the project-integration level, not by editing common root files from the geography workspace.
- No source branch was deleted, merged, or rewritten.

**Audit status:** branch and chapter inventory comparison complete; selected material differences reviewed. Full external-source verification, live URL checking, and a fresh scientific sign-off remain separate tasks.
