# Глава 15. Дистанционное зондирование Земли
# Chapter 15. Remote Sensing of the Earth

> **Часть III. Современная география и технологии / Part III. Modern Geography and Technology**  
> Научно-образовательный атлас географии / Scientific and Educational Geography Atlas

## Цели главы / Chapter objectives

Дистанционное зондирование Земли (ДЗЗ) — получение информации о поверхности и атмосфере без непосредственного контакта с исследуемым объектом, преимущественно с помощью датчиков на спутниках, самолётах и беспилотных летательных аппаратах. Данные ДЗЗ позволяют наблюдать большие территории, повторять измерения во времени и изучать процессы, труднодоступные для наземных обследований.

Глава рассматривает физические основы дистанционного зондирования, электромагнитный спектр, активные и пассивные сенсоры, спутниковые программы, пространственное и временное разрешение, предварительную обработку, спектральные индексы, классификацию, радарные наблюдения, мониторинг изменений и ограничения интерпретации.

Remote sensing of the Earth is the acquisition of information about the surface and atmosphere without direct physical contact, primarily using sensors carried by satellites, aircraft and uncrewed aerial vehicles. Remote sensing data enable large-area observation, repeated measurements and the study of processes that are difficult to investigate through field surveys alone.

This chapter introduces the physical principles of remote sensing, the electromagnetic spectrum, active and passive sensors, satellite programmes, spatial and temporal resolution, preprocessing, spectral indices, classification, radar observations, change detection and interpretation limits.

## 15.1. Понятие и значение ДЗЗ / Concept and Importance of Remote Sensing

Дистанционное зондирование основано на регистрации электромагнитного излучения, отражённого, испускаемого или рассеянного объектами и атмосферой. По измеренным сигналам можно получать сведения о свойствах поверхности, растительности, воде, снегу, льде, облачности, температуре и изменениях землепользования.

Основные платформы:
- **спутники:** обеспечивают регулярное наблюдение больших территорий и глобальный охват;
- **самолёты:** позволяют выполнять съёмку с гибким выбором высоты, сенсора и времени;
- **беспилотные летательные аппараты (БПЛА):** дают детальные изображения локальных участков, но имеют ограничения по площади, погоде, разрешениям на полёты и времени работы;
- **наземные и стационарные платформы:** используются для калибровки, проверки и локального мониторинга.

ДЗЗ дополняет полевые исследования, а не заменяет их. Спутниковый сигнал требует интерпретации и проверки, особенно если речь идёт о конкретном виде растений, типе почвы, причине изменения или юридическом статусе территории.

## 15.2. Электромагнитное излучение и спектральные диапазоны / Electromagnetic Radiation and Spectral Regions

Электромагнитное излучение характеризуется длиной волны и частотой. В дистанционном зондировании применяют видимый свет, ближний и коротковолновый инфракрасный диапазоны, тепловое инфракрасное излучение и микроволны.

Основные диапазоны:
- **видимый:** примерно 0,4–0,7 мкм; воспринимаемые человеком цвета;
- **ближний инфракрасный (NIR):** примерно 0,7–1,3 мкм; чувствителен к структуре и состоянию растительности;
- **коротковолновый инфракрасный (SWIR):** примерно 1,3–3 мкм; полезен для анализа влажности, минералов, пожаров и некоторых характеристик поверхности;
- **тепловой инфракрасный (TIR):** диапазон длин волн, используемый для оценки собственного теплового излучения поверхности;
- **микроволновый:** радиодиапазон, применяемый в радиолокационных системах и некоторых пассивных наблюдениях.

Границы диапазонов условны и зависят от принятой классификации и характеристик сенсора. Атмосфера поглощает излучение в определённых спектральных областях, поэтому спутниковые датчики часто используют атмосферные «окна», где передача сигнала сравнительно благоприятна.

## 15.3. Отражение, поглощение и спектральная сигнатура / Reflection, Absorption and Spectral Signature

Когда излучение достигает поверхности, часть энергии отражается, часть поглощается, а часть может проходить через материал. Соотношение зависит от длины волны, состава, влажности, структуры и состояния объекта.

**Спектральная сигнатура** — характерная зависимость отражательной способности или излучения объекта от длины волны. Она помогает различать типы поверхности, но не является уникальным «отпечатком» при любых условиях.

Примеры:
- здоровая зелёная растительность обычно сильно поглощает красный свет хлорофиллом и отражает значительную долю ближнего инфракрасного излучения;
- вода обычно имеет низкую отражательную способность в ближнем инфракрасном диапазоне, но результат зависит от мутности, глубины, взвесей и отражения неба;
- сухая почва и влажная почва часто различаются по спектральному отклику, особенно в инфракрасных диапазонах;
- снег и лёд имеют характерные спектральные свойства, но загрязнение, размер кристаллов и жидкая вода меняют отражение.

На спектральный сигнал влияют атмосфера, угол освещения, угол наблюдения, рельеф, тени, сезон и калибровка датчика. Поэтому сравнение снимков требует контроля условий съёмки.

## 15.4. Пассивные и активные сенсоры / Passive and Active Sensors

### Пассивное зондирование / Passive sensing

Пассивные сенсоры регистрируют естественное излучение: отражённое солнечное или собственное тепловое излучение Земли. Оптические мультиспектральные и гиперспектральные камеры — распространённые примеры пассивных систем.

Ограничения оптических наблюдений:
- облака и дым закрывают поверхность;
- освещение зависит от времени суток и сезона;
- тени и рельеф усложняют сравнение;
- часть спектральных диапазонов сильно поглощается атмосферой.

### Активное зондирование / Active sensing

Активный сенсор сам излучает сигнал и регистрирует его отражение или рассеяние. Примеры — радар с синтезированной апертурой (SAR) и лазерное сканирование LiDAR.

Активные системы могут работать независимо от солнечного освещения. Радарные микроволны во многих случаях позволяют получать данные сквозь облачность, однако сигнал зависит от влажности, шероховатости, геометрии наблюдения и структуры объектов. LiDAR измеряет время прохождения лазерного импульса и позволяет получать трёхмерные сведения о поверхности и объектах.

## 15.5. Типы спутниковых данных и сенсоров / Satellite Data and Sensor Types

