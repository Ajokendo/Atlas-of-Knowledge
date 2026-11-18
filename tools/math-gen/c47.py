# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Арифметическая прогрессия', 'Arithmetic progression'),
 [('r', 'a1', 'Первый член a₁', 'First term a₁', -10, 20, 1, 3), ('r', 'd', 'Разность d', 'Difference d', -5, 8, 1, 4), ('r', 'n', 'Номер члена n', 'Term number n', 1, 15, 1, 10)],
 [('n-й член aₙ = a₁ + (n − 1)d', 'nth term aₙ = a₁ + (n − 1)d'), ('Первые 6 членов', 'The first 6 terms'), ('Тип', 'Type')],
 'В арифметической прогрессии каждый следующий член больше предыдущего на одно и то же число d.', 'In an arithmetic progression each term is greater than the previous one by the same number d.', ('Члены прогрессии', 'The terms of the progression'),
 r'''const an=v.a1+(v.n-1)*v.d;const G=Gr({x0:0,x1:16,y0:-20,y1:80,L:80,T:10,W:460,H:210});let g=G.grid(2,20);for(let k=1;k<=15;k++)g+=G.pt(k,v.a1+(k-1)*v.d,k===v.n?COL.a:COL.b,k===v.n?8:4);g+=G.seg(1,v.a1,15,v.a1+14*v.d,COL.mut,1);
 const first=[0,1,2,3,4,5].map(i=>v.a1+i*v.d).join(", ");return {svg:g,st:[v.a1+" + "+(v.n-1)+"·"+v.d+" = "+an,first+", …",v.d>0?U("возрастающая","increasing"):v.d<0?U("убывающая","decreasing"):U("постоянная","constant")],fb:U("Точки лежат на одной прямой: линейная зависимость от номера.","The points lie on one line: a linear dependence on the number.")}''', '0 0 600 250')

m2 = M(('Сумма n членов', 'The sum of n terms'),
 [('r', 'a1', 'Первый член', 'First term', 1, 10, 1, 1), ('r', 'd', 'Разность', 'Difference', 1, 6, 1, 1), ('r', 'n', 'Число членов', 'Number of terms', 2, 20, 1, 10)],
 [('Формула', 'Formula'), ('Сумма', 'The sum'), ('Проверка сложением', 'Check by adding')],
 'Складываем ряд сам с собой в обратном порядке: все пары дают одинаковую сумму a₁ + aₙ, пар n, а сумма вдвое меньше.', 'We add the series to itself reversed: all pairs give the same sum a₁ + aₙ, there are n pairs and the sum is half.', ('Прямая и обратная записи', 'Forward and reversed lists'),
 r'''const a=[];for(let i=0;i<v.n;i++)a.push(v.a1+i*v.d);const an=a[v.n-1],S=(v.a1+an)*v.n/2;const w=Math.min(36,520/v.n);let g="";
 a.forEach((x,i)=>{g+=R(40+i*w,40,w-3,34,COL.bg,COL.line,1.5,3)+TX(40+i*w+w/2-1,62,x,COL.ink,Math.min(13,w/2.4),"middle",600)+R(40+i*w,90,w-3,34,"#fdf0c8",COL.line,1.5,3)+TX(40+i*w+w/2-1,112,a[v.n-1-i],COL.ink,Math.min(13,w/2.4),"middle",600)+TX(40+i*w+w/2-1,150,v.a1+an,COL.a,Math.min(12,w/2.6),"middle",700)});
 g+=TX(300,190,"2S = "+v.n+" · "+(v.a1+an)+" = "+v.n*(v.a1+an),COL.ink,18,"middle",700);
 return {svg:g,st:["S = (a₁ + aₙ)·n / 2",String(S),a.reduce((x,y)=>x+y,0)+""],fb:U("Одна и та же сумма a₁ + aₙ = "+(v.a1+an)+" в каждой из "+v.n+" пар.","The same sum a₁ + aₙ = "+(v.a1+an)+" in each of the "+v.n+" pairs.")}''', '0 0 600 205')

