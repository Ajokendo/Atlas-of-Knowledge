# -*- coding: utf-8 -*-
"""Карты местоположения для глав 17, 19, 23, 26. Запуск: python3 locdata2.py && python3 insert.py /home/claude/geo/loc_items2.json"""
import json
from locdata import mk, add as _a, ITEMS as _I, cap
import locdata
locdata.ITEMS.clear()
AP=('Овалы — районы, а не границы; положение приблизительное.','Ovals are areas, not boundaries; positions are approximate.')
def A(lo,la,r,ru,en,dx=0,dy=-10,col='#c0392b',anchor='middle'):
    return dict(t='area',lon=lo,lat=la,r=r,col=col,label=(ru,en),dx=dx,dy=dy,anchor=anchor)
def D(lo,la,ru,en,dx=12,dy=-10,anchor='start'):
    return dict(t='dot',lon=lo,lat=la,label=(ru,en),dx=dx,dy=dy,anchor=anchor)
add=locdata.add
# --- 17.4 Тянь-Шань и Памиро-Алай
add('17','## 17.4. ',mk('17','mountain-systems','Тянь-Шань и Памиро-Алай','Tien Shan and Pamir–Alay','Горные системы','Mountain systems',
  [A(76.4,41.8,1.25,'Тянь-Шань','Tien Shan',dy=-4,col='#7d5ba6'),A(72.4,39.6,0.75,'Памиро-Алай','Pamir–Alay',dy=40,col='#c0392b')],
  AP[0],AP[1],zoom=(69.0,81.0,38.6,43.9),nocity=True),'Две крупные горные системы Кыргызстана.','The two major mountain systems of Kyrgyzstan.')
# --- 17.5 впадины
add('17','## 17.5. ',mk('17','basins','Межгорные впадины и долины','Intermontane basins and valleys','Впадины','Basins',
  [A(74.6,42.78,0.3,'Чуйская','Chuy',dy=-30,col='#27ae60'),A(72.2,42.5,0.22,'Таласская','Talas',dy=-26,col='#27ae60'),A(77.9,42.45,0.5,'Иссык-Кульская','Issyk-Kul',dy=-40,dx=30,col='#27ae60'),A(72.6,40.7,0.45,'Ферганская (кирг. часть)','Fergana (Kyrgyz part)',dy=-36,dx=-20,col='#27ae60'),A(73.5,39.6,0.35,'Алайская','Alay',dy=34,col='#27ae60'),A(76.0,41.3,0.3,'Нарынская','Naryn',dy=34,dx=0,col='#27ae60')],
  AP[0],AP[1],zoom=(69.0,81.0,38.6,43.9),nocity=True),'Главные межгорные впадины и долины.','The main intermontane basins and valleys.')
# --- 19.5 регионы климата
add('19','## 19.5. ',mk('19','climate-regions','Климатические районы Кыргызстана','Climatic regions of Kyrgyzstan','Климатические районы','Climate regions',
  [A(74.6,42.78,0.3,'Чуйская долина','Chuy Valley',dy=-30,col='#d68910'),A(72.2,42.5,0.22,'Талас','Talas',dy=-16,dx=-26,anchor='end',col='#d68910'),A(77.6,42.45,0.5,'Иссык-Куль','Issyk-Kul',dy=38,col='#d68910'),A(78.7,41.4,0.45,'Внутренний Тянь-Шань','Inner Tien Shan',dy=84,dx=70,anchor='end',col='#d68910'),A(75.9,41.1,0.3,'Нарын','Naryn',dy=34,dx=-6,col='#d68910'),A(72.6,40.7,0.4,'Фергана','Fergana',dy=-34,dx=-20,col='#d68910'),A(73.4,39.6,0.35,'Алай, Памиро-Алай','Alay, Pamir–Alay',dy=34,col='#d68910')],
  AP[0],AP[1],zoom=(69.0,81.0,38.6,43.9),nocity=True),'Районы, описанные в разделе 19.5.','The regions described in section 19.5.')
# --- 23.3 концентрация населения
add('23','## 23.3. ',mk('23','population-concentration','Районы концентрации населения','Areas of population concentration','Население','Population',
  [A(74.6,42.8,0.35,'Чуйская долина (Бишкек)','Chuy Valley (Bishkek)',dy=-34,col='#c0392b'),A(72.7,40.75,0.5,'Ферганская долина (Ош, Джалал-Абад)','Fergana Valley (Osh, Jalal-Abad)',dy=-40,dx=-20,anchor='end',col='#c0392b'),A(77.4,42.55,0.5,'Иссык-Кульская котловина','Issyk-Kul Basin',dy=38,col='#c0392b')],
  AP[0],AP[1],zoom=(69.0,81.0,38.6,43.9),nocity=True),'Основные районы концентрации населения.','The main areas of population concentration.')
# --- 23.4 города
CT=[('Бишкек','Bishkek',74.59,42.87),('Ош','Osh',72.80,40.53),('Джалал-Абад','Jalal-Abad',72.98,40.93),('Каракол','Karakol',78.39,42.49),('Токмок','Tokmok',75.30,42.84),('Балыкчы','Balykchy',76.19,42.46),('Нарын','Naryn',76.0,41.43),('Талас','Talas',72.24,42.52),('Баткен','Batken',70.82,40.06),('Узген','Uzgen',73.30,40.77)]
dxdy={'Бишкек':(0,-34,'middle'),'Токмок':(12,-12,'start'),'Ош':(14,30,'start'),'Джалал-Абад':(-12,-16,'end'),'Узген':(14,-14,'start'),'Балыкчы':(-12,34,'end'),'Каракол':(12,26,'start'),'Нарын':(12,26,'start'),'Талас':(-12,-14,'end'),'Баткен':(0,34,'middle')}
objs=[D(lo,la,r,e,dx=dxdy[r][0],dy=dxdy[r][1],anchor=dxdy[r][2]) for r,e,lo,la in CT]
add('23','## 23.4. ',mk('23','main-cities','Крупные города','Main cities','Города','Cities',objs,'Положение городов показано по координатам центров.','Cities are placed at their centre coordinates.',zoom=(69.0,81.0,38.6,43.9),nocity=True),'Крупные города Кыргызстана.','Main cities of Kyrgyzstan.')
# --- 26.3 ледники
add('26','## 26.3. ',mk('26','glacier-areas','Районы крупного оледенения','Major glaciated areas','Ледники','Glaciers',
  [A(80.0,42.1,0.3,'Иныльчек, Хан-Тенгри','Inylchek, Khan Tengri',dy=-34,dx=30,col='#1f6fb2',anchor='end'),A(78.2,41.8,0.25,'Ак-Шыйрак','Ak-Shyirak',dy=40,dx=8,col='#1f6fb2'),A(74.5,42.5,0.15,'Ала-Арча','Ala-Archa',dy=-4,dx=-20,col='#1f6fb2',anchor='end'),A(72.9,39.4,0.3,'Заалайский хребет','Trans-Alay',dy=38,col='#1f6fb2')],
  'Овалы — районы ледников, а не контуры; положение приблизительное.','Ovals are glaciated areas, not outlines; positions are approximate.',zoom=(69.0,81.0,38.6,43.9),nocity=True),'Основные районы современного оледенения.','The main areas of present-day glaciation.')
json.dump(locdata.ITEMS,open('/home/claude/geo/loc_items2.json','w'),ensure_ascii=False,indent=1)
print(len(locdata.ITEMS))
