# Atlas of Biology — production hand-off for Gemini (52 images)

**Назначение:** единое техническое и научно-редакционное задание для генерации 52 отдельных иллюстраций биологического атласа. Передайте Gemini весь документ. Генерировать нужно именно 52 отдельных файла, а не один коллаж.

**Источник истины:** текущая ветка `workspace/biology`; исходные якоря и имена файлов соответствуют `IMAGE_INSERTION_MAP.md`. Не переименовывать файлы и не менять расположение вставки.

## 1. Общие требования ко всем 52 изображениям

1. **Стиль:** современная научно-образовательная энциклопедическая иллюстрация для школьного атласа; натуралистично, точно, чисто, единый уровень детализации.
2. **Никакого текста внутри изображения:** не встраивать слова, буквы, названия видов, цифры, легенды, текстовые стрелки, водяные знаки или логотипы. Подписи будут добавлены отдельно в HTML на русском и английском.
3. **Формат и размеры:** WebP, sRGB. Для 16:9 — 2400 × 1350 px; для 4:3 — 2000 × 1500 px. Точно соблюдать пропорции. Если Gemini не экспортирует WebP, выдать PNG того же размера, сообщить об этом; интегратор конвертирует. Не выдавать JPEG с артефактами как мастер.
4. **Композиция:** безопасные поля около 5%; не обрезать органы, конечности, крылья, цветки, плавники и ключевые детали. Важные элементы должны оставаться различимыми на экране телефона.
5. **Фон:** спокойный и предметно уместный; ландшафтам — реалистичная природная среда. Избегать чрезмерно тёмного фона, бликов, шума и перегруженности.
6. **Научная точность:** не изобретать виды, анатомические структуры, органеллы, процессы, ареалы, высоты, статистику или природоохранные статусы. Следовать индивидуальным ограничениям. При недостатке данных не добавлять спорные детали и отметить неопределённость в отчёте.
7. **География Кыргызстана:** не подменять местные виды произвольными «центральноазиатскими». Страновая встречаемость не доказывает присутствие в конкретной области, заповеднике, озере или ущелье. Региональные виды включать только при подтверждении в главе/источниках.
8. **Составные сцены:** разные местообитания, стадии или сезоны разделять визуально. Не создавать впечатление, что виды из разных высотных поясов живут рядом в одной точке.
9. **Доступность:** хороший контраст, смысл не должен зависеть только от цвета. Не добавлять текстовые метки в растр.
10. **Происхождение:** в manifest указать факт генерации Gemini, дату и модель/режим, если известны. Не использовать чужие фотографии или узнаваемые защищённые художественные работы как основу.

## 2. Общий шаблон промпта

Для каждого файла используй базовый промпт и соответствующее индивидуальное задание из раздела 3:

> Создай одну отдельную научно достоверную энциклопедическую иллюстрацию для школьного двуязычного атласа биологии. Соблюдай предметные ограничения индивидуального задания. Современная качественная учебная иллюстрация, точная морфология и анатомия, естественные пропорции, ясная композиция, достаточная детализация для просмотра на телефоне. Не добавляй букв, слов, цифр, подписей, легенд, текстовых стрелок, водяных знаков или логотипов. Не выдумывай биологические факты. Выведи один файл с точными пропорциями и размером. Не объединяй задания в коллаж.

**Запрещено для всех файлов:** псевдонаучные символы; неправильная геометрия ДНК/молекул; фантастическая анатомия; лишние/дублированные органы; неверное число конечностей; смешение видов; неестественные позы; бессмысленные стрелки; случайные буквы/псевдотекст; водяные знаки; вымышленные карты и ареалы.

## 3. Реестр 52 изображений

### 01. images/generated/biology-cover.webp

- **Название / краткое содержание:** От молекулы до биосферы / From molecule to biosphere. Энциклопедическая обложка: молекула ДНК, клетка, растение, животное и горный ландшафт как единая визуальная панорама; без подписей и псевдонаучных символов.
- **ID якоря:** `image-brief-biology-cover`
- **Страница:** `index.html`
- **Приоритет:** P2
- **Точное имя файла:** `images/generated/biology-cover.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Use an abstract educational composition; do not imply a literal evolutionary ladder or depict DNA/cell structures with fabricated molecular geometry. No unverified species labels.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 02. ../images/generated/anatomy-systems.webp

- **Название / краткое содержание:** Системы органов человека / Human organ systems. Анатомически согласованный фронтальный вид тела с основными системами органов; органы на естественных местах, реалистичные пропорции, без декоративных или лишних структур.
- **ID якоря:** `image-brief-anatomy-systems`
- **Страница:** `chapters/anatomy.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/anatomy-systems.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Keep organs in anatomically plausible positions and proportions; distinguish organ systems without duplicating or omitting structures. Avoid decorative organs not present in human anatomy.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 03. ../images/generated/anatomy-circulation.webp

