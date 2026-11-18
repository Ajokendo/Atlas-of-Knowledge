# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Перестановки: n!', 'Permutations: n!'),
 [('r', 'n', 'Число предметов n', 'Number of objects n', 1, 5, 1, 4), ('r', 'i', 'Номер перестановки', 'Permutation number', 0, 119, 1, 5)],
 [('n! = 1·2·…·n', 'n! = 1·2·…·n'), ('Номер (по кругу)', 'Number (cyclic)'), ('Следующий ряд из n!', 'Next row of n!')],
 'Расставить n разных предметов в ряд можно n! способами: на первое место n вариантов, на второе n − 1 и т. д. Бегунок листает все расстановки по порядку.', 'n different objects can be put in a row in n! ways: n options for the first place, n − 1 for the second and so on. The slider pages through all arrangements in order.', ('Одна из расстановок', 'One of the arrangements'),
 r'''const N=v.n,tot=fact(N),idx=v.i%tot;let pool=[];for(let j=0;j<N;j++)pool.push(j);let k=idx,perm=[];for(let j=N;j>=1;j--){const f=fact(j-1),q2=Math.floor(k/f);k%=f;perm.push(pool.splice(q2,1)[0])}
 const cl=[COL.a,COL.b,COL.c,COL.ink,COL.mut],ch=["А","Б","В","Г","Д"];let g="";perm.forEach((p,j)=>{const x=300+(j-(N-1)/2)*80;g+=C(x,90,30,cl[p])+TX(x,98,ch[p],COL.bg,24,"middle",700)});
 return {svg:g,st:[N+"! = "+tot,(idx+1)+" / "+tot,(N+1)+"! = "+fact(N+1)],fb:U("Каждое новое место умножает число расстановок: 5! = 120, 10! уже 3 628 800.","Each new place multiplies the number of arrangements: 5! = 120, 10! is already 3,628,800.")}''', '0 0 600 150')

m2 = M(('Размещения и сочетания', 'Arrangements and combinations'),
 [('r', 'n', 'Всего n', 'Total n', 1, 12, 1, 6), ('r', 'k', 'Выбираем k', 'Choose k', 0, 12, 1, 3)],
 [('Размещения A = n!/(n−k)! (порядок важен)', 'Arrangements A = n!/(n−k)! (order matters)'), ('Сочетания C = n!/(k!(n−k)!)', 'Combinations C = n!/(k!(n−k)!)'), ('A = C·k!', 'A = C·k!')],
 'Если порядок выбранных важен (призёры соревнования) — размещения. Если важен лишь состав (команда) — сочетания: каждое сочетание даёт k! размещений.', 'If the order of the chosen matters (prize winners) — arrangements. If only the set matters (a team) — combinations: each combination gives k! arrangements.', ('Выбранные k из n', 'k chosen from n'),
 r'''const k=Math.min(v.k,v.n),n=v.n;let g="";for(let i=0;i<n;i++){const x=300+(i-(n-1)/2)*Math.min(44,520/n);g+=C(x,80,16,i<k?COL.b:COL.bg,COL.ink,2)+TX(x,86,String(i+1),i<k?COL.bg:COL.ink,14,"middle",700)}
 const A=fact(n)/fact(n-k),Cc=nCr(n,k);
 return {svg:g,st:[A.toLocaleString("ru-RU"),Cc.toLocaleString("ru-RU"),Cc+"·"+fact(k)+" = "+Cc*fact(k)],fb:k===0||k===n?U("C(n, 0) = C(n, n) = 1: выбрать «ничего» или «всё» можно одним способом.","C(n, 0) = C(n, n) = 1: choosing “nothing” or “everything” can be done in one way."):U("Из "+n+" выбрать "+k+": "+Cc+" составов; если ещё и расставить — "+A+".","From "+n+" choose "+k+": "+Cc+" selections; arranging them too — "+A+".")}''', '0 0 600 135')

