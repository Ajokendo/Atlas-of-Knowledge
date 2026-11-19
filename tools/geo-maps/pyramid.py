# -*- coding: utf-8 -*-
"""Возрастно-половая пирамида (глава 23.6, схема 23-G). Данные: НСК КР, «Численность постоянного населения по полу и возрастным группам»,
таблица 1.3 статистического сборника 2019–2023 (оценка на начало 2024 г., с учётом переписи 2022 г.). Запуск: python3 pyramid.py"""
import re
from kit import esc
G=['0–4','5–9','10–14','15–19','20–24','25–29','30–34','35–39','40–44','45–49','50–54','55–59','60–64','65–69','70–74','75–79','80–84','85+']
M=[393592,416022,380153,68717+125455+116921,257222,267599,277107,258396,210697,181236,158881,141398,122023,82649,48371,19117,10066,5172+1985+96]
F=[371825,395409,358920,64768+117333+109307,264536,274116,280316,261989,217020,187204,169736,159086,147053,108483,68613,30495,17594,10794+4168+270]
TM,TF=3542875,3619035
assert abs(sum(M)-TM)<5 and abs(sum(F)-TF)<5,(sum(M),sum(F))
tot=TM+TF
OUT='/home/claude/atlas-of-knowledge/geography/assets/diagrams/23-G-age-sex-pyramid-bilingual.svg'
W,H=900,720; cx=450; sc=310/ (max(M+F)/tot*100)  # px per %
rows=''; y0=110; rh=28
for i,g in enumerate(G):
    y=y0+(len(G)-1-i)*rh
    pm=M[i]/tot*100; pf=F[i]/tot*100
    rows+=(f'<rect x="{cx-30-pm*sc:.1f}" y="{y}" width="{pm*sc:.1f}" height="{rh-5}" fill="#5b8fc7" stroke="#3f566a"/>'
           f'<rect x="{cx+30:.1f}" y="{y}" width="{pf*sc:.1f}" height="{rh-5}" fill="#d98aa3" stroke="#3f566a"/>'
           f'<text x="{cx}" y="{y+rh-9}" class="a" text-anchor="middle">{g}</text>'
           f'<text x="{cx-34-pm*sc:.1f}" y="{y+rh-9}" class="v" text-anchor="end">{pm:.1f}</text>'
           f'<text x="{cx+34+pf*sc:.1f}" y="{y+rh-9}" class="v">{pf:.1f}</text>')
child=sum(M[:3])+sum(F[:3]); old=sum(M[13:])+sum(F[13:])
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"><title id="t">Возрастно-половая пирамида Кыргызстана / Age-sex pyramid of Kyrgyzstan</title>'
 f'<desc id="d">Доли мужчин и женщин по пятилетним возрастным группам в общей численности постоянного населения, начало 2024 года. / Shares of men and women by five-year age group in the total resident population, start of 2024.</desc>'
 '<style>text{font-family:Arial,sans-serif;fill:#243447}.h{font-size:30px;font-weight:700}.sub{font-size:19px;fill:#526579}.a{font-size:14px;font-weight:700}.v{font-size:13px}.sm{font-size:14px}.lg{font-size:18px;font-weight:700}</style>'
 f'<rect width="{W}" height="{H}" fill="#fbfcfe"/><text x="30" y="42" class="h">Возрастно-половая пирамида Кыргызстана</text><text x="30" y="70" class="sub">Age-sex pyramid of Kyrgyzstan · start of 2024, % of total population</text>'
 f'<text x="{cx-120}" y="100" class="lg" text-anchor="middle">Мужчины / Men</text><text x="{cx+120}" y="100" class="lg" text-anchor="middle">Женщины / Women</text>{rows}'
 f'<text x="30" y="{H-62}" class="sm">Дети 0–14 лет: {child/tot*100:.1f}%; 65 лет и старше: {old/tot*100:.1f}% (по этим же данным). Всего {tot:,}'.replace(',',' ')+' чел.</text>'
 f'<text x="30" y="{H-42}" class="sm">Источник: НСК КР, табл. 1.3 «Численность постоянного населения» (оценка на начало 2024 г., с учётом переписи 2022 г.).</text>'
 f'<text x="30" y="{H-22}" class="sm" style="fill:#526579">Source: NSC KR, table 1.3 “Resident population” (start-of-2024 estimate, based on the 2022 census). Groups 15–19 and 85+ combined by the author.</text></svg>')
open(OUT,'w',encoding='utf-8').write(svg)
print(round(child/tot*100,1),round(old/tot*100,1),tot)
