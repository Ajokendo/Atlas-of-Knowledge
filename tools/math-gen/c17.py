# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Сложение и вычитание дробей', 'Adding and subtracting fractions'),
 [('s', 'op', 'Действие', 'Operation', ['сложить', 'вычесть'], ['add', 'subtract'], 0), ('r', 'a', 'Первая дробь: числитель', 'First fraction: numerator', 1, 8, 1, 1), ('r', 'b', 'Первая дробь: знаменатель', 'First fraction: denominator', 2, 9, 1, 2), ('r', 'c', 'Вторая дробь: числитель', 'Second fraction: numerator', 1, 8, 1, 1), ('r', 'd', 'Вторая дробь: знаменатель', 'Second fraction: denominator', 2, 9, 1, 3)],
 [('Общий знаменатель', 'Common denominator'), ('Результат до сокращения', 'Result before simplifying'), ('Результат', 'Result')],
 'Складывать и вычитать можно только доли одного размера. Поэтому сначала приводим дроби к общему знаменателю (обычно НОК знаменателей).', 'We can only add or subtract pieces of the same size. So first we bring the fractions to a common denominator (usually the LCM of the denominators).', ('Дроби на одной шкале', 'Fractions on one scale'),
 r'''const b=v.b,d=v.d,a=Math.min(v.a,b),c=Math.min(v.c,d),Lc=lcm(b,d),n1=a*Lc/b,n2=c*Lc/d,add=v.op===0,r=add?n1+n2:n1-n2;let g="";
 const row=(y,val,col,lab)=>{g+=R(50,y,Math.max(1,val*250),34,col,COL.ink,1.2,3)+TX(46,y+23,lab,COL.ink,14,"end",600)};
 row(30,a/b,COL.a,frStr(a,b));row(80,c/d,COL.b,frStr(c,d));
 if(r>=0)row(140,r/Lc,COL.c,r===0?"0":frStr(r/gcd(r,Lc),Lc/gcd(r,Lc)));g+=L(50,25,50,185,COL.ink,2)+L(300,25,300,185,COL.mut,1)+TX(300,205,"1",COL.mut,12)+TX(550,205,"2",COL.mut,12)+L(550,25,550,185,COL.mut,1);
 if(r<0)return {svg:g+TX(300,160,U("Из меньшего большее вычесть нельзя","Cannot take the bigger from the smaller"),COL.a,16),st:[Lc,"—","—"],fb:U("Выберите вычитаемое меньше уменьшаемого.","Choose a subtrahend smaller than the minuend.")};
 const gg=r?gcd(r,Lc):1;return {svg:g,st:[Lc,frStr(n1,Lc)+(add?" + ":" − ")+frStr(n2,Lc)+" = "+frStr(r,Lc),r===0?"0":mixed(r/gg,Lc/gg)],fb:U("Общий знаменатель "+Lc+": "+frStr(a,b)+" = "+frStr(n1,Lc)+", "+frStr(c,d)+" = "+frStr(n2,Lc)+".","Common denominator "+Lc+": "+frStr(a,b)+" = "+frStr(n1,Lc)+", "+frStr(c,d)+" = "+frStr(n2,Lc)+".")}''')

m2 = M(('Умножение дробей: площадь', 'Multiplying fractions: area'),
 [('r', 'a', 'Первая дробь: числитель', 'First fraction: numerator', 1, 8, 1, 2), ('r', 'b', 'Первая дробь: знаменатель', 'First fraction: denominator', 2, 8, 1, 3), ('r', 'c', 'Вторая дробь: числитель', 'Second fraction: numerator', 1, 8, 1, 3), ('r', 'd', 'Вторая дробь: знаменатель', 'Second fraction: denominator', 2, 8, 1, 4)],
 [('Произведение', 'Product'), ('Сокращённо', 'Simplified'), ('Заштриховано клеток из', 'Shaded cells out of')],
 'Берём долю от доли. Единичный квадрат делим на b строк и d столбцов; пересечение — искомая часть.', 'We take a fraction of a fraction. The unit square is divided into b rows and d columns; the overlap is the part we want.', ('Единичный квадрат и пересечение долей', 'The unit square and the overlap of fractions'),
 r'''const b=v.b,d=v.d,a=Math.min(v.a,b),c=Math.min(v.c,d),S=190,x0=205,y0=30;let g="";
 for(let i=0;i<b;i++)for(let j=0;j<d;j++){const inA=i<a,inC=j<c;g+=R(x0+j*S/d,y0+i*S/b,S/d,S/b,inA&&inC?COL.a:inA?"#f4dfd8":inC?"#dbe5f2":"#fff",COL.line,1)}
 g+=R(x0,y0,S,S,"none",COL.ink,3)+TX(x0+S+14,y0+S/2,"= "+frStr(a*c,b*d),COL.ink,22,"start",600)+TX(x0-10,y0+S/2,frStr(a,b),COL.a,16,"end",600)+TX(x0+S/2,y0+S+22,frStr(c,d),COL.b,16,"middle",600);
 const n=a*c,m=b*d,gg=gcd(n,m);return {svg:g,st:[frStr(a,b)+" · "+frStr(c,d)+" = "+frStr(n,m),frStr(n/gg,m/gg),n+U(" из "," of ")+m],fb:U("Умножаем числители и знаменатели: "+a+" · "+c+" = "+n+", "+b+" · "+d+" = "+m+".","Multiply numerators and denominators: "+a+" · "+c+" = "+n+", "+b+" · "+d+" = "+m+".")}''')

