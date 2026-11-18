# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Значение выражения', 'The value of an expression'),
 [('r', 'a', 'Коэффициент a', 'Coefficient a', -5, 5, 1, 3), ('r', 'b', 'Число b', 'Number b', -10, 10, 1, 2), ('r', 'x', 'Значение x', 'Value of x', -6, 6, 1, 4)],
 [('Выражение', 'Expression'), ('Подставляем', 'Substituting'), ('Значение', 'Value')],
 'Буква — это «ячейка» для числа. Подставьте число вместо x и вычислите.', 'A letter is a “box” for a number. Put a number in place of x and calculate.', ('Выражение a·x + b на графике', 'The expression a·x + b on a graph'),
 r'''const G=Gr({x0:-7,x1:7,y0:-30,y1:30,L:80,T:10,W:440,H:220});const y=v.a*v.x+v.b;let g=G.grid(1,10)+G.fn(t=>v.a*t+v.b,COL.b,3)+G.seg(v.x,0,v.x,y,COL.mut,1.5)+G.pt(v.x,y,COL.a,8)+G.txt(v.x+0.8,y+3,fnum(y,0),COL.a,15);
 return {svg:g,st:[v.a+"·x "+(v.b<0?"− "+(-v.b):"+ "+v.b),v.a+"·("+v.x+") "+(v.b<0?"− "+(-v.b):"+ "+v.b),y],fb:U("При x = "+v.x+" выражение равно "+y+".","At x = "+v.x+" the expression equals "+y+".")}''', '0 0 600 250')

m2 = M(('Подобные слагаемые', 'Like terms'),
 [('r', 'a', 'Первое слагаемое: коэффициент', 'First term: coefficient', -9, 9, 1, 5), ('r', 'b', 'Второе слагаемое: коэффициент', 'Second term: coefficient', -9, 9, 1, -2), ('r', 'c', 'Число без буквы', 'Plain number', -9, 9, 1, 3)],
 [('Было', 'Before'), ('Стало', 'After'), ('Проверка при x = 2', 'Check at x = 2')],
 'Слагаемые с одинаковой буквенной частью можно собрать: ax + bx = (a + b)x.', 'Terms with the same letter part can be combined: ax + bx = (a + b)x.', ('Плитки x и числа', 'Tiles of x and numbers'),
 r'''const t=(c,s)=>c===0?"0":(c===1?"":c===-1?"-":c)+s;let g="";let px=30;
 const tile=(n,col,lab,row)=>{for(let i=0;i<Math.abs(n);i++)g+=R(30+i*44,row,40,40,n>0?col:COL.bg,n>0?COL.ink:COL.a,n>0?1.5:2.5,4)+TX(50+i*44,row+27,(n<0?"−":"")+lab,n>0?"#fff":COL.a,15,"middle",700)};
 tile(v.a,COL.b,"x",20);tile(v.b,COL.c,"x",75);tile(v.c,COL.a,"1",130);
 const s=v.a+v.b;g+=TX(300,215,U("Итого: "+s+"·x "+(v.c<0?"− "+(-v.c):"+ "+v.c),"Total: "+s+"·x "+(v.c<0?"− "+(-v.c):"+ "+v.c)),COL.ink,22,"middle",600);
 return {svg:g,st:[v.a+"x "+(v.b<0?"− "+(-v.b):"+ "+v.b)+"x "+(v.c<0?"− "+(-v.c):"+ "+v.c),s+"x "+(v.c<0?"− "+(-v.c):"+ "+v.c),(v.a*2+v.b*2+v.c)+" = "+(s*2+v.c)],fb:U("Цвет плитки — тип слагаемого; контурные — отрицательные.","Tile colour is the term type; outlined tiles are negative.")}''', '0 0 600 235')

