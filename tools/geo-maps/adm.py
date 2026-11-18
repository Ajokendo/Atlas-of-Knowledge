# -*- coding: utf-8 -*-
"""Административное деление Кыргызстана: 7 областей, 2 города республиканского значения, 40 районов.
Границы областей — Natural Earth (public domain, ne_10m_admin_1); районов — geoBoundaries KGZ-ADM2 (CC BY-SA 3.0, границы 2010 г.).
Запуск: python3 adm.py -> geography/assets/diagrams/24-M*.svg, 24-R-*.svg и /home/claude/geo/adm_items.json"""
import json, math
from shapely.geometry import shape, mapping
from shapely.ops import unary_union, polylabel
from kit import esc
NE='/home/claude/ne/'
OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams/'
# английское имя района в данных -> (рус., англ.)
OBL={ # ключ NE: (slug, рус., англ., цвет, центр рус., центр англ., (lon,lat))
 'Chuy':('chuy','Чуйская','Chuy','#f3d98b','Бишкек','Bishkek',(74.59,42.87)),
 'Talas':('talas','Таласская','Talas','#b7dba5','Талас','Talas',(72.24,42.52)),
 'Ysyk-Köl':('issyk-kul','Иссык-Кульская','Issyk-Kul','#a5d3e8','Каракол','Karakol',(78.39,42.49)),
 'Naryn':('naryn','Нарынская','Naryn','#d3c1e8','Нарын','Naryn',(76.0,41.43)),
 'Jalal-Abad':('jalal-abad','Джалал-Абадская','Jalal-Abad','#f1b9a3','Джалал-Абад','Jalal-Abad',(72.98,40.93)),
 'Osh':('osh','Ошская','Osh','#d9c3a0','Ош','Osh',(72.80,40.53)),
 'Batken':('batken','Баткенская','Batken','#9fd9cc','Баткен','Batken',(70.82,40.06)),
}
DIST={ # данные -> (рус., англ.)
 'Ysyk-Ata':('Ысык-Атинский','Ysyk-Ata'),'Chuy':('Чуйский','Chuy'),'Panfilov':('Панфиловский','Panfilov'),'Moskva':('Московский','Moskva'),
 'Kemin':('Кеминский','Kemin'),'Jayyl':('Жайыльский','Jayyl'),'Alamudun':('Аламудунский','Alamudun'),'Sokuluk':('Сокулукский','Sokuluk'),
 'Chong-Alay':('Чон-Алайский','Chong-Alay'),'Alay':('Алайский','Alay'),'Aravan':('Араванский','Aravan'),'Nookat':('Ноокатский','Nookat'),
 'Kara-Suu':('Кара-Суйский','Kara-Suu'),'Uzgen':('Узгенский','Uzgen'),'Kara-Kulja':('Кара-Кульджинский','Kara-Kulja'),
 'Batken':('Баткенский','Batken'),'Leilek':('Лейлекский','Leilek'),'Kadamjay':('Кадамжайский','Kadamjay'),
 'Ala-Buka':('Ала-Букинский','Ala-Buka'),'Suzak':('Сузакский','Suzak'),'Bazar-Korgon':('Базар-Коргонский','Bazar-Korgon'),'Nooken':('Ноокенский','Nooken'),
 'Aksy':('Аксыйский','Aksy'),'Chatkal':('Чаткальский','Chatkal'),'Toktogul':('Токтогульский','Toktogul'),'Toguz-Toro':('Тогуз-Тороуский','Toguz-Toro'),
 'At-Bashy':('Ат-Башинский','At-Bashy'),'Naryn':('Нарынский','Naryn'),'Ak-Talaa':('Ак-Талинский','Ak-Talaa'),'Jumgal':('Джумгальский','Jumgal'),'Kochkor':('Кочкорский','Kochkor'),
 'Jeti-Oguz':('Джети-Огузский','Jeti-Oguz'),'Ak-Suu':('Ак-Суйский','Ak-Suu'),'Tup':('Тюпский','Tup'),'Issyk Kul':('Иссык-Кульский','Issyk-Kul'),'Tong':('Тонский','Tong'),
 'Talas':('Таласский','Talas'),'Kara-Buura':('Кара-Бууринский','Kara-Buura'),'Bakay-Ata':('Бакай-Атинский','Bakay-Ata'),'Manas':('Манасский','Manas'),
}
ORDER={ # порядок номеров в легенде — с запада на восток примерно, как в справочниках (по алфавиту рус.)
}
CITIES={ # (рус., англ., lon, lat) — только уверенные координаты центров
 'Chuy':[('Токмок','Tokmok',75.30,42.84),('Кара-Балта','Kara-Balta',73.85,42.82)],
 'Talas':[('Кызыл-Адыр','Kyzyl-Adyr',71.60,42.60)] if False else [],
 'Ysyk-Köl':[('Чолпон-Ата','Cholpon-Ata',77.08,42.65),('Балыкчы','Balykchy',76.19,42.46)],
 'Naryn':[('Кочкор','Kochkor',75.75,42.22),('Ат-Башы','At-Bashy',75.80,41.17)],
 'Jalal-Abad':[('Токтогул','Toktogul',72.94,41.87),('Майлуу-Суу','Mailuu-Suu',72.45,41.27),('Кара-Куль','Kara-Kul',72.60,41.62)],
 'Osh':[('Узген','Uzgen',73.0,40.77),('Гульча','Gulcha',73.45,40.30)],
 'Batken':[('Кызыл-Кия','Kyzyl-Kiya',72.13,40.26),('Исфана','Isfana',69.53,39.83)],
}
STY=('text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:34px;font-weight:700}.sub{font-size:22px;fill:#526579}'
 '.n{font-size:22px;font-weight:700;text-anchor:middle}.ru{font-size:24px;font-weight:700}.en{font-size:20px;fill:#526579}'
 '.lb{font-size:22px;font-weight:700;paint-order:stroke;stroke:#fff;stroke-width:5px;stroke-linejoin:round}'
 '.lc{font-size:16px;fill:#44566a;paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.sm{font-size:16px}')
