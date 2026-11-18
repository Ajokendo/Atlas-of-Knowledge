from m4 import *
import math
W=load('ne_10m_admin_0_countries')
print(sorted(set(f['properties']['POP_YEAR'] for f in W['features']))[:12])
# 09-A
yrs=[1950,1960,1970,1980,1990,2000,2010,2020,2024]; obs=[2.5,3.0,3.7,4.4,5.3,6.1,6.9,7.8,8.2]
pj=[(2024,8.2),(2030,8.5),(2040,9.2),(2050,9.7),(2060,10.1),(2070,10.3),(2080,10.3),(2090,10.3),(2100,10.2)]
X=lambda y:120+(y-1950)*8.0; Y=lambda v:620-(v-2)*48
body='<line x1="110" y1="620" x2="1320" y2="620" stroke="#44586b" stroke-width="2"/><line x1="110" y1="140" x2="110" y2="620" stroke="#44586b" stroke-width="2"/>'
for v in range(2,12,2): body+=f'<line x1="110" y1="{Y(v)}" x2="1320" y2="{Y(v)}" stroke="#e1e6ea"/>'+T(100,Y(v)+5,str(v),'sm','end')
for y in range(1950,2101,25): body+=T(X(y),645,str(y),'sm','middle')
body+='<path d="M'+'L'.join(f'{X(y)} {Y(v)}' for y,v in zip(yrs,obs))+'" fill="none" stroke="#2e86ab" stroke-width="5"/>'
body+='<path d="M'+'L'.join(f'{X(y)} {Y(v)}' for y,v in pj)+'" fill="none" stroke="#c0392b" stroke-width="5" stroke-dasharray="12 8"/>'
body+=T(300,340,'Оценки наблюдений','lab','start','style="fill:#2e86ab"')+T(300,362,'Estimates of observed population','sm')+T(800,230,'Прогноз (средний вариант ООН)','lab','start','style="fill:#c0392b"')+T(800,252,'Projection (UN medium variant)','sm')
body+=T(120,130,'Население мира, млрд / World population, billion','sm')+T(X(2024)+10,Y(8.2)+40,'2024: ≈8,2','sm')+T(X(2080),Y(10.3)-14,'≈10,3 около 2080-х','sm','middle')
S('09-A','world-population-trend','Население мира: оценки и прогноз','World population: estimates and projection','Рост численности в 1950–2024 годах и средний вариант прогноза до 2100 года.','Population growth in 1950–2024 and the medium projection to 2100.',body,'Значения округлены по UN WPP 2024; наблюдения (сплошная) и прогноз (пунктир) показаны раздельно; прогноз — сценарий, не предсказание.','Values rounded from UN WPP 2024; estimates (solid) and projection (dashed) are shown separately; the projection is a scenario, not a prediction.','Население мира: оценки и прогноз.','World population: estimates and projection.')
# world base
def wmap(fillf,P=None,x=30,y=100,w=1340,h=620,stroke='#fff',sw=.6):
    P=P or Moll(x,y,w,h); o=[]
    for f in W['features']:
        p=f['properties']
        if p['ADMIN']=='Antarctica': continue
        o.append(f'<path d="{path_of(f["geometry"],P)}" fill="{fillf(f)}" stroke="{stroke}" stroke-width="{sw}"/>')
    return P,''.join(o)
# 09-E density
def parea(geom,P):
    polys=[geom['coordinates']] if geom['type']=='Polygon' else geom['coordinates']; tot=0
    for poly in polys:
        for i,ring in enumerate(poly):
            q=[P(*p[:2]) for p in ring]; a=0
            for (x1,y1),(x2,y2) in zip(q,q[1:]+q[:1]): a+=x1*y2-x2*y1
            tot+=(abs(a)/2)*(1 if i==0 else -1)
    return tot
P0=Moll(30,100,1340,620); k=510.1e6/(4*math.pi*P0.R**2)
CLS=[(1,'#f7f4e9'),(10,'#fde3a7'),(50,'#f9b872'),(100,'#ee7e4e'),(200,'#c0392b'),(1e9,'#7b241c')]
def dens(f):
    p=f['properties']; a=parea(f['geometry'],P0)*k
    d=p['POP_EST']/a if a>0 else 0
    for t,c in CLS:
        if d<t: return c
