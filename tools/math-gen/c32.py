# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Параллелограмм', 'The parallelogram'),
 [('r', 'a', 'Сторона a', 'Side a', 2, 10, 1, 7), ('r', 'b', 'Сторона b', 'Side b', 2, 10, 1, 4), ('r', 'al', 'Угол α, °', 'Angle α, °', 20, 160, 1, 60)],
 [('Периметр', 'Perimeter'), ('Площадь a·b·sin α', 'Area a·b·sin α'), ('Диагонали', 'Diagonals')],
 'Противоположные стороны параллелограмма равны и параллельны, противоположные углы равны, соседние в сумме дают 180°.', 'Opposite sides of a parallelogram are equal and parallel; opposite angles are equal; adjacent angles add to 180°.', ('Параллелограмм по двум сторонам и углу', 'A parallelogram from two sides and an angle'),
 r'''const al=deg(v.al),P0=[[0,0],[v.a,0],[v.a+v.b*Math.cos(al),v.b*Math.sin(al)],[v.b*Math.cos(al),v.b*Math.sin(al)]],P=fitPts(P0,60,15,470,175,0.95);
 let g=poly(P,"#f4dfd8",COL.ink,3)+L(P[0][0],P[0][1],P[2][0],P[2][1],COL.mut,1.5)+L(P[1][0],P[1][1],P[3][0],P[3][1],COL.mut,1.5);
 const d1=Math.sqrt(v.a*v.a+v.b*v.b+2*v.a*v.b*Math.cos(al)),d2=Math.sqrt(v.a*v.a+v.b*v.b-2*v.a*v.b*Math.cos(al));
 g+=TX(P[0][0]+30,P[0][1]-8,v.al+"°",COL.a,14,"start",700)+TX(P[1][0]-6,P[1][1]-8,(180-v.al)+"°",COL.b,14,"end",700);
 return {svg:g,st:[2*(v.a+v.b),fnum(v.a*v.b*Math.sin(al),2),fnum(d1,2)+" и "+fnum(d2,2)],fb:U("При α = 90° получается прямоугольник, у него площадь a·b.","At α = 90° we get a rectangle with area a·b.")}''', '0 0 600 215')

m2 = M(('Виды четырёхугольников', 'Kinds of quadrilaterals'),
 [('s', 'k', 'Фигура', 'Figure', ['параллелограмм', 'прямоугольник', 'ромб', 'квадрат', 'трапеция'], ['parallelogram', 'rectangle', 'rhombus', 'square', 'trapezoid'], 0)],
 [('Параллельные пары сторон', 'Pairs of parallel sides'), ('Равные стороны', 'Equal sides'), ('Прямые углы', 'Right angles')],
 'Квадрат — одновременно прямоугольник и ромб, а те — параллелограммы. Трапеция имеет лишь одну пару параллельных сторон.', 'A square is both a rectangle and a rhombus, and those are parallelograms. A trapezoid has only one pair of parallel sides.', ('Фигура с отмеченными свойствами', 'A figure with its marked properties'),
 r'''const sh=[[[0,0],[6,0],[8,3],[2,3]],[[0,0],[7,0],[7,4],[0,4]],[[0,0],[5,0],[8,4],[3,4]],[[0,0],[5,0],[5,5],[0,5]],[[0,0],[8,0],[6,4],[2,4]]],P=fitPts(sh[v.k],150,15,300,170,0.95);
 const info=[["2","2 пары","нет"],["2","2 пары","4"],["2","4","нет"],["2","4","4"],["1","1 пара","нет"]],ie=[["2","2 pairs","none"],["2","2 pairs","4"],["2","4","none"],["2","4","4"],["1","1 pair","none"]];
 let g=poly(P,"#f4dfd8",COL.ink,3);
 return {svg:g,st:[info[v.k][0],lang==="ru"?info[v.k][1]:ie[v.k][1],lang==="ru"?info[v.k][2]:ie[v.k][2]],fb:[U("Противоположные стороны равны и параллельны.","Opposite sides are equal and parallel."),U("Все углы прямые; диагонали равны.","All angles are right; the diagonals are equal."),U("Все стороны равны; диагонали перпендикулярны и делят углы пополам.","All sides are equal; the diagonals are perpendicular and bisect the angles."),U("Все стороны равны и все углы прямые.","All sides are equal and all angles are right."),U("Две стороны параллельны (основания), две другие нет (боковые).","Two sides are parallel (the bases), the other two are not (the legs).")][v.k]}''', '0 0 600 205')

