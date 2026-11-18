# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Прямая y = kx + b', 'The line y = kx + b'),
 [('r', 'k', 'Наклон k', 'Slope k', -4, 4, 0.5, 1.5), ('r', 'b', 'Сдвиг b', 'Intercept b', -6, 6, 1, 2)],
 [('Формула', 'Formula'), ('Пересечение с осью y', 'Meets the y-axis'), ('Пересечение с осью x', 'Meets the x-axis')],
 'k — на сколько растёт y при увеличении x на 1; b — значение при x = 0. Если k &gt; 0, функция возрастает, если k &lt; 0 — убывает.', 'k is how much y grows when x increases by 1; b is the value at x = 0. If k &gt; 0 the function increases, if k &lt; 0 it decreases.', ('График линейной функции', 'The graph of a linear function'),
 r'''const G=Gr({x0:-8,x1:8,y0:-8,y1:8,L:100,T:10,W:400,H:210});let g=G.grid(2,2)+G.fn(x=>v.k*x+v.b,COL.a,3.5)+G.pt(0,v.b,COL.b,7);if(v.k!==0)g+=G.pt(-v.b/v.k,0,COL.c,7);
 g+=G.seg(0,v.b,1,v.b,COL.mut,1.5)+G.seg(1,v.b,1,v.b+v.k,COL.mut,1.5);
 return {svg:g,st:["y = "+fnum(v.k,1)+"x "+(v.b<0?"− "+(-v.b):"+ "+v.b),"(0; "+v.b+")",v.k===0?U("не пересекает (или совпадает)","no crossing (or coincides)"):"("+fnum(-v.b/v.k,2)+"; 0)"],fb:v.k>0?U("k > 0: график идёт вверх.","k > 0: the graph goes up."):v.k<0?U("k < 0: график идёт вниз.","k < 0: the graph goes down."):U("k = 0: горизонтальная прямая.","k = 0: a horizontal line.")}''', '0 0 600 250')

m2 = M(('Два тарифа', 'Two tariffs'),
 [('r', 'fa', 'Тариф A: плата за вход', 'Tariff A: fixed fee', 0, 300, 10, 200), ('r', 'ra', 'Тариф A: за км', 'Tariff A: per km', 5, 50, 1, 10), ('r', 'fb', 'Тариф B: плата за вход', 'Tariff B: fixed fee', 0, 300, 10, 50), ('r', 'rb', 'Тариф B: за км', 'Tariff B: per km', 5, 50, 1, 20)],
 [('Тариф A', 'Tariff A'), ('Тариф B', 'Tariff B'), ('Где тарифы равны', 'Where the tariffs are equal')],
 'Графики двух линейных функций пересекаются там, где цены равны. До этой точки выгоден один тариф, после — другой.', 'The graphs of two linear functions meet where the prices are equal. Before this point one tariff is cheaper, after it the other.', ('Стоимость поездки в зависимости от расстояния (условные тарифы)', 'Trip cost depending on distance (illustrative tariffs)'),
 r'''const G=Gr({x0:0,x1:30,y0:0,y1:1000,L:80,T:10,W:460,H:210});let g=G.grid(5,200)+G.fn(x=>v.fa+v.ra*x,COL.a,3)+G.fn(x=>v.fb+v.rb*x,COL.b,3);
 let st3;if(v.ra===v.rb){st3=v.fa===v.fb?U("тарифы совпадают","tariffs coincide"):U("никогда","never")}else{const x=(v.fb-v.fa)/(v.ra-v.rb);if(x>0&&x<=30){g+=G.pt(x,v.fa+v.ra*x,COL.c,8);st3=fnum(x,1)+" км, "+fnum(v.fa+v.ra*x,0)+" сомов"}else st3=U("в диапазоне 0–30 км нет","not within 0–30 km")}
 return {svg:g,st:[v.fa+" + "+v.ra+"·x",v.fb+" + "+v.rb+"·x",st3],fb:U("Выгоднее тот тариф, чей график ниже.","The cheaper tariff is the one whose graph is lower.")}''', '0 0 600 250')

