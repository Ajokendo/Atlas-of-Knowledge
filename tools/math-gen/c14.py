# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Числовые закономерности', 'Number patterns'),
 [('s', 'r', 'Правило', 'Rule', ['прибавляем 3', 'умножаем на 2', 'квадраты чисел', 'числа Фибоначчи', 'треугольные числа', 'прибавляем всё больше: +1, +2, +3…'], ['add 3', 'multiply by 2', 'squares', 'Fibonacci numbers', 'triangular numbers', 'add more each time: +1, +2, +3…'], 0), ('r', 'n', 'Сколько членов показать', 'How many terms to show', 3, 9, 1, 6)],
 [('Следующий член', 'The next term'), ('n-й член (формула)', 'The n-th term (formula)'), ('Как получаем', 'How it works')],
 'Ищем правило: что происходит от члена к члену. Тогда можно предсказать следующий.', 'We look for the rule: what happens from term to term. Then we can predict the next one.', ('Ряд чисел и следующий член', 'A row of numbers and the next term'),
 r'''const fib=n=>{let a=1,b=1;for(let i=3;i<=n;i++){const t=a+b;a=b;b=t}return b};
 const F=[n=>3*n,n=>Math.pow(2,n-1),n=>n*n,fib,n=>n*(n+1)/2,n=>1+n*(n-1)/2],f=F[v.r],N=v.n,w=Math.min(60,540/(N+1));let g="";
 for(let i=1;i<=N+1;i++){const x=30+(i-1)*w,nx=i===N+1;g+=R(x,80,w-8,56,nx?"#fff4e0":COL.bg,nx?COL.d:COL.ink,nx?3:1.5,6)+TX(x+(w-8)/2,115,nx?"?":f(i),nx?COL.a:COL.ink,w>50?18:15,"middle",600);if(i<=N)g+=TX(x+(w-8)/2,70,i,COL.mut,11)}
 const how=U(["+3 каждый раз","×2 каждый раз","n · n","сумма двух предыдущих","1 + 2 + … + n","разность растёт: 1, 2, 3…"],["+3 each time","×2 each time","n · n","sum of the two previous","1 + 2 + … + n","the gap grows: 1, 2, 3…"])[v.r];
 const form=["3n","2ⁿ⁻¹","n²","—","n(n+1)/2","1 + n(n−1)/2"][v.r];g+=TX(300,190,how,COL.b,16);
 return {svg:g,st:[f(N+1),form,how],fb:U("Следующий член: "+f(N+1)+". Правило: "+how+".","The next term is "+f(N+1)+". The rule: "+how+".")}''')

m2 = M(('Закономерность из спичек', 'A matchstick pattern'),
 [('r', 'n', 'Квадратов в ряду', 'Squares in the row', 1, 10, 1, 4)],
 [('Спичек', 'Matchsticks'), ('Формула 3n + 1', 'Formula 3n + 1'), ('Для 100 квадратов', 'For 100 squares'), ('Квадратов из 61 спички', 'Squares from 61 sticks')],
 'Первый квадрат — 4 спички, каждый следующий добавляет по 3 (общую сторону не повторяем).', 'The first square takes 4 sticks, each next one adds 3 (the shared side is not repeated).', ('Ряд квадратов из спичек', 'A row of squares made of matchsticks'),
 r'''const n=v.n,s=Math.min(60,520/n),x0=300-n*s/2,y0=110;let g="";
 for(let i=0;i<=n;i++)g+=L(x0+i*s,y0,x0+i*s,y0+s,COL.a,5);for(let i=0;i<n;i++)g+=L(x0+i*s,y0,x0+(i+1)*s,y0,COL.b,5)+L(x0+i*s,y0+s,x0+(i+1)*s,y0+s,COL.b,5);
 g+=TX(300,230,U("Спичек: ","Matchsticks: ")+(3*n+1),COL.ink,20,"middle",600);
 return {svg:g,st:[3*n+1,"3 · "+n+" + 1 = "+(3*n+1),301,20],fb:U("Каждый новый квадрат добавляет 3 спички: "+ruen(n,["квадрат","квадрата","квадратов"],"square","squares")+" — 4 + 3 · "+(n-1)+" = "+(3*n+1)+".",ruen(n,["","",""],"square","squares")+": 4 + 3 · "+(n-1)+" = "+(3*n+1)+".")}''')

