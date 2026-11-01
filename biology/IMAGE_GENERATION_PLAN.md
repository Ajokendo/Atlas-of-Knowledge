# Atlas of Biology — image generation plan

Status key: `[ ] not yet triaged` · `[~] explicitly deferred` · `[x] generated, reviewed and integrated`.

This register mirrors the in-page illustration markers. Each marker is placed beside the relevant learning section and contains the full Russian and English brief. Existing SVG plates and interactive models are not counted as missing images. Generate only from verified source material; add species names, labels, measurements and maps only after editorial checking.

## Current disposition — 1 November 2026

All 52 planned assets are explicitly **deferred**, not generated. See [`IMAGE_DISPOSITION_REGISTER.md`](IMAGE_DISPOSITION_REGISTER.md) for the per-asset reason, source/licence status, review path and preserved insertion anchor. The 13 P1 briefs are reviewed in [`IMAGE_SCIENTIFIC_REVIEW.md`](IMAGE_SCIENTIFIC_REVIEW.md); the remaining 39 P2/P3 briefs are reviewed in [`IMAGE_BRIEF_REVIEW.md`](IMAGE_BRIEF_REVIEW.md). No unlicensed third-party imagery has been inserted. Visual production resumes only when an exact asset can be created or sourced, reviewed and integrated.

## Priority key

- **P1 — highest value:** distinctive real organisms, regional habitats and biodiversity scenes not already represented by existing SVGs. Produce these first because they add otherwise missing visual evidence and a strong sense of place.
- **P2 — useful complement:** visuals that deepen explanation or connect concepts, but are not essential before the main scientific content is usable.
- **P3 — lower priority:** concepts already substantially represented by an SVG plate or interactive model. Generate only if a different visual mode adds a clear benefit; do not recreate the existing diagram as a near-duplicate.

Priorities are editorial sequencing, not scientific approval. The latest marker audit counted 22 inline SVG elements across the 13 pages carrying planned briefs (updated 1 November 2026). No raster `<img>` elements or generated image directory are present yet. It did not treat every SVG as a complete substitute: the comparison is topic-specific. Priority labels are mirrored in the in-page markers. Exact insertion anchors, target asset filenames, formats and aspect ratios for all 52 briefs are documented in `IMAGE_INSERTION_MAP.md`. Current allocation: **13 P1, 26 P2 and 13 P3**.


## Landing page

- [~] **[P2] От молекулы до биосферы / From molecule to biosphere** — encyclopedic cover panorama connecting DNA, a cell, a plant, an animal and a mountain ecosystem; no labels or pseudo-scientific symbols. Placement: `index.html`.

## Core biology chapters

### Anatomy and physiology — `chapters/anatomy.html`
- [~] **[P2] Системы органов человека / Human organ systems** — anatomically coherent frontal body showing major organ systems in situ and realistic proportions.
- [~] **[P2] Сердце и два круга кровообращения / Heart and the two circulatory circuits** — heart cutaway with chambers, valves and correctly directed pulmonary and systemic blood flow.
- [~] **[P3] Отрицательная обратная связь в организме / Negative feedback in the human body** — thermoregulation sequence: receptor, control centre, effector and return toward the normal range.

### Biochemistry — `chapters/biochemistry.html`
- [~] **[P3] Четыре класса биомолекул / Four classes of biomolecules** — comparative plate of carbohydrates, lipids, proteins and nucleic acids; distinguish monomers and polymers.
- [~] **[P2] Работа фермента и активный центр / Enzyme action and the active site** — substrate binding, enzyme–substrate complex and product release, with accurate molecular specificity.
- [~] **[P2] Этапы клеточного дыхания / Stages of cellular respiration** — locate glycolysis in cytosol, citric acid cycle in mitochondrial matrix and respiratory chain on inner membrane.

### Botany — `chapters/botany.html`
- [~] **[P2] Внутреннее строение корня, стебля и листа / Internal structure of root, stem and leaf** — botanical cross-sections with epidermis, ground and vascular tissues; correctly position xylem and phloem.
- [~] **[P2] Путь воды и органических веществ в растении / Transport of water and organic compounds in plants** — distinguish xylem water/mineral flow from phloem assimilate transport.
- [~] **[P3] Цветок и опыление / Flower structure and pollination** — representative angiosperm flower cutaway showing stamens, anthers, stigma, style, ovary and ovules; do not attribute it to a named species.