P,mp=wmap(dens,P0)
leg=''.join(f'<rect x="{60+i*190}" y="730" width="22" height="14" fill="{c}" stroke="#647789"/>'+T(90+i*190,742,lb,'sm') for i,((t,c),lb) in enumerate(zip(CLS,['< 1','1–10','10–50','50–100','100–200','> 200'])))
S('09-E','world-population-density','Плотность населения по странам мира','World population density by country','Человек на квадратный километр по странам.','People per square kilometre by country.',mp+leg+T(1180,742,'чел./км² / people per km²','sm'),'Данные Natural Earth (оценка населения страны по полю POP_EST, примерно 2009–2020 гг., в зависимости от страны) и площадь по проекции; для сопоставимой даты нужны UN WPP.','Natural Earth data (country population in POP_EST, about 2009–2020, depending on the country) and projected area; use UN WPP for a comparable reference date.','Плотность населения мира по странам.','World population density by country.')
# 10-A political
CC={'Africa':'#f4ecd9','Asia':'#e5efe3','Europe':'#e4eff6','North America':'#f5e7e4','South America':'#ece6f3','Oceania':'#e6f0ee','Seven seas (open ocean)':'#eee'}
def pol(f):
    return CC.get(f['properties']['CONTINENT'],'#eee')
P,mp=wmap(pol,stroke='#7a8a99',sw=.7)
kx,ky=P(74.6,41.5)
mp+=f'<circle cx="{kx:.0f}" cy="{ky:.0f}" r="9" fill="none" stroke="#c0392b" stroke-width="3"/>'+T(kx,ky-16,'Кыргызстан / Kyrgyzstan','lab','middle','style="paint-order:stroke;stroke:#fff;stroke-width:3px"')
leg=''.join(f'<rect x="{60+i*215}" y="730" width="22" height="14" fill="{c}" stroke="#647789"/>'+T(90+i*215,742,lb,'sm') for i,(c,lb) in enumerate([('#f4ecd9','Африка / Africa'),('#e5efe3','Азия / Asia'),('#e4eff6','Европа / Europe'),('#f5e7e4','Сев. Америка / N. America'),('#ece6f3','Юж. Америка / S. America'),('#e6f0ee','Океания / Oceania')]))
S('10-A','world-political-map','Политическая карта мира (учебная)','World political map (teaching version)','Государства мира с выделением Кыргызстана.','The states of the world with Kyrgyzstan highlighted.',mp+leg,'Границы — Natural Earth (версия данных на дату загрузки, ноябрь 2026), фактическое положение дел; спорные территории показаны так, как в источнике, и не выражают позиции атласа.','Boundaries from Natural Earth (data as downloaded in November 2026), de facto situation; disputed territories are shown as in the source and do not express an atlas position.','Политическая карта мира.','World political map.')
# 12-C transboundary
RV=('Nile','Congo','Niger','Zambezi','Danube','Rhine','Mekong','Ganges','Indus','Amazonas','Amazon','Paraná','Parana','Amu Darya','Syr  Darya','Brahmaputra','Yangtze','Tigris','Euphrates')
P=Moll(30,100,1340,620); o=wmap(lambda f:'#eef1f4',P)[1]
for f in feats('ne_10m_rivers_lake_centerlines'):
    n=(f['properties']['name'] or '').strip()
    if n in RV: o+=f'<path d="{path_of(f["geometry"],P)}" fill="none" stroke="#2e86c1" stroke-width="2.4"/>'
for la,lo,ru,en in [(30.0,32.5,'Суэц','Suez'),(9.1,-79.7,'Панама','Panama'),(2.5,101.5,'Малакка','Malacca'),(26.5,56.5,'Ормуз','Hormuz'),(41.1,29.05,'Босфор','Bosporus'),(35.96,-5.5,'Гибралтар','Gibraltar')]:
    x,y=P(lo,la); o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="#c0392b" stroke="#fff" stroke-width="2"/>'+T(x+9,y-6,ru+' / '+en,'sm','start','style="paint-order:stroke;stroke:#fff;stroke-width:3px"')
