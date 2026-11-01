# Глава 14. Геоинформационные системы
# Chapter 14. Geographic Information Systems

> **Часть III. Современная география и технологии / Part III. Modern Geography and Technology**  
> Научно-образовательный атлас географии / Scientific and Educational Geography Atlas

## Цели главы / Chapter objectives

Геоинформационные системы (ГИС, GIS) — совокупность методов, программных средств, данных и организационных процедур для сбора, хранения, управления, анализа и представления информации, связанной с географическим положением объектов и явлений. ГИС позволяют объединять карты, спутниковые снимки, статистику, полевые наблюдения и модели в единой пространственной среде.

Глава рассматривает основы пространственных данных, координатные системы, модели представления географической информации, анализ, картографическую визуализацию, управление качеством, веб-ГИС, этику и практические рабочие процессы.

Geographic Information Systems (GIS) combine methods, software, data and organisational procedures for collecting, storing, managing, analysing and presenting information linked to the geographic location of features and phenomena. GIS integrates maps, satellite imagery, statistics, field observations and models in a common spatial environment.

This chapter introduces spatial data, coordinate reference systems, geographic data models, spatial analysis, cartographic visualisation, data quality, web GIS, ethics and practical workflows.

## 14.1. Понятие ГИС и её компоненты / The Concept of GIS and Its Components

ГИС — не просто электронная карта. Это информационная система, в которой географическое положение связано с описательными характеристиками, а данные могут анализироваться с учётом пространственных отношений.

Основные компоненты ГИС:
1. **Данные:** координаты, геометрия, атрибуты, изображения, таблицы и метаданные.
2. **Программное обеспечение:** инструменты ввода, редактирования, анализа, хранения и визуализации.
3. **Аппаратная инфраструктура:** компьютеры, серверы, GNSS-приёмники, мобильные устройства, датчики и сетевые ресурсы.
4. **Методы и процедуры:** стандарты, модели данных, правила обработки и проверки качества.
5. **Люди и организации:** специалисты, пользователи, владельцы данных и органы управления.

ГИС применяется в кадастре, городском планировании, природоохранной деятельности, транспорте, сельском хозяйстве, управлении водными ресурсами, чрезвычайных ситуациях, здравоохранении и бизнесе.

## 14.2. Пространственные объекты и атрибутивные данные / Spatial Features and Attribute Data

Географический объект обычно описывается геометрией и набором атрибутов.

Основные геометрические типы:
- **точка (point):** источник воды, метеостанция, дерево, остановка;
- **линия (line):** река, дорога, трубопровод, граница маршрута;
- **полигон (polygon):** озеро, административный район, лесной массив, земельный участок;
- **поверхность или объём:** рельеф, температурное поле, подземное геологическое тело.

Атрибутивная таблица содержит характеристики объектов: название, категория, дата наблюдения, площадь, длина, численность населения, состояние или другие параметры. Каждая запись должна быть связана с геометрическим объектом через устойчивый идентификатор.

Важно различать объект реального мира и его цифровую модель. Реальная река имеет ширину, глубину и изменяющееся русло, тогда как её представление на мелкомасштабной карте может быть одной линией.

## 14.3. Векторная и растровая модели / Vector and Raster Data Models

> **[МЕТКА ИЛЛЮСТРАЦИИ 14-A / IMAGE PLACEHOLDER 14-A]** Сравнительная схема векторных точек, линий и полигонов и растровой сетки с примерами задач.

### Векторная модель / Vector model

Векторные данные описывают объекты точками, линиями и полигонами. Они удобны для представления дорог, границ, зданий, участков и сетей.

Преимущества:
- точное описание геометрии отдельных объектов;
- удобная связь с атрибутивными таблицами;
- эффективное представление дискретных объектов;
- поддержка топологических и сетевых операций.

Ограничения:
- сложные поверхности и непрерывные поля могут требовать большого числа объектов;
- качество зависит от масштаба и точности исходной геометрии;
- ошибки топологии могут приводить к разрывам, наложениям и неверным связям.

### Растровая модель / Raster model

Растр представляет пространство сеткой ячеек (пикселей). Каждая ячейка содержит значение: высоту, температуру, отражательную способность, класс земного покрова или вероятность явления.

Преимущества:
- естественное представление непрерывных полей;
- удобство математических операций с ячейками;
- широкое применение в дистанционном зондировании и моделировании.

Ограничения:
- разрешение влияет на детализацию;
- объём данных может быть большим;
- границы объектов представлены ступенчато;
- значения ячеек зависят от способа измерения и агрегирования.

**Разрешение растра** — размер ячейки на местности или пространственный масштаб пикселя. Более мелкая ячейка не гарантирует более высокую фактическую точность: важны качество сенсора, метод обработки и исходные данные.

## 14.4. Координаты и системы координат / Coordinates and Coordinate Reference Systems

> **[МЕТКА ИЛЛЮСТРАЦИИ 14-B / IMAGE PLACEHOLDER 14-B]** Схема географических координат, эллипсоида, геоида и проекции; указать, что градусы не подходят для прямого измерения локальных расстояний.

Координатная система позволяет определить положение объекта на Земле или на плоскости. Географические координаты обычно задаются широтой и долготой, а проецированные координаты — линейными величинами, например метрами.

**Система координат (CRS)** определяет, как координаты связаны с Землёй, включая геодезическую основу, параметры координат и, для проецированных систем, картографическую проекцию.

Основные понятия:
- геодезическая система отсчёта (datum);
- эллипсоид и геоид;
- географическая широта и долгота;
- картографическая проекция;
- единицы координат;
- эпоха координат для динамических систем, если она имеет значение.

Широко используемая глобальная геодезическая основа — WGS 84. Для многих глобальных навигационных и картографических задач применяются географические координаты WGS 84, но не все наборы данных используют одну и ту же систему.

**EPSG-коды** — идентификаторы объектов геодезических и координатных систем в реестре EPSG. Указание только числа EPSG без проверки его смысла и области применения может привести к ошибке.

### Географическая и проецированная система / Geographic and projected CRS

Широта и долгота задают положение на поверхности референц-эллипсоида и обычно выражаются в угловых единицах. Для расчёта площадей, расстояний и буферов часто нужна подходящая проецированная система, параметры которой минимизируют искажения в рассматриваемом районе.

Нельзя бездумно измерять расстояния в градусах: один градус долготы соответствует разной линейной длине на разных широтах. Перед пространственными измерениями следует проверить CRS и единицы.

