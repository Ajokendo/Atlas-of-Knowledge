# -*- coding: utf-8 -*-
"""Вставляет карты местоположения в главы (идемпотентно). Запуск после locdata.py"""
import json,glob
CH='/home/claude/atlas-of-knowledge/geography/chapters/'
items=json.load(open('/home/claude/geo/loc_items.json'))
done=0
for ch,head,fn,cru,cen in items:
    p=glob.glob(CH+ch+'-*.md')[0]
    lines=open(p,encoding='utf-8').read().split('\n')
    if any(fn in l for l in lines): continue
    idx=[i for i,l in enumerate(lines) if l.startswith(head)]
    assert idx,(ch,head)
    i=idx[0]
    alt=cru+' / '+cen
    ins=['',f'![{alt}](../assets/diagrams/{fn})','',f'*{cru} Схематичная карта. / {cen} A schematic map.*']
    lines[i+1:i+1]=ins
    open(p,'w',encoding='utf-8').write('\n'.join(lines)); done+=1
print('inserted',done)
