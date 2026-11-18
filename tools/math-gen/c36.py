# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Теорема Пифагора: квадраты на сторонах', 'The Pythagorean theorem: squares on the sides'),
 [('r', 'a', 'Катет a', 'Leg a', 1, 8, 1, 3), ('r', 'b', 'Катет b', 'Leg b', 1, 8, 1, 4)],
 [('Сумма квадратов катетов', 'Sum of the squares of the legs'), ('Гипотенуза c', 'Hypotenuse c'), ('Квадрат на гипотенузе', 'The square on the hypotenuse')],
 'Площадь квадрата на гипотенузе равна сумме площадей квадратов на катетах: a² + b² = c².', 'The area of the square on the hypotenuse equals the sum of the areas of the squares on the legs: a² + b² = c².', ('Прямоугольный треугольник и три квадрата', 'A right triangle and three squares'),
 r'''const a=v.a,b=v.b,c=Math.hypot(a,b);const A=[0,0],B=[a,0],C2=[0,b],n=[b,a];
 const sq1=[A,B,[a,-a],[0,-a]],sq2=[A,C2,[-b,b],[-b,0]],sq3=[B,C2,[C2[0]+n[0],C2[1]+n[1]],[B[0]+n[0],B[1]+n[1]]];
 const all=[].concat(sq1,sq2,sq3),F=fitPts(all,20,10,560,195,0.98),cut=i=>F.slice(i*4,i*4+4);
 let g=poly(cut(0),"#fdf0c8",COL.ink,2)+poly(cut(1),"#dbe5f2",COL.ink,2)+poly(cut(2),"#e1f0e8",COL.ink,2)+poly([F[0],F[1],F[9]],"#f4dfd8",COL.ink,3);
 const mid=q=>[(q[0][0]+q[2][0])/2,(q[0][1]+q[2][1])/2];
 g+=TX(...mid(cut(0)).concat([a*a,COL.ink,16,"middle",700]))+TX(...mid(cut(1)).concat([b*b,COL.ink,16,"middle",700]))+TX(...mid(cut(2)).concat([fnum(c*c,1),COL.ink,16,"middle",700]));
 return {svg:g,st:[a+"² + "+b+"² = "+(a*a+b*b),fnum(c,3),fnum(c*c,2)],fb:U("c = √("+a+"² + "+b+"²) = √"+(a*a+b*b)+" ≈ "+fnum(c,3)+".","c = √("+a+"² + "+b+"²) = √"+(a*a+b*b)+" ≈ "+fnum(c,3)+".")}''', '0 0 600 215')

m2 = M(('Найдите сторону', 'Find the side'),
 [('s', 'k', 'Что найти', 'What to find', ['гипотенузу c', 'катет b'], ['the hypotenuse c', 'the leg b'], 0), ('r', 'x', 'Первое число', 'First number', 3, 20, 1, 6), ('r', 'y', 'Второе число', 'Second number', 3, 20, 1, 8)],
 [('Формула', 'Formula'), ('Подкоренное', 'Under the root'), ('Результат', 'Result')],
 'Гипотенуза — наибольшая сторона. Если известны гипотенуза и катет, катет находим вычитанием квадратов.', 'The hypotenuse is the longest side. Given the hypotenuse and a leg, we find the other leg by subtracting squares.', ('Прямоугольный треугольник', 'A right triangle'),
 r'''const hyp=v.k===0,a=hyp?v.x:Math.min(v.x,v.y-1),c=hyp?0:Math.max(v.x,v.y),b=hyp?v.y:0,rad=hyp?a*a+b*b:c*c-a*a,res=Math.sqrt(Math.max(0,rad));
 const T=hyp?[[0,0],[a,0],[0,b]]:[[0,0],[a,0],[0,res]];const F=fitPts(T,150,15,300,180),n=F;
 let g=poly(F,"#f4dfd8",COL.ink,3)+poly([[F[0][0],F[0][1]-14],[F[0][0]+14,F[0][1]-14],[F[0][0]+14,F[0][1]]],"none",COL.ink,1.5);
 g+=TX((F[0][0]+F[1][0])/2,F[0][1]+17,hyp?v.x:a,COL.a,15,"middle",700)+TX(F[0][0]-8,(F[0][1]+F[2][1])/2,hyp?v.y:fnum(res,2),COL.b,15,"end",700)+TX((F[1][0]+F[2][0])/2+14,(F[1][1]+F[2][1])/2-6,hyp?"c = ?":String(c),COL.c,15,"start",700);
 return {svg:g,st:[hyp?"c = √(a² + b²)":"b = √(c² − a²)",hyp?v.x+"² + "+v.y+"² = "+rad:c+"² − "+a+"² = "+rad,fnum(res,3)],fb:rad>0&&Math.abs(res-Math.round(res))<1e-9?U("Целое число — получилась пифагорова тройка!","An integer — a Pythagorean triple!"):U("Результат не целый — это нормально: корень не всегда извлекается.","The result is not an integer — that is fine: a root need not be exact.")}''', '0 0 600 210')

