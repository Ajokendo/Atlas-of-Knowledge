# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Предел последовательности', 'Limit of a sequence'),
 [('s', 'k', 'Последовательность', 'Sequence', ['1/n', '(2n+1)/n', '(−1)ⁿ/n', 'n'], ['1/n', '(2n+1)/n', '(−1)ⁿ/n', 'n'], 1), ('r', 'n', 'Номер n', 'Index n', 1, 50, 1, 10)],
 [('aₙ при выбранном n', 'aₙ at the chosen n'), ('Предел', 'The limit'), ('Отличие от предела', 'Distance from the limit')],
 'Члены последовательности могут приближаться к числу сколь угодно близко — это число называют пределом. Если приближения нет, предела нет.', 'The terms of a sequence may approach a number as closely as we wish — that number is the limit. If they do not approach anything, there is no limit.', ('Члены последовательности', 'Terms of the sequence'),
 r'''const F=[n=>1/n,n=>(2*n+1)/n,n=>Math.pow(-1,n)/n,n=>n][v.k],Lm=[0,2,0,null][v.k];const G=Gr({x0:0,x1:50,y0:v.k===3?0:-1.2,y1:v.k===3?55:3.2,L:80,T:10,W:470,H:210});let g=G.grid(10,v.k===3?10:0.5);if(Lm!==null)g+=G.seg(0,Lm,50,Lm,COL.c,2,true);for(let i=1;i<=50;i++)g+=G.pt(i,F(i),i===v.n?COL.b:COL.a,i===v.n?7:3);
 return {svg:g,st:[fnum(F(v.n),5),Lm===null?U("нет (растёт без границ)","none (grows without bound)"):String(Lm),Lm===null?"—":fnum(Math.abs(F(v.n)-Lm),5)],fb:Lm===null?U("Последовательность уходит в бесконечность — предела нет.","The sequence goes to infinity — no limit."):U("Точки сгущаются около предела: расстояние до него становится сколь угодно малым.","The points cluster near the limit: the distance to it becomes arbitrarily small.")}''', '0 0 600 250')

m2 = M(('Предел функции в точке', 'Limit of a function at a point'),
 [('r', 'x', 'x (приближаемся к 1)', 'x (approaching 1)', 0, 2, 0.05, 0.5)],
 [('f(x) = (x² − 1)/(x − 1)', 'f(x) = (x² − 1)/(x − 1)'), ('Предел при x → 1', 'Limit as x → 1'), ('f(1)', 'f(1)')],
 'Функция (x² − 1)/(x − 1) в точке 1 не определена, но при x, близких к 1, значения близки к 2. Предел не зависит от того, определена ли функция в самой точке.', 'The function (x² − 1)/(x − 1) is not defined at 1, but for x near 1 the values are near 2. The limit does not depend on whether the function is defined at the point itself.', ('График с «выколотой» точкой', 'A graph with a “hole”'),
 r'''const G=Gr({x0:0,x1:2,y0:0,y1:3,L:80,T:10,W:470,H:210});const f=x=>x+1;let g=G.grid(0.5,0.5)+G.fn(f,COL.a,3.5,0,2)+C(G.X(1),G.Y(2),6,COL.bg,COL.a,2.5)+G.pt(v.x,Math.abs(v.x-1)<1e-9?2:f(v.x),COL.b,7);
 const same=Math.abs(v.x-1)<1e-9;
 return {svg:g,st:[same?U("нет значения","has no value"):fnum(f(v.x),3),"2",U("нет значения","has no value")],fb:U("Подойдя к 1 слева и справа, значения идут к 2 — предел равен 2, хотя f(1) не существует.","Approaching 1 from left and right the values go to 2 — the limit is 2 although f(1) does not exist.")}''', '0 0 600 250')

