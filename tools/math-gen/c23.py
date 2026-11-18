# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Точка на координатной плоскости', 'A point on the coordinate plane'),
 [('r', 'x', 'x', 'x', -6, 6, 1, 3), ('r', 'y', 'y', 'y', -5, 5, 1, -2)],
 [('Координаты', 'Coordinates'), ('Четверть', 'Quadrant'), ('Расстояние до начала', 'Distance from the origin')],
 'Две оси задают положение точки: x — по горизонтали, y — по вертикали.', 'Two axes fix the position of a point: x horizontally, y vertically.', ('Координатная плоскость', 'The coordinate plane'),
 r'''const G=Gr({x0:-7,x1:7,y0:-6,y1:6,L:100,T:10,W:400,H:220});let g=G.grid(1,1)+G.seg(v.x,0,v.x,v.y,COL.mut,1.5)+G.seg(0,v.y,v.x,v.y,COL.mut,1.5)+G.pt(v.x,v.y,COL.a,8)+G.txt(v.x+0.9,v.y+0.5,"("+v.x+"; "+v.y+")",COL.a,14);
 const qd=v.x===0||v.y===0?U("на оси","on an axis"):v.x>0&&v.y>0?"I":v.x<0&&v.y>0?"II":v.x<0&&v.y<0?"III":"IV";return {svg:g,st:["("+v.x+"; "+v.y+")",qd,fnum(Math.sqrt(v.x*v.x+v.y*v.y),2)],fb:U("Первая координата — абсцисса, вторая — ордината.","The first coordinate is the abscissa, the second the ordinate.")}''', '0 0 600 250')

m2 = M(('Отрезок: длина и середина', 'A segment: length and midpoint'),
 [('r', 'x1', 'x₁', 'x₁', -6, 6, 1, -4), ('r', 'y1', 'y₁', 'y₁', -5, 5, 1, -2), ('r', 'x2', 'x₂', 'x₂', -6, 6, 1, 4), ('r', 'y2', 'y₂', 'y₂', -5, 5, 1, 2)],
 [('Горизонтально и вертикально', 'Horizontally and vertically'), ('Длина отрезка', 'Length of the segment'), ('Середина', 'Midpoint')],
 'Длина по теореме Пифагора: корень из суммы квадратов разностей координат. Середина — средние арифметические координат.', 'Length by the Pythagorean theorem: the root of the sum of squared coordinate differences. The midpoint — the means of the coordinates.', ('Отрезок на плоскости', 'A segment on the plane'),
 r'''const G=Gr({x0:-7,x1:7,y0:-6,y1:6,L:100,T:10,W:400,H:220});const dx=v.x2-v.x1,dy=v.y2-v.y1,len=Math.sqrt(dx*dx+dy*dy),mx=(v.x1+v.x2)/2,my=(v.y1+v.y2)/2;
 let g=G.grid(1,1)+G.seg(v.x1,v.y1,v.x2,v.y1,COL.mut,1.5)+G.seg(v.x2,v.y1,v.x2,v.y2,COL.mut,1.5)+G.seg(v.x1,v.y1,v.x2,v.y2,COL.ink,3)+G.pt(v.x1,v.y1,COL.a,7)+G.pt(v.x2,v.y2,COL.b,7)+G.pt(mx,my,COL.c,6);
 return {svg:g,st:["Δx = "+dx+",  Δy = "+dy,"√("+dx*dx+" + "+dy*dy+") = "+fnum(len,3),"("+fnum(mx,1)+"; "+fnum(my,1)+")"],fb:U("Середина: ("+v.x1+" + "+v.x2+") : 2 и ("+v.y1+" + "+v.y2+") : 2.","Midpoint: ("+v.x1+" + "+v.x2+") : 2 and ("+v.y1+" + "+v.y2+") : 2.")}''', '0 0 600 250')

