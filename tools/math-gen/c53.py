# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Рост и убывание: график aˣ', 'Growth and decay: the graph of aˣ'),
 [('r', 'a', 'Основание a', 'Base a', 0.2, 4, 0.1, 2), ('r', 'x', 'Показатель x', 'Exponent x', -3, 4, 0.5, 2)],
 [('aˣ при выбранном x', 'aˣ at the chosen x'), ('Характер', 'Behaviour'), ('Через точку', 'Through the point')],
 'При a &gt; 1 функция возрастает, при 0 &lt; a &lt; 1 убывает. Все графики проходят через (0; 1), и aˣ всегда положительна.', 'For a &gt; 1 the function increases; for 0 &lt; a &lt; 1 it decreases. All graphs pass through (0; 1) and aˣ is always positive.', ('График показательной функции', 'The graph of an exponential function'),
 r'''const G=Gr({x0:-4,x1:5,y0:-1,y1:12,L:90,T:10,W:450,H:210});const y=Math.pow(v.a,v.x);let g=G.grid(1,2)+G.fn(t=>Math.pow(v.a,t),COL.a,3.5,-4,5)+G.pt(0,1,COL.c,6)+G.seg(v.x,0,v.x,Math.min(y,12),COL.mut,1.5)+G.pt(v.x,Math.min(y,12),COL.b,8);
 return {svg:g,st:[fnum(y,4),v.a>1?U("возрастает","increasing"):v.a<1?U("убывает","decreasing"):U("постоянная y = 1","constant y = 1"),"(0; 1)"],fb:U("Показательная функция не бывает отрицательной или нулевой: aˣ > 0.","An exponential function is never negative or zero: aˣ > 0.")}''', '0 0 600 250')

m2 = M(('Удвоение и полураспад', 'Doubling and half-life'),
 [('s', 'k', 'Процесс', 'Process', ['удвоение (бактерии)', 'полураспад (вещество)'], ['doubling (bacteria)', 'half-life (a substance)'], 0), ('r', 'T', 'Период T (шаг), ч', 'Period T (step), h', 1, 10, 1, 3), ('r', 'N', 'Начальное количество', 'Initial amount', 1, 100, 1, 10), ('r', 't', 'Время t, ч', 'Time t, h', 0, 40, 1, 12)],
 [('Через время t', 'After time t'), ('Число периодов', 'Number of periods'), ('Формула', 'Formula')],
 'Если количество каждые T часов удваивается (или уменьшается вдвое), то после t часов оно равно N·2^(t/T) (или N·2^(−t/T)).', 'If the amount doubles (or halves) every T hours, then after t hours it equals N·2^(t/T) (or N·2^(−t/T)).', ('Изменение количества со временем (условная модель)', 'The change of amount over time (illustrative model)'),
 r'''const sg=v.k===0?1:-1,F=t=>v.N*Math.pow(2,sg*t/v.T),mx=Math.max(F(0),F(40),1);const G=Gr({x0:0,x1:40,y0:0,y1:Math.min(mx*1.1,v.N*60),L:90,T:10,W:450,H:210});let g=G.grid(10,Math.max(1,Math.round(Math.min(mx,v.N*60)/4)))+G.fn(F,COL.a,3.5,0,40)+G.pt(v.t,F(v.t),COL.b,8);
 return {svg:g,st:[fnum(F(v.t),2),fnum(v.t/v.T,2),v.N+"·2"+(sg<0?"^(−t/"+v.T+")":"^(t/"+v.T+")")],fb:U("Условная модель: реальные процессы только приближённо подчиняются такой формуле.","An illustrative model: real processes only approximately follow such a formula.")}''', '0 0 600 250')