# ---------- данные
d2=json.load(open(NE+'geoBoundaries-KGZ-ADM2_simplified.geojson'))['features']
a1=[(f['properties']['name'],shape(f['geometry'])) for f in json.load(open(NE+'admin1.geojson'))['features'] if f['properties'].get('adm0_a3')=='KGZ']
countries={f['properties']['NAME']:shape(f['geometry']) for f in json.load(open(NE+'ne_10m_admin_0_countries.geojson'))['features']}
lake=[shape(f['geometry']) for f in json.load(open(NE+'ne_10m_lakes.geojson'))['features'] if (f['properties'].get('name') or '')=='Issyk-Kul'][0]
districts={}  # oblast -> [(key,geom)]
tokmok=None
for f in d2:
    g=shape(f['geometry']).buffer(0).simplify(0.003); k=f['properties']['shapeName']; p=g.representative_point()
    ob=[n for n,o in a1 if o.contains(p)][0]
    if k=='City of Tomok': tokmok=g; continue
    districts.setdefault(ob,[]).append((k,g))
assert sum(len(v) for v in districts.values())==40
oblast_geom={ob:unary_union([g for _,g in v]+([tokmok] if ob=='Chuy' and tokmok else [])) for ob,v in districts.items()}
kg=unary_union(list(oblast_geom.values()))
from shapely.geometry import box as _box
_clip=_box(kg.bounds[0]-1.2,kg.bounds[1]-1.2,kg.bounds[2]+1.2,kg.bounds[3]+1.2)
countries={k:v.intersection(_clip).simplify(0.012) for k,v in countries.items() if k in ('China','Kazakhstan','Uzbekistan','Tajikistan','Kyrgyzstan')}
lake=lake.simplify(0.004)
# ---------- проекция
class Pj:
    def __init__(s,bounds,x,y,w,h,pad=0.04):
        x0,y0,x1,y1=bounds; dx=(x1-x0)*pad; dy=(y1-y0)*pad; x0-=dx;x1+=dx;y0-=dy;y1+=dy
        s.c=math.cos(math.radians((y0+y1)/2)); k=min(w/((x1-x0)*s.c),h/(y1-y0)); s.k=k
        s.ox=x+(w-(x1-x0)*s.c*k)/2; s.oy=y+(h-(y1-y0)*k)/2; s.x0=x0; s.y1=y1
    def __call__(s,lon,lat): return (s.ox+(lon-s.x0)*s.c*s.k, s.oy+(s.y1-lat)*s.k)
