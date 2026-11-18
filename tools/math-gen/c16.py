# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Неправильная дробь и смешанное число', 'Improper fraction and mixed number'),
 [('r', 'n', 'Числитель', 'Numerator', 1, 25, 1, 7), ('r', 'd', 'Знаменатель', 'Denominator', 2, 8, 1, 4)],
 [('Дробь', 'Fraction'), ('Целых лепёшек', 'Whole flatbreads'), ('Смешанное число', 'Mixed number'), ('Вид дроби', 'Kind of fraction')],
 'Каждая лепёшка разрезана на d частей. Берём n частей: собираем целые лепёшки и остаток.', 'Each flatbread is cut into d pieces. We take n pieces: we collect whole flatbreads and a remainder.', ('Лепёшки, разрезанные на части', 'Flatbreads cut into pieces'),
 r'''const n=v.n,d=v.d,tot=Math.ceil(n/d);let g="";const w=84,h=30;
 for(let b=0;b<tot;b++){const cx=24+(b%6)*92,cy=22+Math.floor(b/6)*60;for(let j=0;j<d;j++){const idx=b*d+j;g+=R(cx+j*w/d,cy,w/d,h,idx<n?COL.a:COL.bg,COL.ink,1.2)}}
 const w0=Math.floor(n/d),r=n%d;return {svg:g,st:[frStr(n,d),w0,mixed(n,d),n<d?U("правильная","proper"):U("неправильная","improper")],fb:n<d?U("Числитель меньше знаменателя — меньше одной лепёшки.","The numerator is less than the denominator — less than one flatbread."):U(frStr(n,d)+" = "+w0+" и "+(r?frStr(r,d):"ничего")+": "+n+" : "+d+" = "+w0+" (ост. "+r+").",frStr(n,d)+" = "+w0+" and "+(r?frStr(r,d):"nothing")+": "+n+" : "+d+" = "+w0+" (rem. "+r+").")}''')

m2 = M(('Сокращение дроби', 'Simplifying a fraction'),
 [('r', 'n', 'Числитель', 'Numerator', 1, 24, 1, 6), ('r', 'd', 'Знаменатель', 'Denominator', 2, 24, 1, 8)],
 [('НОД числителя и знаменателя', 'GCD of numerator and denominator'), ('Сокращённая дробь', 'Simplified fraction'), ('Результат', 'Result')],
 'Делим числитель и знаменатель на НОД — величина дроби не меняется, а запись становится проще.', 'We divide the numerator and the denominator by the GCD — the value does not change but the notation gets simpler.', ('Две записи одной дроби', 'Two notations of one fraction'),
 r'''const n=v.n,d=v.d,g0=gcd(n,d),n2=n/g0,d2=d/g0;let g="";
 if(n<=d){[[n,d,40],[n2,d2,130]].forEach(r=>{for(let j=0;j<r[1];j++)g+=R(50+j*500/r[1],r[2],500/r[1],50,j<r[0]?COL.a:COL.bg,COL.ink,1.2);g+=TX(50,r[2]-6,frStr(r[0],r[1]),COL.ink,16,"start",600)})}
 else g+=TX(300,110,frStr(n,d)+" = "+frStr(n2,d2),COL.ink,34,"middle",600)+TX(300,150,U("неправильная дробь: "+mixed(n2,d2),"improper fraction: "+mixed(n2,d2)),COL.mut,16);
 g+=TX(300,222,frStr(n,d)+" : "+g0+" = "+frStr(n2,d2),COL.b,22,"middle",600);
 return {svg:g,st:[g0,frStr(n2,d2),g0===1?U("несократима","irreducible"):U("сократили в "+g0+" раз(а)","reduced by "+g0)],fb:g0===1?U("НОД = 1: дробь уже несократима.","GCD = 1: the fraction is already irreducible."):U("Делим на "+g0+": "+n+" : "+g0+" = "+n2+" и "+d+" : "+g0+" = "+d2+".","Dividing by "+g0+": "+n+" : "+g0+" = "+n2+" and "+d+" : "+g0+" = "+d2+".")}''')

