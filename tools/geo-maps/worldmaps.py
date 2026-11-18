# -*- coding: utf-8 -*-
"""Мировые и региональные карты на данных Natural Earth (общественное достояние).
09-H население стран; 12-K подрегионы мира (геосхема ООН); 10-H/17-H Центральная Азия и соседи Кыргызстана.
Запуск: python3 worldmaps.py -> geography/assets/diagrams + /home/claude/geo/world_items.json"""
import json, math
from shapely.geometry import shape, box, Point
from shapely.ops import unary_union, polylabel
from kit import esc
NE='/home/claude/ne/'; OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams/'
feats=json.load(open(NE+'ne_10m_admin_0_countries.geojson'))['features']
lakes=[shape(f['geometry']) for f in json.load(open(NE+'ne_10m_lakes.geojson'))['features']]
STY=('text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:34px;font-weight:700}.sub{font-size:22px;fill:#526579}'
 '.n{font-size:17px;font-weight:700;text-anchor:middle}.ru{font-size:21px;font-weight:700}.en{font-size:17px;fill:#526579}'
 '.lb{font-size:19px;font-weight:700;paint-order:stroke;stroke:#fff;stroke-width:4.5px;stroke-linejoin:round}'
 '.lc{font-size:15px;fill:#44566a;paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.sm{font-size:15px}')
def head(ru,en,W,H,desc,body,fru,fen):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"><title id="t">{esc(ru)} / {esc(en)}</title><desc id="d">{esc(desc)}</desc><style>{STY}</style>'
     f'<rect width="{W}" height="{H}" fill="#fbfcfe"/><text x="30" y="46" class="h">{esc(ru)}</text><text x="30" y="76" class="sub">{esc(en)}</text>{body}'
     f'<text x="30" y="{H-38}" class="sm">{esc(fru)}</text><text x="30" y="{H-16}" class="sm" style="fill:#526579">{esc(fen)}</text></svg>')
def ring(r,P): return 'M'+'L'.join('%.1f %.1f'%P(*c) for c in r.coords)+'Z'
def pth(g,P):
    gs=[g] if g.geom_type=='Polygon' else [x for x in g.geoms if x.geom_type=='Polygon']
    return ''.join(ring(p.exterior,P)+''.join(ring(i,P) for i in p.interiors) for p in gs)
def EE(lon,lat):  # Equal Earth
    A1,A2,A3,A4=1.340264,-0.081106,0.000893,0.003796
    l=math.radians(lon); th=math.asin(math.sqrt(3)/2*math.sin(math.radians(lat))); t2=th*th; t6=t2**3
    x=2*math.sqrt(3)*l*math.cos(th)/(3*(9*A4*t6*t2+7*A3*t6+3*A2*t2+A1)); y=th*(A1+A2*t2+A3*t6+A4*t6*t2)
    return x,y
class World:
    def __init__(s,x,y,w):
        s.s=w/(EE(180,0)[0]*2); s.x=x+w/2; s.y=y+EE(0,84)[1]*s.s
    def __call__(s,lon,lat):
        a,b=EE(lon,lat); return s.x+a*s.s, s.y-b*s.s
    height=property(lambda s:(EE(0,84)[1]-EE(0,-58)[1])*s.s)
def prep(f,tol=0.12,minarea=0.4):
    g=shape(f['geometry']).buffer(0)
    gs=[g] if g.geom_type=='Polygon' else list(g.geoms)
    keep=[p for p in gs if p.area>=minarea] or [max(gs,key=lambda p:p.area)]
    return unary_union(keep).simplify(tol)
def pole(g):
    gs=[g] if g.geom_type=='Polygon' else list(g.geoms); big=max(gs,key=lambda p:p.area); q=polylabel(big,0.05); return q.x,q.y
