# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Среднее арифметическое', 'The arithmetic mean'),
 [('r', 'a', 'Первое', 'First', 0, 20, 1, 4), ('r', 'b', 'Второе', 'Second', 0, 20, 1, 9), ('r', 'c', 'Третье', 'Third', 0, 20, 1, 5), ('r', 'd', 'Четвёртое', 'Fourth', 0, 20, 1, 10)],
 [('Сумма', 'Sum'), ('Среднее', 'Mean'), ('Самое далёкое от среднего', 'Furthest from the mean')],
 'Среднее — это то, что получил бы каждый, если бы всё выровняли поровну.', 'The mean is what each would get if everything were levelled out equally.', ('Столбцы и линия среднего', 'Bars and the line of the mean'),
 r'''const a=[v.a,v.b,v.c,v.d],s=a.reduce((x,y)=>x+y,0),m=s/4,mx=Math.max(20,...a);let g=axes(4,mx,4,4,50,560,200,20,0,0);
 a.forEach((x,i)=>{g+=R(80+i*120,200-x/mx*180,70,x/mx*180,[COL.a,COL.b,COL.c,COL.a][i],COL.ink,1.5,2)});
 g+=L(50,200-m/mx*180,560,200-m/mx*180,COL.ink,2.5)+TX(565,200-m/mx*180+5,fnum(m,2),COL.ink,14,"start",700);
 let far=0;a.forEach((x,i)=>{if(Math.abs(x-m)>Math.abs(a[far]-m))far=i});
 return {svg:g,st:[a.join(" + ")+" = "+s,s+" : 4 = "+fnum(m,2),(far+1)+" ("+a[far]+")"],fb:U("Среднее "+fnum(m,2)+": нужно сложить все числа и разделить на их количество.","The mean is "+fnum(m,2)+": add all numbers and divide by how many there are.")}''')

m2 = M(('Встречное движение', 'Motion towards each other'),
 [('r', 'D', 'Расстояние, км', 'Distance, km', 40, 400, 10, 240), ('r', 'v1', 'Скорость первого, км/ч', 'Speed of the first, km/h', 10, 100, 5, 60), ('r', 'v2', 'Скорость второго, км/ч', 'Speed of the second, km/h', 10, 100, 5, 40)],
 [('Скорость сближения', 'Closing speed'), ('Время до встречи', 'Time until meeting'), ('Место встречи от первого', 'Meeting point from the first')],
 'При движении навстречу расстояние сокращается со скоростью v₁ + v₂. Время встречи — расстояние, делённое на эту сумму.', 'Moving towards each other, the distance shrinks at speed v₁ + v₂. The meeting time is the distance divided by this sum.', ('Движение двух путников навстречу', 'Two travellers moving towards each other'),
 r'''const sp=v.v1+v.v2,t=v.D/sp,x=v.v1*t;let g=L(40,120,560,120,COL.ink,3)+TX(40,150,"A",COL.ink,16,"middle",700)+TX(560,150,"B",COL.ink,16,"middle",700);
 const X=k=>40+k/v.D*520;g+=C(X(x),120,10,COL.c)+TX(X(x),95,U("встреча","meeting"),COL.c,13,"middle",600)+R(X(0)-6,108,12,12,COL.a,COL.ink,1,6)+R(X(v.D)-6,108,12,12,COL.b,COL.ink,1,6)+L(X(0),180,X(x),180,COL.a,4)+L(X(x),180,X(v.D),180,COL.b,4)+TX((X(0)+X(x))/2,200,fnum(x,1)+" км",COL.a,14,"middle",600)+TX((X(x)+X(v.D))/2,200,fnum(v.D-x,1)+" км",COL.b,14,"middle",600);
 return {svg:g,st:[sp+" км/ч",fnum(t,2)+" ч"+(t<1?" ("+Math.round(t*60)+" мин)":""),fnum(x,1)+" км"],fb:U(v.D+" : ("+v.v1+" + "+v.v2+") = "+fnum(t,2)+" ч.",v.D+" : ("+v.v1+" + "+v.v2+") = "+fnum(t,2)+" h.")}''')

