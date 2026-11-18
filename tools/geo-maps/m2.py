from m1 import *
def base(**k): m=kg(); lakes_rivers(m); return m
def S(id_,slug,ru,en,dru,den,body,fru,fen,cru,cen): save(id_,slug,ru,en,dru,den,wrap(ru,en,dru+' / '+den,body,fru,fen),cru,cen)
CITY3=lambda m:(m.city('Bishkek'),m.city('Osh',dy=16),m.city('Naryn',dy=16),m.city('Karakol',dy=-8))
# 19-A climatic regions
m=base()
m.blob(72.4,40.75,170,48,'#e67e22','Ферганская: тёплая, сухая','Fergana: warm, dry',.3)
m.blob(74.7,42.75,130,26,'#f1c40f','Чуйская: континентальная','Chuy: continental',.3)
m.blob(77.2,42.35,200,20,'#3498db','Иссык-Кульская: смягчена озером','Issyk-Kul: moderated by the lake',.3)
m.blob(75.7,41.35,160,26,'#7f8c8d','Внутренний Тянь-Шань: холодная, сухая','Inner Tien Shan: cold, dry',.3)
m.blob(72.2,42.4,70,22,'#2ecc71','Таласская','Talas',.3)
m.blob(73.2,39.95,120,24,'#9b59b6','Алай: высокогорная','Alay: high-mountain',.3)
m.legend([('Районы выделены по основным климатическим различиям;','climate regions are qualitative and do not equal physical-geographic regions','#fbfcfe')],x=60,y=700)
CITY3(m)
S('19-A','climatic-regions','Климатические районы Кыргызстана (качественная схема)','Climatic regions of Kyrgyzstan (qualitative schematic)','Основные климатические районы долин и котловин.','Main climatic regions of valleys and basins.',m.svg(),'Климатические районы не совпадают с физико-географическим районированием; границы условны, значения не приводятся.','Climatic regions do not coincide with physical-geographic regions; boundaries are conventional and no values are given.','Качественная схема климатических районов.','Qualitative schematic of climatic regions.')
# 19-G temperature
m=base()
for lo,la,rx,ry,c,ru,en in [(72.4,40.7,170,40,'#e74c3c','Теплее: Ферганская долина','Warmer: Fergana Valley'),(74.8,42.8,130,24,'#f39c12','Тепло: Чуйская долина','Warm: Chuy Valley'),(77.2,42.4,190,18,'#f7dc6f','Умеренно: Иссык-Кульская котловина','Moderate: Issyk-Kul Basin'),(76.0,41.2,200,28,'#85c1e9','Холоднее: Внутренний Тянь-Шань','Colder: Inner Tien Shan'),(79.0,41.3,100,28,'#2e86c1','Очень холодно: высокогорье','Very cold: high mountains')]:
    m.blob(lo,la,rx,ry,c,ru,en,.45)