Спутниковые сенсоры различаются по спектральным каналам, пространственному разрешению, полосе захвата, частоте повторного наблюдения и радиометрической чувствительности.

Основные типы:
- **панхроматические:** один широкий спектральный канал, часто с более высоким пространственным разрешением;
- **мультиспектральные:** несколько относительно широких каналов;
- **гиперспектральные:** десятки или сотни узких, смежных спектральных каналов;
- **тепловые:** регистрируют тепловое излучение поверхности;
- **радиолокационные:** измеряют обратное рассеяние микроволнового сигнала;
- **альтиметрические и лидарные:** измеряют высоту поверхности, расстояния или структуру объектов.

Примеры широко используемых программ и миссий:
- **Landsat** — длительный архив наблюдений суши, совместная программа NASA и USGS;
- **Sentinel** — семейство миссий программы Copernicus Европейского союза и Европейского космического агентства;
- **MODIS** — приборы на спутниках Terra и Aqua, обеспечивающие частые глобальные наблюдения;
- **VIIRS** — приборы для наблюдения поверхности, облаков, температуры и ночных огней;
- **Sentinel-1** — радарная миссия SAR;
- **Sentinel-2** — оптическая мультиспектральная съёмка суши;
- **Sentinel-3** — наблюдения океана, суши и температуры поверхности;
- **ICESat-2** — спутниковая лазерная альтиметрия;
- **WorldView и другие коммерческие системы** — высокодетальные данные с условиями доступа, зависящими от поставщика.

Названия миссий, статус работы, доступность каналов и технические параметры необходимо проверять по актуальной документации операторов.

## 15.6. Четыре вида разрешения / Four Types of Resolution

Для интерпретации данных важно различать четыре характеристики.

**Пространственное разрешение** — размер элемента изображения на местности или степень детализации. Пиксель 10 м представляет участок поверхности, а не обязательно отдельный объект размером 10 м.

**Спектральное разрешение** — число, ширина и расположение спектральных каналов. Узкие и многочисленные каналы позволяют анализировать тонкие спектральные различия.

**Временное разрешение** — интервал повторного наблюдения одной территории. Фактическая частота пригодных снимков зависит от облачности, орбиты, режима съёмки и доступности данных.

**Радиометрическое разрешение** — способность сенсора различать уровни интенсивности сигнала, обычно связанная с числом бит цифрового представления и характеристиками прибора.

Высокое разрешение одного типа не гарантирует высокого разрешения другого. Для мониторинга быстро меняющихся процессов частые наблюдения могут быть важнее очень мелкого пикселя.

## 15.7. Геометрическая и радиометрическая обработка / Geometric and Radiometric Preprocessing

Исходные спутниковые данные могут содержать геометрические и радиометрические искажения. Перед анализом обычно выполняют подготовительные операции.

Основные этапы:
1. проверка метаданных, даты, сенсора и уровня обработки;
2. геометрическая коррекция и ортотрансформирование, если они необходимы;
3. радиометрическая калибровка цифровых значений;
4. атмосферная коррекция для получения сопоставимых оценок отражения поверхности;
5. маскирование облаков, теней и нежелательных областей;
6. коррекция влияния рельефа для горных территорий, если это требуется;
7. приведение данных к общей сетке, проекции и пространственному разрешению;
8. контроль качества и документирование параметров.

Не все продукты требуют одинаковой обработки. Например, готовый продукт поверхностного отражения уже прошёл определённые этапы коррекции. Повторная обработка без понимания уровня продукта может ухудшить данные.

## 15.8. Цветовые композиции и визуальная интерпретация / Colour Composites and Visual Interpretation

Мультиспектральные снимки часто отображают как цветовые композиции, назначая отдельные спектральные каналы красному, зелёному и синему цветам экрана.

**Естественная цветовая композиция** использует каналы видимого диапазона и приближает изображение к привычному зрению. **Ложная цветовая композиция** назначает каналам условные цвета, чтобы выделить нужные свойства.

Например, назначение ближнего инфракрасного канала красному экранному каналу позволяет сделать растительность яркой, поскольку она часто сильно отражает NIR. Но цвет на ложной композиции не является реальным цветом объекта.

Визуальная интерпретация учитывает:
- тон и цвет;
- текстуру;
- форму;
- размер;
- тень;
- рисунок и пространственное положение;
- контекст соседних объектов;
- сезон и условия съёмки.

Один и тот же объект может выглядеть по-разному в зависимости от сенсора, композиции и даты.

## 15.9. Спектральные индексы / Spectral Indices

Спектральные индексы — математические комбинации каналов, предназначенные для усиления определённых различий в данных. Они помогают предварительно оценивать состояние растительности, водных объектов, застроенных территорий и другие характеристики.

### NDVI — нормализованный разностный вегетационный индекс

\[
NDVI = \frac{NIR - Red}{NIR + Red}
\]

NDVI широко применяется для оценки относительной активности зелёной растительности. Значения обычно лежат в диапазоне от −1 до +1, но интерпретация зависит от сенсора, поверхности, сезона и обработки.

Ограничения NDVI:
- насыщение в густой растительности;
- влияние почвенного фона при редком растительном покрове;
- чувствительность к атмосфере и теням;
- невозможность напрямую определить вид растения или точную биомассу без дополнительных данных.

### NDWI и водные индексы / Water indices

Под названием NDWI используются разные формулы. Один вариант, предложенный для выделения открытой воды, сочетает зелёный и ближний инфракрасный каналы:

\[
NDWI = \frac{Green - NIR}{Green + NIR}
\]

Другой индекс, часто называемый NDMI или вариантом NDWI для влажности растительности, использует NIR и SWIR:

\[
NDMI = \frac{NIR - SWIR}{NIR + SWIR}
\]

В публикации индекса всегда указывать формулу и используемые каналы: одинаковое сокращение в разных источниках может обозначать разные показатели.

### NDBI — индекс застроенных территорий / Built-up Index

\[
NDBI = \frac{SWIR - NIR}{SWIR + NIR}
\]

NDBI может помогать выделять застроенные участки, но спектрально похожие сухие почвы, горные породы и другие поверхности могут давать сходный отклик. Индекс не является готовой картой зданий.

### NBR — нормализованный индекс выгоревших территорий / Burn Ratio

