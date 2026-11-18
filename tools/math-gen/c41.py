# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Квадрат и его сторона', 'A square and its side'),
 [('r', 'S', 'Площадь квадрата', 'Area of the square', 1, 100, 1, 25)],
 [('Сторона √S', 'Side √S'), ('Идеальный квадрат?', 'A perfect square?'), ('Между числами', 'Between the numbers')],
 'Квадратный корень из S — сторона квадрата площадью S. Не любая площадь даёт целую сторону.', 'The square root of S is the side of a square of area S. Not every area gives a whole side.', ('Квадрат площадью S', 'A square of area S'),
 r'''const s=Math.sqrt(v.S),k=Math.min(180/s,30);let g=R(300-s*k/2,20,s*k,s*k,"#f4dfd8",COL.ink,3)+TX(300,20+s*k/2+6,"S = "+v.S,COL.a,20,"middle",700)+TX(300,20+s*k+20,"√"+v.S+" ≈ "+fnum(s,3),COL.b,14);
 const fl=Math.floor(s),perf=fl*fl===v.S;return {svg:g,st:[fnum(s,4),perf?U("да: "+fl+"²","yes: "+fl+"²"):U("нет","no"),perf?"√"+v.S+" = "+fl:fl+" < √"+v.S+" < "+(fl+1)],fb:perf?U("√"+v.S+" = "+fl+" — целое.","√"+v.S+" = "+fl+" — an integer."):U("Корень не целый: он лежит между "+fl+" и "+(fl+1)+".","The root is not an integer: it lies between "+fl+" and "+(fl+1)+".")}''', '0 0 600 235')

m2 = M(('Деление отрезка: приближение корня', 'Bisection: approximating a root'),
 [('r', 'n', 'Число n', 'Number n', 2, 50, 1, 2), ('r', 'st', 'Шагов деления пополам', 'Bisection steps', 0, 8, 1, 4)],
 [('Интервал', 'Interval'), ('Длина интервала', 'Interval length'), ('Настоящее значение', 'True value')],
 'Корень лежит между двумя числами. Делим интервал пополам и оставляем половину с корнем. Каждый шаг уточняет значение вдвое.', 'The root lies between two numbers. We halve the interval and keep the half containing the root. Each step doubles the accuracy.', ('Сужение интервала на числовой прямой', 'Narrowing the interval on the number line'),
 r'''let lo=Math.floor(Math.sqrt(v.n)),hi=lo+1;for(let i=0;i<v.st;i++){const m=(lo+hi)/2;if(m*m<=v.n)lo=m;else hi=m}
 const base=Math.floor(Math.sqrt(v.n)),X=t=>40+(t-base)*520;let g=L(40,100,560,100,COL.ink,3)+TX(40,130,base,COL.mut,14)+TX(560,130,base+1,COL.mut,14);
 g+=R(X(lo),88,Math.max(2,X(hi)-X(lo)),24,"#e1f0e8",COL.c,2,3)+C(X(Math.sqrt(v.n)),100,6,COL.a)+TX(X(Math.sqrt(v.n)),70,"√"+v.n,COL.a,14,"middle",700);
 return {svg:g,st:["["+fnum(lo,5)+"; "+fnum(hi,5)+"]",fnum(hi-lo,5),fnum(Math.sqrt(v.n),6)],fb:U("После "+v.st+" шагов длина интервала 1/2^"+v.st+" = "+fnum(1/Math.pow(2,v.st),5)+".","After "+v.st+" steps the interval length is 1/2^"+v.st+" = "+fnum(1/Math.pow(2,v.st),5)+".")}''', '0 0 600 160')

