from m3 import *
# 18-I and 25-C minerals
def minerals(): 
    m=base()
    m.blob(78.3,41.85,60,22,'#d4a017','Золото: Центральный Тянь-Шань','Gold: Central Tien Shan',.4)
    m.blob(71.5,39.9,90,22,'#7f8c8d','Сурьма, ртуть: Баткен','Antimony, mercury: Batken',.4)
    m.blob(72.0,40.3,60,12,'#34495e',None,None,.45); m.blob(72.3,41.3,60,16,'#34495e','Угольные районы','Coal districts',.45)
    m.blob(72.45,41.27,12,8,'#8e44ad',None,None,.7); m.dot(72.45,41.27,'Майлуу-Суу: урановое наследие','Mailuu-Suu: uranium legacy',5,'#8e44ad',10,24)
    m.city('Bishkek'); m.city('Osh',dy=16); return m
m=minerals()
m.legend([('золото','gold','#d4a017'),('сурьма, ртуть','antimony, mercury','#7f8c8d'),('уголь','coal','#34495e'),('урановое наследие','uranium legacy','#8e44ad')],x=60,y=700)
S('18-I','mineragenic-districts','Минерагенические районы Кыргызстана (схема)','Mineragenic districts of Kyrgyzstan (schematic)','Районы золота, сурьмы, ртути, угля и уранового наследия.','Districts of gold, antimony, mercury, coal and uranium legacy.',m.svg(),'Районы, а не рудники: условные проявления не обозначены как действующие объекты; дата и статус — по официальному реестру.','Districts, not mines: prospects are not marked as operating sites; date and status come from the official register.','Минерагенические районы: схема.','Mineragenic districts: schematic.')
m=minerals()
m.legend([('металлы: золото, сурьма, ртуть','metals: gold, antimony, mercury','#d4a017'),('топливо: уголь','fuel: coal','#34495e'),('наследие уранодобычи','uranium-mining legacy','#8e44ad')],x=60,y=700)
S('25-C','mineral-resources-districts','Минеральные ресурсы: районы (схема)','Mineral resources: districts (schematic)','Районы добычи и перспективных ресурсов без статуса отдельных объектов.','Mining and resource districts without the status of individual sites.',m.svg(),'Действующие объекты, разведанные запасы и перспективные участки здесь не различаются: статус нужно брать из реестра недропользования; лицензионные границы не показаны.','Operating sites, explored reserves and prospects are not distinguished here: take status from the subsoil register; licence boundaries are not shown.','Минеральные ресурсы: районы.','Mineral resources: districts.')
# 25-E functional cities
FN={'Bishkek':'АПТ','Osh':'АТГ','Manas':'А','Karakol':'АР','Naryn':'А','Talas':'А','Batken':'АГ','Balykchy':'ТР','Cholpon-Ata':'Р','Kara-Balta':'П','Tokmok':'П','Kara-Suu':'ТГ','Kyzyl-Kiya':'П','Toktogul':'П'}
m=base()
for k,f in FN.items():
    lon,lat,ru,en=CITIES[k]; m.dot(lon,lat,ru+' '+f,None,6,'#243447',8,-6)