m3 = M(('Кресла в амфитеатре', 'Seats in an amphitheatre'),
 [('r', 'r1', 'Мест в первом ряду', 'Seats in the first row', 5, 30, 1, 12), ('r', 'd', 'Прибавка в каждом ряду', 'Extra seats per row', 1, 4, 1, 2), ('r', 'n', 'Число рядов', 'Number of rows', 3, 25, 1, 15)],
 [('Мест в последнем ряду', 'Seats in the last row'), ('Всего мест', 'Total seats'), ('Средняя вместимость ряда', 'Average per row')],
 'Каждый следующий ряд длиннее предыдущего на d мест — арифметическая прогрессия. Всего мест — сумма всех рядов.', 'Each next row is d seats longer than the previous one — an arithmetic progression. The total is the sum of all rows.', ('Ряды амфитеатра (условный пример)', 'Rows of an amphitheatre (illustrative example)'),
 r'''const last=v.r1+(v.n-1)*v.d,tot=(v.r1+last)*v.n/2;let g="";const mx=last;for(let i=0;i<v.n;i++){const w=(v.r1+i*v.d)/mx*480,hh=Math.min(10,190/v.n);g+=R(300-w/2,12+i*(hh+1.5),w,hh,i%2?COL.b:COL.a,"none",0,2)}
 return {svg:g,st:[last,tot,fnum(tot/v.n,1)],fb:U("Сумма = (первый + последний) · число рядов : 2 = ("+v.r1+" + "+last+") · "+v.n+" : 2.","Sum = (first + last) · number of rows : 2 = ("+v.r1+" + "+last+") · "+v.n+" : 2.")}''', '0 0 600 250')