m3 = M(('Треугольник Паскаля', 'Pascal’s triangle'),
 [('r', 'n', 'Строка n', 'Row n', 0, 8, 1, 6), ('r', 'k', 'Место k', 'Position k', 0, 8, 1, 2)],
 [('C(n, k)', 'C(n, k)'), ('Сумма строки = 2ⁿ', 'Row sum = 2ⁿ'), ('Коэффициент в (a + b)ⁿ', 'Coefficient in (a + b)ⁿ')],
 'Числа C(n, k) образуют треугольник: каждое равно сумме двух над ним. Сумма строки n равна 2ⁿ, а сами числа — коэффициенты разложения (a + b)ⁿ.', 'The numbers C(n, k) form a triangle: each equals the sum of the two above it. The sum of row n is 2ⁿ and the numbers are the coefficients of the expansion of (a + b)ⁿ.', ('Строки 0–8', 'Rows 0–8'),
 r'''const kk=Math.min(v.k,v.n);let g="";for(let r=0;r<=8;r++)for(let c=0;c<=r;c++){const x=300+(c-r/2)*52,y=22+r*27,sel=(r===v.n&&c===kk),inrow=(r===v.n);g+=(sel?C(x,y-5,14,COL.b):inrow?C(x,y-5,14,COL.a+"44"):"")+TX(x,y,String(nCr(r,c)),sel?COL.bg:COL.ink,13,"middle",sel?700:400)}
 return {svg:g,st:[nCr(v.n,kk),Math.pow(2,v.n),nCr(v.n,kk)+"·a"+supn(v.n-kk)+"·b"+supn(kk)],fb:U("(a + b)"+supn(v.n)+" = Σ C("+v.n+", k)·aⁿ⁻ᵏ·bᵏ — здесь выбрано слагаемое с b в степени "+kk+".","(a + b)"+supn(v.n)+" = Σ C("+v.n+", k)·aⁿ⁻ᵏ·bᵏ — the term with b to the power "+kk+" is chosen.")}''', '0 0 600 245')

