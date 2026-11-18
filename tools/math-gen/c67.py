# -*- coding: utf-8 -*-
from gen2 import *

GR = "Gr({x0:-7,x1:7,y0:-4,y1:4,L:90,T:10,W:420,H:240})"

m1 = M(('Сложение векторов', 'Adding vectors'),
 [('r', 'ax', 'a: x', 'a: x', -6, 6, 1, 3), ('r', 'ay', 'a: y', 'a: y', -3, 3, 1, 1), ('r', 'bx', 'b: x', 'b: x', -6, 6, 1, 1), ('r', 'by', 'b: y', 'b: y', -3, 3, 1, 2)],
 [('a + b', 'a + b'), ('|a + b|', '|a + b|'), ('|a| + |b| (не меньше)', '|a| + |b| (not smaller)')],
 'Вектор — направленный отрезок: задаётся длиной и направлением. Сумма — диагональ параллелограмма (или «приложить b к концу a»); координаты складываются.', 'A vector is a directed segment: it has a length and a direction. The sum is the diagonal of a parallelogram (or “attach b to the end of a”); coordinates add.', ('Правило параллелограмма', 'The parallelogram rule'),
 r'''const G=''' + GR + r''';const X=G.X,Y=G.Y,sx=v.ax+v.bx,sy=v.ay+v.by;let g=G.grid(1,1)+arrow(X(0),Y(0),X(v.ax),Y(v.ay),COL.a,4)+arrow(X(0),Y(0),X(v.bx),Y(v.by),COL.b,4)+L(X(v.ax),Y(v.ay),X(sx),Y(sy),COL.b,2,0)+L(X(v.bx),Y(v.by),X(sx),Y(sy),COL.a,2,0)+arrow(X(0),Y(0),X(sx),Y(sy),COL.c,5)+TX(X(v.ax)+8,Y(v.ay)-8,"a",COL.a,15,"middle",700)+TX(X(v.bx)+8,Y(v.by)-8,"b",COL.b,15,"middle",700);
 const la=Math.hypot(v.ax,v.ay),lb=Math.hypot(v.bx,v.by),ls=Math.hypot(sx,sy);
 return {svg:g,st:["("+sx+"; "+sy+")",fnum(ls,3),fnum(la+lb,3)],fb:U("Длина суммы не больше суммы длин — неравенство треугольника.","The length of the sum is at most the sum of lengths — the triangle inequality.")}''', '0 0 600 265')

m2 = M(('Умножение на число и длина', 'Scalar multiplication and length'),
 [('r', 'ax', 'a: x', 'a: x', -3, 3, 1, 2), ('r', 'ay', 'a: y', 'a: y', -2, 2, 1, 1), ('r', 'k', 'Число k', 'Number k', -3, 3, 0.5, 2)],
 [('k·a', 'k·a'), ('|a|', '|a|'), ('|k·a| = |k|·|a|', '|k·a| = |k|·|a|')],
 'Умножение на k растягивает вектор в |k| раз; при k &lt; 0 направление меняется на противоположное. Длина: |a| = √(x² + y²).', 'Multiplying by k stretches the vector |k| times; for k &lt; 0 the direction reverses. Length: |a| = √(x² + y²).', ('Вектор a и вектор k·a', 'Vector a and vector k·a'),
 r'''const G=''' + GR + r''';const X=G.X,Y=G.Y,kx=v.k*v.ax,ky=v.k*v.ay;let g=G.grid(1,1)+arrow(X(0),Y(0),X(kx),Y(ky),COL.c,5)+arrow(X(0),Y(0),X(v.ax),Y(v.ay),COL.a,4)+TX(X(v.ax)+8,Y(v.ay)-8,"a",COL.a,15,"middle",700);
 const la=Math.hypot(v.ax,v.ay);
 return {svg:g,st:["("+fnum(kx,1)+"; "+fnum(ky,1)+")",fnum(la,3),fnum(Math.abs(v.k)*la,3)],fb:v.k<0?U("Отрицательное k разворачивает вектор.","A negative k reverses the vector."):v.k===0?U("k = 0 даёт нулевой вектор.","k = 0 gives the zero vector."):U("Положительное k сохраняет направление.","A positive k keeps the direction.")}''', '0 0 600 265')