## 14.5. Картографические проекции в ГИС / Map Projections in GIS

Картографическая проекция преобразует координаты поверхности Земли в плоскую систему. Любая проекция искажает некоторые свойства — площадь, форму, расстояние или направление.

Выбор проекции зависит от задачи:
- для региональных карт — проекция, подходящая по положению и форме территории;
- для сравнения площадей — равновеликая проекция;
- для навигационных и угловых задач — соответствующая конформная или специализированная проекция;
- для локальных инженерных работ — официальная национальная или местная система координат.

В ГИС слои могут отображаться совместно благодаря перепроецированию «на лету», однако это не устраняет ошибок исходных координат. При экспорте и анализе необходимо проверять, в какой CRS реально сохранены данные.


### 14.5.1. Практический пример: почему перед буферным анализом проверяют CRS / Worked Example: Why CRS Must Be Checked Before Buffer Analysis

Предположим, координаты объекта записаны как широта 42° и долгота 74°. Это угловые координаты в географической системе, а не расстояния в метрах. Если программное обеспечение построит буфер радиусом «500» непосредственно в такой системе, значение может быть интерпретировано как градусы, а не как 500 м, что даст бессмысленный результат для задачи локальной доступности.

Правильный рабочий порядок:

1. Проверить метаданные исходного слоя и подтвердить его систему координат, включая порядок осей.
2. Выбрать подходящую местную или региональную проецированную CRS, единицы которой — метры и искажения которой приемлемы для исследуемой территории.
3. Создать перепроецированную копию данных, не подменяя сведения об исходной CRS простым изменением подписи.
4. Построить буфер радиусом 500 м и проверить результат на карте и по контрольным расстояниям.
5. Сохранить в проекте информацию об исходной и целевой CRS и параметрах операции.

Числа 42° и 74° здесь условны и не обозначают точный адрес. Важно не запоминать одну CRS для всех задач, а проверять область применения, единицы, точность и требования анализа.

Assume a feature is stored at latitude 42° and longitude 74°. These are angular coordinates in a geographic coordinate reference system, not distances in metres. If software creates a buffer with a radius of “500” directly in that system, the value may be interpreted as degrees rather than 500 m, producing a meaningless result for a local accessibility study.

A sound workflow is:

1. Inspect the source layer metadata and confirm its coordinate reference system, including axis order.
2. Choose an appropriate local or regional projected CRS whose units are metres and whose distortion is acceptable for the study area.
3. Create a reprojected copy of the data; do not replace the source CRS definition merely by changing its label.
4. Create the 500 m buffer and check it on the map and against known distances.
5. Record both the source and target CRS and the operation parameters in the project metadata.

The coordinates 42° and 74° are illustrative and do not identify an exact address. The important lesson is not to memorise one CRS for every task, but to check its area of use, units, accuracy and suitability for the analysis.

## 14.6. Сбор пространственных данных / Spatial Data Acquisition

Источники пространственных данных:
- геодезическая съёмка и GNSS;
- топографические и тематические карты;
- спутниковые и аэрофотоснимки;
- беспилотные летательные аппараты;
- лазерное сканирование и LiDAR;
- государственная статистика и кадастры;
- датчики и системы мониторинга;
- полевые обследования и краудсорсинг.

При сборе данных следует фиксировать дату, метод, оборудование, координатную систему, масштаб или разрешение, точность и ограничения. Данные, собранные разными методами и в разные сезоны, могут быть несопоставимы без предварительной обработки.

GNSS — общее название спутниковых навигационных систем. GPS — одна из таких систем; существуют также Galileo, GLONASS, BeiDou и другие. Точность позиционирования зависит от приёмника, условий приёма, геометрии спутников, коррекций и метода измерения.

## 14.7. Геокодирование и адресные данные / Geocoding and Address Data

**Геокодирование** преобразует текстовое описание местоположения, например адрес или название объекта, в координаты. Обратное геокодирование связывает координаты с ближайшим адресом или географическим описанием.

Результат геокодирования может быть неоднозначным. Один адрес может соответствовать зданию, входу, центроиду участка или приблизительной точке улицы. Поэтому необходимо проверять:
- точность и тип возвращённого местоположения;
- совпадение населённого пункта и административной единицы;
- качество и полноту адресной базы;
- дату обновления данных;
- правила обработки персональных данных.

Для анализа доступности услуг точка геокодированного адреса не всегда равна фактическому входу или маршруту движения.

## 14.8. Пространственные запросы и операции / Spatial Queries and Operations

> **[МЕТКА ИЛЛЮСТРАЦИИ 14-C / IMAGE PLACEHOLDER 14-C]** Наглядные схемы буфера, пересечения, объединения, разности и пространственного соединения.

Пространственный анализ отвечает на вопросы о взаимном расположении объектов, расстояниях, пересечениях, соседстве и распределении явлений.

Основные операции:
- **буферизация (buffer):** создание зоны заданного расстояния вокруг объекта;
- **пересечение (intersection):** выделение общей части пространственных объектов;
- **объединение (union):** формирование совокупной геометрии и атрибутов;
- **разность (difference):** выделение части одного объекта за пределами другого;
- **пространственное соединение (spatial join):** перенос атрибутов на основе пространственного отношения;
- **выбор по расположению (select by location):** отбор объектов, удовлетворяющих пространственному условию;
- **наложение слоёв (overlay):** совместный анализ нескольких тематических слоёв.

Пример: для оценки доступности медицинских учреждений можно построить зоны расстояния или времени поездки, сопоставить их с населением и определить территории с ограниченным доступом. Простая круговая зона не учитывает дорожную сеть, рельеф, реку или фактические барьеры.

## 14.9. Сетевой анализ и транспорт / Network Analysis and Transport

Сетевой анализ изучает движение по связанным линиям и узлам: дорогам, улицам, железным дорогам, трубопроводам и другим сетям.

Основные задачи:
- поиск кратчайшего или быстрейшего маршрута;
- анализ доступности и времени поездки;
- определение зон обслуживания;
- размещение объектов с учётом спроса;
- моделирование потоков и узких мест;
- анализ связности и устойчивости сети.

«Кратчайший» маршрут не всегда является «быстрейшим»: стоимость перемещения может учитывать скорость, ограничения поворотов, пробки, уклоны, качество покрытия, сезонность и другие факторы.