m.text(74.0,43.45,'Температура убывает с высотой в среднем около 0,6 °C на 100 м','Temperature falls with height by about 0.6 °C per 100 m on average','sm')
CITY3(m)
S('19-G','temperature-zones-schematic','Температурные зоны Кыргызстана (качественная схема)','Temperature zones of Kyrgyzstan (qualitative schematic)','Тепло в низких долинах, холод в высокогорье.','Warm low valleys, cold high mountains.',m.svg(),'Схема без измеренных значений: единый климатический период, станции и метод интерполяции нужны для настоящей карты.','Schematic without measured values: a real map needs a common climatic period, stations and an interpolation method.','Качественная схема температурных зон.','Qualitative schematic of temperature zones.')
# 19-B precipitation + orographic
m=KG(30,100,760,640).ctx().oblasts(opacity=.4).outline(); lakes_rivers(m)
m.blob(71.9,41.3,95,50,'#2980b9','Больше осадков','Wetter',.35); m.blob(76.0,42.4,120,18,'#e0b04a','Меньше','Drier',.35); m.blob(76.0,41.3,110,26,'#e0b04a','Меньше: внутренние впадины','Drier: inner basins',.3)
m.blob(72.9,39.5,90,24,'#2980b9','Алай: выше','Alay: wetter',.3)
body=m.svg()
x0=830
body+=f'<rect x="{x0}" y="110" width="540" height="560" rx="14" fill="#fff" stroke="#c5ced6"/>'
body+=T(x0+20,140,'Орографический подъём воздуха','lab')+T(x0+20,160,'Orographic lift of air','sm','start','style="fill:#526579"')
body+=f'<path d="M{x0+20} 560 L{x0+150} 560 L{x0+270} 260 L{x0+390} 560 L{x0+520} 560 Z" fill="#b59a7a" stroke="#6b5a45" stroke-width="2"/>'
body+=f'<path d="M{x0+30} 470 C{x0+120} 470 {x0+200} 330 {x0+250} 250" class="arr" style="stroke:#2e86ab"/>'
body+=f'<path d="M{x0+300} 270 C{x0+360} 330 {x0+420} 400 {x0+500} 420" class="arr" style="stroke:#c0392b"/>'
body+=f'<ellipse cx="{x0+215}" cy="215" rx="70" ry="26" fill="#dfe6ec" stroke="#8a99a8"/>'
body+=T(x0+120,600,'Наветренный склон: больше осадков','sm')+T(x0+120,618,'Windward slope: more precipitation','sm','start','style="fill:#526579"')
body+=T(x0+330,500,'Дождевая тень','sm')+T(x0+330,518,'Rain shadow','sm','start','style="fill:#526579"')
body+=T(x0+20,650,'Влажный воздух поднимается, охлаждается, отдаёт влагу.','sm')+T(x0+20,668,'Moist air rises, cools and sheds its moisture.','sm','start','style="fill:#526579"')
S('19-B','precipitation-orographic','Осадки и орографический эффект (качественная схема)','Precipitation and the orographic effect (qualitative schematic)','Влажные наветренные склоны и сухие внутренние котловины.','Wet windward slopes and dry inner basins.',body,'Интерполированные значения не показаны; схема отличает общие закономерности от прямых измерений.','Interpolated values are not shown; the schematic conveys general patterns, not direct measurements.','Осадки по рельефу: качественно.','Precipitation and relief: qualitative.')
# 20-A glaciers (NE)
m=KG().ctx().oblasts(opacity=.25).outline()
for lo,la,rx,ry,ang,ru,en in [(80.0,42.15,70,28,-10,'Хан-Тенгри, Иныльчек','Khan Tengri, Inylchek'),(78.2,41.8,60,22,-10,'Ак-Шыйрак','Ak-Shyirak'),(78.0,42.1,90,13,0,'Терскей-Ала-Тоо','Terskey Ala-Too'),(77.8,40.95,130,14,-6,'Кокшаал-Тоо','Kokshaal-Too'),(74.5,42.45,110,13,8,'Кыргызский хребет','Kyrgyz Range'),(72.6,39.5,120,20,0,'Алай, Заалай','Alay, Trans-Alay'),(72.4,42.3,55,12,12,'Таласский Ала-Тоо','Talas Ala-Too')]:
    m.blob(lo,la,rx,ry,'#5dade2',ru,en,.55,ang)
m.water(); m.legend([('районы оледенения (схема)','glaciated areas (schematic)','#5dade2')],x=60,y=700)

