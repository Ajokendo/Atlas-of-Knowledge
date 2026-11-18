# -*- coding: utf-8 -*-
from gen2 import *

AX = r'''function axes3(P,len){let g="";[[[len,0,0],"x"],[[0,len,0],"y"],[[0,0,len],"z"]].forEach(a=>{const o=P(0,0,0),e=P(...a[0]);g+=arrow(o[0],o[1],e[0],e[1],COL.mut,2)+TX(e[0]+10,e[1]-6,a[1],COL.ink,15,"middle",700)});return g}
'''

m1 = M(('Координаты точки в пространстве', 'Coordinates of a point in space'),
 [('r', 'x', 'x', 'x', -3, 3, 1, 2), ('r', 'y', 'y', 'y', -3, 3, 1, 3), ('r', 'z', 'z', 'z', -3, 3, 1, 2), ('r', 'yaw', 'Поворот', 'Rotation', -1, 1, 0.1, 0.5)],
 [('Точка M', 'Point M'), ('Расстояние OM', 'Distance OM'), ('Проекция на плоскость xy', 'Projection on the xy-plane')],
 'Положение точки в пространстве задают тремя числами (x; y; z). Расстояние от начала координат: OM = √(x² + y² + z²).', 'The position of a point in space is given by three numbers (x; y; z). The distance from the origin: OM = √(x² + y² + z²).', ('Прямоугольная система координат', 'A rectangular coordinate system'),
 AX + r'''const P=P3(v.yaw,0.45,48,300,150);let g=axes3(P,3.6);const o=P(0,0,0),m=P(v.x,v.y,v.z),a=P(v.x,v.y,0),bx=P(v.x,0,0),by=P(0,v.y,0);g+=L(o[0],o[1],bx[0],bx[1],COL.a,2,0)+L(bx[0],bx[1],a[0],a[1],COL.a,2)+L(o[0],o[1],by[0],by[1],COL.a,2,0)+L(by[0],by[1],a[0],a[1],COL.a,2)+L(a[0],a[1],m[0],m[1],COL.b,3)+L(o[0],o[1],m[0],m[1],COL.c,3)+C(m[0],m[1],6,COL.b)+TX(m[0]+16,m[1]-8,"M",COL.ink,15,"middle",700);
 return {svg:g,st:["("+v.x+"; "+v.y+"; "+v.z+")",fnum(Math.sqrt(v.x*v.x+v.y*v.y+v.z*v.z),3),"("+v.x+"; "+v.y+"; 0)"],fb:U("Три координаты — три шага вдоль осей: так находят точку.","Three coordinates — three steps along the axes: this is how a point is found.")}''', '0 0 600 280')

m2 = M(('Расстояние между точками', 'Distance between two points'),
 [('r', 'x1', 'A: x', 'A: x', -3, 3, 1, 0), ('r', 'y1', 'A: y', 'A: y', -3, 3, 1, 0), ('r', 'z1', 'A: z', 'A: z', -3, 3, 1, 0), ('r', 'x2', 'B: x', 'B: x', -3, 3, 1, 2), ('r', 'y2', 'B: y', 'B: y', -3, 3, 1, 2), ('r', 'z2', 'B: z', 'B: z', -3, 3, 1, 1)],
 [('Вектор AB', 'Vector AB'), ('|AB|', '|AB|'), ('Середина AB', 'Midpoint of AB')],
 'Вектор AB = (x₂ − x₁; y₂ − y₁; z₂ − z₁), длина |AB| = √(Δx² + Δy² + Δz²) — теорема Пифагора дважды. Середина — полусумма координат.', 'The vector AB = (x₂ − x₁; y₂ − y₁; z₂ − z₁), length |AB| = √(Δx² + Δy² + Δz²) — the Pythagorean theorem twice. The midpoint is the half-sum of coordinates.', ('Отрезок AB в пространстве', 'The segment AB in space'),
 AX + r'''const P=P3(0.5,0.45,48,300,150);let g=axes3(P,3.6);const A=P(v.x1,v.y1,v.z1),B=P(v.x2,v.y2,v.z2),Cc=P(v.x2,v.y2,v.z1);g+=L(A[0],A[1],Cc[0],Cc[1],COL.mut,1.5,0)+L(Cc[0],Cc[1],B[0],B[1],COL.mut,1.5)+L(A[0],A[1],B[0],B[1],COL.b,4)+C(A[0],A[1],6,COL.a)+C(B[0],B[1],6,COL.c)+TX(A[0]-12,A[1]-8,"A",COL.ink,15,"middle",700)+TX(B[0]+12,B[1]-8,"B",COL.ink,15,"middle",700);
 const d=[v.x2-v.x1,v.y2-v.y1,v.z2-v.z1];
 return {svg:g,st:["("+d.join("; ")+")",fnum(len3(d),3),"("+fnum((v.x1+v.x2)/2,1)+"; "+fnum((v.y1+v.y2)/2,1)+"; "+fnum((v.z1+v.z2)/2,1)+")"],fb:U("|AB|² = "+d.map(t=>t*t).join(" + ")+" = "+(d[0]*d[0]+d[1]*d[1]+d[2]*d[2])+".","|AB|² = "+d.map(t=>t*t).join(" + ")+" = "+(d[0]*d[0]+d[1]*d[1]+d[2]*d[2])+".")}''', '0 0 600 280')