for la,lo,ru,en in [(-15,-70,'Анды','Andes'),(28,85,'Гималаи','Himalaya'),(46.5,10,'Альпы','Alps'),(45,-110,'Скалистые горы','Rocky Mountains'),(42,78,'Тянь-Шань','Tien Shan')]:
    x,y=P(lo,la); o+=T(x,y,'▲ '+ru+' / '+en,'sm','middle','style="fill:#5b3e22;font-weight:700;paint-order:stroke;stroke:#fff;stroke-width:3px"')
o+='<rect x="60" y="722" width="26" height="4" fill="#2e86c1"/>'+T(96,728,'трансграничные реки (примеры) / transboundary rivers (examples)','sm')+'<circle cx="640" cy="725" r="6" fill="#c0392b"/>'+T(654,729,'морские проливы и каналы (примеры) / straits and canals (examples)','sm')
S('12-C','transboundary-systems','Трансграничные системы мира (схема)','Transboundary systems of the world (schematic)','Реки, горные системы и морские узлы, связывающие регионы.','Rivers, mountain systems and maritime nodes that link regions.',o,'Выбранные примеры, не полный перечень; реки — Natural Earth, остальное — учебные отметки.','Selected examples, not a complete list; rivers from Natural Earth, other marks are teaching annotations.','Трансграничные системы: примеры.','Transboundary systems: examples.')
# 12-J Antarctica
Pp=Polar(700,420,330,-55)
o='<circle cx="700" cy="420" r="330" fill="#eaf3fa" stroke="#9cc4e4" stroke-width="2"/>'
ant=[f for f in W['features'] if f['properties']['ADMIN']=='Antarctica'][0]
o+=f'<path d="{path_of(ant["geometry"],Pp)}" fill="#ffffff" stroke="#5b8db8" stroke-width="1.5"/>'
for f in feats('ne_10m_antarctic_ice_shelves_polys'): o+=f'<path d="{path_of(f["geometry"],Pp)}" fill="#cfe6f5" stroke="#5b8db8" stroke-width=".8"/>'
for r in (-60,): 
    rad=2*Pp.k*math.tan(math.radians((90+r)/2)); o+=f'<circle cx="700" cy="420" r="{rad:.0f}" fill="none" stroke="#c0392b" stroke-width="2.4" stroke-dasharray="10 6"/>'
o+=T(700+rad*0.71+6,420+rad*0.71+30,'60° ю. ш.: граница Договора об Антарктике','sm')+T(700+rad*0.71+6,420+rad*0.71+48,'60°S: Antarctic Treaty area limit','sm')
for lat,lon,ru,en in [(-77.85,166.67,'Мак-Мёрдо','McMurdo'),(-90,0,'Амундсен–Скотт','Amundsen–Scott'),(-78.46,106.84,'Восток','Vostok'),(-75.1,123.35,'Конкордия','Concordia'),(-64.77,-64.05,'Палмер','Palmer'),(-67.6,62.87,'Моусон','Mawson')]:
    x,y=Pp(lon,lat); o+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#c0392b" stroke="#fff" stroke-width="1.5"/>'+T(x+8,y-6,ru+' / '+en,'sm','start','style="paint-order:stroke;stroke:#fff;stroke-width:3px"')
o+=T(60,140,'Белый — материк и ледниковый щит;','sm')+T(60,160,'голубой — шельфовые ледники','sm')+T(60,190,'White: continent and ice sheet;','sm','start','style="fill:#526579"')+T(60,210,'blue: ice shelves','sm','start','style="fill:#526579"')
S('12-J','antarctica-southern-ocean','Антарктика и Южный океан (схема)','Antarctica and the Southern Ocean (schematic)','Материк, шельфовые ледники, станции и граница Договора об Антарктике.','The continent, ice shelves, research stations and the Antarctic Treaty limit.',o,'Natural Earth, полярная стереографическая проекция; станции — примеры с ориентировочными координатами; граница океана принята по-разному, здесь показана 60° ю. ш.','Natural Earth, polar stereographic projection; stations are examples with approximate coordinates; the ocean limit is defined in several ways, here 60°S is shown.','Антарктика: схема.','Antarctica: schematic.')
print('m5 ok')