m3 = M(('Симметрия относительно осей', 'Symmetry about the axes'),
 [('r', 'x', 'x', 'x', -6, 6, 1, 3), ('r', 'y', 'y', 'y', -5, 5, 1, 2), ('s', 'k', 'Симметрия', 'Symmetry', ['относительно оси x', 'относительно оси y', 'относительно начала координат'], ['about the x-axis', 'about the y-axis', 'about the origin'], 0)],
 [('Исходная точка', 'The original point'), ('Симметричная точка', 'The symmetric point'), ('Правило', 'The rule')],
 'Осевая симметрия меняет знак одной координаты, центральная симметрия — обеих.', 'Reflection in an axis changes the sign of one coordinate; point reflection changes both.', ('Точка и её отражение', 'A point and its reflection'),
 r'''const G=Gr({x0:-7,x1:7,y0:-6,y1:6,L:100,T:10,W:400,H:220});const nx=v.k===0?v.x:-v.x,ny=v.k===1?v.y:-v.y;
 let g=G.grid(1,1)+G.seg(v.x,v.y,nx,ny,COL.mut,1.5)+G.pt(v.x,v.y,COL.a,8)+G.pt(nx,ny,COL.b,8)+G.txt(v.x+0.8,v.y+0.5,"("+v.x+"; "+v.y+")",COL.a,13)+G.txt(nx+0.8,ny-0.7,"("+nx+"; "+ny+")",COL.b,13);
 return {svg:g,st:["("+v.x+"; "+v.y+")","("+nx+"; "+ny+")",["(x; −y)","(−x; y)","(−x; −y)"][v.k]],fb:U("Расстояния до оси или центра симметрии у точки и её образа равны.","A point and its image are equally far from the axis or the centre.")}''', '0 0 600 250')