m3 = M(('Угол между векторами в пространстве', 'The angle between vectors in space'),
 [('r', 'bx', 'b: x', 'b: x', -3, 3, 1, 2), ('r', 'by', 'b: y', 'b: y', -3, 3, 1, 0), ('r', 'bz', 'b: z', 'b: z', -3, 3, 1, 1)],
 [('a·b (a = (1; 2; 2))', 'a·b (a = (1; 2; 2))'), ('|a|, |b|', '|a|, |b|'), ('Угол φ', 'Angle φ')],
 'Скалярное произведение в пространстве: a·b = x₁x₂ + y₁y₂ + z₁z₂, угол: cos φ = a·b / (|a||b|). Нулевое произведение — перпендикулярность.', 'The dot product in space: a·b = x₁x₂ + y₁y₂ + z₁z₂, the angle: cos φ = a·b / (|a||b|). A zero product means perpendicular.', ('Два вектора из начала координат', 'Two vectors from the origin'),
 AX + r'''const P=P3(0.5,0.45,48,300,150);let g=axes3(P,3.6);const o=P(0,0,0),a=P(1,2,2),b=P(v.bx,v.by,v.bz);g+=arrow(o[0],o[1],a[0],a[1],COL.a,4)+arrow(o[0],o[1],b[0],b[1],COL.b,4)+TX(a[0]+10,a[1]-8,"a",COL.a,15,"middle",700)+TX(b[0]+10,b[1]-8,"b",COL.b,15,"middle",700);
 const av=[1,2,2],bv=[v.bx,v.by,v.bz],dp=dot3(av,bv),lb=len3(bv),ph=lb===0?null:Math.acos(clamp(dp/(3*lb),-1,1))*180/Math.PI;
 return {svg:g,st:[dp,"3; "+fnum(lb,3),ph===null?U("нет значения","has no value"):fnum(ph,1)+"°"],fb:lb===0?U("Нулевой вектор не имеет направления — угла нет.","The zero vector has no direction — no angle."):dp===0?U("a·b = 0 — векторы перпендикулярны.","a·b = 0 — the vectors are perpendicular."):U("Знак a·b подсказывает вид угла: плюс — острый, минус — тупой.","The sign of a·b shows the kind of angle: plus — acute, minus — obtuse.")}''', '0 0 600 280')