m3 = M(('Дроби на числовой прямой', 'Fractions on the number line'),
 [('r', 'a', 'Первая дробь: числитель', 'First fraction: numerator', 0, 12, 1, 1), ('r', 'b', 'Первая дробь: знаменатель', 'First fraction: denominator', 2, 8, 1, 3), ('r', 'c', 'Вторая дробь: числитель', 'Second fraction: numerator', 0, 12, 1, 3), ('r', 'e', 'Вторая дробь: знаменатель', 'Second fraction: denominator', 2, 8, 1, 4)],
 [('Сравнение', 'Comparison'), ('Дробь посередине', 'A fraction in the middle'), ('Её значение', 'Its value')],
 'Дроби — это точки на числовой прямой: правее — больше. Между любыми двумя разными дробями есть ещё дробь.', 'Fractions are points on the number line: further right means greater. Between any two different fractions there is another one.', ('Числовая прямая от 0 до 3', 'A number line from 0 to 3'),
 r'''const x=v.a/v.b,y=v.c/v.e,X=t=>40+t/3*520;let g=numLine(40,560,140,0,3,1,1);
 for(let t=0;t<=3;t+=0.25)if(Math.abs(t-Math.round(t))>1e-9)g+=L(X(t),135,X(t),145,COL.mut,1);
 const mid=(v.a*v.e+v.c*v.b),md=2*v.b*v.e,gg=gcd(mid,md);g+=C(X(x),140,9,COL.a)+TX(X(x),105,frStr(v.a,v.b),COL.a,14,"middle",600)+C(X(y),140,9,COL.b)+TX(X(y),85,frStr(v.c,v.e),COL.b,14,"middle",600);
 if(Math.abs(x-y)>1e-9)g+=C(X((x+y)/2),140,6,COL.c)+TX(X((x+y)/2),175,frStr(mid/gg,md/gg),COL.c,14,"middle",600);
 const s=Math.abs(x-y)<1e-9?"=":x<y?"&lt;":"&gt;";return {svg:g,st:[frStr(v.a,v.b)+" "+s+" "+frStr(v.c,v.e),Math.abs(x-y)<1e-9?"—":frStr(mid/gg,md/gg),fnum((x+y)/2,3)],fb:Math.abs(x-y)<1e-9?U("Дроби равны: это одна и та же точка.","The fractions are equal: it is the same point."):U("Полусумма "+frStr(mid/gg,md/gg)+" лежит ровно между дробями.","The half-sum "+frStr(mid/gg,md/gg)+" lies exactly between the fractions.")}''')