m3 = M(('Диагонали четырёхугольника', 'Diagonals of a quadrilateral'),
 [('r', 'd1', 'Диагональ d₁', 'Diagonal d₁', 2, 12, 1, 8), ('r', 'd2', 'Диагональ d₂', 'Diagonal d₂', 2, 12, 1, 5), ('r', 'ph', 'Угол между диагоналями, °', 'Angle between diagonals, °', 20, 90, 1, 70)],
 [('Площадь ½·d₁·d₂·sin φ', 'Area ½·d₁·d₂·sin φ'), ('Фигура', 'Figure'), ('Стороны', 'Sides')],
 'Диагонали, делящие друг друга пополам, дают параллелограмм. Если они равны — прямоугольник, если перпендикулярны — ромб.', 'Diagonals bisecting each other give a parallelogram. If equal — a rectangle; if perpendicular — a rhombus.', ('Четырёхугольник по диагоналям', 'A quadrilateral from its diagonals'),
 r'''const f=deg(v.ph),u=[1,0],w=[Math.cos(f),Math.sin(f)],h1=v.d1/2,h2=v.d2/2;const P0=[[h1*u[0],h1*u[1]],[h2*w[0],h2*w[1]],[-h1*u[0],-h1*u[1]],[-h2*w[0],-h2*w[1]]],P=fitPts(P0,100,15,400,180,0.95),O=[(P[0][0]+P[2][0])/2,(P[0][1]+P[2][1])/2];
 let g=poly(P,"#f4dfd8",COL.ink,3)+L(P[0][0],P[0][1],P[2][0],P[2][1],COL.a,2)+L(P[1][0],P[1][1],P[3][0],P[3][1],COL.b,2)+C(O[0],O[1],4,COL.ink);
 const s1=Math.hypot(h1*u[0]-h2*w[0],h1*u[1]-h2*w[1]),s2=Math.hypot(h1*u[0]+h2*w[0],h1*u[1]+h2*w[1]);
 const nm=v.ph===90&&v.d1===v.d2?U("квадрат","square"):v.ph===90?U("ромб","rhombus"):v.d1===v.d2?U("прямоугольник","rectangle"):U("параллелограмм","parallelogram");
 return {svg:g,st:[fnum(0.5*v.d1*v.d2*Math.sin(f),2),nm,fnum(s1,2)+" и "+fnum(s2,2)],fb:U("Площадь через диагонали: половина произведения на синус угла между ними.","Area via diagonals: half the product times the sine of the angle between them.")}''', '0 0 600 215')

