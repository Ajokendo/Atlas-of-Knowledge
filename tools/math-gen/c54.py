# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Логарифм как показатель', 'A logarithm as an exponent'),
 [('r', 'a', 'Основание a', 'Base a', 2, 10, 1, 2), ('r', 'y', 'Число b', 'Number b', 1, 1000, 1, 8)],
 [('logₐ b', 'logₐ b'), ('Проверка: a^(лог.)', 'Check: a^(log)'), ('Целая степень?', 'Whole power?')],
 'Логарифм logₐ b — это показатель степени, в которую нужно возвести a, чтобы получить b.', 'The logarithm logₐ b is the exponent to which a must be raised to get b.', ('Шкала степеней основания', 'A scale of powers of the base'),
 r'''const L0=Math.log(v.y)/Math.log(v.a),mx=Math.max(4,Math.ceil(L0)+1);let g=L(40,90,560,90,COL.ink,2);for(let k=0;k<=mx&&k<=8;k++){const x=40+k*(520/Math.min(mx,8));g+=L(x,82,x,98,COL.ink,2)+TX(x,120,String(k),COL.mut,13,"middle",600)}
 const xp=40+Math.min(L0,Math.min(mx,8))*(520/Math.min(mx,8));g+=C(xp,90,8,COL.b)+TX(xp,60,"log = "+fnum(L0,3),COL.b,15,"middle",700);
 const isInt=Math.abs(L0-Math.round(L0))<1e-9;
 return {svg:g,st:[fnum(L0,4),fnum(Math.pow(v.a,L0),3),isInt?U("да","yes"):U("нет","no")],fb:U("log"+v.a+" "+v.y+" — показатель: "+v.a+" в степени "+fnum(L0,3)+" даёт "+v.y+".","log"+v.a+" "+v.y+" is the exponent: "+v.a+" to the power "+fnum(L0,3)+" gives "+v.y+".")}''', '0 0 600 140')

m2 = M(('График логарифма', 'The graph of a logarithm'),
 [('r', 'a', 'Основание a', 'Base a', 1.5, 8, 0.5, 2), ('r', 'x', 'Аргумент x', 'Argument x', 0.1, 10, 0.1, 4)],
 [('logₐ x', 'logₐ x'), ('Обратная aˣ', 'Inverse aˣ'), ('Область определения', 'Domain')],
 'График логарифма — зеркальное отражение графика aˣ относительно прямой y = x. Он определён только при x &gt; 0.', 'The graph of a logarithm is the mirror image of the graph of aˣ in the line y = x. It is defined only for x &gt; 0.', ('Логарифм и показательная функция', 'Logarithm and exponential'),
 r'''const G=Gr({x0:-3,x1:10,y0:-3,y1:6,L:70,T:10,W:470,H:210});const ly=Math.log(v.x)/Math.log(v.a);let g=G.grid(1,1)+G.fn(t=>Math.pow(v.a,t),COL.b,2.5,-3,10)+G.fn(t=>t,COL.mut,1.5,-3,6,true)+G.fn(t=>Math.log(t)/Math.log(v.a),COL.a,3.5,0.02,10)+G.pt(v.x,ly,COL.c,8);
 return {svg:g,st:[fnum(ly,4),fnum(Math.pow(v.a,ly),4)+" = x","x > 0"],fb:U("Логарифм и показательная функция «отменяют» друг друга.","The logarithm and the exponential “undo” each other.")}''', '0 0 600 250')

