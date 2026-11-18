from kit import *; from out import save
FR='Основа: Natural Earth (общественное достояние). Учебная схема: положение объектов ориентировочное, не для определения границ и не для навигации.'
FE='Base: Natural Earth (public domain). Teaching schematic: feature positions are approximate; not for boundary delimitation or navigation.'
def kg(): return KG().ctx().oblasts(opacity=.55).outline()
RNG=[ # key,a,b,ru,en,system,offset
('kung',(76.6,42.8),(78.6,42.85),'Кюнгёй-Ала-Тоо','Kungey Ala-Too','N',(0,-12)),
('kyr',(72.4,42.25),(76.3,42.65),'Кыргызский хребет','Kyrgyz Range','N',(0,-12)),
('tal',(70.9,41.95),(72.8,42.4),'Таласский Ала-Тоо','Talas Ala-Too','W',(0,-10)),
('cha',(70.7,41.5),(72.3,41.85),'Чаткальский','Chatkal','W',(0,12)),
('fer',(72.8,41.6),(74.6,40.6),'Ферганский','Fergana Range','W',(30,0)),
('ter',(76.9,42.15),(79.4,42.0),'Терскей-Ала-Тоо','Terskey Ala-Too','C',(0,18)),
('mol',(74.6,41.75),(76.2,41.9),'Молдо-Тоо','Moldo-Too','I',(0,-10)),
('atb',(74.8,41.1),(77.4,41.2),'Ат-Башы','At-Bashy','I',(0,12)),
('kok',(75.8,40.6),(79.8,41.0),'Кокшаал-Тоо','Kokshaal-Too','C',(0,14)),
('ala',(70.5,39.85),(73.8,39.75),'Алайский','Alay','P',(0,-12)),
('tur',(69.4,39.6),(70.6,39.7),'Туркестанский','Turkestan','P',(0,14)),
('zaa',(72.4,39.4),(74.0,39.35),'Заалайский','Trans-Alay','P',(0,12)),
]
SYS={'N':('#2e86ab','Северный Тянь-Шань','Northern Tien Shan'),'W':('#6a994e','Западный Тянь-Шань','Western Tien Shan'),'I':('#bc6c25','Внутренний Тянь-Шань','Inner Tien Shan'),'C':('#7b4b94','Центральный Тянь-Шань','Central Tien Shan'),'P':('#c0392b','Памиро-Алай','Pamir-Alay')}
PEAKS=[(80.12,42.04,'Жеңиш чокусу (Победы) 7439 м','Jengish Chokusu (Pobeda) 7,439 m'),(72.88,39.34,'пик Ибн Сина (Ленина) 7134 м','Ibn Sina (Lenin) Peak 7,134 m')]
def lakes_rivers(m):
    m.water()
    m.line([(76.15,42.5),(75.3,42.85),(74.0,42.93),(72.8,43.05),(71.2,43.3)],w=2.2)
    m.line([(72.3,42.45),(71.2,42.75),(70.2,42.95)],w=2.2)
    return m
# 17-H
m=kg(); lakes_rivers(m)
for lo,la,ru,en,c in [(78.2,41.87,'Кумтор: золото','Kumtor: gold','#d4a017'),(71.7,39.9,'Кадамжай: сурьма','Kadamjai: antimony','#7f8c8d'),(71.3,39.95,'Хайдаркан: ртуть','Khaidarkan: mercury','#7f8c8d'),(71.9,40.3,'Кызыл-Кыя, Сулюкта: уголь','Kyzyl-Kiya, Sulukta: coal','#34495e'),(72.2,41.35,'Таш-Кумыр, Кок-Янгак: уголь','Tash-Kumyr, Kok-Yangak: coal','#34495e'),(72.45,41.27,'Майлуу-Суу: наследие урана','Mailuu-Suu: uranium legacy','#8e44ad')]:
    pass
