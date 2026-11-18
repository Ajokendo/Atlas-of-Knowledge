# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Возрастание и убывание', 'Increase and decrease'),
 [('r', 'x', 'Точка x', 'Point x', -3, 3, 0.1, -2)],
 [('f(x) = x³ − 3x', 'f(x) = x³ − 3x'), ('f′(x) = 3x² − 3', 'f′(x) = 3x² − 3'), ('Вывод', 'Conclusion')],
 'Знак производной определяет поведение функции: f′ &gt; 0 — возрастает (зелёное), f′ &lt; 0 — убывает (красное).', 'The sign of the derivative determines the behaviour: f′ &gt; 0 — increases, f′ &lt; 0 — decreases.', ('Участки монотонности', 'Intervals of monotonicity'),
 r'''const f=x=>x*x*x-3*x,d=x=>3*x*x-3;const G=Gr({x0:-3,x1:3,y0:-6,y1:6,L:80,T:10,W:470,H:210});let g=G.grid(1,2)+G.fn(f,COL.mut,2,-3,3,true);[[-3,-1,COL.a],[-1,1,COL.c],[1,3,COL.a]].forEach(p=>g+=G.fn(f,p[2],4,p[0],p[1]));g+=G.pt(v.x,f(v.x),COL.b,8);const dv=d(v.x);
 return {svg:g,st:[fnum(f(v.x),3),fnum(dv,3),dv>0.001?U("возрастает","increasing"):dv<-0.001?U("убывает","decreasing"):U("стационарная точка","a stationary point")],fb:U("Границы участков — точки, где f′ = 0: x = −1 и x = 1.","The boundaries of the intervals are where f′ = 0: x = −1 and x = 1.")}''', '0 0 600 250')

m2 = M(('Максимум и минимум', 'Maximum and minimum'),
 [('r', 'c', 'Параметр c', 'Parameter c', -1, 3, 0.25, 1)],
 [('Значение в x = −1', 'Value at x = −1'), ('Значение в x = 1', 'Value at x = 1'), ('Вывод', 'Conclusion')],
 'Точка, где f′ меняет знак с плюса на минус, — локальный максимум; с минуса на плюс — минимум. Параметр c поднимает весь график.', 'A point where f′ changes sign from plus to minus is a local maximum; from minus to plus — a minimum. The parameter c lifts the whole graph.', ('Экстремумы x³ − 3x + c', 'Extrema of x³ − 3x + c'),
 r'''const f=x=>x*x*x-3*x+v.c;const G=Gr({x0:-3,x1:3,y0:-6,y1:8,L:80,T:10,W:470,H:210});let g=G.grid(1,2)+G.fn(f,COL.a,3.5,-3,3)+G.pt(-1,f(-1),COL.c,8)+G.pt(1,f(1),COL.b,8)+G.txt(-1,f(-1)+0.8,"max",COL.c)+G.txt(1,f(1)-0.9,"min",COL.b);
 return {svg:g,st:[fnum(f(-1),3)+" (max)",fnum(f(1),3)+" (min)",f(-1)>0&&f(1)<0?U("три корня","three roots"):U("меньше трёх корней","fewer than three roots")],fb:U("Локальный максимум и минимум делят график на три участка монотонности.","The local maximum and minimum divide the graph into three monotone pieces.")}''', '0 0 600 250')

m3 = M(('Задача на наибольшее значение', 'An optimisation problem'),
 [('r', 'x', 'Ширина x, м', 'Width x, m', 1, 49, 1, 10)],
 [('Площадь S = x(50 − x)', 'Area S = x(50 − x)'), ('S′ = 50 − 2x', 'S′ = 50 − 2x'), ('Наибольшая при', 'Maximum at')],
 'Из 100 м забора нужно огородить прямоугольник наибольшей площади. Стороны x и 50 − x, площадь S = x(50 − x). Максимум там, где S′ = 0.', 'With 100 m of fence we want the rectangle of greatest area. The sides are x and 50 − x, area S = x(50 − x). The maximum is where S′ = 0.', ('Площадь как функция ширины', 'Area as a function of width'),
 r'''const S=x=>x*(50-x);const G=Gr({x0:0,x1:50,y0:0,y1:700,L:80,T:10,W:470,H:210});let g=G.grid(10,100)+G.fn(S,COL.a,3.5,0,50)+G.seg(25,0,25,625,COL.c,2,true)+G.pt(v.x,S(v.x),COL.b,8)+G.pt(25,625,COL.c,6);
 return {svg:g,st:[S(v.x)+" м²",fnum(50-2*v.x,0),"x = 25 м → 625 м²"],fb:U("Максимум — квадрат 25 × 25 м: S′ меняет знак с плюса на минус.","The maximum is the 25 × 25 m square: S′ changes sign from plus to minus.")}''', '0 0 600 250')

