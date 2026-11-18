import json, math, html
NE='/home/claude/ne/'
_c={}
def load(n):
    if n not in _c: _c[n]=json.load(open(NE+n+'.geojson'))
    return _c[n]
def esc(s): return html.escape(s,quote=False)
STYLE=('text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:31px;font-weight:700}.sub{font-size:19px}'
 '.t{font-size:23px;font-weight:700}.s{font-size:18px}.sm{font-size:15px}.lab{font-size:16px;font-weight:700}.it{font-style:italic}'
 '.box{stroke:#647789;stroke-width:2;rx:14}.arr{stroke:#526579;stroke-width:4;fill:none;marker-end:url(#arrow)}')
DEFS='<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="#526579"/></marker></defs>'
def wrap(ru,en,desc,body,fru,fen,w=1400,h=800):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{esc(ru)} / {esc(en)}</title><desc id="desc">{esc(desc)}</desc><style>{STYLE}</style>{DEFS}<rect width="{w}" height="{h}" fill="#fbfcfe"/>'
    s+=f'<text x="40" y="44" class="h">{esc(ru)}</text><text x="40" y="74" class="sub" style="fill:#526579">{esc(en)}</text>'
    s+=body
    s+=f'<text x="40" y="{h-34}" class="sm">{esc(fru)}</text><text x="40" y="{h-14}" class="sm" style="fill:#526579">{esc(fen)}</text>'
    return s+'</svg>'
def T(x,y,txt,cls='s',anchor='start',extra=''):
    return f'<text x="{x:.0f}" y="{y:.0f}" class="{cls}" text-anchor="{anchor}" {extra}>{esc(txt)}</text>'
def bi(x,y,ru,en,cls='s',anchor='start',dy=22):
    return T(x,y,ru,cls,anchor)+T(x,y+dy,en,cls,anchor,'style="fill:#526579"')