def ring(r,P): return 'M'+'L'.join('%.1f %.1f'%P(*c) for c in r.coords)+'Z'
def pth(g,P):
    gs=[g] if g.geom_type=='Polygon' else list(g.geoms)
    return ''.join(ring(p.exterior,P)+''.join(ring(i,P) for i in p.interiors) for p in gs if p.geom_type=='Polygon')
def pole(g):
    gs=[g] if g.geom_type=='Polygon' else list(g.geoms)
    big=max(gs,key=lambda p:p.area); q=polylabel(big,0.01); return q.x,q.y
def star(x,y,r=15):
    pts=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5; rr=r if i%2==0 else r*0.42; pts.append('%.1f,%.1f'%(x+rr*math.cos(a),y+rr*math.sin(a)))
    return f'<polygon points="{" ".join(pts)}" fill="#c0392b" stroke="#fff" stroke-width="2.5"/>'
def ctx(P,hl=None,fill_other='#eceff2'):
    s=''
    for n in ('China','Kazakhstan','Uzbekistan','Tajikistan'):
        s+=f'<path d="{pth(countries[n],P)}" fill="#f4f6f8" stroke="#cdd5dc" stroke-width="1.2" fill-rule="evenodd"/>'
    s+=f'<path d="{pth(countries["Kyrgyzstan"],P)}" fill="{fill_other}" stroke="none"/>'
    return s
def head(ru,en,W,H,sub,body,foot_ru,foot_en):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"><title id="t">{esc(ru)} / {esc(en)}</title><desc id="d">{esc(sub)}</desc><style>{STY}</style>'
     f'<rect width="{W}" height="{H}" fill="#fbfcfe"/><text x="30" y="46" class="h">{esc(ru)}</text><text x="30" y="76" class="sub">{esc(en)}</text>{body}'
     f'<text x="30" y="{H-38}" class="sm">{esc(foot_ru)}</text><text x="30" y="{H-16}" class="sm" style="fill:#526579">{esc(foot_en)}</text></svg>')
FOOT=('Области — Natural Earth (общественное достояние); районы — geoBoundaries (CC BY-SA 3.0), 2010 г.',
      'Regions — Natural Earth (public domain); districts — geoBoundaries (CC BY-SA 3.0), as of 2010.')