### Cell biology — `chapters/cell-biology.html`
- [~] **[P3] Животная клетка: ультраструктура / Animal cell ultrastructure** — detailed animal cell with membrane, nucleus, mitochondria, ER, Golgi, ribosomes and vesicles; not to scale.
- [~] **[P2] Мембранный транспорт / Membrane transport** — phospholipid bilayer, channels, carriers, diffusion, osmosis and active transport with correct gradients and ATP use.
- [~] **[P2] Митоз: последовательность стадий / Mitosis: sequence of stages** — chromosomes, spindle and nuclear envelope across mitotic stages; distinguish mitosis from interphase and cytokinesis.

### Ecology — `chapters/ecology.html`
- [~] **[P3] Пищевая сеть горной экосистемы / Food web of a mountain ecosystem** — Central Asian mountain-meadow food web; arrows point from resource to consumer.
- [~] **[P2] Экосистема горного водосбора / Mountain catchment ecosystem** — landscape from glaciers and alpine meadows through forest belt to river and valley, showing ecological connections.
- [~] **[P2] Круговороты вещества в экосистеме / Matter cycles in an ecosystem** — carbon and nitrogen cycles across atmosphere, soil, organisms and microbes; labels require editorial review.

### Evolutionary biology — `chapters/evolution.html`
- [~] **[P3] Филогенетическое дерево и общий предок / Phylogenetic tree and common ancestry** — branching tree with common-ancestry nodes and sister groups; avoid a ladder of progress.
- [~] **[P2] Сравнение гомологичных и аналогичных органов / Homologous and analogous structures** — compare shared ancestry with similar function in structures of different origins.
- [~] **[P2] История жизни на геологической шкале / History of life on the geological timescale** — proportionate geological timeline of major events; do not depict evolution as a linear sequence.

### Genetics — `chapters/genetics.html`
- [~] **[P3] Упаковка ДНК в хромосому / DNA packaging into a chromosome** — double helix, nucleosomes, chromatin and metaphase chromosome.
- [~] **[P2] Трансляция на рибосоме / Translation at the ribosome** — mRNA, ribosome, tRNA, codons and growing polypeptide, with correct reading direction.
- [~] **[P2] Типы генетических мутаций / Types of genetic mutations** — substitution, insertion and deletion with possible reading-frame consequences; avoid implying a universal effect.

### Microbiology — `chapters/microbiology.html`
- [~] **[P3] Бактериальная клетка и вирусная частица / Bacterial cell and virus particle** — contrast prokaryotic cell organisation with a virion; never depict a virus as a cell.
- [~] **[P2] Цикл репликации вируса / Viral replication cycle** — attachment, entry, synthesis, assembly and release without combining unrelated virus-family mechanisms.
- [~] **[P2] Возникновение и распространение устойчивости / Emergence and spread of antimicrobial resistance** — selection of resistant variants in a population, not purposeful microbial adaptation.

### Systematics — `chapters/systematics.html`
- [~] **[P3] Три домена клеточной жизни / The three domains of cellular life** — compare Bacteria, Archaea and Eukarya; do not place viruses among cellular domains.
- [~] **[P2] Таксономические ранги на примере организма / Taxonomic ranks using one organism as an example** — domain-to-species hierarchy; verify every rank and binomial before publication.
- [~] **[P3] Как читать филогенетическое дерево / How to read a phylogenetic tree** — nodes, branches, sister groups and common ancestry; branch rotation does not change relationships.

### Zoology — `chapters/zoology.html`
- [~] **[P3] Пять основных групп позвоночных / Five major vertebrate groups** — compare fish, amphibians, reptiles, birds and mammals, noting diversity within groups.
- [~] **[P2] Сравнение покровов и способов дыхания / Comparison of body coverings and respiration** — scales/skin, feathers, hair and respiratory organs; avoid universalising group traits.
- [~] **[P2] Адаптации животных к среде обитания / Animal adaptations to habitats** — aquatic, terrestrial and aerial adaptations of limbs, coverings and sensory systems.

## Kyrgyzstan regional biodiversity

### Flora of Kyrgyzstan — `chapters/flora-kyrgyzstan.html`
- [~] **[P3] Высотная мозаика растительности Кыргызстана / Altitudinal vegetation mosaic of Kyrgyzstan** — foothill semi-deserts, steppe, juniper and spruce woodland, subalpine and alpine meadows; belts vary by slope.
- [~] **[P1] Ландшафты флоры Джалал-Абадской области / Flora landscapes of Jalal-Abad Region** — Arslanbob walnut-fruit forest, wooded slopes and moist ravines; show communities, not an exhaustive species list.
- [~] **[P1] Растительность Иссык-Кульской котловины / Vegetation of the Issyk-Kul basin** — lake deltas and wetlands, dry western foothills and Terskey Ala-Too spruce forests; keep habitats distinct.
- [~] **[P1] Высокогорные луга и степи Нарынской области / High-altitude meadows and steppes of Naryn Region** — Son-Kul, Chatyr-Kul and inner valleys with wetland, meadow and steppe communities.
- [~] **[P1] Лесные и горные сообщества Ошской области / Forest and mountain communities of Osh Region** — walnut-fruit forests, juniper slopes and Pamir-Alay highlands; no regionally alien plants.
- [~] **[P1] Айгуль и дикие тюльпаны Баткена / Aygul and wild tulips of Batken** — separate, botanically accurate portraits of *Petilium eduardii* and other verified wild tulips; do not conflate species.
- [~] **[P2] Растительность Таласского Ала-Тоо / Vegetation of Talas Ala-Too** — Besh-Tash spruce and juniper communities, river floodplain and subalpine meadows.
- [~] **[P2] От долины Чуя к высокогорьям / From the Chuy Valley to high elevations** — valley steppe and semi-desert through Kyrgyz Range juniper slopes to alpine meadows; no invented elevation labels.