m.legend([('А — административная функция','A — administrative','#fff'),('П — промышленная','P/I — industrial','#fff'),('Т — транспортная','T — transport','#fff'),('Р — туристическая (рекреация)','R — tourism / recreation','#fff'),('Г — приграничная','G — border function','#fff')],x=60,y=590)
S('25-E','functional-cities','Функции городов Кыргызстана (схема)','City functions in Kyrgyzstan (schematic)','У города может быть несколько функций.','A city can have several functions.',m.svg(),'Функции даны обобщённо и не заменяют анализа занятости и данных по предприятиям.','Functions are generalised and do not replace employment and enterprise data.','Функции городов: схема.','City functions: schematic.')
# 25-G south
m=zoom((70.2,74.2,39.5,41.6))
for k,dx,dy,an in [('Osh',-10,-8,'end'),('Kara-Suu',10,-4,'start'),('Uzgen',10,-8,'start'),('Nookat',-10,16,'end'),('Kyzyl-Kiya',-10,-8,'end'),('Batken',-10,14,'end'),('Manas',10,-8,'start'),('Isfana',-10,16,'end')]: m.city(k,dx=dx,dy=dy,anchor=an)
S('25-G','southern-urban-system','Южная городская система (схема)','Southern urban system (schematic)','Ош, Кара-Суу, Узген, Ноокат и центры Баткенской и Джалал-Абадской областей.','Osh, Kara-Suu, Uzgen, Nookat and centres of Batken and Jalal-Abad regions.',m.svg(),'Административные статусы не смешиваются: Ош — город республиканского значения; остальные города — в составе областей.','Administrative statuses are not mixed: Osh is a city of republican significance; the other towns belong to regions.','Южная городская система: схема.','Southern urban system: schematic.')
# 25-H GDP
sec=[('Услуги','Services',48.7,106.1),('Промышленность','Industry',18.4,107.1),('Чистые налоги на продукты','Net taxes on products',15.4,110.8),('Строительство','Construction',9.1,162.2),('Сельское и лесное хозяйство, рыболовство','Agriculture, forestry, fishing',8.4,106.5)]
body=T(60,125,'Доля в ВВП, % / Share of GDP','lab')+T(800,125,'Реальный прирост к янв.–сент. 2025, % / Real growth','lab')
for i,(a,b,sh,ix) in enumerate(sec):
    y=160+i*100; body+=T(60,y+22,a,'t')+T(60,y+46,b,'s','start','style="fill:#526579"')
    body+=f'<rect x="430" y="{y}" width="{sh/48.7*300:.0f}" height="34" fill="#2e86ab"/>'+T(430+sh/48.7*300+8,y+25,f'{sh:.1f}'.replace('.',',')+' %','lab')
    g=ix-100; body+=f'<rect x="1000" y="{y}" width="{g/62.2*300:.0f}" height="34" fill="#c0392b"/>'+T(1000+g/62.2*300+8,y+25,'+'+f'{g:.1f}'.replace('.',',')+' %','lab')
body+=T(60,690,'Строительство даёт 9,1 % ВВП, но растёт быстрее всех (+62,2 %): малая доля не мешает высокому темпу.','s')+T(60,714,'Construction is 9.1% of GDP but grows fastest (+62.2%): a small share can still show a high growth rate.','s','start','style="fill:#526579"')
S('25-H','gdp-structure-2026','Структура ВВП: доли и темпы роста раздельно','GDP structure: shares and growth shown separately','Предварительная оценка НСК за январь–сентябрь 2026 года.','NSC preliminary estimate for January–September 2026.',body,'Источник: НСК, предварительная оценка за январь–сентябрь 2026 (таблица главы 25); данные предварительные, доли округлены.','Source: NSC preliminary estimate for January–September 2026 (Chapter 25 table); data are preliminary, shares rounded.','Структура ВВП и темпы роста.','GDP structure and growth rates.')
# 25-J international corridors
m=KG(box=(66.0,84.0,36.0,48.0)).ctx().oblasts(op:=1,opacity=.8) if False else KG(box=(66.0,84.0,36.0,48.0)).ctx().oblasts(opacity=.8).outline()
PL={}
for f in feats('ne_10m_populated_places_simple',lambda p:p['name'] in ('Almaty','Tashkent','Kashgar','Andijon','Dushanbe','Urumqi','Astana','Namangan')): PL[f['properties']['name']]=f['geometry']['coordinates']
for k,(ru,en) in {'Almaty':('Алматы','Almaty'),'Tashkent':('Ташкент','Tashkent'),'Kashgar':('Кашгар','Kashgar'),'Andijon':('Андижан','Andijan'),'Dushanbe':('Душанбе','Dushanbe')}.items():
    if k in PL: m.dot(PL[k][0],PL[k][1],ru,en,5,'#7f8c8d',8,-6)