items=[]
def save(fn,svg): open(OUT+fn,'w',encoding='utf-8').write(svg)
# ---------- 1. семь областей
def overview():
    W,H=1000,720; P=Pj(kg.bounds,30,100,W-60,H-100-110,0.03); s=ctx(P)
    for ob,g in oblast_geom.items():
        s+=f'<path d="{pth(g,P)}" fill="{OBL[ob][3]}" stroke="#fff" stroke-width="2" fill-rule="evenodd"/>'
    s+=f'<path d="{pth(lake,P)}" fill="#8fc3e3" stroke="#5d9bc4" stroke-width="1.5"/>'
    for ob,g in oblast_geom.items():
        s+=f'<path d="{pth(g,P)}" fill="none" stroke="#4d6577" stroke-width="2.4" stroke-linejoin="round" fill-rule="evenodd"/>'
    off={'Chuy':(-40,-88),'Talas':(-20,-20),'Ysyk-Köl':(36,-62),'Naryn':(0,10),'Jalal-Abad':(-30,-34),'Osh':(70,-5),'Batken':(10,34)}
    for ob,(sl,ru,en,col,cr,ce,(lo,la)) in OBL.items():
        x,y=pole(oblast_geom[ob]); x,y=P(x,y); dx,dy=off[ob]; n=len(districts[ob])
        nru=f'{n} районов' if n>4 else f'{n} района'
        s+=f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" class="lb" text-anchor="middle">{esc(ru)}</text><text x="{x+dx:.0f}" y="{y+dy+21:.0f}" class="lc" text-anchor="middle">{esc(en)} · {n}</text>'
    for ob,(sl,ru,en,col,cr,ce,(lo,la)) in OBL.items():
        x,y=P(lo,la)
        if cr=='Бишкек' or cr=='Ош': continue
        s+=star(x,y)+f'<text x="{x+16:.0f}" y="{y+6:.0f}" class="lc" style="font-size:17px;font-weight:700">{cr}</text>'
    for ru,en,lo,la,dx,dy,anc in (('Бишкек','Bishkek',74.59,42.87,-16,-14,'end'),('Ош','Osh',72.80,40.53,-16,22,'end')):
        x,y=P(lo,la); s+=f'<rect x="{x-9:.0f}" y="{y-9:.0f}" width="18" height="18" fill="#c0392b" stroke="#fff" stroke-width="2.5"/><text x="{x+dx:.0f}" y="{y+dy:.0f}" class="lb" text-anchor="{anc}" style="font-size:19px">{ru}</text>'
    # легенда
    ly=H-100
    s+=star(48,ly,13)+'<text x="72" y="%d" class="ru" style="font-size:19px">Областной центр</text><text x="72" y="%d" class="en" style="font-size:16px">Regional centre</text>'%(ly+6,ly+26)
    s+=f'<rect x="320" y="{ly-9}" width="18" height="18" fill="#c0392b" stroke="#fff" stroke-width="2.5"/><text x="350" y="{ly+6}" class="ru" style="font-size:19px">Город республиканского значения</text><text x="350" y="{ly+26}" class="en" style="font-size:16px">City of republican significance</text>'
    save('24-M-seven-regions-real-bilingual.svg',head('Семь областей и два города республиканского значения','Seven regions and two cities of republican significance',W,H,'Административная карта Кыргызстана: 7 областей, Бишкек и Ош',s,*FOOT))
    items.append(['24','## 24.2. ','24-M-seven-regions-real-bilingual.svg','Административное деление Кыргызстана: 7 областей, города Бишкек и Ош.','Administrative division of Kyrgyzstan: 7 regions, the cities of Bishkek and Osh.'])
