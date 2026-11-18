from m5 import *
rows=[('Сары-Челек','Sary-Chelek','Джалал-Абад; Чаткал','озеро, леса, луга; биосферный резерват UNESCO (1978)','lake, forests, meadows; UNESCO biosphere reserve (1978)'),
('Беш-Арал','Besh-Aral','Джалал-Абад; Западный Тянь-Шань','горные экосистемы, редкие растения и животные','mountain ecosystems, rare plants and animals'),
('Падыша-Ата','Padysha-Ata','Джалал-Абад','арчовые леса и горные экосистемы','juniper woodlands and mountain ecosystems'),
('Нарынский','Naryn','Внутренний Тянь-Шань','горные леса, водосборы, высокогорье','mountain forests, watersheds, high mountains'),
('Иссык-Кульский','Issyk-Kul','побережье Иссык-Куля','водно-болотные угодья, водоплавающие птицы','wetlands, waterbirds'),
('Каратал-Жапырык','Karatal-Zhapyryk','Сон-Куль, Чатыр-Куль','высокогорные озёра и водно-болотные места','high-mountain lakes and wetlands')]
body=T(40,120,'Заповедник / Reserve','lab')+T(330,120,'Где / Where','lab')+T(700,120,'Что охраняется / What is protected','lab')
for i,(a,b,w,p,q) in enumerate(rows):
    y=140+i*90; body+=box(30,y,1340,78,'#e5efe3' if i%2==0 else '#f1f4f6')+T(46,y+32,a,'t')+T(46,y+58,b,'s')+T(330,y+36,w,'s')+T(700,y+30,p,'s')+T(700,y+56,q,'s','start','style="fill:#526579"')
S('22-C','reserves-comparison','Сравнение основных заповедников','Comparison of the main nature reserves','Где расположены заповедники и что они охраняют.','Where the reserves are and what they protect.',body,'По описаниям главы 22; угрозы, площади и точные границы — в официальных источниках.','Based on the Chapter 22 descriptions; threats, areas and exact boundaries are in official sources.','Основные заповедники: сравнение.','Main nature reserves: comparison.')