chapter('59', '59-derivative-applications.html', 'VIII', ('Применения производной', 'Applications of the derivative'),
 ('Где функция растёт, где у неё максимум и минимум, как решать задачи «как сделать лучше всего».', 'Where a function grows, where it has a maximum and minimum, and how to solve “how to do it best” problems.'),
 ('Фермеру нужно огородить забором длиной 100 м прямоугольный загон для овец, прижав его к реке: у реки забор не нужен. Какие размеры выбрать, чтобы загон был как можно больше?', 'A farmer wants a rectangular sheep pen fenced with 100 m of fence, with one side along a river where no fence is needed. What dimensions give the largest pen?'),
 ('Разгадка: 25 м в глубину и 50 м вдоль реки', 'The answer: 25 m deep and 50 m along the river'),
 ('Пусть две стороны забора, перпендикулярные реке, равны x, тогда третья сторона 100 − 2x, площадь S = x(100 − 2x) = 100x − 2x². Производная S′ = 100 − 4x равна нулю при x = 25. Тогда вдоль реки 50 м, а S = 1250 м². S′ положительна до 25 и отрицательна после, значит, это максимум. (Сюжет и числа придуманы для учебной задачи.)', 'Let the two fence sides perpendicular to the river be x; the third is 100 − 2x and the area S = x(100 − 2x) = 100x − 2x². The derivative S′ = 100 − 4x is zero at x = 25. Then the side along the river is 50 m and S = 1250 m². S′ is positive before 25 and negative after, so this is a maximum. (The story and numbers are invented for the exercise.)'),
 [S('mono', 'Монотонность', 'Monotonicity', ('Если f′(x) &gt; 0 на промежутке, функция там возрастает; если f′(x) &lt; 0 — убывает. Чтобы найти промежутки, решают f′ = 0 и смотрят знаки между корнями. Для f = x³ − 3x: f′ = 3(x − 1)(x + 1), промежутки возрастания (−∞; −1) и (1; +∞).', 'If f′(x) &gt; 0 on an interval the function increases there; if f′(x) &lt; 0 it decreases. To find the intervals solve f′ = 0 and check signs between the roots. For f = x³ − 3x: f′ = 3(x − 1)(x + 1), increasing on (−∞; −1) and (1; +∞).'),
    ('f′ > 0 ⇒ возрастает', '', 'f′ > 0 ⇒ increases'), m1),
  S('ext', 'Экстремумы', 'Extrema', ('Точки, где f′ = 0 или не существует, — «подозрительные» (критические). Если f′ меняет знак с + на −, это локальный максимум; с − на + — минимум. Если знак не меняется (как у x³ в нуле), экстремума нет.', 'Points where f′ = 0 or does not exist are “suspects” (critical points). If f′ changes sign from + to − it is a local maximum; from − to + a minimum. If the sign does not change (like x³ at zero) there is no extremum.'),
    ('f′ = 0 — критическая точка', '', 'f′ = 0 — critical point'), m2),
  S('opt', 'Наибольшее и наименьшее значения', 'Greatest and least values', ('На отрезке [a; b] наибольшее и наименьшее значения непрерывной функции достигаются либо в критических точках, либо на концах. Задача на оптимизацию: записать величину как функцию одной переменной, найти f′ = 0, проверить концы и смысл ответа.', 'On a segment [a; b] the greatest and least values of a continuous function are reached either at critical points or at the endpoints. An optimisation problem: write the quantity as a function of one variable, find f′ = 0, check the endpoints and the sense of the answer.'),
    ('max/min — в критических точках или на концах', '', 'max/min — at critical points or endpoints'), m3)],
 [TK(('Монотонность', 'Monotonicity'), ('Найдите промежутки возрастания f = x² − 4x.', 'Find the intervals of increase of f = x² − 4x.'), '', 'f′ = 2x − 4 > 0 при x > 2.', '(2; +∞).'),
  TK(('Минимум', 'Minimum'), ('Найдите точку минимума x² − 4x.', 'Find the minimum point of x² − 4x.'), '', 'f′ = 0 при x = 2, знак − → +. Минимум в x = 2, f(2) = −4.', ('x = 2, f = −4.', 'x = 2, f = −4.')),
  TK(('На отрезке', 'On a segment'), ('Наибольшее значение x³ − 3x на [0; 2].', 'The greatest value of x³ − 3x on [0; 2].'), 'f′ = 0 при x = 1', 'f(0) = 0, f(1) = −2, f(2) = 2. Наибольшее — 2.', '2.'),
  TK(('Оптимизация', 'Optimisation'), ('Сумма двух чисел 10. Какое наибольшее произведение?', 'The sum of two numbers is 10. What is the greatest product?'), 'P = x(10 − x)', 'P′ = 10 − 2x = 0, x = 5, P = 25.', '25.'),
  TK(('Нет экстремума', 'No extremum'), ('Есть ли экстремум у x³ в нуле?', 'Does x³ have an extremum at zero?'), '', 'f′ = 3x² ≥ 0 — знак не меняется, экстремума нет.', ('Нет.', 'No.'))],
 [Q('Если f′ > 0, функция', 'If f′ > 0 the function', ('возрастает', 'increases'), ('убывает', 'decreases'), ('постоянна', 'is constant'), ('Положительная скорость роста.', 'A positive rate of growth.')),
  Q('Точка максимума — где f′ меняет знак', 'A maximum point is where f′ changes sign', ('с + на −', 'from + to −'), ('с − на +', 'from − to +'), ('не меняет', 'does not change'), ('Рост сменяется спадом.', 'Growth turns into decline.')),
  Q('Критические точки — это где', 'Critical points are where', ('f′ = 0 или не существует', 'f′ = 0 or does not exist'), ('f = 0', 'f = 0'), ('f′ > 0', 'f′ > 0'), ('Определение.', 'The definition.')),
  Q('Наибольшее значение на отрезке может быть', 'The greatest value on a segment may be', ('на конце отрезка', 'at an endpoint'), ('только внутри', 'only inside'), ('нигде', 'nowhere'), ('Проверяют концы.', 'The endpoints are checked.')),
  Q('x² − 4x имеет минимум в', 'x² − 4x has a minimum at', 'x = 2', 'x = 4', 'x = 0', ('2x − 4 = 0.', '2x − 4 = 0.')),
  Q('У x³ в нуле', 'For x³ at zero', ('экстремума нет', 'there is no extremum'), ('максимум', 'a maximum'), ('минимум', 'a minimum'), ('Знак f′ не меняется.', 'The sign of f′ does not change.')),
  Q('Для x(10 − x) наибольшее значение при', 'For x(10 − x) the greatest value is at', 'x = 5', 'x = 10', 'x = 0', ('10 − 2x = 0.', '10 − 2x = 0.')),
  Q('Первый шаг оптимизационной задачи', 'The first step of an optimisation problem', ('записать величину функцией одной переменной', 'write the quantity as a function of one variable'), ('найти f(0)', 'find f(0)'), ('нарисовать окружность', 'draw a circle'), ('Нужна функция.', 'A function is needed.'))],
 src=[('Wikipedia: Maxima and minima', 'https://en.wikipedia.org/wiki/Maximum_and_minimum'), ('Wikipedia: Mathematical optimization', 'https://en.wikipedia.org/wiki/Mathematical_optimization'), ('OpenStax: Calculus Volume 1', 'https://openstax.org/details/books/calculus-volume-1')],
 note=('Сюжеты про загон и забор придуманы для задач.', 'The pen and fence stories are invented for the exercises.'))