# ---------- 2. 40 районов
def allmap():
    W,H=1000,720; P=Pj(kg.bounds,30,100,W-60,H-100-110,0.03); s=ctx(P)
    for ob,v in districts.items():
        for k,g in v: s+=f'<path d="{pth(g,P)}" fill="{OBL[ob][3]}" stroke="#fff" stroke-width="1.6" fill-rule="evenodd"/>'
    if tokmok: s+=f'<path d="{pth(tokmok,P)}" fill="#8a96a3" stroke="#fff" stroke-width="1"/>'
    s+=f'<path d="{pth(lake,P)}" fill="#8fc3e3" stroke="#5d9bc4" stroke-width="1.5"/>'
    for ob,g in oblast_geom.items(): s+=f'<path d="{pth(g,P)}" fill="none" stroke="#3f566a" stroke-width="3" stroke-linejoin="round" fill-rule="evenodd"/>'
    for ob,(sl,ru,en,col,cr,ce,ll) in OBL.items():
        x,y=P(*pole(oblast_geom[ob])); n=len(districts[ob])
        off={'Chuy':(-30,-60),'Ysyk-Köl':(34,-70),'Naryn':(0,20),'Jalal-Abad':(-34,-40),'Osh':(60,10),'Batken':(10,38),'Talas':(-26,-26)}[ob]
        s+=f'<text x="{x+off[0]:.0f}" y="{y+off[1]:.0f}" class="lb" text-anchor="middle">{esc(ru)}</text><text x="{x+off[0]:.0f}" y="{y+off[1]+21:.0f}" class="lc" text-anchor="middle" style="font-size:17px">{n} {"районов" if n>4 else "района"} / {n} districts</text>'
    ly=H-98
    s+=f'<rect x="30" y="{ly-12}" width="26" height="16" fill="none" stroke="#3f566a" stroke-width="3"/><text x="68" y="{ly+2}" class="ru" style="font-size:19px">Граница области</text><text x="68" y="{ly+22}" class="en" style="font-size:16px">Region boundary</text>'
    s+=f'<rect x="330" y="{ly-12}" width="26" height="16" fill="#cfd8df" stroke="#fff" stroke-width="2"/><text x="368" y="{ly+2}" class="ru" style="font-size:19px">Граница района (всего 40)</text><text x="368" y="{ly+22}" class="en" style="font-size:16px">District boundary (40 in total)</text>'
    s+=f'<rect x="690" y="{ly-12}" width="26" height="16" fill="#8a96a3"/><text x="728" y="{ly+2}" class="ru" style="font-size:19px">Токмок</text><text x="728" y="{ly+22}" class="en" style="font-size:16px">Tokmok (city)</text>'
    save('24-M2-forty-districts-bilingual.svg',head('40 районов Кыргызстана','The 40 districts of Kyrgyzstan',W,H,'Карта районов Кыргызстана с границами областей',s,*FOOT))
    items.append(['24','## 24.2. ','24-M2-forty-districts-bilingual.svg','Сорок районов Кыргызстана в границах семи областей.','The 40 districts of Kyrgyzstan within the seven regions.'])