m3 = M(('Пифагоровы тройки', 'Pythagorean triples'),
 [('r', 'm', 'Число m', 'Number m', 2, 7, 1, 2), ('r', 'n', 'Число n', 'Number n', 1, 6, 1, 1)],
 [('Катеты 2mn и m² − n²', 'Legs 2mn and m² − n²'), ('Гипотенуза m² + n²', 'Hypotenuse m² + n²'), ('Проверка', 'Check')],
 'Для любых натуральных m &gt; n тройка (m² − n²; 2mn; m² + n²) — пифагорова: её можно использовать для «египетских» треугольников со строго прямым углом.', 'For any naturals m &gt; n the triple (m² − n²; 2mn; m² + n²) is Pythagorean: it can be used for “rope” triangles with an exact right angle.', ('Треугольник с целыми сторонами', 'A triangle with integer sides'),
 r'''const m=Math.max(v.m,v.n+1),n=v.n,p=m*m-n*n,qq=2*m*n,r=m*m+n*n;const F=fitPts([[0,0],[p,0],[0,qq]],150,15,300,180);let g=poly(F,"#f4dfd8",COL.ink,3)+TX((F[0][0]+F[1][0])/2,F[0][1]+17,p,COL.a,15,"middle",700)+TX(F[0][0]-8,(F[0][1]+F[2][1])/2,qq,COL.b,15,"end",700)+TX((F[1][0]+F[2][0])/2+14,(F[1][1]+F[2][1])/2-6,r,COL.c,15,"start",700);
 return {svg:g,st:[p+" и "+qq,r,p+"² + "+qq+"² = "+(p*p+qq*qq)+" = "+r+"²"],fb:gcd(gcd(p,qq),r)>1?U("Это тройка, умноженная на "+gcd(gcd(p,qq),r)+" — подобная меньшей.","This is a triple multiplied by "+gcd(gcd(p,qq),r)+" — similar to a smaller one."):U("Примитивная тройка: у чисел нет общего делителя.","A primitive triple: the numbers share no common divisor.")}''', '0 0 600 210')

