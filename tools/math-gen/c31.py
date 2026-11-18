# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Сумма углов треугольника', 'The angle sum of a triangle'),
 [('r', 'A', 'Угол A, °', 'Angle A, °', 10, 140, 1, 50), ('r', 'B', 'Угол B, °', 'Angle B, °', 10, 140, 1, 60)],
 [('Угол C', 'Angle C'), ('Сумма', 'Sum'), ('Вид треугольника', 'Kind of triangle')],
 'Сумма углов любого треугольника равна 180°. Меняя два угла, вы получаете третий.', 'The angles of any triangle add up to 180°. By changing two angles you get the third.', ('Треугольник по двум углам', 'A triangle from two angles'),
 r'''const A=v.A,B=Math.min(v.B,175-A),C0=180-A-B;const bs=1,k=bs/Math.sin(deg(C0)),b=k*Math.sin(deg(B)),P0=[[0,0],[bs,0],[b*Math.cos(deg(A)),b*Math.sin(deg(A))]];const P=fitPts(P0,70,15,460,190);
 let g=poly(P,"#f4dfd8",COL.ink,3);const nm=["A","B","C"],vals=[A,B,C0];
 P.forEach((p,i)=>{g+=TX(p[0]+(i===1?18:i===0?-16:0),p[1]+(i===2?-12:18),nm[i]+" "+vals[i]+"°",[COL.a,COL.b,COL.c][i],15,"middle",700)});
 return {svg:g,st:[C0+"°",A+"° + "+B+"° + "+C0+"° = 180°",C0>90||A>90||B>90?U("тупоугольный","obtuse"):(C0===90||A===90||B===90)?U("прямоугольный","right"):U("остроугольный","acute")],fb:U("Втроём три угла «собираются» в развёрнутый.","The three angles together make a straight angle.")}''', '0 0 600 230')

m2 = M(('Внешний угол', 'The exterior angle'),
 [('r', 'A', 'Угол A, °', 'Angle A, °', 10, 120, 1, 45), ('r', 'B', 'Угол B, °', 'Angle B, °', 10, 120, 1, 65)],
 [('Внутренний угол B', 'Interior angle B'), ('Внешний угол при B', 'Exterior angle at B'), ('A + C', 'A + C')],
 'Внешний угол равен сумме двух внутренних, не смежных с ним.', 'An exterior angle equals the sum of the two interior angles not adjacent to it.', ('Треугольник с продолжением стороны', 'A triangle with an extended side'),
 r'''const A=v.A,B=Math.min(v.B,175-A),C0=180-A-B;const k=1/Math.sin(deg(C0)),b=k*Math.sin(deg(B));const P=[[0,0],[1,0],[b*Math.cos(deg(A)),b*Math.sin(deg(A))]];const Q=fitPts(P.concat([[1.8,0]]),50,25,420,170);const T=Q.slice(0,3),E=Q[3];
 let g=poly(T,"#f4dfd8",COL.ink,3)+L(T[1][0],T[1][1],E[0],E[1],COL.ink,3);const ex=180-B;

 const ang=Math.atan2(T[1][1]-T[2][1],T[2][0]-T[1][0]);g+=arcA(T[1][0],T[1][1],36,0,ang>0?ang:ang+2*Math.PI,COL.c,6)+TX(T[1][0]+52,T[1][1]-26,(A+C0)+"°",COL.c,15,"start",700)+TX(T[0][0]+34,T[0][1]-8,A+"°",COL.a,14,"start",700)+TX(T[1][0]-30,T[1][1]-8,B+"°",COL.b,14,"end",700);
 return {svg:g,st:[B+"°",(180-B)+"°",A+"° + "+C0+"° = "+(A+C0)+"°"],fb:U("Внешний угол при вершине B = "+(A+C0)+"°: он равен A + C.","The exterior angle at B = "+(A+C0)+"°: it equals A + C.")}''', '0 0 600 230')