# ---------- 3. карта области
PAL=['#f6c6a8','#bfe0b5','#a9d3ea','#e3c7ef','#f4e29a','#f0b7c4','#b6d9d3','#d9cdb0']
def region(ob):
    sl,ru,en,col,cr,ce,(clo,cla)=OBL[ob]
    W=900; ds=sorted(districts[ob],key=lambda kv:DIST[kv[0]][0]); n=len(ds)
    g=oblast_geom[ob]; P0=g.bounds
    asp=((P0[3]-P0[1])*1.0)/((P0[2]-P0[0])*math.cos(math.radians((P0[1]+P0[3])/2)))
    mh=int(min(520,(W-60)*asp*1.1+40)); P=Pj(P0,30,96,W-60,mh,0.05); s=ctx(P)
    # соседние области светло-серым
    for o2,g2 in oblast_geom.items():
        if o2!=ob: s+=f'<path d="{pth(g2,P)}" fill="#e3e8ec" stroke="#fff" stroke-width="1.5" fill-rule="evenodd"/>'
    for i,(k,gg) in enumerate(ds): s+=f'<path d="{pth(gg,P)}" fill="{PAL[i%8]}" stroke="#fff" stroke-width="2" fill-rule="evenodd"/>'
    if ob=='Chuy' and tokmok: s+=f'<path d="{pth(tokmok,P)}" fill="#8a96a3" stroke="#fff" stroke-width="1"/>'
    if lake.intersects(g): s+=f'<path d="{pth(lake,P)}" fill="#8fc3e3" stroke="#5d9bc4" stroke-width="1.5"/>'
    s+=f'<path d="{pth(g,P)}" fill="none" stroke="#3f566a" stroke-width="3.4" stroke-linejoin="round" fill-rule="evenodd"/>'
    for i,(k,gg) in enumerate(ds):
        from shapely.geometry import Point
        avoid=unary_union([Point(clo,cla).buffer(0.15),Point(72.80,40.53).buffer(0.15)]+[Point(c[2],c[3]).buffer(0.15) for c in CITIES.get(ob,[])])
        gp=gg.difference(avoid); gp=gp if not gp.is_empty and gp.area>gg.area*0.4 else gg
        x,y=P(*pole(gp)); s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="#fff" stroke="#3f566a" stroke-width="2"/><text x="{x:.0f}" y="{y+7.5:.0f}" class="n">{i+1}</text>'
    for r_,e_,lo,la in CITIES.get(ob,[]):
        if not g.buffer(-0.03).contains(__import__('shapely.geometry',fromlist=['Point']).Point(lo,la)): continue
        x,y=P(lo,la); s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5.5" fill="#44566a" stroke="#fff" stroke-width="2"/><text x="{x+9:.0f}" y="{y+5:.0f}" class="lc" style="font-size:17px">{esc(r_)}</text>'
    if ob=='Chuy' and tokmok: pass
    x,y=P(clo,cla)
    if ob=='Osh': pass
    elif ob=='Chuy': s+=f'<rect x="{x-9:.0f}" y="{y-9:.0f}" width="18" height="18" fill="#c0392b" stroke="#fff" stroke-width="2.5"/><text x="{x+13:.0f}" y="{y-10:.0f}" class="lb" style="font-size:19px">Бишкек</text>'
    else: s+=star(x,y,15)+f'<text x="{x+17:.0f}" y="{y-8:.0f}" class="lb" style="font-size:19px">{cr}</text>'
    if ob=='Osh':
        x,y=P(72.80,40.53); s+=f'<rect x="{x-9:.0f}" y="{y-9:.0f}" width="18" height="18" fill="#c0392b" stroke="#fff" stroke-width="2.5"/><text x="{x-14:.0f}" y="{y+6:.0f}" class="lb" text-anchor="end" style="font-size:19px">Ош</text>'
    # легенда
    ly=96+mh+34; rows=math.ceil(n/2)
    s+=f'<text x="30" y="{ly}" class="ru">Районы</text><text x="128" y="{ly}" class="en">/ Districts</text>'
    for i,(k,gg) in enumerate(ds):
        cx=30+(i//rows)*265; cy=ly+36+(i%rows)*56
        s+=f'<circle cx="{cx+17}" cy="{cy}" r="17" fill="{PAL[i%8]}" stroke="#3f566a" stroke-width="2"/><text x="{cx+17}" y="{cy+7.5}" class="n">{i+1}</text><text x="{cx+44}" y="{cy-1}" class="ru" style="font-size:21px">{DIST[k][0]}</text><text x="{cx+44}" y="{cy+19}" class="en" style="font-size:17px">{DIST[k][1]}</text>'
    # локатор
    LP=Pj(kg.bounds,585,ly-8,285,rows*56+30,0.02)
    s+=f'<path d="{pth(kg,LP)}" fill="#e3e8ec" stroke="#9aa9b6" stroke-width="1.2" fill-rule="evenodd"/><path d="{pth(g,LP)}" fill="{col}" stroke="#3f566a" stroke-width="1.8" fill-rule="evenodd"/>'
    H=ly+36+rows*56+66
    save(f'24-R-{sl}-districts-bilingual.svg',head(f'{ru} область: районы',f'{en} Region: districts',W,H,f'Районы {ru} области',s,*FOOT))
    h={'chuy':'## 24.3. ','talas':'## 24.4. ','issyk-kul':'## 24.5. ','naryn':'## 24.6. ','jalal-abad':'## 24.7. ','osh':'## 24.8. ','batken':'## 24.9. '}[sl]
    items.append(['24',h,f'24-R-{sl}-districts-bilingual.svg',f'{ru} область: {n} {"районов" if n>4 else "района"} на карте.',f'{en} Region: {n} districts on the map.'])
overview(); allmap()
for ob in OBL: region(ob)
json.dump(items,open('/home/claude/geo/adm_items.json','w'),ensure_ascii=False)
print(len(items),'maps')
