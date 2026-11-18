# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Отношение и деление в данном отношении', 'A ratio and dividing in a given ratio'),
 [('r', 'T', 'Всего', 'Total', 10, 200, 1, 60), ('r', 'a', 'Часть первого', 'Share of the first', 1, 9, 1, 2), ('r', 'b', 'Часть второго', 'Share of the second', 1, 9, 1, 3)],
 [('Отношение', 'Ratio'), ('Одна часть', 'One share'), ('Первому и второму', 'First and second')],
 'Делим целое на a + b равных частей и раздаём a частей первому, b — второму.', 'We split the whole into a + b equal shares and give a shares to the first, b to the second.', ('Целое, разделённое на части', 'A whole split into shares'),
 r'''const n=v.a+v.b,one=v.T/n;let g="";const w=540/n;
 for(let i=0;i<n;i++)g+=R(30+i*w,60,w-2,60,i<v.a?COL.a:COL.b,COL.bg,1,3);
 g+=TX(30+v.a*w/2,150,fnum(one*v.a,2),COL.a,18,"middle",700)+TX(30+(v.a+v.b/2)*w,150,fnum(one*v.b,2),COL.b,18,"middle",700)+TX(300,200,U("Всего "+v.T,"Total "+v.T),COL.mut,15);
 return {svg:g,st:[v.a+" : "+v.b,v.T+" : "+n+" = "+fnum(one,3),fnum(one*v.a,2)+" и "+fnum(one*v.b,2)],fb:U("Всего частей "+n+"; одна часть "+fnum(one,3)+".","Shares in total: "+n+"; one share is "+fnum(one,3)+".")}''')

m2 = M(('Масштаб карты', 'Map scale'),
 [('r', 'cm', 'Расстояние на карте, см', 'Distance on the map, cm', 1, 30, 0.5, 6), ('s', 'sc', 'Масштаб', 'Scale', ['1 : 100 000', '1 : 500 000', '1 : 1 000 000'], ['1 : 100,000', '1 : 500,000', '1 : 1,000,000'], 1)],
 [('Расстояние на местности', 'Real distance'), ('1 см на карте — это', '1 cm on the map is'), ('В метрах', 'In metres')],
 'Масштаб 1 : 500 000 означает, что 1 см на карте — 500 000 см на местности, то есть 5 км.', 'A scale of 1 : 500,000 means 1 cm on the map is 500,000 cm in reality, that is 5 km.', ('Отрезок на карте и на местности', 'A segment on the map and in reality'),
 r'''const k=[100000,500000,1000000][v.sc],km=v.cm*k/100000;let g=R(40,50,v.cm*17,18,COL.a,COL.ink,1.5,2)+TX(40,40,U("на карте "+v.cm+" см","on the map "+v.cm+" cm"),COL.a,14,"start",600)+R(40,140,Math.min(520,km*4),18,COL.b,COL.ink,1.5,2)+TX(40,130,U("на местности "+fnum(km,2)+" км","in reality "+fnum(km,2)+" km"),COL.b,14,"start",600);
 g+=TX(300,215,U("1 см = "+fnum(k/100000,2)+" км","1 cm = "+fnum(k/100000,2)+" km"),COL.mut,15,"middle");
 return {svg:g,st:[fnum(km,2)+" км",fnum(k/100000,2)+" км","" + Math.round(km*1000)],fb:U(v.cm+" см · "+k.toLocaleString("ru")+" = "+Math.round(v.cm*k)+" см = "+fnum(km,2)+" км.",v.cm+" cm · "+k.toLocaleString("en")+" = "+Math.round(v.cm*k)+" cm = "+fnum(km,2)+" km.")}''')