m3 = M(('Круги Эйлера', 'Venn diagram'),
 [('r', 'T', 'Всего в классе', 'Pupils in the class', 10, 40, 1, 25), ('r', 'A', 'Любят футбол (A)', 'Like football (A)', 0, 40, 1, 15), ('r', 'B', 'Любят шахматы (B)', 'Like chess (B)', 0, 40, 1, 12), ('r', 'X', 'Любят оба', 'Like both', 0, 40, 1, 5)],
 [('Только футбол', 'Football only'), ('Только шахматы', 'Chess only'), ('Оба', 'Both'), ('Ни то ни другое', 'Neither')],
 'Число, попавшее в пересечение, считать дважды нельзя: оно уже входит и в A, и в B.', 'A number in the overlap must not be counted twice: it is already in both A and B.', ('Два пересекающихся круга', 'Two overlapping circles'),
 r'''const A=v.A,B=v.B,X=Math.min(v.X,A,B),oa=A-X,ob=B-X,u=A+B-X,ne=v.T-u;let g=R(20,10,560,225,"none",COL.ink,2,6)+C(220,125,85,"rgba(182,83,63,.18)",COL.a,3)+C(380,125,85,"rgba(63,95,143,.18)",COL.b,3)+TX(150,130,oa,COL.a,28,"middle",600)+TX(300,130,X,COL.ink,28,"middle",600)+TX(450,130,ob,COL.b,28,"middle",600)+TX(220,40,"A",COL.a,16,"middle",600)+TX(380,40,"B",COL.b,16,"middle",600)+TX(550,222,ne>=0?ne:"!",ne>=0?COL.mut:COL.a,20,"end",600);
 return {svg:g,st:[oa,ob,X,ne>=0?ne:"—"],fb:ne>=0?U("Объединение: "+A+" + "+B+" − "+X+" = "+u+". Остальные: "+v.T+" − "+u+" = "+ne+".","Union: "+A+" + "+B+" − "+X+" = "+u+". The rest: "+v.T+" − "+u+" = "+ne+"."):U("Невозможно: в объединении "+u+" человек, а в классе только "+v.T+".","Impossible: the union has "+u+" pupils but the class has only "+v.T+".")}''')