\[
NBR = \frac{NIR - SWIR}{NIR + SWIR}
\]

Разность NBR до и после пожара (dNBR) используется для оценки изменений, связанных с выгоранием. Интерпретация требует учитывать сезон, влажность, тип растительности и другие причины спектральных изменений.

## 15.10. Классификация спутниковых изображений / Satellite Image Classification

Классификация присваивает пикселям или объектам категории земного покрова или другие тематические классы.

Основные подходы:
- **контролируемая классификация:** алгоритм обучается на заранее размеченных примерах;
- **неконтролируемая классификация:** алгоритм группирует пиксели по сходству спектральных характеристик;
- **объектно-ориентированный анализ:** классифицируются сегменты или объекты, а не отдельные пиксели;
- **машинное обучение:** используются алгоритмы, например Random Forest, Support Vector Machine и нейронные сети.

Типичные классы земного покрова: лес, кустарник, пашня, пастбище, застройка, вода, снег и лёд, голая почва. Схема классов должна соответствовать цели и масштабу проекта.

### Обучающие и проверочные данные / Training and validation data

Обучающие образцы используются для настройки модели, а независимые проверочные данные — для оценки качества классификации. Если одни и те же участки используются и для обучения, и для проверки, точность может быть завышена.

Матрица ошибок (confusion matrix) показывает совпадения и расхождения между классификацией и эталонными данными. Общая точность не раскрывает все ошибки: важно анализировать точность пользователя и производителя по классам, а также учитывать дисбаланс классов и дизайн выборки.

## 15.11. Радарное зондирование и SAR / Radar Remote Sensing and SAR

Радар с синтезированной апертурой (SAR) использует микроволновые импульсы и регистрирует обратное рассеяние от поверхности. Радарные данные особенно полезны там, где оптические наблюдения ограничены облачностью или отсутствием солнечного освещения.

Сигнал SAR зависит от:
- шероховатости поверхности относительно длины волны;
- влажности почвы и растительности;
- геометрии объекта и угла наблюдения;
- структуры лесного покрова;
- поляризации сигнала;
- длины волны и параметров сенсора.

Применения SAR:
- картирование затоплений;
- мониторинг деформаций поверхности методом интерферометрии;
- оценка влажности и состояния почв при подходящих условиях;
- наблюдение лесов и сельскохозяйственных угодий;
- мониторинг ледников и морского льда;
- обнаружение изменений инфраструктуры.

Радарное изображение не является фотографией в обычном смысле. Яркость пикселя отражает особенности обратного рассеяния и геометрии, поэтому интерпретация требует специальных знаний.

## 15.12. LiDAR и трёхмерное зондирование / LiDAR and Three-dimensional Remote Sensing

LiDAR (Light Detection and Ranging) измеряет расстояние по времени прохождения лазерного импульса. Системы могут быть установлены на самолётах, БПЛА, автомобилях или спутниках.

Результат часто представляется облаком точек, где каждая точка имеет координаты и дополнительные атрибуты. По облаку точек можно создавать:
- цифровую модель поверхности (DSM);
- цифровую модель рельефа (DTM);
- модели зданий и растительности;
- профили и трёхмерные представления объектов.

Лазерные импульсы могут частично проходить через промежутки в растительном покрове, позволяя получать отражения от разных уровней полога и поверхности земли. Однако плотность точек, характеристики сенсора и алгоритмы классификации определяют качество результата.

## 15.13. Мониторинг изменений и временные ряды / Change Detection and Time Series

Мониторинг изменений сравнивает данные разных дат для выявления преобразований поверхности и природных процессов.

Основные методы:
- сравнение классифицированных карт;
- вычитание и нормализация спектральных каналов;
- анализ изменений индексов;
- временные профили пикселей;
- объектный анализ;
- статистические методы обнаружения трендов и сезонности.

Перед сравнением важно обеспечить:
- сопоставимые сезоны и фенологические стадии;
- одинаковую или согласованную систему координат;
- сопоставимые пространственные разрешения;
- радиометрическую и атмосферную согласованность;
- одинаковую схему классов;
- маскирование облаков, теней и снега, если они не являются предметом анализа.

Изменение спектрального сигнала не всегда означает изменение земного покрова. Оно может быть вызвано влажностью, сезоном, углом наблюдения, атмосферой или различиями сенсоров.


### 15.13.1. Практический пример: сезонность или реальное изменение земного покрова? / Worked Example: Seasonality or Actual Land-cover Change?

Предположим, на спутниковом снимке одного участка в июле растительность выглядит значительно зеленее, чем на снимке того же участка в марте. Нельзя сразу заключать, что площадь леса увеличилась или экосистема восстановилась: разница может объясняться сезонным развитием растений, сроками сельскохозяйственных работ, влажностью почвы, облачностью, тенями или различиями обработки изображений.

Для проверки следует:

1. Сопоставить снимки одного и того же сезона в разные годы, если задача — выявить долгосрочное изменение.
2. Использовать одинаковые или сопоставимые сенсоры, пространственное разрешение и методы атмосферной коррекции.
3. Проверить геометрическое совмещение снимков: смещение даже на несколько пикселей может создать ложные границы изменений.
4. Маскировать облака, тени и снег, а также учитывать сезонные особенности территории.
5. Сравнить результат с полевыми наблюдениями, более детальными изображениями или независимыми данными.

Если сравниваются разные сезоны, вывод следует формулировать как сезонное различие спектрального отклика, пока нет дополнительных доказательств долговременного изменения земного покрова.

Suppose vegetation on a satellite image of a site appears much greener in July than in March. It is not safe to conclude immediately that forest area has increased or that an ecosystem has recovered. The difference may reflect seasonal plant growth, agricultural calendars, soil moisture, cloud cover, shadows or differences in image processing.

To investigate the change:

1. Compare images from the same season in different years when the goal is to detect long-term change.
2. Use the same or comparable sensors, spatial resolution and atmospheric-correction methods.
3. Check geometric co-registration: a shift of even a few pixels can create false change boundaries.
4. Mask clouds, shadows and snow, and account for the seasonal characteristics of the area.
5. Compare the result with field observations, higher-resolution imagery or independent datasets.

