# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Уравнение как весы', 'An equation as a balance'),
 [('r', 'a', 'Коэффициент a', 'Coefficient a', 1, 6, 1, 2), ('r', 'b', 'Число b', 'Number b', 0, 15, 1, 3), ('r', 'x', 'Ваш ответ x', 'Your answer x', 0, 15, 1, 4)],
 [('Уравнение', 'Equation'), ('Левая и правая чаши', 'Left and right pans'), ('Корень', 'The root')],
 'Уравнение a·x + b = c — весы. Если одинаково изменить обе чаши, равновесие сохранится. Подбирайте x, пока весы не уравновесятся.', 'The equation a·x + b = c is a balance. If both pans are changed equally the balance holds. Try x until the scale balances.', ('Весы', 'A balance scale'),
 r'''const c=v.a*5+v.b,L0=v.a*v.x+v.b,diff=L0-c,tilt=Math.max(-14,Math.min(14,diff*1.2));let g=L(300,80,300,190,COL.ink,6)+R(220,190,160,12,COL.ink,COL.ink,1,3);
 g+='<g transform="rotate('+tilt+' 300 80)">'+L(120,80,480,80,COL.ink,5)+'<g transform="rotate('+(-tilt)+' 120 80)">'+L(120,80,120,100,COL.ink,2)+R(60,100,120,36,diff===0?"#e1f0e8":COL.bg,COL.ink,2.5,6)+TX(120,125,v.a+"·"+v.x+" + "+v.b+" = "+L0,COL.a,15,"middle",700)+'</g><g transform="rotate('+(-tilt)+' 480 80)">'+L(480,80,480,100,COL.ink,2)+R(420,100,120,36,diff===0?"#e1f0e8":COL.bg,COL.ink,2.5,6)+TX(480,125,c,COL.b,18,"middle",700)+'</g></g>';
 return {svg:g,st:[v.a+"x + "+v.b+" = "+c,L0+(diff===0?" = ":diff>0?" > ":" < ")+c,diff===0?"x = "+v.x:U("подбирайте дальше","keep trying")],fb:diff===0?U("Равновесие! x = "+v.x+" — корень.","Balanced! x = "+v.x+" is the root."):U("Левая чаша "+(diff>0?"тяжелее":"легче")+": ответ "+(diff>0?"слишком велик.":"слишком мал."),"The left pan is "+(diff>0?"heavier":"lighter")+": the answer is "+(diff>0?"too big.":"too small."))}''', '0 0 600 230')

m2 = M(('Пошаговое решение', 'Step-by-step solution'),
 [('r', 'a', 'Коэффициент a', 'Coefficient a', 1, 9, 1, 3), ('r', 'x0', 'Корень x', 'Root x', -9, 9, 1, 4), ('r', 'b', 'Число b', 'Number b', -12, 12, 1, 5)],
 [('Уравнение', 'Equation'), ('Переносим b', 'Moving b'), ('Делим на a', 'Dividing by a')],
 'Переносим слагаемое через «=» с противоположным знаком, затем делим на коэффициент.', 'We move a term across “=” with the opposite sign, then divide by the coefficient.', ('Решение по шагам', 'The solution step by step'),
 r'''const c=v.a*v.x0+v.b,ps=n=>n<0?"− "+(-n):"+ "+n;let g="";const st=[v.a+"x "+ps(v.b)+" = "+c,v.a+"x = "+c+" "+(v.b<0?"+ "+(-v.b):"− "+v.b)+" = "+(c-v.b),"x = "+(c-v.b)+" : "+v.a+" = "+v.x0];
 st.forEach((s,i)=>{g+=R(60,15+i*65,480,50,i===2?"#e1f0e8":COL.bg,i===2?COL.c:COL.line,2,6)+TX(300,48+i*65,s,COL.ink,24,"middle",600)+(i<2?TX(300,75+i*65+11,"↓",COL.a,18,"middle",700):"")});
 return {svg:g,st:st,fb:U("Проверка: "+v.a+" · "+v.x0+" "+ps(v.b)+" = "+c+" ✓.","Check: "+v.a+" · "+v.x0+" "+ps(v.b)+" = "+c+" ✓.")}''', '0 0 600 215')