Результаты сетевого анализа зависят от полноты сети, направления движения, правил связности и актуальности атрибутов. Отсутствие дороги в базе не обязательно означает отсутствие реального пути.

## 14.10. Анализ растров и пространственное моделирование / Raster Analysis and Spatial Modelling

Растровый анализ применяется к непрерывным полям и пространственным моделям.

Распространённые методы:
- классификация и переклассификация;
- арифметические и логические операции с растрами;
- анализ плотности;
- интерполяция измерений;
- анализ уклонов, экспозиции и кривизны рельефа по цифровой модели высот;
- гидрологическое моделирование стока;
- оценка пригодности территории;
- выявление изменений во временных рядах.

Интерполяция оценивает значения между точками наблюдений. Её результат зависит от пространственного распределения измерений, выбранного метода, структуры данных и предположений модели. Интерполированная поверхность не является прямым измерением в каждой ячейке.

При анализе цифровых моделей рельефа следует учитывать разрешение, вертикальную точность, артефакты, заполнение ложных впадин и особенности алгоритма. Производные показатели, например уклон, могут усиливать ошибки исходной модели.

## 14.11. Топология и качество пространственных данных / Topology and Spatial Data Quality

Топология описывает пространственные отношения между объектами: смежность, связность, вложенность и пересечение.

Примеры топологических правил:
- полигоны административных единиц не должны иметь непредусмотренных зазоров или наложений;
- линии дорожной сети должны соединяться в узлах там, где допускается движение;
- здания не должны пересекать границы участков, если это запрещено моделью данных;
- водотоки должны сохранять логическую связность в пределах принятой схемы.

Качество пространственных данных включает:
- позиционную точность;
- тематическую точность;
- полноту;
- логическую согласованность;
- временную актуальность;
- происхождение и прослеживаемость;
- пригодность для конкретной задачи.

**Точность** и **разрешение** — разные характеристики. Набор данных может иметь высокое пространственное разрешение, но низкую позиционную точность или устаревшие атрибуты.

## 14.12. Метаданные, стандарты и совместимость / Metadata, Standards and Interoperability

Метаданные описывают содержание, происхождение, качество, структуру, пространственный охват, временной период, лицензию и условия использования данных.

Без метаданных пользователь может не знать, когда и каким методом получен слой, в какой системе координат он хранится и для каких задач пригоден.

Международные стандарты и спецификации поддерживают совместимость:
- стандарты ISO серии 19100 по географической информации;
- спецификации Open Geospatial Consortium (OGC);
- форматы GeoPackage, GeoTIFF, GeoJSON и другие;
- веб-сервисы карт и объектов, включая WMS и WFS в соответствующих реализациях.

Формат файла не гарантирует качество и совместимость. При обмене данными следует проверять кодировку, CRS, типы геометрии, систему идентификаторов, ограничения атрибутов и лицензию.

## 14.13. Картографическая визуализация и дизайн / Cartographic Visualisation and Design

> **[МЕТКА ИЛЛЮСТРАЦИИ 14-D / IMAGE PLACEHOLDER 14-D]** Примеры последовательной, расходящейся и качественной цветовых шкал и корректного выбора тематического способа отображения.

Карта — средство передачи пространственной информации, а не просто изображение данных. Её оформление должно соответствовать цели, аудитории и масштабу.

Ключевые элементы:
- заголовок и назначение;
- легенда и единицы измерения;
- масштабная линейка, если она уместна;
- указание источника и даты;
- координатная сетка или ориентиры при необходимости;
- понятная иерархия подписей;
- цветовая шкала, соответствующая типу данных;
- пояснение ограничений.

Выбор способа изображения зависит от данных:
- качественные категории — различимые оттенки или символы;
- количественные значения по территориям — последовательная цветовая шкала;
- отклонения относительно нуля — расходящаяся шкала;
- потоки — линии или стрелки с ясной семантикой;
- плотность — карты плотности или агрегированные поверхности с пояснением метода.

Хороплетная карта должна использовать нормированные показатели, например долю или плотность, а не абсолютные величины, если площади территорий и численность населения существенно различаются. Для абсолютных значений могут лучше подходить пропорциональные символы.

Следует избегать ложной точности, чрезмерного числа классов, визуально вводящих в заблуждение цветовых шкал и обрезания важных географических контекстов.

## 14.14. Веб-ГИС, облачные платформы и открытые данные / Web GIS, Cloud Platforms and Open Data

Веб-ГИС предоставляет пространственные данные и инструменты через браузер или сетевые приложения. Пользователь может просматривать слои, выполнять запросы, создавать карты и совместно работать с данными.

Типичная архитектура включает:
1. источники пространственных данных;
2. сервер или облачное хранилище;
3. сервисы публикации и обработки;
4. веб-клиент или мобильное приложение;
5. механизмы аутентификации, доступа и резервного копирования.

Открытые геоданные облегчают исследования и повторное использование информации, но условия лицензирования различаются. Открытость не означает отсутствие требований к атрибуции, ограничениям коммерческого использования или защите чувствительных данных.

Краудсорсинговые карты могут быстро обновляться, но качество отдельных объектов требует проверки. Для критической инфраструктуры и безопасности нельзя полагаться на непроверенный пользовательский ввод.

## 14.15. ГИС и управление территориями / GIS in Territorial Management

ГИС поддерживает принятие решений, когда необходимо сопоставить пространственные данные из разных отраслей.

Примеры применения:
- градостроительство: зонирование, инфраструктура, зелёные пространства;
- сельское хозяйство: мониторинг посевов, орошение, оценка земель;
- водное хозяйство: бассейновое управление, водозаборы, паводковые зоны;
- охрана природы: местообитания, экологические коридоры, мониторинг изменений;
- транспорт: доступность, маршруты, транспортная безопасность;
- чрезвычайные ситуации: оценка опасностей, эвакуация, распределение ресурсов;
- здравоохранение: пространственная доступность услуг и эпидемиологический мониторинг;
- кадастр: учёт земель и недвижимости.

ГИС помогает выявить пространственные закономерности, но не заменяет экспертную оценку, общественные консультации и правовые процедуры. Карта является моделью реальности и должна рассматриваться вместе с неопределённостью и ограничениями данных.

## 14.16. Этика, конфиденциальность и ответственное использование / Ethics, Privacy and Responsible Use

Географические данные могут раскрывать местоположение людей, жилищ, медицинских учреждений, объектов критической инфраструктуры, редких видов и культурно значимых мест.