m3 = M(('Скалярное произведение', 'The dot product'),
 [('r', 'la', '|a|', '|a|', 1, 4, 0.5, 3), ('r', 'aa', 'Угол a, °', 'Angle of a, °', 0, 180, 5, 20), ('r', 'lb', '|b|', '|b|', 1, 4, 0.5, 2), ('r', 'ab', 'Угол b, °', 'Angle of b, °', 0, 180, 5, 110)],
 [('Угол между a и b', 'Angle between a and b'), ('a·b = |a||b|cos φ', 'a·b = |a||b|cos φ'), ('Через координаты xx′ + yy′', 'By coordinates xx′ + yy′')],
 'Скалярное произведение — число: a·b = |a|·|b|·cos φ = x₁x₂ + y₁y₂. Оно равно 0 тогда и только тогда, когда векторы перпендикулярны.', 'The dot product is a number: a·b = |a|·|b|·cos φ = x₁x₂ + y₁y₂. It equals 0 exactly when the vectors are perpendicular.', ('Угол между векторами', 'The angle between vectors'),
 r'''const G=''' + GR + r''';const X=G.X,Y=G.Y,A=deg(v.aa),B=deg(v.ab),ax=v.la*Math.cos(A),ay=v.la*Math.sin(A),bx=v.lb*Math.cos(B),by=v.lb*Math.sin(B);let g=G.grid(1,1)+arrow(X(0),Y(0),X(ax),Y(ay),COL.a,4)+arrow(X(0),Y(0),X(bx),Y(by),COL.b,4)+arcA(X(0),Y(0),30,Math.min(A,B),Math.max(A,B),COL.c,3);
 const phi=Math.abs(v.aa-v.ab),dp=ax*bx+ay*by;
 return {svg:g,st:[fnum(phi,0)+"°",fnum(v.la*v.lb*Math.cos(deg(phi)),3),fnum(dp,3)],fb:Math.abs(dp)<0.01?U("Скалярное произведение равно нулю — векторы перпендикулярны.","The dot product is zero — the vectors are perpendicular."):dp>0?U("Угол острый — произведение положительно.","The angle is acute — the product is positive."):U("Угол тупой — произведение отрицательно.","The angle is obtuse — the product is negative.")}''', '0 0 600 265')