m3 = M(('Текстовая задача', 'A word problem'),
 [('r', 'n', 'Количество билетов x', 'Number of tickets x', 1, 20, 1, 6), ('r', 'p', 'Цена билета', 'Ticket price', 20, 200, 10, 80), ('r', 'f', 'Плата за вход', 'Entrance fee', 0, 300, 10, 100)],
 [('Выражение', 'Expression'), ('Всего заплатили', 'Total paid'), ('Сколько билетов при бюджете 1 000', 'Tickets for a budget of 1,000')],
 'Составляем уравнение: цена · количество + плата = сумма. Меняйте условия и смотрите на зависимость.', 'We build the equation: price · quantity + fee = total. Change the conditions and watch the dependence.', ('Стоимость в зависимости от числа билетов', 'The cost depending on the number of tickets'),
 r'''const G=Gr({x0:0,x1:20,y0:0,y1:4000,L:70,T:10,W:470,H:220});const tot=v.p*v.n+v.f,bud=Math.floor((1000-v.f)/v.p);let g=G.grid(2,1000)+G.fn(t=>v.p*t+v.f,COL.b,3)+G.seg(0,1000,20,1000,COL.a,2)+G.pt(v.n,tot,COL.c,8)+G.txt(v.n+1.5,tot+250,fnum(tot,0),COL.c,14);
 return {svg:g,st:[v.p+"·x + "+v.f,v.p+"·"+v.n+" + "+v.f+" = "+tot,bud>=0?bud:U("не хватает на вход","not enough for the fee")],fb:U("Уравнение "+v.p+"x + "+v.f+" = 1000 даёт x = "+fnum((1000-v.f)/v.p,2)+"; билетов — целое число.","The equation "+v.p+"x + "+v.f+" = 1000 gives x = "+fnum((1000-v.f)/v.p,2)+"; tickets are whole numbers.")}''', '0 0 600 250')

