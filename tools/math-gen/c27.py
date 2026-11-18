# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Квадрат суммы', 'The square of a sum'),
 [('r', 'a', 'Сторона a', 'Side a', 1, 9, 1, 5), ('r', 'b', 'Сторона b', 'Side b', 1, 9, 1, 3)],
 [('(a + b)²', '(a + b)²'), ('a² + 2ab + b²', 'a² + 2ab + b²'), ('Числа', 'Numbers')],
 'Большой квадрат со стороной a + b состоит из квадрата a², квадрата b² и двух прямоугольников ab.', 'A large square with side a + b consists of a square a², a square b² and two rectangles ab.', ('Квадрат, разрезанный на четыре части', 'A square cut into four parts'),
 r'''const u=Math.min(200/(v.a+v.b),30)*1.2,x0=40,y0=15,A=v.a*u,B=v.b*u;let g=R(x0,y0,A,A,"#f4dfd8",COL.ink,2)+R(x0+A,y0,B,A,"#fdf0c8",COL.ink,2)+R(x0,y0+A,A,B,"#fdf0c8",COL.ink,2)+R(x0+A,y0+A,B,B,"#dbe5f2",COL.ink,2)+TX(x0+A/2,y0+A/2+5,"a² = "+v.a*v.a,COL.a,15)+TX(x0+A+B/2,y0+A/2+5,"ab",COL.ink,15)+TX(x0+A/2,y0+A+B/2+5,"ab",COL.ink,15)+TX(x0+A+B/2,y0+A+B/2+5,"b²",COL.b,15);
 g+=TX(400,70,"(a + b)² = "+Math.pow(v.a+v.b,2),COL.ink,22,"start",700)+TX(400,110,"a² + 2ab + b²",COL.mut,18,"start")+TX(400,140,v.a*v.a+" + "+2*v.a*v.b+" + "+v.b*v.b+" = "+Math.pow(v.a+v.b,2),COL.c,18,"start",600);
 return {svg:g,st:["("+v.a+" + "+v.b+")² = "+Math.pow(v.a+v.b,2),v.a*v.a+" + "+2*v.a*v.b+" + "+v.b*v.b+" = "+(v.a*v.a+2*v.a*v.b+v.b*v.b),U("Не забывайте удвоенное произведение: (a + b)² ≠ a² + b²","Don't forget the double product: (a + b)² ≠ a² + b²")],fb:U("Ошибка «(a + b)² = a² + b²» теряет 2ab = "+2*v.a*v.b+".","The mistake “(a + b)² = a² + b²” loses 2ab = "+2*v.a*v.b+".")}''', '0 0 600 250')

m2 = M(('Разность квадратов', 'The difference of squares'),
 [('r', 'a', 'a', 'a', 2, 12, 1, 8), ('r', 'b', 'b', 'b', 1, 11, 1, 3)],
 [('a² − b²', 'a² − b²'), ('(a − b)(a + b)', '(a − b)(a + b)'), ('Быстрый счёт', 'Fast counting')],
 'Из большого квадрата вырезан малый — оставшийся «уголок» можно переложить в прямоугольник (a − b) × (a + b).', 'A small square is cut out of a large one — the remaining “L” can be rearranged into a rectangle (a − b) × (a + b).', ('Уголок и прямоугольник', 'The L-shape and the rectangle'),
 r'''const a=v.a,b=Math.min(v.b,a-1),u=150/a;let g=R(30,20,a*u,a*u,COL.b,COL.ink,2)+R(30+(a-b)*u,20,b*u,b*u,COL.bg,COL.ink,2,0);
 g+=TX(30+a*u/2,20+a*u/2+5,"a² − b²",COL.bg,16,"middle",700)+R(320,20,(a+b)*u*0.9,(a-b)*u*0.9,COL.b,COL.ink,2)+TX(320+(a+b)*u*0.45,20+(a-b)*u*0.45+5,"(a−b)(a+b)",COL.bg,15,"middle",700);
 return {svg:g,st:[a*a+" − "+b*b+" = "+(a*a-b*b),"("+a+" − "+b+")("+a+" + "+b+") = "+(a-b)*(a+b),"101·99 = 100² − 1 = 9999"],fb:U("Две записи дают одно число: "+(a*a-b*b)+".","Both notations give one number: "+(a*a-b*b)+".")}''', '0 0 600 210')