m3 = M(('Совместная работа', 'Working together'),
 [('r', 'x', 'Первый делает всё за, часов', 'The first does it all in, hours', 2, 20, 1, 6), ('r', 'y', 'Второй делает всё за, часов', 'The second does it all in, hours', 2, 20, 1, 12)],
 [('Доля работы в час: первый', 'Share per hour: first'), ('Доля работы в час: второй', 'Share per hour: second'), ('Вместе за', 'Together in')],
 'Принимаем всю работу за 1. Первый делает 1/x в час, второй — 1/y. Вместе за час — 1/x + 1/y.', 'We take the whole job as 1. The first does 1/x per hour, the second 1/y. Together per hour — 1/x + 1/y.', ('Накопление работы со временем', 'The job accumulating over time'),
 r'''const r1=1/v.x,r2=1/v.y,T=1/(r1+r2),TM=Math.max(v.x,v.y);let g=axes(TM,1,5,4,50,560,200,20,0,1);const X=t=>50+t/TM*510,Y=w=>200-Math.min(w,1)*180;
 g+=pline([[X(0),Y(0)],[X(Math.min(TM,v.x)),Y(Math.min(TM,v.x)*r1)]],COL.a,3)+pline([[X(0),Y(0)],[X(Math.min(TM,v.y)),Y(Math.min(TM,v.y)*r2)]],COL.b,3)+pline([[X(0),Y(0)],[X(T),Y(1)]],COL.c,4)+C(X(T),Y(1),7,COL.c)+TX(X(T)+10,Y(1)+16,fnum(T,2)+" ч",COL.c,14,"start",700);
 return {svg:g,st:["1/"+v.x,"1/"+v.y,fnum(T,2)+" ч"],fb:U("Вместе: 1 : (1/"+v.x+" + 1/"+v.y+") = "+fnum(T,2)+" ч — быстрее любого из двоих.","Together: 1 : (1/"+v.x+" + 1/"+v.y+") = "+fnum(T,2)+" h — faster than either alone.")}''')

