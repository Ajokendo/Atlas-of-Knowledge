# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Прямая и парабола', 'A line and a parabola'),
 [('r', 'k', 'Наклон прямой', 'Slope of the line', -4, 4, 1, 1), ('r', 'b', 'Сдвиг прямой', 'Intercept of the line', -8, 8, 1, 2)],
 [('Система', 'The system'), ('Уравнение для x', 'Equation for x'), ('Решения', 'Solutions')],
 'Подставляем y = kx + b в y = x²: получаем x² − kx − b = 0. Число решений — по дискриминанту.', 'Substituting y = kx + b into y = x² gives x² − kx − b = 0. The number of solutions follows the discriminant.', ('Парабола и прямая', 'A parabola and a line'),
 r'''const D=v.k*v.k+4*v.b,G=Gr({x0:-6,x1:6,y0:-4,y1:12,L:100,T:10,W:400,H:210});let g=G.grid(2,2)+G.fn(x=>x*x,COL.b,3.5)+G.fn(x=>v.k*x+v.b,COL.a,3);let sol=[];if(D>=0){const xs=D===0?[v.k/2]:[(v.k-Math.sqrt(D))/2,(v.k+Math.sqrt(D))/2];xs.forEach(x=>{g+=G.pt(x,x*x,COL.c,8);sol.push("("+fnum(x,2)+"; "+fnum(x*x,2)+")")})}
 return {svg:g,st:["y = x²,  y = "+v.k+"x "+(v.b<0?"− "+(-v.b):"+ "+v.b),"x² − "+v.k+"x "+(-v.b<0?"− "+v.b:"+ "+(-v.b))+" = 0, D = "+D,sol.length?sol.join(";  "):U("решений нет","no solutions")],fb:D>0?U("D > 0: две общие точки.","D > 0: two common points."):D===0?U("D = 0: прямая касается параболы.","D = 0: the line touches the parabola."):U("D < 0: прямая не пересекает параболу.","D < 0: the line does not meet the parabola.")}''', '0 0 600 250')

m2 = M(('Прямая и окружность', 'A line and a circle'),
 [('r', 'r', 'Радиус', 'Radius', 2, 7, 1, 5), ('r', 'k', 'Наклон прямой', 'Slope', -3, 3, 1, 1), ('r', 'b', 'Сдвиг прямой', 'Intercept', -9, 9, 1, 1)],
 [('Система', 'The system'), ('Расстояние от центра до прямой', 'Distance from the centre to the line'), ('Решения', 'Solutions')],
 'Окружность x² + y² = r² и прямая y = kx + b: сравним расстояние от центра до прямой с радиусом.', 'The circle x² + y² = r² and the line y = kx + b: compare the distance from the centre to the line with the radius.', ('Окружность и прямая', 'A circle and a line'),
 r'''const d=Math.abs(v.b)/Math.sqrt(1+v.k*v.k),G=Gr({x0:-8,x1:8,y0:-8,y1:8,L:100,T:10,W:400,H:210});let g=G.grid(2,2)+'<ellipse cx="'+G.X(0)+'" cy="'+G.Y(0)+'" rx="'+(G.X(v.r)-G.X(0))+'" ry="'+(G.Y(0)-G.Y(v.r))+'" fill="none" stroke="'+COL.b+'" stroke-width="3.5"/>'+G.fn(x=>v.k*x+v.b,COL.a,3);
 const A=1+v.k*v.k,Bq=2*v.k*v.b,Cq=v.b*v.b-v.r*v.r,D=Bq*Bq-4*A*Cq,sol=[];if(D>=-1e-9){const ws=Math.abs(D)<1e-9?[-Bq/(2*A)]:[(-Bq-Math.sqrt(D))/(2*A),(-Bq+Math.sqrt(D))/(2*A)];ws.forEach(x=>{g+=G.pt(x,v.k*x+v.b,COL.c,8);sol.push("("+fnum(x,2)+"; "+fnum(v.k*x+v.b,2)+")")})}
 return {svg:g,st:["x² + y² = "+v.r*v.r+";  y = "+v.k+"x "+(v.b<0?"− "+(-v.b):"+ "+v.b),fnum(d,2)+" "+(d<v.r?"< ":d>v.r?"> ":"= ")+v.r,sol.length?sol.join(";  "):U("решений нет","no solutions")],fb:d<v.r?U("Расстояние меньше радиуса — прямая — секущая.","The distance is less than the radius — a secant line."):d>v.r?U("Расстояние больше радиуса — прямая не пересекает окружность.","The distance exceeds the radius — the line misses the circle."):U("Расстояние равно радиусу — касательная.","The distance equals the radius — a tangent.")}''', '0 0 600 250')