m.dot(78.2,41.87,'Кумтор: золото','Kumtor: gold',7,'#d4a017',10,-8)
m.dot(71.72,39.92,'Кадамжай: сурьма','Kadamjai: antimony',7,'#7f8c8d',-10,18,'end')
m.dot(71.3,40.0,'Хайдаркан: ртуть','Khaidarkan: mercury',7,'#7f8c8d',-10,-8,'end')
m.dot(72.13,40.26,'Кызыл-Кыя: уголь','Kyzyl-Kiya: coal',7,'#34495e',-10,-10,'end')
m.dot(72.22,41.35,'Таш-Кумыр: уголь','Tash-Kumyr: coal',7,'#34495e',-10,-8,'end')
m.dot(72.45,41.27,'Майлуу-Суу: наследие урана','Mailuu-Suu: uranium legacy',7,'#8e44ad',10,16)
m.dot(73.2,41.0,'Кок-Янгак: уголь','Kok-Yangak: coal',7,'#34495e',10,8)
m.city('Bishkek'); m.city('Osh',dy=16)
m.legend([('золото','gold','#d4a017'),('уголь','coal','#34495e'),('сурьма, ртуть','antimony, mercury','#7f8c8d'),('урановое наследие (не действующий рудник)','uranium legacy (not an active mine)','#8e44ad')],x=60,y=660)
save('17-H','mineral-districts-schematic','Основные минеральные районы Кыргызстана (схема)','Main mineral districts of Kyrgyzstan (schematic)',
 'Схема районов добычи золота, угля, сурьмы и ртути и уранового наследия; запасы не показаны.','Schematic of gold, coal, antimony and mercury districts and uranium legacy; reserves are not shown.',
 wrap('Основные минеральные районы Кыргызстана (схема)','Main mineral districts of Kyrgyzstan (schematic)','Схема районов добычи золота, угля, сурьмы и ртути и уранового наследия.',m.svg(),'Показаны районы, а не доказанные запасы и не лицензионные участки; статус объектов проверять по официальному реестру недропользования. '+FR[:0],'Districts only: no proven reserves or licence areas are shown; check each site\'s status in the official subsoil register.'),
 'Районы добычи и наследия: схема без запасов и лицензионных границ.','Mining districts and legacy sites: schematic without reserves or licence boundaries.')
# 18-A physical
m=kg(); lakes_rivers(m)
for k,a,b,ru,en,sy,off in RNG: m.rng(a,b,ru,en,off=off)
for lo,la,ru,en in PEAKS: m.dot(lo,la,ru,en,6,'#fff',-8,-8,'end') if lo>79 else m.dot(lo,la,ru,en,6,'#fff',8,-8)
for lo,la,ru,en in [(77.2,42.45,'оз. Иссык-Куль','Lake Issyk-Kul'),(72.85,41.7,'Токтогульское вдхр.','Toktogul Reservoir')]: m.text(lo,la-0.0,ru,en,'sm')
m.text(74.5,43.2,'Чуйская долина','Chuy Valley'); m.text(72.0,40.75,'Ферганская долина','Fergana Valley'); m.text(76.1,41.55,'Нарынская впадина','Naryn Basin');m.text(75.4,40.55,'Арпа, Ат-Башы, Чатыр-Куль','Arpa, At-Bashy, Chatyr-Kul basins')
m.city('Bishkek'); m.city('Osh',dy=16); m.city('Naryn',dy=16)
save('18-A','physical-schematic','Физико-географическая схема Кыргызстана','Physical-geography schematic of Kyrgyzstan',
 'Основные хребты, межгорные впадины, озёра, реки и высочайшие вершины.','Main ranges, intermontane basins, lakes, rivers and highest peaks.',
 wrap('Физико-географическая схема Кыргызстана','Physical-geography schematic of Kyrgyzstan','Основные хребты, межгорные впадины, озёра, реки и высочайшие вершины.',m.svg(),'Схема без цифровой модели рельефа: хребты показаны линиями, положение ориентировочное. '+FR[FR.index('Основа'):FR.index('Учебная')] ,'Schematic without a digital elevation model: ranges are lines at approximate positions. '+FE[:FE.index('Teaching')]),
 'Хребты, впадины, озёра и реки; высотная гипсометрия на схеме не показана.','Ranges, basins, lakes and rivers; hypsometry is not shown in this schematic.')
# 18-G orography
m=kg(); lakes_rivers(m)
for k,a,b,ru,en,sy,off in RNG: m.rng(a,b,ru,en,color=SYS[sy][0],w=12,off=off)
m.legend([(SYS[k][1],SYS[k][2],SYS[k][0]) for k in SYS],x=60,y=660)
m.city('Bishkek'); m.city('Osh',dy=16)
save('18-G','orographic-systems','Орографические системы Кыргызстана','Orographic systems of Kyrgyzstan',
 'Главные хребты, сгруппированные по Северному, Западному, Внутреннему, Центральному Тянь-Шаню и Памиро-Алаю.','Main ranges grouped into the Northern, Western, Inner and Central Tien Shan and the Pamir-Alay.',
 wrap('Орографические системы Кыргызстана','Orographic systems of Kyrgyzstan','Главные хребты, сгруппированные по горным системам.',m.svg(),'Группировка условна: разные авторы проводят границы между частями Тянь-Шаня по-разному; положение хребтов ориентировочное.','Grouping is conventional: authors draw the divisions of the Tien Shan differently; range positions are approximate.'),
 'Хребты по горным системам; границы систем условны.','Ranges by mountain system; system boundaries are conventional.')
