# Atlas of Biology

Third subject area of the unified **Atlas of Knowledge** portal.

## Visual production checkpoint — 4 November 2026
- 45 of 53 mapped illustration briefs are produced or integrated (84.9%); 8 remain deferred or pending. The authoritative per-asset status and evidence are in [IMAGE_DISPOSITION_REGISTER.md](IMAGE_DISPOSITION_REGISTER.md).
- Added the original bilingual `fauna-invertebrates.svg` comparison plate to the Kyrgyzstan fauna chapter. It distinguishes insect and arachnid body plans and does not claim to be a regional species inventory.
- Added the bilingual `systematics-tree.svg` teaching diagram to the systematics chapter: nodes, branches, sister groups, the A+B clade, and a rotated equivalent tree.
- Added `evolution-homology.svg` to the evolution chapter, comparing homologous tetrapod forelimbs and analogous bird/insect flight wings.

## Languages and design
- Russian and English versions are available on every page.
- Visual system follows the shared Atlas design: warm paper background, editorial serif headings, restrained green accent, compact monospace labels, responsive cards.
- Scientific explanations are written for learning, with key concepts, structured topic lists and knowledge checks.
- Interactive elements must be scientifically accurate, keyboard-accessible where practical, and usable on mobile.
- The manual [screen-reader and real-device test plan](SCREEN_READER_AND_DEVICE_TEST_PLAN.md) is prepared; all hands-on NVDA, TalkBack, VoiceOver and physical-device checks remain pending.

## Structure
- `index.html` — Biology landing page, subject navigation and interactive eukaryotic-cell model.
- `chapters/botany.html` — Botany, with bilingual learning objectives, a field glossary and a regional flora feature link.
- `chapters/flora-kyrgyzstan.html` — Regional bilingual flora chapter: altitudinal vegetation belts, forest ecosystems, characteristic plant profiles, conservation themes and research sources.
- `chapters/zoology.html` — Zoology, with bilingual learning objectives, a field glossary and a regional fauna feature link.
- `chapters/fauna-kyrgyzstan.html` — Regional bilingual fauna chapter: habitat gradients, mountain mammals, birds and migration, freshwater ecosystems, conservation and research methods.
- `chapters/cell-biology.html` — Cell biology and cytology.
- `chapters/anatomy.html` — Human anatomy and physiology.
- `chapters/genetics.html` — Genetics.
- `chapters/microbiology.html` — Microbiology.
- `chapters/ecology.html` — Ecology.
- `chapters/evolution.html` — Evolutionary biology.
- `chapters/biochemistry.html` — Biochemistry.
- `chapters/systematics.html` — Systematics and classification.

## Current foundation
- Biology has been added as Subject 03 to `portal.html`.
- Ten bilingual chapter pages have been created.
- Each chapter has a topic outline, explanatory text, bilingual learning objectives, a five-term field glossary, and a bilingual multiple-choice knowledge check.
- The landing page includes a selectable SVG cell model and a bilingual self-check question.
- Original responsive vector science plates have been added to Botany (flowering plant morphology), Zoology (major vertebrate groups), Cell Biology (prokaryote/eukaryote comparison), and Genetics (DNA double helix).
- Botany includes an interactive plant-organ learning module covering root, stem, leaf and flower. The chapter also has four bilingual learning objectives and a five-entry glossary covering chloroplasts, xylem, phloem, stomata and angiosperms.
- Botany now includes a bilingual chloroplast diagram and an interactive photosynthesis model. Learners can toggle light, water and carbon dioxide availability and observe how limiting inputs affect the process.
- The botany chapter includes the overall oxygenic photosynthesis equation and distinguishes light-dependent reactions in thylakoid membranes from the Calvin cycle in the stroma.
- Genetics includes an interactive DNA complementary base-pairing module (A–T and G–C).
- Genetics now presents the central dogma with an original bilingual information-flow plate, selectable DNA template-to-RNA transcription examples, a codon-to-amino-acid explorer, and mutation consequence demonstrations (substitution, insertion and deletion).
- Microbiology now includes an original bilingual comparison plate for a bacterial cell and a virus, an interactive comparison of Bacteria, Archaea and viruses, a bacterial cell-shape explorer, and a selectable bacterial population growth-curve module.
- Ecology now includes an original bilingual ecosystem trophic-flow plate, a guided food-chain builder, interactive carbon- and nitrogen-cycle explainers, and a qualitative ecosystem-pressure explorer covering drought, pollution, invasive species and conservation.
- Evolutionary Biology now includes an original bilingual phylogenetic branching plate, a natural-selection frequency model, interactive mechanism comparisons (selection, drift, gene flow and mutation), homologous/analogous structure comparisons, and a geological life-timeline explorer.
- Biochemistry now includes an original bilingual biomolecule-class plate, interactive enzyme–substrate compatibility and enzyme-activity factor explainers, ATP hydrolysis/synthesis comparison, and a cellular-respiration stage explorer (glycolysis, citric acid cycle and electron transport chain).
- Systematics now includes an original bilingual three-domain overview, an interactive taxonomic-rank explorer, comparisons of Bacteria/Archaea/Eukarya, binomial-name examples, and a branching identification-key activity.
- Zoology includes an interactive bilingual explorer for fish, amphibians, reptiles, birds and mammals, comparing body covering, respiration and reproduction while noting group-level exceptions. Its learning objectives and glossary cover core zoological concepts, vertebrates, invertebrates, heterotrophy, metamorphosis and adaptation.
- Anatomy and Physiology includes an original bilingual SVG overview of major organ systems and an interactive explorer for circulation, respiration, digestion, nervous function and urinary function.
- The anatomy chapter explains homeostasis and negative feedback, with a bilingual knowledge check on the left ventricle and systemic circulation.
- Cell Biology now includes a bilingual animal-cell vector plate and interactive organelle guide (nucleus, mitochondria, ribosomes, ER, Golgi apparatus and membrane).
- Cell Biology includes an interactive comparison of simple diffusion, osmosis and active transport, plus a bilingual mitosis stage explorer (interphase, prophase, metaphase, anaphase and telophase).

## Next development stages
1. Scientific review and expansion of chapter content with references and terminology.
2. Expand original botanical, zoological, anatomy, DNA and ecology illustrations.
3. Interactive models: plant transport, deeper animal classification, genetics and ecosystems.
4. Larger question banks, chapter progress and review activities.
5. Responsive and cross-browser testing, accessibility review and link validation.
6. Integrate the Biology section into the unified portal release after Physics and Chemistry are ready.

## Course navigation and integration
- All ten chapter pages now include consistent sequential navigation: previous chapter, all chapters/course overview, and next chapter. The navigation labels switch with the RU/EN page language and adapt to narrow screens.
- The chapter sequence follows the learning path: Botany → Zoology → Cell Biology → Anatomy & Physiology → Genetics → Microbiology → Ecology → Evolution → Biochemistry → Systematics.
- This navigation pass was checked structurally across all ten HTML pages. It is not a substitute for full browser, keyboard-only, and mobile-device testing.

## Regional biodiversity feature: Kyrgyzstan
- After the global foundations of Botany and Zoology are complete, add a substantial dedicated section on the flora of Kyrgyzstan to Botany and a corresponding section on the fauna of Kyrgyzstan to Zoology.
- The first dedicated regional flora chapter is now created at `chapters/flora-kyrgyzstan.html`. It introduces altitudinal vegetation belts, walnut-fruit, spruce, juniper and riparian woodlands, selected wild plant profiles, conservation pressures, research methods and source links. It is an initial scholarly foundation; detailed verified species accounts, distribution maps, photographs and region-by-region inventories remain future work.
- The fauna section is planned to cover major animal groups, characteristic mammals and birds, endemic and rare species, habitats and migration, protected areas and conservation.
- These will be full bilingual regional chapters within the relevant subject pages, supported by maps, original diagrams, species profiles and carefully sourced information. They will be developed after the global subject foundations, and coordinated with the dedicated Kyrgyzstan geography section in the Geography atlas.

- Both regional chapters now include coordinated seven-oblast landscape frameworks for planning deeper species inventories. These tables are explicitly introductory geographic guides, not exhaustive species distributions; future species records must be supported by georeferenced observations, dated surveys, herbarium vouchers or scientific sources.
- The regional chapters link to the Ministry's official protected-area directory and the UNDP account of the State Programme on Biodiversity Conservation until 2040 (endorsed at a national workshop in November 2025).

## Regional biodiversity field dossiers — Jalal-Abad
- The Kyrgyzstan flora chapter now contains a bilingual four-site dossier for Arslanbob, Sary-Chelek, Besh-Aral and Padysha-Ata. It distinguishes regional presence, reserve records and plot-level field observations; includes peer-reviewed walnut-forest research and 2022 vegetation monitoring published in 2025; and flags historical Red Data Book references for rechecking against the current edition.
- The fauna chapter now contains a corresponding bilingual dossier for Besh-Aral, Sary-Chelek and Padysha-Ata, with a sourced profile of Menzbier's marmot, habitat/connectivity context for snow leopard, and explicit treatment of inventory-date and survey-method limitations.
- Sources added include UNESCO's Sary-Chelek MAB profile, a 2015 walnut-fruit forest study, a 2025 vegetation-monitoring paper, the Kyrgyz Ministry's 2025 Besh-Aral notice, UNEP-WCMC's Western Tien Shan datasheet and UNDP's 2023 protected-area review.
- These are regional foundations, not complete oblast checklists. Exact distributions, current conservation categories, abundance estimates and coordinates remain subject to taxonomic review and dated field evidence.

## Regional biodiversity field dossiers — Issyk-Kul
- The flora chapter now includes a bilingual regional dossier covering eastern lake deltas and wetlands, western dry foothills, Terskey Ala-Too spruce forests and the Sarychat-Ertash highlands. Plant records are framed at habitat/genera level where a complete locality-specific checklist is not available.
- The fauna chapter now covers the proposed Kushtar micro-reserve bird observations reported in September 2026, Ramsar importance of Issyk-Kul for waterbirds, the FAO-supported fish-population study reported in December 2024, and the distinct high-mountain context of Sarychat-Ertash.
- The 2026 Kushtar count is explicitly treated as a dated event observation, not an annual population estimate; Kushtar is described as a proposed micro-reserve. Historical Ramsar and KBA inventory figures are dated and not presented as current annual counts.
- New references include UNESCO MAB, Ramsar site no. 1231, Key Biodiversity Areas site factsheets, FAO, CAMP Alatoo and peer-reviewed lake-basin research.
- Current fish totals and endemism estimates remain provisional pending publication of an updated, taxonomically reviewed checklist.

## Regional biodiversity field dossiers — Naryn
- The flora chapter now contains a bilingual dossier on Son-Kul wetlands and meadows, the saline Chatyr-Kul basin, Schrenk spruce forests in Naryn Nature Reserve, and the At-Bashy/Arpa highland vegetation mosaic.
- The fauna chapter covers the 2025 CAMCA survey estimate for Tien Shan maral in the Naryn River valley, snow leopard habitat and ecological connectivity, and wetland birds of Son-Kul and Chatyr-Kul.
- Ramsar site descriptions are treated as dated site information, not current annual counts. The maral estimate is limited to the surveyed Naryn River valley; the wider regional snow leopard estimate is not represented as a reserve-only count.
- References include CAMCA, Ramsar Sites Information Service, FAO/CAMP Alatoo, a 2023 waterbird study, and the Kyrgyz Ministry's 2025 Naryn reserve expedition notice.
- Species lists and totals remain subject to current taxonomic review, survey effort and locality-specific field evidence.

## Regional biodiversity field dossiers — Osh
- Flora: added a bilingual overview of Kulun-Ata Nature Reserve, Kyrgyz-Ata juniper belt, southern walnut-fruit forests, and the Alay/Chon-Alay highlands.
- The Kulun-Ata plant totals are explicitly contextualised: a 2026 Osh State University expedition reports 808 species, while a 2026 literature review cites about 394 vascular plant species and flags outdated taxonomy in source lists. These are not presented as directly comparable inventories.
- Fauna: added camera-trap records from Kulun-Ata reported by the Ministry on 28 August 2026 (Tien Shan brown bear, snow leopard and ibex), plus habitat-based notes for forest mammals, high-mountain ungulates and raptors.
- The dossiers distinguish confirmed monitoring records from broader regional habitat associations and avoid presenting presence records as population estimates.
- Sources include the Kyrgyz Ministry of Natural Resources, Osh State University, the National Academy of Sciences journal, Osh Technological University, IICAS and World Bank environmental assessments.

## Learning framework
- All ten subject chapters now include bilingual learning objectives and concise bilingual glossaries, placed before the knowledge check and styled responsively.
- The objectives describe expected learner outcomes; glossaries define core terms in context. These sections are an introductory framework and will be expanded during scientific review.

## Next quality-assurance phase
- Verify every interactive control in both languages, including keyboard operation and state updates.
- Review scientific wording, diagrams, dates, terminology and citations/recommended reading.
- Test all internal links, portal integration, mobile layouts and browser console output.
- Expand knowledge checks into topic-level assessment sets and add learning objectives/glossaries to all remaining chapters. Botany and Zoology now provide the bilingual model sections.


## Regional flora chapter — first implementation
- A standalone bilingual regional chapter has been added and linked from Botany.
- The chapter includes an original schematic altitudinal vegetation profile, an indicative vegetation-belt table, forest ecosystem profiles, selected botanical portraits, conservation pressures and methods, and an initial source list.
- Altitudinal limits are explicitly presented as variable rather than universal. Species totals and endemicity percentages are not stated as fixed values without a defined checklist and method.
- The page has responsive layouts, RU/EN switching, a skip link, semantic headings and a text-based source list. Structural verification is required; full browser and mobile testing remains pending.

## Regional fauna chapter — first implementation
- Both regional chapters now style their bottom navigation consistently and include an official Ministry of Natural Resources notice dated 9 June 2026: the Kyrgyz Red Data Book is being revised jointly with the National Academy of Sciences over a 24-month period. Species totals and national conservation lists must therefore be presented with edition/date context rather than as timeless current figures.
- A standalone bilingual regional chapter has been added and linked from Zoology.
- The chapter includes an original schematic habitat profile, an indicative habitat/fauna table, species profiles for characteristic mountain and forest mammals and birds, freshwater ecology, conservation threats, ecological connectivity and field methods.
- Taxonomic complexity is acknowledged for argali populations; national Red Data Book categories are not conflated with global IUCN assessments.
- The page references CMS/CAMI, UNEP, CBD and conservation organisations. Its structure, responsive layout, language switch, skip link and source links require final validation; full browser and mobile testing remains pending.

## Final static validation — 31 October 2026
- Audited the 13 Biology HTML pages against the complete Git branch tree; all relative/local links resolve to files in the branch.
- Checked the 12 chapter pages for duplicate HTML IDs and balanced section, article, div and paragraph tags; no duplicate IDs or count mismatches were found.
- Parsed all 13 inline JavaScript blocks with the JavaScript engine; all scripts passed syntax compilation.
- Checked static DOM references and data-attribute hooks used by the interactive modules; no missing element IDs or missing data hooks were identified.
- Confirmed viewport metadata, responsive media-query rules and RU/EN display styles across the chapter pages.
- Added explicit `type="button"` to every button in the Biology portal and chapter pages, including dynamically generated quiz answers; a second pass confirms zero buttons with an implicit submit type.
- This is a static source audit, not a substitute for live browser testing. Cross-browser interaction, keyboard-only operation and real-device mobile rendering still require deployment/browser verification.

## Knowledge checks

All ten global Biology chapters now include a bilingual five-question knowledge check (50 questions in Russian and 50 in English across the atlas). Each item provides three answer choices and explanatory feedback; learners can move through the set, see their running score, and restart the quiz. The language switch refreshes the active question and choices.


## Regional biodiversity field dossiers — Talas
- Added bilingual Talas Region profiles to both Kyrgyzstan flora and fauna chapters, centred on Besh-Tash State Nature Park and the northern Talas Ala-Too.
- Flora coverage distinguishes mountain spruce/juniper woodland, riparian habitats, alpine meadows and KBA trigger plant taxa; the reported figure of 800+ higher plants is treated as a richness summary, not a complete checklist.
- Fauna coverage records Ministry camera-trap detections of snow leopard, argali and ibex (September 2025), the dated Ministry maral estimate (60 in September 2025, with the 2022 Altai reintroduction disclosed), and the regional 2026 marmot count (29,367 across several survey areas, not Besh-Tash alone).
- Sources include the Kyrgyz Ministry of Natural Resources, Kabar and the Besh-Tash Key Biodiversity Area profile. Survey results are carefully scoped by place, date and method; presence records are not presented as population estimates.


## Regional biodiversity field dossiers — Chuy
- Added bilingual Chuy Region dossiers to the Kyrgyzstan flora and fauna chapters, covering Ala-Archa, the Kyrgyz Range, Chon-Kemin and the Chuy Valley.
- Flora coverage explains valley-to-alpine vegetation belts, juniper and spruce woodland, steppe communities and rare plant taxa reported for Chon-Kemin; older species totals are explicitly treated as indicative rather than definitive inventories.
- Fauna coverage adds dated 2026 reports from Ala-Archa and Chon-Kemin, including NABU/park camera-trap detections and the Ministry's Kök-Oyrok monitoring notice. Detections are not misrepresented as population estimates.
- Sources include the Kyrgyz Ministry of Natural Resources, Kabar, Turmush/NABU, Chon-Kemin park profiles and a Chuy vegetation overview.


## Regional biodiversity field dossiers — Batken
- Added bilingual Batken Region profiles to both Kyrgyzstan flora and fauna chapters, covering Aygul-Tash and *Petilium eduardii*, wild tulip conservation, juniper slopes, dry foothills, Surmatash and Sarkan protected landscapes.
- Fauna coverage includes the dated 30 June 2026 spring marmot survey (4,146 records across surveyed areas, including Surmatash); the source does not identify the marmot species, so the chapter retains *Marmota* spp. and does not treat the result as a population estimate for the whole oblast.
- Rare-plant locality details are handled cautiously; sensitive coordinates are not published as general visitor information.
- Sources include the Kyrgyz Ministry of Natural Resources, World Bank environmental assessments and the 2021 Kojo-Kaiyr environmental examination.