chapter('16', '16-common-fractions.html', 'III', ('Обыкновенные дроби', 'Common fractions'),
 ('Что делать, когда дробь больше единицы, как сокращать дроби и где они живут на числовой прямой.', 'What to do when a fraction is greater than one, how to simplify fractions and where they live on the number line.'),
 ('Хозяйка разрезала каждую лепёшку на 4 равные части. К обеду съели 7 таких частей.\n\nСколько это лепёшек? Как записать это число, если дробью 7/4 неудобно?', 'A hostess cut every flatbread into 4 equal pieces. At lunch 7 of these pieces were eaten.\n\nHow many flatbreads is that? How can we write the number if the fraction 7/4 is awkward?'),
 ('Разгадка: 1 ¾ лепёшки', 'The answer: 1¾ flatbreads'),
 ('7 четвертей — это 4 четверти (целая лепёшка) и ещё 3 четверти: 7/4 = 1 3/4. Деление с остатком: 7 : 4 = 1 (ост. 3). Целое — частное, остаток — числитель дробной части. Такую запись называют <strong>смешанным числом</strong>.', '7 quarters are 4 quarters (one whole flatbread) and 3 more quarters: 7/4 = 1 3/4. Division with remainder: 7 : 4 = 1 (rem. 3). The whole part is the quotient and the remainder is the numerator of the fractional part. Such a notation is called a <strong>mixed number</strong>.'),
 [S('mixed', 'Правильные и неправильные дроби', 'Proper and improper fractions', ('Дробь <strong>правильная</strong>, если числитель меньше знаменателя (она меньше 1). Если числитель не меньше знаменателя, дробь <strong>неправильная</strong> (не меньше 1). Чтобы выделить целую часть, делим числитель на знаменатель с остатком: 11/4 = 2 3/4, потому что 11 = 4 · 2 + 3. Обратно: 2 3/4 = (2 · 4 + 3)/4 = 11/4.', 'A fraction is <strong>proper</strong> if the numerator is less than the denominator (it is less than 1). If the numerator is not less than the denominator, the fraction is <strong>improper</strong> (at least 1). To extract the whole part we divide the numerator by the denominator with remainder: 11/4 = 2 3/4 because 11 = 4 · 2 + 3. Backwards: 2 3/4 = (2 · 4 + 3)/4 = 11/4.'),
    ('n/d = целая часть + остаток/d', '7/4 = 1 3/4', '7/4 = 1 3/4'), m1),
  S('simp', 'Сокращение дробей', 'Simplifying fractions', ('Если числитель и знаменатель разделить на одно и то же число, дробь не изменится: 6/8 = 3/4. Это <strong>основное свойство дроби</strong>. Делят на НОД — тогда получается <strong>несократимая</strong> дробь. Обратное — приведение к большему знаменателю: 3/4 = 6/8 = 9/12.', 'If the numerator and the denominator are divided by the same number, the fraction does not change: 6/8 = 3/4. This is the <strong>basic property of a fraction</strong>. We divide by the GCD — then the fraction is <strong>irreducible</strong>. The reverse is bringing to a larger denominator: 3/4 = 6/8 = 9/12.'),
    ('a/b = (a : k)/(b : k)', 'k — общий делитель', 'k is a common divisor'), m2),
  S('line', 'Дроби на числовой прямой', 'Fractions on the number line', ('Каждая дробь — точка на числовой прямой. 3/4 стоит между 0 и 1, 7/4 — между 1 и 2. Чем правее точка, тем больше дробь. Между любыми двумя разными дробями можно найти ещё одну, например их полусумму. Поэтому дробей между числами бесконечно много.', 'Every fraction is a point on the number line. 3/4 stands between 0 and 1, 7/4 between 1 and 2. The further right the point, the greater the fraction. Between any two different fractions we can find another, for example their half-sum. So there are infinitely many fractions between two numbers.'),
    ('(a + b) : 2', 'число между a и b', 'a number between a and b'), m3)],
 [TK(('Смешанное число', 'Mixed number'), ('Запишите 17/5 смешанным числом.', 'Write 17/5 as a mixed number.'), '17 : 5', '17 = 5 · 3 + 2, значит 17/5 = 3 2/5.', ('3 2/5.', '3 2/5.')),
  TK(('Обратно', 'Backwards'), ('Запишите 2 3/8 неправильной дробью.', 'Write 2 3/8 as an improper fraction.'), '2 3/8', '(2 · 8 + 3)/8 = 19/8.', '19/8.'),
  TK(('Сократить', 'Simplify'), ('Сократите 18/24.', 'Simplify 18/24.'), 'НОД(18, 24) = 6', '18 : 6 = 3 и 24 : 6 = 4.', ('3/4.', '3/4.')),
  TK(('Равные дроби', 'Equal fractions'), ('Какое число должно стоять вместо □: 2/5 = □/20?', 'What number goes in □: 2/5 = □/20?'), '5 · 4 = 20', 'Знаменатель умножили на 4, значит и числитель: 2 · 4 = 8.', '8.'),
  TK(('Что больше', 'Which is greater'), ('Сравните 5/6 и 7/9.', 'Compare 5/6 and 7/9.'), '5/6 и 7/9', 'Общий знаменатель 18: 5/6 = 15/18, 7/9 = 14/18. 15 &gt; 14.', ('5/6 &gt; 7/9.', '5/6 &gt; 7/9.'))],
 [Q('Какая дробь неправильная?', 'Which fraction is improper?', '9/4', '3/4', '4/9', ('Числитель больше знаменателя.', 'The numerator is greater than the denominator.')),
  Q('7/4 =', '7/4 =', '1 3/4', '1 4/7', '3 1/4', ('7 = 4 · 1 + 3.', '7 = 4 · 1 + 3.')),
  Q('Сократите 6/8.', 'Simplify 6/8.', '3/4', '2/3', '6/4', ('Делим на 2.', 'Divide by 2.')),
  Q('2 1/3 =', '2 1/3 =', '7/3', '3/2', '6/3', ('(2 · 3 + 1)/3.', '(2 · 3 + 1)/3.')),
  Q('Что больше: 3/4 или 2/3?', 'Which is greater: 3/4 or 2/3?', '3/4', '2/3', ('Равны', 'Equal'), ('9/12 &gt; 8/12.', '9/12 &gt; 8/12.')),
  Q('Дробь 5/7 сократить можно?', 'Can 5/7 be simplified?', ('Нет: НОД(5, 7) = 1', 'No: GCD(5, 7) = 1'), ('Да, на 5', 'Yes, by 5'), ('Да, на 7', 'Yes, by 7'), ('Общих делителей, кроме 1, нет.', 'There are no common divisors except 1.')),
  Q('Сколько целых в 13/4?', 'How many whole ones are in 13/4?', '3', '13', '4', ('13 : 4 = 3 (ост. 1).', '13 : 4 = 3 (rem. 1).')),
  Q('Между 1/2 и 1 лежит дробь', 'Between 1/2 and 1 lies the fraction', '3/4', '1/4', '5/4', ('Полусумма: (1/2 + 1) : 2 = 3/4.', 'Half-sum: (1/2 + 1) : 2 = 3/4.'))],
 src=[('Wikipedia: Fraction', 'https://en.wikipedia.org/wiki/Fraction'), ('Wikipedia: Mixed number', 'https://en.wikipedia.org/wiki/Fraction#Mixed_numbers')])
