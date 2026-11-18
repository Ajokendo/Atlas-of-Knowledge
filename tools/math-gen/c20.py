# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Процент от числа', 'A percentage of a number'),
 [('r', 'T', 'Число', 'The number', 10, 1000, 10, 200), ('r', 'p', 'Процентов', 'Percent', 1, 100, 1, 25)],
 [('Процент как дробь', 'Percent as a fraction'), ('Результат', 'Result'), ('Оставшаяся часть', 'The remaining part')],
 '1 % — это одна сотая. Закрасим p клеток из 100: это p % всей полосы.', '1% is one hundredth. We shade p cells of 100: that is p% of the whole strip.', ('Сетка из 100 клеток', 'A grid of 100 cells'),
 r'''let g="";for(let i=0;i<100;i++){const c=i%25,r=Math.floor(i/25);g+=R(25+c*22,20+r*22,20,20,i<v.p?COL.a:COL.bg,COL.line,1,2)}
 const val=v.T*v.p/100;g+=TX(330+130,60,v.p+" %",COL.a,34,"start",700)+TX(330+130,100,"= "+frStr(v.p,100),COL.ink,18,"start")+TX(300,150,U(v.p+" % от "+v.T+" = "+fnum(val,2),v.p+"% of "+v.T+" = "+fnum(val,2)),COL.ink,24,"middle",600);
 return {svg:g,st:[v.p+"/100 = "+fnum(v.p/100,2),fnum(val,2),fnum(v.T-val,2)],fb:U(v.T+" · "+v.p+" : 100 = "+fnum(val,2)+".",v.T+" · "+v.p+" : 100 = "+fnum(val,2)+".")}''', '0 0 600 150')

m2 = M(('Скидка и надбавка', 'Discount and increase'),
 [('r', 'P', 'Старая цена', 'Old price', 100, 5000, 50, 1500), ('r', 'p', 'Процентов', 'Percent', 1, 90, 1, 20), ('s', 'k', 'Что происходит', 'What happens', ['скидка', 'надбавка'], ['discount', 'increase'], 0)],
 [('Изменение цены', 'Change in price'), ('Новая цена', 'New price'), ('Множитель', 'Multiplier')],
 'Скидка на p % — цена умножается на (1 − p/100); надбавка на p % — на (1 + p/100).', 'A discount of p% multiplies the price by (1 − p/100); an increase of p% multiplies it by (1 + p/100).', ('Старая и новая цена', 'The old and the new price'),
 r'''const s=v.k===0?-1:1,m=1+s*v.p/100,N=v.P*m,mx=Math.max(v.P,N);let g=R(60,50,v.P/mx*440,40,COL.b,COL.ink,1.5,3)+R(60,120,N/mx*440,40,s<0?COL.c:COL.a,COL.ink,1.5,3)+TX(60,40,U("было","was")+" "+v.P,COL.ink,15,"start",600)+TX(60,110,U("стало","now")+" "+fnum(N,2),COL.ink,15,"start",600);
 return {svg:g,st:[(s<0?"−":"+")+fnum(v.P*v.p/100,2),fnum(N,2),fnum(m,2)],fb:U(v.P+" · "+fnum(m,2)+" = "+fnum(N,2)+".",v.P+" · "+fnum(m,2)+" = "+fnum(N,2)+".")}''', '0 0 600 190')

