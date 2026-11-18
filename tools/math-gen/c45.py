# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Линейное неравенство', 'A linear inequality'),
 [('r', 'a', 'a', 'a', -4, 4, 1, 2), ('r', 'b', 'b', 'b', -8, 8, 1, -4), ('s', 'sg', 'Знак', 'Sign', ['>', '≥', '<', '≤'], ['>', '≥', '<', '≤'], 0)],
 [('Неравенство', 'The inequality'), ('Решение', 'The solution'), ('Запись промежутка', 'Interval notation')],
 'Решаем как уравнение, но при умножении или делении на отрицательное число знак неравенства меняется на противоположный.', 'We solve as an equation, but when multiplying or dividing by a negative number the inequality sign flips.', ('Решение на числовой прямой', 'The solution on the number line'),
 r'''const a=v.a===0?1:v.a,sg=[">","≥","<","≤"][v.sg],x0=-v.b/a,flip=a<0,eff=flip?{">":"<","≥":"≤","<":">","≤":"≥"}[sg]:sg,X=t=>300+t*30;let g=L(30,100,570,100,COL.ink,3);for(let t=-9;t<=9;t++)g+=L(X(t),94,X(t),106,COL.ink,1.5)+(t%3===0?TX(X(t),128,t,COL.mut,11):"");
 const right=eff===">"||eff==="≥",cl=eff==="≥"||eff==="≤",xe=clamp(x0,-9.3,9.3);g+=L(X(xe),100,right?570:30,100,COL.a,6)+C(X(xe),100,8,cl?COL.a:"#fff",COL.a,3)+TX(X(xe),75,fnum(x0,2),COL.a,14,"middle",700);
 const iv=right?(cl?"[":"(")+fnum(x0,2)+"; +∞)":"(−∞; "+fnum(x0,2)+(cl?"]":")");return {svg:g,st:[a+"x "+(v.b<0?"− "+(-v.b):"+ "+v.b)+" "+sg+" 0","x "+eff+" "+fnum(x0,2),iv],fb:flip?U("a < 0: знак при делении на "+a+" изменился.","a < 0: the sign flipped when dividing by "+a+"."):U("Знак сохраняется, потому что a > 0.","The sign is kept because a > 0.")}''', '0 0 600 160')

m2 = M(('Квадратное неравенство', 'A quadratic inequality'),
 [('r', 'p', 'Корень x₁', 'Root x₁', -6, 6, 1, -2), ('r', 'q', 'Корень x₂', 'Root x₂', -6, 6, 1, 3), ('s', 'sg', 'Знак', 'Sign', ['> 0', '< 0'], ['> 0', '< 0'], 1)],
 [('Парабола', 'The parabola'), ('Решение', 'The solution'), ('Запись промежутком', 'Interval notation')],
 'Решение квадратного неравенства — те x, где парабола лежит выше (> 0) или ниже (< 0) оси x.', 'The solution of a quadratic inequality is the set of x where the parabola lies above (> 0) or below (< 0) the x-axis.', ('Парабола и закрашенное решение', 'A parabola and the shaded solution'),
 r'''const fx=r=>r<0?"(x + "+(-r)+")":r===0?"x":"(x − "+r+")";const lo=Math.min(v.p,v.q),hi=Math.max(v.p,v.q),G=Gr({x0:-8,x1:8,y0:-12,y1:12,L:100,T:10,W:400,H:210});const pos=v.sg===0;let g=G.grid(2,4);
 const seg=(a,b)=>R(G.X(a),G.Y(0)-5,G.X(b)-G.X(a),10,COL.a,"none",0,0);
 g+=G.fn(x=>(x-lo)*(x-hi),COL.b,3.5);if(pos){g+=seg(-8,lo)+seg(hi,8)}else g+=seg(lo,hi);g+=G.pt(lo,0,COL.c,6)+G.pt(hi,0,COL.c,6);
 return {svg:g,st:[fx(lo)+fx(hi)+" "+(pos?"> 0":"< 0"),pos?U("x &lt; "+lo+" или x &gt; "+hi,"x &lt; "+lo+" or x &gt; "+hi):lo+" < x < "+hi,pos?"(−∞; "+lo+") ∪ ("+hi+"; +∞)":"("+lo+"; "+hi+")"],fb:U("Выше оси — вне корней, ниже — между корнями.","Above the axis — outside the roots, below — between them.")}''', '0 0 600 250')