m3 = M(('Умножение двух двучленов', 'Multiplying two binomials'),
 [('r', 'p', 'p', 'p', -6, 6, 1, 2), ('r', 'q', 'q', 'q', -6, 6, 1, 3), ('r', 'x', 'x для проверки', 'x for the check', -5, 5, 1, 2)],
 [('(x + p)(x + q)', '(x + p)(x + q)'), ('x² + (p + q)x + pq', 'x² + (p + q)x + pq'), ('Проверка при выбранном x', 'Check at the chosen x')],
 'Каждый член первой скобки умножаем на каждый член второй. Сумма средних слагаемых даёт (p + q)x.', 'Each term of the first bracket is multiplied by each term of the second. The sum of the middle terms gives (p + q)x.', ('Таблица умножения', 'The multiplication table'),
 r'''const s=v.p+v.q,pr=v.p*v.q,ps=n=>n<0?"− "+(-n):"+ "+n,c=[["x²","q·x"],["p·x","pq"]];let g="";const lab=[["x·x = x²","x·"+v.q+" = "+v.q+"x"],[v.p+"·x = "+v.p+"x",v.p+"·"+v.q+" = "+pr]];
 for(let i=0;i<2;i++)for(let j=0;j<2;j++)g+=R(120+j*180,25+i*80,170,70,i===j?"#f4dfd8":"#fdf0c8",COL.ink,2,4)+TX(205+j*180,67+i*80,lab[i][j],COL.ink,15,"middle",600);
 g+=TX(205,18,"x",COL.ink,15)+TX(385,18,ps(v.q),COL.ink,15)+TX(100,67,"x",COL.ink,15,"end")+TX(100,147,ps(v.p),COL.ink,15,"end");
 const L0=(v.x+v.p)*(v.x+v.q),R0=v.x*v.x+s*v.x+pr;return {svg:g,st:["(x "+ps(v.p)+")(x "+ps(v.q)+")","x² "+ps(s)+"x "+ps(pr),L0+" = "+R0],fb:U("При x = "+v.x+" обе записи равны "+L0+".","At x = "+v.x+" both notations equal "+L0+".")}''', '0 0 600 210')

