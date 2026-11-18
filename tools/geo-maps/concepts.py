# -*- coding: utf-8 -*-
"""Авторские концептуальные схемы для глав географии (SVG, двуязычные). Запуск: python3 concepts.py -> diagrams + /home/claude/geo/concept_items.json"""
import json, math, random
from kit import esc
OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams/'
STY=('text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:34px;font-weight:700}.sub{font-size:22px;fill:#526579}'
 '.r{font-size:23px;font-weight:700}.e{font-size:18px;fill:#526579}.r2{font-size:19px;font-weight:700}.e2{font-size:15px;fill:#526579}.sm{font-size:15px}')
items=[]
import textwrap
LAST=[0]
def svg(fn,ru,en,W,H,body,fru='Схема.',fen='A schematic.'):
    H=max(H,LAST[0]+95); LAST[0]=0
    s=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{esc(ru)} / {esc(en)}</title><style>{STY}</style>'
       f'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0L8 3L0 6Z" fill="#526579"/></marker></defs>'
       f'<rect width="{W}" height="{H}" fill="#fbfcfe"/><text x="30" y="46" class="h">{esc(ru)}</text><text x="30" y="76" class="sub">{esc(en)}</text>{body}'
       f'<text x="30" y="{H-38}" class="sm">{esc(fru)}</text><text x="30" y="{H-16}" class="sm" style="fill:#526579">{esc(fen)}</text></svg>')
    open(OUT+fn,'w',encoding='utf-8').write(s)
def tx(x,y,ru,en,anc='start',big=True,fill=None,wr=62):
    a,b=('r','e') if big else ('r2','e2'); st=f' style="fill:{fill}"' if fill else ''
    if not big and len(ru)>wr:
        out=''; yy=y
        for l in textwrap.wrap(ru,wr): out+=f'<text x="{x}" y="{yy}" class="r2" text-anchor="{anc}"{st}>{esc(l)}</text>'; yy+=24
        yy-=2
        for l in textwrap.wrap(en,int(wr*1.25)): out+=f'<text x="{x}" y="{yy}" class="e2" text-anchor="{anc}">{esc(l)}</text>'; yy+=19
        LAST[0]=max(LAST[0],yy); return out
    LAST[0]=max(LAST[0],y+30)
    return f'<text x="{x}" y="{y}" class="{a}" text-anchor="{anc}"{st}>{esc(ru)}</text><text x="{x}" y="{y+(24 if big else 19)}" class="{b}" text-anchor="{anc}">{esc(en)}</text>'