When different seasons are compared, describe the result as a seasonal difference in spectral response unless additional evidence supports a long-term land-cover change.

## 15.14. ДЗЗ для изучения природных опасностей и чрезвычайных ситуаций / Remote Sensing for Hazards and Disasters

Данные ДЗЗ помогают до, во время и после чрезвычайных ситуаций:
- картировать площади затопления;
- выявлять следы лесных и степных пожаров;
- оценивать последствия оползней и землетрясений;
- наблюдать движение ледников и изменения ледниковых озёр;
- отслеживать пыльные бури и вулканические выбросы;
- оценивать ущерб сельскому хозяйству и инфраструктуре.

Для оперативного реагирования важны скорость получения данных, доступность снимков, облачность, разрешение и надёжность классификации. Спутниковая карта должна сопровождаться временем съёмки: изображение, полученное после прохождения паводковой волны, может не отражать максимальную площадь затопления.

ДЗЗ следует сочетать с наземными наблюдениями, метеорологическими данными, сообщениями служб и проверенными сведениями о населении и инфраструктуре.

## 15.15. Ограничения, неопределённость и этика ДЗЗ / Limitations, Uncertainty and Ethics

Данные дистанционного зондирования имеют ограничения:
- облачность, дым, туман и атмосферные помехи;
- различия сенсоров и алгоритмов;
- смешанные пиксели на границах объектов;
- сезонные и угловые эффекты;
- недостаток эталонных наземных наблюдений;
- неопределённость классификации и моделей;
- задержки публикации и ограничения доступа.

Этические вопросы включают наблюдение за частными территориями, защиту персональных данных, безопасность объектов, права коренных народов и местных сообществ, а также риск неверного использования карт и аналитики.

Коммерческая доступность снимка не отменяет требований законодательства, лицензии и ответственного обращения с данными. Для публикации чувствительных координат следует оценивать возможный вред.

### 15.15.1. Как отличать реальное изменение от различий съёмки / Separating Real Change from Image Differences

Разность двух спутниковых изображений не всегда означает изменение земной поверхности. Снимки могли быть получены в разные сезоны, при разной облачности, освещённости, влажности почвы, угле наблюдения или разными сенсорами.

Перед сравнением проверяют геометрическую регистрацию, сопоставимость сезонов и дат, маски облаков и теней, атмосферную коррекцию, разрешение, спектральные диапазоны и радиометрическую калибровку. Необходимо документировать алгоритм и порог обнаружения изменений.

В горах интерпретацию усложняют снег, тени склонов и различия сезонного развития растительности по высотным поясам. Например, снижение растительного индекса летом по сравнению с весной может отражать сезонную фенологию, а не деградацию пастбища.

**Проверка.** Выборочные полевые наблюдения, геопривязанные фотографии и независимые данные помогают подтвердить интерпретацию. Для классификации используют матрицу ошибок по независимой выборке; общая точность может скрывать слабое распознавание редких классов.

**Задание.** Сравните два условных снимка одного водосбора, сделанных весной и летом. Перечислите факторы, которые нужно контролировать, прежде чем объявлять снижение растительного индекса деградацией, и предложите способ проверки на местности.

A difference between two satellite images does not always indicate a change on the Earth's surface. Images may have been acquired in different seasons, under different cloud, illumination, soil-moisture or viewing-angle conditions, or by different sensors.

Before comparison, check geometric registration, comparable seasons and dates, cloud and shadow masks, atmospheric correction, resolution, spectral bands and radiometric calibration. Document the change-detection algorithm and threshold.

In mountain areas, snow, slope shadows and seasonal vegetation differences across elevation belts complicate interpretation. For example, a lower vegetation index in summer than in spring may reflect seasonal phenology rather than pasture degradation.

**Validation.** Sample field observations, georeferenced photographs and independent data help confirm an interpretation. Classification should be assessed with an error matrix based on an independent sample; overall accuracy may conceal poor detection of rare classes.

**Activity.** Compare two hypothetical images of the same catchment acquired in spring and summer. List the factors to control before interpreting a lower vegetation index as degradation, and propose a field-validation method.

### 15.15.2. Как отличить реальное изменение от различий съёмки / Separating Real Change from Acquisition Differences

Разница между двумя спутниковыми изображениями не всегда означает изменение на местности. Её могут вызвать разные сезоны, угол освещения и наблюдения, облачность, атмосферные условия, сенсор, пространственное разрешение, геометрическая коррекция или обработка. Прежде чем классифицировать участок как изменившийся, необходимо проверить сопоставимость изображений.

**Минимальные условия сравнения:** одинаковая или близкая сезонная фаза; облачные и теневые участки исключены или обработаны; изображения приведены к сопоставимой геометрии и системе координат; радиометрические значения откалиброваны и, если требуется, скорректированы на атмосферу; выбран единый алгоритм классификации или расчёта индекса. Для растительности важно учитывать фенологию: естественное сезонное пожелтение не равно деградации.

**Проверка результата.** Используйте независимые контрольные участки или данные более высокого разрешения, изучайте матрицу ошибок и отдельно оценивайте классы изменений. Сопоставляйте результат с полевыми наблюдениями, метеорологическими данными и сведениями о землепользовании. Для малых объектов результат может быть искажён смешанными пикселями, в которых объединены несколько типов поверхности.

**Учебное задание.** Представьте два изображения одной долины, полученные в разные месяцы. Составьте список факторов, которые могут объяснить различия растительного индекса без долгосрочного изменения земного покрова. Предложите план проверки, прежде чем делать вывод о деградации пастбища.

A difference between two satellite images does not always represent a change on the ground. It may result from different seasons, illumination and viewing angles, cloud cover, atmospheric conditions, sensors, spatial resolution, geometric correction or processing. Before classifying an area as changed, check whether the images are comparable.

**Minimum comparison conditions:** the same or a similar seasonal phase; cloud and shadow areas masked or treated; images aligned to comparable geometry and a common coordinate reference system; radiometric values calibrated and, where needed, atmospherically corrected; and a consistent classification or index method. For vegetation, account for phenology: natural seasonal browning is not the same as degradation.

**Validate the result.** Use independent reference sites or higher-resolution data, examine the error matrix and assess change classes separately. Compare the result with field observations, meteorological data and land-use information. Small features may be distorted by mixed pixels containing several surface types.