# 18-F tectonic
m=kg(); lakes_rivers(m)
m.line([(71.0,42.7),(72.5,41.8),(74.2,40.5)],'#c0392b',4); m.text(72.6,41.55,'Таласо-Ферганский разлом','Talas–Fergana Fault','sm','middle','#c0392b')
m.line([(74.5,42.2),(76.5,42.15),(79.5,42.0)],'#7b4b94',3,'10 6'); m.text(77.9,41.75,'Линия Николаева (схема)','Nikolaev Line (schematic)','sm','middle','#7b4b94')
m.line([(75.5,41.25),(77.5,41.3),(80,41.4)],'#bc6c25',3,'10 6'); m.text(78.2,41.55,'Атбаши–Иныльчекский разлом','Atbashi–Inylchek Fault','sm','middle','#bc6c25')
m.blob(77.5,42.4,200,28,'#2e86ab','Северный Тянь-Шань','Northern TS',.18,-3)
m.blob(75.8,41.6,170,34,'#bc6c25','Средний Тянь-Шань','Middle TS',.18,-3)
m.blob(77.6,40.95,170,26,'#7b4b94','Южный Тянь-Шань','Southern TS',.18,-4)
m.blob(72.4,39.95,150,28,'#c0392b','Алай (Памиро-Алай)','Alay (Pamir-Alay)',.18)
m.blob(78.0,39.8,150,30,'#7f8c8d','Таримский блок (Китай)','Tarim block (China)',.18)
m.city('Bishkek'); m.city('Osh',dy=16)
save('18-F','tectonic-schematic','Тектоническая схема Тянь-Шаня (упрощённая)','Tectonic schematic of the Tien Shan (simplified)',
 'Упрощённые тектонические зоны Тянь-Шаня и главные разломы.','Simplified Tien Shan tectonic zones and major faults.',
 wrap('Тектоническая схема Тянь-Шаня (упрощённая)','Tectonic schematic of the Tien Shan (simplified)','Упрощённые тектонические зоны и главные разломы.',m.svg(),'Упрощённая схема по учебной модели «северные–средние–южные зоны»; трассы разломов ориентировочные, детали — по геологическим картам КР.','Simplified teaching model of northern–middle–southern zones; fault traces are approximate — see geological maps of Kyrgyzstan for detail.'),
 'Упрощённая тектоника Тянь-Шаня; трассы разломов ориентировочные.','Simplified Tien Shan tectonics; fault traces are approximate.')
# 18-E hazards
m=kg(); lakes_rivers(m)
m.blob(72.2,41.0,150,60,'#c0392b','Сейсмоактивная Ферганская зона','Fergana seismic zone',.28)
m.blob(76.5,42.6,170,38,'#c0392b','Иссык-Куль–Чу: сейсмика','Issyk-Kul–Chuy: seismic',.28,-4)
m.blob(72.6,41.6,120,34,'#8e5b2c','Оползни: предгорья','Landslides: foothills',.32,20)
m.blob(72.8,40.1,150,28,'#8e5b2c','Сели: южные предгорья','Debris flows: southern foothills',.3)
m.blob(74.7,42.4,110,24,'#2e86ab','Ледниковые озёра (сев. склон)','Glacial lakes (north slope)',.3,-4)
m.blob(78.0,42.05,110,22,'#2e86ab','Ледниковые озёра (Терскей)','Glacial lakes (Terskey)',.3)
m.blob(74.5,41.9,70,16,'#7f8c8d','Лавины: перевалы','Avalanches: passes',.4,-8)
m.legend([('землетрясения','earthquakes','#c0392b'),('оползни, сели','landslides, debris flows','#8e5b2c'),('ледниковые озёра','glacial lakes','#2e86ab'),('лавины','avalanches','#7f8c8d')],x=60,y=690)
m.city('Bishkek'); m.city('Osh',dy=16)
save('18-E','geohazard-zones-schematic','Зоны геологических опасностей (качественная схема)','Geological hazard zones (qualitative schematic)',
 'Качественная схема районов землетрясений, оползней, селей, лавин и ледниковых озёр.','Qualitative schematic of earthquake, landslide, debris-flow, avalanche and glacial-lake areas.',
 wrap('Зоны геологических опасностей (качественная схема)','Geological hazard zones (qualitative schematic)','Качественная схема районов опасных процессов.',m.svg(),'Это не карта риска и не оперативная карта опасностей: показаны районы, где процессы типичны; опасность, экспозиция и уязвимость — разные понятия.','Not a risk map or operational hazard map: it shows areas where processes are typical; hazard, exposure and vulnerability are different concepts.'),
 'Качественная схема опасных процессов; не карта риска.','Qualitative schematic of hazardous processes; not a risk map.')
print('ok')