def bx(x,y,w,h,fill='#e4eff6',st='#647789',r=14): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{st}" stroke-width="2"/>'
def ar(x1,y1,x2,y2,c='#526579',w=3): return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{c}" stroke-width="{w}" fill="none" marker-end="url(#a)"/>'
def add(ch,head,fn,ru,en): items.append([ch,head,fn,ru,en,'Схема.','A schematic.'])
# 1. масштаб
def scale():
    b=''
    rows=[('1 : 50 000','1 см = 500 м','1 cm = 500 m',0.5,'#cfe8d4'),('1 : 100 000','1 см = 1 км','1 cm = 1 km',1.0,'#f3e6b0'),('1 : 1 000 000','1 см = 10 км','1 cm = 10 km',10.0,'#e8cfe6')]
    y=130
    for sc,ru,en,km,c in rows:
        b+=bx(30,y,940,120,c,'#647789')+f'<text x="50" y="{y+42}" class="r" style="font-size:30px">{sc}</text>'+f'<text x="50" y="{y+76}" class="r2">{ru}</text><text x="50" y="{y+98}" class="e2">{en}</text>'
        b+=f'<rect x="420" y="{y+30}" width="200" height="22" fill="#fff" stroke="#243447" stroke-width="2"/><rect x="420" y="{y+30}" width="100" height="22" fill="#243447"/><text x="420" y="{y+78}" class="r2">0</text><text x="620" y="{y+78}" class="r2" text-anchor="end">{(2*km):g} км</text><text x="520" y="{y+98}" class="e2" text-anchor="middle">2 см на карте = {(2*km):g} km</text>'
        y+=140
    b+=tx(30,y+30,'Чем меньше знаменатель, тем крупнее масштаб: больше подробностей, меньше территория.','The smaller the denominator, the larger the scale: more detail, smaller area.',big=False)
    svg('01-M-map-scale-bilingual.svg','Масштаб карты','Map scale: what one centimetre stands for',1000,640,b)
    add('01','## 1.10.1. ','01-M-map-scale-bilingual.svg','Три масштаба карты и линейные масштабы.','Three map scales with scale bars.')
# 2. планетарные границы
def planetary():
    names=[('Изменение климата','Climate change'),('Целостность биосферы','Biosphere integrity'),('Землепользование','Land-system change'),('Пресная вода','Freshwater use'),('Потоки азота и фосфора','Nitrogen and phosphorus flows'),('Закисление океана','Ocean acidification'),('Аэрозоли в атмосфере','Atmospheric aerosols'),('Озоновый слой','Stratospheric ozone'),('Новые вещества','Novel entities')]
    cols=['#f4b6a0','#b7dba5','#d9c3a0','#a5d3e8','#f3d98b','#9fd9cc','#d3c1e8','#f0b7c4','#c9d3dc']
    b='';cx,cy=500,350
    for i,(r,e) in enumerate(names):
        a0=-math.pi/2+i*2*math.pi/9; a1=a0+2*math.pi/9
        pt=lambda R,a:(cx+R*math.cos(a),cy+R*math.sin(a))
        p=[pt(55,a0),pt(160,a0),pt(160,a1),pt(55,a1)]
        b+=f'<path d="M{p[0][0]:.0f} {p[0][1]:.0f}L{p[1][0]:.0f} {p[1][1]:.0f}A160 160 0 0 1 {p[2][0]:.0f} {p[2][1]:.0f}L{p[3][0]:.0f} {p[3][1]:.0f}A55 55 0 0 0 {p[0][0]:.0f} {p[0][1]:.0f}Z" fill="{cols[i]}" stroke="#fff" stroke-width="3"/>'
        am=(a0+a1)/2; lx,ly=cx+195*math.cos(am),cy+190*math.sin(am)+0
        anc='start' if math.cos(am)>0.2 else ('end' if math.cos(am)<-0.2 else 'middle')
        b+=f'<text x="{lx:.0f}" y="{ly:.0f}" class="r2" text-anchor="{anc}">{i+1}. {r}</text><text x="{lx:.0f}" y="{ly+19:.0f}" class="e2" text-anchor="{anc}">{e}</text>'
    b+=f'<text x="{cx}" y="{cy+5}" class="e2" text-anchor="middle">9 границ</text>'
    svg('02-M-planetary-boundaries-bilingual.svg','Девять планетарных границ','Nine planetary boundaries',1000,720,b,'Концепция планетарных границ (Рокстрём и др., 2009). Состояние границ не показано.','Planetary-boundaries framework (Rockström et al., 2009). Status of boundaries not shown.')
    add('02','### 2.14.1. ','02-M-planetary-boundaries-bilingual.svg','Девять процессов, образующих «безопасное пространство» для человечества.','The nine processes that make up humanity\'s "safe operating space".')
# 3/13 риск
def risk():
    b=bx(40,130,270,120,'#f4d9cf')+tx(60,170,'Опасность','Hazard')+f'<text x="60" y="225" class="e2">землетрясение, сель, паводок</text>'
    b+=bx(365,130,270,120,'#f3e6b0')+tx(385,170,'Уязвимость','Vulnerability')+f'<text x="385" y="225" class="e2">дома, дороги, подготовка людей</text>'
    b+=bx(690,130,270,120,'#d6e6f3')+tx(710,170,'Экспозиция','Exposure')+f'<text x="710" y="225" class="e2">кто и что оказалось в зоне</text>'
    b+='<text x="337" y="205" class="h" text-anchor="middle">×</text><text x="662" y="205" class="h" text-anchor="middle">×</text>'
    b+=ar(500,255,500,310)+bx(280,315,440,100,'#f2c1b5','#c0392b')+tx(500,358,'РИСК = возможные потери','RISK = possible losses','middle')
    b+=tx(40,470,'Стихия сама по себе — ещё не бедствие. Бедствие возникает там, где опасность встречает людей и постройки.','A natural hazard is not yet a disaster. A disaster occurs where a hazard meets people and buildings.',big=False)
    b+=tx(40,575,'Снизить риск можно, уменьшив уязвимость и экспозицию: сейсмостойкое строительство, карты селей, раннее оповещение.','Risk falls when vulnerability and exposure fall: seismic-resistant building, mudflow maps, early warning.',big=False)
    svg('03-M-risk-formula-bilingual.svg','Из чего складывается риск','What risk is made of',1000,650,b)
    add('03','### 3.6.4. ','03-M-risk-formula-bilingual.svg','Риск = опасность × уязвимость × экспозиция.','Risk = hazard × vulnerability × exposure.')
    add('13','## 13.10. ','03-M-risk-formula-bilingual.svg','Риск = опасность × уязвимость × экспозиция.','Risk = hazard × vulnerability × exposure.')
# 5 климатограмма
def climo():
    t=[-6,-3,5,13,18,23,26,24,18,11,3,-3]; p=[25,30,50,60,50,30,15,12,15,35,40,30]
    x0,y0,w,h=110,150,780,290; b=f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#fff" stroke="#9aa9b6"/>'
    mn=['Я','Ф','М','А','М','И','И','А','С','О','Н','Д']
    for i,v in enumerate(p):
        bw=w/12; hh=v/80*h; b+=f'<rect x="{x0+i*bw+8:.0f}" y="{y0+h-hh:.0f}" width="{bw-16:.0f}" height="{hh:.0f}" fill="#a5d3e8" stroke="#5d9bc4"/><text x="{x0+i*bw+bw/2:.0f}" y="{y0+h+24}" class="r2" text-anchor="middle">{mn[i]}</text>'
    pts=' '.join(f'{x0+i*w/12+w/24:.0f},{y0+h-(v+10)/50*h:.0f}' for i,v in enumerate(t)); b+=f'<polyline points="{pts}" fill="none" stroke="#c0392b" stroke-width="4"/>'
    for yy,l in ((0,'0'),(1,'')): pass
    b+=f'<path d="M{x0} {y0+h-10/50*h:.0f}H{x0+w}" stroke="#c0392b" stroke-dasharray="6 5" stroke-width="1.5"/><text x="{x0-8}" y="{y0+h-10/50*h+6:.0f}" class="e2" text-anchor="end" style="fill:#c0392b">0 °C</text>'
    b+=f'<line x1="110" y1="108" x2="150" y2="108" stroke="#c0392b" stroke-width="5"/><text x="160" y="114" class="r2">температура, °C</text><rect x="420" y="98" width="26" height="20" fill="#a5d3e8" stroke="#5d9bc4"/><text x="456" y="114" class="r2">осадки, мм (столбцы)</text><text x="160" y="132" class="e2" style="font-size:12px">temperature</text><text x="456" y="132" class="e2" style="font-size:12px">precipitation</text>'
    b+=tx(30,520,'1. Когда теплее всего и холоднее всего?  2. Когда больше осадков?  3. Совпадают ли тепло и влага?','1. When is it warmest and coldest?  2. When is it wettest?  3. Do warmth and moisture coincide?',big=False)
    svg('05-M-how-to-read-climograph-bilingual.svg','Как читать климатограмму','How to read a climograph',1000,640,b,'Учебный пример с условными числами — не данные станции.','A teaching example with illustrative numbers, not station data.')
    add('05','## 5.17. ','05-M-how-to-read-climograph-bilingual.svg','Климатограмма: температура — линией, осадки — столбцами.','Climograph: temperature as a line, precipitation as bars.')
# 7 цепь питания
def chain():
    b=''
    lv=[('Продуценты','Producers','трава, арча','grass, juniper','#b7dba5'),('Травоядные','Herbivores','архар, горный козёл','argali, ibex','#f3d98b'),('Хищники','Predators','снежный барс','snow leopard','#f1b9a3')]
    for i,(r,e,ex,ee,c) in enumerate(lv):
        x=40+i*320; b+=bx(x,170,260,170,c)+f'<text x="{x+130}" y="215" class="r" text-anchor="middle">{r}</text><text x="{x+130}" y="240" class="e" text-anchor="middle">{e}</text><text x="{x+130}" y="285" class="r2" text-anchor="middle">{ex}</text><text x="{x+130}" y="306" class="e2" text-anchor="middle">{ee}</text>'
        if i<2: b+=ar(x+265,255,x+315,255)
    b+=bx(40,400,900,70,'#e8e4dc')+tx(60,432,'Разрушители: бактерии, грибы возвращают вещества в почву','Decomposers: bacteria and fungi return nutrients to the soil',big=False)
    b+=tx(40,520,'С каждого уровня дальше передаётся лишь малая часть энергии (в среднем порядка 10 %), поэтому хищников всегда мало.','Only a small part of energy passes up each level (on average about 10 %), so predators are always few.',big=False)
    svg('07-M-food-chain-kyrgyzstan-bilingual.svg','Цепь питания в горах Кыргызстана','A food chain in the mountains of Kyrgyzstan',1000,640,b)
    add('07','## 7.4. ','07-M-food-chain-kyrgyzstan-bilingual.svg','Цепь питания: трава — копытные — снежный барс.','Food chain: grass — ungulates — snow leopard.')
# 7.9 зоны озера
def lakezones():
    b='<path d="M60 190H940V400Q940 470 700 480Q500 500 300 480Q60 470 60 400Z" fill="#cfe5f3" stroke="#5d9bc4" stroke-width="3"/><path d="M60 190L200 150H800L940 190" fill="none"/>'
    b+='<path d="M60 190Q60 410 60 400Q150 460 300 480" fill="none"/>'
    b+='<rect x="60" y="190" width="880" height="18" fill="#a9d1ea"/>'
    b+='<path d="M60 190C80 330 160 430 300 478" stroke="#243447" stroke-dasharray="6 6" fill="none"/><path d="M940 190C920 330 840 430 700 480" stroke="#243447" stroke-dasharray="6 6" fill="none"/>'
    b+=tx(90,170,'Прибрежная зона','Littoral zone',big=False)+tx(380,260,'Открытая вода (свет)','Open water (light)',big=False)+tx(420,420,'Глубинная зона','Profundal zone',big=False)
    b+=tx(740,170,'Прибрежная зона','Littoral zone','start',False)
    b+=tx(40,540,'Растения и больше всего жизни — у берега и на мелководье; в тёмной глубине живут бактерии и донные животные.','Plants and most life are near the shore and in shallows; the dark depths hold bacteria and bottom animals.',big=False)
    svg('07-M-lake-zones-bilingual.svg','Зоны озера','Zones of a lake',1000,660,b)
    add('07','## 7.9. ','07-M-lake-zones-bilingual.svg','Разрез озера: прибрежная, открытая вода, глубинная зона.','Cross-section of a lake: littoral, open water, profundal.')
# 8 почвенный профиль
def soil():
    hz=[('O','Подстилка','Litter','#6b4a2f','#fff'),('A','Гумусовый','Humus','#4a3220','#fff'),('E','Вымывания','Leached','#c9b79a','#243447'),('B','Накопления','Accumulation','#b07a4a','#fff'),('C','Материнская порода','Parent material','#cdb892','#243447'),('R','Коренная порода','Bedrock','#8b8b8b','#fff')]
    hh=[50,80,60,90,90,80]; y=130; b=''
    for (k,r,e,c,tc),h in zip(hz,hh):
        b+=f'<rect x="80" y="{y}" width="300" height="{h}" fill="{c}" stroke="#fff" stroke-width="2"/><text x="230" y="{y+h/2+10}" class="h" text-anchor="middle" style="fill:{tc}">{k}</text>'
        b+=f'<text x="420" y="{y+h/2:.0f}" class="r2">{r}</text><text x="420" y="{y+h/2+20:.0f}" class="e2">{e}</text>'; y+=h
    b+=ar(900,140,900,y-10)+f'<text x="880" y="{(130+y)/2:.0f}" class="e2" text-anchor="end">глубина / depth</text>'
    svg('08-M-soil-profile-bilingual.svg','Почвенный профиль и горизонты','Soil profile and horizons',1000,640,b,'Типовая схема; у разных почв набор горизонтов различается.','A typical scheme; the set of horizons differs between soils.')
    add('08','## 8.3. ','08-M-soil-profile-bilingual.svg','Почвенный профиль: горизонты O, A, E, B, C, R.','Soil profile: horizons O, A, E, B, C, R.')
# 14.4 координаты
def coords():
    cx,cy,R=300,340,190; b=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#e3f0fa" stroke="#5d9bc4" stroke-width="3"/>'
    b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{R}" ry="55" fill="none" stroke="#243447" stroke-width="2"/><text x="{cx+R+10}" y="{cy+6}" class="r2">0° экватор</text>'
    b+=f'<ellipse cx="{cx}" cy="{cy-R*0.68:.0f}" rx="{R*0.73:.0f}" ry="35" fill="none" stroke="#c0392b" stroke-width="3"/>'
    b+=f'<text x="{cx+R*0.73+12:.0f}" y="{cy-R*0.68+6:.0f}" class="r2" style="fill:#c0392b">42,9° с. ш.</text>'
    b+=f'<ellipse cx="{cx}" cy="{cy}" rx="55" ry="{R}" fill="none" stroke="#243447" stroke-width="2" stroke-dasharray="5 5"/><ellipse cx="{cx+85}" cy="{cy}" rx="85" ry="{R}" fill="none" stroke="#c0392b" stroke-width="3" transform="rotate(0)" clip-path="none" opacity="0"/>'
    b+=f'<text x="{cx}" y="{cy-R-14}" class="r2" text-anchor="middle">С</text><text x="{cx}" y="{cy+R+34}" class="r2" text-anchor="middle">Ю</text>'
    b+=bx(620,150,340,200,'#f3e6b0')+tx(640,190,'Бишкек','Bishkek')+f'<text x="640" y="255" class="r2">широта ≈ 42,9° с. ш.</text><text x="640" y="276" class="e2">latitude ≈ 42.9° N</text><text x="640" y="310" class="r2">долгота ≈ 74,6° в. д.</text><text x="640" y="331" class="e2">longitude ≈ 74.6° E</text>'
    b+=tx(620,400,'Широта — угол к северу или югу от экватора (0–90°). Долгота — угол к востоку или западу от Гринвича (0–180°).','Latitude is the angle north or south of the equator (0–90°). Longitude is the angle east or west of Greenwich (0–180°).',big=False,wr=34)
    svg('14-M-latitude-longitude-bilingual.svg','Широта и долгота','Latitude and longitude',1000,700,b,'Координаты Бишкека округлены до 0,1°.','Bishkek coordinates rounded to 0.1°.')
    add('14','## 14.4. ','14-M-latitude-longitude-bilingual.svg','Широта и долгота на примере Бишкека.','Latitude and longitude, with Bishkek as an example.')
# 14.11 топология
def topo():
    b=''
    cases=[('Разрыв','Gap'),('Наложение','Overlap'),('Висячая линия','Dangle'),('Правильно','Correct')]
    for i,(r,e) in enumerate(cases):
        x=40+i*240; b+=bx(x,130,220,220,'#fff','#9aa9b6')
        if i==0: b+=f'<path d="M{x+20} {y_}" />' if False else f'<polygon points="{x+20},150 {x+105},150 {x+105},330 {x+20},330" fill="#cfe8d4" stroke="#243447" stroke-width="2"/><polygon points="{x+120},150 {x+200},150 {x+200},330 {x+120},330" fill="#f3e6b0" stroke="#243447" stroke-width="2"/><rect x="{x+105}" y="150" width="15" height="180" fill="#fff" stroke="#c0392b" stroke-dasharray="4 3"/>'
        if i==1: b+=f'<polygon points="{x+20},150 {x+125},150 {x+125},330 {x+20},330" fill="#cfe8d4" stroke="#243447" stroke-width="2" opacity=".9"/><polygon points="{x+95},150 {x+200},150 {x+200},330 {x+95},330" fill="#f3e6b0" stroke="#243447" stroke-width="2" opacity=".75"/><rect x="{x+95}" y="150" width="30" height="180" fill="#f4b6a0" opacity=".8"/>'
        if i==2: b+=f'<path d="M{x+20} 330V240H{x+110}M{x+110} 240H{x+200}V150M{x+110} 240V200" fill="none" stroke="#243447" stroke-width="3"/><circle cx="{x+110}" cy="200" r="9" fill="#c0392b"/>'
        if i==3: b+=f'<polygon points="{x+20},150 {x+110},150 {x+110},330 {x+20},330" fill="#cfe8d4" stroke="#243447" stroke-width="2"/><polygon points="{x+110},150 {x+200},150 {x+200},330 {x+110},330" fill="#f3e6b0" stroke="#243447" stroke-width="2"/>'
        b+=f'<text x="{x+110}" y="385" class="r2" text-anchor="middle" style="fill:{"#2e7d32" if i==3 else "#c0392b"}">{r}</text><text x="{x+110}" y="405" class="e2" text-anchor="middle">{e}</text>'
    b+=tx(40,470,'Соседние участки должны делить общую границу без щелей и наложений: иначе неверна площадь и сбиваются расчёты.','Neighbouring parcels must share a boundary with no gaps or overlaps; otherwise areas are wrong and analyses fail.',big=False)
    svg('14-M-topology-errors-bilingual.svg','Топологические ошибки в данных','Topology errors in spatial data',1000,600,b)
    add('14','## 14.11. ','14-M-topology-errors-bilingual.svg','Типичные топологические ошибки: разрыв, наложение, висячая линия.','Common topology errors: gap, overlap, dangle.')
# 14.13 элементы карты
def mapanatomy():
    from shapely.geometry import shape
    kg=[f for f in json.load(open('/home/claude/ne/ne_10m_admin_0_countries.geojson'))['features'] if f['properties']['NAME']=='Kyrgyzstan'][0]['geometry']
    s=shape(kg).simplify(0.01); x0,y0,x1,y1=s.bounds; c=math.cos(math.radians(41)); k=min(560/((x1-x0)*c),300/(y1-y0))
    P=lambda lo,la:(220+(lo-x0)*c*k,170+(y1-la)*k)
    gs=[s] if s.geom_type=='Polygon' else list(s.geoms); d=''.join('M'+'L'.join('%.0f %.0f'%P(*q) for q in g.exterior.coords)+'Z' for g in gs)
    b='<g transform="translate(-140,0)">'+bx(190,120,630,400,'#fff','#243447',4)+f'<path d="{d}" fill="#e9f1e2" stroke="#5d7a4f" stroke-width="2"/>'
    b+='<text x="505" y="152" class="r" text-anchor="middle">Название карты</text>'
    b+='<path d="M780 140V190M780 140L770 160M780 140L790 160" stroke="#243447" stroke-width="3" fill="none"/><text x="780" y="210" class="r2" text-anchor="middle">С</text>'
    b+='<rect x="230" y="470" width="120" height="14" fill="#fff" stroke="#243447" stroke-width="2"/><rect x="230" y="470" width="60" height="14" fill="#243447"/><text x="230" y="505" class="e2">0        100 км</text>'
    b+='<rect x="650" y="430" width="150" height="70" fill="#fff" stroke="#9aa9b6"/><rect x="662" y="444" width="22" height="14" fill="#e9f1e2" stroke="#5d7a4f"/><text x="692" y="456" class="e2">Кыргызстан</text><text x="662" y="486" class="e2">Легенда</text>'
    notes=[(30,150,'Название','Title'),(30,230,'Стрелка севера','North arrow'),(30,330,'Масштаб','Scale'),(30,430,'Легенда','Legend')]
    b+='</g>'
    b+=tx(700,160,'Название','Title','start',False)+tx(700,240,'Стрелка севера','North arrow','start',False)+tx(700,455,'Легенда','Legend','start',False)+tx(100,548,'Масштаб (линейка)','Scale bar','start',False)
    b+=tx(40,610,'Источник и дата данных подписываются на карте всегда.','Always state the data source and date on a map.',big=False)
    svg('14-M-map-anatomy-bilingual.svg','Из чего состоит карта','The parts of a map',1000,680,b)
    add('14','## 14.13. ','14-M-map-anatomy-bilingual.svg','Обязательные элементы карты: название, стрелка севера, масштаб, легенда.','Essential map elements: title, north arrow, scale, legend.')
# 16.5 выборка
def sampling():
    random.seed(4); b=''
    names=[('Случайная','Simple random'),('Систематическая','Systematic'),('Расслоённая','Stratified'),('Кластерная','Cluster')]
    for i,(r,e) in enumerate(names):
        x=40+i*240; b+=bx(x,130,220,220,'#fff','#9aa9b6')
        if i==2:
            b+=f'<rect x="{x}" y="130" width="220" height="73" fill="#cfe8d4" opacity=".6"/><rect x="{x}" y="203" width="220" height="74" fill="#f3e6b0" opacity=".6"/><rect x="{x}" y="277" width="220" height="73" fill="#d6e6f3" opacity=".6"/>'
        pts=[]
        if i==0: pts=[(x+20+random.random()*180,150+random.random()*180) for _ in range(12)]
        if i==1: pts=[(x+35+a*50,165+b_*50) for a in range(4) for b_ in range(4)]
        if i==2: pts=[(x+30+random.random()*160,140+yb*73+10+random.random()*50) for yb in range(3) for _ in range(4)]
        if i==3:
            for cx_,cy_ in ((x+60,190),(x+160,300)):
                b+=f'<circle cx="{cx_}" cy="{cy_}" r="50" fill="none" stroke="#c0392b" stroke-dasharray="5 4" stroke-width="2"/>'; pts+=[(cx_+random.uniform(-35,35),cy_+random.uniform(-35,35)) for _ in range(6)]
        for px,py in pts: b+=f'<circle cx="{px:.0f}" cy="{py:.0f}" r="6" fill="#2e86c1" stroke="#fff" stroke-width="1.5"/>'
        b+=f'<text x="{x+110}" y="385" class="r2" text-anchor="middle">{r}</text><text x="{x+110}" y="405" class="e2" text-anchor="middle">{e}</text>'
    b+=tx(40,470,'Выбор схемы зависит от вопроса: как однородна территория и насколько дорого добираться до точек.','The choice depends on the question: how uniform the area is and how costly it is to reach the points.',big=False)
    svg('16-M-sampling-designs-bilingual.svg','Схемы выборки точек наблюдения','Sampling designs for observation points',1000,600,b)
    add('16','## 16.5. ','16-M-sampling-designs-bilingual.svg','Четыре схемы выборки: случайная, систематическая, расслоённая, кластерная.','Four sampling designs: random, systematic, stratified, cluster.')
# 19.4 орографический эффект
def oro():
    b='<path d="M40 460L380 460L560 180L760 460L960 460V500H40Z" fill="#c9b79a" stroke="#6b5a45" stroke-width="3"/><path d="M500 260L560 180L620 260Z" fill="#fff" stroke="#9aa9b6"/>'
    b+='<path d="M60 400C250 400 360 330 470 235" stroke="#2e86c1" stroke-width="5" fill="none" marker-end="url(#a)"/>'
    b+='<path d="M600 205C700 230 800 290 920 330" stroke="#c0392b" stroke-width="5" fill="none" stroke-dasharray="10 8" marker-end="url(#a)"/>'
    for cx_ in (330,400,470): b+=f'<ellipse cx="{cx_}" cy="{250+(cx_-330)*-0.2:.0f}" rx="55" ry="26" fill="#e9eef3" stroke="#9aa9b6"/>'
    for i in range(6): b+=f'<path d="M{420+i*22} {290+i*-4}l-6 22" stroke="#2e86c1" stroke-width="3"/>'
    b+=tx(60,140,'Наветренный склон','Windward slope')+tx(560,140,'Подветренный склон','Leeward slope')+tx(60,545,'Воздух поднимается, остывает, образуются облака и осадки','Air rises, cools; clouds and precipitation form',big=False)
    b+=tx(60,600,'Воздух опускается, нагревается — сухо («дождевая тень»)','Air sinks and warms — dry («rain shadow»)',big=False)
    svg('19-M-orographic-effect-bilingual.svg','Орографический эффект','The orographic effect',1000,660,b)
    add('19','## 19.4. ','19-M-orographic-effect-bilingual.svg','Как горный хребет распределяет осадки между склонами.','How a mountain ridge divides precipitation between its slopes.')
# 20.3 зоны ледника
def glacier():
    b='<path d="M40 380L120 150L420 230L760 340L940 420V470H40Z" fill="#c9b79a"/><path d="M120 150L420 230L760 340L880 400L780 410L420 300L130 210Z" fill="#f3f8fc" stroke="#9fc3dd" stroke-width="3"/>'
    b+='<path d="M120 150L420 230" stroke="none"/><path d="M420 232L430 300" stroke="#c0392b" stroke-width="3" stroke-dasharray="7 5"/><text x="440" y="268" class="r2" style="fill:#c0392b">Линия равновесия</text><text x="440" y="288" class="e2">Equilibrium line (ELA)</text>'
    b+='<path d="M880 400Q900 400 940 420" stroke="#2e86c1" stroke-width="5" fill="none"/>'
    b+='<path d="M780 410Q800 380 830 400" stroke="#6b5a45" stroke-width="8" fill="none"/>'
    b+=tx(150,130,'Область питания','Accumulation zone')+tx(560,395,'Область абляции (таяния)','Ablation zone',big=False)+tx(640,520,'Талая вода → река','Meltwater → river','start',False)+tx(40,520,'Снег прибавляется выше линии равновесия и тает ниже неё','Snow gains above the equilibrium line and melts below it',big=False)
    b+=tx(700,440,'Морена','Moraine','start',False)
    svg('20-M-glacier-zones-bilingual.svg','Как устроен ледник','How a glacier works',1000,660,b)
    add('20','## 20.3. ','20-M-glacier-zones-bilingual.svg','Ледник: область питания, линия равновесия, область таяния, морена.','Glacier: accumulation zone, equilibrium line, ablation zone, moraine.')
# 20.5 режимы стока
def regimes():
    x0,y0,w,h=110,130,780,260; b=f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#fff" stroke="#9aa9b6"/>'
    def curve(f,c,dash=''):
        pts=' '.join(f'{x0+i*w/60:.0f},{y0+h-f(i/60)*h*0.85-10:.0f}' for i in range(61)); return f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="4" {dash}/>'
    b+=curve(lambda t:0.1+0.9*math.exp(-((t-0.42)/0.12)**2),'#2e86c1')+curve(lambda t:0.1+0.9*math.exp(-((t-0.62)/0.14)**2),'#7b4fb0')+curve(lambda t:0.1+0.5*math.exp(-((t-0.3)/0.1)**2)+0.3*math.exp(-((t-0.8)/0.1)**2),'#2e8b57','stroke-dasharray="9 6"')
    for i,m in enumerate('ЯФМАМИИАСОНД'): b+=f'<text x="{x0+(i+.5)*w/12:.0f}" y="{y0+h+24}" class="r2" text-anchor="middle">{m}</text>'
    b+=f'<text x="{x0-10}" y="{y0+10}" class="e2" text-anchor="end">расход</text><text x="{x0-10}" y="{y0+28}" class="e2" text-anchor="end">flow</text>'
    b+='<line x1="130" y1="470" x2="170" y2="470" stroke="#2e86c1" stroke-width="5"/>'+tx(180,468,'Снеговое питание — пик весной','Snow-fed — spring peak',big=False)
    b+='<line x1="130" y1="520" x2="170" y2="520" stroke="#7b4fb0" stroke-width="5"/>'+tx(180,518,'Ледниковое питание — пик в разгар лета','Glacier-fed — peak in mid-summer',big=False)
    b+='<line x1="130" y1="570" x2="170" y2="570" stroke="#2e8b57" stroke-width="5" stroke-dasharray="9 6"/>'+tx(180,568,'Смешанное: два пика (весна и осень, дождь)','Mixed: two peaks (spring and autumn rain)',big=False)
    svg('20-M-river-regimes-bilingual.svg','Режимы питания рек','River flow regimes',1000,690,b,'Схематичные кривые; не данные конкретных рек.','Schematic curves; not data for specific rivers.')
    add('20','## 20.5. ','20-M-river-regimes-bilingual.svg','Годовой ход стока рек разного питания (схема).','Annual flow of rivers with different sources (schematic).')
# 26 пик талой воды
def peak():
    x0,y0,w,h=110,130,780,300; b=f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#fff" stroke="#9aa9b6"/>'
    f=lambda t:0.25+0.7*math.exp(-((t-0.4)/0.22)**2)*(1 if t<0.4 else 1)
    pts=' '.join(f'{x0+i*w/60:.0f},{y0+h-f(i/60)*h*0.9:.0f}' for i in range(61)); b+=f'<polyline points="{pts}" fill="none" stroke="#2e86c1" stroke-width="5"/>'
    px=x0+0.4*w; b+=f'<path d="M{px:.0f} {y0}V{y0+h}" stroke="#c0392b" stroke-dasharray="7 5"/><text x="{px+8:.0f}" y="{y0+20}" class="r2" style="fill:#c0392b">«Пик воды» / peak water</text>'
    b+=f'<text x="{x0+w/2}" y="{y0+h+28}" class="r2" text-anchor="middle">время → / time →</text><text x="{x0}" y="{y0-26}" class="r2">сток от ледников</text><text x="{x0}" y="{y0-8}" class="e2">glacier runoff</text>'
    b+=tx(110,500,'Сначала ледник тает быстрее — талого стока больше. Затем льда становится мало, и сток от ледников падает.','First the glacier melts faster and meltwater grows. Later little ice remains and glacier runoff falls.',big=False)
    svg('26-M-peak-water-bilingual.svg','«Пик воды»: что происходит с ледниковым стоком','«Peak water»: what happens to glacier runoff',1000,620,b,'Общая схема; время «пика» зависит от ледника.','A general scheme; the timing of the peak depends on the glacier.')
    add('26','## 26.3. ','26-M-peak-water-bilingual.svg','Схема «пика воды» при таянии ледников.','The «peak water» scheme for melting glaciers.')
# 26.4 деградация пастбищ
def pasture():
    cx,cy=500,330; steps=[('Перевыпас','Overgrazing'),('Меньше трав и корней','Less vegetation and roots'),('Почва без защиты','Unprotected soil'),('Эрозия, сели, засуха','Erosion, mudflows, drought'),('Меньше корма','Less fodder')]
    b=''
    for i,(r,e) in enumerate(steps):
        a=-math.pi/2+i*2*math.pi/5; x=cx+250*math.cos(a); y=cy+190*math.sin(a)
        b+=bx(int(x-120),int(y-35),240,70,'#f4d9cf' if i==0 else '#f3e6b0')+f'<text x="{x:.0f}" y="{y-2:.0f}" class="r2" text-anchor="middle">{r}</text><text x="{x:.0f}" y="{y+19:.0f}" class="e2" text-anchor="middle">{e}</text>'
        a2=-math.pi/2+(i+1)*2*math.pi/5; x2=cx+250*math.cos(a2); y2=cy+190*math.sin(a2)
        b+=ar(int(x+(x2-x)*0.38),int(y+(y2-y)*0.38),int(x+(x2-x)*0.62),int(y+(y2-y)*0.62))
    b+=tx(500,cy-5,'Порочный круг','Vicious circle','middle')
    b+=tx(40,590,'Разорвать круг помогает ротация пастбищ, учёт нагрузки и восстановление трав.','Pasture rotation, stocking limits and restoring vegetation break the circle.',big=False)
    svg('26-M-pasture-degradation-cycle-bilingual.svg','Круг деградации пастбищ','The pasture degradation cycle',1000,680,b)
    add('26','## 26.4. ','26-M-pasture-degradation-cycle-bilingual.svg','Порочный круг деградации пастбищ.','The vicious circle of pasture degradation.')
# 13.13 цикл мониторинга
def monitor():
    steps=[('Вопрос и цели','Question and goals'),('Показатели','Indicators'),('Наблюдения','Observations'),('Анализ и оценка','Analysis and assessment'),('Решение и действия','Decision and action'),('Проверка результата','Check the result')]
    b=''
    for i,(r,e) in enumerate(steps):
        a=-math.pi/2+i*2*math.pi/6; x=500+300*math.cos(a); y=330+200*math.sin(a)
        b+=bx(int(x-125),int(y-35),250,70,'#d6e6f3')+f'<text x="{x:.0f}" y="{y-2:.0f}" class="r2" text-anchor="middle">{i+1}. {r}</text><text x="{x:.0f}" y="{y+19:.0f}" class="e2" text-anchor="middle">{e}</text>'
        a2=-math.pi/2+(i+1)*2*math.pi/6; x2=500+300*math.cos(a2); y2=330+200*math.sin(a2)
        b+=ar(int(x+(x2-x)*0.4),int(y+(y2-y)*0.4),int(x+(x2-x)*0.62),int(y+(y2-y)*0.62))
    b+=tx(500,325,'Цикл мониторинга','Monitoring cycle','middle')
    svg('13-M-monitoring-cycle-bilingual.svg','Цикл экологического мониторинга','The environmental monitoring cycle',1000,640,b)
    add('13','## 13.13. ','13-M-monitoring-cycle-bilingual.svg','Цикл мониторинга: от вопроса до проверки результата.','Monitoring cycle: from question to checking results.')
for f in (scale,planetary,risk,climo,chain,lakezones,soil,coords,topo,mapanatomy,sampling,oro,glacier,regimes,peak,pasture,monitor): f()
json.dump(items,open('/home/claude/geo/concept_items.json','w'),ensure_ascii=False); print(len(items))