Основные принципы ответственного использования:
- собирать только данные, необходимые для законной и понятной цели;
- учитывать согласие и правовые основания обработки персональных данных;
- минимизировать детализацию там, где она создаёт риск идентификации;
- ограничивать доступ и защищать хранилища;
- документировать источники и ограничения;
- проверять смещения и неравномерность охвата данных;
- не публиковать чувствительные координаты уязвимых видов и объектов без оценки риска.

Пространственная агрегация может снижать риск раскрытия персональных данных, но не всегда гарантирует анонимность. Сочетание нескольких наборов данных иногда позволяет повторно идентифицировать людей.

## 14.17. Практический рабочий процесс ГИС / A Practical GIS Workflow

Типовой проект можно организовать поэтапно:

1. **Постановка задачи:** сформулировать вопрос, территорию, масштаб и конечного пользователя.
2. **Поиск данных:** определить источники, лицензии, даты и ограничения.
3. **Проверка данных:** изучить CRS, геометрию, атрибуты, пропуски и дубликаты.
4. **Подготовка:** исправить ошибки, привести слои к совместимым системам координат и единицам.
5. **Анализ:** выбрать операции, соответствующие вопросу и модели данных.
6. **Проверка результатов:** провести контроль на независимых данных или полевых наблюдениях, оценить неопределённость.
7. **Визуализация:** подготовить карту, легенду, подписи и пояснения.
8. **Документирование:** сохранить метаданные, параметры обработки, версии данных и программ.
9. **Публикация:** проверить права доступа, лицензию, конфиденциальность и доступность материалов.

Воспроизводимый проект должен позволять другому специалисту понять, какие данные, параметры и операции привели к результату.

### 14.17.1. Как оценивать качество пространственных данных / Assessing Spatial Data Quality

Перед анализом в ГИС проверяют не только формат слоя, но и происхождение, точность, полноту и актуальность данных. Пять основных вопросов: кто создал данные и каким методом; насколько точно определены координаты; правильно ли классифицированы объекты; какие объекты или значения отсутствуют; когда данные собраны и подходят ли они для текущей задачи.

Дополнительно проверяют систему координат, единицы измерения, топологические ошибки, метаданные и лицензионные ограничения. Высокое пространственное разрешение не гарантирует высокой точности: детальный слой может содержать смещения или устаревшие объекты.

**Пример.** Для расчёта времени поездки к больнице дорожная сеть должна учитывать проходимость, ограничения движения, сезонные закрытия и реалистичные скорости. Если горные перевалы отмечены как доступные круглый год, расчёт доступности будет завышен.

**Задание.** Составьте карточку качества дорожного слоя: источник, дата, масштаб или разрешение, система координат, атрибуты, пробелы и допустимые способы использования.

Before GIS analysis, assess not only a layer's format but also its lineage, accuracy, completeness and currency. Ask five questions: who created the data and how; how accurate are feature coordinates; are features classified correctly; what features or values are missing; and when were the data collected?

Also check the coordinate reference system, units, topological errors, metadata and licence restrictions. High spatial resolution does not guarantee high accuracy: a detailed layer may still contain positional errors or outdated features.

**Example.** A road network used to calculate travel time to a hospital should account for passability, traffic restrictions, seasonal closures and realistic speeds. If mountain passes are shown as accessible all year, calculated accessibility will be overstated.

**Activity.** Prepare a road-layer quality record with source, date, scale or resolution, coordinate system, attributes, gaps and appropriate uses.

### 14.17.2. Как оценивать точность пространственных данных / Assessing the Accuracy of Spatial Data

Карта или ГИС-слой может выглядеть очень детально, но это не гарантирует точности. Необходимо различать пространственную точность положения объектов, тематическую точность классификации, полноту данных и их актуальность. Эти характеристики отвечают на разные вопросы и не заменяют друг друга.

**Точность положения.** Координаты точек и линий сравнивают с независимыми контрольными измерениями более высокой точности. Ошибки могут выражаться через среднеквадратическое отклонение или другие статистики, соответствующие распределению ошибок и стандарту проекта. Контрольные точки должны быть распределены по территории, а не сосредоточены в одном углу карты.

**Тематическая точность.** Для классифицированной карты (например, типов земного покрова) результаты сравнивают с независимой эталонной выборкой и составляют матрицу ошибок. Общая доля правильных классификаций может скрывать слабое качество редких классов; поэтому полезно отдельно рассматривать ошибки пропуска и ложного отнесения для каждого класса.

**Масштаб, разрешение и дата.** Крупный масштаб отображения не добавляет исходным данным точности. Разрешение растрового пикселя не равно точности положения границы объекта. Указывайте дату съёмки или обследования, масштаб исходной карты, систему координат, метод обработки и ограничения использования.

**Учебное задание.** Для слоя дорог и карты земного покрова составьте отдельные планы контроля качества. Укажите, какие независимые данные нужны, как выбрать контрольные точки или участки и почему одну общую цифру точности нельзя использовать для обоих слоёв.

A map or GIS layer may look highly detailed without being accurate. It is important to distinguish positional accuracy, thematic classification accuracy, data completeness and currency. These characteristics answer different questions and do not replace one another.

**Positional accuracy.** Compare point and line coordinates with independent reference measurements of higher accuracy. Errors may be expressed using root mean square error or other statistics appropriate to the error distribution and project standard. Checkpoints should be distributed across the study area rather than concentrated in one corner of the map.

**Thematic accuracy.** For a classified map, such as land-cover types, compare results with an independent reference sample and build an error matrix. Overall accuracy can conceal poor performance for rare classes; it is therefore useful to examine omission and commission errors for each class separately.

**Scale, resolution and date.** A large display scale does not add accuracy to the source data. Raster pixel size is not the same as the positional accuracy of an object's boundary. State the acquisition or survey date, source-map scale, coordinate reference system, processing method and limitations.

**Activity.** Prepare separate quality-control plans for a road layer and a land-cover map. Identify the independent reference data needed, how checkpoints or sample sites should be selected, and why one overall accuracy figure cannot be used for both layers.

## English-language chapter text

### 14.1. The Concept of GIS and Its Components

A Geographic Information System (GIS) is more than an electronic map. It is an information system in which geographic location is linked to descriptive characteristics and data can be analysed using spatial relationships.