m.city('Bishkek'); m.city('Osh',dy=16)
m.line([(74.6,42.87),(76.9,43.25)],'#c0392b',4); m.line([(72.8,40.53),(73.0,40.7),(72.35,40.8)],'#c0392b',4); m.line([(74.6,42.87),(72.8,40.53)],'#c0392b',4)
m.line([(75.99,39.47),(75.39,40.52),(73.9,41.0),(72.98,40.93),(71.8,40.8)],'#8e44ad',4,'12 8')
m.text(76.0,44.3,'север–юг: Казахстан – Бишкек – Ош – Узбекистан','north–south: Kazakhstan – Bishkek – Osh – Uzbekistan','sm','middle','#c0392b'); m.text(75.0,38.2,'Китай – Кыргызстан – Узбекистан (проектируемая линия)','China – Kyrgyzstan – Uzbekistan (planned line)','sm','middle','#8e44ad')
S('25-J','international-corridors','Международные коридоры (схема)','International corridors (schematic)','Север–юг и проектируемая связь Китай–Кыргызстан–Узбекистан.','North–south links and the planned China–Kyrgyzstan–Uzbekistan connection.',m.svg(),'Схема: ход линий ориентировочный; действующие (сплошные) и проектируемые (пунктир) связи различены; решения и сроки — по официальным данным.','Schematic: routes are approximate; existing (solid) and planned (dashed) links are distinguished; decisions and timing follow official data.','Международные коридоры: схема.','International corridors: schematic.')
# 25-K energy
m=base()
m.blob(72.6,41.75,60,22,'#2e86ab','Токтогульский каскад ГЭС','Toktogul HPP cascade',.4,-10)
m.line([(72.6,41.0),(74.2,42.0),(75.7,42.78)],'#c0392b',3,'10 6'); m.text(74.4,41.7,'ЛЭП 500 кВ Датка–Кемин','500 kV Datka–Kemin line','sm','middle','#c0392b')
m.dot(74.5,42.87,'ТЭЦ Бишкека','Bishkek CHP',6,'#34495e',-10,-8,'end'); m.dot(75.8,41.17,'Ат-Башы ГЭС','At-Bashy HPP',5,'#2e86ab',8,14)
m.blob(73.3,41.95,30,10,'#2e86ab',None,None,.0); m.text(73.6,41.4,'Камбарата-1 (проектируется)','Kambarata-1 (planned)','sm','middle','#2874a6')
m.city('Bishkek',dx=8,dy=-8,anchor='start'); m.city('Osh',dy=16)
m.legend([('ГЭС','hydropower','#2e86ab'),('ТЭЦ','combined heat and power','#34495e'),('ЛЭП (схема)','power line (schematic)','#c0392b')],x=60,y=700)
S('25-K','energy-system','Энергетическая система (схема)','Energy system (schematic)','ГЭС Токтогульского каскада, ТЭЦ Бишкека и линия север–юг.','Toktogul cascade, Bishkek CHP and the north–south line.',m.svg(),'Мощности не указаны: их берут только из проверенных данных; положение объектов ориентировочное.','Capacities are not given: use verified data only; positions are approximate.','Энергетическая система: схема.','Energy system: schematic.')
# 25-L scenarios table
sc=[('Опора на крупные города','Large-city focus',['Рост Бишкека и Оша, нагрузка на транспорт и воду','Села и высокогорье теряют население']),('Сбалансированное развитие','Balanced development',['Рост региональных центров и связей между ними','Умеренная нагрузка на Чуйскую и Ферганскую долины']),('Сильные региональные центры','Strong regional centres',['Рабочие места в областях, коридоры и цифровые услуги','Больше затрат на дороги и сети'])]
body='' 
for i,(a,b,ls) in enumerate(sc):
    x=40+i*450; body+=box(x,110,420,500,['#f4ecd9','#e5efe3','#e4eff6'][i])+T(x+20,150,a,'t')+T(x+20,176,b,'s','start','style="fill:#526579"')
    for j,l in enumerate(ls): body+=T(x+20,230+j*70,'• '+l,'sm')