m3 = M(('Число e', 'The number e'),
 [('r', 'n', 'Число делений года n', 'Number of compounding periods n', 1, 365, 1, 4)],
 [('(1 + 1/n)ⁿ', '(1 + 1/n)ⁿ'), ('Предел e', 'The limit e'), ('Отличие', 'The difference')],
 'Если делить год на всё больше частей и начислять процент всё чаще, итоговая сумма не растёт бесконечно: она приближается к числу e ≈ 2,71828.', 'If we split a year into more and more parts and compound more often, the total does not grow without limit: it approaches the number e ≈ 2.71828.', ('Значения (1 + 1/n)ⁿ при разных n', 'Values of (1 + 1/n)ⁿ for different n'),
 r'''const f=n=>Math.pow(1+1/n,n),G=Gr({x0:0,x1:60,y0:2,y1:3,L:90,T:10,W:450,H:210});let g=G.grid(10,0.2)+G.fn(x=>f(Math.max(x,1)),COL.a,3.5,1,60)+G.seg(0,Math.E,60,Math.E,COL.c,2,true);if(v.n<=60)g+=G.pt(v.n,f(v.n),COL.b,8);
 return {svg:g,st:[fnum(f(v.n),6),fnum(Math.E,6),fnum(Math.E-f(v.n),6)],fb:U("Чем больше n, тем ближе к e: e — предел, а не точная дробь.","The larger n, the closer to e: e is a limit, not an exact fraction.")}''', '0 0 600 250')

