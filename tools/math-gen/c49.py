# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Единичная окружность', 'The unit circle'),
 [('r', 'a', 'Угол, °', 'Angle, °', 0, 360, 5, 50)],
 [('В радианах', 'In radians'), ('cos α (абсцисса)', 'cos α (abscissa)'), ('sin α (ордината)', 'sin α (ordinate)')],
 'Угол α откладываем от оси x против часовой стрелки. Точка на единичной окружности имеет координаты (cos α; sin α).', 'The angle α is measured from the x-axis counter-clockwise. The point on the unit circle has coordinates (cos α; sin α).', ('Единичная окружность и точка на ней', 'The unit circle and a point on it'),
 r'''const a=deg(v.a),R0=85,cx=300,cy=105;const px=cx+R0*Math.cos(a),py=cy-R0*Math.sin(a);let g=L(cx-110,cy,cx+110,cy,COL.mut,1.5)+L(cx,cy-100,cx,cy+100,COL.mut,1.5)+C(cx,cy,R0,"none",COL.ink,2.5)+arcA(cx,cy,24,0,a,COL.a,5)+L(cx,cy,px,py,COL.a,3)+L(px,py,px,cy,COL.c,2.5)+L(cx,cy,px,cy,COL.b,2.5)+C(px,py,7,COL.a);
 g+=TX(cx+36,cy-8,v.a+"°",COL.a,13,"start",700)+TX(px+(px>cx?12:-12),py+(py<cy?-8:16),"("+fnum(Math.cos(a),2)+"; "+fnum(Math.sin(a),2)+")",COL.ink,12,px>cx?"start":"end",600);
 const rad=v.a/180;return {svg:g,st:[fnum(rad,3)+"π ≈ "+fnum(rad*Math.PI,3),fnum(Math.cos(a),4),fnum(Math.sin(a),4)],fb:U("Радиан — угол, для которого длина дуги равна радиусу: 1 рад ≈ 57,3°.","A radian is the angle for which the arc length equals the radius: 1 rad ≈ 57.3°.")}''', '0 0 600 215')

m2 = M(('Длина дуги и радианы', 'Arc length and radians'),
 [('r', 'r', 'Радиус', 'Radius', 1, 10, 1, 5), ('r', 'ph', 'Угол в радианах', 'Angle in radians', 0.2, 6.2, 0.1, 1.5)],
 [('Длина дуги s = r·φ', 'Arc length s = r·φ'), ('Угол в градусах', 'Angle in degrees'), ('Доля окружности', 'Part of the circle')],
 'Если угол измерять в радианах, длина дуги равна произведению радиуса на угол: s = r·φ. Это и есть смысл радиана.', 'If the angle is measured in radians the arc length is the radius times the angle: s = r·φ. This is the meaning of a radian.', ('Дуга и сектор', 'An arc and a sector'),
 r'''const R0=85,cx=300,cy=105,a=v.ph;let g=C(cx,cy,R0,COL.bg,COL.line,2)+'<path d="M'+cx+" "+cy+" L"+(cx+R0)+" "+cy+" A"+R0+" "+R0+" 0 "+(a>Math.PI?1:0)+" 0 "+(cx+R0*Math.cos(a)).toFixed(1)+" "+(cy-R0*Math.sin(a)).toFixed(1)+' Z" fill="#f4dfd8" stroke="'+COL.a+'" stroke-width="3"/>';
 g+=TX(cx+30,cy-8,fnum(a,1)+" рад",COL.a,13,"start",700);return {svg:g,st:[fnum(v.r*a,2),fnum(a*180/Math.PI,1)+"°",fnum(a/(2*Math.PI)*100,1)+" %"],fb:U("1 рад: дуга равна радиусу = "+v.r+"; весь круг = 2π ≈ 6,28 рад.","1 rad: the arc equals the radius = "+v.r+"; the whole circle = 2π ≈ 6.28 rad.")}''', '0 0 600 215')