### Fauna of Kyrgyzstan — `chapters/fauna-kyrgyzstan.html`
- [~] **[P3] Высотные местообитания и фауна Кыргызстана / Altitudinal habitats and fauna of Kyrgyzstan** — valley and riparian habitats through forests, alpine meadows and cliffs; not a precise range map.
- [~] **[P1] Крупные млекопитающие гор Кыргызстана / Large mammals of the Kyrgyz mountains** — snow leopard, argali and Siberian ibex with accurate morphology and natural behaviour.
- [~] **[P1] Птицы гор, озёр и водно-болотных угодий / Birds of mountains, lakes and wetlands** — cliff raptor, high-altitude ground bird and lake waterbirds in distinct habitats.
- [~] **[P1] Пресноводная фауна Кыргызстана / Freshwater fauna of Kyrgyzstan** — Issyk-Kul and clear mountain river, above- and underwater views, only verified local fish; no unverified species or labels.
- [~] **[P2] Земноводные и пресмыкающиеся Кыргызстана / Amphibians and reptiles of Kyrgyzstan** — amphibian by wet habitat and reptiles on dry rocky slopes; only taxa supported by chapter sources.
- [~] **[P2] Наземные беспозвоночные горных экосистем / Terrestrial invertebrates of mountain ecosystems** — macro plate with recognisable arthropod segmentation, legs and wings; not a complete species inventory.
- [~] **[P1] Фауна Западного Тянь-Шаня / Fauna of the Western Tien Shan** — Besh-Aral, Sary-Chelek and forest ravines with locally documented fauna; no unsupported range boundaries.
- [~] **[P1] Фауна Иссык-Кульской области / Fauna of Issyk-Kul Region** — lake, deltas, wetlands, mountain slopes and Sarychat-Ertash; separate habitat scenes for waterbirds, fish and mammals.
- [~] **[P1] Фауна высокогорий Нарынской области / Fauna of the Naryn highlands** — Son-Kul and Naryn Reserve landscape with maral, mountain predators and waterbirds in separate ecological zones.
- [~] **[P1] Фауна Памиро-Алая и юга Кыргызстана / Fauna of the Pamir-Alay and southern Kyrgyzstan** — forest, juniper and mountain habitats; include only regionally documented taxa.
- [~] **[P1] Фауна сухих склонов Баткенской области / Fauna of Batken's dry slopes** — Surmatash and Sarkent dry foothills with verified marmots, reptiles and mountain birds; no invented endemics.
- [~] **[P2] Животные Таласского Ала-Тоо / Wildlife of Talas Ala-Too** — Besh-Tash spruce-juniper slopes, river valley and alpine cliffs with documented regional mammals and birds.
- [~] **[P2] Фауна Чуйской области / Fauna of Chuy Region** — contrast Chuy Valley, Ala-Archa gorge and Chon-Kemin forests; camera-trap detections are not population estimates.

## Production rules
1. Generate the planned image only after checking the chapter's scientific text and cited sources.
2. Do not ask the image model to invent species, localities, distribution boundaries, statistics or labels.
3. For species portraits, verify taxonomy, diagnostic morphology and Kyrgyzstan occurrence before generation.
4. Review anatomy, proportions, ecological context and any text in the generated image; correct errors before publication.
5. Integrate approved assets with responsive sizing, descriptive RU/EN alt text, captions and source/credit metadata where applicable.
6. Every in-page note names the exact WebP target file and aspect ratio. Replace the matching note at its current location with a semantic `<figure>`; do not place the image elsewhere or duplicate it.
7. Change `[~]` to `[x]` only after the exact asset exists, its creator/source and licence are recorded, scientific review and bilingual alt-text/caption review are complete, and the asset is integrated at the mapped anchor. The presence of a generated image alone does not mean the task is complete.