def box(x,y,w,h,fill='#e4eff6',stroke='#647789'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def arrow(x1,y1,x2,y2): return f'<path d="M{x1} {y1} L{x2} {y2}" class="arr"/>'
def pts(c):
    if not c: return
    if isinstance(c[0],(int,float)): yield c
    else:
        for x in c: yield from pts(x)
# ---------- projections
class Eq:  # local equirectangular with cos(lat0)
    def __init__(s,lon0,lon1,lat0,lat1,x,y,w,h):
        s.lon0,s.lat1=lon0,lat1; c=math.cos(math.radians((lat0+lat1)/2))
        k=min(w/((lon1-lon0)*c),h/(lat1-lat0)); s.k=k; s.c=c
        s.x=x+(w-(lon1-lon0)*c*k)/2; s.y=y+(h-(lat1-lat0)*k)/2
        s.b=(lon0,lon1,lat0,lat1)
    def __call__(s,lon,lat): return (s.x+(lon-s.lon0)*s.c*s.k, s.y+(s.lat1-lat)*s.k)
class Moll:
    def __init__(s,x,y,w,h): s.cx=x+w/2; s.cy=y+h/2; s.R=min(w/(4*math.sqrt(2)),h/(2*math.sqrt(2)))*1.0
    def __call__(s,lon,lat):
        p=math.radians(lat); t=p
        for _ in range(12):
            if abs(abs(p)-math.pi/2)<1e-9: break
            d=2*t+math.sin(2*t)-math.pi*math.sin(p); t-=d/(2+2*math.cos(2*t)+1e-12)
        l=math.radians(lon)
        return (s.cx+2*math.sqrt(2)/math.pi*s.R*l*math.cos(t), s.cy-math.sqrt(2)*s.R*math.sin(t))
class Polar: # south polar stereographic
    def __init__(s,cx,cy,R,lat_edge=-55):
        s.cx,s.cy=cx,cy; s.k=R/ (2*math.tan(math.radians((90+lat_edge)/2)))
    def __call__(s,lon,lat):
        r=2*s.k*math.tan(math.radians((90+lat)/2)); l=math.radians(lon)
        return (s.cx+r*math.sin(l), s.cy+r*math.cos(l))
def path_of(geom,P,clip=None,close=True):
    d=[]
    polys=[geom['coordinates']] if geom['type']=='Polygon' else geom['coordinates'] if geom['type']=='MultiPolygon' else None
    if polys is None:
        lines=[geom['coordinates']] if geom['type']=='LineString' else geom['coordinates']
        for ln in lines:
            if clip and not any(clip(p) for p in ln): continue
            d.append('M'+'L'.join('%.1f %.1f'%P(*p[:2]) for p in ln))
        return ''.join(d)
    for poly in polys:
        for ring in poly:
            if clip and not any(clip(p) for p in ring): continue
            d.append('M'+'L'.join('%.1f %.1f'%P(*p[:2]) for p in ring)+'Z')
    return ''.join(d)
def feats(name,flt=None): return [f for f in load(name)['features'] if f['geometry'] and (flt is None or flt(f['properties']))]
KG_BOX=(69.0,80.6,39.0,43.6)
def inbox(b):
    return lambda p: b[0]-0.5<p[0]<b[1]+0.5 and b[2]-0.5<p[1]<b[3]+0.5
# ---------- Kyrgyzstan base map
OBL={'Ysyk-Köl':('Иссык-Кульская','Issyk-Kul'),'Naryn':('Нарынская','Naryn'),'Osh':('Ошская','Osh'),'Chuy':('Чуйская','Chuy'),'Talas':('Таласская','Talas'),'Jalal-Abad':('Джалал-Абадская','Jalal-Abad'),'Batken':('Баткенская','Batken')}
PAL={'Ysyk-Köl':'#f4ecd9','Naryn':'#e5efe3','Osh':'#f5e7e4','Chuy':'#e4eff6','Talas':'#ece6f3','Jalal-Abad':'#f3efd7','Batken':'#e6f0ee','Bishkek':'#d9d9d9'}
CITIES={'Bishkek':(74.59,42.87,'Бишкек','Bishkek'),'Osh':(72.80,40.53,'Ош','Osh'),'Manas':(72.98,40.93,'Манас (б. Джалал-Абад)','Manas (formerly Jalal-Abad)'),
 'Karakol':(78.39,42.49,'Каракол','Karakol'),'Naryn':(76.0,41.43,'Нарын','Naryn'),'Talas':(72.24,42.52,'Талас','Talas'),'Batken':(70.82,40.06,'Баткен','Batken'),
 'Balykchy':(76.19,42.46,'Балыкчы','Balykchy'),'Tokmok':(75.30,42.84,'Токмок','Tokmok'),'Kara-Balta':(73.85,42.81,'Кара-Балта','Kara-Balta'),
 'Cholpon-Ata':(77.08,42.65,'Чолпон-Ата','Cholpon-Ata'),'Uzgen':(73.30,40.77,'Узген','Uzgen'),'Kara-Suu':(72.86,40.70,'Кара-Суу','Kara-Suu'),
 'Kyzyl-Kiya':(72.13,40.26,'Кызыл-Кыя','Kyzyl-Kiya'),'Toktogul':(72.94,41.88,'Токтогул','Toktogul'),'Kochkor':(75.75,42.2,'Кочкор','Kochkor'),
 'Kazarman':(74.03,41.4,'Казарман','Kazarman'),'Tash-Kumyr':(72.22,41.35,'Таш-Кумыр','Tash-Kumyr'),'Mailuu-Suu':(72.45,41.27,'Майлуу-Суу','Mailuu-Suu'),
 'Nookat':(72.5,40.27,'Ноокат','Nookat'),'At-Bashy':(75.8,41.17,'Ат-Баши','At-Bashy'),'Sary-Tash':(73.25,39.73,'Сары-Таш','Sary-Tash'),'Kyzyl-Suu':(78.0,42.34,'Кызыл-Суу','Kyzyl-Suu'),
 'Kant':(74.85,42.89,'Кант','Kant'),'Kemin':(75.7,42.78,'Кемин','Kemin'),'Isfana':(70.6,39.84,'Исфана','Isfana'),'Kadamjai':(71.72,39.9,'Кадамжай','Kadamjai')}
class KG:
    def __init__(s,x=30,y=100,w=1340,h=660,box=KG_BOX):
        s.P=Eq(*box,x,y,w,h); s.o=[]; s.box=box; s.cl=inbox(box); s.R=(x,y,w,h)
    def ctx(s,fill='#eceff2'):
        for f in feats('ne_10m_admin_0_countries',lambda p:p['ADMIN'] in ('Kazakhstan','Uzbekistan','Tajikistan','China','Afghanistan','Pakistan','Turkmenistan')):
            s.o.append(f'<path d="{path_of(f["geometry"],s.P,s.cl)}" fill="{fill}" stroke="#b6bfc8" stroke-width="1.2"/>')
        return s
    def oblasts(s,pal=PAL,stroke='#7a8a99',opacity=1.0,only=None):
        for f in feats('ne_10m_admin_1_states_provinces',lambda p:p['admin']=='Kyrgyzstan'):
            n=f['properties']['name']
            if only and n not in only: continue
            s.o.append(f'<path d="{path_of(f["geometry"],s.P)}" fill="{pal.get(n,"#eee")}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="1.8" stroke-linejoin="round"/>')
        return s
    def outline(s,stroke='#44586b',w=3,fill='none'):
        f=feats('ne_10m_admin_0_countries',lambda p:p['ADMIN']=='Kyrgyzstan')[0]
        s.o.append(f'<path d="{path_of(f["geometry"],s.P)}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" stroke-linejoin="round"/>'); return s
    def water(s):
        for f in feats('ne_10m_lakes',lambda p:p['name'] in ('Issyk-Kul','Toktogul Suu Saktagychy')):
            s.o.append(f'<path d="{path_of(f["geometry"],s.P)}" fill="#9cc4e4" stroke="#5b8db8" stroke-width="1.2"/>')
        for f in feats('ne_10m_rivers_lake_centerlines',lambda p:(p['name'] or '').strip() in ('Naryn','Syr  Darya','Syr Darya','Ile','Toxkan','Aksu')):
            s.o.append(f'<path d="{path_of(f["geometry"],s.P,s.cl)}" fill="none" stroke="#5b8db8" stroke-width="2.4"/>')
        return s
    def line(s,pts_,color='#5b8db8',w=2.4,dash=None):
        d='M'+'L'.join('%.1f %.1f'%s.P(*p) for p in pts_)
        s.o.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'); return s
    def rng(s,a,b,ru,en,color='#a0784f',w=9,off=(0,-14)):
        (x1,y1),(x2,y2)=s.P(*a),s.P(*b)
        s.o.append(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" stroke="{color}" stroke-width="{w}" stroke-opacity=".55" stroke-linecap="round"/>')
        mx,my=(x1+x2)/2+off[0],(y1+y2)/2+off[1]
        ang=math.degrees(math.atan2(y2-y1,x2-x1))
        s.o.append(f'<text x="{mx:.0f}" y="{my:.0f}" class="sm it" text-anchor="middle" transform="rotate({ang:.0f} {mx:.0f} {my:.0f})" style="fill:#5b3e22">{esc(ru)} / {esc(en)}</text>'); return s
    def dot(s,lon,lat,ru,en,r=5,fill='#c0392b',dx=8,dy=-6,anchor='start',cls='sm',two=False):
        x,y=s.P(lon,lat)
        s.o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="1.5"/>')
        if ru is not None:
            s.o.append(T(x+dx,y+dy,ru+(' / '+en if en and not two else ''),cls,anchor,'style="paint-order:stroke;stroke:#fff;stroke-width:3px"'))
            if two and en: s.o.append(T(x+dx,y+dy+16,en,cls,anchor,'style="paint-order:stroke;stroke:#fff;stroke-width:3px;fill:#526579"'))
        return s
    def city(s,key,r=5,fill='#243447',dx=8,dy=-6,anchor='start',two=False):
        lon,lat,ru,en=CITIES[key]; return s.dot(lon,lat,ru,en,r,fill,dx,dy,anchor,two=two)
    def blob(s,lon,lat,rx,ry,fill,ru=None,en=None,op=.45,ang=0,stroke=None):
        x,y=s.P(lon,lat)
        s.o.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx}" ry="{ry}" transform="rotate({ang} {x:.0f} {y:.0f})" fill="{fill}" fill-opacity="{op}" stroke="{stroke or fill}" stroke-width="1.5"/>')
        if ru:
            st='paint-order:stroke;stroke:#fff;stroke-width:3px;font-weight:700'
            s.o.append(T(x,y,ru,'sm','middle','style="%s"'%st)); s.o.append(T(x,y+16,en,'sm','middle','style="%s;fill:#526579"'%st))
        return s
    def text(s,lon,lat,ru,en,cls='sm',anchor='middle',fill=None):
        x,y=s.P(lon,lat)
        st='paint-order:stroke;stroke:#fff;stroke-width:3px'+(f';fill:{fill}' if fill else '')
        s.o.append(T(x,y,ru+' / '+en,cls,anchor,f'style="{st}"')); return s
    def label_obl(s,fs='lab'):
        pos={'Ysyk-Köl':(78.4,42.0),'Naryn':(75.6,41.0),'Osh':(73.4,39.95),'Chuy':(74.4,43.15),'Talas':(72.0,42.55),'Jalal-Abad':(72.4,41.55),'Batken':(70.3,39.7)}
        for k,(lo,la) in pos.items():
            x,y=s.P(lo,la); ru,en=OBL[k]
            s.o.append(T(x,y,ru,fs,'middle','style="fill:#44586b;fill-opacity:.8"')); s.o.append(T(x,y+18,en,'sm','middle','style="fill:#44586b;fill-opacity:.8"'))
        return s
    def legend(s,items,x=50,y=640,cols=1):
        n=len(items); w=max(len(a)+len(b) for a,b,_ in items)*7.4+70
        h=n*26+18
        out=f'<rect x="{x-12}" y="{y-24}" width="{w:.0f}" height="{h}" rx="10" fill="#fff" fill-opacity=".92" stroke="#c5ced6"/>'
        for i,(ru,en,c) in enumerate(items):
            yy=y+i*26
            out+=f'<rect x="{x}" y="{yy-12}" width="22" height="14" rx="3" fill="{c}" stroke="#647789"/>'+T(x+32,yy,ru+' / '+en,'sm')
        s.o.append(out); return s
    def svg(s):
        x,y,w,h=s.R
        return f'<clipPath id="mc"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#mc)">'+''.join(s.o)+'</g>'