chapter('47', '47-arithmetic-progression.html', 'VI', ('Последовательности и арифметическая прогрессия', 'Sequences and arithmetic progression'),
 ('Что такое числовая последовательность, как найти любой член арифметической прогрессии и как быстро сложить сто чисел подряд.', 'What a number sequence is, how to find any term of an arithmetic progression and how to add a hundred consecutive numbers quickly.'),
 ('Говорят, школьнику Карлу Гауссу учитель велел сложить все числа от 1 до 100, надеясь, что тот надолго занят. Мальчик ответил почти сразу.\n\nКак он посчитал?', 'The story goes that a teacher told the schoolboy Carl Gauss to add all numbers from 1 to 100, hoping to keep him busy for long. The boy answered almost at once.\n\nHow did he count?'),
 ('Разгадка: 5 050', 'The answer: 5,050'),
 ('Он заметил, что 1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101 и так далее: таких пар 50. Значит, сумма равна 50 · 101 = 5 050. Это формула суммы арифметической прогрессии: S = (a₁ + aₙ) · n / 2 = (1 + 100) · 100 / 2 = 5 050.', 'He noticed that 1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101 and so on: there are 50 such pairs. So the sum is 50 · 101 = 5,050. This is the formula for the sum of an arithmetic progression: S = (a₁ + aₙ) · n / 2 = (1 + 100) · 100 / 2 = 5,050.'),
 [S('def', 'Последовательность и прогрессия', 'Sequences and progressions', ('<strong>Числовая последовательность</strong> — числа, пронумерованные натуральными числами: a₁, a₂, a₃, … <strong>Арифметическая прогрессия</strong> — последовательность, в которой каждый член получается из предыдущего прибавлением одного и того же числа <em>d</em> (разности): aₙ = a₁ + (n − 1)d. Точки (n; aₙ) лежат на одной прямой.', 'A <strong>number sequence</strong> is numbers labelled by naturals: a₁, a₂, a₃, … An <strong>arithmetic progression</strong> is a sequence in which each term is got from the previous one by adding the same number <em>d</em> (the difference): aₙ = a₁ + (n − 1)d. The points (n; aₙ) lie on one line.'),
    ('aₙ = a₁ + (n − 1)d', '', 'aₙ = a₁ + (n − 1)d'), m1),
  S('sum', 'Сумма членов', 'The sum of terms', ('Сумма первых n членов <strong>S = (a₁ + aₙ)·n / 2</strong> или <strong>S = (2a₁ + (n − 1)d)·n / 2</strong>. Идея Гаусса: пары «первый + последний», «второй + предпоследний» дают одну и ту же сумму. Среднее арифметическое двух соседних членов равно члену между ними.', 'The sum of the first n terms <strong>S = (a₁ + aₙ)·n / 2</strong> or <strong>S = (2a₁ + (n − 1)d)·n / 2</strong>. Gauss’s idea: the pairs “first + last”, “second + second last” give the same sum. The arithmetic mean of two neighbouring terms equals the term between them.'),
    ('S = (a₁ + aₙ)·n/2', '', 'S = (a₁ + aₙ)·n/2'), m2),
  S('use', 'Применение', 'Applications', ('Арифметические прогрессии описывают равномерный рост: ряды в амфитеатре, ступени лестницы, равные ежемесячные взносы. Решая задачи, определяют, что известно: a₁, d, n, aₙ или S, и выбирают формулу.', 'Arithmetic progressions describe steady growth: rows in an amphitheatre, stair steps, equal monthly payments. In problems we determine what is known: a₁, d, n, aₙ or S, and choose a formula.'),
    ('1 + 2 + … + n = n(n + 1)/2', '', '1 + 2 + … + n = n(n + 1)/2'), m3)],
 [TK(('Член', 'A term'), ('a₁ = 5, d = 3. Найдите a₁₀.', 'a₁ = 5, d = 3. Find a₁₀.'), '', 'a₁₀ = 5 + 9 · 3 = 32.', '32.'),
  TK(('Разность', 'Difference'), ('В прогрессии a₁ = 2, a₅ = 18. Найдите d.', 'In a progression a₁ = 2, a₅ = 18. Find d.'), '18 = 2 + 4d', 'd = 4.', 'd = 4.'),
  TK(('Сумма', 'Sum'), ('Найдите сумму 1 + 2 + … + 100.', 'Find the sum 1 + 2 + … + 100.'), '', '101 · 50 = 5 050.', '5 050.'),
  TK(('Сумма n членов', 'Sum of n terms'), ('a₁ = 4, d = 2. Сумма первых 10 членов?', 'a₁ = 4, d = 2. The sum of the first 10 terms?'), 'a₁₀ = 22', '(4 + 22) · 10 / 2 = 130.', '130.'),
  TK(('Задача', 'A problem'), ('В первом ряду 10 мест, в каждом следующем на 2 больше. Сколько мест в 8 рядах?', 'The first row has 10 seats, each next has 2 more. How many seats in 8 rows?'), 'a₈ = 24', '(10 + 24) · 8 / 2 = 136.', '136.')],
 [Q('Разность прогрессии 3, 7, 11, …', 'The difference of the progression 3, 7, 11, …', '4', '3', '7', ('7 − 3.', '7 − 3.')),
  Q('a₁ = 1, d = 2. a₅ =', 'a₁ = 1, d = 2. a₅ =', '9', '10', '5', ('1 + 4 · 2.', '1 + 4 · 2.')),
  Q('Сумма 1 + 2 + … + 10', 'The sum 1 + 2 + … + 10', '55', '50', '100', ('11 · 5.', '11 · 5.')),
  Q('Точки (n; aₙ) арифметической прогрессии лежат на', 'The points (n; aₙ) of an arithmetic progression lie on', ('прямой', 'a line'), ('параболе', 'a parabola'), ('окружности', 'a circle'), ('aₙ линейна по n.', 'aₙ is linear in n.')),
  Q('В арифметической прогрессии со 2, 5, 8 следующий член', 'In the arithmetic progression 2, 5, 8 the next term is', '11', '10', '14', ('8 + 3.', '8 + 3.')),
  Q('Формула суммы', 'The sum formula', ('(a₁ + aₙ)·n/2', '(a₁ + aₙ)·n/2'), ('a₁·n', 'a₁·n'), ('aₙ·n', 'aₙ·n'), ('Идея Гаусса.', 'Gauss’s idea.')),
  Q('Прогрессия 10, 7, 4, …', 'The progression 10, 7, 4, …', ('убывающая', 'is decreasing'), ('возрастающая', 'is increasing'), ('постоянная', 'is constant'), ('d = −3.', 'd = −3.')),
  Q('Среднее двух соседних членов равно', 'The mean of two neighbouring terms equals', ('члену между ними', 'the term between them'), ('разности', 'the difference'), ('первому члену', 'the first term'), ('Свойство прогрессии.', 'A property of progressions.'))],
 src=[('Wikipedia: Arithmetic progression', 'https://en.wikipedia.org/wiki/Arithmetic_progression'), ('Wikipedia: Carl Friedrich Gauss', 'https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss')],
 note=('Рассказ о Гауссе — известная легенда; её подробности могут быть неточны. Амфитеатр придуман.', 'The Gauss story is a well-known legend; its details may be inaccurate. The amphitheatre is invented.'))