m3 = M(('Метод интервалов', 'The interval method'),
 [('r', 'p', 'Корень 1', 'Root 1', -6, 6, 1, -3), ('r', 'q', 'Корень 2', 'Root 2', -6, 6, 1, 1), ('r', 'r', 'Корень 3', 'Root 3', -6, 6, 1, 4)],
 [('Выражение', 'The expression'), ('Знаки справа налево', 'Signs from right to left'), ('Решение f > 0', 'The solution f > 0')],
 'Нули делят прямую на интервалы. Правее наибольшего нуля выражение положительно, и при переходе через каждый простой нуль знак меняется.', 'The zeros divide the line into intervals. To the right of the largest zero the expression is positive and the sign changes at every simple zero.', ('Знаки на числовой прямой', 'Signs on the number line'),
 r'''const fx=r=>r<0?"(x + "+(-r)+")":r===0?"x":"(x − "+r+")";const z=[v.p,v.q,v.r].sort((x,y)=>x-y),X=t=>300+t*30;let g=L(30,100,570,100,COL.ink,3);const edges=[-9.5].concat(z).concat([9.5]);const sg=[];for(let i=0;i<4;i++){const s=((3-i)%2===0)?1:-1;sg.push(s)}
 for(let i=0;i<4;i++){const a=X(edges[i]),b=X(edges[i+1]);g+=R(a,90,b-a,20,sg[i]>0?"#e1f0e8":"#f4dfd8","none",0,0)+TX((a+b)/2,60,sg[i]>0?"+":"−",sg[i]>0?COL.c:COL.a,26,"middle",700)}
 z.forEach(t=>g+=C(X(t),100,7,COL.ink)+TX(X(t),135,t,COL.ink,14,"middle",700));
 const same=z[0]===z[1]||z[1]===z[2];const sol=[];if(!same){sol.push("("+z[0]+"; "+z[1]+")");sol.push("("+z[2]+"; +∞)")}
 return {svg:g,st:[fx(z[0])+fx(z[1])+fx(z[2]),same?U("кратные корни — нужен другой подход","repeated roots need another approach"):"+ − + −",same?"—":sol.join(" ∪ ")],fb:U("Подставьте пробное число в каждый интервал, чтобы проверить знаки.","Test a trial number in each interval to check the signs.")}''', '0 0 600 160')