items=[]
def save(fn,svg): open(OUT+fn,'w',encoding='utf-8').write(svg)
FOOT_NE=('Данные и контуры — Natural Earth (общественное достояние).','Data and outlines — Natural Earth (public domain).')
# ---------- 09-H население стран
def pop_map():
    W=1000; P=World(20,100,W-40); mh=P.height; H=int(100+mh+190)
    cls=[(1e9,'#8c2d04','≥ 1 млрд','≥ 1 billion'),(1e8,'#d95f1f','100 млн – 1 млрд','100 million – 1 billion'),(3e7,'#ee8a4c','30 – 100 млн','30 – 100 million'),
         (1e7,'#f9b57a','10 – 30 млн','10 – 30 million'),(1e6,'#fdd8ae','1 – 10 млн','1 – 10 million'),(0,'#fff1e0','< 1 млн','< 1 million')]
    def col(p):
        for t,c,_,_ in cls:
            if p>=t: return c
    s=f'<rect x="20" y="100" width="{W-40}" height="{mh:.0f}" fill="#eef4f9"/>'
    lab=[]
    for f in feats:
        p=f['properties']
        if p['CONTINENT'] in ('Antarctica','Seven seas (open ocean)'): continue
        g=prep(f)
        s+=f'<path d="{pth(g,P)}" fill="{col(p["POP_EST"])}" stroke="#fff" stroke-width="0.6" fill-rule="evenodd"/>'
        if p['POP_EST']>=2.0e8 and p['NAME']!='United States of America' or p['NAME']=='United States of America':
            lab.append((p['NAME_RU'] if p['NAME']!='United States of America' else 'США',p['NAME'] if p['NAME']!='United States of America' else 'USA',p['POP_EST'],pole(g)))
    manual={'Китайская Народная Республика':('Китай',(103,35)),'Индия':('Индия',(79,21)),'Пакистан':('Пакистан',(66,26.5))}
    for ru,en,pop,(lo,la) in lab:
        if ru in manual: ru,(lo,la)=manual[ru]
        x,y=P(lo,la); s+=f'<text x="{x:.0f}" y="{y:.0f}" class="lb" text-anchor="middle" style="font-size:17px">{esc(ru)}</text><text x="{x:.0f}" y="{y+17:.0f}" class="lc" text-anchor="middle">{pop/1e6:,.0f} млн / M'.replace(',',' ')+'</text>'
    kg=[f for f in feats if f['properties']['NAME']=='Kyrgyzstan'][0]; kp=kg['properties']; x,y=P(74.6,41.5)
    s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="none" stroke="#1b4f9c" stroke-width="3"/><path d="M{x:.0f} {y-6:.0f}L{x+6:.0f} {y-52:.0f}" stroke="#1b4f9c" stroke-width="2"/><text x="{x+6:.0f}" y="{y-58:.0f}" class="lb" style="font-size:17px;fill:#1b4f9c">Кыргызстан ≈ {kp["POP_EST"]/1e6:.1f} млн</text><text x="{x+6:.0f}" y="{y-40:.0f}" class="lc">Kyrgyzstan ≈ {kp["POP_EST"]/1e6:.1f} M</text>'
    ly=100+mh+30
    for i,(t,c,r,e) in enumerate(cls):
        cx=30+(i%3)*320; cy=ly+(i//3)*54
        s+=f'<rect x="{cx}" y="{cy-16}" width="34" height="24" fill="{c}" stroke="#9aa9b6"/><text x="{cx+46}" y="{cy}" class="ru" style="font-size:19px">{esc(r)}</text><text x="{cx+46}" y="{cy+20}" class="en" style="font-size:15px">{esc(e)}</text>'
    save('09-H-world-population-by-country-bilingual.svg',head('Население стран мира','Population of the world\'s countries',W,H,'Карта стран мира по численности населения',s,'Оценки численности — Natural Earth, около 2019 г.; контуры — Natural Earth (общественное достояние).','Population estimates — Natural Earth, c. 2019; outlines — Natural Earth (public domain). Equal Earth projection.'))
    items.append(['09','## 9.2. ','09-H-world-population-by-country-bilingual.svg','Страны мира по численности населения (оценки около 2019 г.).','Countries of the world by population (estimates c. 2019).','Карта по открытым данным.','Map from open data.'])
# ---------- 12-K подрегионы мира
SUB=[ # key, рус, англ, цвет
 ('Northern Africa','Северная Африка','Northern Africa','#f6c28b'),('Western Africa','Западная Африка','Western Africa','#f2a65a'),('Middle Africa','Центральная Африка','Middle Africa','#e8893a'),
 ('Eastern Africa','Восточная Африка','Eastern Africa','#f7d7a8'),('Southern Africa','Южная Африка','Southern Africa','#d9732a'),
 ('Northern America','Северная Америка','Northern America','#a9d8a0'),('Central America','Центральная Америка','Central America','#7cc47a'),('Caribbean','Карибы','Caribbean','#c8e8b8'),('South America','Южная Америка','South America','#58ad5d'),
 ('Northern Europe','Северная Европа','Northern Europe','#9cc4ec'),('Western Europe','Западная Европа','Western Europe','#6fa6df'),('Eastern Europe','Восточная Европа','Eastern Europe','#c3dbf5'),('Southern Europe','Южная Европа','Southern Europe','#4d8bd0'),
 ('Western Asia','Западная Азия','Western Asia','#d9b8ec'),('Central Asia','Центральная Азия','Central Asia','#e84a8a'),('Southern Asia','Южная Азия','Southern Asia','#b98ad8'),('Eastern Asia','Восточная Азия','Eastern Asia','#f0a0c8'),('South-Eastern Asia','Юго-Восточная Азия','South-Eastern Asia','#9a6fc4'),
 ('Australia and New Zealand','Австралия и Новая Зеландия','Australia and New Zealand','#6fcfc4'),('Melanesia','Меланезия','Melanesia','#a6e3dc'),('Micronesia','Микронезия','Micronesia','#46b5aa'),('Polynesia','Полинезия','Polynesia','#cdeeea'),
]
def sub_map():
    W=1000; P=World(20,100,W-40); mh=P.height
    rows=8; H=int(100+mh+30+rows*46+90)
    s=f'<rect x="20" y="100" width="{W-40}" height="{mh:.0f}" fill="#eef4f9"/>'
    col={k:c for k,_,_,c in SUB}; groups={k:[] for k in col}
    for f in feats:
        p=f['properties']; k=p['SUBREGION']
        if k not in col: continue
        g=prep(f,0.12,0.0 if k in ('Micronesia','Polynesia','Melanesia','Caribbean') else 0.4); groups[k].append(g)
        s+=f'<path d="{pth(g,P)}" fill="{col[k]}" stroke="{'#3f566a' if k in ('Micronesia','Polynesia') else '#fff'}" stroke-width="{1.2 if k in ('Micronesia','Polynesia') else 0.7}" fill-rule="evenodd"/>'
    pos={'Caribbean':(-76,19),'Polynesia':(-150,-17),'Micronesia':(150,8),'Melanesia':(147,-6),'South-Eastern Asia':(108,5),'Western Europe':(5,48),'Southern Europe':(15,41.5),'Northern Europe':(15,62)}
    for i,(k,ru,en,c) in enumerate(SUB):
        if k in pos: lo,la=pos[k]
        else: lo,la=pole(unary_union(groups[k]))
        x,y=P(lo,la); s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="11" fill="#fff" stroke="#3f566a" stroke-width="1.6"/><text x="{x:.0f}" y="{y+6:.0f}" class="n">{i+1}</text>'
    ly=100+mh+36
    for i,(k,ru,en,c) in enumerate(SUB):
        cx=30+(i//rows)*325; cy=ly+(i%rows)*46
        s+=f'<circle cx="{cx+13}" cy="{cy}" r="13" fill="{c}" stroke="#3f566a" stroke-width="1.6"/><text x="{cx+13}" y="{cy+6}" class="n" style="font-size:14px">{i+1}</text><text x="{cx+36}" y="{cy}" class="ru" style="font-size:17px">{ru}</text><text x="{cx+36}" y="{cy+18}" class="en" style="font-size:14px">{en}</text>'
    save('12-K-world-subregions-bilingual.svg',head('Регионы мира: подрегионы ООН','World regions: UN geoscheme subregions',W,H,'Карта подрегионов мира',s,'Деление по геосхеме ООН в версии Natural Earth; контуры — Natural Earth (общественное достояние).','UN geoscheme subregions as coded in Natural Earth; outlines — Natural Earth (public domain). Equal Earth projection.'))
    items.append(['12','## 12.1. ','12-K-world-subregions-bilingual.svg','Подрегионы мира по геосхеме ООН.','World subregions by the UN geoscheme.','Одно из возможных делений: границы регионов условны.','One of several possible divisions; regional boundaries are conventional.'])
# ---------- Центральная Азия и соседи
CA=['Kazakhstan','Uzbekistan','Turkmenistan','Tajikistan','Kyrgyzstan']
CAC={'Kazakhstan':'#f3d98b','Uzbekistan':'#b7dba5','Turkmenistan':'#f1b9a3','Tajikistan':'#d3c1e8','Kyrgyzstan':'#e84a6a'}
CAN={'Kazakhstan':('Казахстан','Kazakhstan'),'Uzbekistan':('Узбекистан','Uzbekistan'),'Turkmenistan':('Туркменистан','Turkmenistan'),'Tajikistan':('Таджикистан','Tajikistan'),'Kyrgyzstan':('Кыргызстан','Kyrgyzstan')}
NB={'Russia':('Россия','Russia',(63,54.5)),'China':('Китай','China',(86,38.5)),'Afghanistan':('Афганистан','Afghanistan',(66.5,34)),'Iran':('Иран','Iran',(56.5,34)),'Mongolia':('Монголия','Mongolia',(89.2,47.3)),'Pakistan':('Пакистан','Pakistan',(70,33)),'Azerbaijan':('Азербайджан','Azerbaijan',(48.4,40.4))}
def ca_map():
    W,H=1000,760; x0,x1,y0,y1=44,92,33,56
    c=math.cos(math.radians(44)); k=min((W-60)/((x1-x0)*c),(H-100-110)/(y1-y0)); ox=30+((W-60)-(x1-x0)*c*k)/2; oy=100
    P=lambda lo,la:(ox+(lo-x0)*c*k, oy+(y1-la)*k)
    clip=box(x0-2,y0-2,x1+2,y1+2)
    s=f'<rect x="{ox:.0f}" y="{oy}" width="{(x1-x0)*c*k:.0f}" height="{(y1-y0)*k:.0f}" fill="#eef4f9"/><clipPath id="cp"><rect x="{ox:.0f}" y="{oy}" width="{(x1-x0)*c*k:.0f}" height="{(y1-y0)*k:.0f}"/></clipPath><g clip-path="url(#cp)">'
    for f in feats:
        p=f['properties']; g=shape(f['geometry']).buffer(0).intersection(clip)
        if g.is_empty: continue
        g=g.simplify(0.02); fill=CAC.get(p['NAME'],CAC['Kazakhstan'] if p['NAME'].startswith('Baikonur') or p['NAME'].startswith('Baykonur') else '#eceff2')
        s+=f'<path d="{pth(g,P)}" fill="{fill}" stroke="#fff" stroke-width="1.4" fill-rule="evenodd"/>'
    for lk in lakes:
        if lk.area>0.5 and lk.intersects(clip): s+=f'<path d="{pth(lk.intersection(clip).simplify(0.02),P)}" fill="#8fc3e3" stroke="#5d9bc4" stroke-width="1" fill-rule="evenodd"/>'
    for f in feats:
        p=f['properties']
        if p['NAME'] in CA:
            g=shape(f['geometry']).buffer(0).intersection(clip).simplify(0.02); s+=f'<path d="{pth(g,P)}" fill="none" stroke="#3f566a" stroke-width="2.2" fill-rule="evenodd"/>'
    s+='</g>'
    lp={'Kazakhstan':(67,48.5),'Uzbekistan':(60.2,43.4),'Turkmenistan':(59.8,40.8),'Tajikistan':(71.5,36.4),'Kyrgyzstan':(79.5,45.2)}
    for n,(lo,la) in lp.items():
        x,y=P(lo,la); ru,en=CAN[n]; fs=24 if n!='Kyrgyzstan' else 22
        s+=f'<text x="{x:.0f}" y="{y:.0f}" class="lb" text-anchor="middle" style="font-size:{fs}px">{ru}</text><text x="{x:.0f}" y="{y+19:.0f}" class="lc" text-anchor="middle">{en}</text>'
    for n,(a,b,c_) in {'Kyrgyzstan':((79.5,44.7),(76.5,42.2),0),'Tajikistan':((71.5,36.9),(70.8,38.5),0)}.items():
        (ax,ay),(bx,by)=P(*a),P(*b); s+=f'<path d="M{ax:.0f} {ay:.0f}L{bx:.0f} {by:.0f}" stroke="#3f566a" stroke-width="1.6"/>'
    for n,(ru,en,(lo,la)) in NB.items():
        x,y=P(lo,la); s+=f'<text x="{x:.0f}" y="{y:.0f}" class="lc" text-anchor="middle" style="font-size:17px;fill:#6b7b8a">{ru}</text>'
    for ru,en,lo,la,dx,dy,an in (('Астана','Astana',71.43,51.13,10,-8,'start'),('Ташкент','Tashkent',69.24,41.30,-10,22,'end'),('Ашхабад','Ashgabat',58.38,37.95,10,22,'start'),('Душанбе','Dushanbe',68.78,38.56,-10,20,'end'),('Бишкек','Bishkek',74.59,42.87,-8,-10,'end')):
        x,y=P(lo,la); s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#c0392b" stroke="#fff" stroke-width="2"/><text x="{x+dx:.0f}" y="{y+dy:.0f}" class="lc" text-anchor="{an}" style="font-size:16px;font-weight:700;fill:#243447">{ru}</text>'
    ly=H-100
    s+=f'<circle cx="42" cy="{ly}" r="6" fill="#c0392b" stroke="#fff" stroke-width="2"/><text x="60" y="{ly+6}" class="ru" style="font-size:18px">Столица</text><text x="140" y="{ly+6}" class="en" style="font-size:16px">/ Capital</text>'
    save('10-H-central-asia-neighbours-bilingual.svg',head('Центральная Азия и соседи Кыргызстана','Central Asia and the neighbours of Kyrgyzstan',W,H,'Политическая карта Центральной Азии',s,'Контуры — Natural Earth (общественное достояние); показаны границы де-факто по версии Natural Earth.','Outlines — Natural Earth (public domain); boundaries as coded in Natural Earth.'))
ca_map()
items.append(['10','## 10.4. ','10-H-central-asia-neighbours-bilingual.svg','Пять государств Центральной Азии и их соседи.','The five Central Asian states and their neighbours.','Политическая карта.','A political map.'])
items.append(['17','## 17.1. ','10-H-central-asia-neighbours-bilingual.svg','Кыргызстан среди соседей: Казахстан, Китай, Таджикистан, Узбекистан.','Kyrgyzstan among its neighbours: Kazakhstan, China, Tajikistan, Uzbekistan.','Политическая карта.','A political map.'])
pop_map(); sub_map()
json.dump(items,open('/home/claude/geo/world_items.json','w'),ensure_ascii=False)
print(len(items))
