# -*- coding: utf-8 -*-
import json, re, os
from loc import mk, river_ne
CH='/home/claude/atlas-of-knowledge/geography/chapters/'
SCH=('Русло проведено по опорным точкам и показано схематично.','The course is drawn through reference points and is schematic.')
RED='#c0392b'
def naryn():
    ls=river_ne('Naryn'); ls=sorted(ls,key=lambda l:-l[0][0]); out=[]
    for l in ls: out+=l
    return out
ITEMS=[]  # (chapter prefix, heading prefix, file, cap_ru, cap_en)
def add(ch,head,fn,cru,cen): ITEMS.append((ch,head,fn,cru,cen))
# ---------- peaks (18.5)
pk=lambda lo,la:dict(t='peak',lon=lo,lat=la)
add('18','### 18.5.1. ',mk('18','jengish-chokusu','Пик Жеңиш (Победы)','Jengish Chokusu (Victory Peak)','Гора','Mountain',
  [dict(t='peak',lon=80.13,lat=42.04,label=('Пик Жеңиш, 7 439 м','Jengish Chokusu, 7,439 m'),dx=-16,dy=34,anchor='end'),dict(t='peak',lon=80.17,lat=42.21,col='#7a8794')],
  'Хребет Кокшаал-Тоо на границе с Китаем.','The Kokshaal-Too range on the Chinese border.'),
  'Пик Жеңиш на карте Кыргызстана.','Jengish Chokusu on the map of Kyrgyzstan.')
add('18','### 18.5.2. ',mk('18','khan-tengri','Хан-Тенгри','Khan Tengri','Гора','Mountain',
  [dict(t='peak',lon=80.17,lat=42.21,label=('Хан-Тенгри, 7 010 м','Khan Tengri, 7,010 m'),dx=-16,dy=-18,anchor='end'),dict(t='peak',lon=80.13,lat=42.04,col='#7a8794')],
  'Узел сходства границ Кыргызстана, Казахстана и Китая.','Near the point where the borders of Kyrgyzstan, Kazakhstan and China meet.'),
  'Хан-Тенгри на карте Кыргызстана.','Khan Tengri on the map of Kyrgyzstan.')
add('18','### 18.5.3. ',mk('18','lenin-peak','Пик Ленина (Ленин атындагы чоку)','Lenin Peak','Гора','Mountain',
  [dict(t='peak',lon=72.88,lat=39.34,label=('Пик Ленина, 7 134 м','Lenin Peak, 7,134 m'),dx=16,dy=-12)],
  'Заалайский хребет на границе с Таджикистаном.','The Trans-Alay range on the Tajik border.'),
  'Пик Ленина на карте Кыргызстана.','Lenin Peak on the map of Kyrgyzstan.')
# ---------- rivers (20.4)
nar=naryn()
add('20','### 20.4.3. ',mk('20','naryn','Река Нарын','The Naryn River','Река','River',
  [dict(t='river',pts=nar,arrow=True,label=('Нарын','Naryn'),lpos=(75.2,41.78),dy=-14)],
  'Контур реки — Natural Earth.','River outline — Natural Earth.'),
  'Река Нарын на карте Кыргызстана.','The Naryn River on the map of Kyrgyzstan.')
add('20','### 20.4.4. ',mk('20','kara-darya','Карадарья','The Kara Darya','Река','River',
  [dict(t='river',pts=[(73.95,40.45),(73.45,40.72),(72.85,40.82),(72.3,40.86),(71.9,40.92),(71.55,40.97)],arrow=True,label=('Карадарья','Kara Darya'),lpos=(72.85,40.82),dx=-30,dy=-18,anchor='middle')],
  SCH[0],SCH[1]),'Карадарья на карте Кыргызстана.','The Kara Darya on the map of Kyrgyzstan.')
add('20','### 20.4.5. ',mk('20','chu','Река Чу','The Chu River','Река','River',
  [dict(t='river',pts=[(75.72,42.27),(75.95,42.5),(75.5,42.72),(75.2,42.88),(74.6,43.02),(74.0,43.0),(73.3,43.08),(72.9,43.14)],arrow=True,label=('Чу','Chu'),lpos=(74.2,43.22),dy=-6,dx=0,anchor='middle')],
  SCH[0],SCH[1]),'Река Чу на карте Кыргызстана.','The Chu River on the map of Kyrgyzstan.')