**Activity.** Imagine two images of the same valley acquired in different months. List factors that could explain differences in a vegetation index without long-term land-cover change. Propose a validation plan before concluding that a pasture has degraded.

## English-language chapter text

### 15.1. Concept and Importance of Remote Sensing

Remote sensing is based on detecting electromagnetic radiation reflected, emitted or scattered by objects and the atmosphere. The measured signals can provide information about surface properties, vegetation, water, snow, ice, clouds, temperature and land-use change.

Main platforms include satellites, which provide regular observations over large areas and global coverage; aircraft, which allow flexible choices of altitude, sensor and timing; uncrewed aerial vehicles (UAVs), which provide detailed imagery of local areas but are limited by coverage, weather, flight permissions and operating time; and ground-based or stationary platforms used for calibration, validation and local monitoring.

Remote sensing complements field research rather than replacing it. Satellite signals require interpretation and validation, especially when identifying a particular plant species, soil type, cause of change or legal status of a territory.

### 15.2. Electromagnetic Radiation and Spectral Regions

Electromagnetic radiation is characterised by wavelength and frequency. Remote sensing uses visible light, near-infrared and shortwave-infrared regions, thermal infrared radiation and microwaves.

Approximate spectral regions include:
- **visible:** about 0.4–0.7 μm, the colours perceived by the human eye;
- **near-infrared (NIR):** about 0.7–1.3 μm, sensitive to vegetation structure and condition;
- **shortwave infrared (SWIR):** about 1.3–3 μm, useful for analysing moisture, minerals, fires and some surface characteristics;
- **thermal infrared (TIR):** wavelengths used to assess the surface's own thermal emission; and
- **microwave:** the radio-frequency region used by radar systems and some passive observations.

Boundaries are approximate and depend on the classification and sensor characteristics. The atmosphere absorbs radiation in particular spectral regions, so satellite sensors often use atmospheric windows where transmission is relatively favourable.

### 15.3. Reflection, Absorption and Spectral Signatures

When radiation reaches a surface, some energy is reflected, some absorbed and some may pass through the material. The proportions depend on wavelength, composition, moisture, structure and surface condition.

A **spectral signature** is the characteristic variation of an object's reflectance or emission with wavelength. It helps distinguish surface types, but it is not a unique fingerprint under all conditions.

Examples:
- healthy green vegetation usually absorbs red light strongly through chlorophyll and reflects a substantial share of near-infrared radiation;
- water usually has low reflectance in the near-infrared, although turbidity, depth, suspended material and sky reflection affect the signal;
- dry and wet soils often differ spectrally, particularly in infrared regions; and
- snow and ice have characteristic spectral properties, but impurities, crystal size and liquid water change reflectance.

Atmosphere, illumination angle, viewing angle, relief, shadows, season and sensor calibration all affect the measured signal. Image comparison therefore requires control of acquisition conditions.

### 15.4. Passive and Active Sensors

**Passive sensors** detect natural radiation: reflected sunlight or Earth's own thermal emission. Optical multispectral and hyperspectral cameras are common examples.

Limitations of optical observations include cloud and smoke obstruction; illumination changes with time of day and season; shadows and relief complicate comparison; and some spectral regions are strongly absorbed by the atmosphere.

**Active sensors** emit their own signal and detect its reflection or scattering. Examples include Synthetic Aperture Radar (SAR) and laser scanning (LiDAR).

Active systems can operate independently of sunlight. Radar microwaves can often collect data through cloud cover, but the signal depends on moisture, surface roughness, viewing geometry and object structure. LiDAR measures the travel time of laser pulses and provides three-dimensional information about surfaces and objects.

### 15.5. Satellite Data and Sensor Types

Satellite sensors differ in spectral bands, spatial resolution, swath width, revisit frequency and radiometric sensitivity.

Main types include:
- **panchromatic:** one broad spectral band, often with higher spatial resolution;
- **multispectral:** several relatively broad bands;
- **hyperspectral:** dozens or hundreds of narrow, contiguous bands;
- **thermal:** sensors that detect thermal radiation from the surface;
- **radar:** sensors that measure microwave backscatter; and
- **altimetric and LiDAR systems:** sensors that measure surface height, distance or object structure.

Widely used missions include Landsat, a long-term land-observation archive operated by NASA and USGS; Sentinel, a family of missions within the European Union's Copernicus programme and the European Space Agency; MODIS on Terra and Aqua, which provides frequent global observations; VIIRS, used to observe the surface, clouds, temperature and night lights; Sentinel-1 for SAR; Sentinel-2 for optical multispectral land imaging; Sentinel-3 for ocean, land and surface-temperature observations; ICESat-2 for satellite laser altimetry; and commercial high-resolution systems such as WorldView.

Mission names, operational status, band availability and technical parameters must be checked against current operator documentation.

### 15.6. Four Types of Resolution

Four characteristics should be distinguished when interpreting remote-sensing data.

**Spatial resolution** is the ground size of an image element or the level of detail. A 10 m pixel represents an area of the surface; it does not necessarily represent a separate object that is 10 m in size.

**Spectral resolution** is the number, width and position of spectral bands. Narrower and more numerous bands can reveal subtle spectral differences.

**Temporal resolution** is the interval between observations of the same area. The actual frequency of usable images depends on cloud cover, orbit, acquisition mode and data availability.

**Radiometric resolution** is the sensor's ability to distinguish signal-intensity levels, usually related to the number of digital bits and instrument characteristics.

High resolution in one dimension does not guarantee high resolution in another. For monitoring rapidly changing processes, frequent observations may be more important than very small pixels.

### 15.7. Geometric and Radiometric Preprocessing

Raw satellite data may contain geometric and radiometric distortions. Preprocessing commonly includes checking metadata, acquisition date, sensor and processing level; geometric correction and orthorectification where needed; radiometric calibration of digital values; atmospheric correction to obtain comparable surface-reflectance estimates; masking clouds, shadows and unwanted areas; terrain correction for mountainous areas where necessary; alignment to a common grid, projection and spatial resolution; and quality control with documentation of parameters.

Not all products require the same processing. For example, a surface-reflectance product has already undergone certain correction steps. Reprocessing without understanding the product level may degrade the data.

