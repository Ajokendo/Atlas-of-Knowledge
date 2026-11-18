# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Решение aˣ = b', 'Solving aˣ = b'),
 [('r', 'a', 'Основание a', 'Base a', 2, 5, 1, 2), ('r', 'b', 'Значение b', 'Value b', 1, 100, 1, 20)],
 [('x = logₐ b', 'x = logₐ b'), ('Проверка aˣ', 'Check aˣ'), ('Целое решение?', 'Whole solution?')],
 'Уравнение aˣ = b решается логарифмированием: x = logₐ b. Решение есть только при b &gt; 0.', 'The equation aˣ = b is solved by taking a logarithm: x = logₐ b. A solution exists only for b &gt; 0.', ('Пересечение aˣ и прямой y = b', 'Intersection of aˣ and the line y = b'),
 r'''const x=Math.log(v.b)/Math.log(v.a),G=Gr({x0:-1,x1:7,y0:0,y1:Math.max(v.b*1.3,10),L:90,T:10,W:450,H:210});let g=G.grid(1,Math.max(5,Math.round(v.b/4)))+G.fn(t=>Math.pow(v.a,t),COL.a,3.5,-1,7)+G.fn(t=>v.b,COL.b,2,-1,7,true)+G.pt(x,v.b,COL.c,8);
 return {svg:g,st:[fnum(x,4),fnum(Math.pow(v.a,x),3),Math.abs(x-Math.round(x))<1e-9?U("да","yes"):U("нет","no")],fb:U("Точка пересечения — решение: показатель, при котором aˣ достигает b.","The intersection is the solution: the exponent at which aˣ reaches b.")}''', '0 0 600 250')

m2 = M(('Время удвоения', 'Doubling time'),
 [('r', 'p', 'Рост за период, %', 'Growth per period, %', 1, 50, 1, 7), ('r', 'k', 'Во сколько раз вырасти', 'Growth factor wanted', 2, 10, 1, 2)],
 [('Число периодов n', 'Number of periods n'), ('Формула', 'Formula'), ('Проверка', 'Check')],
 'Если величина растёт на p % за период, то (1 + p/100)ⁿ = k, откуда n = log(k) / log(1 + p/100). Условный пример, не финансовый совет.', 'If a quantity grows by p % per period then (1 + p/100)ⁿ = k, so n = log(k) / log(1 + p/100). An illustrative example, not financial advice.', ('Сколько периодов нужно для роста', 'How many periods growth takes'),
 r'''const r=1+v.p/100,n=Math.log(v.k)/Math.log(r),G=Gr({x0:0,x1:Math.max(n*1.5,10),y0:0,y1:v.k*1.4,L:90,T:10,W:450,H:210});let g=G.grid(Math.max(1,Math.round(n/3)),1)+G.fn(t=>Math.pow(r,t),COL.a,3.5,0,Math.max(n*1.5,10))+G.fn(t=>v.k,COL.b,2,0,Math.max(n*1.5,10),true)+G.pt(n,v.k,COL.c,8);
 return {svg:g,st:[fnum(n,2),"n = ln "+v.k+" / ln "+fnum(r,3),fnum(Math.pow(r,n),3)],fb:U("«Правило 70»: удвоение занимает около 70/p периодов.","The “rule of 70”: doubling takes about 70/p periods.")}''', '0 0 600 250')

m3 = M(('Полураспад: сколько ждать', 'Half-life: how long to wait'),
 [('r', 'T', 'Период полураспада T, сут', 'Half-life T, days', 1, 30, 1, 8), ('r', 'f', 'Осталось, % от начала', 'Remaining, % of start', 1, 99, 1, 10)],
 [('Время t, сут', 'Time t, days'), ('Число периодов', 'Number of periods'), ('Формула', 'Formula')],
 'Из (1/2)^(t/T) = f получаем t = T · log₂(1/f). Чем меньше осталось, тем дольше ждать — и никогда не станет ровно ноль.', 'From (1/2)^(t/T) = f we get t = T · log₂(1/f). The less remains, the longer the wait — and it never reaches exactly zero.', ('Кривая распада', 'The decay curve'),
 r'''const f=v.f/100,t=v.T*Math.log(1/f)/Math.LN2,mx=Math.max(t*1.4,v.T*3),G=Gr({x0:0,x1:mx,y0:0,y1:1.1,L:90,T:10,W:450,H:210});let g=G.grid(Math.max(1,Math.round(mx/5)),0.25)+G.fn(x=>Math.pow(0.5,x/v.T),COL.a,3.5,0,mx)+G.fn(x=>f,COL.b,2,0,mx,true)+G.pt(t,f,COL.c,8);
 return {svg:g,st:[fnum(t,2),fnum(t/v.T,3),"t = T·log₂(1/f)"],fb:U("Условная модель: подставьте период полураспада реального вещества из справочника.","An illustrative model: use a real substance’s half-life from a reference.")}''', '0 0 600 250')