chapter('23', '23-coordinates.html', 'IV', ('Координатная прямая и плоскость', 'The number line and the coordinate plane'),
 ('Как задать положение точки двумя числами, найти расстояние и середину отрезка и отразить точку.', 'How to fix a point by two numbers, find the distance and midpoint of a segment and reflect a point.'),
 ('Туристу сказали: «Озеро находится в 6 км к востоку и в 8 км к северу от лагеря».\n\nНа каком расстоянии по прямой от лагеря озеро?', 'A tourist was told: “The lake is 6 km east and 8 km north of the camp”.\n\nHow far in a straight line is the lake from the camp?'),
 ('Разгадка: 10 км', 'The answer: 10 km'),
 ('Лагерь — начало координат, озеро — точка (6; 8). Путь на восток и на север — катеты прямоугольного треугольника, а прямой путь — его гипотенуза: √(6² + 8²) = √100 = 10 км. Координаты позволяют превратить геометрию в вычисления.', 'The camp is the origin, the lake is the point (6; 8). The way east and north are the legs of a right triangle, the straight way is its hypotenuse: √(6² + 8²) = √100 = 10 km. Coordinates turn geometry into calculations.'),
 [S('plane', 'Координатная плоскость', 'The coordinate plane', ('Две перпендикулярные числовые оси пересекаются в начале координат O. Положение точки задаёт пара чисел (x; y): <strong>абсцисса</strong> и <strong>ордината</strong>. Оси делят плоскость на четыре <strong>четверти</strong>: I (+; +), II (−; +), III (−; −), IV (+; −).', 'Two perpendicular number axes meet at the origin O. The position of a point is given by a pair (x; y): the <strong>abscissa</strong> and <strong>ordinate</strong>. The axes divide the plane into four <strong>quadrants</strong>: I (+; +), II (−; +), III (−; −), IV (+; −).'),
    ('A(x; y)', '', 'A(x; y)'), m1),
  S('seg', 'Расстояние и середина', 'Distance and midpoint', ('Расстояние между точками (x₁; y₁) и (x₂; y₂) находят по теореме Пифагора. Середина отрезка имеет координаты — средние арифметические концов.', 'The distance between points (x₁; y₁) and (x₂; y₂) is found by the Pythagorean theorem. The midpoint of a segment has the mean coordinates of the ends.'),
    ('d = √((x₂−x₁)² + (y₂−y₁)²)', 'M = ((x₁+x₂)/2; (y₁+y₂)/2)', 'M = ((x₁+x₂)/2; (y₁+y₂)/2)'), m2),
  S('sym', 'Симметрия', 'Symmetry', ('Отражение в оси x: (x; y) → (x; −y). В оси y: (x; y) → (−x; y). Относительно начала координат: (x; y) → (−x; −y). Эти правила используют при построении графиков и в геометрии.', 'Reflection in the x-axis: (x; y) → (x; −y). In the y-axis: (x; y) → (−x; y). About the origin: (x; y) → (−x; −y). These rules are used in graphing and geometry.'),
    ('(x; y) → (−x; y)', 'отражение в оси y', 'reflection in the y-axis'), m3)],
 [TK(('Четверть', 'Quadrant'), ('В какой четверти точка (−3; 5)?', 'In which quadrant is the point (−3; 5)?'), '(−; +)', 'x &lt; 0, y &gt; 0 — это вторая четверть.', 'II.'),
  TK(('Расстояние', 'Distance'), ('Найдите расстояние между (1; 2) и (4; 6).', 'Find the distance between (1; 2) and (4; 6).'), 'Δx = 3, Δy = 4', '√(9 + 16) = 5.', '5.'),
  TK(('Середина', 'Midpoint'), ('Найдите середину отрезка с концами (−2; 3) и (6; −1).', 'Find the midpoint of the segment with ends (−2; 3) and (6; −1).'), '', '((−2 + 6) : 2; (3 − 1) : 2) = (2; 1).', '(2; 1).'),
  TK(('Отражение', 'Reflection'), ('Отразите точку (4; −3) относительно оси x.', 'Reflect the point (4; −3) in the x-axis.'), '(x; −y)', '(4; 3).', '(4; 3).'),
  TK(('Параллелограмм', 'A parallelogram'), ('Три вершины параллелограмма: (0; 0), (4; 0), (5; 3). Найдите четвёртую.', 'Three vertices of a parallelogram: (0; 0), (4; 0), (5; 3). Find the fourth.'), 'Сторона (0;0)–(4;0) горизонтальна', 'Четвёртая вершина сдвинута на (5 − 4; 3) от (0; 0): (1; 3).', '(1; 3).')],
 [Q('Абсцисса — это', 'The abscissa is', ('координата x', 'the x-coordinate'), ('координата y', 'the y-coordinate'), ('расстояние до начала', 'the distance from the origin'), ('Первая координата.', 'The first coordinate.')),
  Q('Точка (0; 4) лежит', 'The point (0; 4) lies', ('на оси y', 'on the y-axis'), ('на оси x', 'on the x-axis'), ('в первой четверти', 'in quadrant I'), ('x = 0 — ось y.', 'x = 0 is the y-axis.')),
  Q('Четверть с отрицательными x и y', 'The quadrant with negative x and y', 'III', 'II', 'IV', ('(−; −).', '(−; −).')),
  Q('Расстояние от (0; 0) до (3; 4)', 'The distance from (0; 0) to (3; 4)', '5', '7', '12', ('√(9 + 16).', '√(9 + 16).')),
  Q('Середина (2; 4) и (6; 8)', 'The midpoint of (2; 4) and (6; 8)', '(4; 6)', '(8; 12)', '(2; 2)', ('Средние координат.', 'The means of the coordinates.')),
  Q('Образ (3; 5) при отражении в оси y', 'The image of (3; 5) in the y-axis', '(−3; 5)', '(3; −5)', '(−3; −5)', ('Меняется знак x.', 'The sign of x changes.')),
  Q('Образ (2; −1) при симметрии относительно начала', 'The image of (2; −1) under point reflection', '(−2; 1)', '(2; 1)', '(−2; −1)', ('Меняются оба знака.', 'Both signs change.')),
  Q('Сколько четвертей на плоскости?', 'How many quadrants are on the plane?', '4', '2', '8', ('Две оси делят плоскость на четыре части.', 'Two axes divide the plane into four parts.'))],
 src=[('Wikipedia: Cartesian coordinate system', 'https://en.wikipedia.org/wiki/Cartesian_coordinate_system'), ('Wikipedia: Euclidean distance', 'https://en.wikipedia.org/wiki/Euclidean_distance')],
 note=('Расстояния в загадке придуманы для задачи.', 'The distances in the puzzle are made up for the problem.'))