The main components of GIS are:
1. **Data:** coordinates, geometry, attributes, imagery, tables and metadata.
2. **Software:** tools for data entry, editing, analysis, storage and visualisation.
3. **Hardware and infrastructure:** computers, servers, GNSS receivers, mobile devices, sensors and networks.
4. **Methods and procedures:** standards, data models, processing rules and quality checks.
5. **People and organisations:** specialists, users, data owners and decision-making bodies.

GIS is used in cadastre, urban planning, nature conservation, transport, agriculture, water management, emergency response, health care and business.

### 14.2. Spatial Features and Attribute Data

A geographic feature is usually described by its geometry and a set of attributes.

Main geometry types include:
- **point:** a water source, weather station, tree or bus stop;
- **line:** a river, road, pipeline or route;
- **polygon:** a lake, administrative district, forest or land parcel; and
- **surface or volume:** terrain, a temperature field or an underground geological body.

An attribute table contains feature characteristics such as name, category, observation date, area, length, population, condition or other parameters. Each record should be linked to its geometry through a stable identifier.

A real-world feature must be distinguished from its digital representation. A real river has width, depth and a changing channel, while a small-scale map may represent it as a single line.

### 14.3. Vector and Raster Data Models

**Vector data** represent features as points, lines and polygons. They are useful for roads, boundaries, buildings, land parcels and networks. Advantages include precise geometry for individual features, links to attribute tables, efficient representation of discrete objects, and support for topological and network operations. Limitations include the difficulty of representing complex continuous surfaces, dependence on source scale and geometry accuracy, and the possibility of topology errors.

**Raster data** represent space as a grid of cells or pixels. Each cell stores a value such as elevation, temperature, reflectance, land-cover class or event probability. Rasters are well suited to continuous fields, mathematical cell operations, remote sensing and spatial modelling. Limitations include dependence on resolution, potentially large file sizes, stair-step boundaries and sensitivity to measurement and aggregation methods.

**Raster resolution** is the ground size of a cell or pixel. A smaller cell does not automatically guarantee greater actual accuracy: sensor quality, processing and source data also matter.

### 14.4. Coordinates and Coordinate Reference Systems

A coordinate system specifies the position of a feature on Earth or on a plane. Geographic coordinates are usually latitude and longitude; projected coordinates are linear values, such as metres.

A **coordinate reference system (CRS)** defines how coordinates relate to Earth, including the geodetic reference frame, coordinate parameters and, for projected systems, the map projection.

Important concepts include geodetic datum, ellipsoid and geoid, geographic latitude and longitude, map projection, coordinate units and, where relevant, the coordinate epoch of a dynamic reference system.

WGS 84 is a widely used global geodetic reference system. Geographic coordinates based on WGS 84 are common in global navigation and mapping, but not all datasets use the same system.

**EPSG codes** identify geodetic and coordinate reference systems in the EPSG registry. Using a code without checking its meaning and area of use can lead to errors.

Latitude and longitude define a position on a reference ellipsoid and are usually expressed in angular units. Calculating areas, distances and buffers often requires an appropriate projected CRS whose distortion is acceptable for the study area. A degree of longitude has a different ground length at different latitudes, so distances should not be measured casually in geographic degrees.

### 14.5. Map Projections in GIS

A map projection transforms coordinates on Earth's curved surface into a plane. Every projection distorts some properties, such as area, shape, distance or direction.

The choice depends on the task: a regional map needs a projection appropriate to the territory's position and shape; area comparisons require an equal-area projection; navigation and angle-related tasks may require a conformal or specialised projection; and local engineering work should use an official national or local coordinate system.

GIS software may display layers together through on-the-fly reprojection, but this does not correct errors in the original coordinates. When exporting or analysing data, check the CRS in which the data are actually stored.

### 14.6. Spatial Data Acquisition

Spatial data sources include geodetic surveys and GNSS; topographic and thematic maps; satellite and aerial imagery; unmanned aerial vehicles; laser scanning and LiDAR; government statistics and cadastral systems; sensors and monitoring networks; field surveys and crowdsourcing.

When collecting data, record the date, method, equipment, coordinate system, scale or resolution, accuracy and limitations. Data collected using different methods or in different seasons may not be comparable without preprocessing.

GNSS is the general term for satellite navigation systems. GPS is one such system; others include Galileo, GLONASS and BeiDou. Positioning accuracy depends on the receiver, signal conditions, satellite geometry, correction services and measurement method.

### 14.7. Geocoding and Address Data

**Geocoding** converts a textual location description, such as an address or place name, into coordinates. **Reverse geocoding** links coordinates to a nearby address or geographic description.

Geocoding results may be ambiguous. An address may be matched to a building, entrance, parcel centroid or approximate street point. Check the accuracy and type of returned location; the settlement and administrative unit; completeness of the address database; data-update date; and rules for handling personal data.

For service-accessibility analysis, a geocoded address point is not necessarily the actual entrance or a point on the travel network.

### 14.8. Spatial Queries and Operations

Spatial analysis answers questions about the relative positions of features, distances, intersections, adjacency and spatial distribution.

Common operations include:
- **buffer:** creating a zone at a specified distance around a feature;
- **intersection:** extracting the shared part of spatial features;
- **union:** combining geometry and attributes;
- **difference:** extracting the part of one feature outside another;
- **spatial join:** transferring attributes based on a spatial relationship;
- **select by location:** selecting features that meet a spatial condition; and
- **overlay:** analysing several thematic layers together.

For example, to assess access to medical facilities, analysts can create distance or travel-time zones, compare them with population data and identify areas with limited access. A simple circular buffer does not account for roads, relief, rivers or actual barriers.

### 14.9. Network Analysis and Transport

Network analysis studies movement along connected lines and nodes, such as roads, streets, railways, pipelines and other networks.

Common tasks include finding the shortest or fastest route; analysing accessibility and travel time; defining service areas; locating facilities according to demand; modelling flows and bottlenecks; and assessing network connectivity and resilience.

The “shortest” route is not always the “fastest”. Travel cost may account for speed, turn restrictions, congestion, gradients, road surface, seasonality and other factors.

Network-analysis results depend on network completeness, direction of travel, connectivity rules and the currency of attributes. A road missing from a database does not necessarily mean that no real route exists.

### 14.10. Raster Analysis and Spatial Modelling

Raster analysis is used for continuous fields and spatial models. Common methods include classification and reclassification; raster arithmetic and logical operations; density analysis; interpolation; slope, aspect and curvature analysis from digital elevation models; hydrological flow modelling; land-suitability assessment; and change detection in time series.