m3 = M(('Сумма и произведение', 'Sum and product'),
 [('r', 's', 'Сумма x + y', 'Sum x + y', -10, 10, 1, 7), ('r', 'p', 'Произведение xy', 'Product xy', -20, 25, 1, 12)],
 [('Система', 'The system'), ('Квадратное уравнение', 'The quadratic equation'), ('Решения', 'Solutions')],
 'Если x + y = s и xy = p, то x и y — корни уравнения t² − st + p = 0 (теорема Виета).', 'If x + y = s and xy = p then x and y are the roots of t² − st + p = 0 (Vieta’s theorem).', ('Парабола t² − st + p', 'The parabola t² − st + p'),
 r'''const D=v.s*v.s-4*v.p,G=Gr({x0:-8,x1:12,y0:-15,y1:30,L:80,T:10,W:460,H:210});let g=G.grid(2,10)+G.fn(t=>t*t-v.s*t+v.p,COL.a,3.5);let st3;if(D>=0){const r1=(v.s-Math.sqrt(D))/2,r2=(v.s+Math.sqrt(D))/2;g+=G.pt(r1,0,COL.c,7)+G.pt(r2,0,COL.c,7);st3=D===0?"("+fnum(r1,2)+"; "+fnum(r1,2)+")":"("+fnum(r1,2)+"; "+fnum(r2,2)+") "+U("и","and")+" ("+fnum(r2,2)+"; "+fnum(r1,2)+")"}else st3=U("действительных решений нет","no real solutions");
 return {svg:g,st:["x + y = "+v.s+",  xy = "+v.p,"t² − "+v.s+"t "+(v.p<0?"− "+(-v.p):"+ "+v.p)+" = 0,  D = "+D,st3],fb:D<0?U("D < 0: такого сочетания суммы и произведения не бывает.","D < 0: such a combination of sum and product does not occur."):U("Пара (x; y) и пара (y; x) — разные решения системы.","The pair (x; y) and the pair (y; x) are different solutions of the system.")}''', '0 0 600 250')