chapter('21', '21-mean-motion-work.html', 'III', ('Среднее, движение, работа', 'The mean, motion, work'),
 ('Три типичные школьные задачи: на среднее значение, на встречное движение и на совместную работу.', 'Three typical school problems: on the mean, on motion towards each other and on working together.'),
 ('Два села стоят на одной дороге в 240 км друг от друга. Утром из них одновременно навстречу друг другу выехали два всадника: один со скоростью 60 км/ч, другой 40 км/ч — условно, ради счёта.\n\nЧерез сколько часов они встретятся?', 'Two villages stand on one road 240 km apart. In the morning two riders set out towards each other at the same moment: one at 60 km/h, the other at 40 km/h — a made-up speed for the sum.\n\nHow many hours until they meet?'),
 ('Разгадка: через 2,4 часа', 'The answer: in 2.4 hours'),
 ('Каждый час расстояние между всадниками сокращается на 60 + 40 = 100 км. Значит, 240 км «закончатся» за 240 : 100 = 2,4 часа, то есть через 2 часа 24 минуты. К этому моменту первый проедет 60 · 2,4 = 144 км, второй 40 · 2,4 = 96 км, вместе 240.', 'Every hour the distance between the riders shrinks by 60 + 40 = 100 km. So 240 km will “run out” in 240 : 100 = 2.4 hours, that is in 2 hours 24 minutes. By then the first rides 60 · 2.4 = 144 km, the second 40 · 2.4 = 96 km, 240 together.'),
 [S('mean', 'Среднее арифметическое', 'The arithmetic mean', ('<strong>Среднее арифметическое</strong> нескольких чисел — их сумма, делённая на их количество: (4 + 9 + 5 + 10) : 4 = 7. Это значение, которое получил бы каждый, если бы всё выровняли поровну. Среднее лежит между наименьшим и наибольшим числом, но одно очень большое число может сильно сдвинуть его.', 'The <strong>arithmetic mean</strong> of several numbers is their sum divided by how many there are: (4 + 9 + 5 + 10) : 4 = 7. It is the value each would get if everything were levelled out equally. The mean lies between the smallest and the greatest number, but one very large number can pull it strongly.'),
    ('среднее = сумма : количество', '', 'mean = sum : count'), m1),
  S('motion', 'Задачи на движение', 'Motion problems', ('Основная связь: <strong>путь = скорость · время</strong>. При движении навстречу скорости складываются (скорость сближения v₁ + v₂), при движении вдогонку вычитаются (v₁ − v₂). Время встречи — расстояние, делённое на скорость сближения.', 'The main relation: <strong>distance = speed · time</strong>. When moving towards each other the speeds add (closing speed v₁ + v₂); when chasing they subtract (v₁ − v₂). The meeting time is the distance divided by the closing speed.'),
    ('s = v · t', 't = s : (v₁ + v₂)', 't = s : (v₁ + v₂)'), m2),
  S('work', 'Задачи на работу', 'Work problems', ('Всю работу принимают за 1. Если мастер делает её за x часов, его производительность — 1/x работы в час. При совместной работе производительности складываются: 1/x + 1/y. Время вместе: 1 : (1/x + 1/y) = xy/(x + y).', 'The whole job is taken as 1. If a craftsman does it in x hours, his rate is 1/x of the job per hour. When working together the rates add: 1/x + 1/y. The time together: 1 : (1/x + 1/y) = xy/(x + y).'),
    ('T = xy/(x + y)', '', 'T = xy/(x + y)'), m3)],
 [TK(('Среднее', 'The mean'), ('Найдите среднее чисел 12, 15, 9, 20.', 'Find the mean of 12, 15, 9, 20.'), '12 + 15 + 9 + 20', 'Сумма 56, делим на 4: 14.', '14.'),
  TK(('Средний балл', 'Average mark'), ('Оценки: 5, 4, 5, 3, 5. Какой средний балл?', 'Marks: 5, 4, 5, 3, 5. What is the average mark?'), '5 + 4 + 5 + 3 + 5', '22 : 5 = 4,4.', '4,4.'),
  TK(('Навстречу', 'Towards each other'), ('Расстояние 180 км, скорости 50 и 40 км/ч. Через сколько часов встреча?', 'The distance is 180 km, speeds 50 and 40 km/h. When do they meet?'), '50 + 40 = 90', '180 : 90 = 2.', ('Через 2 часа.', 'In 2 hours.')),
  TK(('Вдогонку', 'Chasing'), ('Пешеход идёт 5 км/ч, велосипедист за ним 15 км/ч, между ними 20 км. Через сколько часов догонит?', 'A pedestrian walks at 5 km/h, a cyclist follows at 15 km/h, 20 km apart. When does the cyclist catch up?'), '15 − 5 = 10', '20 : 10 = 2.', ('Через 2 часа.', 'In 2 hours.')),
  TK(('Совместная работа', 'Working together'), ('Один мастер красит забор за 6 ч, другой за 3 ч. За сколько часов вдвоём?', 'One craftsman paints a fence in 6 h, another in 3 h. How long together?'), '1/6 + 1/3 = 1/2', '1 : 1/2 = 2.', ('За 2 часа.', 'In 2 hours.'))],
 [Q('Среднее арифметическое чисел 2 и 8', 'The arithmetic mean of 2 and 8', '5', '10', '6', ('(2 + 8) : 2.', '(2 + 8) : 2.')),
  Q('Среднее лежит', 'The mean lies', ('между наименьшим и наибольшим', 'between the smallest and the greatest'), ('всегда посередине списка', 'always in the middle of the list'), ('всегда равно одному из чисел', 'always equals one of the numbers'), ('Это выровненное значение.', 'It is a levelled value.')),
  Q('Путь равен', 'Distance equals', ('скорость · время', 'speed · time'), ('скорость : время', 'speed : time'), ('время : скорость', 'time : speed'), ('s = v · t.', 's = v · t.')),
  Q('Навстречу: скорости 30 и 20, расстояние 100. Время', 'Towards: speeds 30 and 20, distance 100. Time', '2', '5', '10', ('100 : 50.', '100 : 50.')),
  Q('Один делает работу за 4 ч. Какая доля за час?', 'One does a job in 4 h. What share per hour?', '1/4', '4', '1/2', ('1 : 4.', '1 : 4.')),
  Q('Вдвоём работа делается', 'Working together the job is done', ('быстрее, чем каждым в одиночку', 'faster than by either alone'), ('так же', 'just as fast'), ('медленнее', 'slower'), ('Производительности складываются.', 'The rates add.')),
  Q('Вдогонку скорости', 'When chasing, speeds', ('вычитаются', 'subtract'), ('складываются', 'add'), ('умножаются', 'multiply'), ('Скорость сближения v₁ − v₂.', 'Closing speed v₁ − v₂.')),
  Q('Средний балл 3, 4, 5 равен', 'The mean mark of 3, 4, 5 is', '4', '5', '3', ('12 : 3.', '12 : 3.'))],
 src=[('Wikipedia: Arithmetic mean', 'https://en.wikipedia.org/wiki/Arithmetic_mean'), ('Wikipedia: Speed', 'https://en.wikipedia.org/wiki/Speed')],
 note=('Сюжеты и числа придуманы для атласа.', 'The stories and numbers are invented for the atlas.'))