### 15.8. Colour Composites and Visual Interpretation

Multispectral images are often displayed as colour composites by assigning individual spectral bands to the red, green and blue channels of a screen.

A **true-colour composite** uses visible bands and approximates human vision. A **false-colour composite** assigns bands to artificial display colours to emphasise selected surface properties.

For example, assigning the near-infrared band to the screen's red channel can make vegetation appear bright because vegetation often strongly reflects NIR. The displayed colour in a false-colour composite is not the object's actual colour.

Visual interpretation considers tone and colour; texture; shape; size; shadow; pattern and spatial position; context of neighbouring features; season; and acquisition conditions.

The same feature may look different depending on sensor, band combination and acquisition date.

### 15.9. Spectral Indices

Spectral indices are mathematical combinations of bands designed to enhance particular differences in data. They can provide preliminary information about vegetation, water bodies, built-up areas and other surface characteristics.

**NDVI — Normalized Difference Vegetation Index**

NDVI = (NIR − Red) / (NIR + Red)

NDVI is widely used to assess the relative activity of green vegetation. Values generally range from −1 to +1, but interpretation depends on sensor, surface, season and processing.

Limitations include saturation in dense vegetation; influence of soil background where vegetation is sparse; sensitivity to atmosphere and shadows; and inability to identify plant species or exact biomass directly without additional data.

**NDWI and water indices.** The name NDWI is used for different formulas. One version, designed to identify open water, combines green and near-infrared bands:

NDWI = (Green − NIR) / (Green + NIR)

Another index, often called NDMI or an NDWI variant for vegetation moisture, uses NIR and SWIR:

NDMI = (NIR − SWIR) / (NIR + SWIR)

Always state the formula and bands used: the same abbreviation may refer to different indicators in different sources.

**NDBI — Normalized Difference Built-up Index**

NDBI = (SWIR − NIR) / (SWIR + NIR)

NDBI may help identify built-up areas, but spectrally similar dry soils, rocks and other surfaces can produce similar responses. It is not a ready-made building map.

**NBR — Normalized Burn Ratio**

NBR = (NIR − SWIR) / (NIR + SWIR)

The difference between pre-fire and post-fire NBR (dNBR) is used to assess changes associated with burning. Interpretation must account for season, moisture, vegetation type and other causes of spectral change.

### 15.10. Satellite Image Classification

Classification assigns pixels or objects to land-cover or other thematic classes.

Main approaches include supervised classification, in which an algorithm is trained using labelled examples; unsupervised classification, in which the algorithm groups pixels by spectral similarity; object-based analysis, which classifies segments or objects rather than individual pixels; and machine learning, using algorithms such as Random Forest, Support Vector Machine and neural networks.

Typical land-cover classes include forest, shrubland, cropland, pasture, built-up areas, water, snow and ice, and bare soil. The class scheme should match the purpose and scale of the project.

**Training and validation data.** Training samples are used to fit the model; independent validation data are used to assess classification quality. If the same sites are used for both training and validation, accuracy may be overstated.

A **confusion matrix** shows agreement and disagreement between the classification and reference data. Overall accuracy does not reveal all errors: producer's and user's accuracy by class should be examined, taking class imbalance and sampling design into account.

### 15.11. Radar Remote Sensing and SAR

Synthetic Aperture Radar (SAR) uses microwave pulses and records backscatter from the surface. Radar data are especially useful where optical observations are limited by cloud cover or lack of sunlight.

The SAR signal depends on surface roughness relative to wavelength; soil and vegetation moisture; object geometry and viewing angle; forest structure; signal polarisation; wavelength; and sensor parameters.

Applications include flood mapping; surface-deformation monitoring using interferometry; soil-moisture and condition assessment under suitable conditions; forest and agricultural monitoring; glacier and sea-ice observation; and infrastructure-change detection.

A radar image is not an ordinary photograph. Pixel brightness reflects backscatter and viewing geometry, so interpretation requires specialist knowledge.

### 15.12. LiDAR and Three-dimensional Remote Sensing

LiDAR (Light Detection and Ranging) measures distance from the travel time of a laser pulse. Systems may be carried by aircraft, UAVs, vehicles or satellites.

The output is often represented as a point cloud, in which each point has coordinates and additional attributes. Point clouds can be used to create a Digital Surface Model (DSM), a Digital Terrain Model (DTM), building and vegetation models, profiles and three-dimensional representations.

Laser pulses may pass through gaps in vegetation and return from different canopy levels and the ground surface. Point density, sensor characteristics and classification algorithms determine the quality of the result.

### 15.13. Change Detection and Time Series

Change detection compares data from different dates to identify surface transformations and natural processes.

Methods include comparison of classified maps; subtraction and normalisation of spectral bands; analysis of index changes; pixel time profiles; object-based analysis; and statistical methods for identifying trends and seasonality.

Before comparison, ensure comparable seasons and phenological stages; the same or harmonised coordinate reference system; comparable spatial resolutions; radiometric and atmospheric consistency; a consistent class scheme; and masking of clouds, shadows and snow where these are not the subject of the analysis.

A change in spectral signal does not always mean a change in land cover. It may result from moisture, season, viewing angle, atmosphere or sensor differences.

### 15.14. Remote Sensing for Natural Hazards and Disasters

Remote-sensing data support work before, during and after emergencies. They can be used to map flooded areas; identify traces of forest and grassland fires; assess landslide and earthquake impacts; observe glacier movement and changes in glacial lakes; track dust storms and volcanic emissions; and assess damage to agriculture and infrastructure.

Operational response depends on data delivery speed, image availability, cloud cover, resolution and classification reliability. A satellite map must state the acquisition time: an image collected after a flood wave has passed may not show the maximum flooded area.

Remote sensing should be combined with ground observations, meteorological data, reports from emergency services and verified information about population and infrastructure.

### 15.15. Limitations, Uncertainty and Ethics of Remote Sensing

Remote-sensing data have limitations, including cloud, smoke, fog and atmospheric interference; differences between sensors and algorithms; mixed pixels at feature boundaries; seasonal and angular effects; insufficient ground reference data; classification and model uncertainty; publication delays; and access restrictions.

Ethical issues include surveillance of private property, protection of personal data, security of sensitive sites, rights of Indigenous peoples and local communities, and the risk of misuse of maps and analytics.

