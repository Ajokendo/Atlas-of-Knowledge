from m2 import *
import math
def zoom(box,op=.5,water=True):
    m=KG(box=box).ctx().oblasts(opacity=op).outline()
    if water: lakes_rivers(m)
    return m
def chuy(m):
    for pts_ in [[(76.15,42.5),(75.3,42.85),(74.0,42.93),(72.8,43.05)]]: pass
    return m
def popbar(vals,x,y,w,h,maxv):
    pass
# ---- 23-A density (qualitative)
m=base()
for lo,la,rx,ry,c,ru,en,op in [(72.5,40.7,170,40,'#7b241c','Ферганская долина: высокая','Fergana Valley: high',.6),(74.8,42.78,120,22,'#a93226','Чуйская долина: высокая','Chuy Valley: high',.6),(77.0,42.5,170,12,'#e67e22','Берега Иссык-Куля: средняя','Issyk-Kul shores: medium',.5),(72.2,42.5,60,16,'#e67e22','Талас: средняя','Talas: medium',.5),(76.0,41.3,150,26,'#f7dc6f','Внутренний Тянь-Шань: низкая','Inner Tien Shan: low',.55),(78.8,41.3,100,24,'#fcf3cf','Высокогорье: очень низкая','High mountains: very low',.8)]:
    m.blob(lo,la,rx,ry,c,ru,en,op,stroke='#fff')
CITY3(m)
S('23-A','population-density-qualitative','Плотность населения: качественная схема','Population density: qualitative schematic','Население сосредоточено в долинах, высокогорье почти не заселено.','Settlement is concentrated in valleys; the high mountains are almost empty.',m.svg(),'Без числовых значений: для карты плотности нужны районы или айылные аймаки на одну дату, единицы и источник.','No numeric values: a real density map needs districts or aiyl aimaks for one date, units and a source.','Плотность населения: качественная схема.','Population density: qualitative schematic.')
# ---- 23-B panel with real figures
body=''
body+=box(40,110,640,300,'#f1f4f6')+T(60,145,'Численность населения, млн','t')+T(60,168,'Population, million','s','start','style="fill:#526579"')
data=[('перепись 2022 / census 2022',6.936,'#7f8c8d'),('01.01.2024',7.162,'#2e86ab'),('01.01.2025',7.282,'#2e86ab'),('01.01.2026',7.404,'#2e86ab')]
for i,(lab,v,c) in enumerate(data):
    h=(v-6.5)*190; x=90+i*150
    body+=f'<rect x="{x}" y="{390-h:.0f}" width="100" height="{h:.0f}" fill="{c}"/>'+T(x+50,382-h,f'{v:.3f}'.replace('.',','),'lab','middle')+T(x+50,408,lab,'sm','middle')
body+=T(60,430,'Ось начинается с 6,5 млн, чтобы показать различия. Перепись и годовые оценки — разные источники.','sm')+T(60,450,'The axis starts at 6.5 million to show differences. Census and annual estimates are different sources.','sm','start','style="fill:#526579"')
body+=box(710,110,650,420,'#f1f4f6')+T(730,145,'Население на 01.01.2026, тыс. чел.','t')+T(730,168,'Population on 1 January 2026, thousand','s','start','style="fill:#526579"')
reg=[('Ошская область','Osh Region',1438.5),('Джалал-Абадская','Jalal-Abad',1379.9),('Бишкек (город)','Bishkek (city)',1358.6),('Чуйская','Chuy',983.7),('Баткенская','Batken',605.3),('Иссык-Кульская','Issyk-Kul',554.3),('Ош (город)','Osh (city)',484.9),('Нарынская','Naryn',316.2),('Таласская','Talas',282.9)]
for i,(a,b,v) in enumerate(reg):
    y=195+i*36; col='#a93226' if 'город' in a else '#2e86ab'
    body+=T(730,y+14,a+' / '+b,'sm')+f'<rect x="1040" y="{y}" width="{v/1438.5*250:.0f}" height="20" fill="{col}"/>'+T(1040+v/1438.5*250+6,y+16,f'{v:,.1f}'.replace(',',' ').replace('.',','),'sm')