chapter('45', '45-inequalities.html', 'VI', ('Неравенства', 'Inequalities'),
 ('Как решать линейные и квадратные неравенства и записывать ответ промежутками.', 'How to solve linear and quadratic inequalities and write the answer as intervals.'),
 ('Билет в кино стоит 150 сомов. Айгуль взяла 1 000 сомов.\n\nСколько билетов она может купить? Сколько — если ещё нужно оставить 200 сомов на проезд?', 'A cinema ticket costs 150 som. Aigul has 1,000 som.\n\nHow many tickets can she buy? How many if she must keep 200 som for the fare?'),
 ('Разгадка: 6 и 5 билетов', 'The answer: 6 and 5 tickets'),
 ('Неравенство 150x ≤ 1000 даёт x ≤ 6,67, а билетов целое число — 6. Если нужно оставить 200 сомов: 150x ≤ 800, x ≤ 5,33, то есть 5 билетов. Неравенство описывает не одно решение, а целое множество; его записывают промежутком и изображают на числовой прямой.', 'The inequality 150x ≤ 1000 gives x ≤ 6.67 and the number of tickets is an integer — 6. If 200 som must stay: 150x ≤ 800, x ≤ 5.33, that is 5 tickets. An inequality describes not one solution but a whole set; it is written as an interval and drawn on the number line.'),
 [S('lin', 'Линейные неравенства', 'Linear inequalities', ('Неравенство решают так же, как уравнение, но: при умножении или делении обеих частей на <em>отрицательное</em> число знак меняется на противоположный. Ответ — промежуток: (−∞; 3) — все x меньше 3 (скобка круглая, число не входит); [3; +∞) — все x не меньше 3 (скобка квадратная, число входит).', 'An inequality is solved like an equation but: when multiplying or dividing both sides by a <em>negative</em> number the sign flips. The answer is an interval: (−∞; 3) — all x less than 3 (round bracket, the number is not included); [3; +∞) — all x at least 3 (square bracket, the number is included).'),
    ('−2x > 6  ⟹  x < −3', '', '−2x > 6  ⟹  x < −3'), m1),
  S('quad', 'Квадратные неравенства', 'Quadratic inequalities', ('Для ax² + bx + c &gt; 0 находят корни и смотрят на параболу: при a &gt; 0 выражение положительно вне корней и отрицательно между ними. Если корней нет, парабола целиком выше (или ниже) оси.', 'For ax² + bx + c &gt; 0 we find the roots and look at the parabola: for a &gt; 0 the expression is positive outside the roots and negative between them. If there are no roots the parabola lies wholly above (or below) the axis.'),
    ('(x − x₁)(x − x₂) < 0 ⟺ x₁ < x < x₂', '', '(x − x₁)(x − x₂) < 0 ⟺ x₁ < x < x₂'), m2),
  S('int', 'Метод интервалов', 'The interval method', ('Для произведений и дробей: 1) находят нули множителей; 2) отмечают их на прямой; 3) определяют знак на правом интервале и чередуют знаки при переходе через каждый простой нуль. Выбирают интервалы с нужным знаком.', 'For products and fractions: 1) find the zeros of the factors; 2) mark them on the line; 3) determine the sign on the rightmost interval and alternate the signs when crossing each simple zero. Choose the intervals with the required sign.'),
    ('знаки чередуются', '', 'the signs alternate'), m3)],
 [TK(('Линейное', 'Linear'), ('Решите 3x − 5 > 7.', 'Solve 3x − 5 > 7.'), '3x > 12', 'x > 4. Ответ (4; +∞).', ('x > 4.', 'x > 4.')),
  TK(('Смена знака', 'Sign flip'), ('Решите −2x + 1 ≥ 9.', 'Solve −2x + 1 ≥ 9.'), '−2x ≥ 8', 'Делим на −2: x ≤ −4.', ('(−∞; −4].', '(−∞; −4].')),
  TK(('Квадратное', 'Quadratic'), ('Решите x² − 4 < 0.', 'Solve x² − 4 < 0.'), '(x − 2)(x + 2) < 0', 'Между корнями: −2 < x < 2.', ('(−2; 2).', '(−2; 2).')),
  TK(('Квадратное, снаружи', 'Quadratic, outside'), ('Решите x² − 5x + 6 > 0.', 'Solve x² − 5x + 6 > 0.'), 'Корни 2 и 3', 'Вне корней: x < 2 или x > 3.', ('(−∞; 2) ∪ (3; +∞).', '(−∞; 2) ∪ (3; +∞).')),
  TK(('Цена', 'Price'), ('Тетрадь 25 сомов. Сколько тетрадей можно купить на 130 сомов?', 'A notebook costs 25 som. How many notebooks can be bought for 130 som?'), '25x ≤ 130', 'x ≤ 5,2, значит 5.', '5.')],
 [Q('Решение x > 3 изображают', 'The solution x > 3 is drawn as', ('луч вправо от 3, точка пустая', 'a ray right of 3 with an open dot'), ('луч влево', 'a ray left'), ('точка 3', 'the point 3'), ('3 не входит.', '3 is not included.')),
  Q('−x < 4 ⟹', '−x < 4 ⟹', 'x > −4', 'x < −4', 'x < 4', ('При делении на −1 знак меняется.', 'Dividing by −1 flips the sign.')),
  Q('Запись [2; 5) означает', 'The notation [2; 5) means', ('2 ≤ x < 5', '2 ≤ x < 5'), ('2 < x ≤ 5', '2 < x ≤ 5'), ('2 < x < 5', '2 < x < 5'), ('Квадратная скобка включает.', 'A square bracket includes.')),
  Q('x² < 9', 'x² < 9', '−3 < x < 3', 'x < 3', 'x > 3', ('Между корнями.', 'Between the roots.')),
  Q('x² > 9', 'x² > 9', ('x < −3 или x > 3', 'x < −3 or x > 3'), ('−3 < x < 3', '−3 < x < 3'), ('x > 3', 'x > 3'), ('Вне корней.', 'Outside the roots.')),
  Q('При умножении на отрицательное число знак неравенства', 'When multiplying by a negative number the sign of an inequality', ('меняется', 'flips'), ('сохраняется', 'stays'), ('исчезает', 'vanishes'), ('Правило.', 'The rule.')),
  Q('Нули (x − 1)(x + 2)(x − 5): сколько интервалов?', 'The zeros of (x − 1)(x + 2)(x − 5): how many intervals?', '4', '3', '2', ('Три точки — четыре интервала.', 'Three points — four intervals.')),
  Q('Целые решения 1 < x ≤ 4', 'The integer solutions of 1 < x ≤ 4', '2, 3, 4', '1, 2, 3, 4', '2, 3', ('1 не входит, 4 входит.', '1 is not included, 4 is.'))],
 src=[('Wikipedia: Inequality (mathematics)', 'https://en.wikipedia.org/wiki/Inequality_(mathematics)'), ('Wikipedia: Interval (mathematics)', 'https://en.wikipedia.org/wiki/Interval_(mathematics)')],
 note=('Цены на билеты в примере придуманы.', 'The ticket prices in the example are made up.'))