m3 = M(('Существует ли треугольник', 'Does the triangle exist'),
 [('r', 'a', 'Сторона a', 'Side a', 1, 12, 1, 4), ('r', 'b', 'Сторона b', 'Side b', 1, 12, 1, 7), ('r', 'c', 'Сторона c', 'Side c', 1, 20, 1, 5)],
 [('Допустимые значения c', 'Allowed values of c'), ('Ваше c', 'Your c'), ('Результат', 'Result')],
 'Третья сторона должна быть больше |a − b| и меньше a + b. Иначе стороны «не сойдутся».', 'The third side must be greater than |a − b| and less than a + b. Otherwise the sides will not meet.', ('Допустимый отрезок для c', 'The allowed interval for c'),
 r'''const lo=Math.abs(v.a-v.b),hi=v.a+v.b,X=t=>40+t/22*520;let g=L(40,100,560,100,COL.ink,3);for(let t=0;t<=20;t+=2)g+=L(X(t),94,X(t),106,COL.ink,1.5)+TX(X(t),124,t,COL.mut,11);
 g+=R(X(lo),88,X(hi)-X(lo),24,"#e1f0e8",COL.c,2,3)+TX((X(lo)+X(hi))/2,60,U("можно","allowed"),COL.c,14,"middle",600)+C(X(v.c),100,9,COL.a)+TX(X(v.c),165,"c = "+v.c,COL.a,15,"middle",700);
 const ok=v.c>lo&&v.c<hi;return {svg:g,st:[lo+" < c < "+hi,"c = "+v.c,ok?U("треугольник есть","a triangle exists"):U("треугольника нет","no triangle")],fb:ok?U("Любую сторону можно сравнить с суммой двух других: все три неравенства верны.","Any side can be compared with the sum of the other two: all three inequalities hold."):U("Нарушено неравенство: сторона не меньше суммы двух других.","An inequality fails: a side is not less than the sum of the other two.")}''', '0 0 600 190')