m3 = M(('Деление на дробь', 'Dividing by a fraction'),
 [('r', 'N', 'Делимое (целое число)', 'Dividend (a whole number)', 1, 6, 1, 3), ('r', 'p', 'Числитель делителя', 'Numerator of the divisor', 1, 7, 1, 3), ('r', 'Dq', 'Знаменатель делителя', 'Denominator of the divisor', 2, 8, 1, 4)],
 [('Результат', 'Result'), ('Заменяем делением на обратную', 'Multiply by the reciprocal'), ('Полных порций и остаток', 'Full portions and remainder')],
 'Сколько раз по p/q помещается в N? Делим N единиц на доли по 1/q и собираем в порции по p долей.', 'How many portions of p/q fit into N? We cut N units into pieces of 1/q and gather them into portions of p pieces.', ('N единиц, разрезанных на доли и собранных в порции', 'N units cut into pieces and gathered into portions'),
 r'''const q2=v.Dq,p=Math.min(v.p,q2),N=v.N,cells=N*q2,cw=Math.min(36,540/cells);let g="";
 for(let i=0;i<cells;i++){const grp=Math.floor(i/p),full=(grp+1)*p<=cells;g+=R(30+i*cw,70,cw-1.5,50,full?(grp%2?COL.b:COL.a):"#d9d7cf",COL.bg,1,2)}
 for(let u=0;u<=N;u++)g+=L(30+u*q2*cw-0.7,62,30+u*q2*cw-0.7,128,COL.ink,2);
 const n=N*q2,m=p,gg=gcd(n,m),full=Math.floor(cells/p),rem=cells%p;
 g+=TX(300,170,N+" : "+frStr(p,q2)+" = "+N+" · "+frStr(q2,p)+" = "+mixed(n/gg,m/gg),COL.ink,22,"middle",600);
 return {svg:g,st:[mixed(n/gg,m/gg),N+" · "+frStr(q2,p),full+(rem?U(" и "+frStr(rem,p)," and "+frStr(rem,p)):"")],fb:U("В "+N+" ед. всего "+cells+" долей по 1/"+q2+"; порция — "+p+" долей: "+full+" полных порций"+(rem?" и "+rem+" лишних долей.":"."),N+" units hold "+cells+" pieces of 1/"+q2+"; a portion is "+p+" pieces: "+full+" full portions"+(rem?" and "+rem+" extra pieces.":"."))}''')