chapter('32', '32-quadrilaterals.html', 'V', ('Четырёхугольники', 'Quadrilaterals'),
 ('Параллелограмм и его частные случаи, трапеция и свойства диагоналей.', 'The parallelogram and its special cases, the trapezoid and the properties of diagonals.'),
 ('Раздвижная решётка (например, гармошка на воротах) складывается и раздвигается, но её звенья остаются равными.\n\nКакая фигура получается и что остаётся неизменным, когда решётку сжимают?', 'A sliding lattice (like an accordion gate) folds and unfolds, but its links stay equal.\n\nWhat shape appears and what stays unchanged when the lattice is squeezed?'),
 ('Разгадка: ромб — стороны равны, углы меняются', 'The answer: a rhombus — the sides stay equal, the angles change'),
 ('Все звенья одинаковы, значит каждая ячейка — ромб. Когда решётку сжимают, углы меняются, а длины сторон нет. Ромб — это параллелограмм с равными сторонами. Его диагонали перпендикулярны; при растяжении одна диагональ растёт, а другая уменьшается. При прямых углах ромб превращается в квадрат.', 'All links are identical, so each cell is a rhombus. When the lattice is squeezed the angles change but the side lengths do not. A rhombus is a parallelogram with equal sides. Its diagonals are perpendicular; as it stretches one diagonal grows and the other shrinks. With right angles the rhombus becomes a square.'),
 [S('par', 'Параллелограмм', 'The parallelogram', ('<strong>Параллелограмм</strong> — четырёхугольник, у которого противоположные стороны параллельны. Тогда противоположные стороны и углы равны, диагонали точкой пересечения делятся пополам, соседние углы в сумме 180°. Площадь S = a·b·sin α. Периметр P = 2(a + b).', 'A <strong>parallelogram</strong> is a quadrilateral whose opposite sides are parallel. Then opposite sides and angles are equal, the diagonals bisect each other and adjacent angles sum to 180°. Area S = a·b·sin α. Perimeter P = 2(a + b).'),
    ('S = a·b·sin α', '', 'S = a·b·sin α'), m1),
  S('kinds', 'Прямоугольник, ромб, квадрат, трапеция', 'Rectangle, rhombus, square, trapezoid', ('<strong>Прямоугольник</strong> — параллелограмм с прямыми углами, диагонали равны. <strong>Ромб</strong> — параллелограмм с равными сторонами, диагонали перпендикулярны и делят углы пополам. <strong>Квадрат</strong> — и то и другое. <strong>Трапеция</strong> — две стороны параллельны (основания), две другие — боковые; средняя линия равна полусумме оснований.', 'A <strong>rectangle</strong> is a parallelogram with right angles; its diagonals are equal. A <strong>rhombus</strong> is a parallelogram with equal sides; its diagonals are perpendicular and bisect the angles. A <strong>square</strong> is both. A <strong>trapezoid</strong> has two parallel sides (the bases) and two others (the legs); the midline equals half the sum of the bases.'),
    ('средняя линия = (a + b)/2', 'трапеция', 'trapezoid'), m2),
  S('diag', 'Диагонали', 'Diagonals', ('Если диагонали четырёхугольника делятся пополам точкой пересечения — это параллелограмм. Равные диагонали — прямоугольник, перпендикулярные — ромб, и то и другое — квадрат. Площадь любого выпуклого четырёхугольника: S = ½ d₁ d₂ sin φ.', 'If the diagonals of a quadrilateral bisect each other, it is a parallelogram. Equal diagonals — a rectangle; perpendicular — a rhombus; both — a square. The area of any convex quadrilateral: S = ½ d₁ d₂ sin φ.'),
    ('S = ½ d₁ d₂ sin φ', '', 'S = ½ d₁ d₂ sin φ'), m3)],
 [TK(('Углы', 'Angles'), ('Один угол параллелограмма 70°. Найдите остальные.', 'One angle of a parallelogram is 70°. Find the others.'), '', 'Противоположный 70°, соседние 180° − 70° = 110°.', ('70°, 110°, 70°, 110°.', '70°, 110°, 70°, 110°.')),
  TK(('Периметр', 'Perimeter'), ('Стороны параллелограмма 9 и 5. Периметр?', 'The sides of a parallelogram are 9 and 5. The perimeter?'), '', '2 · (9 + 5) = 28.', '28.'),
  TK(('Ромб', 'Rhombus'), ('Диагонали ромба 6 и 8. Найдите сторону и площадь.', 'The diagonals of a rhombus are 6 and 8. Find the side and the area.'), 'Половины диагоналей 3 и 4', 'Сторона √(9 + 16) = 5. Площадь ½ · 6 · 8 = 24.', ('Сторона 5, площадь 24.', 'Side 5, area 24.')),
  TK(('Трапеция', 'Trapezoid'), ('Основания трапеции 6 и 10. Найдите среднюю линию.', 'The bases of a trapezoid are 6 and 10. Find the midline.'), '', '(6 + 10) : 2 = 8.', '8.'),
  TK(('Квадрат', 'Square'), ('Диагональ квадрата 10. Его площадь?', 'The diagonal of a square is 10. Its area?'), 'S = d²/2', '100 : 2 = 50.', '50.')],
 [Q('У параллелограмма диагонали', 'In a parallelogram the diagonals', ('делятся пополам', 'bisect each other'), ('всегда равны', 'are always equal'), ('всегда перпендикулярны', 'are always perpendicular'), ('Свойство.', 'The property.')),
  Q('Прямоугольник — это', 'A rectangle is', ('параллелограмм с прямым углом', 'a parallelogram with a right angle'), ('любой четырёхугольник', 'any quadrilateral'), ('трапеция', 'a trapezoid'), ('Определение.', 'The definition.')),
  Q('Диагонали ромба', 'The diagonals of a rhombus are', ('перпендикулярны', 'perpendicular'), ('равны', 'equal'), ('параллельны', 'parallel'), ('Свойство ромба.', 'A rhombus property.')),
  Q('Квадрат является', 'A square is', ('и ромбом, и прямоугольником', 'both a rhombus and a rectangle'), ('только ромбом', 'only a rhombus'), ('только трапецией', 'only a trapezoid'), ('Квадрат — частный случай обоих.', 'A square is a special case of both.')),
  Q('Средняя линия трапеции с основаниями 4 и 8', 'The midline of a trapezoid with bases 4 and 8', '6', '12', '4', ('(4 + 8) : 2.', '(4 + 8) : 2.')),
  Q('Сумма углов четырёхугольника', 'The angle sum of a quadrilateral', '360°', '180°', '270°', ('Два треугольника.', 'Two triangles.')),
  Q('Площадь прямоугольника 5 × 3', 'The area of a 5 × 3 rectangle', '15', '8', '16', ('a · b.', 'a · b.')),
  Q('Параллельных пар сторон у трапеции', 'Pairs of parallel sides in a trapezoid', '1', '2', '0', ('Только основания.', 'Only the bases.'))],
 src=[('Wikipedia: Quadrilateral', 'https://en.wikipedia.org/wiki/Quadrilateral'), ('Wikipedia: Parallelogram', 'https://en.wikipedia.org/wiki/Parallelogram')])