chapter('70', '70-combinatorics.html', 'X', ('Перестановки, размещения, сочетания', 'Permutations, arrangements, combinations'),
 ('Факториал, различие «порядок важен — не важен», числа C(n, k) и треугольник Паскаля.', 'The factorial, the difference between “order matters” and “order does not”, the numbers C(n, k) and Pascal’s triangle.'),
 ('В классе 20 учеников. Нужно выбрать команду из 3 для олимпиады. Сколько существует разных команд? А если надо ещё назначить капитана, вице-капитана и запасного?', 'A class has 20 students. A team of 3 is to be chosen for an olympiad. How many different teams exist? And if a captain, vice-captain and reserve must also be assigned?'),
 ('Разгадка: 1140 команд и 6840 назначений', 'The answer: 1140 teams and 6840 assignments'),
 ('Если важен только состав, это сочетания: C(20, 3) = 20·19·18 / (1·2·3) = 1140. Если важна ещё и роль, порядок существен: размещения A(20, 3) = 20·19·18 = 6840. Размещений в 3! = 6 раз больше, чем сочетаний: одну и ту же тройку можно «разыграть по ролям» шестью способами.', 'If only the membership matters these are combinations: C(20, 3) = 20·19·18 / (1·2·3) = 1140. If the role matters too, order is essential: arrangements A(20, 3) = 20·19·18 = 6840. There are 3! = 6 times as many arrangements as combinations: the same trio can be “cast into roles” in six ways.'),
 [S('perm', 'Перестановки и факториал', 'Permutations and the factorial', ('<strong>n! = 1 · 2 · … · n</strong> — число перестановок n разных предметов; 0! = 1. Рост очень быстрый: 5! = 120, 10! = 3 628 800. Если среди предметов есть одинаковые, делят на факториалы их количеств: слово «МАМА» — 4!/(2!·2!) = 6 перестановок.', '<strong>n! = 1 · 2 · … · n</strong> is the number of permutations of n different objects; 0! = 1. The growth is very fast: 5! = 120, 10! = 3,628,800. If some objects are identical we divide by factorials of their counts: the word “MAMA” gives 4!/(2!·2!) = 6 permutations.'),
    ('Pₙ = n!', '', 'Pₙ = n!'), m1),
  S('comb', 'Размещения и сочетания', 'Arrangements and combinations', ('<strong>Размещения</strong> (порядок важен): A(n, k) = n!/(n − k)!. <strong>Сочетания</strong> (порядок не важен): <strong>C(n, k) = n! / (k!·(n − k)!)</strong>. Свойства: C(n, k) = C(n, n − k); C(n, 0) = 1; A(n, k) = C(n, k)·k!.', '<strong>Arrangements</strong> (order matters): A(n, k) = n!/(n − k)!. <strong>Combinations</strong> (order does not matter): <strong>C(n, k) = n! / (k!·(n − k)!)</strong>. Properties: C(n, k) = C(n, n − k); C(n, 0) = 1; A(n, k) = C(n, k)·k!.'),
    ('C(n, k) = n! / (k!(n − k)!)', '', 'C(n, k) = n! / (k!(n − k)!)'), m2),
  S('pas', 'Треугольник Паскаля и бином', 'Pascal’s triangle and the binomial', ('C(n, k) = C(n − 1, k − 1) + C(n − 1, k) — правило треугольника. Формула бинома Ньютона: <strong>(a + b)ⁿ = Σ C(n, k)·aⁿ⁻ᵏ·bᵏ</strong>. Например, (a + b)³ = a³ + 3a²b + 3ab² + b³ — коэффициенты 1, 3, 3, 1 — третья строка. Сумма строки n равна 2ⁿ: столько же подмножеств у n-элементного множества.', 'C(n, k) = C(n − 1, k − 1) + C(n − 1, k) — the triangle rule. Newton’s binomial formula: <strong>(a + b)ⁿ = Σ C(n, k)·aⁿ⁻ᵏ·bᵏ</strong>. For example (a + b)³ = a³ + 3a²b + 3ab² + b³ — the coefficients 1, 3, 3, 1 are the third row. The sum of row n is 2ⁿ: the number of subsets of an n-element set.'),
    ('(a + b)ⁿ = Σ C(n, k)aⁿ⁻ᵏbᵏ', '', '(a + b)ⁿ = Σ C(n, k)aⁿ⁻ᵏbᵏ'), m3)],
 [TK(('Факториал', 'Factorial'), ('Вычислите 6!/4!.', 'Compute 6!/4!.'), '', '6·5 = 30.', '30.'),
  TK(('Перестановки', 'Permutations'), ('Сколькими способами 5 учеников встанут в очередь?', 'In how many ways can 5 students line up?'), '', '5! = 120.', '120.'),
  TK(('Сочетания', 'Combinations'), ('Сколько способов выбрать 2 дежурных из 6?', 'In how many ways can 2 monitors be chosen from 6?'), '', 'C(6, 2) = 15.', '15.'),
  TK(('Размещения', 'Arrangements'), ('Сколько вариантов распределения золота, серебра, бронзы среди 8 участников?', 'How many ways to award gold, silver and bronze among 8 contestants?'), '', '8 · 7 · 6 = 336.', '336.'),
  TK(('Слово', 'A word'), ('Сколько различных перестановок букв слова «МАМА»?', 'How many different permutations of the letters of “MAMA”?'), '', '4!/(2!·2!) = 6.', '6.')],
 [Q('5! =', '5! =', '120', '25', '60', ('1·2·3·4·5.', '1·2·3·4·5.')),
  Q('0! =', '0! =', '1', '0', 'не определён', ('По определению.', 'By definition.')),
  Q('C(5, 2) =', 'C(5, 2) =', '10', '20', '7', ('5·4/2.', '5·4/2.')),
  Q('Когда порядок важен — это', 'When order matters it is', ('размещения', 'arrangements'), ('сочетания', 'combinations'), ('суммы', 'sums'), ('Определение.', 'Definition.')),
  Q('C(10, 1) =', 'C(10, 1) =', '10', '1', '9', ('Выбрать один из десяти.', 'Choose one of ten.')),
  Q('Сумма чисел строки n треугольника Паскаля', 'The sum of row n of Pascal’s triangle', '2ⁿ', 'n²', 'n!', ('Число подмножеств.', 'The number of subsets.')),
  Q('Сколько подмножеств у 3-элементного множества?', 'How many subsets has a 3-element set?', '8', '6', '9', ('2³.', '2³.')),
  Q('C(8, 3) =', 'C(8, 3) =', '56', '24', '336', ('8·7·6/6.', '8·7·6/6.'))],
 src=[('Wikipedia: Combination', 'https://en.wikipedia.org/wiki/Combination'), ('Wikipedia: Permutation', 'https://en.wikipedia.org/wiki/Permutation'), ('Wikipedia: Pascal’s triangle', 'https://en.wikipedia.org/wiki/Pascal%27s_triangle'), ('OpenStax: Introductory Statistics 2e', 'https://openstax.org/details/books/introductory-statistics-2e')],
 note=('Школьная олимпиада и числа в задачах придуманы для атласа.', 'The school olympiad and numbers in the exercises are invented for the atlas.'))