- **Название / краткое содержание:** Сердце и два круга кровообращения / Heart and the two circulatory circuits. Научная иллюстрация сердца в разрезе с камерами, клапанами и направлением кровотока по малому и большому кругам; цветовая кодировка условная и последовательная.
- **ID якоря:** `image-brief-anatomy-circulation`
- **Страница:** `chapters/anatomy.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/anatomy-circulation.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show four heart chambers and valves coherently; pulmonary and systemic circuits must be continuous and correctly directed. Red/blue is a conventional oxygenation key, not literal blood colour.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 04. ../images/generated/anatomy-homeostasis.webp

- **Название / краткое содержание:** Отрицательная обратная связь в организме / Negative feedback in the human body. Пошаговая схема терморегуляции: рецептор, центр регуляции, эффектор и возврат показателя к диапазону нормы; не изображать регуляцию как однонаправленную цепь.
- **ID якоря:** `image-brief-anatomy-homeostasis`
- **Страница:** `chapters/anatomy.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/anatomy-homeostasis.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Represent negative feedback as receptor → control centre → effector → response reducing the original deviation. Do not depict homeostasis as a one-way growth chain.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 05. ../images/generated/biochem-molecules.webp

- **Название / краткое содержание:** Четыре класса биомолекул / Four classes of biomolecules. Сравнительная научная таблица-иллюстрация углеводов, липидов, белков и нуклеиновых кислот с корректными структурными мотивами и примерами; не смешивать полимеры и мономеры.
- **ID якоря:** `image-brief-biochem-molecules`
- **Страница:** `chapters/biochemistry.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/biochem-molecules.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Distinguish carbohydrates, lipids, proteins and nucleic acids. Lipids are not conventional repeating-unit polymers; do not depict amino acids, nucleotides or monosaccharides as interchangeable building blocks.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 06. ../images/generated/biochem-enzyme.webp

- **Название / краткое содержание:** Работа фермента и активный центр / Enzyme action and the active site. Крупный молекулярный план взаимодействия субстрата с активным центром, образование комплекса и высвобождение продуктов; показать специфичность без буквального «замка с ключом».
- **ID якоря:** `image-brief-biochem-enzyme`
- **Страница:** `chapters/biochemistry.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/biochem-enzyme.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show substrate binding at an active site and product release without implying the enzyme is consumed. Avoid a rigid lock-and-key metaphor as a universal mechanism.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 07. ../images/generated/biochem-respiration.webp

- **Название / краткое содержание:** Этапы клеточного дыхания / Stages of cellular respiration. Схематичная клетка с локализацией гликолиза в цитозоле, цикла лимонной кислоты в матриксе митохондрии и дыхательной цепи на внутренней мембране.
- **ID якоря:** `image-brief-biochem-respiration`
- **Страница:** `chapters/biochemistry.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/biochem-respiration.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Place glycolysis in cytosol, the citric-acid cycle in mitochondrial matrix and the electron-transport chain on the inner mitochondrial membrane. ATP synthase orientation and proton gradient must be coherent.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 08. ../images/generated/botany-anatomy.webp

- **Название / краткое содержание:** Внутреннее строение корня, стебля и листа / Internal structure of root, stem and leaf. Три ботанических поперечных среза с эпидермой, проводящими тканями и основными тканями; ксилема и флоэма показаны в правильном взаимном положении.
- **ID якоря:** `image-brief-botany-anatomy`
- **Страница:** `chapters/botany.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/botany-anatomy.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Use organ-appropriate cross-sections; xylem/phloem arrangement differs between roots, stems and leaves. Do not copy one vascular-bundle layout into all three.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 09. ../images/generated/botany-transport.webp

- **Название / краткое содержание:** Путь воды и органических веществ в растении / Transport of water and organic compounds in plants. Научная схема целого растения: движение воды и минеральных веществ по ксилеме и перенос продуктов фотосинтеза по флоэме; стрелки не должны смешивать потоки.
- **ID якоря:** `image-brief-botany-transport`
- **Страница:** `chapters/botany.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/botany-transport.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Separate xylem water/mineral transport from phloem assimilate transport. Phloem movement is source-to-sink and should not be presented as a single universal upward stream.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 10. ../images/generated/botany-flower.webp

- **Название / краткое содержание:** Строение цветка и опыление / Flower structure and pollination. Детальный разрез типичного цветка покрытосеменного растения с тычинками, пыльниками, рыльцем, столбиком, завязью и семязачатками; не приписывать его конкретному виду.
- **ID якоря:** `image-brief-botany-flower`
- **Страница:** `chapters/botany.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/botany-flower.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Use a generic angiosperm flower unless a species is explicitly named. Distinguish anther, stigma, style, ovary and ovules; do not imply every flower has identical symmetry or structure.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 11. ../images/generated/cell-animal.webp