Commercial availability of an image does not remove legal, licensing or responsible-use requirements. Before publishing sensitive coordinates, assess possible harm.

## 15.16. Итоги главы / Chapter Summary

1. ДЗЗ позволяет получать информацию о поверхности и атмосфере без непосредственного контакта с объектом.
2. Сигналы зависят от спектральных свойств поверхности, атмосферы и геометрии наблюдения.
3. Пассивные и активные сенсоры используют разные физические принципы.
4. Пространственное, спектральное, временное и радиометрическое разрешение описывают разные свойства данных.
5. Перед анализом необходимо учитывать калибровку, атмосферу, геометрию, рельеф и качество исходного продукта.
6. Спектральные индексы помогают выделять особенности поверхности, но не заменяют полноценную классификацию и проверку.
7. Качество классификации оценивается по независимым эталонным данным и матрице ошибок.
8. SAR и LiDAR расширяют возможности наблюдений за счёт радарных и лазерных методов.
9. Мониторинг изменений требует сопоставимости снимков и учёта сезонности.
10. ДЗЗ эффективно при сочетании со спутниковыми, полевыми и статистическими данными.

## 15.17. Ключевые понятия / Key Terms

Дистанционное зондирование Земли — Remote sensing of the Earth; электромагнитный спектр — Electromagnetic spectrum; спектральная сигнатура — Spectral signature; пассивный сенсор — Passive sensor; активный сенсор — Active sensor; мультиспектральная съёмка — Multispectral imaging; гиперспектральная съёмка — Hyperspectral imaging; пространственное разрешение — Spatial resolution; временное разрешение — Temporal resolution; радиометрическое разрешение — Radiometric resolution; NDVI — Normalized Difference Vegetation Index; SAR — Synthetic Aperture Radar; LiDAR — Light Detection and Ranging; облако точек — Point cloud; классификация — Classification; матрица ошибок — Confusion matrix; мониторинг изменений — Change detection; цифровая модель рельефа — Digital Terrain Model; поверхностное отражение — Surface reflectance.

## 15.18. Контрольные вопросы и практические задания / Review Questions and Practical Activities

### Вопросы для самопроверки / Review Questions

1. Что такое дистанционное зондирование и чем оно дополняет полевые наблюдения?
2. Чем отражённое солнечное излучение отличается от собственного теплового излучения поверхности?
3. Почему растительность обычно имеет высокий отклик в ближнем инфракрасном диапазоне?
4. В чём разница между пассивным и активным сенсором?
5. Чем отличаются четыре вида разрешения?
6. Почему облачность ограничивает оптические наблюдения, но не всегда препятствует радарной съёмке?
7. Для чего выполняется атмосферная коррекция?
8. Что показывает NDVI и какие у него ограничения?
9. Почему NDWI необходимо сопровождать формулой?
10. Как устроена контролируемая классификация и зачем нужны независимые проверочные данные?
11. Какие сведения можно получить с помощью SAR и LiDAR?
12. Почему сезонность важна при сравнении снимков разных дат?
13. Какие факторы могут привести к ложному обнаружению изменений?
14. Какие этические ограничения следует учитывать при использовании детальных снимков?

### Разобранный пример. Расчёт NDVI / Worked example: Calculating NDVI

Рассмотрим условный пиксель спутникового снимка. После необходимой калибровки и атмосферной коррекции отражение в красном канале (Red) равно 0,10, а в ближнем инфракрасном канале (NIR) — 0,50. Эти числа условны и приведены только для обучения.

Формула нормализованного разностного вегетационного индекса:

\[
NDVI = \frac{NIR-Red}{NIR+Red}
\]

**Шаг 1. Подставим значения:**

\[
NDVI = \frac{0{,}50-0{,}10}{0{,}50+0{,}10}
= \frac{0{,}40}{0{,}60}
\]

**Шаг 2. Выполним деление:**

\[
NDVI \approx 0{,}67
\]

**Как понимать результат?** Значение около 0,67 указывает на заметный контраст между низким отражением в красном канале и более высоким отражением в ближнем инфракрасном. Такое сочетание часто характерно для участков с зелёной растительностью. Однако по одному значению NDVI нельзя надёжно определить вид растений, урожайность или точное состояние экосистемы.

**Важно:** для корректного сравнения нужно использовать данные одного сенсора или согласованные продукты, проверять дату и сезон съёмки, маскировать облака и тени и учитывать фон почвы. NDVI также может насыщаться в густой растительности.

**Проверьте себя:** если Red = 0,20, а NIR = 0,40, чему будет равен NDVI? Почему он ниже, чем в первом примере?

Consider a hypothetical pixel in a satellite image. After the required calibration and atmospheric correction, reflectance in the red band is 0.10 and reflectance in the near-infrared band (NIR) is 0.50. These values are illustrative and are used for learning only.

The Normalized Difference Vegetation Index is calculated as:

\[
NDVI = \frac{NIR-Red}{NIR+Red}
\]

**Step 1. Substitute the values:**

\[
NDVI = \frac{0.50-0.10}{0.50+0.10}
= \frac{0.40}{0.60}
\]

**Step 2. Divide:**

\[
NDVI \approx 0.67
\]

**How should the result be interpreted?** A value of about 0.67 indicates a clear contrast between low reflectance in the red band and higher reflectance in the near-infrared band. This combination is often characteristic of areas with green vegetation. However, a single NDVI value cannot reliably identify plant species, crop yield or the exact condition of an ecosystem.

**Important:** for valid comparisons, use data from the same sensor or harmonised products, check the acquisition date and season, mask clouds and shadows, and consider the soil background. NDVI can also become saturated in dense vegetation.

**Check your understanding:** If Red = 0.20 and NIR = 0.40, what is the NDVI? Why is it lower than in the first example?

### Практическая работа 1. Спектральная сигнатура / Practical Activity 1. Spectral Signature

Сравните спектральные кривые растительности, воды, сухой и влажной почвы. Объясните различия по диапазонам и укажите, почему кривые зависят от условий наблюдения.

### Практическая работа 2. Расчёт NDVI / Practical Activity 2. Calculating NDVI