m3 = M(('Свойства логарифмов', 'Properties of logarithms'),
 [('r', 'm', 'Число m', 'Number m', 1, 100, 1, 8), ('r', 'n', 'Число n', 'Number n', 1, 100, 1, 4)],
 [('log₂(m·n)', 'log₂(m·n)'), ('log₂ m + log₂ n', 'log₂ m + log₂ n'), ('log₂(m/n) = log₂ m − log₂ n', 'log₂(m/n) = log₂ m − log₂ n')],
 'Логарифм превращает умножение в сложение, а деление — в вычитание. Раньше на этом строились логарифмические линейки.', 'A logarithm turns multiplication into addition and division into subtraction. Slide rules were once built on this.', ('Сложение длин вместо умножения', 'Adding lengths instead of multiplying'),
 r'''const l2=x=>Math.log(x)/Math.LN2,a=l2(v.m),b=l2(v.n),sc=500/Math.max(a+b,1);let g=R(50,40,a*sc,34,COL.a,COL.ink,1.5,2)+R(50+a*sc,40,b*sc,34,COL.b,COL.ink,1.5,2)+TX(50+a*sc/2,62,"log₂ "+v.m,COL.bg,13,"middle",700)+TX(50+a*sc+b*sc/2,62,"log₂ "+v.n,COL.bg,13,"middle",700)+TX(300,120,"log₂("+v.m+"·"+v.n+") = "+fnum(a+b,3),COL.ink,18,"middle",700);
 return {svg:g,st:[fnum(l2(v.m*v.n),4),fnum(a+b,4),fnum(l2(v.m/v.n),4)+" = "+fnum(a-b,4)],fb:U("Длины отрезков складываются — это и есть логарифм произведения.","The lengths add up — that is the logarithm of the product.")}''', '0 0 600 150')

