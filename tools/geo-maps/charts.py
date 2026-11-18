# -*- coding: utf-8 -*-
"""Столбчатые диаграммы по таблице главы 24.2 (площадь, население на 01.01.2026, плотность). Данные — только из таблицы главы."""
import json
from kit import esc
OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams/'
D=[ # рус, англ, площадь тыс. км², население тыс., плотность, цвет
 ('Баткенская','Batken',17.0,605.3,35.6,'#9fd9cc'),('Джалал-Абадская','Jalal-Abad',33.7,1379.9,40.9,'#f1b9a3'),('Иссык-Кульская','Issyk-Kul',43.1,554.3,12.9,'#a5d3e8'),
 ('Нарынская','Naryn',45.2,316.2,7.0,'#d3c1e8'),('Ошская','Osh',29.0,1438.5,49.6,'#d9c3a0'),('Таласская','Talas',11.4,282.9,24.8,'#b7dba5'),('Чуйская','Chuy',20.2,983.7,48.7,'#f3d98b')]
STY=('text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:34px;font-weight:700}.sub{font-size:22px;fill:#526579}.pt{font-size:23px;font-weight:700}'
 '.ru{font-size:20px;font-weight:700}.en{font-size:15px;fill:#526579}.v{font-size:19px;font-weight:700}.sm{font-size:15px}')
def fmt(v,d): return (f'{v:,.{d}f}'.replace(',',' ')).replace('.',',')
panels=[('Площадь, тыс. км²','Area, thousand km²',2,1),('Население на 1 января 2026 г., тыс. чел.','Population, 1 January 2026, thousand',3,1),('Расчётная плотность, чел./км²','Calculated density, people per km²',4,1)]
W=900; x0=250; bw=520; rowh=50; y=100; body=''
for ru,en,idx,dec in panels:
    rows=sorted(D,key=lambda r:-r[idx]); mx=max(r[idx] for r in rows)
    body+=f'<text x="30" y="{y+24}" class="pt">{ru}</text><text x="30" y="{y+46}" class="en">{en}</text>'; y+=66
    for r in rows:
        w=bw*r[idx]/mx
        body+=f'<text x="{x0-12}" y="{y+19}" class="ru" text-anchor="end">{r[0]}</text><text x="{x0-12}" y="{y+37}" class="en" text-anchor="end">{r[1]}</text>'
        body+=f'<rect x="{x0}" y="{y+4}" width="{w:.0f}" height="34" rx="5" fill="{r[5]}" stroke="#3f566a" stroke-width="1.5"/><text x="{x0+w+10:.0f}" y="{y+28}" class="v">{fmt(r[idx],dec)}</text>'
        y+=rowh
    y+=26
H=y+60
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"><title id="t">Семь областей: площадь, население, плотность / Seven regions: area, population, density</title><desc id="d">Три столбчатые диаграммы по таблице главы</desc><style>{STY}</style>'
 f'<rect width="{W}" height="{H}" fill="#fbfcfe"/><text x="30" y="46" class="h">Семь областей в цифрах</text><text x="30" y="76" class="sub">The seven regions in numbers</text>{body}'
 f'<text x="30" y="{H-38}" class="sm">Источник: таблица главы 24.2 (НСК КР, население на 01.01.2026). Бишкек и Ош в данные областей не входят.</text>'
 f'<text x="30" y="{H-16}" class="sm" style="fill:#526579">Source: table in chapter 24.2 (NSC KR, 1 Jan 2026). Bishkek and Osh are not included in the regional figures.</text></svg>')
open(OUT+'24-N-regions-in-numbers-bilingual.svg','w',encoding='utf-8').write(svg)
json.dump([['24','### Население, площадь и расчётная','24-N-regions-in-numbers-bilingual.svg','Семь областей в цифрах: площадь, население, плотность.','Seven regions in numbers: area, population, density.','Диаграммы по таблице ниже.','Charts based on the table below.'],
 ['23','## 23.5. ','24-N-regions-in-numbers-bilingual.svg','Семь областей в цифрах: площадь, население, плотность.','Seven regions in numbers: area, population, density.','Диаграммы по таблице главы 24.','Charts based on the table in chapter 24.']],open('/home/claude/geo/chart_items.json','w'),ensure_ascii=False)