chapter('17', '17-fraction-operations.html', 'III', ('Действия с дробями', 'Operations with fractions'),
 ('Как складывать, вычитать, умножать и делить дроби — и почему делить на дробь значит умножать на перевёрнутую.', 'How to add, subtract, multiply and divide fractions — and why dividing by a fraction means multiplying by the flipped one.'),
 ('У хозяина 3 литра молока. Он наливает его в стаканы по 3/4 литра.\n\nСколько стаканов получится?', 'A host has 3 litres of milk. He pours it into glasses of 3/4 litre each.\n\nHow many glasses will he fill?'),
 ('Разгадка: 4 стакана', 'The answer: 4 glasses'),
 ('Нужно узнать, сколько раз 3/4 помещается в 3: 3 : 3/4. В каждом литре 4 четверти, в 3 литрах — 12 четвертей. Стакан — 3 четверти. 12 : 3 = 4. По правилу: 3 : 3/4 = 3 · 4/3 = 4. Деление на дробь — умножение на перевёрнутую дробь.', 'We need to find how many times 3/4 fits into 3: 3 : 3/4. Each litre has 4 quarters, 3 litres have 12 quarters. A glass is 3 quarters. 12 : 3 = 4. By the rule: 3 : 3/4 = 3 · 4/3 = 4. Dividing by a fraction is multiplying by the flipped fraction.'),
 [S('addsub', 'Сложение и вычитание', 'Adding and subtracting', ('Дроби с одинаковым знаменателем складывают и вычитают по числителям: 2/7 + 3/7 = 5/7. Если знаменатели разные, приводим к общему: 1/2 + 1/3 = 3/6 + 2/6 = 5/6. Результат сокращаем и, если можно, записываем смешанным числом.', 'Fractions with the same denominator are added and subtracted by their numerators: 2/7 + 3/7 = 5/7. If the denominators differ we bring them to a common one: 1/2 + 1/3 = 3/6 + 2/6 = 5/6. We simplify the result and, if possible, write it as a mixed number.'),
    ('a/c + b/c = (a + b)/c', 'знаменатель не складываем', 'the denominator is not added'), m1),
  S('mul', 'Умножение', 'Multiplication', ('Чтобы умножить дроби, умножают числители и знаменатели: 2/3 · 3/4 = 6/12 = 1/2. Смысл: «две трети от трёх четвертей». На картинке это пересечение двух полос единичного квадрата. Заранее можно сократить: в 2/3 · 3/4 двойку и четвёрку, тройку и тройку.', 'To multiply fractions we multiply the numerators and the denominators: 2/3 · 3/4 = 6/12 = 1/2. The meaning: “two thirds of three quarters”. On the picture it is the overlap of two strips in the unit square. We can cancel in advance: in 2/3 · 3/4 the two and four, the three and three.'),
    ('a/b · c/d = ac/bd', '', 'a/b · c/d = ac/bd'), m2),
  S('div', 'Деление', 'Division', ('Делить на дробь — значит умножать на <strong>обратную</strong> (перевёрнутую) дробь: a/b : c/d = a/b · d/c. Обратная к 3/4 — это 4/3. Убедиться можно на картинке: сколько порций по p/q в N единицах.', 'To divide by a fraction we multiply by the <strong>reciprocal</strong> (the flipped fraction): a/b : c/d = a/b · d/c. The reciprocal of 3/4 is 4/3. A picture confirms it: how many portions of p/q are in N units.'),
    ('a/b : c/d = a/b · d/c', '3 : 3/4 = 3 · 4/3 = 4', '3 : 3/4 = 3 · 4/3 = 4'), m3)],
 [TK(('Разные знаменатели', 'Different denominators'), ('Найдите 1/2 + 1/3.', 'Find 1/2 + 1/3.'), 'НОК(2, 3) = 6', '1/2 = 3/6, 1/3 = 2/6. 3/6 + 2/6 = 5/6.', ('5/6.', '5/6.')),
  TK(('Вычитание', 'Subtraction'), ('Найдите 3/4 − 1/6.', 'Find 3/4 − 1/6.'), 'НОК(4, 6) = 12', '3/4 = 9/12, 1/6 = 2/12. 9/12 − 2/12 = 7/12.', ('7/12.', '7/12.')),
  TK(('Умножение', 'Multiplication'), ('Найдите 2/3 · 3/4.', 'Find 2/3 · 3/4.'), '2/3 · 3/4', '(2 · 3)/(3 · 4) = 6/12 = 1/2. Или сразу сократим тройки: 2/4 = 1/2.', ('1/2.', '1/2.')),
  TK(('Деление', 'Division'), ('Найдите 5/6 : 5/12.', 'Find 5/6 : 5/12.'), '5/6 : 5/12', '5/6 · 12/5 = (5 · 12)/(6 · 5) = 60/30 = 2.', '2.'),
  TK(('Задача про банку', 'A jar problem'), ('Из бидона в 2 л молока взяли 3/8 л. Сколько осталось?', 'From a 2-litre milk can 3/8 litre was taken. How much is left?'), '2 − 3/8', '2 = 16/8, 16/8 − 3/8 = 13/8 = 1 5/8.', ('1 5/8 л.', '1 5/8 L.'))],
 [Q('1/5 + 2/5 =', '1/5 + 2/5 =', '3/5', '3/10', '2/5', ('Знаменатель сохраняем.', 'The denominator stays.')),
  Q('1/2 + 1/4 =', '1/2 + 1/4 =', '3/4', '2/6', '1/6', ('2/4 + 1/4 = 3/4.', '2/4 + 1/4 = 3/4.')),
  Q('1/2 · 1/3 =', '1/2 · 1/3 =', '1/6', '2/5', '5/6', ('1 · 1 = 1, 2 · 3 = 6.', '1 · 1 = 1, 2 · 3 = 6.')),
  Q('Обратная дробь к 3/4', 'The reciprocal of 3/4', '4/3', '3/4', '−3/4', ('Меняем числитель и знаменатель.', 'Swap numerator and denominator.')),
  Q('2 : 1/2 =', '2 : 1/2 =', '4', '1', '1/4', ('2 · 2 = 4: в двух единицах четыре половины.', '2 · 2 = 4: two units hold four halves.')),
  Q('3/4 − 1/4 =', '3/4 − 1/4 =', '1/2', '2/0', '2/4 + 1', ('2/4 = 1/2.', '2/4 = 1/2.')),
  Q('Что нужно сделать перед сложением дробей с разными знаменателями?', 'What must be done before adding fractions with different denominators?', ('Привести к общему знаменателю', 'Bring to a common denominator'), ('Сложить знаменатели', 'Add the denominators'), ('Ничего', 'Nothing'), ('Складывать можно доли одного размера.', 'Only pieces of the same size can be added.')),
  Q('3/5 от 20 равно', '3/5 of 20 equals', '12', '15', '8', ('20 : 5 · 3 = 12.', '20 : 5 · 3 = 12.'))],
 src=[('Wikipedia: Fraction (arithmetic with fractions)', 'https://en.wikipedia.org/wiki/Fraction#Arithmetic_with_fractions'), ('Wikipedia: Multiplicative inverse', 'https://en.wikipedia.org/wiki/Multiplicative_inverse')])