Interpolation estimates values between observation points. Its result depends on the spatial distribution of measurements, the selected method, data structure and model assumptions. An interpolated surface is not a direct measurement at every cell.

When analysing digital elevation models, consider resolution, vertical accuracy, artefacts, filling of spurious depressions and algorithm characteristics. Derived indicators such as slope may amplify errors in the source model.

### 14.11. Topology and Spatial Data Quality

Topology describes spatial relationships among features, including adjacency, connectivity, containment and intersection.

Examples of topological rules include: administrative polygons should not contain unintended gaps or overlaps; road lines should connect at nodes where movement is allowed; buildings should not cross parcel boundaries if the data model prohibits it; and watercourses should maintain logical connectivity within the adopted network model.

Spatial data quality includes positional accuracy, thematic accuracy, completeness, logical consistency, temporal currency, lineage and fitness for purpose.

**Accuracy** and **resolution** are different characteristics. A dataset may have high spatial resolution but low positional accuracy or outdated attributes.

### 14.12. Metadata, Standards and Interoperability

Metadata describe the content, origin, quality, structure, spatial coverage, time period, licence and conditions of use of a dataset.

Without metadata, users may not know when and how a layer was created, which CRS it uses or which tasks it is suitable for.

International standards and specifications support interoperability. These include the ISO 19100 series on geographic information; Open Geospatial Consortium (OGC) specifications; formats such as GeoPackage, GeoTIFF and GeoJSON; and map and feature web services, including WMS and WFS in relevant implementations.

A file format does not guarantee quality or interoperability. When exchanging data, check encoding, CRS, geometry types, identifier systems, attribute constraints and licence conditions.

### 14.13. Cartographic Visualisation and Design

A map is a means of communicating spatial information, not simply a picture of data. Its design should fit the purpose, audience and scale.

Key elements include a title and purpose; legend and units; a scale bar where appropriate; source and date; coordinate grid or reference features where needed; a clear hierarchy of labels; a colour scheme suited to the data type; and an explanation of limitations.

The method of representation depends on the data:
- qualitative categories: distinct hues or symbols;
- quantitative values by area: sequential colour schemes;
- deviations around zero: diverging schemes;
- flows: lines or arrows with clear meaning; and
- density: density maps or aggregated surfaces with the method explained.

A choropleth map should use normalised indicators, such as a share or density, rather than absolute values when areas and populations differ substantially. Proportional symbols may be more appropriate for absolute totals.

Avoid false precision, too many classes, misleading colour schemes and the removal of important geographic context.

### 14.14. Web GIS, Cloud Platforms and Open Data

Web GIS provides spatial data and tools through browsers or network applications. Users can view layers, run queries, create maps and collaborate.

A typical architecture includes spatial data sources; a server or cloud store; publication and processing services; a web client or mobile application; and authentication, access-control and backup mechanisms.

Open geospatial data support research and reuse, but licences differ. “Open” does not necessarily mean that attribution is unnecessary, commercial use is unrestricted or sensitive data can be published.

Crowdsourced maps can be updated quickly, but individual features may require verification. Unverified user input should not be relied on for critical infrastructure or safety decisions.

### 14.15. GIS in Territorial Management

GIS supports decision-making when spatial data from different sectors need to be compared.

Applications include urban planning (zoning, infrastructure and green space); agriculture (crop monitoring, irrigation and land assessment); water management (basin planning, abstraction points and flood zones); conservation (habitats, ecological corridors and change monitoring); transport (accessibility, routes and safety); emergencies (hazard assessment, evacuation and resource allocation); health care (spatial access to services and epidemiological monitoring); and cadastre (land and property records).

GIS helps identify spatial patterns, but it does not replace expert judgement, public consultation or legal procedures. A map is a model of reality and must be considered together with data uncertainty and limitations.

### 14.16. Ethics, Privacy and Responsible Use

Geographic data may reveal the locations of people, homes, medical facilities, critical infrastructure, rare species and culturally significant sites.

Responsible use requires collecting only data necessary for a lawful and clearly defined purpose; considering consent and legal grounds for processing personal data; reducing detail where it creates identification risks; restricting access and securing storage; documenting sources and limitations; checking bias and uneven data coverage; and avoiding publication of sensitive coordinates of vulnerable species and sites without risk assessment.

Spatial aggregation may reduce privacy risks but does not always guarantee anonymity. Combining several datasets can sometimes make individuals identifiable again.

### 14.17. A Practical GIS Workflow

A typical project can be organised into stages:

1. **Define the task:** formulate the question, territory, scale and end user.
2. **Find data:** identify sources, licences, dates and limitations.
3. **Check data:** examine CRS, geometry, attributes, missing values and duplicates.
4. **Prepare:** correct errors and make layers compatible in coordinate systems and units.
5. **Analyse:** select operations appropriate to the question and data model.
6. **Validate results:** use independent data or field observations and assess uncertainty.
7. **Visualise:** prepare the map, legend, labels and explanations.
8. **Document:** preserve metadata, processing parameters, data versions and software versions.
9. **Publish:** check access rights, licence, privacy and accessibility.

A reproducible project should allow another specialist to understand which data, parameters and operations produced the result.

## 14.18. Итоги главы / Chapter Summary

1. ГИС объединяет пространственные данные, программные средства, методы, инфраструктуру и пользователей.
2. Географические объекты описываются геометрией и атрибутами.
3. Векторная и растровая модели предназначены для разных типов пространственной информации.
4. Координатная система и проекция должны соответствовать территории и задаче.
5. Пространственные операции выявляют отношения между объектами и слоями.
6. Сетевой и растровый анализ позволяют решать задачи доступности и моделирования.
7. Качество данных включает точность, полноту, актуальность, согласованность и происхождение.
8. Метаданные и стандарты обеспечивают интерпретируемость и совместимость.
9. Картографический дизайн влияет на корректность восприятия данных.
10. Этика и защита конфиденциальности являются обязательной частью ГИС-практики.
11. Воспроизводимый рабочий процесс должен документировать данные и методы.

## 14.19. Ключевые понятия / Key Terms