m3 = M(('Непрерывность и разрыв', 'Continuity and a jump'),
 [('r', 'h', 'Скачок h', 'Jump h', -2, 2, 0.5, 1), ('r', 'x', 'Точка x', 'Point x', -2, 2, 0.1, -0.5)],
 [('Слева от 0', 'Left of 0'), ('Справа от 0', 'Right of 0'), ('Вывод', 'Conclusion')],
 'Функция непрерывна в точке, если предел слева, предел справа и значение совпадают — график можно провести, не отрывая карандаша.', 'A function is continuous at a point if the left limit, the right limit and the value coincide — the graph can be drawn without lifting the pencil.', ('Функция со скачком в нуле', 'A function with a jump at zero'),
 r'''const G=Gr({x0:-2,x1:2,y0:-3,y1:4,L:80,T:10,W:470,H:210});const f=x=>x<0?x+1:x+1+v.h;let g=G.grid(1,1)+G.fn(f,COL.a,3.5,-2,-0.001)+G.fn(f,COL.a,3.5,0,2)+G.pt(v.x,f(v.x),COL.b,7);if(v.h!==0)g+=C(G.X(0),G.Y(1),6,COL.bg,COL.a,2.5);
 return {svg:g,st:[fnum(1,2),fnum(1+v.h,2),v.h===0?U("непрерывна","continuous"):U("разрыв","discontinuous")],fb:v.h===0?U("Пределы слева и справа равны — график сплошной.","The left and right limits are equal — the graph is unbroken."):U("Пределы слева и справа различны — функция в нуле разрывна.","The left and right limits differ — the function is discontinuous at zero.")}''', '0 0 600 250')