chapter('55', '55-exp-log-equations.html', 'VII', ('Показательные и логарифмические уравнения', 'Exponential and logarithmic equations'),
 ('Как решать уравнения, где неизвестное в показателе или под знаком логарифма.', 'How to solve equations with the unknown in an exponent or under a logarithm.'),
 ('Лекарство выводится из организма так, что его количество каждые 6 часов уменьшается вдвое (условно). Через сколько часов останется 10 % от первоначальной дозы?', 'A medicine leaves the body so that its amount halves every 6 hours (illustratively). After how many hours does 10 % of the first dose remain?'),
 ('Разгадка: около 20 часов', 'The answer: about 20 hours'),
 ('Нужно (1/2)^(t/6) = 0,1. Берём логарифм: t/6 = log₂ 10 ≈ 3,32, значит t ≈ 19,9 ч. Неизвестное в показателе «достаётся» только логарифмированием. Реальные сроки зависят от вещества и организма — это учебная модель, не медицинский совет.', 'We need (1/2)^(t/6) = 0.1. Take a logarithm: t/6 = log₂ 10 ≈ 3.32, so t ≈ 19.9 h. An unknown in the exponent is reached only by a logarithm. Real times depend on the substance and the body — this is a teaching model, not medical advice.'),
 [S('exp', 'Показательные уравнения', 'Exponential equations', ('Если основания приводятся к одинаковым: aᶠ = aᵍ ⇒ f = g, например 2ˣ = 32 ⇒ x = 5. Иначе логарифмируют: aˣ = b ⇒ x = logₐ b. Часто помогает замена t = aˣ: 4ˣ − 3·2ˣ + 2 = 0 → t² − 3t + 2 = 0 (t &gt; 0).', 'If the bases can be made equal: aᶠ = aᵍ ⇒ f = g, e.g. 2ˣ = 32 ⇒ x = 5. Otherwise take logarithms: aˣ = b ⇒ x = logₐ b. A substitution t = aˣ often helps: 4ˣ − 3·2ˣ + 2 = 0 → t² − 3t + 2 = 0 (t &gt; 0).'),
    ('aˣ = b ⇒ x = logₐ b', '', 'aˣ = b ⇒ x = logₐ b'), m1),
  S('log', 'Логарифмические уравнения', 'Logarithmic equations', ('logₐ f = logₐ g ⇒ f = g, но только при f &gt; 0 и g &gt; 0. <strong>Обязательно проверяйте область определения</strong>: log₂(x − 1) + log₂(x + 1) = 3 даёт x² − 1 = 8, x = ±3, но x = −3 не подходит — под логарифмом отрицательное число.', 'logₐ f = logₐ g ⇒ f = g, but only when f &gt; 0 and g &gt; 0. <strong>Always check the domain</strong>: log₂(x − 1) + log₂(x + 1) = 3 gives x² − 1 = 8, x = ±3, but x = −3 is rejected — the logarithm would get a negative number.'),
    ('logₐ f = logₐ g ⇒ f = g > 0', '', 'logₐ f = logₐ g ⇒ f = g > 0'), m2),
  S('app', 'Приложения', 'Applications', ('Время роста или распада всегда ищется через логарифм: <strong>t = T · log₂(1/f)</strong> для полураспада и <strong>n = ln k / ln(1 + p/100)</strong> для роста. Показатели pH, децибелы и магнитуда — те же логарифмы.', 'The time of growth or decay is always found with a logarithm: <strong>t = T · log₂(1/f)</strong> for half-life and <strong>n = ln k / ln(1 + p/100)</strong> for growth. pH, decibels and magnitude are the same logarithms.'),
    ('t = T · log₂(1/f)', '', 't = T · log₂(1/f)'), m3)],
 [TK(('Одинаковые основания', 'Equal bases'), ('Решите 2ˣ = 32 и 3ˣ⁻¹ = 9.', 'Solve 2ˣ = 32 and 3ˣ⁻¹ = 9.'), '', 'x = 5; x − 1 = 2, x = 3.', ('5 и 3.', '5 and 3.')),
  TK(('Логарифмирование', 'Logarithms'), ('Решите 3ˣ = 20 (ответ с точностью до 0,01).', 'Solve 3ˣ = 20 (to 0.01).'), '', 'x = ln 20 / ln 3 ≈ 2,73.', '≈ 2.73.'),
  TK(('Замена', 'Substitution'), ('Решите 4ˣ − 3·2ˣ + 2 = 0.', 'Solve 4ˣ − 3·2ˣ + 2 = 0.'), 't = 2ˣ', 't² − 3t + 2 = 0: t = 1, 2 → x = 0 или x = 1.', ('x = 0 и x = 1.', 'x = 0 and x = 1.')),
  TK(('Логарифмическое', 'Logarithmic'), ('Решите log₂(x + 1) = 4.', 'Solve log₂(x + 1) = 4.'), '', 'x + 1 = 16, x = 15.', 'x = 15.'),
  TK(('Область определения', 'Domain'), ('Решите log₂(x − 1) + log₂(x + 1) = 3.', 'Solve log₂(x − 1) + log₂(x + 1) = 3.'), 'x² − 1 = 8', 'x = ±3; при x = −3 логарифмы не определены. Ответ: x = 3.', ('x = 3.', 'x = 3.'))],
 [Q('2ˣ = 16. x =', '2ˣ = 16. x =', '4', '8', '2', ('2⁴ = 16.', '2⁴ = 16.')),
  Q('aˣ = b решается', 'aˣ = b is solved by', ('логарифмированием', 'taking a logarithm'), ('делением', 'division'), ('извлечением корня', 'taking a root'), ('x = logₐ b.', 'x = logₐ b.')),
  Q('Решения 2ˣ = −4', 'Solutions of 2ˣ = −4', ('нет', 'none'), ('x = −2', 'x = −2'), ('x = 2', 'x = 2'), ('aˣ > 0.', 'aˣ > 0.')),
  Q('log₂ x = 3. x =', 'log₂ x = 3. x =', '8', '6', '9', ('2³ = 8.', '2³ = 8.')),
  Q('Что нужно проверить в логарифмическом уравнении?', 'What must be checked in a logarithmic equation?', ('область определения', 'the domain'), ('чётность', 'parity'), ('период', 'the period'), ('Аргумент > 0.', 'The argument > 0.')),
  Q('Полураспад 5 суток. Через 10 суток останется', 'Half-life 5 days. After 10 days remains', '1/4', '1/2', '1/10', ('Два периода.', 'Two periods.')),
  Q('3ˣ = 1. x =', '3ˣ = 1. x =', '0', '1', '3', ('3⁰ = 1.', '3⁰ = 1.')),
  Q('Замена t = 2ˣ требует', 'The substitution t = 2ˣ requires', ('t > 0', 't > 0'), ('t < 0', 't < 0'), ('t = 0', 't = 0'), ('Показательная функция положительна.', 'The exponential is positive.'))],
 src=[('Wikipedia: Exponential decay', 'https://en.wikipedia.org/wiki/Exponential_decay'), ('Wikipedia: Half-life', 'https://en.wikipedia.org/wiki/Half-life'), ('OpenStax: Algebra and Trigonometry 2e', 'https://openstax.org/details/books/algebra-and-trigonometry-2e')],
 note=('Сюжеты про лекарство и проценты роста условные; не медицинский и не финансовый совет.', 'The medicine and growth-rate stories are illustrative; not medical or financial advice.'))
