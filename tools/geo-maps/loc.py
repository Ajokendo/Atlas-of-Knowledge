# -*- coding: utf-8 -*-
"""Карты местоположения объектов Кыргызстана (озёра, реки, горы...) на контурах Natural Earth.
Запуск: python3 loc.py  -> geography/assets/diagrams/NN-L-*.svg и /home/claude/geo/loc_index.json"""
import json, os, math
from kit import load, esc, Eq, path_of, feats, KG_BOX
OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams'
W,H=1000,600
P=Eq(69.0,81.0,39.0,43.8,30,95,W-60,H-150)
STY=('text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:30px;font-weight:700}.sub{font-size:19px}'
 '.lb{font-size:19px;font-weight:700;paint-order:stroke;stroke:#fff;stroke-width:5px;stroke-linejoin:round}'
 '.lc{font-size:14px;paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round;fill:#526579}'
 '.sm{font-size:14px}')
def country(name): return [f for f in load('ne_10m_admin_0_countries')['features'] if f['properties']['NAME']==name][0]['geometry']
def river_ne(name,box=None):
    out=[]
    for f in load('ne_10m_rivers_lake_centerlines')['features']:
        if (f['properties'].get('name') or '').strip()==name: out+=f['geometry']['coordinates']
    return out
def line(pts,P=P): return 'M'+'L'.join('%.1f %.1f'%P(*p) for p in pts)
CITY={'Бишкек':('Bishkek',74.59,42.87),'Ош':('Osh',72.80,40.53),'Нарын':('Naryn',76.0,41.43),'Каракол':('Karakol',78.39,42.49),'Талас':('Talas',72.24,42.52),'Джалал-Абад':('Jalal-Abad',72.98,40.93),'Баткен':('Batken',70.82,40.06)}
def layers(spec,Pj,labels,zoom=False):
    s=''
    for n in ('China','Kazakhstan','Uzbekistan','Tajikistan'):
        s+=f'<path d="{path_of(country(n),Pj)}" fill="#eef1f4" stroke="#c3ccd5" stroke-width="1"/>'
    s+=f'<path d="{path_of(country("Kyrgyzstan"),Pj)}" fill="#e9f1e2" stroke="#5d7a4f" stroke-width="{3 if zoom else 2.2}"/>'
    for f in load('ne_10m_lakes')['features']:
        if (f['properties'].get('name') or '')=='Issyk-Kul':
            s+=f'<path d="{path_of(f["geometry"],Pj)}" fill="#bcd8ec" stroke="#6a9cc0" stroke-width="1.5"/>'
    for ln in river_ne('Naryn'): s+=f'<path d="{line(ln,Pj)}" fill="none" stroke="#8fb5d3" stroke-width="1.6"/>'
    for k,(e,lo,la) in CITY.items():
        x,y=Pj(lo,la)
        if labels and not spec.get('nocity'): s+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3.5" fill="#7a8794"/><text x="{x+6:.0f}" y="{y+4:.0f}" class="lc">{k}</text>'
    for o in spec['objs']:
        t=o['t']; col=o.get('col','#c0392b')
        if t=='river':
            d=line(o['pts'],Pj); s+=f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{9 if zoom else 7}" stroke-linecap="round" stroke-linejoin="round"/><path d="{d}" fill="none" stroke="{o.get("rc","#1f6fb2")}" stroke-width="{5 if zoom else 3.5}" stroke-linecap="round" stroke-linejoin="round"/>'
            if o.get('arrow') and zoom:
                a=o['pts'][-2];b=o['pts'][-1];x0,y0=Pj(*a);x1,y1=Pj(*b);ang=math.atan2(y1-y0,x1-x0)
                s+=f'<path d="M{x1:.1f} {y1:.1f}l{-14*math.cos(ang-.4):.1f} {-14*math.sin(ang-.4):.1f}l{14*(math.cos(ang-.4)-math.cos(ang+.4)):.1f} {14*(math.sin(ang-.4)-math.sin(ang+.4)):.1f}z" fill="#1f6fb2" stroke="#fff" stroke-width="1.5"/>'
        elif t=='lakepoly':
            for f in load('ne_10m_lakes')['features']:
                if (f['properties'].get('name') or '')==o['name']:
                    s+=f'<path d="{path_of(f["geometry"],Pj)}" fill="#2e86c1" stroke="{col}" stroke-width="3.5"/>'
        elif t=='lake':
            x,y=Pj(o['lon'],o['lat']); rx=max(o.get('rx',0.1)*Pj.c*Pj.k,4); ry=max(o.get('ry',0.07)*Pj.k,3)
            s+=f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx+5:.1f}" ry="{ry+5:.1f}" fill="none" stroke="{col}" stroke-width="3"/><ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="#2e86c1" stroke="#fff" stroke-width="1.2"/>'
        elif t=='peak':
            x,y=Pj(o['lon'],o['lat']); r=1 if zoom else .7; s+=f'<path d="M{x:.1f} {y-12*r:.1f}L{x+11*r:.1f} {y+8*r:.1f}L{x-11*r:.1f} {y+8*r:.1f}Z" fill="{col}" stroke="#fff" stroke-width="2"/>'
        elif t=='dot':
            x,y=Pj(o['lon'],o['lat']); s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8 if zoom else 5}" fill="{col}" stroke="#fff" stroke-width="2.5"/>'
        elif t=='dam':
            x,y=Pj(o['lon'],o['lat']); h=8 if zoom else 5; s+=f'<rect x="{x-h:.1f}" y="{y-h:.1f}" width="{2*h}" height="{2*h}" fill="{col}" stroke="#fff" stroke-width="2.5"/>'
        elif t=='area':
            x,y=Pj(o['lon'],o['lat']); rr=o['r']*Pj.k; s+=f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rr*1.35:.1f}" ry="{rr:.1f}" fill="{col}" fill-opacity="0.25" stroke="{col}" stroke-width="2.5" stroke-dasharray="7 5"/>'
        if labels and 'label' in o:
            lx,ly=Pj(*o['lpos']) if 'lpos' in o else Pj(o['lon'],o['lat'])
            ru_,en_=o['label']; anc=o.get('anchor','start')
            s+=f'<text x="{lx+o.get("dx",14):.0f}" y="{ly+o.get("dy",-6):.0f}" class="lb" text-anchor="{anc}">{esc(ru_)}</text><text x="{lx+o.get("dx",14):.0f}" y="{ly+o.get("dy",-6)+21:.0f}" class="lc" text-anchor="{anc}" style="font-size:16px">{esc(en_)}</text>'
    return s
