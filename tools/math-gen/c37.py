# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Синус, косинус, тангенс', 'Sine, cosine, tangent'),
 [('r', 'al', 'Угол α, °', 'Angle α, °', 5, 85, 1, 37), ('r', 'c', 'Гипотенуза', 'Hypotenuse', 5, 20, 1, 10)],
 [('sin α = противолежащий : гипотенуза', 'sin α = opposite : hypotenuse'), ('cos α = прилежащий : гипотенуза', 'cos α = adjacent : hypotenuse'), ('tan α = противолежащий : прилежащий', 'tan α = opposite : adjacent')],
 'Отношения сторон прямоугольного треугольника зависят только от угла, а не от размеров. Поэтому для угла придумали таблицы и кнопки калькулятора.', 'The ratios of sides of a right triangle depend only on the angle, not on the size. That is why angles got tables and calculator keys.', ('Прямоугольный треугольник с углом α', 'A right triangle with angle α'),
 r'''const a=deg(v.al),c=v.c,ad=c*Math.cos(a),op=c*Math.sin(a);const F=fitPts([[0,0],[ad,0],[ad,op]],130,15,340,180);
 let g=poly(F,"#f4dfd8",COL.ink,3)+poly([[F[1][0]-13,F[1][1]],[F[1][0]-13,F[1][1]-13],[F[1][0],F[1][1]-13]],"none",COL.ink,1.5)+arcA(F[0][0],F[0][1],34,0,a,COL.a,5)+TX(F[0][0]+50,F[0][1]-10,v.al+"°",COL.a,14,"start",700);
 g+=TX((F[0][0]+F[1][0])/2,F[0][1]+17,U("прилежащий ","adjacent ")+fnum(ad,2),COL.b,13,"middle",600)+TX(F[1][0]+8,(F[1][1]+F[2][1])/2,U("противолежащий ","opposite ")+fnum(op,2),COL.c,13,"start",600)+TX((F[0][0]+F[2][0])/2-10,(F[0][1]+F[2][1])/2-8,fnum(c,0),COL.ink,13,"end",600);
 return {svg:g,st:[fnum(Math.sin(a),4),fnum(Math.cos(a),4),fnum(Math.tan(a),4)],fb:U("Измените гипотенузу — отношения не изменятся: они зависят только от угла.","Change the hypotenuse — the ratios do not change: they depend only on the angle.")}''', '0 0 600 215')

m2 = M(('Решение прямоугольного треугольника', 'Solving a right triangle'),
 [('r', 'c', 'Гипотенуза', 'Hypotenuse', 5, 30, 1, 20), ('r', 'al', 'Угол α, °', 'Angle α, °', 10, 80, 1, 30)],
 [('Катет напротив α = c·sin α', 'Leg opposite α = c·sin α'), ('Катет рядом с α = c·cos α', 'Leg adjacent to α = c·cos α'), ('Второй угол', 'The other angle')],
 'Зная гипотенузу и острый угол, находим оба катета и второй угол — «решаем» треугольник.', 'Knowing the hypotenuse and an acute angle we find both legs and the other angle — we “solve” the triangle.', ('Решённый треугольник', 'A solved triangle'),
 r'''const a=deg(v.al),ad=v.c*Math.cos(a),op=v.c*Math.sin(a);const F=fitPts([[0,0],[ad,0],[ad,op]],130,15,340,180);
 let g=poly(F,"#f4dfd8",COL.ink,3)+arcA(F[0][0],F[0][1],34,0,a,COL.a,5)+arcA(F[2][0],F[2][1],34,deg(270)-0,deg(270)+deg(90-v.al)*0+0,COL.b,0)+TX(F[0][0]+50,F[0][1]-10,v.al+"°",COL.a,14,"start",700)+TX(F[2][0]-10,F[2][1]+36,(90-v.al)+"°",COL.b,14,"end",700);
 g+=TX((F[0][0]+F[1][0])/2,F[0][1]+17,fnum(ad,2),COL.b,14,"middle",700)+TX(F[1][0]+8,(F[1][1]+F[2][1])/2,fnum(op,2),COL.c,14,"start",700);
 return {svg:g,st:[fnum(op,2),fnum(ad,2),(90-v.al)+"°"],fb:U("Проверка по Пифагору: "+fnum(op*op+ad*ad,1)+" = "+v.c+"² = "+v.c*v.c+".","Pythagoras check: "+fnum(op*op+ad*ad,1)+" = "+v.c+"² = "+v.c*v.c+".")}''', '0 0 600 215')