chapter('36', '36-pythagoras.html', 'V', ('Теорема Пифагора', 'The Pythagorean theorem'),
 ('Главная теорема о прямоугольном треугольнике, её применение и пифагоровы тройки.', 'The main theorem about the right triangle, its uses and Pythagorean triples.'),
 ('Лестница длиной 5 м приставлена к стене так, что нижний конец стоит на расстоянии 3 м от стены.\n\nНа какой высоте верхний конец лестницы касается стены?', 'A 5 m ladder leans on a wall so that its lower end is 3 m from the wall.\n\nHow high up the wall does the top of the ladder reach?'),
 ('Разгадка: 4 м', 'The answer: 4 m'),
 ('Стена, земля и лестница образуют прямоугольный треугольник: лестница — гипотенуза c = 5, расстояние до стены — катет a = 3. По теореме Пифагора b² = c² − a² = 25 − 9 = 16, b = 4 м. Тройка 3–4–5 — самая известная: ею пользовались строители, чтобы получить прямой угол из верёвки.', 'The wall, the ground and the ladder form a right triangle: the ladder is the hypotenuse c = 5, the distance from the wall is the leg a = 3. By the Pythagorean theorem b² = c² − a² = 25 − 9 = 16, b = 4 m. The triple 3–4–5 is the best known: builders used it to get a right angle from a rope.'),
 [S('thm', 'Теорема Пифагора', 'The Pythagorean theorem', ('В прямоугольном треугольнике <strong>квадрат гипотенузы равен сумме квадратов катетов</strong>: c² = a² + b². Гипотенуза — сторона против прямого угла, она самая длинная. Теорема известна очень давно и имеет сотни доказательств; одно из них — через площади квадратов.', 'In a right triangle <strong>the square of the hypotenuse equals the sum of the squares of the legs</strong>: c² = a² + b². The hypotenuse is the side opposite the right angle; it is the longest. The theorem has been known for a very long time and has hundreds of proofs; one is via areas of squares.'),
    ('c² = a² + b²', '', 'c² = a² + b²'), m1),
  S('use', 'Применение', 'Applications', ('Теорема позволяет найти любую сторону, если известны две другие: c = √(a² + b²), a = √(c² − b²). <strong>Обратная теорема</strong>: если c² = a² + b², то треугольник прямоугольный. Расстояние между точками на плоскости — тоже теорема Пифагора.', 'The theorem lets us find any side from the other two: c = √(a² + b²), a = √(c² − b²). The <strong>converse</strong>: if c² = a² + b², the triangle is right-angled. The distance between points on a plane is also the Pythagorean theorem.'),
    ('a = √(c² − b²)', '', 'a = √(c² − b²)'), m2),
  S('trip', 'Пифагоровы тройки', 'Pythagorean triples', ('Натуральные числа, для которых c² = a² + b², — <strong>пифагорова тройка</strong>: (3; 4; 5), (5; 12; 13), (8; 15; 17). Умножая на одно число, получают новые: (6; 8; 10). Все тройки можно получить по формуле (m² − n²; 2mn; m² + n²).', 'Natural numbers with c² = a² + b² form a <strong>Pythagorean triple</strong>: (3; 4; 5), (5; 12; 13), (8; 15; 17). Multiplying by a number gives new ones: (6; 8; 10). All primitive triples come from the formula (m² − n²; 2mn; m² + n²).'),
    ('(m² − n²; 2mn; m² + n²)', '', '(m² − n²; 2mn; m² + n²)'), m3)],
 [TK(('Гипотенуза', 'Hypotenuse'), ('Катеты 6 и 8. Найдите гипотенузу.', 'Legs 6 and 8. Find the hypotenuse.'), '36 + 64', '√100 = 10.', '10.'),
  TK(('Катет', 'A leg'), ('Гипотенуза 13, катет 5. Найдите другой катет.', 'Hypotenuse 13, a leg 5. Find the other leg.'), '169 − 25', '√144 = 12.', '12.'),
  TK(('Диагональ', 'Diagonal'), ('Стороны прямоугольника 9 и 12. Его диагональ?', 'The sides of a rectangle are 9 and 12. Its diagonal?'), '81 + 144', '√225 = 15.', '15.'),
  TK(('Обратная теорема', 'The converse'), ('Прямоугольный ли треугольник со сторонами 7, 24, 25?', 'Is the triangle with sides 7, 24, 25 right-angled?'), '49 + 576 = 625', '25² = 625 — да.', ('Да.', 'Yes.')),
  TK(('Расстояние', 'Distance'), ('Найдите расстояние между (0; 0) и (5; 12).', 'Find the distance between (0; 0) and (5; 12).'), '', '√(25 + 144) = 13.', '13.')],
 [Q('Гипотенуза — это', 'The hypotenuse is', ('сторона против прямого угла', 'the side opposite the right angle'), ('меньший катет', 'the shorter leg'), ('высота', 'an altitude'), ('Определение.', 'The definition.')),
  Q('Катеты 3 и 4. Гипотенуза', 'Legs 3 and 4. The hypotenuse', '5', '7', '12', ('√25.', '√25.')),
  Q('c² =', 'c² =', 'a² + b²', 'a + b', '(a + b)²', ('Теорема.', 'The theorem.')),
  Q('Какая из троек пифагорова?', 'Which triple is Pythagorean?', '5, 12, 13', '4, 5, 6', '6, 7, 8', ('25 + 144 = 169.', '25 + 144 = 169.')),
  Q('Диагональ квадрата со стороной 1', 'The diagonal of a unit square', '√2', '2', '1', ('√(1 + 1).', '√(1 + 1).')),
  Q('Гипотенуза 10, катет 6. Другой катет', 'Hypotenuse 10, a leg 6. The other leg', '8', '4', '16', ('100 − 36 = 64.', '100 − 36 = 64.')),
  Q('Верна ли обратная теорема?', 'Is the converse true?', ('да', 'yes'), ('нет', 'no'), ('иногда', 'sometimes'), ('Если c² = a² + b², угол прямой.', 'If c² = a² + b², the angle is right.')),
  Q('(6; 8; 10) получена из тройки', '(6; 8; 10) comes from the triple', '(3; 4; 5)', '(5; 12; 13)', '(8; 15; 17)', ('Умножили на 2.', 'Multiplied by 2.'))],
 src=[('Wikipedia: Pythagorean theorem', 'https://en.wikipedia.org/wiki/Pythagorean_theorem'), ('Wikipedia: Pythagorean triple', 'https://en.wikipedia.org/wiki/Pythagorean_triple')],
 note=('Лестница и стена в загадке — условный пример.', 'The ladder and wall in the puzzle are an illustrative example.'))