chapter('46', '46-nonlinear-systems.html', 'VI', ('Системы нелинейных уравнений', 'Nonlinear systems'),
 ('Как решать системы, где одно уравнение нелинейное: подстановкой, через дискриминант, по теореме Виета.', 'How to solve systems where an equation is nonlinear: by substitution, via the discriminant, by Vieta’s theorem.'),
 ('Сумма двух чисел равна 7, а произведение 12.\n\nНайдите эти числа.', 'The sum of two numbers is 7 and the product is 12.\n\nFind the numbers.'),
 ('Разгадка: 3 и 4', 'The answer: 3 and 4'),
 ('Числа x и y — корни уравнения t² − 7t + 12 = 0 (по теореме Виета). D = 49 − 48 = 1, t = (7 ± 1)/2: 3 и 4. Проверка: 3 + 4 = 7, 3 · 4 = 12. Система из линейного и нелинейного уравнений сводится к квадратному уравнению подстановкой одного неизвестного в другое.', 'The numbers x and y are the roots of t² − 7t + 12 = 0 (by Vieta’s theorem). D = 49 − 48 = 1, t = (7 ± 1)/2: 3 and 4. Check: 3 + 4 = 7, 3 · 4 = 12. A system of a linear and a nonlinear equation reduces to a quadratic equation by substituting one unknown into the other.'),
 [S('par', 'Прямая и парабола', 'A line and a parabola', ('Система y = x², y = kx + b: подставляем y и получаем квадратное уравнение x² − kx − b = 0. D &gt; 0 — две общие точки, D = 0 — касание, D &lt; 0 — нет общих точек. Найденные x подставляют в одно из уравнений, чтобы найти y.', 'The system y = x², y = kx + b: substituting y gives the quadratic x² − kx − b = 0. D &gt; 0 — two common points, D = 0 — tangency, D &lt; 0 — none. The found x are substituted into one equation to find y.'),
    ('x² = kx + b', '', 'x² = kx + b'), m1),
  S('circ', 'Прямая и окружность', 'A line and a circle', ('Система x² + y² = r², y = kx + b: подстановка даёт (1 + k²)x² + 2kbx + b² − r² = 0. Расстояние от начала координат до прямой d = |b|/√(1 + k²): d &lt; r — две точки, d = r — касание, d &gt; r — нет точек.', 'The system x² + y² = r², y = kx + b: substitution gives (1 + k²)x² + 2kbx + b² − r² = 0. The distance from the origin to the line d = |b|/√(1 + k²): d &lt; r — two points, d = r — tangent, d &gt; r — none.'),
    ('d = |b|/√(1 + k²)', '', 'd = |b|/√(1 + k²)'), m2),
  S('vi', 'Метод Виета для суммы и произведения', 'Vieta’s method for sum and product', ('Система x + y = s, xy = p равносильна тому, что x и y — корни t² − st + p = 0. Получаем две пары: (x₁; x₂) и (x₂; x₁). Если D &lt; 0, решений нет. Такой приём называют <em>симметрическим</em>.', 'The system x + y = s, xy = p means that x and y are the roots of t² − st + p = 0. This gives two pairs: (x₁; x₂) and (x₂; x₁). If D &lt; 0 there are no solutions. This trick is called <em>symmetric</em>.'),
    ('t² − st + p = 0', '', 't² − st + p = 0'), m3)],
 [TK(('Подстановка', 'Substitution'), ('Решите: y = x + 2, y = x².', 'Solve: y = x + 2, y = x².'), 'x² = x + 2', 'x² − x − 2 = 0, x = 2 или −1. Решения (2; 4) и (−1; 1).', ('(2; 4) и (−1; 1).', '(2; 4) and (−1; 1).')),
  TK(('Окружность и прямая', 'Circle and line'), ('Решите: x² + y² = 25, y = x − 1.', 'Solve: x² + y² = 25, y = x − 1.'), '', 'x² + (x − 1)² = 25 → x² − x − 12 = 0, x = 4 или −3. (4; 3) и (−3; −4).', ('(4; 3) и (−3; −4).', '(4; 3) and (−3; −4).')),
  TK(('Сумма и произведение', 'Sum and product'), ('x + y = 5, xy = 6.', 'x + y = 5, xy = 6.'), 't² − 5t + 6 = 0', 't = 2 и 3: (2; 3) и (3; 2).', ('(2; 3) и (3; 2).', '(2; 3) and (3; 2).')),
  TK(('Касание', 'Tangency'), ('При каком b прямая y = 2x + b касается y = x²?', 'For which b does the line y = 2x + b touch y = x²?'), 'x² − 2x − b = 0', 'D = 4 + 4b = 0, b = −1.', 'b = −1.'),
  TK(('Нет решений', 'No solutions'), ('Есть ли решения у x + y = 2, xy = 5?', 'Does x + y = 2, xy = 5 have solutions?'), 't² − 2t + 5', 'D = 4 − 20 &lt; 0 — нет.', ('Нет.', 'No.'))],
 [Q('Решение системы нелинейных уравнений ищут', 'A nonlinear system is often solved by', ('подстановкой', 'substitution'), ('угадыванием', 'guessing'), ('только графиком', 'only graphs'), ('Сводят к одному уравнению.', 'Reduce to one equation.')),
  Q('Прямая касается параболы, если D', 'A line touches a parabola when D', '= 0', '> 0', '< 0', ('Один общий корень.', 'One common root.')),
  Q('x + y = 4, xy = 4. Решение', 'x + y = 4, xy = 4. The solution', '(2; 2)', '(1; 3)', '(4; 0)', ('t² − 4t + 4 = 0.', 't² − 4t + 4 = 0.')),
  Q('Окружность x² + y² = 1 и прямая y = 2: общих точек', 'The circle x² + y² = 1 and the line y = 2: common points', '0', '1', '2', ('Расстояние 2 > 1.', 'Distance 2 > 1.')),
  Q('Сколько решений у y = x², y = −1?', 'How many solutions has y = x², y = −1?', '0', '1', '2', ('x² не бывает отрицательным.', 'x² is never negative.')),
  Q('Пары (2; 3) и (3; 2) для x + y = 5, xy = 6 —', 'The pairs (2; 3) and (3; 2) for x + y = 5, xy = 6 are', ('два решения', 'two solutions'), ('одно решение', 'one solution'), ('не решения', 'not solutions'), ('Порядок важен.', 'The order matters.')),
  Q('Проверка решения системы обязательна для', 'Checking a system’s solution is needed in', ('обоих уравнений', 'both equations'), ('первого', 'the first only'), ('не нужна', 'it is not needed'), ('Пара должна подходить обоим.', 'The pair must satisfy both.')),
  Q('x² + y² = 4 — это', 'x² + y² = 4 is', ('окружность радиуса 2', 'a circle of radius 2'), ('прямая', 'a line'), ('парабола', 'a parabola'), ('r² = 4.', 'r² = 4.'))],
 src=[('Wikipedia: System of polynomial equations', 'https://en.wikipedia.org/wiki/System_of_polynomial_equations'), ('Wikipedia: Vieta’s formulas', 'https://en.wikipedia.org/wiki/Vieta%27s_formulas')])