m3 = M(('Какую часть составляет число', 'What part one number is of another'),
 [('r', 'a', 'Часть', 'The part', 1, 200, 1, 30), ('r', 'b', 'Целое', 'The whole', 10, 200, 1, 120)],
 [('Отношение', 'Ratio'), ('В процентах', 'In percent'), ('Целое составляет', 'The whole is')],
 'Часть в процентах: делим часть на целое и умножаем на 100.', 'The part in percent: divide the part by the whole and multiply by 100.', ('Часть и целое', 'The part and the whole'),
 r'''const a=Math.min(v.a,v.b*3),b=v.b,pc=a/b*100;let g=R(60,50,440,40,COL.bg,COL.ink,2,3)+R(60,50,Math.min(440,a/b*440),40,COL.a,COL.ink,2,3)+TX(60,40,U("целое "+b,"whole "+b),COL.ink,14,"start")+TX(60,125,U("часть "+a+" = "+fnum(pc,1)+" %","part "+a+" = "+fnum(pc,1)+"%"),COL.a,22,"start",700);
 return {svg:g,st:[frStr(a,b),fnum(pc,1)+" %","100 %"],fb:pc>100?U("Часть больше целого — больше 100 %.","The part exceeds the whole — more than 100%."):U(a+" : "+b+" · 100 = "+fnum(pc,1)+" %.",a+" : "+b+" · 100 = "+fnum(pc,1)+"%.")}''', '0 0 600 150')