chapter('54', '54-logarithms.html', 'VII', ('Логарифмы', 'Logarithms'),
 ('Логарифм как показатель степени, его график и три главных свойства.', 'A logarithm as an exponent, its graph and the three main properties.'),
 ('Землетрясение в 6 баллов магнитуды выделяет энергии не в 6, а примерно в миллионы раз больше, чем слабое в 2 балла. Почему шкала сделана так, что числа маленькие, а различия огромные?', 'A magnitude-6 earthquake releases not 6 times but millions of times more energy than a weak one of magnitude 2. Why is the scale built so that the numbers are small but the differences huge?'),
 ('Разгадка: шкала логарифмическая', 'The answer: the scale is logarithmic'),
 ('Магнитуда — логарифм измеренной величины: рост на единицу означает, что амплитуда колебаний вырастает в 10 раз (энергия — примерно в 32 раза). Поэтому разница в 4 единицы — это 10⁴ = 10 000 раз по амплитуде и около 10⁶ по энергии. Логарифмические шкалы используют там, где величины различаются в миллионы раз: магнитуда, децибелы, pH.', 'Magnitude is a logarithm of the measured quantity: one unit means the amplitude grows 10 times (energy about 32 times). So a 4-unit difference is 10⁴ = 10,000 times in amplitude and about 10⁶ in energy. Logarithmic scales are used where quantities differ by millions: magnitude, decibels, pH.'),
 [S('def', 'Что такое логарифм', 'What a logarithm is', ('<strong>logₐ b = x</strong> означает aˣ = b (a &gt; 0, a ≠ 1, b &gt; 0). Например, log₂ 8 = 3, потому что 2³ = 8; log₁₀ 1000 = 3. Основное логарифмическое тождество: a^(logₐ b) = b. Десятичный логарифм lg b — по основанию 10, натуральный ln b — по основанию e.', '<strong>logₐ b = x</strong> means aˣ = b (a &gt; 0, a ≠ 1, b &gt; 0). For example log₂ 8 = 3 because 2³ = 8; log₁₀ 1000 = 3. The basic identity: a^(logₐ b) = b. The common logarithm lg b has base 10, the natural one ln b has base e.'),
    ('logₐ b = x ⇔ aˣ = b', '', 'logₐ b = x ⇔ aˣ = b'), m1),
  S('graph', 'График', 'The graph', ('Логарифмическая функция y = logₐ x — обратная к y = aˣ. Определена при x &gt; 0, проходит через (1; 0), при a &gt; 1 возрастает: медленно, но без предела. Ось y — вертикальная асимптота.', 'The logarithmic function y = logₐ x is the inverse of y = aˣ. It is defined for x &gt; 0, passes through (1; 0) and for a &gt; 1 increases slowly but without bound. The y-axis is a vertical asymptote.'),
    ('y = logₐ x,  x > 0', '', 'y = logₐ x,  x > 0'), m2),
  S('props', 'Свойства', 'Properties', ('<strong>logₐ(mn) = logₐ m + logₐ n</strong>; <strong>logₐ(m/n) = logₐ m − logₐ n</strong>; <strong>logₐ mᵖ = p · logₐ m</strong>. Формула перехода к другому основанию: logₐ b = lg b / lg a — так считают на калькуляторе.', '<strong>logₐ(mn) = logₐ m + logₐ n</strong>; <strong>logₐ(m/n) = logₐ m − logₐ n</strong>; <strong>logₐ mᵖ = p · logₐ m</strong>. Change of base: logₐ b = lg b / lg a — this is how a calculator computes it.'),
    ('logₐ(mn) = logₐ m + logₐ n', '', 'logₐ(mn) = logₐ m + logₐ n'), m3)],
 [TK(('Вычислить', 'Compute'), ('Найдите log₃ 81 и log₂ (1/8).', 'Find log₃ 81 and log₂ (1/8).'), '', '3⁴ = 81 → 4; 2⁻³ = 1/8 → −3.', ('4 и −3.', '4 and −3.')),
  TK(('Сумма', 'Sum'), ('Вычислите log₂ 8 + log₂ 4.', 'Compute log₂ 8 + log₂ 4.'), '', '= log₂ 32 = 5.', '5.'),
  TK(('Степень', 'Power'), ('Вычислите log₅ 25³.', 'Compute log₅ 25³.'), '', '3 · log₅ 25 = 3 · 2 = 6.', '6.'),
  TK(('Магнитуда', 'Magnitude'), ('Во сколько раз амплитуда при магнитуде 7 больше, чем при 5?', 'How many times larger is the amplitude at magnitude 7 than at 5?'), '', '10⁷⁻⁵ = 100.', ('В 100 раз.', '100 times.')),
  TK(('Область', 'Domain'), ('Для каких x определён log₂(x − 3)?', 'For which x is log₂(x − 3) defined?'), '', 'x − 3 > 0, значит x > 3.', 'x > 3.')],
 [Q('log₂ 8 =', 'log₂ 8 =', '3', '4', '2', ('2³ = 8.', '2³ = 8.')),
  Q('log₁₀ 1000 =', 'log₁₀ 1000 =', '3', '10', '100', ('10³ = 1000.', '10³ = 1000.')),
  Q('logₐ 1 =', 'logₐ 1 =', '0', '1', 'a', ('a⁰ = 1.', 'a⁰ = 1.')),
  Q('log₂ 4 + log₂ 8 =', 'log₂ 4 + log₂ 8 =', '5', '12', '32', ('log₂ 32.', 'log₂ 32.')),
  Q('log₂ x определён при', 'log₂ x is defined for', 'x > 0', 'любом x', 'x < 0', ('Аргумент положителен.', 'The argument is positive.')),
  Q('Логарифм и aˣ — это функции', 'Logarithm and aˣ are', ('взаимно обратные', 'inverse to each other'), ('одинаковые', 'identical'), ('противоположные', 'opposite'), ('Они «отменяют» друг друга.', 'They undo each other.')),
  Q('log₃ 3⁵ =', 'log₃ 3⁵ =', '5', '3', '15', ('Показатель степени.', 'The exponent.')),
  Q('Рост магнитуды на 1 даёт амплитуду', 'A rise of magnitude by 1 gives an amplitude', ('в 10 раз больше', '10 times larger'), ('на 1 больше', '1 larger'), ('в 2 раза больше', '2 times larger'), ('Логарифм по основанию 10.', 'A base-10 logarithm.'))],
 src=[('Wikipedia: Logarithm', 'https://en.wikipedia.org/wiki/Logarithm'), ('Wikipedia: Richter magnitude scale', 'https://en.wikipedia.org/wiki/Richter_magnitude_scale'), ('OpenStax: Algebra and Trigonometry 2e', 'https://openstax.org/details/books/algebra-and-trigonometry-2e')])