chapter('31', '31-triangle-angle-sum.html', 'V', ('Сумма углов и неравенство треугольника', 'Angle sum and the triangle inequality'),
 ('Почему сумма углов треугольника всегда 180°, что такое внешний угол и когда из трёх отрезков можно составить треугольник.', 'Why the angles of a triangle always add to 180°, what an exterior angle is and when three segments can form a triangle.'),
 ('Есть три палки длиной 2, 3 и 6 дм.\n\nМожно ли сложить из них треугольник? А из палок 3, 4 и 6?', 'There are three sticks 2, 3 and 6 dm long.\n\nCan they form a triangle? And sticks 3, 4 and 6?'),
 ('Разгадка: 2, 3, 6 — нельзя; 3, 4, 6 — можно', 'The answer: 2, 3, 6 — no; 3, 4, 6 — yes'),
 ('Две короткие палки вместе должны быть длиннее третьей, иначе они не «достанут» друг до друга. 2 + 3 = 5 &lt; 6 — треугольника нет. 3 + 4 = 7 &gt; 6, 3 + 6 &gt; 4, 4 + 6 &gt; 3 — все три неравенства верны, треугольник получится. Кратчайший путь между точками — прямая: обход через третью вершину всегда длиннее.', 'The two shorter sticks together must be longer than the third, otherwise they cannot reach each other. 2 + 3 = 5 &lt; 6 — no triangle. 3 + 4 = 7 &gt; 6, 3 + 6 &gt; 4, 4 + 6 &gt; 3 — all three inequalities hold, so a triangle exists. The shortest path between points is a straight line: a detour via a third vertex is always longer.'),
 [S('sum', 'Сумма углов', 'The angle sum', ('<strong>Сумма углов треугольника равна 180°.</strong> Доказательство: через вершину проводим прямую, параллельную противоположной стороне; два накрест лежащих угла равны двум углам треугольника, а вместе с третьим они образуют развёрнутый угол. Следствия: в треугольнике не более одного прямого или тупого угла; острые углы прямоугольного треугольника в сумме 90°.', '<strong>The angle sum of a triangle is 180°.</strong> Proof: through a vertex draw a line parallel to the opposite side; two alternate angles equal two angles of the triangle and together with the third they form a straight angle. Consequences: a triangle has at most one right or obtuse angle; the acute angles of a right triangle sum to 90°.'),
    ('∠A + ∠B + ∠C = 180°', '', '∠A + ∠B + ∠C = 180°'), m1),
  S('ext', 'Внешний угол', 'The exterior angle', ('<strong>Внешний угол</strong> образуется продолжением стороны: он смежен с внутренним углом и поэтому равен 180° минус внутренний. Отсюда: внешний угол равен сумме двух внутренних, не смежных с ним. Сумма внешних углов треугольника (по одному при вершине) равна 360°.', 'An <strong>exterior angle</strong> is formed by extending a side: it is adjacent to the interior angle and so equals 180° minus it. Hence an exterior angle equals the sum of the two interior angles not adjacent to it. The exterior angles of a triangle (one at each vertex) sum to 360°.'),
    ('внешний = A + B', '', 'exterior = A + B'), m2),
  S('ineq', 'Неравенство треугольника', 'The triangle inequality', ('В любом треугольнике каждая сторона меньше суммы двух других и больше их разности: |a − b| &lt; c &lt; a + b. Против большей стороны лежит больший угол. Эти условия нужны, чтобы треугольник существовал, и используются в навигации и строительстве.', 'In any triangle each side is less than the sum of the other two and greater than their difference: |a − b| &lt; c &lt; a + b. The greater angle lies opposite the greater side. These conditions are needed for a triangle to exist and are used in navigation and building.'),
    ('|a − b| < c < a + b', '', '|a − b| < c < a + b'), m3)],
 [TK(('Третий угол', 'The third angle'), ('Два угла треугольника 47° и 68°. Найдите третий.', 'Two angles of a triangle are 47° and 68°. Find the third.'), '', '180° − 47° − 68° = 65°.', '65°.'),
  TK(('Прямоугольный', 'Right triangle'), ('Один острый угол прямоугольного треугольника 35°. Найдите другой.', 'One acute angle of a right triangle is 35°. Find the other.'), '', '90° − 35° = 55°.', '55°.'),
  TK(('Внешний угол', 'Exterior angle'), ('Углы треугольника при A и B — 40° и 70°. Найдите внешний угол при C.', 'The angles of a triangle at A and B are 40° and 70°. Find the exterior angle at C.'), '', '40° + 70° = 110°.', '110°.'),
  TK(('Существует ли', 'Does it exist'), ('Могут ли стороны быть 5, 5 и 10?', 'Can the sides be 5, 5 and 10?'), '5 + 5 = 10', 'Сумма равна третьей, а должна быть больше. Нет, получится отрезок.', ('Нет.', 'No.')),
  TK(('Какое c', 'Which c'), ('Две стороны 6 и 9. В каких пределах третья?', 'Two sides are 6 and 9. What are the limits of the third?'), '9 − 6 и 9 + 6', '3 &lt; c &lt; 15.', '3 &lt; c &lt; 15.')],
 [Q('Сумма углов треугольника', 'The angle sum of a triangle', '180°', '360°', '90°', ('Теорема.', 'The theorem.')),
  Q('Углы 50° и 60°. Третий', 'Angles 50° and 60°. The third', '70°', '80°', '110°', ('180° − 110°.', '180° − 110°.')),
  Q('Сколько тупых углов может быть в треугольнике?', 'How many obtuse angles can a triangle have?', ('не более одного', 'at most one'), ('два', 'two'), ('три', 'three'), ('Иначе сумма больше 180°.', 'Otherwise the sum exceeds 180°.')),
  Q('Внешний угол равен', 'An exterior angle equals', ('сумме двух несмежных внутренних', 'the sum of the two non-adjacent interior angles'), ('третьему углу', 'the third angle'), ('180° + внутренний', '180° + the interior'), ('Теорема о внешнем угле.', 'The exterior angle theorem.')),
  Q('Стороны 3, 4, 9', 'Sides 3, 4, 9', ('не образуют треугольник', 'do not form a triangle'), ('образуют', 'form a triangle'), ('образуют прямоугольный', 'form a right triangle'), ('3 + 4 &lt; 9.', '3 + 4 &lt; 9.')),
  Q('Против большей стороны лежит', 'Opposite the greater side lies', ('больший угол', 'the greater angle'), ('меньший угол', 'the smaller angle'), ('прямой угол', 'a right angle'), ('Соответствие.', 'The correspondence.')),
  Q('Острые углы прямоугольного треугольника в сумме', 'The acute angles of a right triangle sum to', '90°', '180°', '45°', ('180° − 90°.', '180° − 90°.')),
  Q('Сумма внешних углов (по одному при вершине)', 'The sum of exterior angles (one per vertex)', '360°', '180°', '540°', ('Каждый = 180° − внутренний.', 'Each = 180° − interior.'))],
 src=[('Wikipedia: Triangle', 'https://en.wikipedia.org/wiki/Triangle'), ('Wikipedia: Triangle inequality', 'https://en.wikipedia.org/wiki/Triangle_inequality')])