m3 = M(('Обратная пропорциональность', 'Inverse proportion'),
 [('r', 'k', 'Постоянная k', 'The constant k', -12, 12, 1, 6), ('r', 'x', 'Точка x', 'Point x', -6, 6, 0.5, 2)],
 [('Формула', 'Formula'), ('y в точке x', 'y at the point x'), ('Произведение x·y', 'Product x·y')],
 'В обратной пропорциональности y = k/x произведение x·y всегда равно k. График — гипербола из двух ветвей.', 'In inverse proportion y = k/x the product x·y is always k. The graph is a hyperbola with two branches.', ('Гипербола', 'The hyperbola'),
 r'''const G=Gr({x0:-8,x1:8,y0:-8,y1:8,L:100,T:10,W:400,H:210});let g=G.grid(2,2);if(v.k!==0){g+=G.fn(x=>v.k/x,COL.a,3.5,-8,-0.05)+G.fn(x=>v.k/x,COL.a,3.5,0.05,8);if(v.x!==0){const y=v.k/v.x;g+=G.seg(v.x,0,v.x,y,COL.mut,1.5)+G.seg(0,y,v.x,y,COL.mut,1.5)+G.pt(v.x,y,COL.b,7)}}
 return {svg:g,st:["y = "+v.k+"/x",v.x===0?U("не определено","undefined"):fnum(v.k/v.x,3),v.x===0?"—":fnum(v.x*(v.k/v.x),2)],fb:v.k>0?U("k > 0: ветви в I и III четвертях.","k > 0: the branches lie in quadrants I and III."):v.k<0?U("k < 0: ветви во II и IV четвертях.","k < 0: the branches lie in quadrants II and IV."):U("k = 0: функция y = 0 (кроме x = 0).","k = 0: the function y = 0 (except x = 0).")}''', '0 0 600 250')