m3 = M(('Высота по углу подъёма', 'Height from the angle of elevation'),
 [('r', 'd', 'Расстояние до основания, м', 'Distance to the base, m', 10, 200, 5, 80), ('r', 'al', 'Угол подъёма, °', 'Angle of elevation, °', 5, 75, 1, 30), ('r', 'e', 'Высота глаза, м', 'Eye height, m', 1, 2, 0.1, 1.6)],
 [('Высота над глазом d·tan α', 'Height above the eye d·tan α'), ('Полная высота', 'Total height'), ('Прямая до вершины', 'Straight line to the top')],
 'Смотрим на вершину под углом α с расстояния d. Тогда высота над уровнем глаз равна d · tan α.', 'We look at the top at angle α from distance d. Then the height above eye level is d · tan α.', ('Измерение высоты угломером', 'Measuring height with a protractor'),
 r'''const a=deg(v.al),hh=v.d*Math.tan(a),tot=hh+v.e,sc=Math.min(500/v.d,170/tot*0.9),ox=50,oy=185,X=t=>ox+t*sc,Y=t=>oy-t*sc;
 let g=L(30,oy,570,oy,COL.ink,3)+R(X(v.d)-8,Y(tot),16,tot*sc,COL.c,COL.ink,1.5,2)+L(X(0),Y(v.e),X(v.d),Y(v.e),COL.mut,1.5)+L(X(0),Y(v.e),X(v.d),Y(tot),COL.a,3)+L(X(0),oy,X(0),Y(v.e),COL.b,5)+C(X(0),Y(v.e)-4,5,COL.b)+arcA(X(0),Y(v.e),44,0,a,COL.a,5)+TX(X(0)+56,Y(v.e)-6,v.al+"°",COL.a,14,"start",700)+TX(X(v.d/2),oy+17,v.d+" м",COL.mut,13);
 return {svg:g,st:[fnum(hh,1)+" м",fnum(tot,1)+" м",fnum(v.d/Math.cos(a),1)+" м"],fb:U("Чем дальше от основания, тем меньше нужен угол для той же высоты.","The farther from the base, the smaller the angle needed for the same height.")}''', '0 0 600 215')