- **Название / краткое содержание:** Животная клетка: ультраструктура / Animal cell ultrastructure. Детализированная, но читаемая иллюстрация животной клетки с мембраной, ядром, митохондриями, ЭПС, аппаратом Гольджи, рибосомами и везикулами; органеллы не масштабировать как реальные.
- **ID якоря:** `image-brief-cell-animal`
- **Страница:** `chapters/cell-biology.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/cell-animal.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Do not add a cell wall or chloroplast to an animal cell. Organelles should be recognisable but not shown at mutually misleading scale.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 12. ../images/generated/cell-membrane.webp

- **Название / краткое содержание:** Мембранный транспорт / Membrane transport. Молекулярный разрез фосфолипидного бислоя с каналом, переносчиком, простой диффузией, осмосом и активным транспортом с корректным направлением градиентов и затратой АТФ.
- **ID якоря:** `image-brief-cell-membrane`
- **Страница:** `chapters/cell-biology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/cell-membrane.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Keep phospholipid heads hydrophilic and tails hydrophobic; distinguish passive movement down gradients from active transport requiring energy. Osmosis concerns water movement.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 13. ../images/generated/cell-mitosis.webp

- **Название / краткое содержание:** Митоз: последовательность стадий / Mitosis: sequence of stages. Последовательные стадии митоза с хромосомами, веретеном деления и ядерной оболочкой; отличать митоз от интерфазы и цитокинеза.
- **ID якоря:** `image-brief-cell-mitosis`
- **Страница:** `chapters/cell-biology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/cell-mitosis.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show chromosome condensation, spindle attachment and separation in the correct order. Keep mitosis distinct from interphase and cytokinesis; do not duplicate chromatids after separation.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 14. ../images/generated/ecology-web.webp

- **Название / краткое содержание:** Пищевая сеть горной экосистемы / Food web of a mountain ecosystem. Схематичная пищевая сеть горно-луговой экосистемы Центральной Азии: растения, травоядные, хищники и редуценты; стрелки направлены от ресурса к потребителю.
- **ID якоря:** `image-brief-ecology-web`
- **Страница:** `chapters/ecology.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/ecology-web.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Arrows should show energy transfer from food/resource to consumer. Include decomposers without making them a single terminal endpoint for all matter and energy.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 15. ../images/generated/ecology-cycles.webp

- **Название / краткое содержание:** Круговороты вещества в экосистеме / Matter cycles in an ecosystem. Согласованная научная инфографика углеродного и азотного циклов с атмосферой, почвой, организмами и микробными процессами; процессы подписывать только после редакционной проверки.
- **ID якоря:** `image-brief-ecology-cycles`
- **Страница:** `chapters/ecology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/ecology-cycles.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Distinguish carbon fluxes from nitrogen transformations; label fixation, nitrification, assimilation and denitrification only where the diagram depicts them correctly.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 16. ../images/generated/ecology-mountain.webp

- **Название / краткое содержание:** Экосистема горного водосбора / Mountain catchment ecosystem. Цельный ландшафтный разрез от ледников и альпийских лугов через лесной пояс к реке и долине; показать связи воды, почвы, растений и животных без вымышленных видов.
- **ID якоря:** `image-brief-ecology-mountain`
- **Страница:** `chapters/ecology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/ecology-mountain.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Present a general mountain catchment, not a precise map of a named Kyrgyz site. Do not add species labels or imply that all vegetation belts occur at fixed elevations on every slope.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 17. ../images/generated/evolution-tree.webp

- **Название / краткое содержание:** Филогенетическое дерево и общий предок / Phylogenetic tree and common ancestry. Научная схема ветвящегося дерева с узлами общего происхождения, сестринскими группами и корректным чтением эволюционного родства; не использовать лестничную модель прогресса.
- **ID якоря:** `image-brief-evolution-tree`
- **Страница:** `chapters/evolution.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/evolution-tree.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Use branching common ancestry, not a ladder of progress. Branch rotations must not alter the implied relationships; branch lengths need a stated meaning if scaled.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 18. ../images/generated/evolution-homology.webp

- **Название / краткое содержание:** Сравнение гомологичных и аналогичных органов / Homologous and analogous structures. Сравнительная пластина конечностей позвоночных и функционально сходных структур разного происхождения; подчёркивать различие общего происхождения и сходной функции.
- **ID якоря:** `image-brief-evolution-homology`
- **Страница:** `chapters/evolution.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/evolution-homology.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Homologous structures indicate shared ancestry even when functions differ; analogous structures may share function without the same structural origin. Do not conflate the two.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 19. ../images/generated/evolution-timeline.webp