m3 = M(('Прямая и обратная пропорциональность', 'Direct and inverse proportion'),
 [('s', 'kind', 'Вид', 'Kind', ['прямая (цена и количество)', 'обратная (рабочие и время)'], ['direct (price and quantity)', 'inverse (workers and time)'], 0), ('r', 'x', 'Количество x', 'Quantity x', 1, 12, 1, 4)],
 [('Значение y', 'Value y'), ('Что постоянно', 'What stays constant'), ('Как меняется y при удвоении x', 'How y changes when x doubles')],
 'Прямая: во сколько раз больше x, во столько же больше y (y = k·x). Обратная: во сколько раз больше x, во столько раз меньше y (x·y = k).', 'Direct: as x grows, y grows by the same factor (y = k·x). Inverse: as x grows, y shrinks by that factor (x·y = k).', ('График зависимости', 'The graph of the relation'),
 r'''const dir=v.kind===0,K=dir?30:24,y=dir?K*v.x:K/v.x,YM=dir?360:48,X=t=>50+t/12*510,Y=t=>200-Math.min(t,YM)/YM*180;let g=axes(12,YM,12,4,50,560,200,20,0,0);
 let p=[];for(let i=1;i<=48;i++){const xx=i/4;if(!dir&&xx<0.5)continue;p.push([X(xx),Y(dir?K*xx:K/xx)])}
 g+=pline(p,COL.b,3)+C(X(v.x),Y(y),8,COL.a)+TX(X(v.x)+12,Y(y)-10,fnum(y,2),COL.a,14,"start",600);
 return {svg:g,st:[fnum(y,2),dir?U("отношение y/x = "+K,"ratio y/x = "+K):U("произведение x·y = "+K,"product x·y = "+K),dir?U("тоже в 2 раза больше","also doubles"):U("в 2 раза меньше","halves")],fb:dir?U("Цена: 1 кг = "+K+" сомов, "+v.x+" кг = "+y+" сомов.","Price: 1 kg = "+K+" som, "+v.x+" kg = "+y+" som."):U("Работа 24 «человеко-часа»: "+v.x+" чел. делают её за "+fnum(y,2)+" ч.","The job is 24 person-hours: "+v.x+" people do it in "+fnum(y,2)+" h.")}''')