body+=T(40,650,'Три условных сценария для обсуждения; измеримые показатели и допущения нужно задать отдельно (население, расходы, время в пути).','s')+T(40,676,'Three conventional scenarios for discussion; measurable indicators and assumptions must be set separately (population, spending, travel time).','s','start','style="fill:#526579"')
S('25-L','spatial-development-scenarios','Три сценария пространственного развития','Three spatial-development scenarios','Качественное сравнение трёх путей развития.','A qualitative comparison of three development paths.',body,'Учебные сценарии без цифр: это не прогноз и не официальная программа.','Teaching scenarios without numbers: not a forecast or an official programme.','Три сценария: качественно.','Three scenarios: qualitative.')
# 23-K settlements + hazards
m=base()
m.blob(72.2,41.0,150,60,'#c0392b','Сейсмика','Seismicity',.22); m.blob(76.5,42.6,170,34,'#c0392b',None,None,.22,-4); m.blob(72.6,41.3,110,24,'#8e5b2c','Оползни','Landslides',.3,18); m.blob(72.8,40.1,130,18,'#8e5b2c','Сели','Debris flows',.3); m.blob(74.5,42.0,70,14,'#7f8c8d','Лавины','Avalanches',.4,-8)
for k in ['Bishkek','Osh','Manas','Karakol','Naryn','Talas','Batken']: m.city(k,dx=8,dy=-6)
S('23-K','settlements-and-hazards','Поселения и природные опасности (схема)','Settlements and natural hazards (schematic)','Города на фоне качественных зон опасностей.','Cities set against qualitative hazard zones.',m.svg(),'Не карта риска: зоны качественные; риск = опасность × экспозиция × уязвимость.','Not a risk map: zones are qualitative; risk = hazard × exposure × vulnerability.','Поселения и опасности: схема.','Settlements and hazards: schematic.')
# 23-L scenario fan
body='<line x1="120" y1="620" x2="1280" y2="620" stroke="#44586b" stroke-width="2"/><line x1="120" y1="140" x2="120" y2="620" stroke="#44586b" stroke-width="2"/>'
body+=f'<circle cx="260" cy="450" r="9" fill="#243447"/>'+T(280,440,'2026: 7,404 млн (НСК)','lab')+T(280,462,'2026: 7.404 million (NSC)','sm','start','style="fill:#526579"')
for lab_r,lab_e,y,c in [('высокий сценарий','high scenario',230,'#c0392b'),('базовый сценарий','base scenario',330,'#2e86ab'),('низкий сценарий','low scenario',420,'#27ae60')]:
    body+=f'<path d="M260 450 C600 {450-(450-y)*0.3:.0f} 900 {y+20} 1200 {y}" fill="none" stroke="{c}" stroke-width="5"/>'+T(1215,y+6,lab_r,'lab','start','style="fill:%s"'%c)+T(1215,y+26,lab_e,'sm')