add('20','### 20.4.6. ',mk('20','talas','Река Талас','The Talas River','Река','River',
  [dict(t='river',pts=[(72.75,42.48),(72.24,42.57),(71.7,42.68),(71.2,42.85),(70.7,43.0)],arrow=True,label=('Талас','Talas'),lpos=(71.9,42.66),dy=-14,dx=0,anchor='middle')],
  SCH[0],SCH[1]),'Река Талас на карте Кыргызстана.','The Talas River on the map of Kyrgyzstan.')
add('20','### 20.4.7. ',mk('20','sary-jaz','Сары-Джаз','The Sary-Jaz River','Река','River',
  [dict(t='river',pts=[(78.7,42.0),(79.3,41.97),(79.9,41.9),(80.4,41.8)],arrow=True,label=('Сары-Джаз','Sary-Jaz'),lpos=(79.3,41.97),dy=-14,dx=0,anchor='middle'),dict(t='area',lon=80.0,lat=42.15,r=0.12,col='#8e44ad')],
  SCH[0]+' Фиолетовый овал — район ледника Иныльчек.',SCH[1]+' The purple oval is the Inylchek glacier area.'),
  'Сары-Джаз на карте Кыргызстана.','The Sary-Jaz River on the map of Kyrgyzstan.')
add('20','### 20.4.8. ',mk('20','chatkal','Чаткал и реки юго-запада','The Chatkal and rivers of the south-west','Речной бассейн','River basin',
  [dict(t='area',lon=71.8,lat=41.9,r=0.35,col='#1f6fb2',label=('Бассейн Чаткала','Chatkal basin'),dx=60,dy=-30),dict(t='area',lon=72.5,lat=39.7,r=0.25,col='#1f6fb2',label=('Алайская долина (Кызыл-Суу)','Alay Valley (Kyzyl-Suu)'),dx=70,dy=24)],
  'Овалы показывают районы бассейнов, а не русла.','Ovals show basin areas, not channels.'),
  'Чаткал и реки юго-запада.','The Chatkal and south-western rivers.')
# ---------- lakes (20.6)
add('20','### 20.6.1. ',mk('20','issyk-kul','Иссык-Куль','Lake Issyk-Kul','Озеро','Lake',
  [dict(t='lakepoly',name='Issyk-Kul',label=('Иссык-Куль','Issyk-Kul'),lpos=(77.2,42.45),dx=-55,dy=48,anchor='middle')],
  'Контур озера — Natural Earth.','Lake outline — Natural Earth.'),
  'Иссык-Куль на карте Кыргызстана.','Lake Issyk-Kul on the map of Kyrgyzstan.')
add('20','### 20.6.2. ',mk('20','son-kul','Сон-Куль','Lake Song-Kul','Озеро','Lake',
  [dict(t='lake',lon=75.12,lat=41.83,rx=0.17,ry=0.08,label=('Сон-Куль','Song-Kul'),dx=20,dy=-16)],
  'Размер и положение озера показаны приблизительно.','The size and position of the lake are approximate.'),
  'Сон-Куль на карте Кыргызстана.','Lake Song-Kul on the map of Kyrgyzstan.')
add('20','### 20.6.3. ',mk('20','chatyr-kul','Чатыр-Куль','Lake Chatyr-Kul','Озеро','Lake',
  [dict(t='lake',lon=75.3,lat=40.6,rx=0.13,ry=0.05,label=('Чатыр-Куль','Chatyr-Kul'),dx=22,dy=-14)],
  'Размер и положение озера показаны приблизительно.','The size and position of the lake are approximate.'),
  'Чатыр-Куль на карте Кыргызстана.','Lake Chatyr-Kul on the map of Kyrgyzstan.')
add('20','### 20.6.4. ',mk('20','sary-chelek','Сары-Челек','Lake Sary-Chelek','Озеро','Lake',
  [dict(t='lake',lon=71.95,lat=41.83,rx=0.04,ry=0.03,label=('Сары-Челек','Sary-Chelek'),dx=20,dy=-14)],
  'Размер и положение озера показаны приблизительно.','The size and position of the lake are approximate.'),
  'Сары-Челек на карте Кыргызстана.','Lake Sary-Chelek on the map of Kyrgyzstan.')
add('20','### 20.6.5. ',mk('20','merzbacher','Озеро Мерцбахера','Merzbacher Lake','Ледниковое озеро','Glacial lake',
  [dict(t='lake',lon=79.9,lat=42.19,rx=0.03,ry=0.02,label=('Озеро Мерцбахера','Merzbacher Lake'),dx=-22,dy=-24,anchor='end')],
  'Ледник Иныльчек; положение озера показано приблизительно.','Inylchek glacier; the lake position is approximate.'),
  'Озеро Мерцбахера на карте Кыргызстана.','Merzbacher Lake on the map of Kyrgyzstan.')