m3 = M(('Раскрытие скобок: площадь', 'Expanding brackets: area'),
 [('r', 'k', 'Множитель k', 'Factor k', 1, 6, 1, 3), ('r', 'a', 'Первое слагаемое a', 'First addend a', 1, 8, 1, 5), ('r', 'b', 'Второе слагаемое b', 'Second addend b', 1, 8, 1, 2)],
 [('Произведение со скобками', 'Product with brackets'), ('Без скобок', 'Without brackets'), ('Результат', 'Result')],
 'Площадь большого прямоугольника k(a + b) равна сумме площадей двух частей: k·a и k·b.', 'The area of the large rectangle k(a + b) is the sum of the areas of two parts: k·a and k·b.', ('Прямоугольник из двух частей', 'A rectangle of two parts'),
 r'''const u=Math.min(40,520/(v.a+v.b)),h=Math.min(28,170/v.k);let g=R(40,30,v.a*u,v.k*h,"#f4dfd8",COL.ink,2)+R(40+v.a*u,30,v.b*u,v.k*h,"#dbe5f2",COL.ink,2)+TX(40+v.a*u/2,30+v.k*h/2+5,v.k*v.a,COL.a,18,"middle",700)+TX(40+v.a*u+v.b*u/2,30+v.k*h/2+5,v.k*v.b,COL.b,18,"middle",700)+TX(40+(v.a+v.b)*u/2,22,v.a+"+"+v.b,COL.ink,13)+TX(30,30+v.k*h/2+5,v.k,COL.ink,15,"end");
 return {svg:g,st:[v.k+"·("+v.a+" + "+v.b+")",v.k+"·"+v.a+" + "+v.k+"·"+v.b,v.k*(v.a+v.b)],fb:U("Распределительный закон: k(a + b) = ka + kb.","The distributive law: k(a + b) = ka + kb.")}''', '0 0 600 230')