chapter('27', '27-polynomials.html', 'IV', ('Многочлены и формулы сокращённого умножения', 'Polynomials and special products'),
 ('Как складывать и умножать многочлены и почему (a + b)² и a² − b² раскрываются «по формуле».', 'How to add and multiply polynomials and why (a + b)² and a² − b² expand “by a formula”.'),
 ('Надо быстро в уме посчитать 101 · 99.\n\nКак, не выполняя умножение «в столбик»?', 'We need to calculate 101 · 99 quickly in our head.\n\nHow, without long multiplication?'),
 ('Разгадка: 9 999', 'The answer: 9,999'),
 ('Запишем 101 = 100 + 1 и 99 = 100 − 1. Тогда произведение — это (100 + 1)(100 − 1) = 100² − 1² = 10 000 − 1 = 9 999. Формула разности квадратов (a − b)(a + b) = a² − b² превращает трудное умножение в лёгкое вычитание.', 'Write 101 = 100 + 1 and 99 = 100 − 1. Then the product is (100 + 1)(100 − 1) = 100² − 1² = 10,000 − 1 = 9,999. The difference-of-squares formula (a − b)(a + b) = a² − b² turns hard multiplication into easy subtraction.'),
 [S('sq', 'Квадрат суммы и разности', 'The square of a sum and difference', ('<strong>Многочлен</strong> — сумма одночленов, например x² − 3x + 5. Складывая и вычитая многочлены, собирают подобные слагаемые. Квадрат суммы: (a + b)² = a² + 2ab + b²; квадрат разности: (a − b)² = a² − 2ab + b². Это хорошо видно на площади квадрата со стороной a + b.', 'A <strong>polynomial</strong> is a sum of monomials, for example x² − 3x + 5. When adding and subtracting polynomials we combine like terms. The square of a sum: (a + b)² = a² + 2ab + b²; of a difference: (a − b)² = a² − 2ab + b². It is visible on the area of a square with side a + b.'),
    ('(a ± b)² = a² ± 2ab + b²', '', '(a ± b)² = a² ± 2ab + b²'), m1),
  S('dif', 'Разность квадратов', 'The difference of squares', ('(a − b)(a + b) = a² − b². Из квадрата вырезали меньший, оставшийся «уголок» разрезаем и перекладываем в прямоугольник со сторонами a − b и a + b — площадь не изменилась. Формулу применяют и для счёта в уме, и для разложения на множители.', '(a − b)(a + b) = a² − b². A smaller square is cut out of a square; the remaining “L” is cut and rearranged into a rectangle with sides a − b and a + b — the area is unchanged. The formula is used both for mental arithmetic and for factorising.'),
    ('a² − b² = (a − b)(a + b)', '', 'a² − b² = (a − b)(a + b)'), m2),
  S('mul', 'Умножение многочленов', 'Multiplying polynomials', ('Чтобы умножить многочлен на многочлен, каждое слагаемое первого умножают на каждое слагаемое второго и собирают подобные: (x + 2)(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6. Проверка: подставьте любое число, например x = 1: 3 · 4 = 12 и 1 + 5 + 6 = 12.', 'To multiply a polynomial by a polynomial we multiply each term of the first by each term of the second and combine like terms: (x + 2)(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6. Check: substitute any number, for example x = 1: 3 · 4 = 12 and 1 + 5 + 6 = 12.'),
    ('(x+p)(x+q) = x² + (p+q)x + pq', '', '(x+p)(x+q) = x² + (p+q)x + pq')
    , m3)],
 [TK(('Сложение', 'Addition'), ('Найдите (3x² + 2x − 1) + (x² − 5x + 4).', 'Find (3x² + 2x − 1) + (x² − 5x + 4).'), '', '4x² − 3x + 3.', '4x² − 3x + 3.'),
  TK(('Умножение', 'Multiplication'), ('Раскройте (x + 4)(x − 2).', 'Expand (x + 4)(x − 2).'), 'p = 4, q = −2', 'x² + 2x − 8.', 'x² + 2x − 8.'),
  TK(('Квадрат суммы', 'Square of a sum'), ('Раскройте (2x + 3)².', 'Expand (2x + 3)².'), '(2x)² + 2·2x·3 + 3²', '4x² + 12x + 9.', '4x² + 12x + 9.'),
  TK(('Разность квадратов', 'Difference of squares'), ('Разложите на множители 49 − x².', 'Factorise 49 − x².'), '7² − x²', '(7 − x)(7 + x).', '(7 − x)(7 + x).'),
  TK(('Счёт в уме', 'Mental arithmetic'), ('Вычислите 52 · 48.', 'Calculate 52 · 48.'), '(50 + 2)(50 − 2)', '2 500 − 4 = 2 496.', '2 496.')],
 [Q('(a + b)² =', '(a + b)² =', 'a² + 2ab + b²', 'a² + b²', 'a² + ab + b²', ('Есть удвоенное произведение.', 'There is a double product.')),
  Q('(x − 3)² =', '(x − 3)² =', 'x² − 6x + 9', 'x² − 9', 'x² + 6x + 9', ('(x − 3)(x − 3).', '(x − 3)(x − 3).')),
  Q('(x − 4)(x + 4) =', '(x − 4)(x + 4) =', 'x² − 16', 'x² + 16', 'x² − 8x', ('Разность квадратов.', 'Difference of squares.')),
  Q('x² − 25 =', 'x² − 25 =', '(x − 5)(x + 5)', '(x − 5)²', '(x − 25)(x + 1)', ('25 = 5².', '25 = 5².')),
  Q('(x + 1)(x + 2) =', '(x + 1)(x + 2) =', 'x² + 3x + 2', 'x² + 2', 'x² + 3x + 3', ('x² + 2x + x + 2.', 'x² + 2x + x + 2.')),
  Q('Степень многочлена x³ − x + 7', 'The degree of x³ − x + 7', '3', '7', '1', ('Наибольший показатель.', 'The highest exponent.')),
  Q('99² =', '99² =', '9 801', '9 801 + 198', '9 600', ('(100 − 1)² = 10 000 − 200 + 1.', '(100 − 1)² = 10,000 − 200 + 1.')),
  Q('Верно ли (a + b)² = a² + b²?', 'Is (a + b)² = a² + b² true?', ('нет, в общем случае', 'no, in general'), ('да, всегда', 'yes, always'), ('только при a = b', 'only when a = b'), ('Теряется 2ab.', '2ab is lost.'))],
 src=[('Wikipedia: Polynomial', 'https://en.wikipedia.org/wiki/Polynomial'), ('Wikipedia: Difference of two squares', 'https://en.wikipedia.org/wiki/Difference_of_two_squares')])