# ---------- reservoir (20.8.1)
res=[l for l in river_ne('Naryn') if abs(l[0][0]-73.3)<0.01 and abs(l[-1][0]-72.65)<0.01]
add('20','### 20.8.1. ',mk('20','toktogul','Токтогульское водохранилище','Toktogul Reservoir','Водохранилище','Reservoir',
  [dict(t='river',pts=res[0] if res else [(73.3,41.78),(72.65,41.67)],col='#2e86c1'),dict(t='dam',lon=72.65,lat=41.67,label=('Токтогульская ГЭС','Toktogul HPP'),dx=-16,dy=34,anchor='end')],
  'Водохранилище показано по контуру Natural Earth.','The reservoir follows the Natural Earth outline.'),
  'Токтогульское водохранилище на карте Кыргызстана.','Toktogul Reservoir on the map of Kyrgyzstan.')
# ================= batch 2: ch21, 22, 25
CITYNOTE=('Положение города показано по координатам центра.','The city is placed at its centre coordinates.')
def city(id_,slug,ru,en,lo,la,extra=None,**kw):
    objs=[dict(t='dot',lon=lo,lat=la,label=(ru,en),dx=14,dy=-10)]
    if extra: objs+=extra
    return mk(id_,slug,ru,en,'Город','City',objs,CITYNOTE[0],CITYNOTE[1],**kw)
cap=lambda r,e:(r+' на карте Кыргызстана.',e+' on the map of Kyrgyzstan.')
add('22','### Сары-Челекский государственный биосферный',mk('22','sary-chelek-reserve','Сары-Челекский заповедник','Sary-Chelek Reserve','Заповедник','Nature reserve',
  [dict(t='area',lon=71.95,lat=41.83,r=0.18,col='#27ae60',label=('Сары-Челекский заповедник','Sary-Chelek Reserve'),dx=60,dy=-30),dict(t='lake',lon=71.95,lat=41.83,rx=0.04,ry=0.03,col='#27ae60')],
  'Овал показывает район заповедника, а не его границы.','The oval shows the reserve area, not its boundary.'),*cap('Сары-Челекский заповедник','Sary-Chelek Reserve'))
add('22','### Ала-Арча',mk('22','ala-archa','Ала-Арча','Ala-Archa','Национальный парк','National park',
  [dict(t='area',lon=74.48,lat=42.55,r=0.1,col='#27ae60',label=('Ала-Арча','Ala-Archa'),dx=40,dy=-30)],
  'Овал показывает район парка, а не его границы.','The oval shows the park area, not its boundary.'),*cap('Национальный парк «Ала-Арча»','Ala-Archa National Park'))
add('22','### Каракол',mk('22','karakol-park','Парк «Каракол»','Karakol Nature Park','Природный парк','Nature park',
  [dict(t='area',lon=78.55,lat=42.35,r=0.12,col='#27ae60',label=('Каракол (парк)','Karakol (park)'),dx=44,dy=30)],
  'Овал показывает район парка, а не его границы.','The oval shows the park area, not its boundary.'),*cap('Природный парк «Каракол»','Karakol Nature Park'))
add('22','### Чон-Кемин',mk('22','chon-kemin','Чон-Кемин','Chon-Kemin','Национальный парк','National park',
  [dict(t='area',lon=76.3,lat=42.75,r=0.22,col='#27ae60',label=('Чон-Кемин','Chon-Kemin'),dx=60,dy=-34)],
  'Овал показывает район парка, а не его границы.','The oval shows the park area, not its boundary.'),*cap('Парк «Чон-Кемин»','Chon-Kemin Park'))
add('22','### Хан-Тенири',mk('22','khan-tengri-park','Парк «Хан-Тенири»','Khan Tengri Nature Park','Природный парк','Nature park',
  [dict(t='area',lon=79.9,lat=42.2,r=0.2,col='#27ae60',label=('Хан-Тенири (парк)','Khan Tengri (park)'),dx=-60,dy=-40,anchor='end')],
  'Овал показывает район парка, а не его границы.','The oval shows the park area, not its boundary.'),*cap('Природный парк «Хан-Тенири»','Khan Tengri Nature Park'))