- **Название / краткое содержание:** История жизни на геологической шкале / History of life on the geological timescale. Хронологическая панорама ключевых этапов истории жизни с пропорциональной геологической шкалой и аккуратными временными границами; не изображать эволюцию как линейный ряд.
- **ID якоря:** `image-brief-evolution-timeline`
- **Страница:** `chapters/evolution.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/evolution-timeline.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Use a proportionate geological timescale and checked dates. Avoid a linear procession from “primitive” to “advanced” organisms or false simultaneity.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 20. ../images/generated/genetics-dna-packaging.webp

- **Название / краткое содержание:** Упаковка ДНК в хромосому / DNA packaging into a chromosome. Последовательные уровни организации: двойная спираль, нуклеосомы, хроматин и метафазная хромосома; не смешивать репликацию с упаковкой.
- **ID якоря:** `image-brief-genetics-dna-packaging`
- **Страница:** `chapters/genetics.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/genetics-dna-packaging.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show double helix → nucleosomes → chromatin → metaphase chromosome as levels of packaging. Keep this separate from the DNA → RNA → protein central-dogma diagram; the target filename now matches the packaging subject.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 21. ../images/generated/genetics-translation.webp

- **Название / краткое содержание:** Трансляция на рибосоме / Translation at the ribosome. Молекулярная сцена трансляции с мРНК, рибосомой, тРНК, кодонами и растущей полипептидной цепью; направление чтения и роли молекул должны быть верны.
- **ID якоря:** `image-brief-genetics-translation`
- **Страница:** `chapters/genetics.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/genetics-translation.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show mRNA read 5′→3′, codon/anticodon pairing, tRNA delivery and peptide-bond formation in the ribosome. Do not reverse the reading direction or confuse transcription with translation.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 22. ../images/generated/genetics-mutations.webp

- **Название / краткое содержание:** Типы генетических мутаций / Types of genetic mutations. Сравнение замены, вставки и делеции в короткой последовательности ДНК и их возможных последствий для рамки считывания; не обещать одинаковый эффект для всех генов.
- **ID якоря:** `image-brief-genetics-mutations`
- **Страница:** `chapters/genetics.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/genetics-mutations.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Distinguish substitution, insertion and deletion; frameshifts generally follow non-triplet insertions/deletions. Do not imply that every mutation is harmful or changes phenotype.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 23. ../images/generated/microbe-compare.webp

- **Название / краткое содержание:** Бактериальная клетка и вирусная частица / Bacterial cell and virus particle. Сравнительная научная иллюстрация прокариотической бактериальной клетки и вирусного вириона с различием клеточной организации; вирус не изображать как клетку.
- **ID якоря:** `image-brief-microbe-compare`
- **Страница:** `chapters/microbiology.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/microbe-compare.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** A bacterium is a cell with prokaryotic organisation; a virion is acellular. Viral envelopes are not universal, and bacterial structures such as peptidoglycan must not be assigned to all microbes.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 24. ../images/generated/microbe-virus-cycle.webp

- **Название / краткое содержание:** Цикл репликации вируса / Viral replication cycle. Обобщённая схема прикрепления, проникновения, синтеза компонентов, сборки и выхода вирионов; не смешивать детали разных вирусных семейств в один универсальный механизм.
- **ID якоря:** `image-brief-microbe-virus-cycle`
- **Страница:** `chapters/microbiology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/microbe-virus-cycle.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Present a clearly labelled generalised cycle; entry, replication and release differ among virus families. Avoid combining incompatible details into a purported universal viral life cycle.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 25. ../images/generated/microbe-resistance.webp

- **Название / краткое содержание:** Возникновение и распространение устойчивости / Emergence and spread of antimicrobial resistance. Схема отбора устойчивых вариантов в микробной популяции при воздействии антимикробного препарата; показать отбор существующей вариации, а не целенаправленное «привыкание».
- **ID якоря:** `image-brief-microbe-resistance`
- **Страница:** `chapters/microbiology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/microbe-resistance.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show selection of resistant variants and possible gene transfer, not an individual bacterium intentionally learning to resist. Do not imply antibiotics treat viral infections.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 26. ../images/generated/systematics-domains.webp

- **Название / краткое содержание:** Три домена клеточной жизни / The three domains of cellular life. Научная сравнительная пластина Bacteria, Archaea и Eukarya с отличиями клеточной организации; вирусы не включать в домены клеточной жизни.
- **ID якоря:** `image-brief-systematics-domains`
- **Страница:** `chapters/systematics.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/systematics-domains.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show Bacteria, Archaea and Eukarya as the three domains of cellular life. Viruses are not a fourth cellular domain and should be kept outside this tree.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 27. ../images/generated/systematics-ranks.webp