Используйте мультиспектральный снимок с каналами Red и NIR. Рассчитайте NDVI, постройте карту и сравните несколько типов поверхности. Укажите сенсор, дату, формулу и ограничения.

### Практическая работа 3. Классификация земного покрова / Practical Activity 3. Land-cover Classification

Создайте схему классов и обучающие образцы для леса, воды, застройки, сельскохозяйственных угодий и открытой почвы. Проведите классификацию и оцените её по независимым проверочным точкам.

### Практическая работа 4. Оптический и радарный снимки / Practical Activity 4. Optical and Radar Comparison

Сопоставьте оптический снимок и изображение Sentinel-1 SAR одной территории. Выделите возможности и ограничения каждого источника, не интерпретируя яркость SAR как обычный цвет поверхности.

### Практическая работа 5. Мониторинг изменений / Practical Activity 5. Change Monitoring

Выберите два сопоставимых снимка разных дат. Проведите маскирование облаков, выровняйте данные и определите участки изменений. Проверьте несколько участков по независимым источникам.

### Практическая работа 6. Мини-проект по природной опасности / Practical Activity 6. Natural Hazard Mini-project

Используйте спутниковые данные для картирования одного события — например, паводка или пожара. Укажите дату съёмки, метод, ограничения и способы проверки результата.

## Технические задания для будущих иллюстраций / Visual Briefs

**Иллюстрация 15.1 / Figure 15.1 — Принцип дистанционного зондирования / Remote sensing principle.**  
Схема спутника, атмосферы, поверхности, отражённого и собственного излучения, приёмника и наземной обработки. Не путать направление падающего и отражённого сигнала.

**Иллюстрация 15.2 / Figure 15.2 — Электромагнитный спектр для ДЗЗ / Electromagnetic spectrum for remote sensing.**  
Показать видимый, NIR, SWIR, тепловой инфракрасный и микроволновый диапазоны; границы подписать как приблизительные и согласовать с используемой шкалой.

**Иллюстрация 15.3 / Figure 15.3 — Спектральные сигнатуры поверхностей / Spectral signatures of surfaces.**  
Схематические кривые растительности, воды, сухой и влажной почвы с корректным поведением в видимом и инфракрасном диапазонах; обозначить как иллюстративные, а не измеренные данные.

**Иллюстрация 15.4 / Figure 15.4 — Четыре вида разрешения / Four types of resolution.**  
Четыре панели: размер пикселя, ширина спектрального канала, частота повторного наблюдения и число уровней сигнала.

**Иллюстрация 15.5 / Figure 15.5 — Естественная и ложная цветовые композиции / True-colour and false-colour composites.**  
Одна территория в двух композициях; легенда должна объяснять назначение каналов экранным цветам.

**Иллюстрация 15.6 / Figure 15.6 — Спектральные индексы / Spectral indices.**  
Формулы NDVI, NDWI, NDMI, NDBI и NBR с обозначением каналов; особо отметить, что названия водных индексов в литературе неоднозначны.

**Иллюстрация 15.7 / Figure 15.7 — Классификация земного покрова / Land-cover classification.**  
Исходный снимок, обучающие образцы, карта классов и матрица ошибок; все данные условные и должны быть подписаны как учебный пример.

**Иллюстрация 15.8 / Figure 15.8 — Принцип SAR / SAR principle.**  
Схема бокового обзора радара, импульса, обратного рассеяния и геометрии наблюдения; не изображать SAR как обычную фотокамеру.

**Иллюстрация 15.9 / Figure 15.9 — LiDAR и облако точек / LiDAR and point cloud.**  
Показать импульсы, отражения от верхней части растительности и поверхности земли, а также построение DSM и DTM.

**Иллюстрация 15.10 / Figure 15.10 — Мониторинг изменений / Change detection.**  
Сопоставимые изображения двух дат, карта изменений и этап независимой проверки; отметить влияние сезонности и облачности.

## Научные редакционные примечания / Scientific Editorial Notes

- Точные характеристики каналов, разрешение, полосу захвата и период повторного наблюдения приводить только по документации конкретного сенсора и версии продукта.
- Различать цифровые значения, радианс, отражение на верхней границе атмосферы и поверхностное отражение.
- Не считать размер пикселя гарантией позиционной или тематической точности.
- Для индексов приводить формулу и названия каналов; учитывать различия в определениях NDWI.
- Не трактовать NDVI как прямое измерение биомассы, урожайности или здоровья отдельного вида растений.
- При оценке классификации использовать независимую выборку и документировать схему выборки.
- Для SAR указывать поляризацию, режим, направление обзора и уровень обработки; учитывать геометрические эффекты и спекл.
- Для сравнения временных рядов контролировать сезонность, атмосферу, геометрию и различия сенсоров.
- Не делать вывод о причине изменения только по спектральному различию без дополнительной проверки.
- Для БПЛА учитывать авиационные правила, безопасность полётов, приватность и разрешения на съёмку.

## Основные источники и рекомендуемая литература / Core Sources and Further Reading

1. NASA. **Earthdata** — доступ к спутниковым данным, документации и учебным материалам.
2. United States Geological Survey (USGS). **Landsat Missions and Landsat Collection Documentation** — характеристики и обработка данных Landsat.
3. European Space Agency (ESA). **Sentinel Online and Copernicus Data Space Ecosystem** — документация миссий Sentinel и доступ к данным.
4. Copernicus Programme. **Sentinel-1, Sentinel-2 and Sentinel-3 User Guides** — спецификации сенсоров и продуктов.
5. NASA Earth Observatory. **Remote Sensing** — образовательные материалы по наблюдению Земли.
6. Jensen, J. R. **Remote Sensing of the Environment: An Earth Resource Perspective**. Pearson.
7. Lillesand, T., Kiefer, R. W., Chipman, J. **Remote Sensing and Image Interpretation**. Wiley.
8. Richards, J. A. **Remote Sensing Digital Image Analysis**. Springer.
9. European Space Agency. **Radar and SAR Principles** — основы радиолокационного наблюдения.
10. International Society for Photogrammetry and Remote Sensing (ISPRS). **ISPRS Journal of Photogrammetry and Remote Sensing** — научные исследования методов фотограмметрии и ДЗЗ.

---
**Конец главы 15 / End of Chapter 15**