add('22','### Иссык-Куль',mk('22','issyk-kul-biosphere','Иссык-Кульская биосферная территория','Issyk-Kul Biosphere Territory','Биосферная территория','Biosphere territory',
  [dict(t='lakepoly',name='Issyk-Kul',col='#27ae60',label=('Иссык-Куль','Issyk-Kul'),lpos=(77.2,42.45),dx=-55,dy=48,anchor='middle')],
  'Показан контур озера, а не границы биосферной территории.','The lake outline is shown, not the boundaries of the biosphere territory.'),*cap('Иссык-Кульская биосферная территория','Issyk-Kul Biosphere Territory'))
add('25','### Бишкек — ',city('25','bishkek','Бишкек','Bishkek',74.59,42.87),*cap('Бишкек','Bishkek'))
add('25','### Ош — ',city('25','osh','Ош','Osh',72.80,40.53),*cap('Ош','Osh'))
add('25','### Каракол — ',city('25','karakol','Каракол','Karakol',78.39,42.49),*cap('Каракол','Karakol'))
add('25','### Джалал-Абадская городская',city('25','jalal-abad','Джалал-Абад','Jalal-Abad',72.98,40.93),*cap('Джалал-Абад','Jalal-Abad'))
add('25','### Нарын — ',city('25','naryn-city','Нарын','Naryn',76.0,41.43),*cap('Нарын','Naryn'))
add('25','### Талас — ',city('25','talas-city','Талас','Talas',72.24,42.52),*cap('Талас','Talas'))
add('25','### Баткен, Кызыл',mk('25','batken','Баткен, Кызыл-Кия, Кадамжай','Batken, Kyzyl-Kiya, Kadamjay','Города','Towns',
  [dict(t='dot',lon=70.82,lat=40.06,label=('Баткен','Batken'),dx=-14,dy=26,anchor='end'),dict(t='dot',lon=72.13,lat=40.26,label=('Кызыл-Кия','Kyzyl-Kiya'),dx=12,dy=26),dict(t='dot',lon=71.77,lat=40.13,label=('Кадамжай','Kadamjay'),dx=-12,dy=-14,anchor='end')],
  CITYNOTE[0],CITYNOTE[1],zoom=(69.8,73.0,39.3,41.2)),*cap('Города Баткенской области','Towns of the Batken region'))
add('25','### Гидроэнергетика',mk('25','toktogul-hpp','Токтогульская ГЭС и водохранилище','Toktogul HPP and reservoir','Гидроузел','Hydropower scheme',
  [dict(t='river',pts=res[0] if res else [(73.3,41.78),(72.65,41.67)],rc='#2e86c1'),dict(t='dam',lon=72.65,lat=41.67,label=('Токтогульская ГЭС','Toktogul HPP'),dx=-16,dy=34,anchor='end')],
  'Водохранилище показано по контуру Natural Earth.','The reservoir follows the Natural Earth outline.'),*cap('Токтогульская ГЭС','Toktogul HPP'))
add('25','### Металлические',mk('25','kumtor','Месторождение Кумтор','Kumtor gold deposit','Месторождение','Mineral deposit',
  [dict(t='dot',lon=78.2,lat=41.87,label=('Кумтор','Kumtor'),dx=-14,dy=26,anchor='end')],
  'Положение показано приблизительно.','The position is approximate.'),*cap('Месторождение Кумтор','The Kumtor deposit'))
add('25','### Авиация',mk('25','manas-airport','Аэропорт «Манас»','Manas International Airport','Аэропорт','Airport',
  [dict(t='dot',lon=74.48,lat=43.06,label=('Аэропорт «Манас»','Manas Airport'),dx=14,dy=-14)],
  'Положение показано приблизительно.','The position is approximate.'),*cap('Аэропорт «Манас»','Manas Airport'))
# ch21: reuse lake maps in biology
for ch,head,fn,r,e in [('21','### Иссык-Куль','20-L-issyk-kul-bilingual.svg','Иссык-Куль','Lake Issyk-Kul'),('21','### Сон-Куль и Чатыр-Куль','20-L-son-kul-bilingual.svg','Сон-Куль','Lake Song-Kul'),('21','### Сары-Челек и горные','20-L-sary-chelek-bilingual.svg','Сары-Челек','Lake Sary-Chelek')]:
    add(ch,head,fn,*cap(r,e))
if __name__=='__main__':
    json.dump(ITEMS,open('/home/claude/geo/loc_items.json','w'),ensure_ascii=False,indent=1)
    for it in ITEMS: print(it[2])