chapter('20', '20-percent.html', 'III', ('Проценты', 'Percentages'),
 ('Как находить процент от числа, считать скидки и надбавки и выяснять, какую часть одно число составляет от другого.', 'How to find a percentage of a number, calculate discounts and increases and tell what part one number is of another.'),
 ('В магазине куртка стоила 4 000 сомов. Цену сначала повысили на 25 %, а через неделю снизили на 25 %.\n\nВернулась ли куртка к прежней цене?', 'In a shop a jacket cost 4,000 som. The price was first raised by 25%, and a week later lowered by 25%.\n\nDid the jacket return to its old price?'),
 ('Разгадка: нет, она стоит 3 750 сомов', 'The answer: no, it costs 3,750 som'),
 ('После повышения: 4 000 · 1,25 = 5 000. Скидка 25 % — от <em>новой</em> цены 5 000: 5 000 · 0,75 = 3 750. Проценты всегда считаются от текущей цены, поэтому «+25 %, потом −25 %» не отменяют друг друга. Множители: 1,25 · 0,75 = 0,9375 — итоговая цена 93,75 % от прежней.', 'After the increase: 4,000 · 1.25 = 5,000. The 25% discount is taken from the <em>new</em> price 5,000: 5,000 · 0.75 = 3,750. Percentages are always taken from the current price, so “+25%, then −25%” do not cancel. The multipliers: 1.25 · 0.75 = 0.9375 — the final price is 93.75% of the original.'),
 [S('of', 'Процент от числа', 'A percentage of a number', ('<strong>Процент</strong> — одна сотая часть: 1 % = 1/100 = 0,01. Чтобы найти p % от числа T, умножают T на p/100. Например, 15 % от 200 — это 200 · 0,15 = 30. Полезно помнить: 50 % — половина, 25 % — четверть, 10 % — сдвиг запятой на один знак.', 'A <strong>percent</strong> is one hundredth: 1% = 1/100 = 0.01. To find p% of a number T we multiply T by p/100. For example, 15% of 200 is 200 · 0.15 = 30. Worth remembering: 50% is a half, 25% a quarter, 10% a shift of the point by one place.'),
    ('p % от T = T · p/100', '', 'p% of T = T · p/100'), m1),
  S('disc', 'Скидки и надбавки', 'Discounts and increases', ('Если цена изменилась на p %, новую цену получают умножением: при скидке на (1 − p/100), при надбавке на (1 + p/100). Двойное изменение — произведение множителей. Поэтому процент от процента не складывается: сначала −20 %, потом +20 % даёт 0,8 · 1,2 = 0,96, то есть цена стала на 4 % ниже.', 'If a price changes by p%, the new price is got by multiplication: for a discount by (1 − p/100), for an increase by (1 + p/100). A double change is the product of multipliers. So percentages do not add: first −20%, then +20% gives 0.8 · 1.2 = 0.96, which means the price became 4% lower.'),
    ('новая цена = цена · (1 ± p/100)', '', 'new price = price · (1 ± p/100)'), m2),
  S('part', 'Какую часть составляет число', 'What part one number is', ('Чтобы узнать, сколько процентов a составляет от b, делим a на b и умножаем на 100: (a : b) · 100 %. Если в классе 30 учеников, а 12 из них ходят в кружок, то это 12 : 30 · 100 = 40 %. Часть может быть больше целого — тогда процентов больше 100.', 'To find what percent a is of b we divide a by b and multiply by 100: (a : b) · 100%. If a class has 30 pupils and 12 of them attend a club, that is 12 : 30 · 100 = 40%. The part may be bigger than the whole — then the percentage exceeds 100.'),
    ('a от b = a : b · 100 %', '', 'a of b = a : b · 100%'), m3)],
 [TK(('Процент от числа', 'A percentage'), ('Найдите 15 % от 240.', 'Find 15% of 240.'), '240 · 0,15', '10 % = 24, 5 % = 12, итого 36.', '36.'),
  TK(('Скидка', 'Discount'), ('Книга стоит 800 сомов. Скидка 30 %. Сколько заплатим?', 'A book costs 800 som. The discount is 30%. How much will we pay?'), '800 · 0,7', '800 · 0,7 = 560.', ('560 сомов.', '560 som.')),
  TK(('Какую часть', 'What part'), ('В классе 25 учеников, 20 из них — на экскурсии. Сколько это процентов?', 'A class has 25 pupils, 20 of them are on a trip. What percent is that?'), '20 : 25', '20 : 25 = 0,8 = 80 %.', '80 %.'),
  TK(('Надбавка', 'Increase'), ('Цена 500 сомов выросла на 12 %. Новая цена?', 'A price of 500 som rose by 12%. What is the new price?'), '500 · 1,12', '500 · 1,12 = 560.', ('560 сомов.', '560 som.')),
  TK(('Найти целое', 'Find the whole'), ('20 % числа равны 30. Найдите число.', '20% of a number is 30. Find the number.'), '30 : 0,2', '30 : 0,2 = 150. Проверка: 150 · 0,2 = 30.', '150.')],
 [Q('10 % от 350 равно', '10% of 350 is', '35', '3,5', '350', ('Делим на 10.', 'Divide by 10.')),
  Q('50 % — это', '50% is', ('половина', 'a half'), ('четверть', 'a quarter'), ('десятая часть', 'a tenth'), ('50/100 = 1/2.', '50/100 = 1/2.')),
  Q('Цена 200, скидка 25 %. Новая цена', 'Price 200, discount 25%. New price', '150', '175', '50', ('200 · 0,75.', '200 · 0,75.')),
  Q('12 от 48 — это', '12 out of 48 is', '25 %', '12 %', '40 %', ('12 : 48 = 0,25.', '12 : 48 = 0.25.')),
  Q('+10 %, затем −10 %: цена', '+10%, then −10%: the price', ('стала меньше исходной', 'is below the original'), ('вернулась', 'returned'), ('выросла', 'went up'), ('1,1 · 0,9 = 0,99.', '1.1 · 0.9 = 0.99.')),
  Q('0,07 в процентах', '0.07 in percent', '7 %', '0,7 %', '70 %', ('0,07 = 7/100.', '0.07 = 7/100.')),
  Q('Можно ли получить больше 100 %?', 'Can we get more than 100%?', ('Да, если часть больше целого', 'Yes, if the part exceeds the whole'), ('Нет, никогда', 'No, never'), ('Только в банке', 'Only in a bank'), ('150 от 100 — это 150 %.', '150 of 100 is 150%.')),
  Q('Увеличить число на 100 % — значит', 'Increasing a number by 100% means', ('удвоить его', 'doubling it'), ('оставить прежним', 'keeping it'), ('утроить', 'tripling it'), ('Множитель 1 + 1 = 2.', 'The multiplier 1 + 1 = 2.'))],
 src=[('Wikipedia: Percentage', 'https://en.wikipedia.org/wiki/Percentage')],
 note=('Цены и сюжет про куртку придуманы для атласа.', 'The prices and the jacket story are invented for the atlas.'))