m.city('Bishkek'); m.city('Osh',dy=16)
S('20-A','glaciated-areas','Ледниковые районы Кыргызстана','Glaciated areas of Kyrgyzstan','Основные районы современного оледенения.','Main areas of present-day glaciation.',m.svg(),'Схема районов оледенения, не инвентаризация ледников: контуры, порог учёта, дату и метод берут из каталогов (например, GLIMS, RGI).','Schematic of glaciated areas, not a glacier inventory: outlines, size threshold, date and method come from catalogues (e.g. GLIMS, RGI).','Районы оледенения: схема.','Glaciated areas: schematic.')
# 20-B basins
m=KG().ctx().oblasts(opacity=.35).outline(); lakes_rivers(m)
def arr(m,a,b,c,ru,en):
    (x1,y1),(x2,y2)=m.P(*a),m.P(*b)
    m.o.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{c}" stroke-width="5" marker-end="url(#arrow)" fill="none" stroke-opacity=".8"/>')
    m.o.append(T((x1+x2)/2,(y1+y2)/2-10,ru+' / '+en,'sm','middle','style="paint-order:stroke;stroke:#fff;stroke-width:3px;font-weight:700"'))
arr(m,(72.8,41.0),(70.2,40.9),'#2e86ab','Нарын → Сырдарья → Узбекистан','Naryn → Syr Darya → Uzbekistan')
arr(m,(74.2,42.7),(71.4,43.1),'#27ae60','Чу → Казахстан','Chu → Kazakhstan')
arr(m,(72.4,42.4),(70.4,42.9),'#8e44ad','Талас → Казахстан','Talas → Kazakhstan')
arr(m,(78.5,41.0),(80.3,40.6),'#e67e22','Аксу, Сарыджаз → Тарим (Китай)','Aksu, Sary-Jaz → Tarim (China)')
arr(m,(73.0,39.6),(72.4,39.0),'#c0392b','Кызыл-Суу → Вахш → Амударья','Kyzyl-Suu → Vakhsh → Amu Darya')
m.blob(77.2,42.45,60,8,'#3498db',None,None,.0)
m.text(77.2,42.1,'Иссык-Куль: бессточный','Issyk-Kul: endorheic','sm')
m.city('Bishkek'); m.city('Osh',dy=16)
S('20-B','river-basins-flow-directions','Речные бассейны и направления стока','River basins and flow directions','Куда уходит вода Кыргызстана: бассейны Сырдарьи, Чу, Таласа, Тарима и Амударьи.','Where Kyrgyzstan\'s water goes: the Syr Darya, Chu, Talas, Tarim and Amu Darya basins.',m.svg(),'Стрелки показывают общее направление стока, а не точные русла и водоразделы; реки Чу и Талас проведены схематично.','Arrows show general flow direction, not exact channels or divides; the Chu and Talas rivers are schematic lines.','Направления стока по основным бассейнам.','Flow directions of the main basins.')
# 20-G hydrograph
import math
def curve(fn): return ' '.join(('M' if i==0 else 'L')+f'{100+i*100:.0f} {fn(i):.0f}' for i in range(12))
snow=lambda i:620-380*math.exp(-((i-4.3)**2)/2.2)
gl=lambda i:620-300*math.exp(-((i-6.5)**2)/2.6)
rain=lambda i:620-120*math.exp(-((i-3.2)**2)/3)
body='<line x1="90" y1="620" x2="1330" y2="620" stroke="#44586b" stroke-width="2"/><line x1="90" y1="140" x2="90" y2="620" stroke="#44586b" stroke-width="2"/>'
for i,mn in enumerate('Я Ф М А М И И А С О Н Д'.split()):
    pass
for i,(ru,en) in enumerate([('янв','Jan'),('фев','Feb'),('мар','Mar'),('апр','Apr'),('май','May'),('июн','Jun'),('июл','Jul'),('авг','Aug'),('сен','Sep'),('окт','Oct'),('ноя','Nov'),('дек','Dec')]):
    body+=T(100+i*100,646,ru+'/'+en,'sm','middle')
body+=f'<path d="{curve(snow)}" fill="none" stroke="#2e86c1" stroke-width="5"/><path d="{curve(gl)}" fill="none" stroke="#17a589" stroke-width="5"/><path d="{curve(rain)}" fill="none" stroke="#8e44ad" stroke-width="5" stroke-dasharray="10 6"/>'
body+=T(560,200,'Снеговое питание: пик в мае–июне','lab','middle','style="fill:#2e86c1"')+T(560,222,'Snowmelt: peak in May–June','sm','middle')
body+=T(930,330,'Ледниковое питание: пик в июле–августе','lab','middle','style="fill:#17a589"')+T(930,352,'Glacier melt: peak in July–August','sm','middle')
body+=T(430,520,'Дожди: весна и начало лета','lab','middle','style="fill:#8e44ad"')+T(430,542,'Rain: spring and early summer','sm','middle')
body+=T(80,130,'Расход воды (условные единицы) / Discharge (arbitrary units)','sm')
S('20-G','hydrograph-schematic','Сезонный сток горной реки (условная схема)','Seasonal flow of a mountain river (schematic)','Вклад снегового, ледникового и дождевого питания по месяцам.','Contribution of snowmelt, glacier melt and rain by month.',body,'Условная схема без данных конкретного створа: форма и сроки пиков зависят от высоты бассейна и доли ледников.','Schematic without data from a specific gauge: peak shape and timing depend on basin altitude and glacier share.','Сезонный сток горной реки: условная схема.','Seasonal flow of a mountain river: schematic.')
# 21-A biogeography / belts schematic map
m=base()
for lo,la,rx,ry,c,ru,en in [(72.4,40.7,160,40,'#e6b85c','Пустыни и полупустыни, лёссовые предгорья','Deserts, semi-deserts, loess foothills'),(74.9,42.7,120,20,'#c8d86a','Степи','Steppes'),(76.2,41.2,180,26,'#7fb069','Высокогорные степи и луга','High-mountain steppes and meadows'),(72.0,41.5,110,32,'#2e8b57','Ореховые и плодовые леса, арчовники','Walnut-fruit forests and juniper'),(77.9,42.55,110,16,'#1e6b45','Еловые леса Тянь-Шаня','Tien Shan spruce forests')]:
    m.blob(lo,la,rx,ry,c,ru,en,.4)
CITY3(m)
S('21-A','biogeography-belts','Биогеографические комплексы Кыргызстана (схема)','Biogeographic complexes of Kyrgyzstan (schematic)','Основные природные комплексы гор и котловин.','Main natural complexes of mountains and basins.',m.svg(),'Границы комплексов условны и не совпадают с областями; настоящую карту строят по геоботаническим данным.','Complex boundaries are conventional and do not follow oblasts; a real map is built from geobotanical data.','Природные комплексы Кыргызстана: схема.','Natural complexes of Kyrgyzstan: schematic.')
# 21-G vegetation types
m=base()
for lo,la,rx,ry,c,ru,en in [(72.4,40.7,170,34,'#e6b85c','Полупустыня','Semi-desert'),(74.9,42.75,130,18,'#c8d86a','Степь','Steppe'),(72.0,41.5,110,32,'#2e8b57','Орехово-плодовые леса','Walnut-fruit forests'),(73.9,42.3,120,14,'#1e6b45','Ель, арча','Spruce, juniper'),(76.2,41.3,170,24,'#7fb069','Горные степи','Mountain steppes'),(78.3,41.9,120,24,'#a8d5ba','Альпийские луга','Alpine meadows')]:
    m.blob(lo,la,rx,ry,c,ru,en,.42)
CITY3(m)
S('21-G','vegetation-types','Основные типы растительности (схема)','Main vegetation types (schematic)','Типы растительности по природным поясам.','Vegetation types by natural belts.',m.svg(),'Типы растительности показаны по природным, а не административным границам; контуры схематичны, источник геоданных для детальной карты нужно указывать отдельно.','Vegetation types follow natural, not administrative, boundaries; outlines are schematic and a detailed map needs a named geodata source.','Типы растительности: схема.','Vegetation types: schematic.')
# 21-D fauna habitats
m=base()
for lo,la,rx,ry,c,ru,en in [(72.0,41.6,120,34,'#2e8b57','Лесные виды: медведь, марал','Forest species: bear, maral'),(78.4,41.2,170,30,'#7f8c8d','Высокогорье: снежный барс, архар, кийик','High mountains: snow leopard, argali, ibex'),(77.2,42.45,140,12,'#3498db','Водоплавающие птицы Иссык-Куля','Waterbirds of Issyk-Kul'),(75.2,41.2,90,12,'#16a085','Сон-Куль, Чатыр-Куль: водно-болотные места','Song-Kul, Chatyr-Kul wetlands')]:
    m.blob(lo,la,rx,ry,c,ru,en,.38)
CITY3(m)
S('21-D','fauna-habitats','Местообитания ключевых групп фауны (обобщённо)','Habitats of key fauna groups (generalised)','Крупные районы обитания; точные координаты редких видов не показаны.','Broad habitat areas; exact locations of rare species are not shown.',m.svg(),'Чувствительные координаты редких видов намеренно обобщены; схема не заменяет карты ареалов.','Sensitive coordinates of rare species are deliberately generalised; the schematic does not replace range maps.','Местообитания фауны: обобщённая схема.','Fauna habitats: generalised schematic.')
# 21-E / 22-B protected areas markers
def pa(m):
    for lo,la,ru,en,c in [(71.95,41.83,'Сары-Челек','Sary-Chelek','#27ae60'),(75.0,41.8,'Каратал-Жапырык (Сон-Куль)','Karatal-Zhapyryk (Song-Kul)','#27ae60'),(75.3,40.6,'Каратал-Жапырык (Чатыр-Куль)','Karatal-Zhapyryk (Chatyr-Kul)','#27ae60'),(74.5,42.55,'Ала-Арча','Ala-Archa','#2980b9'),(78.5,42.4,'Каракол','Karakol','#2980b9'),(76.4,42.8,'Чон-Кемин','Chon-Kemin','#2980b9'),(72.2,42.4,'Беш-Таш','Besh-Tash','#2980b9'),(72.45,40.3,'Кыргыз-Ата','Kyrgyz-Ata','#2980b9')]:
        m.dot(lo,la,ru,en,6,c,8,-6)
m=base(); pa(m); m.text(77.2,42.2,'Иссык-Кульский заповедник (побережье)','Issyk-Kul Reserve (coast)','sm')
m.legend([('заповедник','state nature reserve','#27ae60'),('природный парк','nature park','#2980b9')],x=60,y=700)
S('21-E','protected-areas-examples','Охраняемые территории: примеры (схема)','Protected areas: examples (schematic)','Примеры заповедников и природных парков.','Examples of nature reserves and nature parks.',m.svg(),'Показаны отдельные примеры точками; официальные границы, категории и дату геоданных нужно брать из реестра ООПТ.','Selected examples as points; official boundaries, categories and geodata date must come from the protected-area register.','Примеры ООПТ точками.','Examples of protected areas as points.')
m=base(); pa(m); m.dot(77.2,42.45,'Иссык-Кульский заповедник','Issyk-Kul Reserve',5,'#27ae60',10,22)
m.legend([('заповедник','state nature reserve','#27ae60'),('природный парк','nature park','#2980b9')],x=60,y=700)
S('22-B','protected-network-examples','Сеть ООПТ Кыргызстана: примеры по категориям','Protected-area network of Kyrgyzstan: examples by category','Заповедники и природные парки как отдельные категории.','Nature reserves and nature parks as separate categories.',m.svg(),'Это не полная карта сети: заказники, памятники природы и точные границы не показаны; нужен официальный реестр.','Not a full network map: sanctuaries, natural monuments and exact boundaries are not shown; the official register is required.','Категории ООПТ: примеры.','Protected-area categories: examples.')
# 22-E parks
m=base()
for lo,la,ru,en in [(74.5,42.55,'Ала-Арча','Ala-Archa'),(78.5,42.4,'Каракол','Karakol'),(76.4,42.8,'Чон-Кемин','Chon-Kemin'),(72.2,42.4,'Беш-Таш','Besh-Tash'),(72.45,40.3,'Кыргыз-Ата','Kyrgyz-Ata')]:
    m.dot(lo,la,ru,en,7,'#2980b9',9,-8)
CITY3(m)
S('22-E','nature-parks-examples','Государственные природные парки: примеры','State nature parks: examples','Расположение нескольких природных парков.','Locations of several nature parks.',m.svg(),'Показаны отдельные примеры; официальные границы и категории — в реестре ООПТ.','Selected examples only; official boundaries and categories are in the protected-area register.','Примеры природных парков.','Examples of nature parks.')
# 22-A natural belts (altitude schematic)
body=''
bands=[('Ледники и снега','Glaciers and snow','#e8f6ff',130),('Альпийские и субальпийские луга','Alpine and subalpine meadows','#a8d5ba',230),('Леса: ель, арча','Forests: spruce, juniper','#2e8b57',330),('Степи и лугостепи','Steppes and meadow steppes','#c8d86a',430),('Полупустыни и пустыни','Semi-deserts and deserts','#e6b85c',530)]
for ru,en,c,y in bands:
    body+=f'<rect x="120" y="{y}" width="900" height="90" fill="{c}" stroke="#647789"/>'+T(140,y+40,ru,'t')+T(140,y+66,en,'s')
body+=arrow(1100,560,1100,140)+T(1120,150,'выше / higher','s')+T(1120,560,'ниже / lower','s')
body+=T(1120,300,'Порядок поясов верный; высоты границ','sm')+T(1120,320,'зависят от склона и района','sm')+T(1120,350,'Order of belts is general; belt limits','sm')+T(1120,370,'depend on slope and region','sm')
S('22-A','natural-belts','Природные пояса Кыргызстана (схема)','Natural belts of Kyrgyzstan (schematic)','Смена природных поясов от долин к вершинам.','Change of natural belts from valleys to summits.',body,'Показан общий порядок поясов; высоты границ не приводятся, они зависят от экспозиции склона, района и увлажнения.','General order of belts; belt altitudes are omitted because they depend on slope aspect, region and moisture.','Природные пояса: общий порядок.','Natural belts: general order.')
# 22-D corridors & designations
body=''
cols=[('Национальный статус','National status',['Заповедник','Природный парк','Заказник','Памятник природы'],['Nature reserve','Nature park','Sanctuary','Natural monument'],'#e5efe3'),('Международное признание','International recognition',['Биосферный резерват UNESCO (Сары-Челек)','Рамсарское угодье','Всемирное наследие UNESCO'],['UNESCO biosphere reserve (Sary-Chelek)','Ramsar wetland','UNESCO World Heritage'],'#e4eff6')]
for i,(hr,he,ru,en,c) in enumerate(cols):
    x=80+i*660
    body+=box(x,120,600,540,c)+T(x+24,160,hr,'t')+T(x+24,186,he,'s','start','style="fill:#526579"')
    for j in range(len(ru)): body+=T(x+30,240+j*90,'• '+ru[j],'s')+T(x+44,264+j*90,en[j],'sm','start','style="fill:#526579"')
body+=T(80,700,'Эти статусы не заменяют друг друга: у территории может быть один, другой или оба.','s')+T(80,724,'These statuses do not replace each other: an area may hold one, the other or both.','s','start','style="fill:#526579"')
S('22-D','national-vs-international-status','Национальный статус и международное признание','National status versus international recognition','Две разные системы признания природных территорий.','Two separate systems of recognising natural areas.',body,'Схема без карты: показывает, что национальный статус и международные списки различаются; конкретные территории проверять по перечням.','A non-map schematic: it shows that national status and international listings differ; check specific areas against the lists.','Национальный статус и международное признание.','National status and international recognition.')
# 22-I threats matrix
th=[('Пожары','Fires'),('Выпас','Grazing'),('Инфраструктура','Infrastructure'),('Инвазивные виды','Invasive species'),('Загрязнение','Pollution'),('Климат','Climate change')]
ty=[('Леса','Forests'),('Луга','Meadows'),('Озёра и водно-болотные','Lakes, wetlands'),('Высокогорье','High mountains')]
body='';cw=170
body+=T(80,130,'Таблица показывает, где угроза обычно значима (●) или менее выражена (○); это качественная оценка.','sm')
for j,(r,e) in enumerate(th): body+=T(360+j*cw,170,r,'lab','middle')+T(360+j*cw,190,e,'sm','middle','style="fill:#526579"')
M={ 'Леса':'●○●○●●','Луга':'○●○●○●','Озёра и водно-болотные':'○●●○●●','Высокогорье':'○○●○○●'}
for i,(r,e) in enumerate(ty):
    y=250+i*100; body+=box(60,y-40,170+80,80,'#f1f4f6')+T(80,y-4,r,'t')+T(80,y+20,e,'s')
    for j,ch in enumerate(M[r]): body+=f'<text x="{360+j*cw}" y="{y+10}" font-size="38" text-anchor="middle" style="fill:{"#c0392b" if ch=="●" else "#7f8c8d"}">{ch}</text>'
body+=T(80,680,'Качественная матрица: оценка угроз для конкретной территории требует мониторинга.','s')+T(80,704,'Qualitative matrix: assessing threats to a specific area requires monitoring.','s','start','style="fill:#526579"')
S('22-I','threat-matrix','Угрозы природным территориям (качественная матрица)','Threats to natural areas (qualitative matrix)','Какие угрозы типичны для лесов, лугов, озёр и высокогорья.','Which threats are typical for forests, meadows, lakes and high mountains.',body,'Матрица обобщённая и не заменяет оценки конкретных территорий.','Generalised matrix; it does not replace assessments of specific areas.','Матрица угроз природным территориям.','Threat matrix for natural areas.')
# 21-F wild relatives table
rows=[('Яблоня Сиверса','Sievers\' apple','Malus sieversii','Дикий родич яблони','Wild relative of apple'),('Абрикос','Apricot','Prunus armeniaca','Плодовые леса и склоны','Fruit forests and slopes'),('Грецкий орех','Walnut','Juglans regia','Ореховые леса юга Кыргызстана','Walnut forests in the south'),('Фисташка','Pistachio','Pistacia vera','Сухие южные склоны','Dry southern slopes'),('Груша','Pear','Pyrus spp.','Горные леса и кустарники','Mountain forests and scrub')]
body=T(60,125,'Культура / Crop','lab')+T(400,125,'Латинское название / Latin name','lab')+T(780,125,'Где растёт / Typical habitat','lab')
for i,(a,b,c,d,e) in enumerate(rows):
    y=150+i*110; body+=box(40,y,1320,92,'#f1f4f6' if i%2 else '#e5efe3')+T(60,y+38,a,'t')+T(60,y+66,b,'s')+T(400,y+46,c,'t','start','style="font-style:italic"')+T(780,y+38,d,'s')+T(780,y+66,e,'s','start','style="fill:#526579"')
S('21-F','crop-wild-relatives-table','Дикие родичи культурных растений Кыргызстана','Crop wild relatives of Kyrgyzstan','Таблица основных диких родичей плодовых и орехоплодных культур.','Table of the main wild relatives of fruit and nut crops.',body,'Названия приведены по тексту главы; таксоны и охранный статус проверяйте по ботаническим источникам и Красной книге КР.','Names follow the chapter text; verify taxa and conservation status against botanical sources and the Red Data Book of Kyrgyzstan.','Дикие родичи культурных растений: таблица.','Crop wild relatives: table.')
print('m2 ok')