m3 = M(('Точные значения', 'Exact values'),
 [('s', 'k', 'Угол', 'Angle', ['0°', '30°', '45°', '60°', '90°', '120°', '135°', '150°', '180°'], ['0°', '30°', '45°', '60°', '90°', '120°', '135°', '150°', '180°'], 1)],
 [('Радианы', 'Radians'), ('sin', 'sin'), ('cos', 'cos')],
 'Для углов 30°, 45°, 60° значения синуса и косинуса записывают точно: ½, √2/2, √3/2. Остальные получают симметрией.', 'For 30°, 45°, 60° the sine and cosine are written exactly: ½, √2/2, √3/2. The rest follow by symmetry.', ('Точка на единичной окружности', 'A point on the unit circle'),
 r'''const A=[0,30,45,60,90,120,135,150,180][v.k],rd=["0","π/6","π/4","π/3","π/2","2π/3","3π/4","5π/6","π"][v.k],sn=["0","1/2","√2/2","√3/2","1","√3/2","√2/2","1/2","0"][v.k],cs=["1","√3/2","√2/2","1/2","0","−1/2","−√2/2","−√3/2","−1"][v.k],a=deg(A),R0=85,cx=300,cy=105;
 let g=L(cx-110,cy,cx+110,cy,COL.mut,1.5)+L(cx,cy-100,cx,cy+100,COL.mut,1.5)+C(cx,cy,R0,"none",COL.ink,2.5)+L(cx,cy,cx+R0*Math.cos(a),cy-R0*Math.sin(a),COL.a,3)+C(cx+R0*Math.cos(a),cy-R0*Math.sin(a),7,COL.a);
 return {svg:g,st:[rd,sn,cs],fb:U("Проверка: sin² + cos² = 1.","Check: sin² + cos² = 1.")}''', '0 0 600 215')