Геоинформационная система — Geographic Information System; пространственные данные — Spatial data; атрибутивные данные — Attribute data; векторная модель — Vector model; растровая модель — Raster model; координатная система — Coordinate reference system; геодезическая основа — Geodetic datum; картографическая проекция — Map projection; геокодирование — Geocoding; буферизация — Buffering; пространственное наложение — Spatial overlay; сетевой анализ — Network analysis; топология — Topology; пространственное разрешение — Spatial resolution; позиционная точность — Positional accuracy; метаданные — Metadata; интероперабельность — Interoperability; веб-ГИС — Web GIS; цифровая модель высот — Digital Elevation Model; дистанционное зондирование — Remote sensing.

## 14.20. Контрольные вопросы и практические задания / Review Questions and Practical Activities

### Вопросы для самопроверки / Review Questions

1. Чем ГИС отличается от обычной электронной карты?
2. Какие компоненты образуют ГИС?
3. В каких случаях целесообразна векторная модель, а в каких — растровая?
4. Почему размер пикселя не равен автоматически точности данных?
5. Что определяет система координат и зачем проверять CRS каждого слоя?
6. Почему расстояния нельзя бездумно измерять в географических градусах?
7. Чем геокодирование отличается от обратного геокодирования?
8. Для чего применяются буферизация, пересечение и пространственное соединение?
9. Чем кратчайший маршрут отличается от быстрейшего?
10. Что такое топология и какие ошибки она помогает обнаружить?
11. Какие характеристики входят в оценку качества пространственных данных?
12. Почему метаданные важны для воспроизводимости?
13. Как выбрать способ тематического картографирования?
14. Какие риски конфиденциальности могут возникать при публикации геоданных?

### Разобранный пример. Буферная зона вокруг объекта / Worked example: Creating a buffer around a feature

Предположим, что нужно предварительно оценить территорию в радиусе 500 м от поликлиники. Для учебного расчёта представим поликлинику точкой, а буфер — кругом.

**Шаг 1. Проверим систему координат.** Расчёт расстояния должен выполняться в подходящей проецированной системе координат с линейными единицами, например метрами. Если слой хранится в географических координатах широты и долготы, нельзя просто задать буфер «500» и считать, что это 500 м: единицы будут угловыми, а длина градуса долготы меняется с широтой.

**Шаг 2. Создадим буфер радиусом 500 м.** В ГИС выбираем операцию Buffer и задаём расстояние 500 м. Для идеального круга его площадь можно проверить по формуле (S=\pi r^2):

(S \approx 3{,}1416 \times 500^2 = 785\,400\ м^2 \approx 0{,}785\ км^2.)

**Шаг 3. Правильно истолкуем карту.** Буфер показывает геометрическую зону на расстоянии до 500 м по прямой от точки. Он не показывает реальное время ходьбы и не гарантирует доступность поликлиники: на пути могут быть река, железная дорога, закрытая территория, отсутствие перехода или крутой склон.

**Вывод:** круговой буфер подходит для первичного пространственного отбора. Для оценки фактической доступности лучше использовать сетевой анализ по пешеходным маршрутам и проверенные данные о входах, переходах и препятствиях.

**Проверьте себя:** что произойдёт с площадью идеального буфера, если радиус увеличить с 500 до 1 000 м? Во сколько раз изменится площадь и почему?

Suppose we need a preliminary estimate of the area within 500 m of a clinic. For this learning example, represent the clinic as a point and the buffer as a circle.

**Step 1. Check the coordinate reference system.** Distance calculations should use a suitable projected coordinate system with linear units, such as metres. If the layer uses geographic latitude and longitude, do not enter “500” and assume it means 500 m: the units are angular, and the ground length of a degree of longitude varies with latitude.

**Step 2. Create a 500 m buffer.** In GIS, choose the Buffer operation and set the distance to 500 m. The area of an ideal circle can be checked using (A=\pi r^2):

(A \approx 3.1416 \times 500^2 = 785,400\ m^2 \approx 0.785\ km^2.)

**Step 3. Interpret the map correctly.** The buffer represents a geometric zone within 500 m in a straight line from the point. It does not show actual walking time or guarantee access to the clinic: a river, railway, restricted area, missing crossing or steep slope may lie along the route.

**Conclusion:** A circular buffer is useful for an initial spatial selection. To estimate actual accessibility, use network analysis based on pedestrian routes and verified data about entrances, crossings and barriers.

**Check your understanding:** What happens to the area of an ideal buffer if its radius increases from 500 m to 1,000 m? By what factor does the area change, and why?

### Практическая работа 1. Создание тематической карты / Practical Activity 1. Creating a Thematic Map

Загрузите открытые данные о населении и административных границах. Проверьте CRS, соедините таблицу с геометрией по идентификатору и создайте хороплетную карту нормированного показателя. Укажите год, источник и ограничения.

### Практическая работа 2. Вектор и растр / Practical Activity 2. Vector and Raster

Создайте или загрузите векторный слой водоёмов и растровую модель высот. Сравните способы представления объектов и непрерывных поверхностей. Объясните влияние разрешения на результат.

### Практическая работа 3. Доступность услуг / Practical Activity 3. Service Accessibility

Выберите населённые пункты и объекты социальной инфраструктуры. Сначала рассчитайте простые зоны расстояния, затем — зоны по дорожной сети, если доступна качественная сеть. Сравните различия и объясните их причины.

### Практическая работа 4. Анализ рельефа / Practical Activity 4. Terrain Analysis

По цифровой модели высот постройте карту уклонов и экспозиций склонов. Проверьте разрешение и вертикальную точность исходного растра. Опишите возможное применение и ограничения.

### Практическая работа 5. Контроль качества данных / Practical Activity 5. Data Quality Control

Проверьте набор административных полигонов на зазоры, наложения, самопересечения и пропущенные атрибуты. Подготовьте таблицу обнаруженных ошибок, способов исправления и оставшейся неопределённости.

### Практическая работа 6. Воспроизводимый ГИС-проект / Practical Activity 6. Reproducible GIS Project

Подготовьте небольшой проект с исходными данными, описанием CRS, шагами обработки, итоговой картой, метаданными и перечнем ограничений. Другой участник должен иметь возможность повторить основные операции.

### English Summary

1. GIS combines spatial data, software, methods, infrastructure and users.
2. Geographic features are described by geometry and attributes.
3. Vector and raster models are suited to different types of spatial information.
4. Coordinate systems and projections must match the territory and analytical task.
5. Spatial operations identify relationships between features and layers.
6. Network and raster analysis support accessibility studies and spatial modelling.
7. Data quality includes accuracy, completeness, currency, consistency and lineage.
8. Metadata and standards support interpretation and interoperability.
9. Cartographic design influences how data are understood.
10. Ethics and privacy protection are essential parts of GIS practice.
11. A reproducible workflow documents data and methods.