m3 = M(('Иррациональные числа', 'Irrational numbers'),
 [('r', 'n', 'Число n', 'Number n', 2, 60, 1, 2)],
 [('√n', '√n'), ('Рациональное?', 'Rational?'), ('Десятичная запись', 'Decimal notation')],
 'Если n — не квадрат целого числа, то √n — иррациональное число: бесконечная десятичная дробь без повторяющейся группы цифр.', 'If n is not the square of an integer then √n is irrational: an infinite decimal with no repeating group of digits.', ('Цифры корня', 'The digits of the root'),
 r'''const s=Math.sqrt(v.n),fl=Math.floor(s),perf=fl*fl===v.n;let digs=String(Math.round(s*1e10)).padStart(11,"0");let g="";
 let txt=perf?String(fl):(String(fl)+","+digs.slice(-10).replace(/^(\d{10}).*/,"$1"));g+=TX(300,70,"√"+v.n+" =",COL.mut,20)+TX(300,125,txt+(perf?"":"…"),perf?COL.c:COL.a,30,"middle",700)+TX(300,175,perf?U("целое число","an integer"):U("цифры не повторяются по периоду","no repeating period"),COL.ink,15);
 return {svg:g,st:[perf?fl:fnum(s,6),perf?U("да (целое)","yes (integer)"):U("нет, иррациональное","no, irrational"),perf?fl+"":fl+","+digs.slice(-10).slice(0,6)+"…"],fb:perf?U("n = "+fl+"² — идеальный квадрат.","n = "+fl+"² — a perfect square."):U("Все цифры показаны с точностью калькулятора; настоящие ещё бесконечно продолжаются.","The digits are shown to calculator precision; the real ones continue forever.")}''', '0 0 600 205')