- **Название / краткое содержание:** Таксономические ранги на примере организма / Taxonomic ranks using one organism as an example. Вертикальная схема от домена до вида на одном корректно классифицированном примере; все ранги и написание биноминального названия проверить перед публикацией.
- **ID якоря:** `image-brief-systematics-ranks`
- **Страница:** `chapters/systematics.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/systematics-ranks.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Use one example with a verified classification and consistent rank order. Italicise genus/species binomials; do not invent a taxonomic assignment for a familiar organism.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 28. ../images/generated/systematics-tree.webp

- **Название / краткое содержание:** Как читать филогенетическое дерево / How to read a phylogenetic tree. Чёткая схема узлов, ветвей, сестринских групп и общего предка с примерами поворота ветвей без изменения родства; не трактовать положение выше как «более развитое».
- **ID якоря:** `image-brief-systematics-tree`
- **Страница:** `chapters/systematics.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/systematics-tree.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Nodes represent common ancestors and sister groups share a more recent common ancestor. Rotating branches around a node does not change relationships; vertical position is not evolutionary advancement.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 29. ../images/generated/zoology-vertebrates.webp

- **Название / краткое содержание:** Пять основных групп позвоночных / Five major vertebrate groups. Сравнительная естественнонаучная пластина рыб, земноводных, пресмыкающихся, птиц и млекопитающих с характерными признаками и оговоркой о разнообразии внутри групп.
- **ID якоря:** `image-brief-zoology-vertebrates`
- **Страница:** `chapters/zoology.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/zoology-vertebrates.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** The five familiar teaching groups are a pedagogical overview, not five equivalent clades under modern phylogeny. Birds are nested within reptiles in cladistic classification.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 30. ../images/generated/zoology-anatomy.webp

- **Название / краткое содержание:** Сравнение покровов и способов дыхания / Comparison of body coverings and respiration. Сравнительная иллюстрация кожи/чешуи, перьев, волос и основных дыхательных органов позвоночных; не создавать впечатление, что один признак универсален для всей группы.
- **ID якоря:** `image-brief-zoology-anatomy`
- **Страница:** `chapters/zoology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/zoology-anatomy.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Treat body coverings and respiratory structures as group-level patterns with exceptions. Do not imply every fish, amphibian or reptile has one identical respiratory arrangement.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 31. ../images/generated/zoology-adaptation.webp

- **Название / краткое содержание:** Адаптации животных к среде обитания / Animal adaptations to habitats. Сопоставление водной, наземной и воздушной сред с соответствующими адаптациями конечностей, покровов и органов чувств; без фантастических промежуточных форм.
- **ID якоря:** `image-brief-zoology-adaptation`
- **Страница:** `chapters/zoology.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/zoology-adaptation.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Show inherited population-level adaptations shaped over generations, not individuals changing their bodies because they need to. Match each structure to a plausible habitat and function.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 32. ../images/generated/flora-altitude.webp

- **Название / краткое содержание:** Высотная мозаика растительности Кыргызстана / Altitudinal vegetation mosaic of Kyrgyzstan. Панорама от предгорных полупустынь через степи, арчовые и еловые леса к субальпийским и альпийским лугам; высотные границы условны и меняются по склонам.
- **ID якоря:** `image-brief-flora-altitude`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/flora-altitude.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Keep vegetation belts as a broad mosaic whose limits vary with aspect, moisture and local relief. Do not add exact elevations or imply a uniform sequence on every mountain slope.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 33. ../images/generated/flora-jalalabad.webp

- **Название / краткое содержание:** Ландшафты флоры Джалал-Абадской области / Flora landscapes of Jalal-Abad Region. Ботаническая панорама орехоплодового леса Арсланбоба, лесных склонов и влажных ущелий; растения изображать как характерные сообщества, не как полный список видов.
- **ID якоря:** `image-brief-flora-jalalabad`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/flora-jalalabad.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 34. ../images/generated/flora-issyk.webp

- **Название / краткое содержание:** Растительность Иссык-Кульской котловины / Vegetation of the Issyk-Kul basin. Мозаика озёрных дельт и болот, сухих западных предгорий и еловых лесов Терскей-Ала-Тоо; не переносить растения одной зоны в другую.
- **ID якоря:** `image-brief-flora-issyk`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/flora-issyk.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 35. ../images/generated/flora-naryn.webp

- **Название / краткое содержание:** Высокогорные луга и степи Нарынской области / High-altitude meadows and steppes of Naryn Region. Ландшафт Сон-Куля, Чатыр-Куля и внутренних долин с водно-болотными, луговыми и степными сообществами; сезонность и высотность передать реалистично.
- **ID якоря:** `image-brief-flora-naryn`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/flora-naryn.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 36. ../images/generated/flora-osh.webp

- **Название / краткое содержание:** Лесные и горные сообщества Ошской области / Forest and mountain communities of Osh Region. Переход от орехоплодовых лесов к арчовым склонам и высокогорьям Памиро-Алая; не добавлять тропические или чуждые региону растения.
- **ID якоря:** `image-brief-flora-osh`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/flora-osh.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 37. ../images/generated/flora-batken.webp

- **Название / краткое содержание:** Айгуль и дикие тюльпаны Баткена / Aygul and wild tulips of Batken. Ботаническая натуралистическая пластина *Fritillaria eduardii* (синоним *Petilium eduardii*) и отдельно характерных диких тюльпанов Баткена; точная форма по ботаническим источникам, без смешения видов. Не изображать сбор, вытаптывание или неподтверждённый свободный доступ к охраняемой популяции.
- **ID якоря:** `image-brief-flora-batken`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/flora-batken.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 38. ../images/generated/flora-talas.webp

- **Название / краткое содержание:** Растительность Таласского Ала-Тоо / Vegetation of Talas Ala-Too. Горная панорама Беш-Таша с еловыми и арчовыми сообществами, речной поймой и субальпийскими лугами; композиция должна отражать реальные высотные пояса.
- **ID якоря:** `image-brief-flora-talas`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/flora-talas.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Use the Besh-Tash / Talas Ala-Too context from the chapter; distinguish riparian, forest and alpine communities. Any species label needs a Talas-specific source.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 39. ../images/generated/flora-chuy.webp

- **Название / краткое содержание:** От долины Чуя к высокогорьям / From the Chuy Valley to high elevations. Единый разрез от долинных степей и полупустынь к арчовым склонам Кыргызского хребта и высокогорным лугам; без выдуманных точных высотных отметок.
- **ID якоря:** `image-brief-flora-chuy`
- **Страница:** `chapters/flora-kyrgyzstan.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/flora-chuy.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Show the Chuy Valley-to-Kyrgyz Range transition without invented altitude labels. Keep valley steppe, juniper slopes and high meadows ecologically distinct.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 40. ../images/generated/fauna-habitats.webp