chapter('67', '67-vectors-plane.html', 'IX', ('Векторы на плоскости', 'Vectors in the plane'),
 ('Сложение, умножение на число, координаты, длина, скалярное произведение и угол между векторами.', 'Addition, scalar multiplication, coordinates, length, the dot product and the angle between vectors.'),
 ('Лодка идёт со скоростью 3 км/ч поперёк реки, а течение уносит её вдоль берега со скоростью 4 км/ч. С какой скоростью и в каком направлении она в самом деле движется?', 'A boat moves at 3 km/h across a river while the current carries it along the bank at 4 km/h. At what speed and in what direction does it really move?'),
 ('Разгадка: 5 км/ч под углом ≈ 37° к берегу', 'The answer: 5 km/h at about 37° to the bank'),
 ('Скорости складываются как векторы: итоговый вектор — диагональ прямоугольника 3 × 4, его длина √(9 + 16) = 5 км/ч. Направление: tan φ = 3/4, φ ≈ 37° к берегу. Векторы нужны там, где важно не только «сколько», но и «куда»: скорость, сила, ускорение. (Числа условные.)', 'Velocities add as vectors: the resulting vector is the diagonal of a 3 × 4 rectangle, with length √(9 + 16) = 5 km/h. Direction: tan φ = 3/4, φ ≈ 37° to the bank. Vectors are needed where not only “how much” but also “where to” matters: velocity, force, acceleration. (The numbers are illustrative.)'),
 [S('add', 'Сложение и вычитание', 'Addition and subtraction', ('Вектор a = (x; y) — стрелка с длиной и направлением; равные по длине и направлению векторы считаются равными. <strong>Сумма</strong>: (x₁ + x₂; y₁ + y₂); правило треугольника и параллелограмма. <strong>Разность</strong>: a − b = a + (−b). Всегда |a + b| ≤ |a| + |b|.', 'A vector a = (x; y) is an arrow with a length and a direction; vectors of equal length and direction are equal. <strong>Sum</strong>: (x₁ + x₂; y₁ + y₂); the triangle and parallelogram rules. <strong>Difference</strong>: a − b = a + (−b). Always |a + b| ≤ |a| + |b|.'),
    ('a + b = (x₁ + x₂; y₁ + y₂)', '', 'a + b = (x₁ + x₂; y₁ + y₂)'), m1),
  S('mul', 'Умножение на число и длина', 'Scalar multiplication and length', ('<strong>k·a = (kx; ky)</strong>; параллельные векторы отличаются множителем: b = k·a. <strong>Длина |a| = √(x² + y²)</strong>. Единичный вектор: a/|a|. Середина отрезка AB: (A + B)/2.', '<strong>k·a = (kx; ky)</strong>; parallel vectors differ by a factor: b = k·a. <strong>Length |a| = √(x² + y²)</strong>. The unit vector is a/|a|. The midpoint of AB: (A + B)/2.'),
    ('|a| = √(x² + y²)', '', '|a| = √(x² + y²)'), m2),
  S('dot', 'Скалярное произведение', 'The dot product', ('<strong>a·b = |a|·|b|·cos φ = x₁x₂ + y₁y₂</strong>. Угол между векторами: cos φ = a·b / (|a||b|). Условие перпендикулярности: a·b = 0. Применения: работа силы A = F·s·cos φ, проекции, расстояния.', '<strong>a·b = |a|·|b|·cos φ = x₁x₂ + y₁y₂</strong>. The angle between vectors: cos φ = a·b / (|a||b|). The perpendicularity condition: a·b = 0. Uses: the work of a force A = F·s·cos φ, projections, distances.'),
    ('a·b = x₁x₂ + y₁y₂', '', 'a·b = x₁x₂ + y₁y₂'), m3)],
 [TK(('Сумма', 'Sum'), ('a = (2; 3), b = (−1; 4). Найдите a + b.', 'a = (2; 3), b = (−1; 4). Find a + b.'), '', '(1; 7).', '(1; 7).'),
  TK(('Длина', 'Length'), ('Длина вектора (6; 8).', 'The length of the vector (6; 8).'), '', '√(36 + 64) = 10.', '10.'),
  TK(('Число', 'Scalar'), ('Найдите −2·(1; −3).', 'Find −2·(1; −3).'), '', '(−2; 6).', '(−2; 6).'),
  TK(('Угол', 'Angle'), ('a = (1; 0), b = (1; 1). Найдите угол между ними.', 'a = (1; 0), b = (1; 1). Find the angle between them.'), '', 'cos φ = 1/√2, φ = 45°.', '45°.'),
  TK(('Перпендикулярность', 'Perpendicularity'), ('Перпендикулярны ли (2; 3) и (−3; 2)?', 'Are (2; 3) and (−3; 2) perpendicular?'), '', '−6 + 6 = 0 — да.', ('Да.', 'Yes.'))],
 [Q('(1; 2) + (3; 4) =', '(1; 2) + (3; 4) =', '(4; 6)', '(3; 8)', '(2; 2)', ('Складываем координаты.', 'Add coordinates.')),
  Q('Длина (3; 4)', 'The length of (3; 4)', '5', '7', '12', ('√25.', '√25.')),
  Q('2·(1; −1) =', '2·(1; −1) =', '(2; −2)', '(1; −2)', '(3; 1)', ('Умножаем каждую координату.', 'Multiply each coordinate.')),
  Q('a·b = 0 означает, что векторы', 'a·b = 0 means that the vectors are', ('перпендикулярны', 'perpendicular'), ('параллельны', 'parallel'), ('равны', 'equal'), ('cos 90° = 0.', 'cos 90° = 0.')),
  Q('(1; 2)·(3; 4) =', '(1; 2)·(3; 4) =', '11', '10', '14', ('3 + 8.', '3 + 8.')),
  Q('Скалярное произведение — это', 'The dot product is a', ('число', 'number'), ('вектор', 'vector'), ('угол', 'angle'), ('Результат — скаляр.', 'The result is a scalar.')),
  Q('|a + b| ≤ |a| + |b| называют неравенством', 'The inequality |a + b| ≤ |a| + |b| is called the', ('треугольника', 'triangle inequality'), ('Коши', 'Cauchy'), ('Бернулли', 'Bernoulli'), ('Сторона треугольника не больше суммы двух других.', 'A side of a triangle is at most the sum of the other two.')),
  Q('Скорости лодки и течения складываются как', 'The velocities of a boat and the current add as', ('векторы', 'vectors'), ('числа', 'plain numbers'), ('площади', 'areas'), ('Важны направления.', 'Directions matter.'))],
 src=[('Wikipedia: Euclidean vector', 'https://en.wikipedia.org/wiki/Euclidean_vector'), ('Wikipedia: Dot product', 'https://en.wikipedia.org/wiki/Dot_product'), ('Wikipedia: Parallelogram law', 'https://en.wikipedia.org/wiki/Parallelogram_law')],
 note=('Сюжет с лодкой и числа условные.', 'The boat story and the numbers are illustrative.'))