### English Review Questions

1. How does GIS differ from an ordinary electronic map?
2. Which components make up a GIS?
3. When is a vector model more appropriate, and when is a raster model?
4. Why is pixel size not automatically the same as data accuracy?
5. What does a coordinate reference system define, and why should the CRS of every layer be checked?
6. Why should distances not be measured casually in geographic degrees?
7. How does geocoding differ from reverse geocoding?
8. What are buffers, intersections and spatial joins used for?
9. How does the shortest route differ from the fastest route?
10. What is topology, and which errors can it help identify?
11. Which characteristics are included in spatial data quality?
12. Why are metadata important for reproducibility?
13. How should a thematic mapping method be selected?
14. Which privacy risks may arise when geographic data are published?

### English Practical Activities

**1. Creating a thematic map.** Download open population data and administrative boundaries. Check the CRS, join the table to the geometry using an identifier and create a choropleth of a normalised indicator. State the year, source and limitations.

**2. Vector and raster.** Create or download a vector layer of water bodies and a raster elevation model. Compare how discrete features and continuous surfaces are represented. Explain how resolution affects the result.

**3. Service accessibility.** Select settlements and social-service facilities. First calculate simple distance zones, then network-based zones if a reliable road network is available. Compare the results and explain the differences.

**4. Terrain analysis.** Use a digital elevation model to create slope and aspect maps. Check the source raster's resolution and vertical accuracy. Describe possible applications and limitations.

**5. Data quality control.** Check an administrative polygon dataset for gaps, overlaps, self-intersections and missing attributes. Prepare a table of errors found, correction methods and remaining uncertainty.

**6. Reproducible GIS project.** Prepare a small project containing source data, CRS information, processing steps, a final map, metadata and a list of limitations. Another participant should be able to repeat the main operations.

## Технические задания для будущих иллюстраций / Visual Briefs

**Иллюстрация 14.1 / Figure 14.1 — Архитектура ГИС / GIS architecture.**  
Схема компонентов: данные, программное обеспечение, оборудование, методы, люди и результаты. Показать цикл от сбора данных до анализа и принятия решений.

**Иллюстрация 14.2 / Figure 14.2 — Векторная и растровая модели / Vector and raster models.**  
Один участок местности показать как точки, линии и полигоны, а рядом — как сетку пикселей. Объяснить различие дискретных объектов и непрерывных полей.

**Иллюстрация 14.3 / Figure 14.3 — Координатные системы и проекции / Coordinate reference systems and projections.**  
Схема географических координат, референц-эллипсоида и проецированной сетки; не смешивать геоид, эллипсоид и картографическую проекцию.

**Иллюстрация 14.4 / Figure 14.4 — Пространственное наложение слоёв / Spatial overlay.**  
Пошаговая схема пересечения двух полигональных слоёв с атрибутами; геометрический результат должен соответствовать операции.

**Иллюстрация 14.5 / Figure 14.5 — Сетевой анализ доступности / Network accessibility analysis.**  
Сравнить круговой буфер и зону доступности по реальной дорожной сети, показав барьеры и различия маршрутов.

**Иллюстрация 14.6 / Figure 14.6 — Цифровая модель рельефа / Digital elevation model.**  
Показать исходный растр высот и производные карты уклона и экспозиции; подчеркнуть зависимость детализации от разрешения и качества.

**Иллюстрация 14.7 / Figure 14.7 — Контроль качества геоданных / Spatial data quality control.**  
Примеры зазора, наложения, разрыва линии, дубликата и ошибки CRS; каждому дефекту дать корректную подпись.

**Иллюстрация 14.8 / Figure 14.8 — Картографическая визуализация / Cartographic visualisation.**  
Сравнить корректную хороплетную карту нормированного показателя с вводящей в заблуждение картой абсолютных значений; показать легенду, источник и дату.

**Иллюстрация 14.9 / Figure 14.9 — Воспроизводимый ГИС-процесс / Reproducible GIS workflow.**  
Диаграмма этапов от постановки задачи и получения данных до проверки, документирования и публикации.

## Научные редакционные примечания / Scientific Editorial Notes

- Все примеры координатных систем должны сопровождаться корректными названиями и областью применения; EPSG-коды проверять по актуальному реестру.
- Не смешивать географические координаты, проецированные координаты, геодезический датум, эллипсоид и геоид.
- При измерении расстояний и площадей указывать CRS и метод расчёта.
- Утверждения о точности данных должны основываться на документации поставщика или независимой проверке.
- При анализе растров указывать размер ячейки, метод ресэмплинга, NoData и происхождение данных.
- Карты плотности и хороплеты должны использовать методически корректные знаменатели и классификацию.
- Для сетевого анализа документировать правила связности, направления, скорости и ограничения движения.
- При публикации геоданных проверять лицензии, персональные данные и чувствительные объекты.
- Иллюстрации должны сохранять научно корректную геометрию операций и не подменять реальные данные декоративными схемами.

## Основные источники и рекомендуемая литература / Core Sources and Further Reading

1. Open Geospatial Consortium (OGC). **Standards and Abstract Specifications** — стандарты обмена и публикации геопространственных данных.
2. International Organization for Standardization (ISO). **ISO 19100 Geographic information series** — стандарты географической информации.
3. EPSG Geodetic Parameter Dataset. **EPSG Registry** — определения систем координат и геодезических параметров.
4. QGIS Documentation. **QGIS User Guide and Training Manual** — открытая документация по настольной ГИС и пространственному анализу.
5. Esri. **GIS Dictionary and ArcGIS Pro Documentation** — справочные материалы и описания методов ГИС.
6. Longley, P. A., Goodchild, M. F., Maguire, D. J., Rhind, D. W. **Geographic Information Science and Systems**. Wiley.
7. O'Sullivan, D., Unwin, D. J. **Geographic Information Analysis**. Wiley.
8. de Smith, M., Goodchild, M., Longley, P. **Geospatial Analysis: A Comprehensive Guide**.
9. United Nations Committee of Experts on Global Geospatial Information Management (UN-GGIM). **Integrated Geospatial Information Framework (IGIF)**.
10. World Geodetic System 1984 (WGS 84). **Technical documentation** — описание глобальной геодезической системы.

---
**Конец главы 14 / End of Chapter 14**
