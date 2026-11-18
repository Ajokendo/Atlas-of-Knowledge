# -*- coding: utf-8 -*-
"""Вставляет карты местоположения в главы (идемпотентно). Запуск после locdata.py"""
import json,glob,sys
CH='/home/claude/atlas-of-knowledge/geography/chapters/'
items=json.load(open(sys.argv[1] if len(sys.argv)>1 else '/home/claude/geo/loc_items.json'))
done=0
for it in items:
    ch,head,fn,cru,cen=it[:5]; sru,sen=(it[5],it[6]) if len(it)>5 else ('Схематичная карта.','A schematic map.')
    p=glob.glob(CH+ch+'-*.md')[0]
    lines=open(p,encoding='utf-8').read().split('\n')
    if any(fn in l for l in lines): continue
    idx=[i for i,l in enumerate(lines) if l.startswith(head)]
    assert idx,(ch,head)
    i=idx[0]
    alt=cru+' / '+cen
    ins=['',f'![{alt}](../assets/diagrams/{fn})','',f'*{cru} {sru} / {cen} {sen}*']
    lines[i+1:i+1]=ins
    open(p,'w',encoding='utf-8').write('\n'.join(lines)); done+=1
print('inserted',done)