body+=box(40,560,1320,150,'#fff')+T(60,595,'Как читать панель','lab')+T(60,622,'Переписные данные 2022 года и ежегодные оценки НСК различаются по методике; Бишкек и Ош — города республиканского значения, а не области.','s')+T(60,664,'How to read the panel: 2022 census data and annual NSC estimates differ in method; Bishkek and Osh are cities of republican significance, not oblasts.','s','start','style="fill:#526579"')
S('23-B','demographic-panel','Демографическая панель Кыргызстана','Demographic panel of Kyrgyzstan','Динамика численности населения и распределение по областям и городам.','Population trend and distribution by region and city.',body,'Источник чисел: переписи 2022 года и НСК (открытые ряды) по тексту главы 23. Возрастно-половая пирамида на панель не вынесена.','Figures: 2022 census and NSC open series as quoted in Chapter 23. The age-sex pyramid is not included in this panel.','Численность и региональное распределение населения.','Population trend and regional distribution.')
# ---- 23-C / 25-A urban system
SIZES={'Bishkek':14,'Osh':12,'Manas':9,'Karakol':8,'Naryn':7,'Talas':7,'Batken':6,'Balykchy':6,'Tokmok':6,'Kara-Balta':6,'Kara-Suu':6,'Uzgen':6,'Kyzyl-Kiya':6}
def urban(m,keys):
    for k in keys:
        lon,lat,ru,en=CITIES[k]; r=SIZES.get(k,6)
        m.dot(lon,lat,ru,en,r,'#c0392b' if k in('Bishkek','Osh') else '#243447',r+4,-4)