- **Название / краткое содержание:** Высотные местообитания и фауна Кыргызстана / Altitudinal habitats and fauna of Kyrgyzstan. Ландшафтная панорама от долин и тугайных участков до лесов, альпийских лугов и скал; животные показаны в подходящих местообитаниях, без карты точных ареалов.
- **ID якоря:** `image-brief-fauna-habitats`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P3
- **Точное имя файла:** `../images/generated/fauna-habitats.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Treat the scene as a habitat panorama, not a distribution map or census. Place animals in suitable zones and label it as a composite illustration if multiple sites are combined.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 41. ../images/generated/fauna-mammals.webp

- **Название / краткое содержание:** Крупные млекопитающие гор Кыргызстана / Large mammals of the Kyrgyz mountains. Натуралистическая сцена с ирбисом, архаром и сибирским горным козлом в горном ландшафте; корректные пропорции и поведение, виды не должны взаимодействовать искусственно.
- **ID якоря:** `image-brief-fauna-mammals`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-mammals.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 42. ../images/generated/fauna-birds.webp

- **Название / краткое содержание:** Птицы гор, озёр и водно-болотных угодий / Birds of mountains, lakes and wetlands. Композиция с характерными экологическими группами: хищная птица на скалах, высокогорная наземная птица и водоплавающие на озере; не изображать всех в одном микроместообитании.
- **ID якоря:** `image-brief-fauna-birds`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-birds.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 43. ../images/generated/fauna-freshwater.webp

- **Название / краткое содержание:** Пресноводная фауна Кыргызстана / Freshwater fauna of Kyrgyzstan. Энциклопедическая композиция: Иссык-Куль и прозрачная горная река, подводные и надводные планы, только достоверные местные рыбы из проверенных профилей главы; не добавлять неподтверждённые виды или подписи.
- **ID якоря:** `image-brief-fauna-freshwater`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-freshwater.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 44. ../images/generated/fauna-herps.webp

- **Название / краткое содержание:** Земноводные и пресмыкающиеся Кыргызстана / Amphibians and reptiles of Kyrgyzstan. Натуралистическая сравнительная пластина земноводного у влажного водоёма и рептилий сухих каменистых склонов; изображать только таксоны, подтверждённые источниками главы.
- **ID якоря:** `image-brief-fauna-herps`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/fauna-herps.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Keep amphibians associated with suitable moist breeding/shore habitats and reptiles in appropriate terrestrial settings. Use only taxa supported by the chapter; do not convert national-list inclusion into local occurrence.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 45. ../images/generated/fauna-invertebrates.webp

- **Название / краткое содержание:** Наземные беспозвоночные горных экосистем / Terrestrial invertebrates of mountain ecosystems. Макроиллюстрация нескольких экологических групп насекомых и других членистоногих с различимыми сегментами тела, конечностями и крыльями; не выдавать композицию за полный видовой перечень.
- **ID якоря:** `image-brief-fauna-invertebrates`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/fauna-invertebrates.webp`
- **Формат / пропорции / размер:** WebP, 4:3; 2000 × 1500 px
- **Дополнительные научные ограничения:** Use recognisable arthropod body plans and correct segment/appendage placement. A multi-group composition is illustrative, not a complete Kyrgyzstan species list.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 46. ../images/generated/fauna-jalalabad.webp