chapter('19', '19-ratios-proportions.html', 'III', ('Отношения и пропорции', 'Ratios and proportions'),
 ('Как сравнивать величины делением, делить поровну «в пропорции», читать масштаб и отличать прямую зависимость от обратной.', 'How to compare quantities by division, split in a proportion, read a scale and tell direct from inverse dependence.'),
 ('Двое пастухов пасли общую отару из 60 овец. Один выделил на выпас 2 дня, другой 3 дня.\n\nКак по справедливости разделить 60 000 сомов, вырученных от продажи шерсти?', 'Two shepherds grazed a common flock of 60 sheep. One worked 2 days, the other 3 days.\n\nHow should 60,000 som from the wool sale be split fairly?'),
 ('Разгадка: 24 000 и 36 000 сомов', 'The answer: 24,000 and 36,000 som'),
 ('Делим в отношении 2 : 3. Всего 2 + 3 = 5 частей. Одна часть: 60 000 : 5 = 12 000 сомов. Первому — 2 · 12 000 = 24 000, второму — 3 · 12 000 = 36 000. Проверка: 24 000 + 36 000 = 60 000.', 'We split in the ratio 2 : 3. Altogether 2 + 3 = 5 shares. One share: 60,000 : 5 = 12,000 som. The first gets 2 · 12,000 = 24,000, the second 3 · 12,000 = 36,000. Check: 24,000 + 36,000 = 60,000.'),
 [S('ratio', 'Отношение', 'A ratio', ('<strong>Отношение</strong> двух чисел — это их частное: a : b = a/b. Оно показывает, во сколько раз a больше b (или какую часть a составляет от b). Чтобы разделить число в отношении a : b, находят сумму частей a + b, затем одну часть T/(a + b) и умножают на a и на b.', 'A <strong>ratio</strong> of two numbers is their quotient: a : b = a/b. It shows how many times a is greater than b (or what part a is of b). To split a number in the ratio a : b we find the total of shares a + b, then one share T/(a + b), and multiply it by a and by b.'),
    ('одна часть = T : (a + b)', '', 'one share = T : (a + b)'), m1),
  S('scale', 'Масштаб', 'Scale', ('<strong>Масштаб</strong> — это отношение длины на карте к длине на местности. Масштаб 1 : 500 000 значит, что 1 см на карте соответствует 500 000 см = 5 км. Чем больше второе число, тем мельче карта и тем больше территории на ней помещается.', 'The <strong>scale</strong> is the ratio of a length on the map to the length in reality. A scale of 1 : 500,000 means 1 cm on the map corresponds to 500,000 cm = 5 km. The larger the second number, the smaller the map and the more territory fits on it.'),
    ('1 : 500 000', '1 см = 5 км', '1 cm = 5 km'), m2),
  S('prop', 'Прямая и обратная пропорциональность', 'Direct and inverse proportion', ('Если величины связаны <strong>прямой</strong> пропорциональностью, их отношение постоянно: цена и количество товара. Если <strong>обратной</strong> — постоянно их произведение: чем больше рабочих, тем меньше времени на ту же работу. Равенство двух отношений называется <strong>пропорцией</strong>: a/b = c/d, откуда ad = bc.', 'If quantities are <strong>directly</strong> proportional, their ratio is constant: the price and the quantity of goods. If <strong>inversely</strong>, their product is constant: the more workers, the less time for the same job. An equality of two ratios is called a <strong>proportion</strong>: a/b = c/d, hence ad = bc.'),
    ('y = k·x  и  x·y = k', 'прямая и обратная', 'direct and inverse'), m3)],
 [TK(('Деление в отношении', 'Splitting in a ratio'), ('Раздел 90 сомов в отношении 4 : 5.', 'Split 90 som in the ratio 4 : 5.'), '4 + 5 = 9', 'Одна часть 90 : 9 = 10. Доли: 40 и 50.', ('40 и 50 сомов.', '40 and 50 som.')),
  TK(('Масштаб', 'Scale'), ('На карте 1 : 200 000 расстояние 7 см. Сколько километров?', 'On a 1 : 200,000 map the distance is 7 cm. How many kilometres?'), '1 см = 2 км', '7 · 2 = 14 км.', ('14 км.', '14 km.')),
  TK(('Пропорция', 'Proportion'), ('3 кг сыра стоят 1 200 сомов. Сколько стоят 5 кг?', '3 kg of cheese cost 1,200 som. How much do 5 kg cost?'), '1 кг = 400', '400 · 5 = 2000.', ('2 000 сомов.', '2,000 som.')),
  TK(('Обратная зависимость', 'Inverse dependence'), ('4 рабочих копают траншею за 6 дней. За сколько дней её выкопают 8 рабочих?', '4 workers dig a trench in 6 days. In how many days will 8 workers dig it?'), '4 · 6 = 24', '24 : 8 = 3.', ('За 3 дня.', 'In 3 days.')),
  TK(('Решить пропорцию', 'Solve a proportion'), ('Найдите x: 3/5 = x/20.', 'Find x: 3/5 = x/20.'), '3 · 20 = 5 · x', 'x = 60 : 5 = 12.', '12.')],
 [Q('Отношение 6 : 3 равно', 'The ratio 6 : 3 equals', '2', '3', '1/2', ('6 : 3 = 2.', '6 : 3 = 2.')),
  Q('60 разделили в отношении 1 : 2. Большая часть', '60 is split in the ratio 1 : 2. The bigger share is', '40', '30', '20', ('Часть 20, а большая — две части.', 'One share is 20; the bigger is two shares.')),
  Q('Масштаб 1 : 100 000. 3 см на карте — это', 'Scale 1 : 100,000. 3 cm on the map is', ('3 км', '3 km'), ('30 км', '30 km'), ('300 м', '300 m'), ('3 · 100 000 см = 3 км.', '3 · 100,000 cm = 3 km.')),
  Q('Какая зависимость обратная?', 'Which dependence is inverse?', ('скорость и время на тот же путь', 'speed and time for the same distance'), ('цена и количество', 'price and quantity'), ('сторона и периметр квадрата', 'side and perimeter of a square'), ('Больше скорость — меньше время.', 'Higher speed — less time.')),
  Q('2/3 = x/12. x =', '2/3 = x/12. x =', '8', '6', '18', ('2 · 12 : 3 = 8.', '2 · 12 : 3 = 8.')),
  Q('Если масштаб крупнее, то', 'A larger scale means', ('видно больше деталей', 'more detail is visible'), ('охвачена большая территория', 'a larger territory is covered'), ('карта точнее всегда', 'the map is always more accurate'), ('Крупный масштаб — меньше территория, больше подробностей.', 'Large scale — smaller area, more detail.')),
  Q('Для 5 литров нужно 3 кг. Для 10 литров нужно', 'For 5 litres you need 3 kg. For 10 litres you need', ('6 кг', '6 kg'), ('4 кг', '4 kg'), ('1,5 кг', '1.5 kg'), ('Прямая зависимость: ×2.', 'Direct dependence: ×2.')),
  Q('Что называют пропорцией?', 'What is called a proportion?', ('равенство двух отношений', 'an equality of two ratios'), ('сумму двух чисел', 'a sum of two numbers'), ('разность частей', 'a difference of shares'), ('a/b = c/d.', 'a/b = c/d.'))],
 src=[('Wikipedia: Ratio', 'https://en.wikipedia.org/wiki/Ratio'), ('Wikipedia: Proportionality (mathematics)', 'https://en.wikipedia.org/wiki/Proportionality_(mathematics)')],
 note=('Сюжет про пастухов и суммы придуманы для атласа.', 'The shepherd story and sums are invented for the atlas.'))