chapter('24', '24-expressions.html', 'IV', ('Буквенные выражения', 'Letter expressions'),
 ('Зачем нужны буквы в математике, как вычислять значение выражения, собирать подобные слагаемые и раскрывать скобки.', 'Why mathematics uses letters, how to evaluate an expression, combine like terms and expand brackets.'),
 ('Такси в Бишкеке берёт 100 сомов за посадку и 20 сомов за километр.\n\nКак записать стоимость поездки на любое расстояние и сколько стоит поездка на 12 км?', 'A taxi in Bishkek charges 100 som for boarding and 20 som per kilometre.\n\nHow can we write the cost of a ride of any length and what does a 12 km ride cost?'),
 ('Разгадка: 100 + 20x; 340 сомов', 'The answer: 100 + 20x; 340 som'),
 ('Если поездка x километров, то цена равна 100 + 20x. Одно выражение заменяет таблицу цен для любого расстояния. При x = 12: 100 + 20 · 12 = 100 + 240 = 340 сомов. Буква x — переменная: вместо неё можно подставлять разные числа.', 'If the ride is x kilometres, the cost is 100 + 20x. One expression replaces a price table for any distance. At x = 12: 100 + 20 · 12 = 100 + 240 = 340 som. The letter x is a variable: different numbers can be put in its place.'),
 [S('val', 'Переменная и значение выражения', 'A variable and the value of an expression', ('<strong>Буквенное выражение</strong> — запись из чисел, букв и знаков действий. Чтобы найти его <strong>значение</strong>, подставляют числа вместо букв и выполняют действия по порядку. Выражение ax + b задаёт линейную зависимость; на графике это прямая.', 'A <strong>letter expression</strong> is a notation made of numbers, letters and operation signs. To find its <strong>value</strong> we substitute numbers for letters and perform the operations in order. The expression ax + b describes a linear dependence; on a graph it is a straight line.'),
    ('a·x + b', 'при x = 12: 100 + 20·12 = 340', 'at x = 12: 100 + 20·12 = 340'), m1),
  S('like', 'Подобные слагаемые', 'Like terms', ('<strong>Подобные слагаемые</strong> отличаются только числовым множителем (коэффициентом): 5x и −2x. Их складывают: 5x − 2x = 3x. Слагаемые 3x и 3 — не подобные: одно с буквой, другое без, их не объединить.', '<strong>Like terms</strong> differ only in the numerical factor (the coefficient): 5x and −2x. They are added: 5x − 2x = 3x. The terms 3x and 3 are not like: one has a letter, the other does not; they cannot be merged.'),
    ('ax + bx = (a + b)x', '', 'ax + bx = (a + b)x'), m2),
  S('brk', 'Раскрытие скобок', 'Expanding brackets', ('Распределительный закон: k(a + b) = ka + kb. Если перед скобками знак «−», знаки внутри меняются на противоположные: −(a − b) = −a + b. Закон хорошо видно на площади: большой прямоугольник состоит из двух частей.', 'The distributive law: k(a + b) = ka + kb. If there is a “−” before the brackets, the signs inside change: −(a − b) = −a + b. The law is visible on an area: a large rectangle consists of two parts.'),
    ('k(a + b) = ka + kb', '', 'k(a + b) = ka + kb'), m3)],
 [TK(('Значение', 'Value'), ('Найдите значение 3x − 5 при x = 4.', 'Find the value of 3x − 5 at x = 4.'), '3 · 4 − 5', '12 − 5 = 7.', '7.'),
  TK(('Подобные', 'Like terms'), ('Упростите 7a − 3a + 2b + b.', 'Simplify 7a − 3a + 2b + b.'), 'a и b — разные буквы', '(7 − 3)a + (2 + 1)b = 4a + 3b.', '4a + 3b.'),
  TK(('Скобки', 'Brackets'), ('Раскройте 5(2x − 3).', 'Expand 5(2x − 3).'), '', '5 · 2x − 5 · 3 = 10x − 15.', '10x − 15.'),
  TK(('Минус перед скобками', 'Minus before brackets'), ('Упростите 8 − (3 − x).', 'Simplify 8 − (3 − x).'), '', '8 − 3 + x = 5 + x.', '5 + x.'),
  TK(('Формула', 'A formula'), ('Периметр прямоугольника P = 2(a + b). Найдите P при a = 7, b = 5.', 'The perimeter of a rectangle P = 2(a + b). Find P at a = 7, b = 5.'), '2 · 12', '2 · (7 + 5) = 24.', '24.')],
 [Q('Значение 2x + 1 при x = 5', 'The value of 2x + 1 at x = 5', '11', '10', '15', ('2 · 5 + 1.', '2 · 5 + 1.')),
  Q('3x + 4x =', '3x + 4x =', '7x', '12x', '7x²', ('Складываем коэффициенты.', 'We add the coefficients.')),
  Q('Какие слагаемые подобные?', 'Which terms are like?', '5y и −2y', '5y и 5', '3x и 3y', ('Одна и та же буквенная часть.', 'The same letter part.')),
  Q('2(x + 3) =', '2(x + 3) =', '2x + 6', '2x + 3', 'x + 6', ('Умножаем оба слагаемых.', 'Multiply both terms.')),
  Q('−(a − 2) =', '−(a − 2) =', '−a + 2', '−a − 2', 'a − 2', ('Знаки меняются.', 'The signs change.')),
  Q('Что называют коэффициентом в 7x?', 'What is the coefficient in 7x?', '7', 'x', '7x', ('Числовой множитель.', 'The numerical factor.')),
  Q('Верно ли a + b = b + a?', 'Is a + b = b + a true?', ('Да, всегда', 'Yes, always'), ('Только для натуральных', 'Only for naturals'), ('Нет', 'No'), ('Переместительный закон.', 'The commutative law.')),
  Q('5x − 5x =', '5x − 5x =', '0', 'x', '10x', ('Коэффициенты 5 − 5 = 0.', 'The coefficients 5 − 5 = 0.'))],
 src=[('Wikipedia: Variable (mathematics)', 'https://en.wikipedia.org/wiki/Variable_(mathematics)'), ('Wikipedia: Distributive property', 'https://en.wikipedia.org/wiki/Distributive_property')],
 note=('Тариф такси в загадке придуман для задачи.', 'The taxi tariff in the puzzle is made up for the problem.'))