- **Название / краткое содержание:** Фауна Западного Тянь-Шаня / Fauna of the Western Tien Shan. Ландшафт Беш-Арала, Сары-Челека и лесных ущелий с местными горными и лесными животными; не наносить неподтверждённые границы ареалов.
- **ID якоря:** `image-brief-fauna-jalalabad`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-jalalabad.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 47. ../images/generated/fauna-issyk.webp

- **Название / краткое содержание:** Фауна Иссык-Кульской области / Fauna of Issyk-Kul Region. Экологическая панорама озера, дельт и заболоченных берегов, горных склонов и Сарычат-Ээрташа; водоплавающие птицы, рыбы и горные млекопитающие в раздельных местообитаниях.
- **ID якоря:** `image-brief-fauna-issyk`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-issyk.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 48. ../images/generated/fauna-naryn.webp

- **Название / краткое содержание:** Фауна высокогорий Нарынской области / Fauna of the Naryn highlands. Пейзаж Сон-Куля и Нарынского заповедника с маралом, горными хищниками и водоплавающими птицами в отдельных природных зонах; не показывать животных как совместное стадо.
- **ID якоря:** `image-brief-fauna-naryn`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-naryn.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 49. ../images/generated/fauna-osh.webp

- **Название / краткое содержание:** Фауна Памиро-Алая и юга Кыргызстана / Fauna of the Pamir-Alay and southern Kyrgyzstan. Горный ландшафт с лесными и арчовыми местообитаниями, хищниками и копытными; включать только виды с подтверждёнными региональными записями в тексте главы.
- **ID якоря:** `image-brief-fauna-osh`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-osh.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 50. ../images/generated/fauna-batken.webp