chapter('49', '49-radians-unit-circle.html', 'VII', ('Радианы и единичная окружность', 'Radians and the unit circle'),
 ('Новый способ измерять углы и новое определение синуса и косинуса — для любых углов, не только острых.', 'A new way to measure angles and a new definition of sine and cosine — for any angles, not only acute ones.'),
 ('Колесо арбы радиусом 0,5 м повернулось на угол 2 радиана.\n\nНа какое расстояние откатилась арба?', 'A cart wheel of radius 0.5 m turned through 2 radians.\n\nHow far did the cart roll?'),
 ('Разгадка: 1 метр', 'The answer: 1 metre'),
 ('Если угол измерен в радианах, то длина дуги s = r · φ = 0,5 · 2 = 1 м. Радиан удобен именно этим: он связывает угол и длину без лишних множителей. Полный оборот — это 2π радиан ≈ 6,28, значит, 360° = 2π рад, 180° = π рад.', 'If the angle is measured in radians, the arc length s = r · φ = 0.5 · 2 = 1 m. The radian is convenient exactly for this: it links angle and length without extra factors. A full turn is 2π radians ≈ 6.28, so 360° = 2π rad, 180° = π rad.'),
 [S('rad', 'Радианная мера', 'Radian measure', ('<strong>1 радиан</strong> — центральный угол, длина дуги которого равна радиусу. Перевод: 180° = π рад, поэтому α° = α · π / 180 рад, а φ рад = φ · 180 / π °. Например, 90° = π/2, 60° = π/3, 45° = π/4, 30° = π/6.', 'A <strong>radian</strong> is the central angle whose arc equals the radius. Conversion: 180° = π rad so α° = α · π / 180 rad and φ rad = φ · 180 / π °. For example 90° = π/2, 60° = π/3, 45° = π/4, 30° = π/6.'),
    ('s = r·φ,  180° = π', '', 's = r·φ,  180° = π'), m2),
  S('uc', 'Единичная окружность', 'The unit circle', ('Окружность радиуса 1 с центром в начале координат — <strong>единичная</strong>. Для угла α (откладывают от оси x против часовой стрелки) точка окружности имеет координаты <strong>(cos α; sin α)</strong>. Так определяют синус и косинус для любого угла, в том числе тупого и отрицательного. Всегда sin²α + cos²α = 1.', 'The circle of radius 1 centred at the origin is the <strong>unit circle</strong>. For an angle α (measured from the x-axis counter-clockwise) the point of the circle has coordinates <strong>(cos α; sin α)</strong>. This defines sine and cosine for any angle, including obtuse and negative ones. Always sin²α + cos²α = 1.'),
    ('(cos α; sin α)', '', '(cos α; sin α)'), m1),
  S('ex', 'Точные значения', 'Exact values', ('Значения для 0°, 30°, 45°, 60°, 90° полезно знать: sin = 0, ½, √2/2, √3/2, 1, а cos идут в обратном порядке. Для углов в других четвертях используют симметрию: sin(180° − α) = sin α, cos(180° − α) = −cos α.', 'It is worth knowing the values for 0°, 30°, 45°, 60°, 90°: sin = 0, ½, √2/2, √3/2, 1 and cos goes in reverse order. For angles in other quadrants we use symmetry: sin(180° − α) = sin α, cos(180° − α) = −cos α.'),
    ('sin(π − α) = sin α', '', 'sin(π − α) = sin α'), m3)],
 [TK(('В радианы', 'To radians'), ('Переведите 120° в радианы.', 'Convert 120° to radians.'), '120 · π / 180', '2π/3.', '2π/3.'),
  TK(('В градусы', 'To degrees'), ('Переведите 3π/4 в градусы.', 'Convert 3π/4 to degrees.'), '3 · 180 / 4', '135°.', '135°.'),
  TK(('Длина дуги', 'Arc length'), ('Радиус 6, угол 1,5 рад. Длина дуги?', 'Radius 6, angle 1.5 rad. The arc length?'), 's = rφ', '6 · 1,5 = 9.', '9.'),
  TK(('Координаты', 'Coordinates'), ('Найдите координаты точки на единичной окружности при угле 90°.', 'Find the coordinates of the point on the unit circle at 90°.'), '', '(cos 90°; sin 90°) = (0; 1).', '(0; 1).'),
  TK(('Симметрия', 'Symmetry'), ('Найдите sin 150°.', 'Find sin 150°.'), '150° = 180° − 30°', 'sin 150° = sin 30° = 1/2.', '1/2.')],
 [Q('π радиан это', 'π radians is', '180°', '90°', '360°', ('Полуоборот.', 'A half turn.')),
  Q('90° в радианах', '90° in radians', 'π/2', 'π', 'π/4', ('180° : 2.', '180° : 2.')),
  Q('Единичная окружность имеет радиус', 'The unit circle has radius', '1', '2', 'π', ('По названию.', 'By name.')),
  Q('Точка при угле 0°', 'The point at angle 0°', '(1; 0)', '(0; 1)', '(0; 0)', ('cos 0 = 1, sin 0 = 0.', 'cos 0 = 1, sin 0 = 0.')),
  Q('sin 90° =', 'sin 90° =', '1', '0', '−1', ('Верхняя точка окружности.', 'The top point of the circle.')),
  Q('cos 180° =', 'cos 180° =', '−1', '1', '0', ('Левая точка окружности.', 'The left point of the circle.')),
  Q('sin²α + cos²α =', 'sin²α + cos²α =', '1', '0', '2', ('Радиус окружности равен 1.', 'The radius of the circle is 1.')),
  Q('Длина дуги при φ = 2π, r = 1', 'Arc length at φ = 2π, r = 1', '2π', 'π', '1', ('Вся окружность.', 'The whole circle.'))],
 src=[('Wikipedia: Radian', 'https://en.wikipedia.org/wiki/Radian'), ('Wikipedia: Unit circle', 'https://en.wikipedia.org/wiki/Unit_circle')],
 note=('Арба и размеры колеса в загадке условные.', 'The cart and wheel size in the puzzle are illustrative.'))