chapter('56', '56-limits.html', 'VIII', ('Пределы и непрерывность', 'Limits and continuity'),
 ('Что значит «приближаться» к числу и когда график можно рисовать, не отрывая руки.', 'What it means to “approach” a number and when a graph can be drawn without lifting the hand.'),
 ('Мяч каждый раз подпрыгивает ровно на половину высоты прошлого прыжка. Сколько раз он подпрыгнет и где окажется «в конце»?', 'A ball bounces to exactly half the height of the previous bounce. How many bounces will it make and where is it “in the end”?'),
 ('Разгадка: прыжков бесконечно много, а высота стремится к 0', 'The answer: infinitely many bounces, and the height tends to 0'),
 ('В идеальной модели высоты 1, 1/2, 1/4, 1/8… никогда не обращаются в ноль, но становятся меньше любого заданного числа — говорят, что предел высоты равен 0. Идея предела позволяет иметь дело с бесконечными процессами, не заканчивая их. (Настоящий мяч, конечно, останавливается — это идеальная модель.)', 'In the ideal model the heights 1, 1/2, 1/4, 1/8… never become zero but become smaller than any given number — we say the limit of the height is 0. The idea of a limit lets us handle infinite processes without finishing them. (A real ball stops, of course — this is an ideal model.)'),
 [S('seq', 'Предел последовательности', 'Limit of a sequence', ('Число A — предел последовательности aₙ, если для любого сколь угодно малого ε, начиная с некоторого номера, все члены отличаются от A меньше чем на ε. Пишут lim aₙ = A. Например, lim 1/n = 0; lim (2n + 1)/n = 2. Последовательность 1, 2, 3, … предела не имеет — она растёт без границ.', 'A number A is the limit of a sequence aₙ if for any arbitrarily small ε, from some index on, all terms differ from A by less than ε. We write lim aₙ = A. For example lim 1/n = 0; lim (2n + 1)/n = 2. The sequence 1, 2, 3, … has no limit — it grows without bound.'),
    ('lim aₙ = A', '', 'lim aₙ = A'), m1),
  S('fn', 'Предел функции', 'Limit of a function', ('lim f(x) при x → a — число, к которому приближается f(x), когда x приближается к a (но не равно a). Основные правила: предел суммы, произведения и частного равен сумме, произведению и частному пределов (знаменатель ≠ 0). Если подстановка даёт 0/0, нужно преобразовать выражение: (x² − 1)/(x − 1) = x + 1 → 2.', 'lim f(x) as x → a is the number f(x) approaches when x approaches a (but is not equal to a). Main rules: the limit of a sum, product and quotient is the sum, product and quotient of the limits (denominator ≠ 0). If substitution gives 0/0 we transform the expression: (x² − 1)/(x − 1) = x + 1 → 2.'),
    ('(x² − 1)/(x − 1) → 2', '', '(x² − 1)/(x − 1) → 2'), m2),
  S('cont', 'Непрерывность', 'Continuity', ('Функция непрерывна в точке a, если lim f(x) = f(a). Многочлены, sin, cos, aˣ непрерывны всюду; 1/x разрывна в нуле. Непрерывные функции обладают важным свойством: если f(a) &lt; 0 и f(b) &gt; 0, то между a и b есть корень.', 'A function is continuous at a if lim f(x) = f(a). Polynomials, sin, cos, aˣ are continuous everywhere; 1/x is discontinuous at zero. Continuous functions have an important property: if f(a) &lt; 0 and f(b) &gt; 0 then there is a root between a and b.'),
    ('lim f(x) = f(a)', '', 'lim f(x) = f(a)'), m3)],
 [TK(('Предел', 'Limit'), ('Найдите lim (3n + 2)/n.', 'Find lim (3n + 2)/n.'), '3 + 2/n', '2/n → 0, значит предел 3.', '3.'),
  TK(('0/0', '0/0'), ('Найдите lim (x² − 4)/(x − 2) при x → 2.', 'Find lim (x² − 4)/(x − 2) as x → 2.'), '', '= x + 2 → 4.', '4.'),
  TK(('Подстановка', 'Substitution'), ('Найдите lim (x² + 3x) при x → 2.', 'Find lim (x² + 3x) as x → 2.'), '', 'Многочлен непрерывен: 4 + 6 = 10.', '10.'),
  TK(('Нет предела', 'No limit'), ('Есть ли предел у (−1)ⁿ?', 'Does (−1)ⁿ have a limit?'), '', 'Члены чередуются −1, 1, −1, … и ни к чему не приближаются.', ('Нет.', 'No.')),
  TK(('Корень', 'A root'), ('f(x) = x² − 2: f(1) = −1, f(2) = 2. Есть ли корень на [1; 2]?', 'f(x) = x² − 2: f(1) = −1, f(2) = 2. Is there a root on [1; 2]?'), '', 'Функция непрерывна, знак меняется — корень есть (√2).', ('Да, √2.', 'Yes, √2.'))],
 [Q('lim 1/n =', 'lim 1/n =', '0', '1', ('не существует', 'does not exist'), ('Члены стремятся к 0.', 'The terms tend to 0.')),
  Q('lim (2n + 1)/n =', 'lim (2n + 1)/n =', '2', '1', '0', ('2 + 1/n.', '2 + 1/n.')),
  Q('Последовательность 1, 2, 3, …', 'The sequence 1, 2, 3, …', ('предела не имеет', 'has no limit'), ('имеет предел 0', 'has limit 0'), ('имеет предел 1', 'has limit 1'), ('Растёт без границ.', 'Grows without bound.')),
  Q('Предел функции в точке зависит от f(a)?', 'Does the limit at a point depend on f(a)?', ('нет', 'no'), ('да', 'yes'), ('всегда равен f(a)', 'always equals f(a)'), ('Важны значения рядом.', 'Nearby values matter.')),
  Q('Функция непрерывна в a, если', 'A function is continuous at a if', ('lim f(x) = f(a)', 'lim f(x) = f(a)'), ('f(a) = 0', 'f(a) = 0'), ('f возрастает', 'f is increasing'), ('Определение.', 'The definition.')),
  Q('Где разрывна 1/x?', 'Where is 1/x discontinuous?', ('в 0', 'at 0'), ('в 1', 'at 1'), ('нигде', 'nowhere'), ('Деление на 0.', 'Division by 0.')),
  Q('lim (x² − 1)/(x − 1) при x → 1 =', 'lim (x² − 1)/(x − 1) as x → 1 =', '2', '0', '1', ('x + 1 → 2.', 'x + 1 → 2.')),
  Q('Если непрерывная f меняет знак на [a; b], то', 'If a continuous f changes sign on [a; b] then', ('есть корень', 'there is a root'), ('корня нет', 'there is no root'), ('f возрастает', 'f is increasing'), ('Нельзя «перепрыгнуть» 0.', 'It cannot “jump over” 0.'))],
 src=[('Wikipedia: Limit (mathematics)', 'https://en.wikipedia.org/wiki/Limit_(mathematics)'), ('Wikipedia: Continuous function', 'https://en.wikipedia.org/wiki/Continuous_function'), ('OpenStax: Calculus Volume 1', 'https://openstax.org/details/books/calculus-volume-1')])