chapter('25', '25-linear-equations.html', 'IV', ('Линейные уравнения', 'Linear equations'),
 ('Как решать уравнения вида ax + b = c, проверять ответ и составлять уравнения по условию задачи.', 'How to solve equations of the form ax + b = c, check the answer and build equations from a problem.'),
 ('Айгуль купила 3 одинаковые тетради и ручку за 20 сомов. Всего она заплатила 110 сомов.\n\nСколько стоит одна тетрадь?', 'Aigul bought 3 identical notebooks and a pen for 20 som. She paid 110 som in total.\n\nHow much does one notebook cost?'),
 ('Разгадка: 30 сомов', 'The answer: 30 som'),
 ('Пусть тетрадь стоит x сомов. Тогда 3x + 20 = 110. Вычтем 20 из обеих частей: 3x = 90. Разделим на 3: x = 30. Проверка: 3 · 30 + 20 = 110. Уравнение — как весы: что делаем с одной чашей, то делаем и с другой.', 'Let a notebook cost x som. Then 3x + 20 = 110. Subtract 20 from both sides: 3x = 90. Divide by 3: x = 30. Check: 3 · 30 + 20 = 110. An equation is like a balance: whatever we do to one pan we do to the other.'),
 [S('bal', 'Уравнение и корень', 'An equation and its root', ('<strong>Уравнение</strong> — равенство с неизвестным. <strong>Корень</strong> — значение неизвестного, при котором равенство верно. Решить уравнение — найти все корни. Самое надёжное — проверить: подставить корень в уравнение.', 'An <strong>equation</strong> is an equality with an unknown. A <strong>root</strong> is the value of the unknown for which the equality holds. To solve an equation is to find all roots. The most reliable thing is to check: substitute the root.'),
    ('ax + b = c', '', 'ax + b = c'), m1),
  S('steps', 'Решение по шагам', 'Solving step by step', ('Правила: любое слагаемое можно перенести через знак «=», изменив его знак; обе части можно умножить или разделить на число, не равное нулю. Так ax + b = c превращается в ax = c − b, а затем x = (c − b)/a.', 'Rules: any term can be moved across “=” with its sign changed; both sides can be multiplied or divided by a nonzero number. So ax + b = c turns into ax = c − b and then x = (c − b)/a.'),
    ('x = (c − b) : a', '', 'x = (c − b) : a'), m2),
  S('word', 'Задачи с уравнением', 'Word problems with an equation', ('План: 1) обозначить неизвестное буквой; 2) выразить через неё другие величины; 3) составить уравнение по условию; 4) решить; 5) проверить и записать ответ в единицах задачи. Следите за смыслом: количество билетов — целое число.', 'The plan: 1) denote the unknown by a letter; 2) express other quantities through it; 3) build an equation from the condition; 4) solve; 5) check and write the answer in the problem’s units. Mind the meaning: the number of tickets is a whole number.'),
    ('цена · количество + плата = сумма', '', 'price · quantity + fee = total'), m3)],
 [TK(('Простое уравнение', 'A simple equation'), ('Решите 5x − 7 = 18.', 'Solve 5x − 7 = 18.'), '5x = 18 + 7', '5x = 25, x = 5. Проверка: 25 − 7 = 18.', 'x = 5.'),
  TK(('Неизвестное с обеих сторон', 'Unknown on both sides'), ('Решите 3x + 4 = x + 10.', 'Solve 3x + 4 = x + 10.'), '3x − x = 10 − 4', '2x = 6, x = 3.', 'x = 3.'),
  TK(('Скобки', 'Brackets'), ('Решите 2(x − 3) = 10.', 'Solve 2(x − 3) = 10.'), '', 'x − 3 = 5, x = 8. Или: 2x − 6 = 10, 2x = 16.', 'x = 8.'),
  TK(('Задача', 'A problem'), ('Отару разделили так: в первой части на 12 овец больше, чем во второй; всего 100 овец. Сколько во второй?', 'A flock was split so that the first part has 12 more sheep than the second; there are 100 in all. How many in the second?'), 'x + (x + 12) = 100', '2x = 88, x = 44.', ('44 овцы.', '44 sheep.')),
  TK(('Нет корней', 'No roots'), ('Решите x + 3 = x + 5.', 'Solve x + 3 = x + 5.'), '', 'Вычтем x: 3 = 5 — неверно. Корней нет.', ('Корней нет.', 'No roots.'))],
 [Q('Корень уравнения x + 7 = 12', 'The root of x + 7 = 12', '5', '19', '−5', ('12 − 7.', '12 − 7.')),
  Q('2x = 14. x =', '2x = 14. x =', '7', '12', '28', ('Делим на 2.', 'Divide by 2.')),
  Q('При переносе слагаемого через «=» знак', 'When a term moves across “=” its sign', ('меняется на противоположный', 'changes to the opposite'), ('сохраняется', 'stays'), ('исчезает', 'disappears'), ('Это правило переноса.', 'This is the transfer rule.')),
  Q('3x − 4 = 11. x =', '3x − 4 = 11. x =', '5', '7/3', '15', ('3x = 15.', '3x = 15.')),
  Q('Как проверить корень?', 'How to check a root?', ('подставить в уравнение', 'substitute into the equation'), ('прибавить 1', 'add 1'), ('умножить на 2', 'multiply by 2'), ('Равенство должно стать верным.', 'The equality must become true.')),
  Q('Сколько корней у x + 1 = x + 2?', 'How many roots has x + 1 = x + 2?', ('ни одного', 'none'), ('один', 'one'), ('бесконечно много', 'infinitely many'), ('1 = 2 неверно.', '1 = 2 is false.')),
  Q('Сколько корней у 2x = 2x?', 'How many roots has 2x = 2x?', ('бесконечно много', 'infinitely many'), ('нуль', 'none'), ('один', 'one'), ('Верно при любом x.', 'True for any x.')),
  Q('Тетрадь стоит x, 2 тетради и ручка (10) — 50. Уравнение', 'A notebook costs x; 2 notebooks and a pen (10) cost 50. The equation', '2x + 10 = 50', 'x + 10 = 50', '2x = 10', ('Две тетради плюс ручка.', 'Two notebooks plus a pen.'))],
 src=[('Wikipedia: Linear equation', 'https://en.wikipedia.org/wiki/Linear_equation'), ('OpenStax: Elementary Algebra 2e', 'https://openstax.org/details/books/elementary-algebra-2e')],
 note=('Цены и сюжеты задач придуманы для атласа.', 'The prices and problem stories are invented for the atlas.'))