def bbox(spec):
    xs=[];ys=[]
    for o in spec['objs']:
        if o.get('ctx'): continue
        if 'pts' in o: xs+=[p[0] for p in o['pts']]; ys+=[p[1] for p in o['pts']]
        elif o['t']=='lakepoly':
            for f in load('ne_10m_lakes')['features']:
                if (f['properties'].get('name') or '')==o['name']:
                    from kit import pts as _p
                    for p in _p(f['geometry']['coordinates']): xs.append(p[0]); ys.append(p[1])
        else:
            r=o.get('r',0.1); xs+=[o['lon']-r,o['lon']+r]; ys+=[o['lat']-r*.7,o['lat']+r*.7]
    return min(xs),max(xs),min(ys),max(ys)
def render(spec):
    ru,en=spec['ru'],spec['en']
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"><title id="t">{esc(ru)} / {esc(en)}</title><desc id="d">{esc(spec["descr"])} / {esc(spec["descen"])}</desc><style>{STY}</style><rect width="{W}" height="{H}" fill="#fbfcfe"/>'
    s+=f'<text x="30" y="40" class="h">{esc(ru)}</text><text x="30" y="68" class="sub" style="fill:#526579">{esc(en)} · {esc(spec["kind_en"])}</text>'
    # left: country
    P1=Eq(69.0,81.0,39.0,43.8,30,150,470,300)
    s+='<clipPath id="c1"><rect x="30" y="95" width="470" height="410"/></clipPath><g clip-path="url(#c1)"><rect x="30" y="95" width="470" height="410" fill="#f4f6f8"/>'+layers(spec,P1,False)
    x0,x1,y0,y1=zoomwin(spec)
    a=P1(x0,y1);b=P1(x1,y0)
    s+=f'<rect x="{a[0]:.1f}" y="{a[1]:.1f}" width="{b[0]-a[0]:.1f}" height="{b[1]-a[1]:.1f}" fill="none" stroke="#243447" stroke-width="2.5" stroke-dasharray="6 4"/></g><rect x="30" y="95" width="470" height="410" fill="none" stroke="#c3ccd5"/>'
    s+=f'<text x="38" y="118" class="sm">{esc("Кыргызстан / Kyrgyzstan")}</text>'
    # right: zoom
    P2=Eq(x0,x1,y0,y1,520,95,450,410)
    s+='<clipPath id="c2"><rect x="520" y="95" width="450" height="410"/></clipPath><g clip-path="url(#c2)"><rect x="520" y="95" width="450" height="410" fill="#f4f6f8"/>'+layers(spec,P2,True,True)+'</g><rect x="520" y="95" width="450" height="410" fill="none" stroke="#243447" stroke-width="1.5"/>'
    s+=f'<text x="{W-40}" y="40" class="sub" text-anchor="end">N ↑</text>'
    kmpx=111.32*math.cos(math.radians((y0+y1)/2))/P2.k
    for nice in (200,100,50,20,10):
        if nice/kmpx<150: break
    Ls=nice/kmpx; s+=f'<path d="M{W-50-Ls:.0f} {H-95} h{Ls:.0f}" stroke="#243447" stroke-width="3"/><text x="{W-50-Ls/2:.0f}" y="{H-101}" class="sm" text-anchor="middle">{nice} km</text>'
    s+=f'<rect x="30" y="{H-62}" width="{W-60}" height="1" fill="#c3ccd5"/><text x="30" y="{H-40}" class="sm">{esc(spec["note_ru"])}</text><text x="30" y="{H-20}" class="sm" style="fill:#526579">{esc(spec["note_en"])}</text>'
    return s+'</svg>'