## Seven-oblast coverage and evidence standard
- The flora and fauna regional chapters now contain introductory landscape frameworks for all seven oblasts: Batken, Jalal-Abad, Issyk-Kul, Naryn, Osh, Talas and Chuy. Dedicated dossiers are provided for each oblast; these are regional learning profiles, not exhaustive biodiversity inventories.
- Records are distinguished by evidence type: published checklist, dated field observation, camera-trap detection, habitat association or provisional estimate. A presence record is never presented as an abundance estimate.
- Species names and conservation categories require current taxonomic and national/global status checks. The Ministry and National Academy of Sciences began a 24-month Red Data Book revision in June 2026; the Institute of Biology described the planned field, taxonomic, mapping and digital-database work in October 2026.
- Official reference: Ministry of Natural Resources, 9 June 2026, [Red Data Book revision announcement](https://mnr.gov.kg/ru/posts/news/ministerstvo-prirodnyx-resursov-ekologii-i-texniceskogo-nadzora-kyrgyzskoi-respubliki-sovmestno-s-nacionalnoi-akademiei-nauk-pristupaet-k-rabote-po-obnovleniyu-krasnoi-knigi). Further project details: [Institute of Biology, NAS KR, 14 October 2026](https://ibnaskr.org/red-data-book-kyrgyzstan-project-2026-2028/).


## Mainline integration and publication — 31 October 2026

The bilingual Biology Atlas was integrated into `main` through pull request #3 (merge commit `e48c8e63aac0d8e79fb75895c5311ded331e70e9`). The unified portal now links to the Biology Atlas in Russian and English. The release contains the ten global chapters, the Kyrgyzstan flora and fauna regional chapters, and the Biology README.

Release validation on the integration branch completed successfully: 13 Biology HTML pages passed static validation (78 local paths, 13 inline scripts, 163 explicitly typed buttons), and Chromium smoke tests passed at mobile (390 px) and desktop (1365 px) viewports, including language-toggle interactions and uncaught page-error checks. JavaScript validation also passed.

GitHub Pages deployment completed successfully for main commit `39fc80c4f03dd247af9dc3331501a30f2ef5698c` on 31 October 2026. Deployment run: https://github.com/Ajokendo/Atlas-of-Physics/actions/runs/41214973040. This confirms a successful Pages build and publish job; independent access from every browser/device should still be checked after publication.


## Scientific editorial standard and 2026 Red Data Book revision

- The project-wide bilingual scientific and editorial standard is maintained in [EDITORIAL-AND-SCIENTIFIC-STANDARDS.md](EDITORIAL-AND-SCIENTIFIC-STANDARDS.md). It applies to all chapter text, species profiles, maps, datasets, diagrams, interactive models and assessments.
- On 9 June 2026, the Ministry of Natural Resources announced a 24-month joint project with the National Academy of Sciences to update the Kyrgyz Red Data Book. The Ministry's announcement reports 89 higher-plant and fungi species, 23 mammals, 57 birds, 2 amphibians, 8 reptiles, 7 fish and 18 arthropods in the figures associated with the ongoing revision. These are announcement figures, not the completed results of the new assessment or a newly published edition.
- The flora and fauna chapters now explicitly distinguish project-announcement figures from verified species assessments. National Red Data Book status and IUCN categories remain separate systems and must be dated and sourced independently.
- The Institute of Biology of the National Academy of Sciences reported on 14 October 2026 that the revision is planned for 2026–2028 and includes field research, updated species accounts, maps and a digital database. The planned publication dates are not evidence that the new edition has already been released.
- Official references: [Ministry announcement, 9 June 2026](https://mnr.gov.kg/ru/posts/news/ministerstvo-prirodnyx-resursov-ekologii-i-texniceskogo-nadzora-kyrgyzskoi-respubliki-sovmestno-s-nacionalnoi-akademiei-nauk-pristupaet-k-rabote-po-obnovleniyu-krasnoi-knigi); [Institute of Biology, 14 October 2026](https://ibnaskr.org/red-data-book-kyrgyzstan-project-2026-2028/).


## Learner experience and editorial enrichment — 31 October 2026

- Added a bilingual “Start with wonder / A minute to explore” opening to all ten global chapters and both Kyrgyzstan biodiversity chapters. Each opening begins with a concrete everyday image or field situation, then invites learners to reveal an explanatory answer through a native keyboard-accessible disclosure control.
- The chapter hooks are subject-specific: plant systems, animal adaptations, cell organisation, coordinated body systems, gene expression, microbial diversity, food-web connections, evolution across generations, cellular chemistry, evolutionary classification, elevation-driven flora and habitat connectivity for wildlife.
- Added a bilingual learner-orientation panel to the Biology landing page, encouraging observation, questioning and model-based exploration rather than memorisation of isolated definitions.
- New blocks preserve the Atlas visual language, responsive layout and RU/EN language switching. They supplement existing scientific plates, interactive models, glossaries, learning objectives and five-question knowledge checks.
- Editorial principle for subsequent revisions: introduce a phenomenon in familiar language, explain the idea, then introduce the precise scientific term; use analogies as entry points and explain their limits. Do not remove necessary scientific vocabulary or overstate simplified models.
- This is a pedagogical enrichment pass, not a complete line-by-line scientific peer review. Expert review of specialist claims, species accounts, source freshness and terminology remains a separate quality-assurance task.

## Accessibility follow-up — 31 October 2026

- Improved the landing-page cell model for keyboard and assistive-technology users: each selectable organelle now receives a language-aware accessible name and points to the live description panel.
- Added a consistent visible keyboard-focus indicator for the SVG controls and clarified the Tab, Enter and Space interaction in both Russian and English.
- Preserved the existing model geometry, explanatory biology content, quiz behaviour and language toggle.
- Static source verification is recorded for this change; live screen-reader and browser/device testing remains part of the outstanding QA phase.


## Editorial and source pass — 31 October 2026
- Added bilingual selected-reference sections to all ten global foundation chapters: Botany, Zoology, Cell Biology, Anatomy and Physiology, Genetics, Microbiology, Ecology, Evolutionary Biology, Biochemistry, and Systematics.
- The selected references point to topic-matched OpenStax Biology, Microbiology and Anatomy & Physiology materials, plus the NCBI Taxonomy resource for nomenclature and lineage checks. Links were checked on 31 October 2026.
- The regional Flora and Fauna of Kyrgyzstan chapters were not changed in this pass; their existing source dossiers remain in place.
- Extended `checks.mjs` so the ten global foundation chapters must each contain a bilingual selected-references section with at least two external source links; the source-section rule was also checked against all ten current pages.
- This is a bibliography and traceability improvement, not a claim that every individual scientific statement has completed line-by-line peer review. Claim-level source mapping, terminology review and independent bilingual proofreading remain part of the next editorial stage.


## Editorial readiness baseline — 31 October 2026

**Working editorial readiness: 70/100.** This score applies only to the Biology branch and is a staged editorial estimate, not a claim of expert peer-review completion. Five equally weighted dimensions are used so later progress reports can be compared consistently:

| Dimension | Score | Basis |
|---|---:|---|
| Course structure and navigation | 18/20 | Landing page, ten global foundations, two regional chapters and sequential chapter navigation are present. |
| Russian–English editorial parity | 14/20 | Both language layers are present across the pages; independent proofreading and terminology harmonisation remain. |
| Learning design and content coverage | 16/20 | Learning objectives, glossaries, knowledge checks and multiple interactive models are in place; depth and assessment coverage still vary. |
| Scientific evidence and traceability | 10/20 | Regional dossiers have substantial sources and the ten global chapters now have selected references; claim-level citation mapping and expert scientific review remain. |
| Accessibility and technical quality assurance | 12/20 | Static checks cover page structure, local paths, script syntax and controls; live browser, mobile-device and screen-reader testing remain. |

The score should increase only when evidence for the relevant checklist items is recorded. The next priority is claim-level scientific/source review of the ten global chapters, followed by independent bilingual copy-editing and live accessibility testing.


## Scientific wording review — Genetics — 31 October 2026
- Clarified that not every gene encodes a protein: some genes produce functional non-coding RNAs, including rRNA and tRNA, and some regulatory RNAs. The clarification is bilingual and distinguishes the general DNA → RNA → protein model for protein-coding genes from the broader range of gene products.
- Added an NCBI Bookshelf reference on transcription and RNA classes. The change was checked for RU/EN parity, source presence, unique IDs and balanced script tags.
- This is a targeted conceptual correction, not a complete expert review of the Genetics chapter or the remaining Biology chapters.


## Scientific wording and interaction review — Ecology, Cell Biology and Biochemistry — 31 October 2026
- Ecology: made the food-chain builder enforce the intended trophic sequence (producer → primary consumer → secondary consumer → higher consumers). Out-of-order selections now prompt the learner instead of being appended into a misleading chain; selecting an earlier step truncates later choices. Added bilingual organism labels, `aria-pressed` state and a polite live status output.
- Biochemistry: clarified in both languages that enzymes lower activation energy and speed the approach to equilibrium, but do not shift equilibrium or change the overall Gibbs free-energy change (ΔG). Clarified that the actual ΔG of ATP hydrolysis in cells depends on reactant and product concentrations, while retaining the standard biochemical-condition statement.
- Cell Biology: reviewed the organelle, membrane-transport and mitosis explanations. The current text correctly distinguishes passive diffusion, osmosis and energy-dependent active transport; explains that interphase is not a mitotic stage; and treats nuclear-envelope breakdown as late prophase/prometaphase depending on staging convention. No wording change was required in this targeted pass.
- These are targeted scientific and interaction corrections, not a completed expert review of the three chapters. Live browser, keyboard and assistive-technology testing remains outstanding.

- Extended `biology/checks.mjs` with regression assertions for the ecology builder's ordered trophic choices, bilingual button labels and accessible live feedback, plus the biochemistry enzyme-equilibrium and cellular ATP ΔG qualifications.


## Language-state and interaction review — Botany and Genetics — 31 October 2026
- Botany: language switching now refreshes the selected organ explanation, photosynthesis-condition feedback and all condition-button labels while preserving the selected on/off state. The organ selector exposes its current selection through `aria-pressed` and returns to a translated prompt when no organ is selected.
- Genetics: the mutation explorer now retains the selected mutation across language changes, translates its explanation and control labels, and restores a translated introductory explanation when no mutation has been selected.
- The review also checked the active interactive outputs in Zoology, Anatomy & Physiology, Microbiology, Evolution and Systematics; their language-change handlers refresh the currently selected model output.
- This was a targeted interaction and wording pass. It does not replace full browser, keyboard-only and screen-reader testing.

- Extended the automated checks to guard against regressions in Botany's translated organ and photosynthesis state and Genetics' selected mutation state; corrected the food-chain button matcher so it checks actual button elements.


## Kyrgyzstan regional biodiversity source audit — 31 October 2026
- Reviewed the flora and fauna regional dossiers for all seven oblasts, their habitat descriptions, field-count caveats, Red Data Book status language and source lists.
- Confirmed the 30 June 2026 Batken marmot count against the Ministry's official notice: 4,146 animals were recorded (759 in the surveyed Batken-area sites and 3,387 in Surma-Tash Nature Reserve). The atlas appropriately treats this as a dated survey result, not a permanent region-wide population estimate; added the direct Ministry source.
- Confirmed that the Ministry's 9 June 2026 Red Data Book figures describe the ongoing 24-month revision project, not a completed new edition. The flora and fauna chapters preserve this distinction.
- Confirmed the current NCBI Taxonomy record for the Tian Shan maral name `Cervus canadensis songaricus`; it lists `Cervus elaphus songaricus` as a synonym. Added the taxonomic record as a reference, while retaining the current record's name in the chapter.
- Added the Ministry's 10 March 2026 notice on protection of Aygul-Tash and Madygen to the flora sources.
- This is a source-verification pass, not a complete species-by-species expert inventory. Taxon-level distribution and conservation status still require specialist review and dated locality evidence.


## Interactive language-state audit — Evolution, Microbiology and Systematics — 31 October 2026
- Evolution: selection-pressure, mechanism, homology and geological-timeline buttons now relabel on RU/EN switching. The selected model state is retained; all controls have explicit initial pressed states.
- Microbiology: domain/group, bacterial-shape and population-growth phase buttons now relabel on language switching while retaining the selected model state; initial pressed states are explicit.
- Systematics: classification-rank, domain, species-name and identification-key controls now relabel on language switching. The identification key restricts the next trait choices to the selected branch and clears a stale trait when the first branch changes.
- Added regression assertions for these language-state and branch-reset behaviors in `biology/checks.mjs`.
- Static source QA after the edits: 13 HTML pages, 13 inline scripts parsed successfully, 163 buttons all declare `type="button"`, and no duplicate HTML IDs were found. The repository's Node-based check script has not yet been executed in a Node runtime; no browser, keyboard-only or screen-reader run is claimed.

- Editorial refinement: the evolution model labels now identify predation pressure specifically (rather than implying generic selection pressure); the systematics key explicitly tells learners when one trait is insufficient for identification.


## Regional species-range evidence review — 31 October 2026
- Rechecked the Menzbier's marmot (*Marmota menzbieri*) profile in the Jalal-Abad / Besh-Aral section against the Kyrgyz Ministry's 10 March 2025 notice, the Mammal Diversity Database and published historical-range literature.
- The Ministry directly reports the species in Besh-Aral Reserve; the Mammal Diversity Database recognises Kyrgyzstan in the country-level range. Some older regional accounts disagree about particular Chatkal localities and fine-scale range boundaries. The chapter now distinguishes confirmed reserve-level occurrence from uncertain neighbouring localities and avoids extrapolating national presence to every valley.
- Added the Mammal Diversity Database taxon record and the 2016 Tokarsky, Atemasov & Shakula paper to the fauna source list.
- Rechecked the Aygul / *Petilium eduardii* profile and the Sievers' apple (*Malus sieversii*) discussion. The chapter retains the conservative wording: a documented local population at Aygul-Tash, current access restrictions to be verified before visits, and no simplistic claim that *M. sieversii* alone is the ancestor of all cultivated apples.
- The 2026–2028 Red Data Book revision remains a work in progress; no provisional status is presented as a completed official reassessment.


## Snow leopard evidence update — 1 November 2026
- Added the 2026 national status assessment of the snow leopard (*Panthera uncia*) in Kyrgyzstan to the regional fauna evidence base. The published 2026 scientific contribution summarises the proposed national IUCN range map, drawing on camera trapping, field surveys and community information across the Tien Shan and Pamir–Alai.
- Updated the western Tien Shan species profile to distinguish this nationwide evidence synthesis from proof of occurrence at a specific locality.
- Added the Ministry-attributed field-patrol record reported by Kabar on 14 October 2026: snow leopard, argali and ibex were observed in mountainous Issyk-Kul Region. The chapter labels this as a dated occurrence record and explicitly does not treat it as an abundance or density estimate.
- Added bilingual source annotations and regression checks for the new species evidence. No national population total or oblast-wide range claim was inferred from the event report.
- This is a targeted source update, not a completed expert review of all regional taxa. The working editorial readiness score remains 70/100 pending wider claim-level source mapping, independent bilingual editing and live accessibility/browser QA.


## Naryn regional fauna evidence update — 1 November 2026
- Added two official 2026 records: Ministry-reported camera-trap detections of brown bear and snow leopard in Naryn State Nature Reserve (2 September), and a regional patrol video of snow leopard and ibex from an unnamed valley in Naryn Region (30 September).
- Explicitly distinguished the Naryn Reserve camera-trap records from the unnamed-valley regional patrol footage; the latter is not assigned to the reserve because the source does not identify its locality.
- Clarified that the September camera-trap notice confirms detections but does not publish individual counts, sampling effort or density estimates.
- Corrected the mixed-script spelling of the protected-area name to the official Russian form «Каратал-Жапырык» and expanded the bilingual regional introduction.
- The regional audit remains in progress. No new population estimate was inferred from either notice; editorial readiness remains 70/100 pending claim-level review of all seven oblast dossiers, broader scientific source mapping, independent bilingual editing and live browser/accessibility QA.


## Argali and maral taxonomy and population-evidence audit — 1 November 2026
- Standardised the argali account at species level as *Ovis ammon* and clarified that subspecies boundaries within the argali complex remain disputed; the page no longer implies one uncontested subspecies assignment for all Kyrgyz argali.
- Added the Ministry's 10 December 2025 report with the correct scope: on 8 December, approximately 450–500 argali were recorded at two Sarychat-Ertash sectors, while about 900 were recorded in a separate hunting area. These are distinct first-day site records, not a national estimate or a single combined population figure.
- Corrected the Naryn maral chronology. The CAMCA estimate of 400–600 animals for the Naryn River valley and tributaries is based on the combined survey of 7–12 October 2024, which directly recorded 160 animals and extrapolated to account for unexamined habitat. The 15–20 September 2025 repeat census published preliminary positive findings but no final number; the 400–600 estimate is no longer attributed to that 2025 survey.
- Clarified the maral taxon as subspecies *Cervus canadensis songaricus*, with *Cervus elaphus songaricus* documented as a synonym in NCBI Taxonomy; source notes distinguish database nomenclature from final taxonomic authority.
- Clarified that Besh-Tash's 60 maral (Ministry notice, 19 September 2025) includes a group of 35 animals brought from Altai in 2022. This park population is not conflated with the naturally occurring Naryn and Issyk-Kul populations.
- Added bilingual source annotations and regression assertions for taxonomy, dated survey scopes, the 2024/2025 maral chronology and the Besh-Tash introduction history.
- This remains a targeted evidence audit, not a completed expert review of every mammal record. Editorial readiness remains 70/100 pending broader claim-level source mapping, independent bilingual editing and live accessibility/browser QA.



## Argali genetic evidence update — 1 November 2026
- Added the March 2026 Kyrgyz argali population-genetics study (72 samples, 135,242 SNP markers) to the regional dossier and source list.
- Reported the study's result narrowly: no clustering corresponding to discrete subspecies was detected within the sampled population. The chapter explicitly notes that this sample does not cover every Kyrgyz population and does not settle all regional taxonomic hypotheses.
- Added a regression assertion to preserve the sample size, marker count and geographic-scope caveat. The species-level name remains *Ovis ammon*; subspecies assignments remain qualified rather than silently treated as settled.
- Editorial readiness remains 70/100: this strengthens one species dossier but does not replace the broader seven-oblast source audit, independent bilingual editing or live browser/accessibility QA.
- Expanded the maral audit after reading the CAMCA concept note itself: it lists 689 animals for Kyrgyzstan in 2024, while the National Statistics Committee's open series lists 47 for 2024 and 61 for 2023. The chapter now presents these as conflicting, unreconciled series and does not add or average them; the 400–600 Naryn-valley estimate remains a separate 2024 field-survey extrapolation.
- Added the CAMCA/IUCN taxonomic qualification: NCBI lists *Cervus canadensis songaricus* as a subspecies with *C. elaphus songaricus* as synonym, whereas the CAMCA note says the IUCN Red List places it within *C. c. sibiricus* and questions whether it is a clearly distinct subspecies. The atlas preserves this disagreement rather than asserting a settled rank.
- Extended regression checks to protect both the conflicting population series and the taxonomic qualification.
- Refined the genetics summary after checking the full 2026 paper: 88 samples were initially collected in Kyrgyzstan, 72 passed quality control, and the analysis found no genomic support for separating *O. a. polii* and *O. a. karelini* in the sampled Kyrgyz region. The study did not include Pamir Plateau samples, so its conclusion is explicitly bounded.
- Added the Kyrgyz National Statistics Committee's ungulate series as a separate evidence stream: 47 maral in 2024 and 61 in 2023. These official statistical figures differ markedly from CAMCA's 400–600 Naryn-valley extrapolation; the atlas now flags the differing scopes/methods rather than combining or silently choosing one series.


## Maral estimate comparability note — 1 November 2026
- Cross-checked the detailed CAMCA October 2024 survey report against its 2025 Kyrgyzstan concept note. The detailed report records 160 animals and extrapolates 400–600 for the Naryn River valley and tributaries; the concept note separately lists 689 for Kyrgyzstan in 2024.
- The chapter now displays this difference and explains that the brief concept-note table does not document method and spatial coverage at the same level. The two figures are not treated as directly comparable or silently merged.
- Added the concept note to the bilingual source list and a regression assertion preserving the comparability caveat. Readiness remains 70/100.


## Naryn snow leopard survey-scope update — 1 November 2026
- Added the peer-reviewed 2021 camera-trap study from Naryn State Nature Reserve (four field seasons, 2016–2019): a minimum of five adult snow leopards were identified, together with five cubs or subadults from three litters of two females.
- Distinguished this local, minimum-detection result from CAMCA's approximately 62-individual estimate for the wider Naryn region. The two figures refer to different spatial scopes and study designs and must not be interpreted as a population trend or direct cross-check.
- Added a regression assertion preserving the local-study period, minimum adult count, evidence of reproduction and the geographic-scope caveat. Editorial readiness remains 70/100; one stronger species account does not close the seven-oblast evidence audit or outstanding independent and live QA.


## Tian Shan brown bear taxonomy note — 1 November 2026
- Reviewed the regional name *Tian Shan brown bear* against CAMCA's use of *Ursus arctos isabellinus*, the Mammal Diversity Database's species-level treatment of *Ursus arctos* and nomenclatural history, and the 2019 Central Asian brown-bear phylogeography paper.
- Kept *Ursus arctos* as the unambiguous species-level heading and qualified *U. a. isabellinus* as a regional subspecies designation used by conservation sources, rather than implying that all taxonomic frameworks treat Central Asian forms identically.
- Added source references and a regression assertion to preserve this qualification. Editorial readiness remains 70/100 pending broader review, independent bilingual editing and live QA.

## Naryn high-lake bird evidence audit — 1 November 2026
- Expanded the Son-Kul bird profile using the OSME-published 2019 field account: approximately 70 species were reported for the lake and adjacent area; the project covered breeding and passage birds and identified six focal species. The chapter now records the 2019 account's observations on Bar-headed Goose and Demoiselle Crane as dated historical findings, not current counts.
- Expanded the Chatyr-Kul profile using the Ramsar Information Sheet completed in 2004 and updated in 2005. The historical moulting concentrations of Ruddy Shelduck and other ducks are explicitly dated and are not presented as current annual population estimates.
- Added direct source links for the OSME 2019 field account, Son-Kol Ramsar Information Sheet (2010), Chatyr-Kul Ramsar Information Sheet (2004/2005), and the historical 2003 Son-Kul wetland-bird survey.
- Verified that the Russian and English passages preserve the same dates, species, scope limitations and conservation pressures. The source links are present in the branch file; live browser/device testing remains outstanding.
- Added an explicit comparability note: the 2003 Son-Kul survey's 41 wetland/water-associated species and the 2019 account's approximately 70 species for the lake plus adjacent land have different taxonomic and spatial scopes and are not a population trend.
- Current working editorial readiness: **71/100**. The scientific evidence and traceability dimension moves from 10/20 to 11/20 for this documented source-level improvement in the Naryn bird dossier. This is a staged editorial-readiness score, not a completion percentage or expert peer-review certification. Remaining work includes broader claim-level review across all chapters, independent bilingual copy-editing, and live browser, mobile, keyboard and screen-reader QA.

## Naryn ichthyofauna and reserve-inventory update — 1 November 2026
- Added a bilingual account of Son-Kul fish based on Sarieva, Konurbaev & Osmonov (2023), drawing on Institute of Biology NAS KR field visits from 2020–2023. The entry distinguishes introduced whitefish and peled from other recorded fish taxa and includes the study's reported concerns about weak juvenile representation, fishing pressure and possible egg predation.
- Explicitly distinguished fish-bearing Son-Kul from fishless Chatyr-Kul as described in the latter's 2004–2005 Ramsar Information Sheet. The text avoids treating the study's historical catch observations as a current whole-lake population estimate.
- Added the 25 August 2025 reserve inventory published by 24.kg: 26 mammals, 104 birds, 3 fish, 4 reptiles and 1 amphibian species in Naryn State Nature Reserve (105,519 ha). The dated source and non-exhaustive/current-inventory caveat are stated.
- Added the Ministry's 14 July 2026 report of route-based bird surveys at Karatal and Son-Kul, and its 21 September 2026 report on the Batai-Aral observation tower. The chapter distinguishes monitoring activity and visitor infrastructure from published abundance results.
- Added direct sources and regression checks for the bilingual fish account, the lake-to-lake ecological distinction, reserve inventory date/scope, and 2026 ornithology updates.
- Current working editorial readiness: **72/100**. One point added for this traceable improvement to regional taxonomic coverage and current evidence. This remains a staged editorial-readiness score, not a completion percentage or expert peer-review certification. Outstanding work includes species-level verification across all seven oblasts, independent bilingual copy-editing, and live browser, mobile, keyboard and screen-reader QA.


## Naryn fish-source precision and reserve-area update — 1 November 2026
- Rechecked the full 2023 Son-Kul fisheries paper, not only its abstract. Corrected the fieldwork description: the abstract summarizes visits as 2021–2023, while the methods section specifically lists 2020, 2021 and 2023. The bilingual account now preserves this source-internal distinction rather than flattening it to an imprecise date range.
- Corrected a geographic error: Kok-Jerty is the river flowing out of Son-Kul, not a tributary flowing into the lake. The four osman/loach/minnow taxa recorded in September 2023 are now explicitly assigned to this outlet river, separate from the lake fish discussed in the paper.
- Added the Kyrgyz Ministry's 15 July 2026 notice. It gives the Naryn State Nature Reserve area as 112,363.5 ha and repeats the inventory of 26 mammal, 104 bird, 3 fish, 4 reptile and 1 amphibian species. The older 105,519 ha figure is retained only as the area reported in the 25 August 2025 notice; the newer official figure is identified as the latest available.
- Added the official Ministry source and recorded these source-scope corrections. Editorial readiness remains **72/100**: this is a precision correction to the preceding Naryn evidence update, not an additional breadth point. Independent bilingual editing and live browser/device/accessibility QA remain outstanding.


## National Red Data Book scope clarification — 1 November 2026
- Added a dated bilingual note based on the Ministry's 2 September 2026 notice: revision of the Red Data Book was still under way, while the then-current list was described as covering 23 mammals, 57 birds, 7 fish, 10 amphibians and reptiles combined, and 18 arthropods.
- Clarified that the combined figure of 10 does not mean ten species in each of the two groups, and that national Red Data Book totals are not directly comparable with an inventory for an individual protected area.
- Added the primary government source. The counts are explicitly dated and are not presented as the result of the unfinished revision.
- Editorial readiness: **73/100**. One point added for a traceable improvement in conservation-status interpretation and numerical comparability. This remains a staged editorial-readiness score, not a completion percentage or external certification. Independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA remain outstanding.


## Naryn reserve mammal coverage — 1 November 2026
- Expanded the Naryn regional dossier with three additional species explicitly named by the Ministry in its 15 July 2026 reserve update: Pallas's cat (*Otocolobus manul*), Eurasian lynx (*Lynx lynx*) and argali (*Ovis ammon*).
- Cross-checked scientific names against the American Society of Mammalogists' Mammal Diversity Database and the CMS Central Asian Mammals Initiative. The entry distinguishes official presence records from population estimates: the Ministry notice gives no counts or trend data for these species.
- Added direct taxonomy and conservation references and synchronized Russian and English wording.
- Editorial readiness: **74/100**. One point added for a documented increase in species-level coverage of the Naryn fauna. Remaining work includes the wider seven-oblast claim audit, independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA.


## Naryn maral conservation measures — 1 November 2026
- Added a bilingual species-conservation profile documenting the Naryn Reserve maral breeding centre: the Ministry reported that its fenced area had reached 82 ha by 15 July 2026 after a 32 ha expansion, and that nine captive-raised deer were transferred to Avletim Forestry in 2018.
- Explicitly distinguished a documented transfer between institutions from proof of successful wild-population recovery. The text identifies the survival, reproduction and follow-up monitoring evidence that would be needed to make that stronger claim.
- Linked the profile to the existing primary Ministry source and synchronized Russian and English wording.
- Editorial readiness: **75/100**. One point added for a traceable improvement in species-conservation history and interpretation of management outcomes. This is a staged editorial-readiness score, not a completion percentage or external certification. Independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA remain outstanding.


## Regional fauna audit and protected-area enforcement update — 1 November 2026
- Expanded the Naryn snow-leopard dossier with the documented OSI-Panthera monitoring protocol: sign surveys, scat sampling for genetic analysis, camera-trap photo-identification, prey observations and other-predator sign records. Clarified that detailed seasonal reports (including Naryn 2016–2025) are not openly published because they contain sensitive local-species information; public notices therefore do not support independent recalculation of abundance.
- Added a dated Chuy-region account of the 27 camera traps installed in Shamshy-Tuyuk on 15–21 September 2025 with Kyrgyz and Japanese research partners, and a separate Ak-Suu reserve camera-trap record. Both entries distinguish survey effort/detections from an abundance estimate.
- Added the Ministry's Besh-Aral protected-area checklist (46 mammal and 150 bird species, reported 10 March 2025), explicitly labelling it as a dated reserve inventory rather than a population count or an oblast-wide total.
- Refined the Talas 2026 census interpretation: the 29,367 marmots are a combined result from four named sites; muskrats were also surveyed but no separate total was published, and no site-by-site allocation of marmots was supplied.
- Added the national 2025 protected-area enforcement context: 139 detected violations overall, including 14 wildlife-related cases with reported damage of KGS 125,270. The text explicitly identifies this as administrative detection data, not a complete estimate of poaching or wildlife mortality.
- Editorial readiness: **80/100**. Five points since the 75/100 checkpoint reflect five documented improvements: monitoring-method transparency, Chuy field coverage, Besh-Aral inventory scope, Talas census interpretation, and national protected-area enforcement context. This remains a staged editorial-readiness score, not a completion percentage or external certification. Independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA remain outstanding.


## Fish biogeography and herpetofauna audit — 1 November 2026
- Expanded the freshwater chapter from a habitat overview into a basin-based fish account. Added the seven aquatic biogeographic systems discussed by Kustareva and Naseka (2015), and made explicit that drainage basins do not follow oblast boundaries.
- Added the review's reported endemism estimates (up to 70% for Issyk-Kul and 55% for the Talas system) with a clear date/taxonomy caveat; distinguished native fish from introduced species and fisheries/aquaculture pressures.
- Clarified the status of the 2026 Institute of Biology–American Museum of Natural History fieldwork: fish material was collected in Issyk-Kul, Chu and Talas basins and initially identified, while laboratory processing and analysis were still ongoing on 14 October 2026. No unpublished results or species-level basin records are inferred.
- Added a dedicated bilingual amphibian and reptile section. It separates the 2015 reference chapter's historical totals (four amphibians and 37 reptiles) from the Ministry's 2026 national protected-list counts (two amphibian taxa), and explains why those numbers are not competing estimates of the same thing.
- Added the 2026 GBIF Central Asian amphibian checklist as a modern taxonomic compilation, not a field census; expanded explanation of range-edge populations, habitat fragmentation, breeding/overwintering sites and the need for georeferenced records before drawing oblast-level distribution maps.
- Editorial readiness: **85/100**. Five points since 80/100 reflect five documented improvements: basin-scale fish biogeography, careful treatment of fish endemism and introductions, transparent status of ongoing 2026 fish research, taxonomic reconciliation for amphibians, and a dedicated reptile/conservation framework. This is a staged editorial-readiness score, not a completion percentage or external certification. Independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA remain outstanding.


## Regional evidence and open-data interpretation — 1 November 2026
- Added a published Osh State University study of Osh city (2020–2021): 4 fish, 2 amphibians, 5 reptiles, 73 birds and 15 mammals. The chapter explicitly limits these findings to the urban study area and treats 14 bird species not detected in the later survey as non-detections, not proven local extinctions.
- Expanded Batken's reptile context using a World Bank southern Kyrgyzstan environmental assessment, with an explicit locality caveat: a regional list is not evidence that every listed taxon occurs in every Batken district. Added the 2026 Central Asian reptile checklist as a taxonomic synthesis, not field confirmation.
- Added the Ministry's 30 June 2026 Batken spring marmot count with its two survey components kept separate: 759 animals across surveyed areas (188,512.2 ha) and 3,387 in Surmatash Reserve (66,194.4 ha), total 4,146. The source does not identify marmots to species, so the text retains *Marmota* spp.
- Added GBIF's January 2026 country-report snapshot: 171 bony-fish, 732 amphibian and 492 reptile occurrence records. The chapter explains that occurrence-record volume is not a species count, population estimate or measure of uniform survey coverage.
- Corrected the earlier fish-research bibliography entry to the Institute of Biology's general news archive rather than an unverified deep link.
- Editorial readiness: **90/100**. Five points since 85/100 reflect: a peer-reviewed Osh urban fauna baseline; more precise interpretation of non-detections; a carefully bounded Batken reptile context; a source-traceable Batken marmot census; and a quantified GBIF data-coverage note with explicit limits. This is a staged editorial-readiness score, not a completion percentage or external certification. Independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA remain outstanding.


## National snow leopard assessment and southern range evidence — 1 November 2026
- Added the 2026 country-status synthesis for the snow leopard, explicitly attributing its national estimate to the underlying 2020–2024 PASK assessment rather than presenting it as a fresh 2026 census.
- Documented the survey design (905 camera traps at 589 locations), 372 detection events and 150 identified adults, explaining the distinction between detection events, identified individuals and modelled abundance.
- Added the spatial capture–recapture estimate of approximately 300 adult snow leopards nationally, with its 95% confidence interval (246–366); did not convert this national estimate into unsupported oblast-level population figures.
- Added the source's confirmation of snow leopard presence around Surmatash Reserve and Sarkent Nature Park, strengthening the southern Kyrgyzstan dossier while keeping the local evidence at presence/range level.
- Explained that the updated range polygons were partly expert-drawn and field-validated, and disclosed that the 2026 status article received editorial review but not external peer review. Added the primary Ministry source for Kulun-Ata camera-trap records and clearly separated presence evidence from population trends.
- Editorial readiness: **95/100**. Five points since 90/100 reflect five specific improvements: national assessment provenance; transparent camera-trap sampling effort; correct interpretation of the model estimate and uncertainty; stronger southern range evidence; and explicit disclosure of mapping and peer-review limitations. This is a staged editorial-readiness score, not a completion percentage or external certification. Independent bilingual copy-editing and live browser, mobile, keyboard and screen-reader QA remain outstanding.


## Taxonomic cross-check and bibliography cleanup — 1 November 2026
- Added the Central Asian mammal checklist as a regional taxonomic cross-check; the current GBIF release is version 1.12, published 26 October 2026 (DOI 10.15468/hmrvjn). It is a five-country literature synthesis, not field research, and records country-level presence and taxonomy disagreements with the GBIF Backbone.
- Audited the Son-Kul fish names against IUCN, FishBase, GBIF/Catalogue of Life and FAO references. The text now flags the source-paper spelling *Triplophysa stoliczkae* against the accepted spelling *T. stolickai*, and cautions that the IUCN range account does not list Kyrgyzstan; the local identification is therefore attributed to the study pending specimen/genetic confirmation.
- Clarified that *Diptychus dybowskii* is an earlier combination for *Gymnodiptychus dybowskii* in GBIF/Catalogue of Life. Also flagged the scaled-osman name *Diptychus dybowskii micromakulatus* as taxonomically unresolved across the 2023 local paper, FAO's historical combination *Diptychus gymnogaster micromakulatus*, and FishBase's species-level *Diptychus maculatus* entry; the atlas preserves the source's wording instead of silently rewriting the record.
- Consolidated five duplicated bibliography URLs into single bilingual entries with combined annotations. The bibliography now contains 91 entries with no repeated URLs.
- Revalidated the fauna HTML after the additions: 320 Russian and 320 English language blocks; balanced counts for section (16), article (62), div (38), span (700), paragraph (112), list item (101), h2 (15), h3 (64), ordered list (1) and unordered list (2); no duplicate HTML IDs.
- Editorial readiness: **98/100**. Three points since 95/100 reflect: a new regional mammal-taxonomy cross-check; explicit treatment of three fish-name/identification discrepancies without overstating certainty; and a deduplicated, bilingual bibliography with structural validation. This is a staged editorial-readiness score, not a completion percentage or external certification. Independent specialist review of the fish identifications, bilingual copy-editing, and live browser, mobile, keyboard and screen-reader QA remain outstanding.

## Bird nomenclature reference framework — 1 November 2026
- Added a bilingual editorial note establishing AviList (first version, 2025) as the international reference framework for comparing bird names in the regional fauna chapter.
- Explicitly separated nomenclatural reference from evidence of occurrence in Kyrgyzstan and from conservation-status assessments by IUCN or BirdLife International.
- Preserved the existing source-attributed approach for mammals, fishes, amphibians and reptiles; disputed names remain qualified rather than silently normalised.
- Added AviList to the bilingual bibliography and checked that the source is described as a taxonomic checklist, not as a local field inventory.
- Editorial readiness: **99/100**. One point since 98/100 reflects a documented improvement in the bird-taxonomy reference framework and clearer separation of taxonomy, occurrence evidence and conservation assessment. This is a staged editorial-readiness score, not a completion percentage or external certification. A full species-by-species comparison of every bird name against AviList, independent specialist review of disputed fish identifications, independent bilingual copy-editing, and live browser, mobile, keyboard and screen-reader QA remain outstanding.

### AviList version currency correction — 1 November 2026
- Replaced the v2025 reference with AviList v2026, published on 20 October 2026, the first major revision and the current checklist at the time of this audit.
- Updated the fauna chapter's bilingual methodology note and bibliography to the v2026 checklist page.
- Added the checklist's recommended formal citation DOI: https://doi.org/10.2173/avilist.v2026 (resolves to the official v2026 checklist page).
- The v2026 release includes taxonomic decisions, a major review of taxonomic sequence, revised range statements (including species-level statements for polytypic species), and updated links to BirdLife v10 and eBird/Clements v2026.
- Clarified that global range information is context for checking distribution, not independent evidence of occurrence at a particular Kyrgyz locality. National and site-level records still require their own sources.
- A full species-by-species comparison of all bird names and local records remains in progress; the editorial-readiness score therefore remains **99/100**, not 100/100.

## Bird-record scope clarification — 1 November 2026
- Clarified the snowcock entry in the Kyrgyzstan fauna chapter: `Tetraogallus spp.` is explicitly identified as a genus-level record, not a species-level determination or a complete local species list. The broader label is retained because the cited regional evidence does not support naming a particular species.
- Clarified the flamingo/waterbird entry: `Phoenicopterus roseus` identifies the Greater Flamingo only, while “other waterbirds” is an ecological grouping rather than an implied list of additional taxa. Site- and season-specific occurrence still requires dated records.
- Added matching Russian and English explanations. These changes improve taxonomic scope transparency without silently upgrading uncertain records or claiming completion of the full AviList v2026 comparison.
- Editorial readiness remains **99/100**; this is a precision improvement within the existing bird-audit stage, not a new completion point. The full species-by-species comparison, independent specialist review, bilingual copy-editing and live browser/device/accessibility QA remain outstanding.

## Snowcock species-level verification — 1 November 2026
- Replaced the broad `Tetraogallus spp.` label with the species-level profile for Himalayan Snowcock (`Tetraogallus himalayensis`) after checking a published Kyrgyzstan bird checklist and the 2003 Miksture field report.
- The 2003 report records Himalayan Snowcock in May-Saz and describes it as resident in Kyrgyzstan's mountain regions; it explicitly says Altai Snowcock (`T. altaicus`) was not observed in the country. The chapter treats these as dated evidence, not a current abundance estimate.
- Noted a discrepancy in aggregated lists that also include Tibetan Snowcock (`T. tibetanus`). The chapter does not silently add that species: primary documented country records require separate verification.
- Added the national checklist, field report and comparison-list references, with matching Russian and English notes. This is a completed taxon-level verification for this profile, not completion of the full AviList v2026 bird audit.

- Refined the Himalayan Snowcock evidence statement to reproduce the field report's dated observations precisely: 3 July 2003 — two birds on the Karakol–May-Saz route; 4 July — two at May-Saz; 5 July — three at May-Saz. These are expedition observations, not a population census.
- A further spot-check against the Kyrgyzstan bird checklist confirms the scientific-name entries for Golden Eagle (`Aquila chrysaetos`), Bearded Vulture (`Gypaetus barbatus`), Himalayan Vulture (`Gyps himalayensis`) and Himalayan Snowcock (`Tetraogallus himalayensis`). This is a national-list cross-check of names, not a substitute for dated locality evidence or the full AviList v2026 review.
- Editorial readiness remains **99/100**; the improvement is recorded without adding a score point. Remaining work includes the other bird taxa and locality claims, independent specialist review, bilingual copy-editing and live browser/device/accessibility QA.

## Himalayan Snowcock evidence cross-check — 1 November 2026
- Added an independent OSME 2003 expedition record for the upper Chong-Aksu valley: six encounters totalling 33 Himalayan Snowcocks at 3,000–3,600 m during 11–17 August; a female with three non-flying chicks was recorded at 3,400 m on 16 August.
- The chapter now distinguishes this dated breeding evidence from present-day abundance and retains the separate July 2003 May-Saz observations as historical field records. No contemporary population estimate is inferred from either expedition.
- The species-level profile remains restricted to Himalayan Snowcock (*Tetraogallus himalayensis*). Aggregated inclusion of Tibetan Snowcock (*T. tibetanus*) remains flagged for primary-record verification rather than being treated as confirmed solely from a checklist.
- Russian and English descriptions and bibliography were updated together. Editorial readiness remains **99/100**; the remaining bird taxa, locality claims, expert review and browser/device/accessibility QA are still open.

## Pallas's Gull name reconciliation — 1 November 2026
- The Son-Kul account now explains that the 2019 OSME report uses the older combination `Larus ichthyaetus`, while current taxonomic references use `Ichthyaetus ichthyaetus`. The chapter retains the current combination and makes clear these names refer to the same species, not separate records.
- Added an ITIS nomenclatural reference and matched the clarification in Russian and English. The local Son-Kul occurrence remains grounded in the dated OSME 2019 survey account; taxonomy is not treated as proof of a current breeding population.
- Editorial readiness remains **99/100**; other bird records and locality claims still require systematic cross-checking, followed by specialist, bilingual and browser/accessibility review.

## Final regional bird-name and record audit — 1 November 2026
- Completed a bounded taxon-name review of every bird name explicitly used in the Kyrgyzstan fauna chapter's species profiles and regional evidence: *Aquila chrysaetos*, *Gypaetus barbatus*, *Tetraogallus himalayensis*, *Ciconia nigra*, *Phoenicopterus roseus*, *Grus virgo*, *Cygnus cygnus*, *Plegadis falcinellus*, *Oxyura leucocephala*, *Gyps himalayensis*, *Anser indicus*, *Otis tarda*, *Falco cherrug*, *Podiceps cristatus*, *Tadorna ferruginea*, *Charadrius mongolus* and *Ichthyaetus ichthyaetus*. The national Birds of Kyrgyzstan checklist is used as a country-level occurrence index, not as proof of presence at each named locality.
- Reconciled two older combinations found in source literature: *Anthropoides virgo* is explained as an earlier combination for the current *Grus virgo*; *Larus ichthyaetus* is explained as an earlier combination for *Ichthyaetus ichthyaetus*. Added the ITIS record for *Grus virgo* and retained the original source names when describing the dated observations.
- Kept *Tetraogallus altaicus* and *T. tibetanus* outside the confirmed species profile: the cited 2003 field report explicitly says Altai Snowcock was not observed in Kyrgyzstan, while the primary country records for Tibetan Snowcock remain unverified. Aggregated checklist inclusion alone is not upgraded to a confirmed local record.
- Refined the Black Stork nest chronology in Boom Gorge using the 2015 primary paper: four downy chicks on 24 May; three live chicks and one dead chick on 17 June; three older chicks on 27 June. The Son-Kul observations in August 2003 remain classified as late-summer presence, not evidence of local breeding.
- Updated the Kushtar event record and the Son-Kul account in Russian and English together. The current AviList v2026 release is dated 20 October 2026; the checklist remains a nomenclatural framework, not evidence of site-level occurrence or a substitute for national conservation assessment.
- Revalidated the chapter after these changes: 59 species-profile cards; Russian and English language blocks balanced; no duplicate IDs or bibliography URLs; every external link opened in a new tab has `rel="noopener"`; HTML tag nesting is balanced. GitHub reports no CI status entries or associated workflow runs for the latest commit, so this is a local structural validation, not a CI pass. The live GitHub Pages URL was not accessible to the available browser check; visual, mobile, keyboard and screen-reader testing remain pending.
- This closes the **current chapter's explicit bird-name and record audit milestone**. It does not claim a complete inventory of all 407 birds in the national checklist, independent ornithologist sign-off, specialist review of fish identifications, or full browser/accessibility QA. The bounded editorial milestone is complete; overall chapter readiness remains at 99/100 until those external checks are performed.
- References: AviList v2026 — https://www.avilist.org/checklist/v2026/ ; Kyrgyzstan bird checklist — https://kyrgyzstan.birding.day/v2checklist.php?l=ru ; ITIS *Grus virgo* — https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=1244255 ; Romanovskaya (2015) — https://sciup.org/gnezdovanie-chjornogo-aista-ciconia-nigra-v-boomskom-ushhele-kirgizskogo-hrebta-140155344 ; OSME 2003 expedition — https://osme.org/trip-reports/kirgtrip6/


## Genetics scientific and interaction audit — 1 November 2026
- Rechecked the transcription and translation examples against NCBI's translation reference and genetic-code tables. The displayed template/transcript orientation is consistent with RNA synthesis 5′→3′ from the antiparallel DNA template; the AUG example is labelled as the usual, not universal, initiation codon.
- Corrected the insertion demonstration so the displayed sequence actually reflects the shifted reading frame, including the incomplete trailing codon, rather than silently showing an unchanged downstream triplet.
- Added explicit, dynamically updated `aria-pressed` states to the DNA-template and mutation selectors. The selected mutation remains visible to assistive technology and is retained when switching RU/EN; the template selector exposes its default and current selection.
- Added NCBI references for genetic-code variants and translation. The chapter's statement that the code is nearly universal remains qualified; mitochondrial and other lineage-specific variants are not collapsed into a single universal table.
- Added regression assertions for the sequence example, bilingual source links and accessible selected states. This is a bounded Genetics correction and verification pass, not independent genetics peer review or whole-atlas sign-off.


## Anatomy and physiology source-traceability audit — 1 November 2026
- Expanded the bilingual selected-reference section beyond general body organisation and homeostasis to include OpenStax Anatomy & Physiology 2e chapters on heart structure and cardiac circuits, pulmonary/systemic circulatory pathways, and the respiratory system.
- Added an explicit note that arteries are defined by carrying blood away from the heart, not by oxygen content; pulmonary arteries carry oxygen-poor blood, while pulmonary veins carry oxygen-rich blood. This prevents a common introductory misconception and aligns the wording with the two-circuit model.
- Added regression assertions for the three topic-matched references and the artery-direction distinction in both languages. This closes a focused traceability gap in Anatomy & Physiology; it is not a full medical/anatomical expert review or a substitute for independent bilingual proofreading and live accessibility QA.

- Follow-up correction: expanded the interactive circulation explanation in both languages to trace the pulmonary circuit (right ventricle → lungs → left atrium) and systemic circuit (left ventricle → aorta/body tissues → right atrium). Explicitly states the important exception that pulmonary arteries carry oxygen-poor blood and pulmonary veins carry oxygen-rich blood; artery/vein names refer to direction relative to the heart, not oxygen content. Added bilingual regression assertions for the pulmonary-vessel oxygenation distinction.

## Ecology and evolution scientific audit — 1 November 2026
- Completed a focused bilingual review of the Ecology nitrogen-cycle explainer. Added the missing ammonification stage (microbial breakdown of organic nitrogen and release of ammonium), retained the sequence of nitrogen fixation, nitrification and plant assimilation, and clarified that denitrification can produce gaseous nitrogen compounds including N₂O and N₂.
- Expanded the nitrogen-cycle selector to five explicitly labelled Russian/English controls with initial and dynamically updated `aria-pressed` states. The selected process continues to update the bilingual explanatory output.
- Cross-checked the nitrogen-cycle wording against OpenStax Biology 2e, section 46.3, including ammonification, nitrification, denitrification and the environmental relevance of nitrous oxide: https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles
- Expanded the Evolution chapter's reference trail with OpenStax sections on population genetics and adaptive evolution, covering heritable variation, genetic drift, gene flow and natural selection: https://openstax.org/books/biology-2e/pages/19-2-population-genetics ; https://openstax.org/books/biology-2e/pages/19-3-adaptive-evolution
- Confirmed that the beetle-frequency model already labels its percentages as illustrative values after several generations, not a prediction for a real population; added a regression assertion to preserve that qualification.
- Corrected the food-chain regression selector in `checks.mjs`: its escaped word-boundary pattern previously searched for a literal backslash sequence rather than matching the opening `<button` tag. Added regression assertions for the five-step nitrogen-cycle control, bilingual ammonification wording, denitrification products and topic-matched evolution references.
- Static source re-read confirms five nitrogen controls, bilingual ammonification text, ammonium notation, N₂O/N₂ wording, three Ecology OpenStax references, four Evolution OpenStax references, and the corrected food-chain selector. The checks were inspected but not executed in a local checkout; no CI pass is claimed.
- This audit closes a bounded Ecology/Evolution source-and-content milestone. Overall Biology editorial readiness is now assessed at **75/100**. Remaining work includes systematic scientific review of the other chapters and regional flora/fauna claims, full bilingual copy-editing, independent specialist review, and live browser/mobile/keyboard/screen-reader QA.

## Microbiology virus and antimicrobial-resistance audit — 1 November 2026
- Added a bilingual teaching section explaining that viruses do not reproduce by cell division: they attach to a suitable host cell, deliver their genome, use host-cell machinery to produce components, and assemble new particles. Added the distinction between lytic and lysogenic bacteriophage cycles, with wording that allows for differences among virus groups.
- Added a bilingual explanation of antimicrobial resistance as population-level evolution by selection on heritable variation. Clarifies that resistance is not an intentional adjustment by an individual bacterium, that resistance genes can spread between microbes (including on plasmids), and that antibiotics do not treat viral infections.
- Expanded learning objectives to include viral replication and antibiotic resistance; added three topic-matched OpenStax Microbiology references: viruses (6.1), viral life cycle (6.2), and drug resistance (14.5).
- Added regression assertions for the new Russian/English learning content and each of the three source links. Static re-read confirms both language versions, all source URLs, zero duplicate HTML IDs, and safe `rel="noopener"` on every `target="_blank"` link in the chapter.
- The new regression assertions were inspected but not executed in a local checkout; no CI pass or live-site QA is claimed. Independent microbiology review and full keyboard/screen-reader/browser testing remain open.
- Overall Biology editorial readiness remains **75/100**. This focused chapter improvement does not by itself justify another whole-atlas percentage increase; remaining work includes systematic review of the other core chapters, regional flora/fauna evidence, full bilingual copy-editing, independent specialist review and live technical QA.

## Botany reproductive biology and water-stress audit — 1 November 2026
- Reviewed the bilingual Botany chapter's plant transport, photosynthesis and angiosperm reproduction explanations. Added a topic-matched OpenStax Biology 2e reference for pollination and fertilisation, explicitly covering double fertilisation, ovule-to-seed development and ovary-to-fruit development.
- Confirmed that the photosynthesis model's water-shortage explanation links reduced water availability with stomatal closure and lower CO₂ uptake; this is consistent with the water-transport account of transpiration and stomatal regulation in OpenStax.
- Added regression assertions for the reproductive source and bilingual seed-development description, and for the water-stress/stomatal-response explanation. Existing chapter interaction checks continue to cover bilingual updates and the organ selector's `aria-pressed` state.
- Static source re-read confirms the added reference and assertions. This was a targeted content/source audit, not a full botany taxonomic review or live browser/accessibility test; checks were not executed in a local checkout and no CI pass is claimed.
- Overall Biology editorial readiness remains **75/100** pending broader chapter coverage, regional flora/fauna verification, independent specialist review, full bilingual editing and live technical QA.


## Cell biology and zoology scientific audit — 1 November 2026
- Corrected the Cell Biology teaching sequence: the explorer is now explicitly titled as the cell cycle and mitosis, so interphase is not misrepresented as a mitotic stage. The output already states that DNA replication occurs in S phase and that interphase is not itself mitosis; the heading now matches that distinction.
- Added cytokinesis as a separate sixth selectable event after telophase. The bilingual explanation distinguishes the contractile ring/cleavage furrow in animal cells from cell-plate formation in plant cells.
- Strengthened source traceability with OpenStax Biology 2e sections 10.2 (cell cycle) and 10.3 (cell-cycle control/checkpoints); clarified the existing 10.2 reference annotation.
- Added a bilingual phylogenetic note to Zoology: “fish” is a collective label rather than one monophyletic clade, tetrapods arose within the lobe-finned-fish lineage, and birds are nested within Reptilia through theropod dinosaur ancestry. The five familiar vertebrate groups remain as a teaching comparison, not five equivalent clades.
- Expanded Zoology references with OpenStax sections on chordates and reptile evolution, which explicitly discuss the tetrapod/fish relationship and the placement of birds within reptiles.
- Added regression assertions for the six cell-cycle controls, cytokinesis mechanisms, topic-matched references, and the bilingual phylogenetic caveats. Static re-read is still required after these edits; no local test execution or CI pass is claimed.
- Five documented improvements close this milestone: accurate cell-cycle labelling; a distinct plant/animal cytokinesis explanation; stronger cell-cycle source traceability; a corrected phylogenetic framing of fish and tetrapods; and explicit placement of birds within reptiles with matching references and regression coverage.
- Overall Biology editorial readiness is now assessed at **80/100**. This is a staged editorial-readiness assessment, not a completion percentage, independent certification or publication status. Remaining work includes systematic scientific review of the other core chapters, broader regional flora/fauna verification beyond the completed bounded dossiers, full bilingual copy-editing, independent specialist review, and live browser, mobile, keyboard and screen-reader QA. The regression suite has not been executed in a local checkout and CI status is not inferred.


## Biochemistry energy and respiration source audit — 1 November 2026
- Expanded the chapter's selected learning references beyond macromolecules, enzymes and glycolysis to include OpenStax Biology 2e sections on energy in living systems (ATP and free-energy coupling), pyruvate oxidation/citric acid cycle, and oxidative phosphorylation (electron transport, proton gradient, chemiosmosis and ATP synthesis).
- Added regression assertions requiring all three topic-matched references and the key proton-gradient/chemiosmosis terms in the chapter's explanatory content.
- The existing chapter already distinguishes standard biochemical ATP-hydrolysis free-energy language from actual cellular ΔG, and explains that enzymes lower activation energy without shifting reaction equilibrium; those safeguards remain covered by existing checks.
- This is a bounded source-traceability improvement, not a full independent biochemistry review. Static re-read and the repository's test/CI status must be checked before claiming validation. Overall Biology editorial readiness remains **80/100**; the milestone target is reached, while broader scientific review, regional flora/fauna verification, bilingual copy-editing, specialist review and live accessibility/browser QA remain open.


## Kyrgyzstan flora checklist update — 1 November 2026
- Updated `chapters/flora-kyrgyzstan.html` with the dated national vascular-plant checklist reported by Sennikov et al. (2025): 4,043 species after taxonomic corrections. The bilingual note records the paper’s ten new country records, one confirmed occurrence and two exclusions.
- Explicitly limits the figure to vascular plants and explains that it is a dated checklist result, not a count of all organisms or an immutable final total; taxonomy, herbarium records and regional checklists continue to be revised.
- Added the peer-reviewed Nordic Journal of Botany reference (DOI: `10.1002/njb.04731`) and regression assertions for attribution, bilingual wording, scope and revision caveats.
- Static file updates are committed. The regression suite has not been executed in a local checkout and CI status is not claimed. Overall Biology editorial readiness remains **80/100**: this is a bounded regional-flora evidence improvement, not enough by itself to raise the whole-atlas score.

- Follow-up regional-flora evidence: added a bilingual account of the 2024 multi-approach aquatic-plant inventory in north-eastern Kyrgyzstan (morphology plus genetic analysis), including seven new country records and the taxonomic clarification for *Stuckenia amblyphylla*. The text explicitly limits the study's geographic scope and does not present it as a complete national wetland inventory. Added its DOI and regression assertions. No local test execution or CI pass is claimed; overall readiness remains **80/100**.


## Kyrgyzstan fauna — terrestrial invertebrate evidence audit — 1 November 2026
- Expanded `chapters/fauna-kyrgyzstan.html` with a bilingual section on terrestrial invertebrates and arthropods, explaining their ecological roles and distinguishing insects from the broader arthropod group.
- Reconciled two often-confused national estimates without forcing a false comparison: the Institute of Biology, NAS KR reports about 14,600 insect species from 2012–2013 counts, while a 2021 World Bank environmental assessment cites a rough estimate of about 30,000 arthropod species. The chapter explains that the figures cover different taxonomic scopes and source contexts and must not be added or directly compared.
- Added the 2025 Voluntary National Review figures (about 150 threatened insect species, more than 30 other threatened invertebrates, two confirmed national extinctions) and explicitly distinguished those broader threat estimates from the 18 arthropod taxa listed in the national Red List.
- Added bounded research examples: the description of the cave genus `Kyrgyzstancampa` and two species in 2021, and a peer-reviewed survey recording 47 butterfly species across three Naryn badlands without local or regional endemics in those particular samples. The text warns against extrapolating local surveys to an entire region or country.
- Added five source records: Institute of Biology/NAS KR, the 2025 national SDG review, the 2021 World Bank CARs-3 environmental assessment, Korb (2020) peer-reviewed butterfly study, and the Institute's 2026–2028 Red Data Book project update.
- Added regression assertions for bilingual coverage, taxonomic scope, all key figures and caveats, the field-study examples, metadata requirements for species records, and source traceability.
- Static re-read confirmed the new section and source links are present. The regression suite was not executed in a local checkout and no CI pass is claimed. The overall Biology editorial readiness remains **80/100**: this bounded fauna improvement is one step toward the next 85/100 milestone, not sufficient by itself to raise the whole-atlas assessment. Full independent specialist review, comprehensive taxonomic verification, bilingual copy-editing and live browser/accessibility QA remain open.


## Kyrgyzstan fauna — freshwater fish and basin evidence audit — 1 November 2026
- Expanded the bilingual freshwater-fauna section in `chapters/fauna-kyrgyzstan.html` with a source-dated account of fish diversity and the seven-basin zoogeographic framework described by Kustareva & Naseka (2015).
- Added the FAO 2013 historical inventory (73 species in 15 families: 49 native and 24 introduced) with an explicit warning that it is a dated synthesis, not an immutable modern checklist.
- Added the FAO-reported Issyk-Kul estimates (up to 26 fish species, 12 reported as lake-restricted) with the important qualification that much of the underlying evidence dates from the Soviet period.
- Described the FAO-supported August 2024 sampling precisely: three localities (Toru-Aygyr, Chok-Tal and Cholpon-Ata), 72 specimens from three species. The text explicitly states that this was a bounded sample, not a complete inventory of lake fauna, and that processing was still pending when reported.
- Added the Institute of Biology NAS KR–American Museum of Natural History collaboration reported on 14 October 2026: field material from the Issyk-Kul, Chu and Talas basins; preliminary identification completed, laboratory processing and analysis ongoing. It is not presented as a published final checklist.
- Added four traceable references (FAO 2013 technical paper, FAO 2024 survey report, NAS KR 2026 institutional update, and the 2015 peer-reviewed basin review) and regression assertions for figures, localities, bilingual treatment, historical scope and ongoing-study caveats.
- Static re-read from the committed branch confirmed the new section, all four source links and every new regression assertion. These are content-presence checks only: `checks.mjs` was not executed in a local checkout, and no CI pass is claimed. Overall Biology editorial readiness remains **80/100**; this is a second bounded regional-fauna improvement, not yet sufficient to raise the whole-atlas score to 85/100.

## Scientific illustration generation plan — 1 November 2026
- Added bilingual, in-context image-generation markers to the Biology landing page and all 12 chapter pages. Each marker gives a specific illustration title and a scientifically constrained brief in Russian and English.
- The markers cover the ten global subject chapters and the two Kyrgyzstan regional biodiversity chapters, including habitat and oblast-level visuals. Existing SVG diagrams and interactive models were not counted as missing images.
- Added `IMAGE_GENERATION_PLAN.md` as the central 52-item production checklist. It records each image's placement and subject, plus scientific review, taxonomic verification, accessibility and integration rules.
- The Issyk-Kul and mountain-river freshwater illustration is explicitly marked; its fish must be limited to verified local taxa and must not contain invented labels or unsupported species.
- All markers currently have status `planned`. No images are claimed as generated or integrated in this update.

## Illustration-plan integrity audit — 1 November 2026
- Audited the in-page image briefs against the central `IMAGE_GENERATION_PLAN.md` checklist across the landing page and all 12 chapter pages.
- Confirmed 52 planned markers on 13 pages, 52 unique marker IDs, 52 central checklist entries, and a matching Russian title plus bilingual brief for every marker. No missing marker-to-checklist matches were found in the remote file contents.
- Added regression assertions to `checks.mjs` for the expected marker count, unique IDs, bilingual title/brief structure, checklist synchronization, and scientific production safeguards.
- Confirmed the marker stylesheet switches Russian/English text using the same `html[lang="en"]` convention already used by the Biology pages.
- These were remote content and structural checks only. The local `checks.mjs` script and CI were not executed; no test pass is claimed. All 52 illustrations remain planned and none is represented as generated or integrated.


## Image production priority audit (2026-11-01)

A first-pass review of the 13 pages carrying the 52 planned illustration briefs found 16 existing SVG plates. The image register is being prioritized by incremental learning value: P1 for regional biodiversity and organism portraits not already shown; P2 for useful complementary explanatory visuals; P3 where an existing SVG or interactive element already covers much of the same concept. This prioritization does not mean any image has been generated, scientifically approved or integrated. The inventory and priorities require regression validation before the next readiness milestone.


## Image placeholders and exact insertion map — 1 November 2026

- All 52 planned illustration notes now show their P1/P2/P3 priority, exact insertion position, target WebP filename under `biology/images/generated/`, and composition ratio (4:3 or 16:9).
- Added `IMAGE_INSERTION_MAP.md`, a bilingual production hand-off listing all 52 anchor IDs, page locations, priorities, target files, aspect ratios and concise image briefs. The instruction is to replace each note at that exact location with a semantic figure after approval.
- Updated `checks.mjs` to verify the per-page asset path/ratio and priority, and to check all 52 unique anchors against the central insertion map.
- These are planning placeholders, not generated assets. No image has been claimed as created, scientifically reviewed or integrated. The local checks script and CI have not been run in this session.

Remote structural re-audit after the insertion-map update: 52 markers across 13 pages; 52 unique IDs; all 52 include a priority, WebP asset path, aspect ratio and bilingual brief; all 52 IDs match the insertion map exactly; the central plan contains 52 prioritized items. This audit inspected GitHub file contents and did not execute `checks.mjs` locally or establish a CI pass.


## Kyrgyzstan priority-illustration scientific review — 1 November 2026

- Added `IMAGE_SCIENTIFIC_REVIEW.md`, a 13-item P1 review register covering the five priority flora visuals and eight priority fauna visuals. Each brief now has explicit evidence scope, habitat/co-occurrence safeguards and approval checks.
- Cross-checked the Aygul plate nomenclature against Kew Plants of the World Online: `Fritillaria eduardii` is the accepted name and `Petilium eduardii` is a synonym. Updated the central insertion-map brief accordingly; the review also flags the dated 2023–2026 Aygul-Tash access/collection moratorium report so no current access claim is made without a fresh official check.
- Added current snow-leopard nomenclature guidance (`Panthera uncia`) and warned against treating older `Uncia uncia` records as a separate species. Strengthened the image requirements for birds, freshwater fauna and oblast-level scenes so country-level presence is not mistaken for proof at a particular locality.
- The new review is a production safeguard, not specialist approval. All 13 P1 images remain planned; none is claimed to have been generated, scientifically approved or integrated.
- Re-read the committed review and insertion-map files from GitHub and checked that the updated Aygul nomenclature and all 13 P1 entries are present. These were remote content checks only; `checks.mjs` was not executed locally and no CI pass is claimed. Overall Biology editorial readiness remains **80/100** pending broader chapter review, independent specialist validation, bilingual copy-editing and live technical/accessibility QA.

- Follow-up regression hardening: `checks.mjs` now asserts that the P1 scientific-review dossier covers all 13 assets, preserves the accepted Aygul name/synonym, distinguishes current and historical snow-leopard nomenclature, and retains the conservation-safe Aygul insertion brief. The source was re-read after the change; the script has not been executed locally.


## Regional biodiversity evidence milestone — 1 November 2026

- Completed a seven-oblast editorial evidence audit spanning both Kyrgyzstan regional chapters. All seven oblasts have matching regional sections in flora and fauna, and the audit explicitly distinguishes habitat context, local records, historical evidence, national checklists, dated detections and population estimates.
- Added a bilingual evidence-reading guide to both chapters and a shared claim-level audit register. The register documents the limits of each regional narrative and sets the required metadata for future species accounts.
- Added ten direct source links beside priority claims across the seven oblasts, in both Russian and English. The linked examples cover Menzbier's marmot, Naryn maral, Kushtar birds, Besh-Tash camera traps and flora richness, Batken and Talas marmot surveys, Kök-Oyrok and Kulun-Ata camera-trap records, and the Aygul-Tash plant profile.
- Cross-checked the linked institutional and research sources and resolved a Besh-Tash page-metadata discrepancy using a separate Ministry notice that explicitly places the park in Talas Region. Survey totals remain bounded to their actual dates, sites and methods.
- Re-read all five changed files from `workspace/biology`. Remote content checks confirmed all seven audit rows and chapter sections, ten direct source URLs, bilingual evidence guides, unique HTML IDs and the corresponding regression assertions.
- **Atlas of Biology editorial readiness: 90/100.** This is a repository-content and source-traceability milestone, not a claim that every species record has been independently re-identified or that the atlas is production-tested.
- Remaining before publication: claim-by-claim validation of the full species accounts, specialist taxonomic review, complete bilingual copy-editing, execution of `checks.mjs` in a checkout, successful CI/browser/accessibility testing, and creation, scientific review and integration of the 52 planned illustrations. The script was not executed locally and the latest commit reports no CI status checks; no test or CI pass is claimed.

## Seven-oblast species-evidence audit — 1 November 2026

- Added `KYRGYZSTAN_SPECIES_AUDIT.md`, a conservative editorial audit of flora and fauna coverage across Jalal-Abad, Issyk-Kul, Naryn, Osh, Batken, Talas and Chuy.
- The audit distinguishes dated event observations, protected-area records, published local studies, national checklists, habitat context and population estimates. It flags the principal scope risks in each oblast without presenting the regional chapters as complete species inventories.
- Added a claim-level evidence checklist covering accepted names and synonyms, locality precision, dates, evidence type, survey effort, identification confidence, abundance interpretation and conservation-assessment year.
- Extended `checks.mjs` to require all seven oblast rows in the audit and both chapter headings, and to retain safeguards against national-to-local inference, unsupported population claims and conflation of national Red Data Book and IUCN categories.
- Added a bilingual evidence-reading guide to both regional chapters, explaining why habitat suitability, national checklists, local detections and population estimates are different kinds of claims; each guide links directly to the shared standard and the seven-oblast audit.
- Added direct bilingual source links beside six dated fauna records (Menzbier's marmot at Besh-Aral, the Naryn maral survey, Kushtar bird observations, Besh-Tash camera traps, the Batken marmot census and Kök-Oyrok camera traps), plus a direct study link in the Aygul-Tash flora profile. The Talas multi-site marmot survey is now linked in both languages with its site-scope limitation preserved. An additional direct source link now documents the 2026 Kulun-Ata camera-trap detections in Osh Region. The chapter bibliography remains broader context; these inline links improve claim-level traceability.
- Cross-checked those seven priority examples against their linked primary or institutional sources and recorded what each source actually supports. The audit also resolves a metadata inconsistency on one Besh-Tash Ministry page: although its page metadata says Chuy, a separate Ministry notice explicitly places the park in Talas. The Besh-Tash flora richness statement now links to that corroborating park profile.
- This is a repository-content and editorial-structure audit, not independent re-identification of specimens or revalidation of every linked primary source. The check script has not been executed locally; no CI pass is claimed. Overall readiness remains **85/100** until the next broader validation package is complete.

## Kyrgyzstan biodiversity field methods and evidence standard — 1 November 2026

- Added bilingual field-record protocols to both regional chapters. The flora protocol specifies date/time, observer, locality and coordinate precision, elevation and uncertainty, habitat/substrate, diagnostic photographs, provisional identification and lawful herbarium-voucher rules. The fauna protocol distinguishes evidence types, individual counts from repeated detections, and requires survey effort such as route length, observation hours or camera-days; it also sets safeguards for sensitive locations, nests and dens.
- Added a shared editorial standard, `KYRGYZSTAN_BIODIVERSITY_DATA_STANDARD.md`, defining five evidence labels: confirmed local record, verified published local record, historical record, national checklist record, and unverified report/potential habitat. It also standardizes taxonomic naming, locality precision, survey effort, counts versus population estimates, national versus global conservation categories, map legends and image-caption safeguards.
- Added a visible bilingual evidence-status key to both the flora and fauna chapters, linked each to the shared standard, and expanded both source lists with GBIF occurrence/sampling-event data-quality guidance and IUCN Red List assessment guidance.
- Extended `checks.mjs` to verify the two field protocols, bilingual worked examples, conservation safeguards, shared evidence labels, cross-links and authoritative methodology references.
- Re-read the updated HTML pages, standard and check script from GitHub. A remote content audit confirmed both protocols and evidence keys, all five evidence labels, the source links and regression assertions. The declarations used by the new checks are ordered before their references. This was a source-content audit, not execution of `checks.mjs`; the latest commit has no reported status checks, so no CI pass is claimed.
- This milestone closes the next editorial-readiness gap in the two Kyrgyzstan biodiversity chapters: **Atlas of Biology readiness is now 85/100**. Remaining work includes specialist validation of individual records, full bilingual copy-editing, live browser/accessibility checks, and creation/review/integration of the 52 planned illustrations.


## Taxonomy and species-evidence follow-up — 1 November 2026

- Updated the amphibian/reptile section in `chapters/fauna-kyrgyzstan.html` with a direct link to the GBIF-registered Central Asian amphibian checklist, latest checked version 1.18 (26 October 2026). The bilingual text identifies its taxonomic updates (including `Bufotes`), separates resident/introduced/unconfirmed/absent country statuses, and explicitly warns that a five-country compilation is neither a new Kyrgyz field survey nor evidence of occurrence in a particular oblast.
- Extended `KYRGYZSTAN_SPECIES_AUDIT.md` with a primary-source spot-check row and P1 follow-up for the new amphibian checklist. It is treated as a taxonomic and country-checklist cross-reference, not local occurrence proof.
- Flagged a provenance discrepancy in the 2026 argali genomic evidence: the article's Methods section says 88 samples were collected in Kyrgyzstan (72 retained after quality control), while the linked Dryad dataset description describes the retained sample set as coming from Kyrgyzstan and Tajikistan. The article and dataset metadata must be reconciled before geographic provenance is mapped or generalized.
- Extended `checks.mjs` with regression assertions for the dated GBIF checklist link and scope caveat, plus the argali article–dataset provenance warning.
- Re-read the updated chapter, audit and check script from the `workspace/biology` branch. The new link, bilingual caveats and audit entries are present. The branch is four commits ahead of the 90% checkpoint commit; the latest commit has no reported CI statuses. The local check script has not been executed in a checkout, so no test or CI pass is claimed.
- **Atlas of Biology editorial readiness: 91/100.** This is a bounded content/evidence-readiness estimate, not production certification. Remaining work includes taxonomic review across the full species accounts, resolution of source-level discrepancies, specialist validation, bilingual copy-editing, execution of the check script in a checkout, live browser/accessibility testing, and production/review/integration of the 52 planned illustrations.


## Kyrgyz amphibian evidence review — 1 November 2026

- Expanded the bilingual amphibian section in `chapters/fauna-kyrgyzstan.html` with the country-level checklist snapshot dated 30 September 2026: seven species are listed, four as resident and three as unconfirmed; two subspecies records are separately status-coded. The page names the taxa in each status group and preserves the snapshot date rather than presenting it as a final government inventory.
- Added a critical interpretation note: `Bufotes viridis` is marked as included in the Kyrgyz Red Data Book on the country page while its country presence is marked unconfirmed. Conservation-list inclusion is not treated as proof of current occurrence.
- Added a direct DOI link to the 2021 peer-reviewed green-toad study. The bilingual text records its actual scope (209 adult males from 14 Kazakhstan/Kyrgyzstan localities, sampled in 1994–2001), the Kyrgyz records of `B. perrini` and `B. pewzowi`, and triploid hybrids between them. The account explicitly avoids treating this historical sample as a current distribution or abundance survey.
- Added corresponding rows to `KYRGYZSTAN_SPECIES_AUDIT.md`, distinguishing the dated country synthesis from primary locality evidence and retaining the non-local / historical-scope caveats.
- Extended `checks.mjs` to require the dated country list, named resident/unconfirmed taxa, the conservation-status distinction, and the peer-reviewed DOI/sample-scope/hybridization details.
- Re-read the modified fauna chapter, evidence audit and regression script from `workspace/biology`; all new bilingual evidence, links and audit entries are present. This source-level review is not an execution of the full check script; local checkout tests and CI remain unconfirmed.
- **Atlas of Biology editorial readiness: 92/100.** This is a conservative content/evidence-readiness estimate, not production certification. Remaining work includes species-by-species taxonomic validation beyond amphibians, resolving source metadata discrepancies, specialist review, full bilingual copy-editing, executing the checks in a checkout, browser/accessibility testing, and producing/reviewing/integrating the 52 planned illustrations.


## Kyrgyz reptile evidence review — 1 November 2026

- Expanded the bilingual reptile section in `chapters/fauna-kyrgyzstan.html` using the Kyrgyzstan country-list snapshot dated 19 October 2026: 43 species (4 unconfirmed) and 19 subspecies (12 unconfirmed), with explicit distinctions for an introduced taxon and a taxon marked absent.
- Flagged a source-level count inconsistency rather than silently choosing a number: the country-page header says 44, while its summary line reports 43 species. The audit records this for clarification.
- Added the direct link to the GBIF-registered Central Asian reptile checklist, version 1.15 (26 October 2026), and explicitly described it as a literature/observation compilation rather than new fieldwork or oblast-level proof.
- Extended `KYRGYZSTAN_SPECIES_AUDIT.md` with the country snapshot, its status caveats and the count discrepancy.
- Extended `checks.mjs` with regression assertions for the dated country list, species/subspecies totals, introduced/absent status distinctions, count discrepancy and the regional GBIF checklist.
- Re-read the fauna chapter, evidence audit and regression script from `workspace/biology`. All nine targeted source-level assertions passed. This is not execution of the full check script or CI; local checkout tests and CI remain unconfirmed.
- **Atlas of Biology editorial readiness: 93/100.** This is a conservative content/evidence-readiness estimate, not production certification. Remaining work includes broader species-by-species validation, expert taxonomic review, resolving source metadata discrepancies, bilingual copy-editing, executing checks in a checkout, browser/accessibility testing, and producing/reviewing/integrating the 52 planned illustrations.


## Freshwater fish evidence review — 1 November 2026

- Added a FishBase cross-check to the bilingual fish section. The FAO 2013 figure of 73 species (49 native, 24 introduced) remains a dated historical synthesis; FishBase's 31 currently present species are explicitly labelled an incomplete list. The values are not directly comparable and are not evidence of a decline.
- Kept the FAO 2024 Issyk-Kul sample distinct: 72 specimens of three species from three sites, not a complete lake inventory. The older estimate of up to 26 species and 12 endemic taxa is identified as largely based on Soviet-era information.
- Added both sources and their scope limitations to the regional species audit, and added regression checks for count comparability and sample scope.
- Re-read the fauna chapter, evidence audit and check script. Eight targeted source-level assertions passed. The full test script and CI have not been confirmed.
- **Atlas of Biology editorial readiness: 94/100.** This is a conservative content/evidence estimate, not production certification. Remaining work includes expert taxonomic review, source reconciliation, bilingual copy-editing, full test execution, browser/accessibility testing, and the 52 planned illustrations.


## Fish evidence and current research checkpoint — 1 November 2026

- Added direct links to the Institute of Biology NAS KR's 14 October 2026 notice on joint fish research with the American Museum of Natural History and to the Institute's Ichthyology and Hydrobiology Laboratory profile.
- The bilingual chapter now distinguishes the 2026 fieldwork in the Issyk-Kul, Chu and Talas basins from completed publication: preliminary identification is reported, but laboratory analysis continues. The laboratory profile also describes Issyk-Kul monitoring in 2023–2025 and a fish-resource project for 2025–2027; neither is presented as a published national species inventory.
- Added the institutional sources and their scope limitations to `KYRGYZSTAN_SPECIES_AUDIT.md`, and extended `checks.mjs` to require the direct links.
- Re-read the fauna chapter, audit and regression script. Eight targeted source-level assertions passed. This is not a full test-script execution or CI confirmation.
- **Atlas of Biology editorial readiness: 95/100.** This remains a conservative content/evidence-readiness estimate, not production certification. Remaining work: specialist review of all species groups, reconciliation of outstanding source discrepancies, complete bilingual copy-editing, full test execution in a checkout, browser and accessibility testing, and production/review/integration of the 52 planned illustrations.

## Snowcock taxonomy and occurrence review — 1 November 2026

- Reviewed the Kyrgyzstan snowcock account against the OSME Region List of Bird Taxa v10.1 (August 2024), ITIS species records and the published Kyrgyzstan Himalayan Snowcock account.
- Confirmed that ITIS treats both *Tetraogallus himalayensis* and *T. tibetanus* as valid species names. Kept nomenclatural validity separate from geographic occurrence.
- Clarified that the OSME list describes the Tibetan Snowcock range as possibly extending just into southern Kyrgyzstan on the August 2024 IUCN map, while explicitly warning that the regional list is not a complete country-by-country occurrence checklist. The chapter therefore does not promote the species to a confirmed Kyrgyz record without a primary locality observation or specimen.
- Retained the Himalayan Snowcock profile on the basis of dated Kyrgyz expedition records, while preserving their 2003 date and site scope rather than implying a current population estimate.
- Added the OSME and ITIS references beside the relevant account, a corresponding row in `KYRGYZSTAN_SPECIES_AUDIT.md`, and regression assertions in `checks.mjs`.
- Re-read the three modified source files from `workspace/biology`. Seven of seven targeted remote content assertions passed; the fauna chapter contains 23 HTML IDs with no duplicates. This was a targeted source-level check, not execution of the full `checks.mjs` script, browser testing or CI.
- **Atlas of Biology editorial readiness: 95/100.** This is a conservative editorial/evidence-readiness milestone, not production certification. Remaining work includes wider species-by-species taxonomic review, specialist validation, source reconciliation, full bilingual copy-editing, full local test execution, browser/mobile/accessibility testing, and creation, scientific review and integration of the 52 planned illustrations.

## Bilingual and static accessibility audit — 1 November 2026

- Re-read all 13 Biology HTML pages from `workspace/biology` and ran a remote source audit of language markers, language-switch logic, SVG accessible names, button types, duplicate IDs and external-link safety attributes.
- Russian and English content markers are balanced on all 13 pages; each page updates the document language when the RU/EN switch is used.
- All 16 inline SVG graphics expose an accessible name through `aria-label`, `aria-labelledby` or an image role. All 165 buttons declare `type="button"`; no duplicate HTML IDs were found.
- Reviewed 264 external-link references. No link using `target="_blank"` was found without `rel="noopener"`. This does not establish that every external destination is currently reachable.
- Extended `checks.mjs` with regression assertions for balanced bilingual markers, document-language updates, accessible SVG names and safe new-tab links. The updated script was saved to the branch.
- This was a source-level remote audit. The complete `checks.mjs` program has still not been executed in a local checkout, and no CI or live-browser pass is claimed. Image assets, independent specialist review and real-device/browser accessibility verification remain open publication tasks.
- **Atlas of Biology editorial readiness remains 95/100.** The static audit strengthens the evidence base but does not close a major publication gate or justify an additional score point. The five remaining points are reserved for executable test/CI evidence, live browser and device checks, independent specialist validation, and creation/review/integration or formally approved deferral of the 52 planned illustrations.

## Internal navigation and fragment audit — 1 November 2026

- Followed all local HTML links and fragment targets across the 13 Biology pages and the shared `portal.html` entry point. The remote audit covered 95 local HTML references, including the two links back to the main portal; no missing target pages or element IDs were found.
- Extended `checks.mjs` so future local test runs verify fragment targets as well as the existence of local files. The check deliberately skips external URLs and non-HTML document fragments, which require separate validation methods.
- This is a remote source audit, not a claim that all external links resolve or that the test script has been executed. Overall Biology editorial readiness remains **95/100**; no extra score point is assigned for a bounded navigation check. The remaining publication gates are executable tests/CI, live browser and device/accessibility QA, independent specialist validation, and creation/review/integration or explicit editorial deferral of the 52 planned illustrations.

## Final 100% completion gates — control checklist

The 100% milestone is reserved for a reproducible release-readiness record, not for a larger amount of prose or a subjective percentage increase.

- [x] Thirteen bilingual HTML pages are present: the landing page, ten global foundation chapters and two Kyrgyzstan regional chapters.
- [x] Chapter navigation, local HTML page targets and 95 local HTML link/fragment references have been checked; the current remote audit found no broken local HTML targets.
- [x] The 52 image placements have unique IDs, bilingual briefs, priorities, target filenames, aspect ratios and a central insertion map. This satisfies the project's instruction to leave exact image placeholders where finished artwork cannot yet be integrated. The 52 visual assets themselves are **not** claimed as generated or approved.
- [x] Static source review found balanced RU/EN markers on all 13 pages, accessible names on all 16 SVGs, explicit button types on all 165 buttons, no duplicate IDs, and safe `noopener` handling for new-tab external links.
- [ ] Execute `node biology/checks.mjs` in a real repository checkout and record the complete output; a remote source inspection is not execution.
- [ ] Obtain a successful CI result for the final commit, or document a reproducible equivalent test run if repository CI is unavailable.
- [ ] Complete live browser/device QA for both languages, interactive state changes, keyboard-only navigation, screen-reader announcements and narrow mobile layouts. The attempted live GitHub Pages URL was not accessible to the available browser check.
- [ ] Obtain independent specialist review for the remaining taxonomic and species-identification uncertainties, especially freshwater fish records, and independent Russian–English copy-editing. Editorial caveats and source audits do not substitute for expert sign-off.

Until the four unchecked release gates are evidenced, the atlas remains at **95/100 editorial readiness**. Artwork production remains transparently deferred behind the 52 exact placeholders; no generated, reviewed or integrated image is implied by this checklist.



## Browser QA harness enhancement — 1 November 2026

- Extended `biology/browser-smoke.mjs` to check horizontal overflow at the 390 px mobile and 1365 px desktop viewports, visible interactive controls without accessible names, and whether keyboard Tab navigation reaches an interactive element.
- Retained the existing checks for all Biology pages, HTTP responses, main landmarks, language-toggle changes, explicit button types and uncaught page errors.
- The workflow `.github/workflows/biology-checks.yml` already installs Chromium and runs this browser smoke test after the static check; no workflow outside the Biology scope was changed.
- Saved the enhanced test harness to `workspace/biology` in commit `e53162accc658938963037b8a5a2945b6f7c9c75`.
- This is an improvement to test coverage, not a test result. The browser workflow has not yet been run against this commit; the full local check script and independent specialist review also remain outstanding. The overall readiness score therefore remains **95/100** until evidence is available.


## Illustration-anchor integrity checkpoint — 1 November 2026

- Cross-checked the central `IMAGE_INSERTION_MAP.md` against all 13 Biology HTML pages: exactly 52 planned illustration rows and 52 in-page placeholder anchors are present, with a one-to-one match, no duplicate IDs, and no missing map/page entries.
- Added a regression check to `biology/checks.mjs` so the 52-row count, unique target filenames, unique placeholder IDs and map-to-page correspondence are checked during the full test run.
- Re-read the updated check script from GitHub and confirmed the new regression block is present. The one-to-one audit was performed against the remote source contents; the full Node test program has not yet been executed in a repository checkout.
- The generated-asset directory is not present in the branch. The 52 image briefs remain placeholders, as required until artwork can be produced, scientifically reviewed and integrated. No image asset is claimed as completed.
- Saved the test enhancement and its correction in `workspace/biology`; the illustration-integrity checkpoint was recorded in commit `38cceb5bdd8dfda5b8c206618fdef040c1d386c1`. The full Node test program has not yet been executed in a repository checkout. Overall editorial readiness remains **95/100** pending execution of tests/CI, live browser/device QA, and independent specialist review.


## Final 100% closure plan — control markers

The remaining five percentage points are reserved for evidence, not additional prose. Do not mark the atlas 100% until every gate below is closed and its evidence is recorded in this README and the relevant QA/audit files.

- [x] **G1 — Static validation:** passed in clean GitHub Actions checkout on commit `275fdb602b858e8fdda1b171b6468fa4afeb4122`; `node biology/checks.mjs` completed successfully in run [#41275274366](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41275274366).
- [x] **G2 — Browser validation:** passed in Chromium on the same commit and run. All 13 pages passed at 390px and 1365px; 26 language-toggle interactions completed; no missing accessible names, horizontal overflow or uncaught page errors were reported.
- [x] **G3 — CI evidence:** the Biology workflow completed successfully on the `workspace/biology` push trigger. Run [#41275274366](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41275274366), commit `275fdb602b858e8fdda1b171b6468fa4afeb4122`, job `validate` — success. The run includes both the Node static suite and Chromium browser suite.
- [x] **G4 — Internal scientific audit:** complete; four planned author-side blocks (4/4, 100%). Unresolved taxonomy/source questions remain qualified or deferred in the atlas. External specialist consultation is optional.
- [x] **G5 — Internal editorial and bilingual audit:** complete; four planned author-side blocks (4/4, 100%). Structural parity and editorial corrections are recorded. External professional copy-editing is optional.
- Optional consultation materials: [EXTERNAL_REVIEW_PACKET.md](EXTERNAL_REVIEW_PACKET.md) and [INDEPENDENT_REVIEW_HANDOFF.md](INDEPENDENT_REVIEW_HANDOFF.md) are archived for possible future use only. The measured [BILINGUAL_PARITY_AUDIT.md](BILINGUAL_PARITY_AUDIT.md) is an author-side check, not a claim of independent professional translation certification.
- [x] **G6 — Illustration disposition (deferred):** all 52 assets are explicitly deferred in [IMAGE_DISPOSITION_REGISTER.md](IMAGE_DISPOSITION_REGISTER.md), with rationale, source/licence status and verified placeholder integration. The 13 P1 briefs have detailed review in [IMAGE_SCIENTIFIC_REVIEW.md](IMAGE_SCIENTIFIC_REVIEW.md); the remaining 39 P2/P3 briefs have individual review in [IMAGE_BRIEF_REVIEW.md](IMAGE_BRIEF_REVIEW.md). No images have been generated or sourced; visual production remains pending.

**Control rule:** keep the readiness score evidence-based. G4 and G5 are the internal scientific and editorial/bilingual audits; each is complete at 4/4 planned blocks (100%). G6 is closed as a documented deferral only; the 52 visual assets have not been produced. Portal feedback integration and remaining accessibility/device checks are tracked separately. Save each completed stage and update this plan only with verifiable evidence.


## Source-level structure audit — 1 November 2026

A read-only audit of the 13 HTML pages on `workspace/biology` confirmed:

- All 13 pages contain a declared document language, a responsive viewport declaration, a main landmark, a language-switch control and code to update the document language.
- All 13 pages contain both Russian and English content markers in balanced pairs.
- No duplicate HTML IDs were found within any individual page.
- The illustration inventory remains exactly 52 mapped placeholders, with 52 unique anchor IDs and 52 unique target filenames; all 52 page anchors match the central map in both directions.
- These are source-level checks against the current GitHub file contents. They do **not** replace execution of `checks.mjs`, browser automation, the CI workflow, real-device testing or expert review.

Latest documentation checkpoint at the time of this entry: `01d77b7ef93ccb89be2172a6cc478066e0f87bd3`. Keep the readiness score at **95/100** until the remaining release gates have actual evidence.

## Bilingual learning-clarity pass and follow-up source audit — 1 November 2026

- A subsequent editorial commit, `67dc12b7d5793e1d73c5f58047027c6a707fef07`, revised key explanations across all 12 chapter pages in Russian and English while retaining the existing scientific terminology, chapter structure and interactive learning features.
- Re-read the current source of all 13 Biology HTML pages after that pass. Each page still declares its document language, viewport and main landmark; each has a language-switch control and document-language update logic.
- The Russian and English content-marker counts remain balanced on every page. The audit found no duplicate IDs, no buttons missing explicit `type="button"`, and no inline SVG without an accessible name.
- This is a read-only source audit of the current GitHub branch. It does not establish that the rewritten text has passed independent bilingual copy-editing, that interactive behavior works in a real browser, or that the Node/Playwright test suites have executed.
- The 100% closure gates remain open until their evidence is recorded. Keep the readiness score at **95/100**; the content-clarity pass is substantive progress but does not replace executable validation, CI, specialist review or release QA.


## Readiness-score and CI status clarification — 1 November 2026

- Earlier entries in this README record interim **98/100** and **99/100** editorial-readiness milestones for bounded content and taxonomic-review stages. Those historical scores are not the current whole-atlas release score.
- The later 100% closure framework deliberately applies a stricter, evidence-based standard across the entire Biology branch. Under that framework, the current controlled score is **95/100** until executable validation, browser/device QA, independent scientific and bilingual review, and the illustration disposition are evidenced. Do not read the earlier chapter-stage scores as a claim that the full atlas is 99% release-ready.
- At this earlier checkpoint, the GitHub Actions query for `workspace/biology` returned no workflow runs and no commit-status entries. This was an absence of CI evidence at that time; the later push-triggered successful run is recorded below.
- At that checkpoint, the default-branch workflow only listed pushes to `main`. The Biology-branch copy was subsequently updated to include `workspace/biology`, enabling the successful push-triggered run recorded below. No change was made to `main`, and no PR or merge was created.
- Current source checkpoint before the osman synonym cross-check: `095aa61045eb3d092dd74c145af05fda99776380`.


## Freshwater field-evidence update — 1 November 2026

- Added the Osh State University notice of the 30 July–4 August 2026 joint Kempir-Abad basin expedition with Fergana State University. The chapter records the reported 14 fish identifications, five surveyed lower-river reaches, the separate upper-Jazy / Kara-Shoro observations concerning `Diptychus maculatus`, and pending molecular-genetic analysis of samples from two taxa. The notice does not publish the full species list, so the number is not treated as a complete reservoir or oblast checklist.
- Added the 2025 *Vestnik KRSU* paper reporting 2024 fish research in the Suusamyr, Karakol and Uch-Emchek rivers. The chapter and species audit preserve the source's four named fish taxa and explicitly flag the abstract's "four recreational species plus one weed species" wording against the four-species total in the body/conclusion.
- Documented the unresolved `Triplophysa stoliczkai` identification: the current Eschmeyer's Catalog of Fishes entry treats `Triplophysa elegans` as valid and includes Kyrgyzstan in its stated range, while the IUCN assessment for `T. stolickai` uses a different taxonomic concept and range. The Atlas retains the paper's author-reported identification pending voucher/specimen review rather than silently changing the name.
- Updated `KYRGYZSTAN_SPECIES_AUDIT.md` and added regression assertions in `checks.mjs` for both new field-evidence records and their scope/taxonomy caveats.
- At the time of this field-evidence entry, the Node, Playwright and CI suites had not yet been executed. Their later successful run is recorded in the CI validation section below; G4–G6 remain open and the controlled readiness score remains **95/100**.
- Evidence sources: [Osh State University, 5 August 2026](https://oshsu.kg/public/en/news/4569); [*Vestnik KRSU*, 2025, DOI 10.36979/1694-500X-2025-25-12-159-166](https://vestnik.krsu.kg/en/archive/220/8664); [Eschmeyer's Catalog of Fishes](https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatget.asp?spid=53209); [IUCN assessment](https://doi.org/10.2305/IUCN.UK.2022-1.RLTS.T168488A1186806.en).


## Post-fieldwork source-integrity audit — 1 November 2026

A fresh read-only audit was performed against the current `workspace/biology` tree after the Kempir-Abad and Suusamyr updates:

- All 13 Biology HTML pages still have balanced Russian/English content markers; no duplicate IDs were found.
- All 165 Biology-page buttons declare `type="button"`; all 16 inline SVGs expose accessible names.
- Checked 95 local file references and local HTML fragment links across the 13 Biology pages and the shared portal entry point: no missing local targets or broken HTML fragments were found.
- Checked 246 external links in those pages and the portal entry point: no link opening a new tab lacked a safe `noopener` or `noreferrer` relation.
- The image map remains 52 rows with 52 unique anchor IDs and filenames, matching all 52 page placeholders in both directions.
- At the time of this source-integrity audit, these were remote source-content checks rather than executed tests. G1–G3 were later completed by the successful workflow run below; G4–G6 remain open and the score remains **95/100**.
- Audit source revision: `095aa61045eb3d092dd74c145af05fda99776380`.


## Freshwater fish synonym reconciliation — 1 November 2026

- Cross-checked the Suusamyr paper's `Diptychus gymnogaster` against the current Eschmeyer's Catalog of Fishes entry (13 August 2026): the catalogue treats that name as a synonym of `Diptychus maculatus`. The 2020 IUCN assessment for `D. maculatus` also lists `D. gymnogaster` as a synonym.
- Updated the bilingual fauna account and species audit so the two names are not counted as separate species. The text links the 2025 Suusamyr paper to the 2026 Kempir-Abad research notice, which separately reports further taxonomic observations on `D. maculatus` in the upper Jazy; no unpublished result is inferred.
- Strengthened the freshwater image-review constraints so future artwork does not duplicate the synonym as a second fish species or invent taxa from the unpublished Kempir-Abad list. Added regression assertions for these safeguards.
- This is a source-based nomenclatural cross-check, not specimen identification or independent ichthyologist sign-off. The Suusamyr paper's `Triplophysa stoliczkai` determination and its abstract/body fish-total discrepancy remain open for specialist clarification.
- Sources: [Eschmeyer's Catalog — `Diptychus gymnogaster`](https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatget.asp?spid=31906); [IUCN — `Diptychus maculatus`](https://doi.org/10.2305/IUCN.UK.2020-3.RLTS.T128719071A128719148.en).
- G4 remains open; no change to the controlled **95/100** readiness score.


## Post-synonym source verification — 1 November 2026

After the latest fish-taxonomy and illustration-guard updates, all 13 Biology HTML pages were re-read from GitHub:

- Russian and English marker counts remain balanced on all 13 pages.
- No duplicate HTML IDs; all 165 Biology-page buttons have explicit `type="button"`; all 16 inline SVGs have accessible names.
- All 52 image-map rows and all 52 in-page placeholders remain unique and in one-to-one correspondence.
- The new Kempir-Abad, Suusamyr, `Triplophysa` uncertainty and `Diptychus gymnogaster` synonym assertions are present in `checks.mjs`; the corresponding chapter, audit and image-review wording is present.
- No Biology-page external link opening a new tab was found without `rel="noopener"`.
- At the time of this read-only source check, the full Node, Playwright and CI suites had not yet run. The later workflow closed G1–G3; independent scientific review, editorial release review and illustration disposition remain open.
- Branch checkpoint before this documentation entry: `e7104273b6ae7ab4f09bd2637511fcce85bb2143`.


## Static-checker repair and in-memory preflight — 1 November 2026

- A syntax compilation pass exposed two malformed regular expressions in `checks.mjs`: the planned-image path pattern had escaped its forward slashes twice, and the insertion-map pattern did not match a literal leading pipe. Both expressions are corrected.
- Re-ran JavaScript syntax compilation for `checks.mjs` and `browser-smoke.mjs`; both compile successfully.
- Executed the current `checks.mjs` assertion logic in an in-memory V8 compatibility harness using the GitHub-fetched `workspace/biology` files and repository tree. Result: **PASS** — 13 HTML pages, 88 local paths, 13 inline scripts syntax-compiled, and 165 explicitly typed buttons; no assertion failures.
- The harness supplies in-memory filesystem/path and inline-script compilation shims. It was a useful preflight, but not a clean local checkout. G1 was subsequently closed by the real Node run in GitHub Actions; G2 and G3 were closed by the same successful workflow run.
- The initial preflight surfaced 12 stale wording assertions after the bilingual editorial pass. Those assertions were aligned to the actual current RU/EN text and re-run; the harness now passes. The scientific claims themselves were not weakened to make the tests pass.
- Source checkpoint before this note: `e4ce15919286a1bba704685b3071225161b352b3`. Readiness remains **95/100** until all closure gates have their required evidence.


## Son-Kul fish taxonomy review and regression re-run — 1 November 2026

- Added the 2023 *Bulletin of KNAU* Son-Kul fisheries paper to the regional source audit, preserving the discrepancy between its abstract's 2021–2023 fieldwork description and the Methods section's 2020, 2021 and 2023 sampling years.
- Recorded the paper's processed sample counts as study material, not population estimates: 100 `Coregonus lavaretus`, 1 `C. peled`, 13 `Diptychus dybowskii`, 2 `D. dybowskii micromakulatus`, 17 `Triplophysa stoliczkae` and 4 `Phoxinus brachurus`.
- Cross-checked the Son-Kul `Triplophysa` determination against IUCN/FishBase and Eschmeyer's Catalog of Fishes. The sources use different taxonomic concepts and range treatments; the chapter now retains the study authors' determination and explicitly requires voucher/genetic review rather than resolving the discrepancy by spelling alone.
- Updated the freshwater image review to prevent either the Son-Kul or Suusamyr disputed `Triplophysa` record from being depicted as a settled species identification.
- Added regression checks for the new Son-Kul source-audit row and taxonomy caveat. Re-executed the in-memory V8 compatibility preflight after these changes: **PASS** — 13 pages, 88 local paths, 13 inline scripts syntax-compiled, 165 typed buttons, no assertion failures.
- This preflight did not replace a clean Node checkout run or real Chromium/Playwright QA. Those gates were subsequently closed by the successful workflow run below; independent ichthyologist review and the remaining release gates are still pending.
- Source checkpoint before this note: `7012896d02cadc2a02a5d756e97224d202813b4b`.


## CI trigger preparation — 1 November 2026

- Updated the Biology-branch copy of `.github/workflows/biology-checks.yml` so its `push` trigger includes `workspace/biology` as well as `main`. This is a preparatory change intended to run the same Node and Chromium checks on future authoring-branch pushes once the workflow definition is available from the default branch.
- The default-branch (`main`) copy was read-only checked and still lists only `main` under `push.branches`. GitHub Actions has returned no runs for `workspace/biology`, and the latest branch commit has no combined-status entries. The branch-local trigger alone cannot activate a workflow that has not yet been updated on the default branch.
- No change was made to `main`; no pull request or merge was created. The workflow's existing manual-dispatch option remains available to an authorized repository user, but this session has no dispatch action.
- The CI trigger change was followed by successful G1–G3 execution in run [#41275274366](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41275274366) on commit `275fdb602b858e8fdda1b171b6468fa4afeb4122`. Earlier empty-run checks and failed diagnostic runs are historical; the final run completed successfully.
- Branch checkpoint before this documentation entry: `f81bb19def78ea4c74f6889091e91e182696d9ee`.


## CI and Chromium validation pass — 1 November 2026


- **Run:** [GitHub Actions #41275274366](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41275274366)
- **Commit tested:** `275fdb602b858e8fdda1b171b6468fa4afeb4122`
- **Job:** `validate` — **success**.
- **Static suite:** `node biology/checks.mjs` passed in a clean GitHub Actions checkout: 13 HTML pages, local links/scripts and regression assertions.
- **Browser suite:** `node biology/browser-smoke.mjs` passed with Chromium on all 13 pages at mobile (390px) and desktop (1365px) widths; 26 language-toggle interactions; no missing accessible names, horizontal overflow or uncaught page errors.
- The first browser run exposed an empty nested catalogue link in the fauna chapter. The nested anchor was repaired, a regression assertion was added, and the subsequent complete run passed.
- G1–G3 are now closed with a recorded successful workflow run. G4 independent scientific review and G5 independent bilingual/release review remain open. G6 is now closed as an explicit 52-asset deferral; actual visual production remains pending. Therefore the controlled readiness score remains **95/100**.


## Independent reviewer handoff prepared — 1 November 2026

- Created [`EXTERNAL_REVIEW_PACKET.md`](EXTERNAL_REVIEW_PACKET.md) with the G4 scientific review register, high-priority fish/taxonomy and locality questions, G5 bilingual editorial checklist, and formal sign-off records.
- The packet deliberately separates the author's source audit from independent approval. It identifies the open Son-Kul, Suusamyr and Kempir-Abad fish questions, argali sample-provenance discrepancy, maral count conflict, Tibetan Snowcock locality gap, reptile count discrepancy and amphibian status checks.
- Added regression assertions so the packet retains both review scopes and the requirement for qualified independent sign-off.
- This prepares external review but does not complete it. G4 and G5 remain unchecked until qualified reviewers return their findings and sign-offs. G1–G3 remain supported by the successful CI run recorded above; the controlled readiness score remains **95/100**.
- Source checkpoint before this note: `da1edffbdbd9ea33f40170b9f260fa0f3cebf7dc`.


## G6 illustration disposition closed by explicit deferral — 1 November 2026

- Created [`IMAGE_DISPOSITION_REGISTER.md`](IMAGE_DISPOSITION_REGISTER.md) with an individual disposition for all 52 target assets, including exact anchor and filename, priority, deferral reason, source/licence status, brief-review status and future activation criteria. Added [`IMAGE_BRIEF_REVIEW.md`](IMAGE_BRIEF_REVIEW.md) for the 39 P2/P3 briefs; the 13 P1 briefs remain covered by [`IMAGE_SCIENTIFIC_REVIEW.md`](IMAGE_SCIENTIFIC_REVIEW.md).
- All 52 are **Deferred**, not **Produced**. No third-party image was inserted without verified licence/attribution; no generated WebP was claimed to exist. The user-approved image-note fallback remains in place at all 52 anchors.
- Updated `IMAGE_INSERTION_MAP.md` to link the disposition register and clarify that visual production remains pending.
- Added regression assertions requiring 52 unique deferral rows matching the 52 mapped page anchors. The gate is closed as a disposition decision only; it does not certify that the Atlas has its final illustrations.
- G6 is checked. G4 and G5 still require qualified independent reviewers. Readiness remains **95/100**.
- Source checkpoint before this note: `7abcaca92c9c2796e19241551fd0d4282ff36dbe`.


## Complete image-brief review coverage — 1 November 2026

- The detailed P1 review covers all 13 highest-priority Kyrgyzstan flora/fauna assets.
- Created `IMAGE_BRIEF_REVIEW.md` with individual scientific constraints for the remaining 39 P2/P3 briefs, bringing brief-level review coverage to all 52 mapped assets.
- Updated `IMAGE_DISPOSITION_REGISTER.md` so each deferred P1 row points to the detailed review and each deferred P2/P3 row points to the individual brief review.
- Added regression checks for the 39 P2/P3 review rows, the 13 P1 asset-to-review matches and all 52 deferral dispositions.
- All 52 images remain **Deferred**; no image file has been generated, sourced or inserted. The brief reviews are complete, but actual image production and asset-level QA remain pending.
- G6 remains closed as an explicit deferral decision; G4 and G5 remain open. Readiness remains **95/100**.
- Source checkpoint before this note: `e5d52491ebc3b219e68bb82203dd96c6c012c9e5`.


## Bilingual parity audit added — 1 November 2026

- Created [`BILINGUAL_PARITY_AUDIT.md`](BILINGUAL_PARITY_AUDIT.md): all 13 pages have balanced RU/EN content-block counts, totalling 1,136 paired blocks.
- Numeric-token multisets match in all 1,136 block pairs. Scientific-name sets match across the Russian and English content blocks on every page; the Kyrgyzstan flora and fauna chapters contain 34 and 69 unique Latin-name strings respectively in each language.
- The audit found and corrected an English/Russian evidence-scope gap in the Himalayan Snowcock note; it also aligned the OSME 2019 date and two fauna numeric values.
- These checks are now automated in `checks.mjs`. The CI run [#41275876545](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41275876545) passed after adding the parity assertions.
- This is author-side structural parity evidence, not independent copy-editing or an idiomatic-language review. G5 remains open until a qualified bilingual editor signs off.

## Additional core-content development — 1 November 2026

- Added a bilingual lesson on ecosystem productivity and trophic efficiency to `chapters/ecology.html`: GPP/NPP, energy-transfer efficiency, the limits of the simplified “10% rule”, and the distinction between energy and biomass pyramids. The energy-pyramid SVG includes a title and description for assistive technology. Commit: `e2cb743769ec6f30c1c82633f6b2e8e58ade1e29`.
- Added a bilingual speciation lesson to `chapters/evolution.html`: allopatric and sympatric pathways, prezygotic and postzygotic reproductive barriers, polyploidy and the limits of a single universal speciation model. Commit: `1124de622af9878799cbddeaebe7cc0038894580`.
- Added a bilingual horizontal gene transfer lesson to `chapters/microbiology.html`, distinguishing transformation, transduction and conjugation and qualifying the spread of antimicrobial-resistance genes. Commit: `f183a91c8e90dfb32f29edca02f4f73e90fe783d`.
- Added a bilingual genetics lesson to `chapters/genetics.html` on gene-expression regulation in bacteria and eukaryotes, chromatin accessibility and epigenetic mechanisms; it distinguishes changes in expression from mutations and qualifies transgenerational inheritance. Commit: `a53317046d14b6d939de0e295732e4404d44bc6c`.
- Extended `checks.mjs` with regression assertions for all four additions, including ordering, bilingual presence, core mechanisms and scientific caveats. Test updates: `050662340a112b01b7c7a0094209ccd65ac7a7d3`, `4f6060a0e31afc2e972075b858f193e1b3182d56`, `6fede848c410135dccd164f87aabf6f682f7227b`.
- Focused GitHub source verification confirms each new section is present in its intended chapter and in the expected order. Full `node biology/checks.mjs`, Chromium smoke tests and a new CI run have not yet been executed for these latest commits.
- All 52 illustration insertion anchors remain deferred and must stay matched to `IMAGE_INSERTION_MAP.md` and `IMAGE_DISPOSITION_REGISTER.md`; no image has been marked generated or complete.
- Controlled editorial readiness remains **95/100**. This content expansion does not close the outstanding independent scientific review (G4) or independent bilingual/release review (G5); neither is claimed complete. The next readiness increase requires documented evidence against the existing gates, not simply additional commits.

## Genetics inheritance lesson added — 1 November 2026

- Added a bilingual Mendelian inheritance section to `chapters/genetics.html`: genotype and phenotype, homozygous and heterozygous states, allele segregation and an `Aa × Aa` Punnett square.
- The lesson distinguishes expected genotypic and phenotypic ratios, states the complete-dominance assumption, and explains why many traits do not follow a simple Mendelian pattern.
- The Punnett square is a semantic HTML table with caption and row/column headers; responsive styling was added for narrow screens.
- Chapter commits: `58fb4df00485a74db502973bb29b5a4481710fc2` and `ac6f6a937e5dfc8f76b3f96453167d1869e6e5e4`. Regression assertions: `0947593055409086a77245a376b5f2302767c665`.
- Controlled readiness remains **95/100**; G4 and G5 remain open. The additional chapter material does not replace independent review.

## Cell communication lesson — 1 November 2026

- Added a bilingual cell-signalling lesson to `chapters/cell-biology.html`, covering contact-dependent, paracrine, endocrine and synaptic signalling; receptor activation; intracellular relay proteins and second messengers; amplification, feedback and pathway cross-talk.
- Added an accessible explanatory SVG with a title and description. The diagram is explicitly identified as a general pathway model, not a specific molecular mechanism.
- Focused regression assertions were added to `checks.mjs` for content, bilingual structure, placement and SVG accessibility.
- Chapter commit: `d7c3c181dc3c5f486d3cabf78ce2fb0da9c496b9`. Regression-check commit: `bd0009d56bace3c1b20f11012ed5d6e61151d6e6`.
- Full Node.js, Chromium and CI checks have not yet been run for this latest addition. Controlled editorial readiness remains **95/100** pending G4/G5 independent reviews.

## Cell-cycle regulation and apoptosis — 1 November 2026

- Added a bilingual lesson to `chapters/cell-biology.html` on G1/S, G2/M and spindle-assembly checkpoints; cyclin–CDK regulation; DNA-damage responses; apoptosis and necrosis; and the relationship between disrupted control pathways and tumour development.
- The text distinguishes general mechanisms from oversimplified one-cause explanations and avoids presenting apoptosis/necrosis as an exhaustive classification of all cell-death processes.
- Added regression assertions for the mechanisms, distinctions, bilingual blocks and section order.
- Chapter commit: `f96f28c4386afca6e23437d0aedc14bc49233323`. Test commit: `6d680c4e08ea76372b9232bd2b00c6eb58622707`.
- Focused read-back and complete Node.js/Chromium/CI execution remain pending. Controlled readiness remains 95/100; independent gates G4 and G5 remain open.

## Homeostatic control and feedback lesson — 1 November 2026

- Expanded `chapters/anatomy.html` with a bilingual explanation of negative-feedback control loops, receptor/integrator/effector roles and physiological ranges.
- Added applied examples: thermoregulation, insulin/glucagon control of blood glucose, vasopressin and water balance, plus bounded positive-feedback examples in labour and blood clotting.
- Added an accessible SVG feedback-loop overview with a title, description and bilingual labels. The text distinguishes positive/negative feedback by direction of effect, not by value judgement.
- Added regression assertions for the mechanisms, examples, bilingual content, section placement and SVG accessibility.
- Chapter commit: `851d39f57321940c90562b681fd59b7578b2895e`. Test commit: `4cc01025f6066befd783b9b745747392ae14cbab`.
- Full Node.js, Chromium and CI runs have not yet been executed on these latest commits. Controlled readiness remains **95/100** pending G4/G5 independent review.


## Renal physiology and nephron regulation — 1 November 2026

- Added a bilingual renal-physiology lesson to `chapters/anatomy.html`, covering glomerular filtration, selective tubular reabsorption and secretion, aldosterone, vasopressin and the renin–angiotensin–aldosterone system (RAAS).
- Added an accessible bilingual nephron SVG with a title and description. The text distinguishes filtration from reabsorption and explains that filtration rate and urine output vary with physiological state.
- Added regression assertions for lesson placement, bilingual content, the three renal processes, hormonal regulation, physiological qualifications and SVG accessibility.
- Chapter commit: `029a51f04974c6e6c1a06065bdec60c8bd1f09c5`. Nephron flow-arrow refinement: `a85f987c716a5d71cda01a11bdc99a5b80e53de8`. Regression-check commit: `c3a24ceae7d3b933118ab5f9cdd9a5bb7de7d99c`.
- Focused GitHub read-back and assertion review are pending. The full Node.js suite, Chromium smoke suite and CI have not been run on these commits. Controlled readiness remains **95/100**; independent G4/G5 reviews remain open.
- No new image insertion anchor was added; the existing 52-image map and deferral register are to remain unchanged.


## Cardiovascular physiology and cardiac conduction — 1 November 2026

- Added a bilingual cardiovascular physiology lesson to `chapters/anatomy.html`: cardiac cycle (diastole and ventricular systole), stroke volume and cardiac output, the electrical conduction sequence (SA node → atria → AV node → His bundle and branches → Purkinje fibres), baroreceptor reflex, and integration with renal RAAS and vasopressin regulation.
- Added an accessible SVG flow diagram for cardiac electrical conduction with bilingual title and description.
- Included the cardiac-output relationship and explicit distinctions between heart rate, cardiac output and arterial pressure; clarified rapid baroreflex versus longer-term renal/hormonal regulation.
- Chapter commit: `af8a0108af71f0c93d10ff2b70dddb1be04cacd1`. Regression-check commit: `55a7262c61db31b4d6d6ea3d5dc14bfe8a30b0dd`. Boundary correction in regression assertions: `3ca37b077b4cd0ab829394e1b562843f6f495b48`.
- Focused read-back verification is pending. Full Node.js, Chromium and CI checks have not yet been run on these commits. Controlled readiness remains **95/100**; independent G4/G5 reviews remain open.
- Existing 52 image anchors and all Deferred dispositions are to remain unchanged.


## Illustration marker readiness audit — 1 November 2026

- Audited all 52 mapped illustration markers against the actual 13 page files: 52/52 anchors exist, IDs are unique, descriptions are non-empty and all markers contain Russian and English brief text.
- The insertion map and disposition register match 52/52; all 52 remain intentionally deferred. Priority allocation is 13 P1, 26 P2 and 13 P3. All 13 P1 briefs match the detailed scientific review; all 39 P2/P3 briefs match the individual brief review.
- Actual asset inventory: the Biology root has no `images/` directory, `images/generated/` is absent, and the 13 marker-bearing pages contain 22 inline SVGs but zero HTML raster-image elements. No WebP asset is claimed as generated.
- Corrected the stale SVG inventory count in `IMAGE_GENERATION_PLAN.md` from 16 to 22.
- Added `IMAGE_READINESS_AUDIT_2026-11-01.md` with the full marker audit, asset-pipeline limitation, production sequence and scientific holds (especially freshwater fish taxonomy and Batken Aygul/wild tulips).
- Audit commit: `1cc58a7da6c13c53c8693452fa3f975739b5a906`. Plan update commit: `5591bf5f4089eef983a282269777e1154afe9623`.
- No marker IDs, positions, filenames, priorities or page anchors were changed. No image was generated or marked complete. A verified binary-image ingestion route is still required before a rendered image can be committed at its exact WebP path.


## First illustration production attempt — 1 November 2026

- Generated a local 1280×720 concept preview for the Batken flora P1 brief, pairing Aygul-like fritillary and an unlabeled wild-tulip depiction. It is a local working-session file only, not committed to the repository or integrated into the chapter.
- The original generated sheet labeled the tulip `Tulipa greigii`; that label was removed. The chapter lists other Batken tulip taxa, so the tulip morphology remains unverified and must not be identified or published without botanical review. Aygul nomenclature must follow the chapter's `Petilium eduardii` usage.
- Detailed cautions and the decision to keep the marker deferred are recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- No page markers or disposition statuses changed. Controlled readiness remains 95/100; G4/G5 remain open.


## Second illustration production attempt — 1 November 2026

- Generated a six-panel mountain biodiversity concept sheet (ImageGen generation ID `decb1eeb-b86a-4b4c-abc7-9d6e5efcdd66`) and extracted three local square WebP review crops: snow-leopard-like cat (500×500), golden-eagle-like raptor (496×500), and an unidentified horned mountain ram (498×500).
- These are generated concepts, not field photographs or verified Kyrgyzstan locality records. The ram is deliberately left taxonomically unresolved; no argali/subspecies or regional claim is approved. All three require expert visual review.
- The local files are not in GitHub and are not integrated into chapters. Full source and caution notes are in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- All 52 image anchors and Deferred dispositions remain unchanged. Controlled readiness remains 95/100; G4/G5 remain open.


## Third illustration production attempt — 1 November 2026

- Generated a six-panel alpine biodiversity concept collage (ImageGen generation ID `d34da22d-d7e5-4247-9be9-e2f29d102e1a`) and cropped six separate local WebP candidates: snow-leopard-like cat (509×508), eagle-like raptor (502×508), argali-like ram (508×508), partridge-like bird (509×508), unidentified marmot (502×508) and unidentified butterfly (508×508).
- Species identities are intentionally unassigned where the generated morphology is insufficient. These are concept illustrations, not documentary wildlife photographs or verified Kyrgyzstan locality records.
- All six remain local-only drafts, not committed or integrated. Scientific holds and provenance are documented in `IMAGE_DRAFT_REVIEW_2026-11-01.md`.
- The 52 illustration markers and Deferred dispositions are unchanged. Readiness remains 95/100; G4/G5 remain open.


## Fourth illustration production attempt — 1 November 2026

- Generated a six-panel alpine biodiversity concept collage (ImageGen generation ID `a8488692-9869-4410-bd90-6443aa2631e1`) and extracted one distinct botanical crop: an unidentified edelweiss-like alpine flower (503×507 WebP).
- The flower is not identified to genus or species; it is not evidence of a Kyrgyzstan locality. Repeated wildlife panels were not counted as new assets.
- The candidate remains local-only, uncommitted and unapproved. See `IMAGE_DRAFT_REVIEW_2026-11-01.md`. All 52 markers remain Deferred; readiness remains 95/100.


## Fifth illustration production attempt — 1 November 2026

- Generated collage ID `727a305a-0525-40e2-a221-34f9d82156b0`; extracted one new local WebP candidate, a red-orange pendant bell-shaped alpine flower (505×504).
- Taxonomic hold: do not label as `Petilium eduardii`, `Fritillaria`, or another taxon without botanical review. No Kyrgyzstan locality is established.
- Candidate remains local-only, uncommitted and unapproved. All 52 insertion markers remain Deferred; readiness remains 95/100. See `IMAGE_DRAFT_REVIEW_2026-11-01.md`.


## Sixth illustration production attempt — 1 November 2026

- Generated a standalone square alpine-flower concept (ImageGen ID `e4c6a92e-803e-4c4e-9b1f-d9ff6fe68671`) and created local WebP `biology-fritillary-like-flower-standalone-candidate.webp` (1254×1254).
- It is only visually fritillary-like; no genus/species attribution or Kyrgyzstan locality is claimed. Expert botanical review is required.
- Local-only, uncommitted and unapproved. Existing 52 image markers remain Deferred. Readiness remains 95/100.


## Seventh illustration production attempt — 1 November 2026

- Generated standalone snow-leopard-like wildlife concept (ImageGen ID `52ae788d-57df-49ea-ade4-598d8f1ad812`); local WebP candidate `biology-snow-leopard-standalone-candidate.webp` (1254×1254).
- It is generated concept art, not a field record; no location, individual, behavior or population is inferred. Anatomical/zoological review remains required.
- Local-only, uncommitted and unapproved. The repeated flower attempt was not counted as a new candidate. Markers remain unchanged; readiness remains 95/100.


## Illustration quality-control audit — 1 November 2026

- Three further generation attempts repeated the existing snow-leopard composition; they were explicitly excluded from the new-candidate count.
- The next distinct P1 target is `fauna-birds.webp`. The chapter's named examples include `Aquila chrysaetos`, `Gypaetus barbatus`, `Tetraogallus himalayensis` and `Ciconia nigra`, alongside wetland birds. See the review log for habitat-separation requirements.
- No new image asset, chapter insertion or marker-status change resulted from this audit. All 52 markers remain Deferred; readiness remains 95/100.


## Eighth illustration production attempt — 1 November 2026

- Generated a distinct horizontal golden-eagle-in-flight concept (ImageGen ID `95b58769-7232-4b29-bea2-5c2ac391a9c2`); local WebP `biology-golden-eagle-flight-candidate.webp` (1536×1024, 233,558 bytes).
- Intended for the `Aquila chrysaetos` subject, but species-level anatomy and plumage require ornithological review. It is concept art, not a field record or verified Kyrgyzstan locality.
- Local-only, uncommitted and unapproved. All 52 markers remain Deferred; readiness remains 95/100. See the image review log.


## Ninth illustration production attempt — 1 November 2026

- Generated a perched golden-eagle visual variant (ImageGen ID `1191d3c1-3f8d-474b-b05a-b1c4fdb3d4d8`); local WebP `biology-golden-eagle-perched-candidate.webp` (1536×1024, 337,922 bytes).
- This is a different pose from the flight draft, but repeats the golden-eagle subject and does not complete the P1 multi-species bird plate. Expert ornithological review remains necessary.
- Local-only, uncommitted and unapproved; no chapter insertion or marker change. All 52 markers remain Deferred; readiness remains 95/100. See the image review log.


## Tenth illustration production attempt — 1 November 2026

- Generated a bearded-vulture-like alpine bird concept (ImageGen ID `ab53454c-977c-4c89-8b84-c15459d6e227`); local WebP `biology-bearded-vulture-candidate.webp` (1536×1024, 336,576 bytes).
- Intended as a visual study for the chapter's `Gypaetus barbatus` entry, but species identity and anatomy require ornithological review; the breast colour is not diagnostic evidence.
- Local-only, uncommitted and unapproved. The P1 bird plate and all 52 markers remain Deferred; readiness remains 95/100. See the image review log.


## Illustration queue quality-control — 1 November 2026

- Three further generation attempts repeated the perched bearded-vulture composition (IDs recorded in `IMAGE_DRAFT_REVIEW_2026-11-01.md`); all were excluded as near-duplicates, not new assets.
- The next intended distinct bird subject is Himalayan snowcock (`Tetraogallus himalayensis`). No new raster asset, chapter insertion or marker completion resulted from this cycle.
- All 52 image markers remain Deferred; controlled readiness remains 95/100.


## Gamebird illustration quality-control — 1 November 2026

- Two further bird-image attempts produced a monal-like pheasant and a chukar-like partridge, not a reliable Himalayan snowcock (`Tetraogallus himalayensis`) depiction. Both are excluded from the candidate count; the partridge-like output also repeats an existing concept.
- The snowcock target remains unfulfilled. No new raster asset, insertion or marker completion resulted. All 52 markers remain Deferred; readiness remains 95/100.


## Image production quality-control — 1 November 2026

- A further Himalayan gamebird attempt (ImageGen ID `f4878bf9-3cea-45f2-b522-72c97e52b446`) repeated the rejected monal-like/pheasant appearance and was excluded as a duplicate, not counted as an asset.
- Clarified `IMAGE_DISPOSITION_REGISTER.md`: local-only concept drafts exist for some subjects, but none has passed scientific/editorial approval or been committed/integrated. This replaces the inaccurate blanket wording that no rendered drafts exist.
- The 52 mapped publication assets remain Deferred; controlled readiness remains 95/100.


## User-provided snowcock visual candidate — 1 November 2026

- Reviewed a user-provided 1536×1024 bird image and created a local WebP review copy (`biology-himalayan-snowcock-user-candidate.webp`, 345,724 bytes; not committed).
- The overall alpine gamebird form and chestnut neck markings are relevant, but the dark throat/face pattern does not clearly match the regional description of adult `Tetraogallus himalayensis` (white throat/neck bordered by rufous, spotted creamy crop, darker grey belly). Species identity, local subspecies context, source and licence need expert verification.
- It is a single bird, not the complete mapped 16:9 three-habitat bird plate. No insertion or marker status change; all 52 mapped assets remain Deferred. See `IMAGE_DRAFT_REVIEW_2026-11-01.md`.


## Eleventh illustration production attempt — 1 November 2026

- Generated a horizontal black-stork-at-alpine-wetland concept (ImageGen ID `dff4afc7-e1b8-4f79-9a10-fc7e333c4795`); local WebP `biology-black-stork-wetland-candidate.webp` (1672×941, 346,448 bytes).
- Red bill and legs, dark iridescent upperparts and white underparts broadly fit the intended `Ciconia nigra` study, but species/anatomical review remains required. The wetland setting is regionally plausible; the generated scene is not a field record or verified Son-Kul photograph.
- Local-only, uncommitted, uninserted and unapproved. It supplies only the wetland portion of the 16:9 bird plate; cliff-raptor and alpine-ground-bird components remain necessary. All 52 mapped image assets remain Deferred; controlled readiness remains 95/100 and G4/G5 remain open. See `IMAGE_DRAFT_REVIEW_2026-11-01.md`.


## Full repeat audit — 1 November 2026

- Started a unified editorial, scientific, technical and visual audit of all 13 Biology HTML pages, interactive tools, references, SVGs and the 52-item image production map.
- Completed the initial 5% inventory milestone. The 13-page source scan found balanced Russian/English markers, no duplicate HTML IDs, 22 inline SVG elements and no integrated raster `<img>` assets.
- Confirmed that all 52 mapped image assets remain Deferred; no raster asset is approved or integrated. G4 scientific review and G5 independent bilingual/editorial review remain open.
- Audit findings and method are recorded in `REPEAT_AUDIT_2026-11-01.md`. The 95/100 controlled editorial-readiness score is unchanged; audit completion is tracked separately.


## Full repeat audit — 10% milestone — 1 November 2026

- Completed source-level technical/accessibility review of all 13 pages: one H1 and populated H2 structure per page; named inline SVGs; no unlabeled inputs; no external `_blank` links missing `noopener`; interactive buttons use explicit types and visible labels.
- Inspected the 81 KB regression script and existing bilingual parity report (1,147 RU / 1,147 EN blocks). These are source-level checks, not a fresh test execution or independent language sign-off.
- No confirmed defect justified a speculative code edit. Node/Chromium execution and browser/manual accessibility checks remain pending because a runnable repository checkout and dependencies are not available through the current file connection.
- Detailed findings: `REPEAT_AUDIT_2026-11-01.md`. Audit completion 10%; controlled editorial readiness remains 95/100; G4/G5 remain open.


## 15% milestone — interactive quiz state audit — 1 November 2026

### Completed checks

- Inspected the quiz state model and language-switch handlers in all ten core chapter scripts: Botany, Zoology, Cell Biology, Anatomy and Physiology, Genetics, Microbiology, Ecology, Evolution, Biochemistry and Systematics.
- Confirmed a repeatable state-transition defect: changing RU/EN after answering a question re-rendered the quiz and cleared `quizAnswered` while retaining the current question index and score. A learner could therefore answer the same question again and potentially score twice before advancing.
- Corrected all ten chapter scripts. The answered state now persists through a language switch; it is cleared when the learner explicitly advances to the next question. The Next control remains available when the current question has already been answered.
- Added a regression assertion to `checks.mjs` for all ten core chapters, checking both preservation across re-render and reset on advancement.
- Read-back of the ten chapter changes and regression assertion is recorded as the source-level verification for this milestone.

### Scientific and model review observations

- The sampled DNA transcription model preserves template direction (3′→5′) and complementary RNA output (5′→3′); the example `TAC` → `AUG` is consistent.
- The ecology food-chain builder enforces sequential trophic choices and allows correction by returning to an earlier choice. The explanatory text correctly cautions that real food webs are more complex than the five-step teaching example.
- The microbiology growth-phase model labels the phases as a simplified closed-system pattern and describes the stationary phase as approximate balance between new-cell formation and cell death.
- The evolution selection visual uses illustrative percentage values (50/50 and 78/22); these are model settings, not measured field data. The text frames the result conditionally and notes drift, mutation and gene flow as additional processes.
- These are source-level plausibility checks, not independent scientific sign-off. Targeted claim-to-source sampling in the regional flora/fauna chapters remains in progress.

### Limitations

- No Node.js suite, browser automation, mobile rendering, keyboard interaction or assistive-technology test was executed in this milestone. The new regression assertion is committed but has not yet been run.
- Calculations and state transitions have been inspected in source; real browser behaviour and visual feedback still require execution.
- G4 independent scientific review and G5 independent bilingual/editorial review remain open. All 52 illustration markers remain unchanged and Deferred.

### Change log

- 1 November 2026: advanced the repeat audit to 15%; corrected the shared quiz answer-state defect in ten core chapters and added a regression assertion. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.

## 20% milestone — regional flora/fauna source-traceability pass — 1 November 2026

### Completed source checks

- Rechecked the high-priority national flora claims against the primary publications: Sennikov et al. (2025), *Nordic Journal of Botany*, DOI 10.1002/njb.04731, supports the dated total of 4,043 vascular-plant species, ten new country records, one confirmed record and two exclusions. The chapter correctly presents this as a 2025 published count rather than an immutable total.
- Rechecked the north-eastern aquatic-plant study (2024), DOI 10.1016/j.japb.2023.09.002. The paper supports seven species newly recorded for Kyrgyzstan, a newly detected hybrid, and the treatment of *Stuckenia amblyphylla* as not a separate species. The chapter correctly limits the study to sampled waterbodies in north-eastern Kyrgyzstan rather than claiming a national wetland inventory.
- Rechecked the Ministry / National Academy announcement of 9 June 2026. The 24-month Red Data Book update is ongoing; the cited 89 higher-plant and fungi figure is a number in the announcement/list being prepared, not a completed new Red Data Book edition. The chapter's caveat is appropriate.
- Rechecked the argali genomic paper (Thomson, Davletbakov & Frisina, 2026; *Diversity* 18(3):194; DOI 10.3390/d18030194) against its linked Dryad dataset (DOI 10.5061/dryad.76hdr7t7t). The paper's Methods section says 88 samples were collected in Kyrgyzstan and 72 retained; the dataset abstract describes the 72 retained samples as collected across Kyrgyzstan and Tajikistan. This is a genuine article–dataset geographic metadata discrepancy and must remain unresolved until the sample-provenance table or authors clarify it.

### Confirmed correction saved

- Updated chapters/fauna-kyrgyzstan.html in Russian and English to describe the argali article–dataset discrepancy explicitly, avoid assigning all 72 retained samples to Kyrgyzstan without provenance reconciliation, and cite the correct article and dataset DOIs. The previous DOI placeholder was replaced with the verified DOI 10.3390/d18030194.
- Added a regression assertion in checks.mjs requiring the correct article DOI, dataset DOI and unresolved-provenance caveat to remain in the fauna chapter.
- Updated KYRGYZSTAN_SPECIES_AUDIT.md with the verified bibliographic identifiers and the chapter correction.
- Read-back verification is still required after the final documentation update; no Node.js or browser test execution is claimed.

### Scope and limitations

- This pass verifies selected high-priority claims, not every species account, oblast record, map point or bibliography entry.
- The source-traceability gap remains for many individual species claims where a chapter-wide bibliography is not a direct claim-level citation.
- The seven-oblast framework remains an editorial structure, not seven complete verified species checklists.
- G4 independent scientific review and G5 independent editorial/language review remain open. All illustration markers are preserved; no image production or publication approval is claimed.
- Fresh execution of checks.mjs, browser/mobile rendering, keyboard-only operation, contrast measurement and assistive-technology review remain pending.

### Change log

- 1 November 2026: advanced the repeat audit to 20%; verified selected national flora and regional biodiversity claims against primary sources; corrected the argali genomic sample-provenance caveat and added a regression guard. Controlled editorial readiness remains 95/100. No test pass or publication approval is claimed.

## Repeat-audit milestone — 30% — 1 November 2026

- Reviewed the 2025 regional vascular-plant records paper (DOI 10.5281/zenodo.15253859) and added it to the flora chapter bibliography with a clear distinction between seven floristic provinces and seven administrative oblasts.
- Added a voucher-backed *Allium filifolium* record from Besh-Tash Gorge (23 July 2016; 2,170 m; MW0896287) to the Talas dossier, retaining the paper's taxonomic caveat about the *A. kokanicum* complex.
- Expanded the regional species-evidence audit and added regression guards for source scope, unresolved identifications and voucher provenance.
- Read-back confirmed saved changes. The 52 image insertion anchors remain mapped and Deferred; no new visual asset was integrated.
- Regression assertions are committed but `checks.mjs`, browser tests and CI have not been rerun. No test pass is claimed.
- Repeat-audit coverage is 30%; controlled editorial readiness remains 95/100. G4 and G5 remain open.

## Repeat-audit milestone — 40% — 1 November 2026

- Added the unresolved comparison between the 2020–2024 PASK model estimate for adult snow leopards (about 300; 95% CI 246–366) and the Ministry's October 2026 estimate (450–550, method not stated in the notice).
- Added site-level Terskey Ala-Too expedition evidence from the 2025 Burkhan / Archaly survey, with limitations on sampling effort, separate DNA and camera-trap evidence, local argali scope and a corrected Pallas's cat scientific-name spelling.
- Added FFI/CEPF Menzbier's marmot survey estimate (about 16,145, surveys in 2021 and 2022) and distinguished IUCN Red List VU from the IUCN Green Status recovery result.
- Expanded the regional evidence audit and regression assertions. Read-back confirmed saved changes.
- The 52 image insertion anchors remain mapped and Deferred; no new visual asset was integrated.
- Regression assertions are committed but checks.mjs, browser tests and CI have not been run. No test pass is claimed.
- Repeat-audit coverage is 40%; controlled editorial readiness remains 95/100. G4 and G5 remain open.



## Repeat-audit milestone — 50% — 1 November 2026

- Corrected the Kyrgyzstan amphibian country-page snapshot date to 12 October 2026 and distinguished it from the five-country GBIF checklist version 1.18 published 26 October 2026.
- Retained the country-level 7-species / 2-subspecies list and resident / unconfirmed statuses as a compiled checklist, not as field confirmation for each oblast.
- Clarified that the 2021 green-toad paper's 209 adult males from 14 localities are a combined Kazakhstan–Kyrgyzstan sample; six localities and 117 specimens are from Kyrgyzstan.
- Updated the regional evidence audit and regression guards; GitHub read-back verified the saved text.
- The 52 image anchors remain mapped and Deferred. No image was generated or integrated.
- `checks.mjs`, browser tests, mobile checks and CI were not run. No test pass is claimed.
- Repeat-audit coverage is 50%; controlled editorial readiness remains 95/100. G4 and G5 remain open.


## Repeat-audit milestone — 60% — 1 November 2026

- Rechecked the Kyrgyzstan reptile country page: its country selector displays 44 while the numbered species table and summary give 43; 19 subspecies are listed separately, 12 unconfirmed. The count discrepancy remains unresolved.
- Clarified the scope and method of the GBIF Central Asian reptile checklist v1.15: five-country, literature-based synthesis, not a field survey.
- Verified the 2015 Black Stork breeding record at Boom Gorge. The chapter retains the dated brood observations but now deliberately generalizes the nest location to avoid disclosing a sensitive site.
- Updated the regional species audit and source-level regression guards; GitHub changes are saved. `checks.mjs`, browser tests, mobile checks and CI were not run. No test pass is claimed.
- The 52 image insertion anchors remain mapped and Deferred; no image asset was added.
- Repeat-audit coverage is 60%; controlled editorial readiness remains 95/100. G4 and G5 remain open.


## Repeat-audit milestone — 70% — 1 November 2026

- Updated the fauna chapter from mammal checklist v1.11 to GBIF v1.12 (published 26 October 2026) and clarified its literature-synthesis / non-field-sampling method.
- Compared four bird-list references and documented why their reported totals (407, 327, 380 and 133 regular open-data species) have different scopes and must not be combined into a definitive national total.
- Added bilingual explanatory text, direct links and regression guards; expanded the seven-oblast species-evidence audit.
- GitHub read-back verified all changed source and checkpoint files. `checks.mjs`, browser tests, mobile checks and CI were not run; no test pass is claimed.
- The 52 image insertion anchors remain mapped and Deferred; no image asset was added.
- Repeat-audit coverage is 70%; controlled editorial readiness remains 95/100. G4 and G5 remain open.


## Repeat-audit milestone — 80% — 1 November 2026

- Added the Ministry's dated Zhetim-Bel ridge / Karakol State Nature Park camera-trap records (2 July 2026) and explicitly distinguished presence detections from abundance estimates.
- Added UNDP's 7 December 2025 account of the Important Bird Area near Bishkek, preserving the difference between its reported year-round species richness and the approximately 40 species observed during a short field visit.
- Kept the white-tailed eagle nesting superlative attributed to UNDP; exact sensitive nest locations remain undisclosed.
- Updated the fauna chapter bibliography, regional evidence audit and regression guards; GitHub read-back verified all changed files.
- `checks.mjs`, browser tests, mobile checks, accessibility tests and CI were not run; no test pass is claimed.
- The 52 image insertion anchors remain mapped and Deferred; no image asset was added.
- Repeat-audit coverage is 80%; controlled editorial readiness remains 95/100. G4 and G5 remain open.


## Repeat-audit milestone — 90% — 1 November 2026

- Reviewed the Institute of Biology of the National Academy of Sciences of the Kyrgyz Republic's report on an August 2026 expedition that recorded approximately 2,000 Demoiselle Cranes (*Grus virgo*) along the Issyk-Kul shore.
- Added the record in Russian and English to the fauna chapter and documented its evidence class and limits in the regional species audit. The figure remains an attributed approximate migration-aggregation count, not a national population estimate or trend; the public notice does not provide a counting protocol or uncertainty estimate.
- Explicitly kept the Institute's Issyk-Kul shoreline record separate from CAMP Alatoo's event-specific count at the proposed Kushtar micro-reserve; the two observations are not added together.
- Added source-level regression guards for the date, taxon, source URL, approximate count and interpretation limits.
- GitHub read-back verified the saved files in this save cycle. The 52 image anchors and 52 Deferred dispositions remain unchanged; no image asset is claimed as generated or integrated.
- The regression script, browser, mobile, accessibility and CI checks have not been run; no test pass is claimed. G4 independent scientific review and G5 independent bilingual/editorial review remain open.
- Repeat-audit coverage: **90%**. Controlled editorial readiness remains **95/100**; this is not publication approval.


## 100% author-side repeat-audit milestone — 1 November 2026

- Added the Ministry of Natural Resources' 3 June 2026 notice on the Common Crane (Grus grus) breeding record at Jety-Oguz, Issyk-Kul: nest found 19 April; pair with two chicks observed 24 May. The chapter describes this as the first ministry-reported Issyk-Kul record and the second known national nesting record only according to the Ministry's historical summary (one prior Chui Valley record in 1958). It does not infer range expansion, fledging success or a population trend.
- Added a bilingual chapter entry, an evidence-classification note in the Kyrgyzstan species audit, an explicit P2 question in the independent scientific-review packet, and source/date/scope regression guards.
- Evaluated a May 2026 media report of a possible Black-necked Crane (*Grus nigricollis*) observation near Soek Pass. Because the report relays a social-media statement without a verifiable primary field record or diagnostic documentation, the candidate was explicitly excluded from the confirmed chapter checklist and added to the audit and independent-review packet as unresolved.

- Author-side source-led repeat-audit work is marked 100% complete. This does not close G4 independent scientific review or G5 independent bilingual/editorial release review; both remain open and require qualified external sign-off. It is not publication approval.
- All 52 image anchors remain mapped and all 52 image dispositions remain Deferred; visual production is not complete.
- The regression script and browser/mobile/accessibility/CI checks have not been run in this save cycle. No test pass is claimed.
- Controlled editorial-readiness score remains 95/100; it is not increased by completing the author-side repeat audit.

## Optional external scientific / editorial consultation materials (not a completion gate)

Start with `INDEPENDENT_REVIEW_BUNDLE.md` for the frozen-snapshot instructions and complete reviewer deliverables. The Biology atlas has a dedicated external-review handoff. These documents are working materials for independent reviewers; none is itself an independent approval:

- `INDEPENDENT_REVIEW_HANDOFF.md` — reviewer qualifications, evidence protocol, acceptance criteria and G4/G5 sign-off forms.
- `INDEPENDENT_REVIEW_PAGE_MATRIX.md` — assignment scope and recommended specialist competence for all 13 bilingual pages, plus cross-page checks.
- `INDEPENDENT_REVIEW_TRACKING_REGISTER.md` — 10 priority scientific claims (six P1, four P2), page-level G4/G5 coverage, cross-page review and issue tracking.
- `EXTERNAL_REVIEW_PACKET.md` — detailed scientific questions, source conflicts and editorial review brief.
- `EDITORIAL-AND-SCIENTIFIC-STANDARDS.md` — project-wide evidence, taxonomy, quantitative, bilingual and attribution rules.
- `G4_SCIENTIFIC_AUDIT_2026-11-01.md`, `G5_EDITORIAL_AUDIT_2026-11-01.md` and `BILINGUAL_PARITY_AUDIT.md` — author-side audit records only; they do not replace independent review.

**Current status:** G4 internal scientific audit and G5 internal editorial/bilingual audit are complete (4/4 planned blocks each). The external-review materials below are retained for optional future consultation only; independent reviewer sign-off is not required. The 52 planned illustration assets remain deferred. Further screen-reader, keyboard and physical-device checks, plus shared-portal feedback integration and secure-intake testing, remain separate project tasks.

- `INDEPENDENT_REVIEW_RECRUITMENT_PLAN.md` — specialist roles, independence checks, invitation sequence, deliverables and draft invitations.


## Reader feedback and public review
- The reusable feedback policy and moderation model are defined in `FEEDBACK_SYSTEM_STANDARD.md`.
- `FEEDBACK_PORTING_GUIDE.md` contains copy-ready instructions for other subject teams. Biology is the pilot; this work does not modify other subjects or the shared portal.
- The live intake channel is not enabled: a secure HTTPS endpoint and private moderation queue still need to be selected, configured and tested. No submission is claimed to be operational.

- `FEEDBACK_WIDGET_TEMPLATE.html` provides a reusable bilingual form component; submission remains disabled until a secure endpoint and private moderation queue are configured.


## Agreed completion model — current status (2 November 2026)

- G4 internal scientific audit: **complete, 4/4 blocks (100%)**. Unresolved source and taxonomy issues remain qualified/deferred; they are not silently converted into confirmed facts.
- G5 internal editorial and bilingual audit: **complete, 4/4 blocks (100%)**. The separate parity audit records 1,147 RU / 1,147 EN blocks with matching numeric-token and scientific-name sets in its measured scope.
- Independent external scientific or professional bilingual review: optional consultation only, not a required gate.
- The feedback standard and reusable bilingual widget are prepared in Biology. Shared-portal integration is a separate cross-project task; feedback intake remains disabled until the portal integration, privacy/security and end-to-end technical checks are complete and the owner is ready to invite teachers.
- Teacher feedback after portal completion is a pedagogical pilot, not formal independent peer review.
- All 52 visual assets remain deferred. Automated browser/contrast/name checks have passed within their stated scope; full keyboard traversal, screen-reader and physical-device checks are not claimed complete.
- Controlled editorial readiness remains **95/100** pending the remaining project tasks above; this is not publication approval.


## Supersession note — 2 November 2026

Earlier historical entries in this README may describe G4/G5 as independent external-review gates. Those entries record the former draft plan and are superseded by the current closure plan above and the agreed project model: G4 and G5 are internal scientific and editorial/bilingual audits, both complete. External expert/editor review is optional. Unresolved evidence limitations remain qualified/deferred. Teacher feedback will be gathered as a later pedagogical pilot after the shared portal is complete and secure feedback intake has been tested.


## Visual-production status supersession — 3 November 2026

Earlier statements in this README that all 52 illustration assets remain deferred are historical and are superseded by the current records in `IMAGE_GENERATION_PLAN.md`, `IMAGE_INSERTION_MAP.md` and `IMAGE_DISPOSITION_REGISTER.md`.

- Two of 52 visual briefs are produced (**3.8%**): Chüy fauna (six verified/licensed local WebP photographs) and Jalal-Abad flora (one verified/licensed local WebP photograph).
- The Jalal-Abad flora figure is integrated at the original anchor in `chapters/flora-kyrgyzstan.html`; the source and checksum audit is `FLORA_JALALABAD_IMAGE_AUDIT_2026-11-03.md`.
- Focused chapter browser QA passed (run 41599165657). Latest full Biology CI passed on branch head `057cc6ef354f6a89d0feafe46d2288ac8dabfc64` (run 41599553658).
- The other 50 visual briefs remain pending/deferred. Offline image caching is not implemented or verified.
- Controlled editorial readiness remains 95/100; visual production is reported separately and does not change that score.


## Visual-production status supersession — 3 November 2026 (later update)

This entry supersedes the earlier 2/52 visual-production status above. Three of 52 mapped visual briefs are now produced (**5.8%**): Chüy fauna (six photographs), Jalal-Abad flora (one) and Issyk-Kul flora (four). The other 49 briefs remain pending/deferred.

The Issyk-Kul flora figure is integrated at the original anchor in `chapters/flora-kyrgyzstan.html`. Four original photographs were downloaded, checked against live Commons SHA-1 metadata and converted to local WebP files. Focused bilingual chapter QA passed in run 41608849568. Full Biology CI must be rerun on the asset-bearing branch head after the bot-generated image commit.

Controlled editorial readiness remains 95/100; visual production does not raise that score. Offline caching is not implemented or verified.


## Full Biology CI confirmation — 3 November 2026

The complete Biology CI passed on commit `cedc296d07ca85842c0b501388f8d4df497471fd` after the Issyk-Kul WebP assets and register corrections were committed: [run 41609646836](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41609646836). Static checks covered 13 HTML pages and 99 local paths; Chromium covered all 13 pages at mobile and desktop widths, 30 language toggles, with no uncaught page errors. Contrast sampling covered 21,529 text instances with zero below threshold, and keyboard focus indicators were checked.

Current visual-brief production is 3/52 (5.8%); eleven photographs are included in those three briefs. Editorial readiness remains 95/100. Offline caching is not implemented or verified.


## Visual-production status supersession — 3 November 2026 (Naryn update)

This entry supersedes the earlier 3/52 production count above. **Four of 52 mapped visual briefs are produced (7.7%)**: Chüy fauna (six photographs), Jalal-Abad flora (one), Issyk-Kul flora (four) and Naryn flora (three). The other 48 briefs remain pending or deferred.

The Naryn flora figure is integrated at its original anchor in `chapters/flora-kyrgyzstan.html`. Three source originals were downloaded and verified against live Wikimedia Commons SHA-1 metadata, converted to local WebP, and committed with a machine-readable manifest. Focused bilingual Chromium QA passed in [run 41611003785](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41611003785). Full provenance and individual checksums are recorded in `FLORA_NARYN_IMAGE_AUDIT_2026-11-03.md`.

The complete Biology CI still needs to be rerun on the asset-bearing branch head after this checkpoint commit. The earlier CI failure was caused by the Naryn assets not yet being committed at the time that run checked out the branch; the separate Naryn asset workflow subsequently passed and committed them.

Controlled editorial readiness remains 95/100. Offline caching is not implemented or verified.


## Visual-production status supersession — 3 November 2026 (Osh update)

This entry supersedes the earlier 4/52 count. **Five of 52 mapped visual briefs are produced (9.6%)**: Chüy fauna (six photographs), Jalal-Abad flora (one), Issyk-Kul flora (four), Naryn flora (three) and Osh flora (one). The other 47 briefs remain pending or deferred.

The Osh flora figure is integrated at the original anchor in `chapters/flora-kyrgyzstan.html`. It documents a river corridor and riparian woody vegetation in Kulun-Ata State Nature Reserve; it does not identify individual tree species or claim to represent the full flora of Osh Region. The original JPEG matched the Commons SHA-1, the WebP derivative and manifest were committed, and focused Chromium QA passed in [run 41611930095](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41611930095). Full provenance: `FLORA_OSH_IMAGE_AUDIT_2026-11-03.md`.

Full Biology CI passed after the Naryn assets and audit updates in [run 41611232412](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41611232412): 13 HTML pages, 102 local paths, 13 inline scripts, 165 typed buttons and 41 accessible dynamic output regions; browser smoke passed for all 13 pages at mobile and desktop widths, 30 language toggles and no uncaught page errors. Contrast sampling covered 21,533 text instances with zero below threshold, and keyboard Tab-sequence focus indicators were checked. A new full CI run is required after the Osh image and register commits.

Controlled editorial readiness remains 95/100. Offline caching is not implemented or verified.


## Full Biology CI confirmation — 4 November 2026

The complete Biology workflow passed on commit `afbe0bd2c9afecdac162fa78f0cbf5102bbf893d`: [run 41774678633](https://github.com/Ajokendo/Atlas-of-Knowledge/actions/runs/41774678633). Static validation covered 13 HTML pages, 121 local paths, 13 inline scripts, 165 typed buttons and 41 accessible dynamic output regions. Chromium smoke tests passed on all 13 pages at mobile and desktop widths; 30 language-toggle interactions passed; no uncaught page errors were reported. Preliminary contrast sampling covered 20,701 text instances with zero below-threshold instances, and keyboard Tab-sequence focus indicators were checked.

The current `IMAGE_DISPOSITION_REGISTER.md` contains 52 mapped briefs: 26 are marked produced or integrated (**50.0%**), and 26 remain deferred. This is the authoritative brief-level count; individual briefs may contain multiple photographs or SVGs. The register currently accounts for 15 local WebP photographs and 21 original SVG schematics across those 26 briefs. The 52-row register is the source of truth where older narrative checkpoints or the abbreviated checkbox list in `IMAGE_GENERATION_PLAN.md` differ.

The Biochemistry responsive-image fix is included in the tested commit. Full physical-device, screen-reader and offline-cache testing remains pending; successful CI does not claim those manual checks are complete. Controlled editorial readiness remains 95/100 and is reported separately from visual production.


## Visual-production checkpoint — 4 November 2026 (membrane transport)

The current visual register now records **24 of 52 mapped briefs produced (46.2%)**: 15 local WebP photographs and 19 original SVG schematics. The new membrane-transport plate is an original bilingual SVG integrated at the existing anchor in `chapters/cell-biology.html`. It distinguishes simple diffusion, channel-mediated facilitated diffusion, osmosis toward the side with higher solute concentration, and ATP-powered active transport against a gradient. The asset is authored for this atlas; no third-party image is used. Focused browser image-decode QA and the full Biology CI run are pending for this commit series.

This count supersedes earlier visual-production checkpoints in this README; `IMAGE_DISPOSITION_REGISTER.md` remains the source of truth. Controlled editorial readiness is tracked separately. Physical-device, screen-reader and offline-cache checks remain pending.


## Visual-production checkpoint — 4 November 2026 (mitosis)

The current visual register now records **25 of 52 mapped briefs produced (48.1%)**: 15 local WebP photographs and 20 original SVG schematics. A new original bilingual mitosis plate is integrated at the existing anchor in `chapters/cell-biology.html`. It shows prophase, prometaphase, metaphase, anaphase and telophase in sequence, and distinguishes nuclear division (mitosis) from cytoplasmic division (cytokinesis). No third-party image is used. Focused browser image-decode QA and the full Biology CI run are pending for this commit series.

This count supersedes earlier visual-production checkpoints in this README; `IMAGE_DISPOSITION_REGISTER.md` remains the source of truth. Physical-device, screen-reader and offline-cache checks remain pending.


## Corrected visual-production count — 4 November 2026

A row-by-row recount of the 52 entries in `IMAGE_DISPOSITION_REGISTER.md` found **28 briefs marked Produced or Integrated (53.8%)**, not 25. The earlier 25/52 checkpoint undercounted the six fauna briefs already marked Integrated and some other integrated assets. This count is by visual brief, not by individual file. Three botanical plates are counted as produced/integrated but still carry focused browser-QA pending notes; those checks remain open and are not represented as passed. The register is the source of truth.


## Visual production checkpoint — 4 November 2026

The animal-cell ultrastructure brief has now been produced as an original bilingual SVG and integrated at its existing anchor in `chapters/cell-biology.html`. The authoritative disposition register now records **29 of 52 briefs produced or integrated (55.8%)**. This is a brief-level count, not a file count. Browser QA for the new animal-cell figure is pending until the Biology workflow completes.


## Cell-cycle visual checkpoint — 4 November 2026

Added an original bilingual cell-cycle SVG at `images/generated/cell-cycle.svg` and integrated it immediately before the cell-cycle control and apoptosis section in `chapters/cell-biology.html`. The diagram distinguishes interphase (G₁, S, G₂), M phase (mitosis plus cytokinesis), the G₁/S and G₂/M checkpoints, the spindle checkpoint, and exit into G₀. The production register and insertion map now track **30 of 53 visual briefs (56.6%)**; the additional brief expands the programme denominator from 52 to 53. Focused browser image-decode QA and scientific review remain pending; this is not reported as a full visual QA pass.


## Ecology cycles visual checkpoint — 4 November 2026

Created and integrated `images/generated/ecology-cycles.svg` at the original `image-brief-ecology-cycles` anchor in `chapters/ecology.html`. The bilingual infographic presents simplified carbon and nitrogen cycles and distinguishes carbon transfer from microbial nitrogen transformations. Updated the insertion map, disposition register and production plan. The visual programme now records **31 of 53 briefs produced or integrated (58.5%)**, including 15 local WebP photographs and 20 original SVG schematics. Focused browser image-decode QA and scientific review of the new plate remain pending.


## Ecology mountain catchment visual checkpoint — 4 November 2026

Created and integrated the original bilingual-accessible SVG `images/generated/ecology-mountain.svg` at the existing `image-brief-ecology-mountain` anchor in `chapters/ecology.html`. The generalized landscape links glacier melt and surface runoff with stream channels, soil infiltration, subsurface flow, vegetation roots and river-valley habitats. It contains no named species, fixed elevation labels or claim that vegetation belts occur at identical elevations on every slope. The visual register now records **32 of 53 briefs produced or integrated (60.4%)**: 15 locally packaged WebP photographs and 21 original SVG schematics. Focused browser image-decode QA is pending.


## Ecology food-web visual checkpoint — 4 November 2026

Created and integrated the original `images/generated/ecology-web.svg` at the existing `image-brief-ecology-web` anchor in `chapters/ecology.html`. The diagram uses generalized organism groups and resource-to-consumer arrows; decomposers return mineral nutrients, while energy is not depicted as cycling. The visual register now records **33 of 53 briefs produced or integrated (62.3%)**: 15 locally packaged WebP photographs and 22 original SVG schematics. Focused browser image-decode QA is pending.


## Visual programme update — 4 November 2026
- Added and integrated `images/generated/flora-talas-vegetation.svg` at the preserved `image-brief-flora-talas` anchor in `chapters/flora-kyrgyzstan.html`. The bilingual conceptual panorama shows the Besh-Tash habitat mosaic: spruce woodland, juniper communities, subalpine and alpine meadows, and river floodplain. It is explicitly not to scale and does not invent elevation limits or species records.
- The visual programme now records **34 of 53 briefs produced or integrated (64.2%)**; 19 remain deferred or pending. The new SVG is original atlas artwork; focused browser visual QA is pending.

## Visual programme update — 4 November 2026
- Added `images/generated/fauna-habitats.svg` and integrated it at the preserved `image-brief-fauna-habitats` anchor in `chapters/fauna-kyrgyzstan.html`. The bilingual composite panorama distinguishes valley floodplain, forested slopes, mountain meadows and cliffs; generic animal silhouettes are not assigned species names. Caption states that the image is not a range map, census or single real site.
- The visual programme now records **35 of 53 briefs produced or integrated (66.0%)**; 18 remain deferred or pending. Browser visual QA for this new illustration is pending.


## Zoology adaptation visual checkpoint — 4 November 2026

Created and integrated the original bilingual SVG `images/generated/zoology-adaptation.svg` at the preserved `image-brief-zoology-adaptation` anchor in `chapters/zoology.html`. The comparison covers aquatic, terrestrial and aerial habitats and links body form to function without presenting traits as universal. It explicitly describes adaptation as inherited population-level variation shaped over generations. The visual programme now records **36 of 53 briefs produced or integrated (67.9%)**; 17 remain deferred or pending. Focused browser visual QA for this new plate is pending.


## Visual production update — 4 November 2026
- Added and integrated `images/generated/zoology-anatomy.svg`, an original bilingual comparison of typical body coverings and respiratory structures across the five familiar vertebrate teaching groups.
- The figure explicitly qualifies group-level patterns: gills occur in most fish but are not universal; amphibian respiration changes through development; and within-group exceptions exist. It is a simplified teaching comparison, not a species-level diagnostic chart.
- The visual programme now stands at **39 of 53 briefs (73.6%)**; 14 briefs remain. This is a brief-level production count and does not imply that focused browser QA or manual device/accessibility testing is complete.


## Visual production update — 4 November 2026
- Added and integrated `images/generated/microbe-virus-cycle.svg` in `chapters/microbiology.html`.
- The bilingual plate presents a five-stage generalised viral replication sequence and explicitly avoids implying that entry, genome replication or release follows one universal mechanism across virus families.
- The visual programme now stands at **39 of 53 briefs (73.6%)**; 14 remain. Focused browser visual QA for the newly produced microbiology figures is still pending.


## Visual production update — 4 November 2026
- Added and integrated `images/generated/microbe-resistance.svg` in `chapters/microbiology.html`.
- The bilingual figure demonstrates natural selection at population level: susceptible cells are suppressed under antimicrobial pressure, while heritably resistant variants survive and reproduce. It notes mutation or acquisition of resistance genes and rejects purposeful adaptation.
- The visual programme now stands at **42 of 53 briefs (79.2%)**; 11 briefs remain. Focused browser visual QA for these new microbiology figures is pending.


## Systematics taxonomy hierarchy visual checkpoint — 4 November 2026
Created and integrated the original bilingual SVG `images/generated/systematics-ranks.svg` at the preserved `image-brief-systematics-ranks` anchor in `chapters/systematics.html`. The eight-rank grey-wolf example is consistent with the chapter's interactive hierarchy: Eukarya → Animalia → Chordata → Mammalia → Carnivora → Canidae → *Canis* → *Canis lupus*. The binomial is italicised, and the caption identifies the scheme as a conventional teaching classification that may be revised. The visual programme now records **43 of 53 briefs produced or integrated (81.1%)**; 10 remain deferred. Focused browser visual QA for this figure is pending; no browser rendering or full CI pass is claimed in this checkpoint.