body+=T(130,130,'Численность населения (условная шкала) / Population (conventional scale)','sm')+T(1100,650,'время / time','sm','middle')
S('23-L','population-scenarios-fan','Сценарии численности населения (концептуальная схема)','Population scenarios (conceptual schematic)','Три траектории от базового года; значения не показаны.','Three trajectories from the baseline year; values are not shown.',body,'Концептуальная схема: расходятся траектории из-за допущений о рождаемости, смертности и миграции; реальные прогнозы — с источником и датой.','Conceptual schematic: trajectories diverge because of assumptions on fertility, mortality and migration; real projections need a source and date.','Сценарии численности: схема.','Population scenarios: schematic.')
# ---- ch26
m=base()
body=m.svg()
body+=box(760,110,600,320,'#fff')+T(780,145,'Рост температуры, 1960–2023','t')+T(780,168,'Temperature rise, 1960–2023','s','start','style="fill:#526579"')
body+=f'<rect x="800" y="{410-1.2*150:.0f}" width="110" height="{1.2*150:.0f}" fill="#c0392b"/>'+T(855,250,'+1,2 °C','t','middle')+T(855,272,'Кыргызстан / Kyrgyzstan','sm','middle')
body+=f'<rect x="1000" y="{410-0.6*150:.0f}" width="110" height="{0.6*150:.0f}" fill="#7f8c8d"/>'+T(1055,300,'≈ вдвое меньше','sm','middle')+T(1055,320,'about half as much','sm','middle')+T(1055,338,'(глобальное значение)','sm','middle')+T(1055,356,'(global figure)','sm','middle')
body+=T(780,460,'По оценке UNEP; национальная оценка для периода, не для каждой станции.','sm')+T(780,480,'UNEP estimate; a national estimate for the period, not for every station.','sm','start','style="fill:#526579"')
m2=KG(30,110,700,600).ctx().oblasts(opacity=.5).outline(); 
for lo,la,rx,ry,c,ru,en in [(72.4,40.7,100,30,'#e74c3c','Теплее','Warmer'),(76.0,41.3,100,22,'#85c1e9','Холоднее','Colder')]: m2.blob(lo,la,rx,ry,c,ru,en,.4)
body=m2.svg()+body[body.index('<rect x="760"'):] if False else m2.svg()+body[body.index('<rect x="760"'):]
S('26-A','climate-trend-and-regions','Потепление в Кыргызстане и региональные различия','Warming in Kyrgyzstan and regional differences','Оценка прироста температуры и качественная схема различий.','Estimated temperature rise and a qualitative schematic of differences.',body,'Только оценка UNEP для 1960–2023: годовой ряд не показан; наблюдения и модельные проекции не смешаны.','Only the UNEP estimate for 1960–2023: no annual series is shown; observations and model projections are not mixed.','Потепление: оценка и региональные различия.','Warming: estimate and regional differences.')
m=base()
for lo,la,rx,ry,ang,ru,en in [(80.0,42.15,70,26,-10,'Ледники','Glaciers'),(78.0,41.5,110,18,-4,None,None),(72.6,39.5,110,16,0,None,None)]: m.blob(lo,la,rx,ry,'#5dade2',ru,en,.55,ang)
def arr2(m,a,b,c,ru,en):
    (x1,y1),(x2,y2)=m.P(*a),m.P(*b); m.o.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{c}" stroke-width="5" marker-end="url(#arrow)" fill="none"/>'+T((x1+x2)/2,(y1+y2)/2-8,ru+' / '+en,'sm','middle','style="paint-order:stroke;stroke:#fff;stroke-width:3px;font-weight:700"'))
arr2(m,(72.8,41.1),(70.4,40.9),'#2e86ab','Нарын → Сырдарья','Naryn → Syr Darya'); arr2(m,(74.2,42.7),(71.6,43.2),'#27ae60','Чу','Chu'); arr2(m,(73.0,39.6),(72.4,39.0),'#c0392b','Кызыл-Суу','Kyzyl-Suu')
m.text(77.2,41.55,'Снеговое и ледниковое питание: роль ледников меняется с климатом','Snow and glacier supply: the role of glaciers changes with climate','sm')
S('26-B','water-security-schematic','Водная безопасность: ледники и бассейны (схема)','Water security: glaciers and basins (schematic)','Ледники питают реки, уходящие в соседние страны.','Glaciers feed rivers that flow into neighbouring countries.',m.svg(),'Сравнение инвентаризаций ледников — в тексте главы; контуры здесь схематичны и не заменяют каталогов.','Comparison of glacier inventories is in the chapter text; outlines here are schematic and do not replace catalogues.','Водная безопасность: схема.','Water security: schematic.')
m=base()
for lo,la,rx,ry,c,ru,en in [(72.4,40.7,170,34,'#2ecc71','Орошаемые земли','Irrigated land'),(74.8,42.78,120,18,'#2ecc71','Орошение','Irrigation'),(72.2,42.5,50,14,'#2ecc71','Орошение','Irrigation')]: m.blob(lo,la,rx,ry,c,ru,en,.35)
arr2(m,(72.8,41.0),(70.4,40.9),'#2e86ab','к Узбекистану','to Uzbekistan'); arr2(m,(74.2,42.8),(71.7,43.2),'#27ae60','к Казахстану','to Kazakhstan')
m.city('Bishkek'); m.city('Osh',dy=16)
S('26-C','river-basin-vulnerability','Уязвимость речных бассейнов (схема)','River-basin vulnerability (schematic)','Орошение, города и направления трансграничного стока.','Irrigation, cities and transboundary flow directions.',m.svg(),'Схема: водозаборы и числа не показаны; для оценки уязвимости нужны данные с датой и источником.','Schematic: intakes and numbers are not shown; assessing vulnerability needs dated and sourced data.','Уязвимость бассейнов: схема.','Basin vulnerability: schematic.')
m=base()
for lo,la,rx,ry,c,ru,en in [(78.4,41.6,170,40,'#7fb069','Летние пастбища (джайлоо)','Summer pastures (jailoo)'),(75.6,41.0,150,24,'#7fb069',None,None),(74.0,42.9,70,12,'#e6b85c','Зимние пастбища','Winter pastures'),(72.4,40.4,100,14,'#e6b85c',None,None),(74.6,42.55,60,10,'#c0392b','Выбитые пастбища у сёл','Overgrazed near villages',)]:
    m.blob(lo,la,rx,ry,c,ru,en,.4)
S('26-D','pastures-schematic','Пастбища и их состояние (схема)','Pastures and their condition (schematic)','Летние и зимние пастбища и участки перегрузки.','Summer and winter pastures and overloaded sites.',m.svg(),'Национальная оценка деградации, локальные обследования и спутниковые индексы — разные источники: здесь только схема.','National degradation estimates, local surveys and satellite indices are different sources: this is only a schematic.','Пастбища: схема.','Pastures: schematic.')
m=base()
for lo,la,rx,ry,c,ru,en in [(72.4,41.5,100,30,'#2e8b57','Ореховые леса и арчовники','Walnut forests and juniper'),(77.8,42.5,100,14,'#1e6b45','Ельники','Spruce forests'),(74.5,42.5,60,10,'#1e6b45',None,None)]: m.blob(lo,la,rx,ry,c,ru,en,.45)
for a,b in [((72.0,41.8),(72.9,41.35)),((74.5,42.55),(76.4,42.8)),((76.4,42.8),(78.5,42.4))]: m.line([a,b],'#27ae60',3,'8 6')
m.dot(71.95,41.83,None,None,6,'#27ae60'); m.dot(72.93,41.33,None,None,6,'#27ae60'); m.dot(74.5,42.55,None,None,6,'#2980b9'); m.dot(76.4,42.8,None,None,6,'#2980b9'); m.dot(78.5,42.4,None,None,6,'#2980b9')
m.text(75.5,43.2,'условные экологические связи (пунктир)','conceptual ecological links (dashed)','sm','middle','#27ae60')
S('26-E','forests-and-corridors','Леса и экологические связи (схема)','Forests and ecological links (schematic)','Основные лесные комплексы и условные связи между охраняемыми территориями.','Main forest complexes and conceptual links between protected areas.',m.svg(),'Пунктир — идея связности, не утверждённые коридоры; границы ООПТ и дата геоданных — по официальным источникам.','Dashed lines show the idea of connectivity, not approved corridors; boundaries and geodata date come from official sources.','Леса и связность: схема.','Forests and connectivity: schematic.')
# 26-F air
body=''
body+=box(40,110,640,600,'#fff')+T(60,145,'Зимняя температурная инверсия в котловине','t')+T(60,168,'Winter temperature inversion in a basin','s','start','style="fill:#526579"')
body+=f'<path d="M60 560 L200 560 L300 330 L420 560 L520 560 L620 330 L660 560 L660 640 L60 640Z" fill="#b59a7a" stroke="#6b5a45" stroke-width="2"/>'
body+=f'<rect x="60" y="400" width="600" height="150" fill="#dfe6ec" fill-opacity=".8"/><path d="M60 400 L660 400" stroke="#2e86ab" stroke-width="3" stroke-dasharray="8 5"/>'
body+=T(280,385,'тёплый воздух сверху / warmer air above','sm','middle')+T(360,540,'холодный воздух и выбросы у земли','sm','middle')+T(360,558,'cold air and emissions trapped near the ground','sm','middle')
body+=box(710,110,650,600,'#f1f4f6')+T(730,145,'Источники и меры','t')+T(730,168,'Sources and responses','s','start','style="fill:#526579"')
items=[('Печное отопление и уголь','Stove heating and coal'),('Транспорт','Traffic'),('Теплоэлектроцентрали','Heat and power plants'),('Пыль и сжигание отходов','Dust and waste burning'),('Посты наблюдений: PM2,5, PM10','Monitoring stations: PM2.5, PM10')]
for j,(a,b) in enumerate(items): body+=T(740,225+j*80,'• '+a,'lab')+T(760,247+j*80,b,'s','start','style="fill:#526579"')
S('26-F','urban-air-inversion','Городской воздух: инверсия, источники, наблюдения','Urban air: inversion, sources, monitoring','Почему зимой воздух в котловинах хуже.','Why winter air is worse in basins.',body,'Схема процесса, а не карта загрязнения; уровни загрязнения берут из постов наблюдений с датой.','A process schematic, not a pollution map; pollution levels come from dated monitoring stations.','Городской воздух: схема.','Urban air: schematic.')
# 26-G water & sanitation
steps=[('Водозабор','Intake'),('Очистка воды','Water treatment'),('Водопровод','Supply network'),('Потребители','Users'),('Канализация','Sewers'),('Очистные сооружения','Wastewater treatment'),('Сброс в водоём','Discharge to a water body')]
body=''
for i,(a,b) in enumerate(steps):
    x=30+i*190; body+=box(x,250,170,130,['#e4eff6','#e4eff6','#e5efe3','#f4ecd9','#f5e7e4','#f5e7e4','#e4eff6'][i])+T(x+85,310,a,'lab','middle')+T(x+85,334,b,'sm','middle','style="fill:#526579"')
    if i<6: body+=arrow(x+172,315,x+188,315)
body+=T(40,470,'Потери в сетях, неочищенные стоки и сбросы в чувствительные водоёмы — места, где цепочка рвётся.','s')+T(40,494,'Network losses, untreated wastewater and discharges to sensitive waters are where the chain breaks.','s','start','style="fill:#526579"')
S('26-G','water-sanitation-chain','Водоснабжение и канализация: цепочка','Water supply and sanitation: the chain','Путь воды от источника до водоёма-приёмника.','The path of water from source to receiving water body.',body,'Обобщённая схема; сведения о конкретных очистных сооружениях и сбросах — из официальных данных.','A generalised schematic; data on specific treatment plants and discharges come from official sources.','Водоснабжение и канализация: цепочка.','Water supply and sanitation: the chain.')
# 26-J mining
steps=[('Карьер или шахта','Pit or mine'),('Хвостохранилище','Tailings storage'),('Нарушенные земли','Disturbed land'),('Мониторинг','Monitoring'),('Рекультивация','Reclamation')]
body=''
for i,(a,b) in enumerate(steps):
    x=40+i*270; body+=box(x,250,240,130,['#f4ecd9','#f5e7e4','#f5e7e4','#e4eff6','#e5efe3'][i])+T(x+120,310,a,'lab','middle')+T(x+120,334,b,'sm','middle','style="fill:#526579"')
    if i<4: body+=arrow(x+244,315,x+266,315)
body+=T(40,470,'Экологические обязательства начинаются до добычи (оценка воздействия) и продолжаются после закрытия.','s')+T(40,494,'Environmental obligations start before extraction (impact assessment) and continue after closure.','s','start','style="fill:#526579"')
S('26-J','mining-obligations-cycle','Горнодобыча: от карьера до рекультивации','Mining: from pit to reclamation','Последовательность экологических обязательств.','The sequence of environmental obligations.',body,'Схема цикла без карты: расположение хвостохранилищ и нарушенных земель — по официальным реестрам.','A cycle schematic without a map: locations of tailings and disturbed land come from official registers.','Горнодобыча и рекультивация: цикл.','Mining and reclamation: cycle.')
# 26-L scenarios 2050
ind=['Климат','Вода','Земли','Биоразнообразие','Воздух','Качество жизни']; ind_e=['Climate','Water','Land','Biodiversity','Air','Quality of life']
scn=[('Без дополнительных мер','No additional measures','#c0392b','↓↓↓↓↓↓'),('Частичные меры','Partial measures','#e67e22','→→↓→→→'),('Согласованные меры','Coordinated measures','#27ae60','↑↑↑↑↑↑')]
body=''
for j in range(6): body+=T(380+j*155,140,ind[j],'lab','middle')+T(380+j*155,160,ind_e[j],'sm','middle','style="fill:#526579"')
for i,(a,b,c,ar) in enumerate(scn):
    y=210+i*130; body+=box(40,y-45,260,100,'#f1f4f6')+T(60,y-8,a,'t')+T(60,y+16,b,'s')
    for j,ch in enumerate(ar): body+=f'<text x="{380+j*155}" y="{y+18}" font-size="52" text-anchor="middle" style="fill:{c}">{ch}</text>'
body+=T(40,640,'Стрелки — качественная иллюстрация направления; числа зависят от допущений, которые нужно назвать.','s')+T(40,664,'Arrows are a qualitative illustration of direction; numbers depend on assumptions that must be stated.','s','start','style="fill:#526579"')
S('26-L','scenarios-2050','Три сценария до 2050 года (качественно)','Three scenarios to 2050 (qualitative)','Как меры влияют на климат, воду, земли, воздух и жизнь.','How measures affect climate, water, land, air and quality of life.',body,'Это не прогноз: учебная иллюстрация логики сценариев без чисел.','Not a forecast: a teaching illustration of scenario logic without numbers.','Сценарии до 2050: качественно.','Scenarios to 2050: qualitative.')
print('m4 ok')