chapter('40', '40-linear-inverse.html', 'VI', ('Линейная функция и обратная пропорциональность', 'The linear function and inverse proportion'),
 ('Две простейшие функции: прямая y = kx + b и гипербола y = k/x.', 'The two simplest functions: the line y = kx + b and the hyperbola y = k/x.'),
 ('Две мастерские шьют шапки. Первая берёт 200 сомов за настройку станка и 10 сомов за шапку, вторая — 50 сомов за настройку и 20 сомов за шапку.\n\nПри каком количестве шапок цены равны?', 'Two workshops sew hats. The first charges 200 som for setting up and 10 som per hat, the second 50 som for setting up and 20 som per hat.\n\nFor how many hats are the prices equal?'),
 ('Разгадка: при 15 шапках', 'The answer: at 15 hats'),
 ('Стоимости: 200 + 10x и 50 + 20x. Приравняем: 200 + 10x = 50 + 20x, откуда 10x = 150 и x = 15. При 15 шапках в обеих мастерских цена одна и та же — 350 сомов. Меньше 15 шапок выгоднее вторая мастерская, больше — первая. На графике это точка пересечения двух прямых.', 'The costs are 200 + 10x and 50 + 20x. Equating: 200 + 10x = 50 + 20x, so 10x = 150 and x = 15. For 15 hats both workshops charge the same — 350 som. For fewer than 15 hats the second workshop is cheaper, for more — the first. On a graph it is the intersection of two lines.'),
 [S('lin', 'Линейная функция', 'The linear function', ('<strong>Линейная функция</strong> y = kx + b. Её график — прямая. <strong>k</strong> — угловой коэффициент (наклон): при k &gt; 0 функция возрастает, при k &lt; 0 убывает. <strong>b</strong> — ордината пересечения с осью y. Прямые с равными k параллельны. Нуль функции x = −b/k.', 'The <strong>linear function</strong> y = kx + b. Its graph is a straight line. <strong>k</strong> is the slope: for k &gt; 0 the function increases, for k &lt; 0 it decreases. <strong>b</strong> is the y-intercept. Lines with equal k are parallel. The zero of the function is x = −b/k.'),
    ('y = kx + b;  x₀ = −b/k', '', 'y = kx + b;  x₀ = −b/k'), m1),
  S('two', 'Два графика', 'Two graphs', ('Чтобы найти, где две функции равны, приравнивают их формулы или находят точку пересечения графиков. Если один график лежит ниже другого — для таких x значение первой функции меньше. Так сравнивают тарифы, планы, зарплаты.', 'To find where two functions are equal we equate their formulas or find the intersection of their graphs. If one graph lies lower than another — for such x the first function’s value is smaller. This is how tariffs, plans and salaries are compared.'),
    ('f(x) = g(x)', 'точка пересечения', 'the intersection point'), m2),
  S('inv', 'Обратная пропорциональность', 'Inverse proportion', ('Функция y = k/x (k ≠ 0, x ≠ 0). Чем больше x, тем меньше |y|, а произведение xy остаётся равным k. График — <strong>гипербола</strong>, она не пересекает оси, но неограниченно приближается к ним (оси — <em>асимптоты</em>). Пример: время в пути на один путь при разных скоростях.', 'The function y = k/x (k ≠ 0, x ≠ 0). As x grows |y| shrinks while the product xy stays equal to k. The graph is a <strong>hyperbola</strong>; it never crosses the axes but approaches them without limit (the axes are <em>asymptotes</em>). Example: travel time over one distance at different speeds.'),
    ('x·y = k', '', 'x·y = k'), m3)],
 [TK(('Угловой коэффициент', 'Slope'), ('Найдите k для прямой, проходящей через (0; 1) и (2; 7).', 'Find k for the line through (0; 1) and (2; 7).'), '(7 − 1) : (2 − 0)', 'k = 3, значит y = 3x + 1.', ('k = 3.', 'k = 3.')),
  TK(('Нуль', 'Zero'), ('Найдите нуль функции y = −2x + 6.', 'Find the zero of y = −2x + 6.'), '', '−2x + 6 = 0, x = 3.', 'x = 3.'),
  TK(('Параллельные', 'Parallel'), ('Параллельна ли y = 3x + 1 прямой y = 3x − 5?', 'Is y = 3x + 1 parallel to y = 3x − 5?'), '', 'Угловые коэффициенты равны (3) — параллельны.', ('Да.', 'Yes.')),
  TK(('Равные цены', 'Equal prices'), ('При каком x равны 100 + 5x и 20 + 15x?', 'For which x are 100 + 5x and 20 + 15x equal?'), '', '80 = 10x, x = 8.', 'x = 8.'),
  TK(('Гипербола', 'Hyperbola'), ('y = 12/x. Найдите y при x = 4 и x при y = 3.', 'y = 12/x. Find y at x = 4 and x at y = 3.'), '', 'y = 12 : 4 = 3; x = 12 : 3 = 4.', ('3 и 4.', '3 and 4.'))],
 [Q('У y = 2x − 3 наклон равен', 'The slope of y = 2x − 3 is', '2', '−3', '3', ('Коэффициент при x.', 'The coefficient of x.')),
  Q('Прямая y = x + 5 пересекает ось y в точке', 'The line y = x + 5 meets the y-axis at', '(0; 5)', '(5; 0)', '(−5; 0)', ('При x = 0 y = 5.', 'At x = 0, y = 5.')),
  Q('Функция y = −3x + 1', 'The function y = −3x + 1', ('убывает', 'is decreasing'), ('возрастает', 'is increasing'), ('постоянна', 'is constant'), ('k = −3 < 0.', 'k = −3 < 0.')),
  Q('Нуль функции y = 4x − 8', 'The zero of y = 4x − 8', '2', '−2', '8', ('4x = 8.', '4x = 8.')),
  Q('График y = 5/x', 'The graph of y = 5/x', ('гипербола', 'a hyperbola'), ('прямая', 'a line'), ('парабола', 'a parabola'), ('Обратная пропорциональность.', 'Inverse proportion.')),
  Q('Для y = 6/x произведение x·y', 'For y = 6/x the product x·y', 'всегда 6', 'меняется', 'всегда 1', ('x · (6/x) = 6.', 'x · (6/x) = 6.')),
  Q('Прямые y = 2x и y = 2x + 7', 'The lines y = 2x and y = 2x + 7', ('параллельны', 'are parallel'), ('пересекаются', 'intersect'), ('совпадают', 'coincide'), ('Равные k.', 'Equal k.')),
  Q('Ось x для гиперболы y = k/x — это', 'For the hyperbola y = k/x the x-axis is', ('асимптота', 'an asymptote'), ('касательная', 'a tangent'), ('ось симметрии', 'an axis of symmetry'), ('Ветви приближаются, но не касаются.', 'The branches approach but never touch it.'))],
 src=[('Wikipedia: Linear function', 'https://en.wikipedia.org/wiki/Linear_function'), ('Wikipedia: Hyperbola', 'https://en.wikipedia.org/wiki/Hyperbola')],
 note=('Мастерские и тарифы в примерах придуманы.', 'The workshops and tariffs in the examples are made up.'))