chapter('53', '53-exponential.html', 'VII', ('Показательная функция', 'The exponential function'),
 ('Функции вида aˣ: удвоение, полураспад, сложные проценты и число e.', 'Functions of the form aˣ: doubling, half-life, compound interest and the number e.'),
 ('Вам предлагают на месяц два варианта подарка. Первый: каждый день по 1 000 сомов. Второй: в первый день 1 сом, а каждый следующий день вдвое больше предыдущего.\n\nЧто выгоднее за 30 дней?', 'You are offered two gift options for a month. The first: 1,000 som each day. The second: 1 som on the first day and each next day twice the previous.\n\nWhich is better over 30 days?'),
 ('Разгадка: второй, получится более 1 млрд', 'The answer: the second, over 1 billion'),
 ('Первый вариант за 30 дней — 30 000 сомов. Во втором в день n выплата 2ⁿ⁻¹; в 30-й день 2²⁹ ≈ 537 млн сомов, а сумма за 30 дней 2³⁰ − 1 ≈ 1,07 млрд. Показательный рост поначалу выглядит скромным (1, 2, 4, 8…), но неизбежно обгоняет любой линейный.', 'The first option over 30 days is 30,000 som. In the second the payout on day n is 2ⁿ⁻¹; on day 30 it is 2²⁹ ≈ 537 million som, and the total over 30 days is 2³⁰ − 1 ≈ 1.07 billion. Exponential growth looks modest at first (1, 2, 4, 8…) but inevitably overtakes any linear growth.'),
 [S('def', 'Показательная функция', 'The exponential function', ('<strong>y = aˣ</strong> (a &gt; 0, a ≠ 1). Степень с нулевым показателем равна 1, с отрицательным — обратному числу: a⁻ⁿ = 1/aⁿ, с дробным — корню: a^(1/n) = ⁿ√a. Область значений — все положительные числа. Свойства: aˣ · aʸ = aˣ⁺ʸ, (aˣ)ʸ = aˣʸ.', '<strong>y = aˣ</strong> (a &gt; 0, a ≠ 1). A power with exponent zero is 1, with a negative one the reciprocal: a⁻ⁿ = 1/aⁿ, with a fractional one a root: a^(1/n) = ⁿ√a. The range is all positive numbers. Properties: aˣ · aʸ = aˣ⁺ʸ, (aˣ)ʸ = aˣʸ.'),
    ('aˣ · aʸ = aˣ⁺ʸ', '', 'aˣ · aʸ = aˣ⁺ʸ'), m1),
  S('growth', 'Рост и распад', 'Growth and decay', ('Если величина умножается на одно и то же число за равные промежутки времени, она меняется по показательному закону: N(t) = N₀ · 2^(t/T) — удвоение за период T; N(t) = N₀ · 2^(−t/T) — полураспад. Так моделируют размножение бактерий, радиоактивный распад, сложные проценты, но только при условиях, когда модель выполняется.', 'If a quantity is multiplied by the same number over equal time intervals it changes exponentially: N(t) = N₀ · 2^(t/T) — doubling every period T; N(t) = N₀ · 2^(−t/T) — a half-life. This models bacterial growth, radioactive decay and compound interest — but only while the model holds.'),
    ('N = N₀·2^(t/T)', '', 'N = N₀·2^(t/T)'), m2),
  S('e', 'Число e', 'The number e', ('Предел (1 + 1/n)ⁿ при n → ∞ — число <strong>e ≈ 2,71828</strong>, как π, иррациональное. Показательная функция eˣ особенна: скорость её роста в каждой точке равна самому значению. Поэтому её используют в уравнениях роста, охлаждения, разряда конденсатора.', 'The limit of (1 + 1/n)ⁿ as n → ∞ is the number <strong>e ≈ 2.71828</strong>, irrational like π. The exponential eˣ is special: its rate of growth at each point equals its own value. This is why it appears in equations of growth, cooling and capacitor discharge.'),
    ('e ≈ 2,71828', '', 'e ≈ 2.71828'), m3)],
 [TK(('Значение', 'Value'), ('Найдите 2⁻³ и 8^(1/3).', 'Find 2⁻³ and 8^(1/3).'), '', '2⁻³ = 1/8; 8^(1/3) = 2.', ('1/8 и 2.', '1/8 and 2.')),
  TK(('Свойства', 'Properties'), ('Упростите 3⁵ · 3⁻² и (2³)².', 'Simplify 3⁵ · 3⁻² and (2³)².'), '', '3³ = 27; 2⁶ = 64.', '27; 64.'),
  TK(('Рост', 'Growth'), ('Колония из 100 клеток удваивается каждый час. Сколько клеток через 5 часов?', 'A colony of 100 cells doubles every hour. How many cells after 5 hours?'), '', '100 · 2⁵ = 3200.', ('3 200.', '3,200.')),
  TK(('Полураспад', 'Half-life'), ('Период полураспада 4 суток. Сколько останется от 80 г через 12 суток?', 'The half-life is 4 days. How much remains of 80 g after 12 days?'), '12 : 4 = 3', '80 · (1/2)³ = 10 г.', '10 г.'),
  TK(('Сравнить', 'Compare'), ('Что больше: 2¹⁰ или 10²?', 'Which is larger: 2¹⁰ or 10²?'), '', '2¹⁰ = 1024 > 100.', '2¹⁰.')],
 [Q('a⁰ (a ≠ 0) =', 'a⁰ (a ≠ 0) =', '1', '0', 'a', ('По определению.', 'By definition.')),
  Q('2⁻² =', '2⁻² =', '1/4', '−4', '4', ('1/2².', '1/2².')),
  Q('Функция y = (1/2)ˣ', 'The function y = (1/2)ˣ', ('убывает', 'is decreasing'), ('возрастает', 'is increasing'), ('постоянна', 'is constant'), ('0 < a < 1.', '0 < a < 1.')),
  Q('2ˣ · 2³ =', '2ˣ · 2³ =', '2ˣ⁺³', '4ˣ⁺³', '2³ˣ', ('Показатели складываются.', 'Exponents add.')),
  Q('Может ли aˣ быть отрицательным (a > 0)?', 'Can aˣ be negative (a > 0)?', ('нет', 'no'), ('да', 'yes'), ('при x < 0', 'when x < 0'), ('Положительная функция.', 'A positive function.')),
  Q('Через какую точку проходит график aˣ?', 'Through which point does the graph of aˣ pass?', '(0; 1)', '(1; 0)', '(0; 0)', ('a⁰ = 1.', 'a⁰ = 1.')),
  Q('Число e приблизительно', 'The number e is about', '2,718', '3,14', '1,414', ('e ≈ 2,718.', 'e ≈ 2.718.')),
  Q('Удвоение каждые 2 часа. За 6 часов количество', 'Doubling every 2 hours. In 6 hours the amount', ('вырастет в 8 раз', 'grows 8 times'), ('вырастет в 6 раз', 'grows 6 times'), ('вырастет в 4 раза', 'grows 4 times'), ('2³ = 8.', '2³ = 8.'))],
 src=[('Wikipedia: Exponential function', 'https://en.wikipedia.org/wiki/Exponential_function'), ('Wikipedia: E (mathematical constant)', 'https://en.wikipedia.org/wiki/E_(mathematical_constant)'), ('OpenStax: Algebra and Trigonometry 2e', 'https://openstax.org/details/books/algebra-and-trigonometry-2e')],
 note=('Условия «подарка» и числа в моделях придуманы.', 'The “gift” terms and the numbers in the models are invented.'))