m=base(); urban(m,SIZES.keys())
m.legend([('города республиканского значения','cities of republican significance','#c0392b'),('областные и другие города','oblast centres and other cities','#243447')],x=60,y=700)
S('23-C','urban-system','Городская система Кыргызстана (схема)','Urban system of Kyrgyzstan (schematic)','Бишкек и Ош, областные центры и другие крупные города.','Bishkek and Osh, oblast centres and other major cities.',m.svg(),'Размер значка условный и не равен численности; границы и статус населённых пунктов — по официальным данным.','Symbol size is conventional, not population; boundaries and status of settlements follow official data.','Городская система: схема.','Urban system: schematic.')
m=base(); urban(m,SIZES.keys())
m.dot(72.98,40.93,None,None,0)
m.line([(74.6,42.87),(73.9,42.3),(73.0,41.9),(72.7,41.6),(72.2,41.35),(72.98,40.93),(72.8,40.53)],'#c0392b',3,'8 5'); m.line([(74.6,42.87),(76.2,42.46),(77.1,42.65),(78.4,42.49)],'#c0392b',3,'8 5')
m.text(73.4,42.25,'главные связи','main links','sm','middle','#c0392b')
S('25-A','urban-system-links','Городская система и главные связи','Urban system and main links','Бишкек, Ош, областные центры и транспортные связи между ними.','Bishkek, Osh, oblast centres and the transport links between them.',m.svg(),'Схема: ход связей ориентировочный; Манас — бывший Джалал-Абад; статус и границы населённых пунктов проверять по официальным данным.','Schematic: link routes are approximate; Manas is the former Jalal-Abad; check settlement status and boundaries against official data.','Города и главные связи: схема.','Cities and main links: schematic.')
# ---- 23-D / 23-H migration
def mig(m,both=True):
    def A(a,b,c,ru,en,w=4):
        (x1,y1),(x2,y2)=m.P(*a),m.P(*b)
        m.o.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{c}" stroke-width="{w}" marker-end="url(#arrow)" fill="none" stroke-opacity=".85"/>')
        if ru: m.o.append(T((x1+x2)/2,(y1+y2)/2-8,ru+' / '+en,'sm','middle','style="paint-order:stroke;stroke:#fff;stroke-width:3px;font-weight:700"'))
    return A
m=base(); A=mig(m)
A((76.0,41.6),(74.7,42.8),'#2e86ab','из сёл и гор в Чуйскую долину','from villages and mountains to Chuy Valley')
A((72.8,41.1),(74.2,42.8),'#2e86ab',None,None); A((79.0,42.0),(75.0,42.9),'#2e86ab',None,None)
A((72.5,40.6),(72.2,39.5),'#2e86ab',None,None)
A((74.0,43.2),(74.0,43.55),'#e67e22','трудовая миграция за рубеж','labour migration abroad',5)
A((71.2,40.6),(69.4,40.8),'#e67e22',None,None,5)
m.city('Bishkek'); m.city('Osh',dy=16)
m.legend([('внутренние перемещения','internal movements','#2e86ab'),('международная трудовая миграция','international labour migration','#e67e22')],x=60,y=700)
S('23-D','migration-schematic','Миграция и расселение (схема потоков)','Migration and settlement (flow schematic)','Внутренние перемещения и международная трудовая миграция.','Internal movements and international labour migration.',m.svg(),'Стрелки показывают направления, а не объёмы: ширина потоков не используется без сопоставимых количественных данных.','Arrows show directions, not volumes: flow width is not used without comparable quantitative data.','Миграция: направления потоков.','Migration: flow directions.')
# 23-H two panels
body=''
for i,(ttl_r,ttl_e,c) in enumerate([('Внутренние потоки','Internal flows','#2e86ab'),('Международные потоки','International flows','#e67e22')]):
    mm=KG(30+i*680,120,650,600,box=(69.0,80.6,38.0,44.5)).ctx().oblasts(opacity=.45).outline()
    mm.o.append(T(30+i*680,112,ttl_r+' / '+ttl_e,'lab'))
    AA=mig(mm)
    if i==0:
        for a,b in [((76.0,41.6),(74.7,42.8)),((72.8,41.1),(74.4,42.8)),((79,42),(75.1,42.9)),((72.5,40.6),(72.8,39.8))]: AA(a,b,c,None,None)
    else:
        for a,b in [((74.6,43.0),(74.6,44.3)),((71.5,40.3),(69.2,40.2)),((74.7,42.9),(77.2,44.0))]: AA(a,b,c,None,None,5)
    mm.city('Bishkek',dx=-8,anchor='end'); mm.city('Osh',dy=16)
    body+=mm.svg().replace('id="mc"','id="mc%d"'%i).replace('url(#mc)','url(#mc%d)'%i)
S('23-H','migration-layers','Миграционные потоки по слоям (схема)','Migration flows by layer (schematic)','Внутренние и международные потоки показаны раздельно.','Internal and international flows are shown separately.',body,'Только направления; без объёмов. Источники — миграционный баланс НСК и оценки МОМ (разные методики), как в тексте главы.','Directions only, no volumes. Sources: NSC migration balance and IOM estimates (different methods), as in the chapter text.','Миграция: внутренние и международные слои.','Migration: internal and international layers.')
# ---- 23-F regional pop choropleth
popm={'Osh':1438.5,'Jalal-Abad':1379.9,'Chuy':983.7,'Batken':605.3,'Ysyk-Köl':554.3,'Naryn':316.2,'Talas':282.9}
def col(v): 
    t=min(1,v/1500); r=int(255-(255-120)*t); g=int(235-(235-30)*t); b=int(220-(220-20)*t); return f'#{r:02x}{g:02x}{b:02x}'
pal={k:col(v) for k,v in popm.items()}; pal['Bishkek']='#ffffff'
m=KG().ctx().oblasts(pal=pal,opacity=1).outline(); lakes_rivers(m)
for k,(lo,la,ru,en,v) in {'b':(74.59,42.87,'Бишкек','Bishkek',1358.6),'o':(72.8,40.53,'Ош','Osh',484.9)}.items():
    r=math.sqrt(v)/2.6; x,y=m.P(lo,la)
    m.o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="#a93226" fill-opacity=".8" stroke="#fff" stroke-width="2"/>'+T(x+r+6,y+5,f'{ru} {v:,.1f}'.replace(',',' ').replace('.',',')+f' / {en}','sm','start','style="paint-order:stroke;stroke:#fff;stroke-width:3px;font-weight:700"'))
for k,v in popm.items():
    lo,la={'Osh':(72.9,40.15),'Jalal-Abad':(72.5,41.45),'Chuy':(74.6,43.3),'Batken':(70.6,39.9),'Ysyk-Köl':(78.4,41.75),'Naryn':(75.6,40.75),'Talas':(72.0,42.55)}[k]
    x,y=m.P(lo,la); m.o.append(T(x,y+30,OBL[k][0]+' / '+OBL[k][1],'sm','middle','style="fill:#fff;stroke:#243447;stroke-width:3px;paint-order:stroke"')+T(x,y+50,f'{v:,.1f}'.replace(',',' ').replace('.',',')+' тыс.','lab','middle','style="fill:#fff;stroke:#243447;stroke-width:4px;paint-order:stroke"'))
S('23-F','regional-population-2026','Население областей и городов, 01.01.2026','Population of regions and cities, 1 January 2026','Области закрашены по численности, Бишкек и Ош показаны кругами.','Regions are shaded by population; Bishkek and Osh are shown as circles.',m.svg(),'Источник: НСК (по таблице главы 23), тыс. чел. Города республиканского значения не входят в области; контур области в Natural Earth может включать территорию города.','Source: NSC (table in Chapter 23), thousand people. Cities of republican significance are not part of regions; the Natural Earth region outline may include the city area.','Население областей на 01.01.2026.','Regional population on 1 January 2026.')
# ---- 23-I Bishkek agglomeration / 25-F
def aggl():
    m=zoom((73.2,76.0,42.3,43.3)); 
    m.line([(73.2,43.0),(75.0,42.95),(76.0,42.85)],'#5b8db8',2.2)
    m.rng((73.4,42.4),(75.9,42.7),'Кыргызский хребет','Kyrgyz Range',off=(0,22))
    for k,dx,dy,an in [('Bishkek',10,-10,'start'),('Kant',10,-8,'start'),('Tokmok',10,-8,'start'),('Kara-Balta',-10,-8,'end'),('Kemin',10,-8,'start')]: m.city(k,dx=dx,dy=dy,anchor=an,r=7 if k=='Bishkek' else 5)
    return m
m=aggl(); m.blob(74.6,42.87,70,40,'#c0392b',None,None,.2)
S('23-I','bishkek-agglomeration','Бишкекская агломерация (схема)','Bishkek agglomeration (schematic)','Центральный город, спутники и связи вдоль Чуйской долины.','The central city, satellites and links along the Chuy Valley.',m.svg(),'Границы агломерации определяются методикой и здесь не проведены; кружок — условная зона влияния.','Agglomeration boundaries depend on methodology and are not drawn here; the circle is a conventional zone of influence.','Бишкекская агломерация: схема.','Bishkek agglomeration: schematic.')
m=aggl()
def A2(m,a,b,c,w=4):
    (x1,y1),(x2,y2)=m.P(*a),m.P(*b); m.o.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{c}" stroke-width="{w}" stroke-dasharray="9 6" marker-end="url(#arrow)" fill="none"/>')
for lo,la in [(74.85,42.89),(75.3,42.84),(73.85,42.81)]: A2(m,(lo,la),(74.6,42.87),'#c0392b')
m.text(75.0,43.15,'маятниковые потоки (направление)','commuting flows (direction)','sm','middle','#c0392b'); m.text(74.2,42.45,'пригородные сельхозземли и орошение','peri-urban farmland and irrigation','sm')
S('25-F','bishkek-chuy-commuting','Агломерация Бишкек–Чуй: связи и потоки','Bishkek–Chuy agglomeration: links and flows','Города-спутники, маятниковые потоки и окружающие земли.','Satellite towns, commuting flows and surrounding land.',m.svg(),'Схема без объёмов потоков: направления условные; границы — по методике.','Schematic without flow volumes: directions are conventional; boundaries follow the methodology.','Агломерация Бишкек–Чуй.','Bishkek–Chuy agglomeration.')
# 24-E Chuy valley
m=zoom((73.0,76.6,42.2,43.4)); m.rng((73.2,42.3),(76.3,42.7),'Кыргызский хребет','Kyrgyz Range',off=(0,22))
for a,b in [((73.9,42.86),(75.3,42.9)),((74.6,42.75),(75.3,42.83))]: m.line([a,b],'#5b8db8',1.6,'6 4')
for k,dx,dy,an in [('Bishkek',10,-10,'start'),('Kant',10,-8,'start'),('Tokmok',10,-8,'start'),('Kara-Balta',-10,-8,'end'),('Kemin',10,-8,'start')]: m.city(k,dx=dx,dy=dy,anchor=an)
m.text(74.7,43.3,'река Чу','Chu River','sm'); m.text(75.0,42.55,'оросительные каналы (схема)','irrigation canals (schematic)','sm','middle','#2874a6')
S('24-E','chuy-valley','Чуйская долина (схема)','Chuy Valley (schematic)','Река Чу, оросительные системы, города и хребет с юга.','The Chu River, irrigation systems, towns and the range to the south.',m.svg(),'Русло Чу и каналы показаны схематично; рельеф передан только положением хребта.','The Chu channel and canals are schematic; relief is conveyed only by the position of the range.','Чуйская долина: схема.','Chuy Valley: schematic.')
# 24-F Talas
m=zoom((70.6,73.6,41.7,43.1)); m.rng((70.7,41.95),(72.9,42.4),'Таласский Ала-Тоо','Talas Ala-Too',off=(0,-14)); m.line([(72.3,42.45),(71.2,42.75),(70.2,42.95)],w=2.6)
m.city('Talas',dx=10); m.dot(72.2,42.4,'Беш-Таш','Besh-Tash',6,'#2980b9',10,18); m.text(71.3,42.55,'река Талас','Talas River','sm'); m.text(70.9,42.95,'к Казахстану','toward Kazakhstan','sm','middle','#526579'); m.text(71.8,41.95,'пастбища','pastures','sm')
S('24-F','talas-basin','Бассейн Таласа (схема)','Talas basin (schematic)','Долина реки Талас, город Талас и связи с Казахстаном.','The Talas river valley, Talas city and links to Kazakhstan.',m.svg(),'Русло и положение пастбищ схематичны.','The channel and pasture positions are schematic.','Бассейн Таласа: схема.','Talas basin: schematic.')
# 24-G Issyk-Kul
m=zoom((75.8,80.6,41.3,43.3)); m.rng((76.6,42.8),(78.8,42.85),'Кюнгёй-Ала-Тоо','Kungey Ala-Too',off=(0,-16)); m.rng((76.9,42.15),(79.4,42.0),'Терскей-Ала-Тоо','Terskey Ala-Too',off=(0,20))
for k,dx,dy,an in [('Cholpon-Ata',-10,-10,'end'),('Karakol',10,-8,'start'),('Balykchy',-10,-6,'end'),('Kyzyl-Suu',10,14,'start')]: m.city(k,dx=dx,dy=dy,anchor=an)
m.dot(78.3,42.35,'Жети-Огуз','Jeti-Oguz',5,'#2980b9',8,14); m.dot(78.5,42.4,None,None,0); m.text(77.2,42.45,'Иссык-Куль','Issyk-Kul','lab')
S('24-G','issyk-kul-basin','Иссык-Кульская котловина (схема)','Issyk-Kul Basin (schematic)','Озеро, прибрежные города, хребты и туристические районы.','The lake, coastal towns, ranges and tourist areas.',m.svg(),'Границы ООПТ и чувствительные водно-болотные участки не показаны; для них нужны официальные данные.','Protected-area boundaries and sensitive wetlands are not shown; official data are needed for them.','Иссык-Кульская котловина: схема.','Issyk-Kul Basin: schematic.')
# 24-H Inner TS
m=zoom((73.4,78.6,40.2,42.7)); m.rng((74.8,41.1),(77.4,41.2),'Ат-Башы','At-Bashy',off=(0,14)); m.rng((74.6,41.75),(76.2,41.9),'Молдо-Тоо','Moldo-Too',off=(0,-10))
m.blob(75.1,41.8,22,14,'#3498db',None,None,.6); m.text(75.1,42.05,'Сон-Куль','Song-Kul'); m.blob(75.3,40.6,18,12,'#3498db',None,None,.6); m.text(75.3,40.38,'Чатыр-Куль','Chatyr-Kul')
m.dot(75.28,40.82,'Таш-Рабат','Tash-Rabat',5,'#c0392b',8,-4); m.dot(75.39,40.52,'Торугарт (перевал)','Torugart (pass)',5,'#c0392b',8,14)
for k,dx,dy,an in [('Naryn',10,16,'start'),('At-Bashy',10,14,'start'),('Kochkor',10,-8,'start'),('Kazarman',10,-8,'start')]: m.city(k,dx=dx,dy=dy,anchor=an)
S('24-H','inner-tien-shan','Внутренний Тянь-Шань (схема)','Inner Tien Shan (schematic)','Нарын, Сон-Куль, Чатыр-Куль, перевалы и Таш-Рабат.','Naryn, Song-Kul, Chatyr-Kul, passes and Tash-Rabat.',m.svg(),'Озёра показаны условными кругами; положение объектов ориентировочное.','Lakes are drawn as conventional circles; positions of features are approximate.','Внутренний Тянь-Шань: схема.','Inner Tien Shan: schematic.')
# 24-I Jalal-Abad
m=zoom((70.6,74.6,40.4,42.5)); 
for k,dx,dy,an in [('Manas',10,14,'start'),('Toktogul',10,-8,'start'),('Tash-Kumyr',-10,-8,'end'),('Mailuu-Suu',-10,14,'end'),('Kazarman',10,-8,'start')]: m.city(k,dx=dx,dy=dy,anchor=an)
m.dot(72.93,41.33,'Арсланбоб','Arslanbob',6,'#27ae60',10,-6); m.dot(71.95,41.83,'Сары-Челек','Sary-Chelek',6,'#27ae60',-10,-6,'end'); m.text(72.9,42.0,'Токтогульское водохранилище','Toktogul Reservoir','sm'); m.rng((70.7,41.5),(72.3,41.85),'Чаткальский хребет','Chatkal Range',off=(0,-12))
S('24-I','jalal-abad-region','Джалал-Абадская область (схема)','Jalal-Abad Region (schematic)','Долина Нарына, Токтогульское водохранилище, Чаткал, Арсланбоб, Сары-Челек и город Манас.','The Naryn valley, Toktogul Reservoir, Chatkal, Arslanbob, Sary-Chelek and Manas city.',m.svg(),'Манас — прежнее название Джалал-Абад; подпись «Манас (б. Джалал-Абад)» принята по тексту главы.','Manas is the former Jalal-Abad; the label follows the chapter text.','Джалал-Абадская область: схема.','Jalal-Abad Region: schematic.')
# 24-J Osh
m=zoom((71.2,75.0,38.9,41.0)); 
for k,dx,dy,an in [('Osh',-10,-8,'end'),('Kara-Suu',10,-4,'start'),('Uzgen',10,-8,'start'),('Nookat',-10,14,'end'),('Sary-Tash',10,14,'start')]: m.city(k,dx=dx,dy=dy,anchor=an)
m.text(72.6,40.8,'Ферганская долина','Fergana Valley'); m.text(73.0,39.95,'Алайская долина','Alay Valley'); m.text(73.5,39.5,'Заалайский хребет','Trans-Alay'); m.rng((70.5,39.85),(73.8,39.75),'Алайский хребет','Alay Range',off=(0,-12)); m.dot(72.88,39.34,'пик Ибн Сина','Ibn Sina Peak',6,'#7b241c',8,-6)
S('24-J','osh-region','Ошская область (схема)','Osh Region (schematic)','Ферганская, Алайская и Чон-Алайская долины; город Ош отдельно.','The Fergana, Alay and Chon-Alay valleys; Osh city shown separately.',m.svg(),'Ош — город республиканского значения, не входящий в область; контур области в Natural Earth может его включать.','Osh is a city of republican significance outside the region; the Natural Earth outline may include it.','Ошская область: схема.','Osh Region: schematic.')
# 24-K Batken
m=zoom((69.2,72.6,39.4,40.7))
for k,dx,dy,an in [('Batken',10,14,'start'),('Isfana',-10,-8,'end'),('Kyzyl-Kiya',10,-8,'start'),('Kadamjai',10,14,'start')]: m.city(k,dx=dx,dy=dy,anchor=an)
m.rng((69.4,39.65),(71.6,39.75),'Туркестанский хребет','Turkestan Range',off=(0,16)); m.text(70.4,40.4,'Ферганская долина (юг)','Fergana Valley (south)','sm')
S('24-K','batken-region','Баткенская область (схема)','Batken Region (schematic)','Рельеф, города и водные объекты; сложные участки границы не показаны.','Relief, towns and water bodies; complex border segments are not shown.',m.svg(),'Сложные участки границ и анклавы намеренно не прорисованы: их берут только из проверенного официального источника.','Complex border segments and enclaves are deliberately not drawn: use only a verified official source for them.','Баткенская область: схема.','Batken Region: schematic.')
# 24-A seven regions
m=KG().ctx().oblasts(opacity=.9).outline(); lakes_rivers(m); m.label_obl()
for k,dx,dy,an in [('Bishkek',-10,-8,'end'),('Osh',-10,16,'end'),('Manas',-10,16,'end'),('Karakol',10,-8,'start'),('Naryn',10,16,'start'),('Talas',-10,-8,'end'),('Batken',10,16,'start')]: m.city(k,dx=dx,dy=dy,anchor=an,r=7 if k in('Bishkek','Osh') else 5,fill='#c0392b' if k in('Bishkek','Osh') else '#243447')
m.legend([('города республиканского значения (вне областей)','cities of republican significance (outside regions)','#c0392b'),('центры областей','regional centres','#243447')],x=60,y=700)
S('24-A','seven-regions-map','Семь областей Кыргызстана','The seven regions of Kyrgyzstan','Области, их центры и города республиканского значения.','Regions, their centres and cities of republican significance.',m.svg(),'Границы — Natural Earth (учебная точность); Бишкек и Ош не входят в Чуйскую и Ошскую области. Для точных границ — официальные геоданные.','Boundaries from Natural Earth (teaching accuracy); Bishkek and Osh are outside Chuy and Osh regions. Use official geodata for exact boundaries.','Семь областей и города республиканского значения.','Seven regions and cities of republican significance.')
# 24-B seven profiles
rows=[('Баткенская','Batken',17.0,605.3,35.6),('Джалал-Абадская','Jalal-Abad',33.7,1379.9,40.9),('Иссык-Кульская','Issyk-Kul',43.1,554.3,12.9),('Нарынская','Naryn',45.2,316.2,7.0),('Ошская','Osh',29.0,1438.5,49.6),('Таласская','Talas',11.4,282.9,24.8),('Чуйская','Chuy',20.2,983.7,48.7)]
body=T(60,118,'Область / Region','lab')+T(430,118,'Площадь, тыс. км²','lab','middle')+T(700,118,'Население 01.01.2026, тыс.','lab','middle')+T(1000,118,'Плотность, чел./км² (расчётная)','lab','middle')
for i,(a,b,ar,p,d) in enumerate(rows):
    y=135+i*80; body+=box(40,y,1320,68,'#f1f4f6' if i%2 else '#e5efe3')+T(60,y+30,a,'t')+T(60,y+54,b,'s')
    body+=f'<rect x="340" y="{y+22}" width="{ar/45.2*180:.0f}" height="24" fill="#7f8c8d"/>'+T(340+ar/45.2*180+6,y+40,f'{ar:.1f}'.replace('.',','),'s')
    body+=f'<rect x="620" y="{y+22}" width="{p/1438.5*200:.0f}" height="24" fill="#2e86ab"/>'+T(620+p/1438.5*200+6,y+40,f'{p:,.1f}'.replace(',',' ').replace('.',','),'s')
    body+=f'<rect x="920" y="{y+22}" width="{d/49.6*220:.0f}" height="24" fill="#c0392b"/>'+T(920+d/49.6*220+6,y+40,f'{d:.1f}'.replace('.',','),'s')
S('24-B','regional-profiles','Семь областей: площадь, население, плотность','Seven regions: area, population, density','Единый формат сравнения областей.','A consistent format for comparing regions.',body,'Источник: НСК, таблица главы 24; население на 01.01.2026 без Бишкека и Оша; плотность расчётная.','Source: NSC, Chapter 24 table; population on 1 January 2026 excluding Bishkek and Osh; density is calculated.','Области: площадь, население, плотность.','Regions: area, population, density.')
# 24-D physical + 24-C risk + 24-L corridors
m=KG().ctx().oblasts(op:=0.0,stroke='#a9b6c2') if False else KG().ctx().oblasts(pal={},opacity=.0,stroke='#b6bfc8').outline(); lakes_rivers(m)
for k,a,b,ru,en,sy,off in RNG: m.rng(a,b,ru,en,off=off)
for lo,la,rx,ry,ang,ru,en in [(80.0,42.15,60,22,-10,'ледники','glaciers'),(72.6,39.5,90,14,0,'ледники','glaciers')]: m.blob(lo,la,rx,ry,'#5dade2',None,None,.5,ang)
m.text(77.2,42.4,'Иссык-Куль','Issyk-Kul','lab'); m.text(74.5,43.2,'Чуйская долина','Chuy Valley'); m.text(72.0,40.75,'Ферганская долина','Fergana Valley'); m.text(76.1,41.55,'Нарынская впадина','Naryn Basin')
S('24-D','physical-map-regions','Физико-географическая схема (административные границы вторичны)','Physical-geography schematic (administrative boundaries secondary)','Хребты, долины, котловины, ледники, реки и озёра.','Ranges, valleys, basins, glaciers, rivers and lakes.',m.svg(),FR[FR.index('Основа'):FR.index('Учебная')]+'Хребты показаны линиями; рельеф не передан.',FE[:FE.index('Teaching')]+'Ranges are lines; relief is not rendered.','Физико-географическая схема Кыргызстана.','Physical-geography schematic of Kyrgyzstan.')
m=base()
m.blob(74.7,42.2,70,15,'#2e86ab','Селевые бассейны','Debris-flow basins',.3); m.blob(72.8,40.2,150,22,'#8e5b2c','Оползни, сели','Landslides, debris flows',.3); m.blob(72.8,41.1,120,30,'#8e5b2c',None,None,.25)
m.blob(70.8,39.9,70,20,'#e67e22','Засушливые территории','Arid territories',.35); m.blob(76.0,42.55,40,10,'#c0392b',None,None,.0)
m.line([(74.6,42.87),(74.3,42.5),(73.8,42.3),(73.0,41.9),(72.7,41.6),(72.2,41.35),(72.98,40.93),(72.8,40.53)],'#c0392b',3,'8 5'); m.text(73.6,42.15,'Бишкек–Ош: уязвимые перевалы','Bishkek–Osh: vulnerable passes','sm','middle','#c0392b')
m.legend([('сели, оползни','debris flows, landslides','#8e5b2c'),('засушливые территории','arid territories','#e67e22'),('транспортный коридор','transport corridor','#c0392b')],x=60,y=700)
S('24-C','regional-risk-schematic','Региональные природные риски (качественная схема)','Regional natural risks (qualitative schematic)','Районы типичных опасностей и уязвимый транспортный коридор.','Areas of typical hazards and a vulnerable transport corridor.',m.svg(),'Схема не является картой риска: опасность, экспозиция и уязвимость нужно оценивать отдельно.','Not a risk map: hazard, exposure and vulnerability must be assessed separately.','Региональные риски: качественная схема.','Regional risks: qualitative schematic.')
def corr(plan=True):
    m=base()
    m.line([(74.6,42.87),(74.3,42.5),(73.8,42.3),(73.0,41.9),(72.7,41.6),(72.2,41.35),(72.98,40.93),(72.8,40.53)],'#c0392b',4)
    m.line([(74.6,42.87),(76.2,42.46),(77.1,42.65),(78.4,42.49)],'#c0392b',4)
    m.line([(72.8,40.53),(73.25,39.73),(73.9,39.7)],'#c0392b',4); m.line([(76.0,41.43),(75.39,40.52)],'#c0392b',4); m.line([(76.2,42.46),(76.0,41.43)],'#c0392b',4)
    m.line([(74.6,42.87),(76.2,42.46)],'#243447',3,'2 8'); m.line([(74.6,42.87),(71.0,43.3)],'#243447',3,'2 8')
    m.line([(75.39,40.52),(74.0,41.4),(72.98,40.93)],'#8e44ad',4,'12 8')
    for lo,la,ru,en in [(75.39,40.52,'Торугарт','Torugart'),(73.9,39.7,'Иркештам','Irkeshtam'),(72.86,40.7,'Кара-Суу (граница)','Kara-Suu (border)')]: m.dot(lo,la,ru,en,6,'#27ae60',8,16)
    m.city('Bishkek'); m.city('Osh',dy=16); m.city('Balykchy',dx=-8,anchor='end',dy=-8)
    m.legend([('автодороги (схема)','main roads (schematic)','#c0392b'),('железная дорога (схема)','railway (schematic)','#243447'),('проектируемая: Китай–Кыргызстан–Узбекистан (ориентировочно)','planned: China–Kyrgyzstan–Uzbekistan (approximate)','#8e44ad'),('пункты пропуска (примеры)','border crossings (examples)','#27ae60')],x=60,y=600)
    return m
m=corr()
S('24-L','transport-corridors','Транспортно-экономические коридоры (схема)','Transport and economic corridors (schematic)','Главные дороги, железные дороги, пункты пропуска и проектируемая линия.','Main roads, railways, border crossings and the planned line.',m.svg(),'Ход линий ориентировочный; действующие и проектируемые объекты различены стилем линии; точные трассы — по официальным данным.','Line routes are approximate; existing and planned objects differ by line style; exact routes come from official data.','Транспортные коридоры: схема.','Transport corridors: schematic.')
m=corr()
S('25-B','transport-network','Транспортная сеть Кыргызстана (схема)','Transport network of Kyrgyzstan (schematic)','Основные автодороги, железные дороги, пункты пропуска и строящаяся линия.','Main roads, railways, border crossings and the line under development.',m.svg(),'Ход линий ориентировочный; аэропорты на схеме не показаны, строящаяся/проектируемая линия показана пунктиром.','Line routes are approximate; airports are not shown; the planned/under-construction line is dashed.','Транспортная сеть: схема.','Transport network: schematic.')
print('m3a ok')