def zoomwin(spec):
    if spec.get('zoom'): return spec['zoom']
    x0,x1,y0,y1=bbox(spec); pad=spec.get('pad',0.5)
    cx,cy=(x0+x1)/2,(y0+y1)/2; hw=max((x1-x0)/2+pad,1.0); hh=max((y1-y0)/2+pad*.7,0.7)
    # aspect of panel 450x410 in equirect: width deg*cos(lat) / height deg
    c=math.cos(math.radians(cy)); asp=450/410
    if hw*c/hh>asp: hh=hw*c/asp
    else: hw=hh*asp/c
    return cx-hw,cx+hw,cy-hh,cy+hh
NOTE=('Карта схематична: контуры — Natural Earth (общественное достояние). ','Schematic map: outlines — Natural Earth (public domain). ')
def mk(id_,slug,ru,en,kind_ru,kind_en,objs,extra_ru='',extra_en='',descr=None,**kw):
    spec=dict(ru=ru,en=en,kind_ru=kind_ru,kind_en=kind_en,objs=objs,descr=descr or f'{kind_ru} {ru} на карте Кыргызстана.',descen=f'{kind_en} {en} on the map of Kyrgyzstan.',
      note_ru=NOTE[0]+extra_ru,note_en=NOTE[1]+extra_en,**kw)
    fn=f'{id_}-L-{slug}-bilingual.svg'
    open(os.path.join(OUT,fn),'w',encoding='utf-8').write(render(spec))
    return fn