chapter('41', '41-square-roots.html', 'VI', ('Квадратный корень и иррациональные числа', 'Square roots and irrational numbers'),
 ('Что такое квадратный корень, как его оценить и почему √2 нельзя записать дробью.', 'What a square root is, how to estimate it and why √2 cannot be written as a fraction.'),
 ('Квадратный участок площадью 2 га нужно обнести забором.\n\nКакой длины сторона и можно ли выразить её точной дробью?', 'A square plot of area 2 hectares needs a fence.\n\nWhat is the length of its side and can it be expressed as an exact fraction?'),
 ('Разгадка: √2 ≈ 1,414…, точной дроби нет', 'The answer: √2 ≈ 1.414…, no exact fraction'),
 ('Сторона квадрата площадью S равна √S. Для S = 2 получаем √2 ≈ 1,41421356… Сколько бы цифр мы ни выписали, они не заканчиваются и не повторяются периодом. Древние греки доказали: никакая дробь m/n в квадрате не равна 2. Такие числа назвали иррациональными. Они заполняют числовую прямую вместе с рациональными, образуя действительные числа.', 'The side of a square of area S is √S. For S = 2 we get √2 ≈ 1.41421356… However many digits we write they never end and never repeat with a period. The ancient Greeks proved: no fraction m/n squared equals 2. Such numbers are called irrational. They fill the number line together with the rationals, forming the real numbers.'),
 [S('root', 'Квадратный корень', 'The square root', ('<strong>Арифметический квадратный корень</strong> числа a ≥ 0 — неотрицательное число, квадрат которого равен a: √9 = 3 (а не −3). Из отрицательного числа корень не извлекается. Квадратный корень из S — сторона квадрата площадью S. Всегда √(a²) = |a|.', 'The <strong>arithmetic square root</strong> of a number a ≥ 0 is the non-negative number whose square is a: √9 = 3 (not −3). The square root of a negative number does not exist among the reals. The square root of S is the side of a square of area S. Always √(a²) = |a|.'),
    ('√(a²) = |a|', '', '√(a²) = |a|'), m1),
  S('approx', 'Оценка корня', 'Estimating a root', ('Чтобы оценить √n, находят соседние квадраты: 25 &lt; 30 &lt; 36, значит 5 &lt; √30 &lt; 6. Затем уточняют, например, делением промежутка пополам (метод бисекции). Правила: √(ab) = √a · √b; √(a/b) = √a / √b (a, b ≥ 0); сумма корней не равна корню суммы: √9 + √16 = 7, а √25 = 5.', 'To estimate √n we find neighbouring squares: 25 &lt; 30 &lt; 36, so 5 &lt; √30 &lt; 6. Then refine, for instance by halving the interval (bisection). Rules: √(ab) = √a · √b; √(a/b) = √a / √b (a, b ≥ 0); the sum of roots is not the root of the sum: √9 + √16 = 7 but √25 = 5.'),
    ('√(ab) = √a · √b', '', '√(ab) = √a · √b'), m2),
  S('irr', 'Иррациональные числа', 'Irrational numbers', ('<strong>Рациональные</strong> числа — это дроби m/n; их десятичная запись конечна или периодична. <strong>Иррациональные</strong> (√2, √3, π) — бесконечные непериодические дроби. Вместе они образуют <strong>действительные</strong> числа. √n иррационален, если n — не квадрат натурального числа.', '<strong>Rational</strong> numbers are fractions m/n; their decimal notation is finite or periodic. <strong>Irrational</strong> numbers (√2, √3, π) are infinite non-periodic decimals. Together they form the <strong>real</strong> numbers. √n is irrational if n is not the square of a natural number.'),
    ('ℚ ∪ иррациональные = ℝ', '', 'ℚ ∪ irrationals = ℝ'), m3)],
 [TK(('Значение', 'Value'), ('Найдите √144 и √0,25.', 'Find √144 and √0.25.'), '', '12 и 0,5.', '12; 0,5.'),
  TK(('Оценка', 'Estimate'), ('Между какими целыми числами √50?', 'Between which integers is √50?'), '49 &lt; 50 &lt; 64', '7 &lt; √50 &lt; 8.', '7 &lt; √50 &lt; 8.'),
  TK(('Свойство', 'Property'), ('Упростите √12.', 'Simplify √12.'), '12 = 4 · 3', '√4 · √3 = 2√3.', '2√3.'),
  TK(('Модуль', 'Absolute value'), ('Найдите √((−7)²).', 'Find √((−7)²).'), '', '√49 = 7.', '7.'),
  TK(('Рациональное?', 'Rational?'), ('Рационально ли √16? А √17?', 'Is √16 rational? And √17?'), '', '√16 = 4 — рациональное; 17 не квадрат — √17 иррационально.', ('√16 — да; √17 — нет.', '√16 — yes; √17 — no.'))],
 [Q('√81 =', '√81 =', '9', '−9', '40,5', ('9² = 81.', '9² = 81.')),
  Q('√(−4) среди действительных', '√(−4) among the reals', ('не существует', 'does not exist'), ('равен 2', 'equals 2'), ('равен −2', 'equals −2'), ('Квадрат не бывает отрицательным.', 'A square is never negative.')),
  Q('√2 — число', '√2 is a', ('иррациональное', 'irrational number'), ('целое', 'whole number'), ('рациональное', 'rational number'), ('Нет точной дроби.', 'There is no exact fraction.')),
  Q('√(a²) =', '√(a²) =', '|a|', 'a', '−a', ('Корень неотрицателен.', 'The root is non-negative.')),
  Q('Между какими числами √20?', 'Between which numbers is √20?', '4 и 5', '3 и 4', '5 и 6', ('16 < 20 < 25.', '16 < 20 < 25.')),
  Q('√(9 · 4) =', '√(9 · 4) =', '6', '5', '13', ('3 · 2.', '3 · 2.')),
  Q('Верно ли √9 + √16 = √25?', 'Is √9 + √16 = √25 true?', ('нет: 7 ≠ 5', 'no: 7 ≠ 5'), ('да', 'yes'), ('иногда', 'sometimes'), ('Корень суммы не равен сумме корней.', 'The root of a sum is not the sum of roots.')),
  Q('Десятичная запись иррационального числа', 'The decimal notation of an irrational number is', ('бесконечная непериодическая', 'infinite non-periodic'), ('конечная', 'finite'), ('периодическая', 'periodic'), ('Определение.', 'The definition.'))],
 src=[('Wikipedia: Square root', 'https://en.wikipedia.org/wiki/Square_root'), ('Wikipedia: Irrational number', 'https://en.wikipedia.org/wiki/Irrational_number'), ('Wikipedia: Square root of 2', 'https://en.wikipedia.org/wiki/Square_root_of_2')],
 note=('Участок в загадке придуман.', 'The plot in the puzzle is made up.'))