chapter('68', '68-vectors-space.html', 'IX', ('Векторы и координаты в пространстве', 'Vectors and coordinates in space'),
 ('Три координаты, расстояние между точками, длина и угол между векторами в пространстве.', 'Three coordinates, the distance between points, and the length and angle between vectors in space.'),
 ('Дрон взлетел из точки (0; 0; 0) на 30 м на восток, 40 м на север и 120 м вверх. На каком расстоянии по прямой он оказался от места старта?', 'A drone took off from the point (0; 0; 0) and moved 30 m east, 40 m north and 120 m up. How far in a straight line is it from the start?'),
 ('Разгадка: 130 м', 'The answer: 130 m'),
 ('По горизонтали дрон сместился на √(30² + 40²) = 50 м, потом поднялся на 120 м: √(50² + 120²) = 130 м. Это та же формула расстояния √(x² + y² + z²) — теорема Пифагора, применённая дважды. (Числа подобраны так, чтобы корни получились целыми; сюжет условный.)', 'Horizontally the drone moved √(30² + 40²) = 50 m, then rose 120 m: √(50² + 120²) = 130 m. This is the same distance formula √(x² + y² + z²) — the Pythagorean theorem applied twice. (The numbers are chosen so that the roots are integers; the story is illustrative.)'),
 [S('coord', 'Координаты в пространстве', 'Coordinates in space', ('Три взаимно перпендикулярные оси x, y, z задают систему координат. Точка M(x; y; z). Расстояние от начала: <strong>OM = √(x² + y² + z²)</strong>. Координатные плоскости: xy (z = 0), xz (y = 0), yz (x = 0).', 'Three mutually perpendicular axes x, y, z define a coordinate system. A point M(x; y; z). The distance from the origin: <strong>OM = √(x² + y² + z²)</strong>. Coordinate planes: xy (z = 0), xz (y = 0), yz (x = 0).'),
    ('OM = √(x² + y² + z²)', '', 'OM = √(x² + y² + z²)'), m1),
  S('dist', 'Вектор и расстояние', 'Vector and distance', ('Вектор AB = (x₂ − x₁; y₂ − y₁; z₂ − z₁). <strong>|AB| = √((x₂ − x₁)² + (y₂ − y₁)² + (z₂ − z₁)²)</strong>. Середина отрезка: ((x₁ + x₂)/2; (y₁ + y₂)/2; (z₁ + z₂)/2). Сложение векторов и умножение на число — покоординатно, как на плоскости.', 'The vector AB = (x₂ − x₁; y₂ − y₁; z₂ − z₁). <strong>|AB| = √((x₂ − x₁)² + (y₂ − y₁)² + (z₂ − z₁)²)</strong>. The midpoint of a segment: ((x₁ + x₂)/2; (y₁ + y₂)/2; (z₁ + z₂)/2). Addition of vectors and multiplication by a number are coordinatewise, as in the plane.'),
    ('|AB| = √(Δx² + Δy² + Δz²)', '', '|AB| = √(Δx² + Δy² + Δz²)'), m2),
  S('ang', 'Скалярное произведение', 'The dot product', ('<strong>a·b = x₁x₂ + y₁y₂ + z₁z₂ = |a||b| cos φ</strong>. Отсюда cos φ = a·b / (|a||b|). Векторы перпендикулярны, когда a·b = 0. Так находят углы в многогранниках: введите координаты вершин и сосчитайте.', '<strong>a·b = x₁x₂ + y₁y₂ + z₁z₂ = |a||b| cos φ</strong>. Hence cos φ = a·b / (|a||b|). Vectors are perpendicular when a·b = 0. This is how angles in polyhedra are found: introduce coordinates of the vertices and compute.'),
    ('cos φ = a·b / (|a||b|)', '', 'cos φ = a·b / (|a||b|)'), m3)],
 [TK(('Расстояние', 'Distance'), ('Расстояние от O до M(2; 3; 6).', 'The distance from O to M(2; 3; 6).'), '', '√(4 + 9 + 36) = 7.', '7.'),
  TK(('Вектор', 'Vector'), ('A(1; 2; 3), B(4; 6; 3). Найдите AB и |AB|.', 'A(1; 2; 3), B(4; 6; 3). Find AB and |AB|.'), '', 'AB = (3; 4; 0); |AB| = 5.', 'AB = (3; 4; 0); |AB| = 5.'),
  TK(('Середина', 'Midpoint'), ('Середина A(2; 0; 4) и B(4; 6; 0).', 'The midpoint of A(2; 0; 4) and B(4; 6; 0).'), '', '(3; 3; 2).', '(3; 3; 2).'),
  TK(('Скалярное', 'Dot product'), ('a = (1; 2; 2), b = (2; 0; −1). Найдите a·b.', 'a = (1; 2; 2), b = (2; 0; −1). Find a·b.'), '', '2 + 0 − 2 = 0 — перпендикулярны.', ('0, перпендикулярны.', '0, perpendicular.')),
  TK(('Угол', 'Angle'), ('Угол между (1; 0; 0) и (1; 1; 0).', 'The angle between (1; 0; 0) and (1; 1; 0).'), '', 'cos φ = 1/√2, φ = 45°.', '45°.')],
 [Q('Сколько чисел задают точку в пространстве?', 'How many numbers specify a point in space?', '3', '2', '4', ('x, y, z.', 'x, y, z.')),
  Q('Расстояние от O до (1; 2; 2)', 'The distance from O to (1; 2; 2)', '3', '5', '9', ('√9.', '√9.')),
  Q('Середина отрезка (0; 0; 0) — (2; 4; 6)', 'The midpoint of (0; 0; 0)–(2; 4; 6)', '(1; 2; 3)', '(2; 4; 6)', '(0; 0; 0)', ('Полусумма.', 'The half-sum.')),
  Q('a·b = 0 для ненулевых векторов — это', 'a·b = 0 for non-zero vectors means they are', ('перпендикулярность', 'perpendicular'), ('параллельность', 'parallel'), ('равенство', 'equal'), ('cos 90° = 0.', 'cos 90° = 0.')),
  Q('(1; 2; 3)·(1; 0; 1) =', '(1; 2; 3)·(1; 0; 1) =', '4', '5', '6', ('1 + 0 + 3.', '1 + 0 + 3.')),
  Q('Координатная плоскость xy задаётся уравнением', 'The coordinate plane xy is given by', 'z = 0', 'x = 0', 'y = 0', ('Все точки с z = 0.', 'All points with z = 0.')),
  Q('Вектор AB для A(1; 1; 1), B(3; 2; 1)', 'The vector AB for A(1; 1; 1), B(3; 2; 1)', '(2; 1; 0)', '(4; 3; 2)', '(−2; −1; 0)', ('B − A.', 'B − A.')),
  Q('Длина (2; 3; 6)', 'The length of (2; 3; 6)', '7', '11', '5', ('√49.', '√49.'))],
 src=[('Wikipedia: Three-dimensional space', 'https://en.wikipedia.org/wiki/Three-dimensional_space'), ('Wikipedia: Cartesian coordinate system', 'https://en.wikipedia.org/wiki/Cartesian_coordinate_system'), ('Wikipedia: Euclidean distance', 'https://en.wikipedia.org/wiki/Euclidean_distance')],
 note=('Сюжет с дроном и числа условные.', 'The drone story and numbers are illustrative.'))