chapter('37', '37-right-triangle-trig.html', 'V', ('Тригонометрия в прямоугольном треугольнике', 'Trigonometry in a right triangle'),
 ('Что такое синус, косинус и тангенс острого угла и как они помогают решать треугольники и измерять высоты.', 'What the sine, cosine and tangent of an acute angle are and how they help to solve triangles and measure heights.'),
 ('Геодезист стоит в 100 м от подножия башни и видит её вершину под углом 30° к горизонту.\n\nКак найти высоту башни, не поднимаясь на неё? (tan 30° ≈ 0,577)', 'A surveyor stands 100 m from the foot of a tower and sees its top at 30° above the horizon.\n\nHow can the height of the tower be found without climbing it? (tan 30° ≈ 0.577)'),
 ('Разгадка: около 58 м', 'The answer: about 58 m'),
 ('Расстояние до башни — прилежащий катет, высота — противолежащий. Тангенс угла — их отношение: tan 30° = h : 100. Значит, h = 100 · 0,577 ≈ 57,7 м (плюс высота глаза геодезиста, если нужна полная высота). Так измеряют горы и здания — по одному расстоянию и одному углу.', 'The distance to the tower is the adjacent leg, the height is the opposite one. The tangent of the angle is their ratio: tan 30° = h : 100. So h = 100 · 0.577 ≈ 57.7 m (plus the surveyor’s eye height if the total height is needed). This is how mountains and buildings are measured — from one distance and one angle.'),
 [S('def', 'Синус, косинус, тангенс', 'Sine, cosine, tangent', ('Для острого угла α прямоугольного треугольника: <strong>sin α</strong> = противолежащий катет : гипотенуза; <strong>cos α</strong> = прилежащий катет : гипотенуза; <strong>tan α</strong> = противолежащий : прилежащий. Эти отношения не зависят от размеров треугольника, только от угла. Основное тождество: sin²α + cos²α = 1 (это теорема Пифагора).', 'For an acute angle α of a right triangle: <strong>sin α</strong> = opposite leg : hypotenuse; <strong>cos α</strong> = adjacent leg : hypotenuse; <strong>tan α</strong> = opposite : adjacent. These ratios do not depend on the size of the triangle, only on the angle. The basic identity: sin²α + cos²α = 1 (this is the Pythagorean theorem).'),
    ('sin²α + cos²α = 1', 'tan α = sin α / cos α', 'tan α = sin α / cos α'), m1),
  S('solve', 'Решение прямоугольных треугольников', 'Solving right triangles', ('Решить треугольник — найти все его стороны и углы. По гипотенузе c и углу α: противолежащий катет a = c · sin α, прилежащий b = c · cos α, второй угол 90° − α. Запомните значения для 30°, 45°, 60°: sin = ½, √2/2, √3/2.', 'To solve a triangle is to find all its sides and angles. From hypotenuse c and angle α: the opposite leg a = c · sin α, the adjacent leg b = c · cos α, the other angle 90° − α. Remember the values for 30°, 45°, 60°: sin = ½, √2/2, √3/2.'),
    ('a = c·sin α,  b = c·cos α', '', 'a = c·sin α,  b = c·cos α'), m2),
  S('elev', 'Угол подъёма', 'The angle of elevation', ('<strong>Угол подъёма</strong> — угол между горизонтом и направлением на предмет. Если расстояние до основания d, то высота над уровнем глаз h = d · tan α. Угол находят угломером, или телефоном с датчиками, а тангенс — по таблице или калькулятору.', 'The <strong>angle of elevation</strong> is the angle between the horizon and the direction to an object. If the distance to the base is d, the height above eye level is h = d · tan α. The angle is found with a protractor or a phone’s sensors, the tangent from a table or calculator.'),
    ('h = d · tan α', '', 'h = d · tan α'), m3)],
 [TK(('Синус', 'Sine'), ('Катет 3, гипотенуза 5. Найдите sin и cos угла, противолежащего катету 3.', 'Leg 3, hypotenuse 5. Find sin and cos of the angle opposite the leg 3.'), '', 'sin = 3/5 = 0,6; cos = 4/5 = 0,8 (второй катет 4).', ('0,6 и 0,8.', '0.6 and 0.8.')),
  TK(('Катет', 'A leg'), ('Гипотенуза 20, угол 30°. Катет против угла?', 'Hypotenuse 20, angle 30°. The leg opposite the angle?'), 'sin 30° = 0,5', '20 · 0,5 = 10.', '10.'),
  TK(('Тангенс', 'Tangent'), ('Катеты 5 и 5. Найдите угол.', 'Legs 5 and 5. Find the angle.'), 'tan α = 1', 'α = 45°.', '45°.'),
  TK(('Высота', 'Height'), ('Расстояние до дерева 40 м, угол подъёма 45°. Высота над уровнем глаз?', 'Distance to a tree 40 m, angle of elevation 45°. Height above eye level?'), 'tan 45° = 1', '40 · 1 = 40.', '40 м.'),
  TK(('Тождество', 'Identity'), ('sin α = 0,6. Найдите cos α (α острый).', 'sin α = 0.6. Find cos α (α acute).'), 'cos² = 1 − 0,36', 'cos² = 0,64, cos = 0,8.', '0,8.')],
 [Q('sin α =', 'sin α =', ('противолежащий : гипотенуза', 'opposite : hypotenuse'), ('прилежащий : гипотенуза', 'adjacent : hypotenuse'), ('противолежащий : прилежащий', 'opposite : adjacent'), ('Определение.', 'The definition.')),
  Q('tan α =', 'tan α =', ('sin α : cos α', 'sin α : cos α'), ('cos α : sin α', 'cos α : sin α'), ('sin α · cos α', 'sin α · cos α'), ('Отношение катетов.', 'The ratio of legs.')),
  Q('sin 30° =', 'sin 30° =', '1/2', '√3/2', '1', ('Значение для 30°.', 'The value for 30°.')),
  Q('sin²α + cos²α =', 'sin²α + cos²α =', '1', '0', '2', ('Тождество.', 'The identity.')),
  Q('Угол 45° — катеты', 'At 45° the legs are', ('равны', 'equal'), ('1 и 2', '1 and 2'), ('3 и 4', '3 and 4'), ('tan 45° = 1.', 'tan 45° = 1.')),
  Q('Чему равен cos 60°?', 'What is cos 60°?', '1/2', '√3/2', '0', ('cos 60° = sin 30°.', 'cos 60° = sin 30°.')),
  Q('Острые углы прямоугольного: 35° и', 'Acute angles of a right triangle: 35° and', '55°', '45°', '65°', ('90° − 35°.', '90° − 35°.')),
  Q('Угол подъёма измеряют от', 'The angle of elevation is measured from', ('горизонта', 'the horizon'), ('вертикали', 'the vertical'), ('земли вниз', 'the ground downwards'), ('Между горизонтом и направлением взгляда.', 'Between the horizon and the line of sight.'))],
 src=[('Wikipedia: Trigonometric functions', 'https://en.wikipedia.org/wiki/Trigonometric_functions'), ('Wikipedia: Solution of triangles', 'https://en.wikipedia.org/wiki/Solution_of_triangles')],
 note=('Башня и расстояния в загадке условные.', 'The tower and distances in the puzzle are illustrative.'))