chapter('14', '14-patterns-logic.html', 'II', ('Закономерности и логика', 'Patterns and logic'),
 ('Как найти правило в ряду чисел, записать его формулой и не посчитать лишнее дважды.', 'How to find the rule in a row of numbers, write it as a formula and not count anything twice.'),
 ('В классе 25 учеников. 15 любят футбол, 12 — шахматы, 5 любят и то и другое.\n\nСколько учеников не любят ни футбол, ни шахматы?', 'A class has 25 pupils. 15 like football, 12 like chess and 5 like both.\n\nHow many pupils like neither football nor chess?'),
 ('Разгадка: 3 ученика', 'The answer: 3 pupils'),
 ('15 + 12 = 27 — больше, чем всего в классе, потому что 5 любителей обоих посчитали дважды. Значит, любят хотя бы одно: 15 + 12 − 5 = 22. Не любят ни то ни другое: 25 − 22 = 3. Так работают круги Эйлера: общую часть вычитаем один раз.', '15 + 12 = 27 — more than the whole class, because the 5 who like both were counted twice. So the number who like at least one is 15 + 12 − 5 = 22. Those who like neither: 25 − 22 = 3. This is how Venn diagrams work: the shared part is subtracted once.'),
 [S('seq', 'Числовые закономерности', 'Number patterns', ('<strong>Последовательность</strong> — числа, выписанные по порядку. Чтобы продолжить её, ищем правило: прибавляют одно и то же число, умножают на одно и то же, складывают два предыдущих. Правило можно записать <strong>формулой</strong> для n-го члена: 3, 6, 9, … — это 3n.', 'A <strong>sequence</strong> is numbers written in order. To continue it we look for the rule: the same number is added, the same multiplier is used, or the two previous terms are added. A rule can be written as a <strong>formula</strong> for the n-th term: 3, 6, 9, … is 3n.'),
    ('3, 6, 9, 12, …  →  3n', 'n-й член', 'the n-th term'), m1),
  S('match', 'Закономерности в фигурах', 'Patterns in figures', ('Закономерность можно увидеть и в картинках. Ряд из n квадратов спичками: первый квадрат — 4 спички, каждый следующий — ещё 3. Значит, спичек <strong>3n + 1</strong>. По формуле можно сразу найти ответ для 100 квадратов, не рисуя их.', 'A pattern can also be seen in pictures. A row of n squares made of matchsticks: the first square takes 4 sticks, each next one 3 more. So there are <strong>3n + 1</strong> sticks. The formula gives the answer for 100 squares at once, without drawing them.'),
    ('3n + 1', 'n = 100 → 301', 'n = 100 → 301'), m2),
  S('venn', 'Круги Эйлера', 'Venn diagrams', ('Когда множества пересекаются, общую часть нельзя считать дважды. Для двух множеств: <strong>|A ∪ B| = |A| + |B| − |A ∩ B|</strong>. Те, кто не вошёл в объединение, — «ни то ни другое».', 'When sets overlap, the shared part must not be counted twice. For two sets: <strong>|A ∪ B| = |A| + |B| − |A ∩ B|</strong>. Those outside the union are “neither”.'),
    ('15 + 12 − 5 = 22', 'любят хотя бы одно', 'like at least one'), m3)],
 [TK(('Продолжи ряд', 'Continue the row'), ('Продолжите ряд: 5, 8, 11, 14, … Каков 10-й член?', 'Continue the row: 5, 8, 11, 14, … What is the 10th term?'), '5, 8, 11, 14', 'Прибавляем 3 каждый раз. Формула: 3n + 2. 10-й член: 3 · 10 + 2 = 32.', ('Следующий 17; 10-й член 32.', 'Next is 17; the 10th term is 32.')),
  TK(('Удвоение', 'Doubling'), ('Бактерия делится на две каждый час. Сколько их будет через 6 часов, если в начале одна?', 'A bacterium divides into two every hour. How many after 6 hours if there is one at the start?'), '1, 2, 4, …', 'Каждый час число удваивается: 1 · 2⁶ = 64.', ('64.', '64.')),
  TK(('Спички', 'Matchsticks'), ('Сколько спичек нужно для ряда из 20 квадратов (формула 3n + 1)?', 'How many matchsticks are needed for a row of 20 squares (formula 3n + 1)?'), 'n = 20', '3 · 20 + 1 = 61.', '61.'),
  TK(('Круги Эйлера', 'Venn diagram'), ('В группе 30 человек. 18 знают русский, 14 — английский, 6 — оба языка. Сколько не знают ни одного?', 'A group has 30 people. 18 know Russian, 14 know English, 6 know both. How many know neither?'), '30; 18; 14; 6', 'Хотя бы один язык: 18 + 14 − 6 = 26. Ни одного: 30 − 26 = 4.', ('4 человека.', '4 people.')),
  TK(('Числа Фибоначчи', 'Fibonacci numbers'), ('Ряд: 1, 1, 2, 3, 5, 8, … Каждый член — сумма двух предыдущих. Найдите следующие три члена.', 'The row: 1, 1, 2, 3, 5, 8, … Each term is the sum of the two previous. Find the next three terms.'), '1, 1, 2, 3, 5, 8', '5 + 8 = 13; 8 + 13 = 21; 13 + 21 = 34.', ('13, 21, 34.', '13, 21, 34.'))],
 [Q('Продолжите: 2, 4, 6, 8, …', 'Continue: 2, 4, 6, 8, …', '10', '12', '9', ('Прибавляем 2.', 'We add 2.')),
  Q('Продолжите: 1, 2, 4, 8, …', 'Continue: 1, 2, 4, 8, …', '16', '10', '12', ('Умножаем на 2.', 'We multiply by 2.')),
  Q('Формула членов 3, 6, 9, 12, …', 'The formula for the terms 3, 6, 9, 12, …', '3n', 'n + 3', 'n · n', ('Третий член 3 · 3 = 9.', 'The third term is 3 · 3 = 9.')),
  Q('Сколько спичек в ряду из 5 квадратов (3n + 1)?', 'How many sticks in a row of 5 squares (3n + 1)?', '16', '15', '20', ('3 · 5 + 1 = 16.', '3 · 5 + 1 = 16.')),
  Q('Следующий член ряда 1, 4, 9, 16, …', 'The next term of 1, 4, 9, 16, …', '25', '20', '24', ('Квадраты: 5² = 25.', 'Squares: 5² = 25.')),
  Q('В классе 20 человек: 10 любят A, 8 любят B, 3 любят оба. Сколько любят хотя бы одно?', 'A class of 20: 10 like A, 8 like B, 3 like both. How many like at least one?', '15', '18', '21', ('10 + 8 − 3 = 15.', '10 + 8 − 3 = 15.')),
  Q('Почему общую часть вычитают при подсчёте объединения?', 'Why is the shared part subtracted when counting the union?', ('Чтобы не посчитать дважды', 'To avoid counting it twice'), ('Это правило без причины', 'It is a rule without a reason'), ('Чтобы число стало меньше', 'To make the number smaller'), ('Общая часть входит в оба множества.', 'The shared part belongs to both sets.')),
  Q('Следующий член ряда 1, 1, 2, 3, 5, …', 'The next term of 1, 1, 2, 3, 5, …', '8', '7', '6', ('3 + 5 = 8.', '3 + 5 = 8.'))],
 src=[('Wikipedia: Sequence', 'https://en.wikipedia.org/wiki/Sequence'), ('Wikipedia: Venn diagram', 'https://en.wikipedia.org/wiki/Venn_diagram')])