- **Название / краткое содержание:** Фауна сухих склонов Баткенской области / Fauna of Batken's dry slopes. Сухие предгорья и каменистые склоны Сурматаша и Саркента с характерными сурками, рептилиями и горными птицами; избегать выдуманных локальных эндемиков.
- **ID якоря:** `image-brief-fauna-batken`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P1
- **Точное имя файла:** `../images/generated/fauna-batken.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Detailed P1 review: see `IMAGE_SCIENTIFIC_REVIEW.md`; actual image not produced.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 51. ../images/generated/fauna-talas.webp

- **Название / краткое содержание:** Животные Таласского Ала-Тоо / Wildlife of Talas Ala-Too. Панорама Беш-Таша: елово-арчовые склоны, речная долина и высокогорные скалы с подтверждёнными для региона млекопитающими и птицами.
- **ID якоря:** `image-brief-fauna-talas`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/fauna-talas.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Use the Talas / Besh-Tash habitat context; separate river valley, forested slopes and high rocky terrain. Do not add unverified local endemics or unsupported species labels.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

### 52. ../images/generated/fauna-chuy.webp

- **Название / краткое содержание:** Фауна Чуйской области / Fauna of Chuy Region. Контраст долины Чуя, ущелья Ала-Арча и лесов Чон-Кемина с животными, подтверждёнными для соответствующих местообитаний; фотоловушечные виды не превращать в оценки численности.
- **ID якоря:** `image-brief-fauna-chuy`
- **Страница:** `chapters/fauna-kyrgyzstan.html`
- **Приоритет:** P2
- **Точное имя файла:** `../images/generated/fauna-chuy.webp`
- **Формат / пропорции / размер:** WebP, 16:9; 2400 × 1350 px
- **Дополнительные научные ограничения:** Separate Chuy Valley, Ala-Archa gorge and Chon-Kemin forest habitats. Match each animal to the habitat supported by the chapter rather than combining all species in one microhabitat.
- **Правило:** никаких текстовых подписей и обозначений внутри изображения; не добавлять неподтверждённые объекты. Подписи/alt будут подготовлены после проверки.

## 4. Дополнительные ограничения для 13 региональных P1-иллюстраций

### Флора Кыргызстана
- **flora-jalalabad.webp:** орехоплодовые леса Арсланбоба, лесистые склоны и влажные ущелья как мозаика местообитаний. Не подписывать каждое дерево как подтверждённую находку Арсланбоба без отдельного источника.
- **flora-issyk.webp:** разделить дельты/болота, сухие западные предгорья и еловые леса Терскей-Ала-Тоо. Не переносить водные растения на сухие склоны.
- **flora-naryn.webp:** Сон-Куль, Чатыр-Куль и внутренние долины — разные контексты. Берега озёр, влажные луга и сухие степи раздельно; сезон и снежный покров реалистичны.
- **flora-osh.webp:** переход от орехоплодовых лесов к арчовым склонам и высокогорьям Памиро-Алая. Не изображать тропический лес, непрерывный лесной пояс через сухие склоны или выдуманные эндемики.
- **flora-batken.webp:** принятое имя айгуль — *Fritillaria eduardii*; *Petilium eduardii* — синоним. Точно передать поникающие колокольчатые цветки и облиственный стебель. Не смешивать айгуль с другими дикими тюльпанами. Не изображать сбор, вытаптывание или туристов у редкой популяции; не заявлять текущий режим доступа.

### Фауна Кыргызстана
- **fauna-mammals.webp:** ирбис, архар и сибирский горный козёл — с правильной морфологией и в отдельных правдоподобных позициях. Современное имя ирбиса — *Panthera uncia* (старое *Uncia uncia* не означает другой вид). Не изображать атаку или искусственное взаимодействие.
- **fauna-birds.webp:** раздельно показать скальный участок с хищной птицей, высокогорную наземную птицу и водоплавающих на озере/болоте. Не помещать уларов в камыши, водоплавающих — на отвесные скалы. Конкретные виды — только при подтверждении в главе.
- **fauna-freshwater.webp:** не указывать общее число видов и не выдавать ограниченные выборки за полный список рыб Кыргызстана. Не добавлять виды из неопубликованного списка экспедиции Кемпир-Абада; спорную идентификацию *Triplophysa* не считать установленной. Использовать только виды с проверенным профилем и подтверждённым бассейном. Иссык-Куль и горную реку показать как разные системы; не подразумевать, что каждая рыба живёт в обеих.
- **fauna-jalalabad.webp:** Беш-Арал, Сары-Челек и лесные ущелья — панорама местообитаний, не перепись животных. Не рисовать точные границы ареалов и не помещать лесные и высокогорные виды в одно микроместообитание.
- **fauna-issyk.webp:** разделить озеро, водоплавающих птиц, дельты/болота и горные склоны/Сарычат-Ээрташ. Не подразумевать круглогодичное присутствие всех видов.
- **fauna-naryn.webp:** водоплавающие птицы — у озёрных угодий; марал — в подходящем лесном местообитании; альпийские млекопитающие — отдельно. Не помещать маралов на безлесный берег без подтверждения.
- **fauna-osh.webp:** включать только виды с подтверждёнными региональными записями для юга/конкретного места. Страновая запись не доказывает присутствие в Ошской области или заповеднике.
- **fauna-batken.webp:** сухие предгорья и каменистые склоны Сурматаша и Саркента. Сурков, рептилий и птиц добавлять только при подтверждении точной местности и местообитания; не выдумывать эндемиков.

## 5. Порядок генерации и пакетная выдача

Генерировать партиями по 5–8 отдельных файлов, чтобы можно было проверить качество до следующей партии. Сначала 13 P1, затем 26 P2, затем 13 P3. Не менять имена. Каждый файл — отдельный asset, не контактный лист.

Для каждой партии вернуть таблицу: точное имя файла, ID якоря, страница, приоритет, фактический размер, формат, соотношение сторон, описание, изображённые таксоны/структуры, известные ограничения. Сообщить обо всех отклонениях. Не переиспользовать один файл под несколькими именами. Не редактировать сайт.

## 6. Обязательная передача результата

1. ZIP-архив с папкой `biology/images/generated/` и всеми 52 файлами с точными именами.
2. Файл `GEMINI_IMAGE_MANIFEST.md`: одна запись на каждый файл — имя, anchor ID, страница, приоритет, формат, пиксели, размер файла, описание, таксоны (если есть), условно упрощённые детали, дата и модель генерации.
3. Список файлов, которые не удалось создать, с причиной. Не заявлять 52/52, если уникальных файлов меньше.
4. Если архивов несколько — перечислить каждый архив и содержимое.
5. Дать ссылку/путь, по которому можно скачать именно исходные файлы и manifest, а не только превью.

## 7. Граница ответственности

Gemini выполняет только генерацию и возвращает файлы/manifest. Не изменять HTML/CSS/JavaScript, имена, пути, якоря, alt-тексты сайта и статусы утверждения. После получения файлов интегратор проверит наличие и уникальность, формат/размеры, научную корректность, происхождение и соответствие якорям. Только после проверки одобренные изображения будут интегрированы в `workspace/biology`; исходные заметки сохраняются до успешной проверки.

**Текущий статус на момент подготовки задания:** 0 из 52 изображений сгенерированы, научно проверены и интегрированы. Этот документ — production hand-off, а не подтверждение готовности иллюстраций.
