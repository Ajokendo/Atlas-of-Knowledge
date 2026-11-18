# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ЭНЕРГИЯ ПРИБОРА И СЧЁТ', 'AN APPLIANCE’S ENERGY AND THE BILL', 'apSvg', '0 0 600 230',
  select('as', 'Прибор', 'Appliance') + slider('ah', 'Время работы', 'Running time', 0.5, 24, 0.5, 2) + slider('ac', 'Цена 1 кВт·ч (условная)', 'Price of 1 kWh (assumed)', 1, 10, 0.5, 5),
  stats([('aI', 'Ток при 220 В', 'Current at 220 V'), ('aE', 'Энергия', 'Energy'), ('aM', 'Стоимость (усл. ед.)', 'Cost (assumed units)')]),
  'apFb', 'Схема условная: мощности — типичные для бытовых приборов; цена — учебная, в условных единицах (не тариф).',
  'A schematic drawing: the powers are typical for household appliances; the price is illustrative, in assumed units (not a tariff).')
s1 = section('power', 'Работа и мощность тока', 'Work and power of current',
 bd('<p>Электрическое поле совершает работу, перемещая заряд: <em>A = q·U</em>. Так как <em>q = I·t</em>, то работа тока за время <em>t</em>:</p>',
    '<p>The electric field does work in moving a charge: <em>A = q·U</em>. Since <em>q = I·t</em>, the work of the current in time <em>t</em> is:</p>')
 + formula('A = U · I · t,   P = A / t = U · I', 'мощность в ваттах, работа в джоулях; с законом Ома: P = I²R = U²/R', 'power in watts, work in joules; with Ohm’s law: P = I²R = U²/R')
 + bd('<p>Электроэнергию в быту измеряют в <strong>киловатт-часах</strong>: 1 кВт·ч — это работа мощностью 1 кВт за 1 час, то есть 3,6 МДж (глава 10). Счётчик электроэнергии показывает именно киловатт-часы. Мощный прибор, даже включённый ненадолго, потребляет много: чайник на 2 кВт за 15 минут «съедает» 0,5 кВт·ч.</p>',
      '<p>At home electric energy is measured in <strong>kilowatt-hours</strong>: 1 kWh is the work of 1 kW over 1 hour, that is 3.6 MJ (chapter 10). The electricity meter shows exactly kilowatt-hours. A powerful appliance, even switched on briefly, uses a lot: a 2 kW kettle “eats” 0.5 kWh in 15 minutes.</p>'),
 lab1)

lab2 = model(2, 'ТЕПЛО В ПРОВОДНИКЕ', 'HEAT IN A CONDUCTOR', 'jlSvg', '0 0 600 230',
  slider('ji', 'Сила тока', 'Current', 0.5, 20, 0.5, 5) + slider('jr', 'Сопротивление', 'Resistance', 0.1, 50, 0.1, 10) + slider('jt', 'Время', 'Time', 1, 600, 1, 60),
  stats([('jQ', 'Выделится тепла Q = I²Rt', 'Heat released Q = I²Rt'), ('jP', 'Мощность нагрева', 'Heating power'), ('jT', 'Нагрев 1 кг воды на', 'Warming of 1 kg of water by')]),
  'jlFb', 'Схема условная: считаем, что всё тепло идёт в воду (c = 4186 Дж/(кг·К)), потерь нет.', 'A schematic drawing: all the heat is assumed to go into the water (c = 4,186 J/(kg·K)), no losses.')
s2 = section('joule', 'Закон Джоуля — Ленца', 'The Joule–Lenz law',
 bd('<p>Когда ток идёт по проводнику, электроны сталкиваются с частицами вещества, и энергия поля переходит в тепло. Если больше ничего не происходит (нет двигателя, нет химической реакции), вся работа тока превращается в тепло. Из <em>A = U·I·t</em> и закона Ома получаем <strong>закон Джоуля — Ленца</strong>:</p>',
    '<p>When current flows through a conductor the electrons collide with the particles of the substance, and the energy of the field turns into heat. If nothing else is happening (no motor, no chemical reaction) all the work of the current turns into heat. From <em>A = U·I·t</em> and Ohm’s law we get the <strong>Joule–Lenz law</strong>:</p>')
 + formula('Q = I² · R · t', 'тепло растёт с квадратом тока: ток вдвое больше — тепла в 4 раза больше', 'heat grows with the square of the current: twice the current gives 4 times the heat')
 + bd('<p>Так работают чайник, утюг, электроплита и лампа накаливания. А в проводах это тепло вредно: слишком большой ток нагревает провод и может вызвать пожар. Для защиты ставят <strong>плавкие предохранители</strong> и автоматические выключатели: они размыкают цепь, когда ток превышает допустимое значение.</p>',
      '<p>This is how a kettle, an iron, an electric stove and an incandescent lamp work. In wires, however, this heat is harmful: too large a current heats the wire and may cause a fire. To protect against that, <strong>fuses</strong> and circuit breakers are fitted: they open the circuit when the current exceeds a permitted value.</p>'),
 lab2)

lab3 = model(3, 'ПРЕДОХРАНИТЕЛЬ', 'THE FUSE', 'fsSvg', '0 0 600 230',
  select('fr', 'Автомат на', 'Breaker rated') + slider('fl', 'Суммарная мощность включённых приборов', 'Total power of appliances switched on', 0, 6000, 100, 3000),
  stats([('fI', 'Ток в проводке (220 В)', 'Current in the wiring (220 V)'), ('fS', 'Состояние', 'State')]),
  'fsFb', 'Схема условная: автомат на 16 А допускает мощность около 3,5 кВт при напряжении 220 В.', 'A schematic drawing: a 16 A breaker allows about 3.5 kW at 220 V.')
s3 = section('fuse', 'Предохранитель и перегрузка', 'The fuse and overload',
 bd('<p>Ток в общей проводке равен сумме токов включённых приборов: <em>I = P<sub>общ</sub> / U</em>. Если включить слишком много мощных приборов (чайник, утюг, обогреватель) в одну линию, ток превысит допустимый, и автомат отключит цепь. Это не поломка, а защита: без неё провод нагрелся бы по закону Джоуля — Ленца.</p>',
    '<p>The current in shared wiring equals the sum of the currents of the appliances switched on: <em>I = P<sub>total</sub> / U</em>. If too many powerful appliances (a kettle, an iron, a heater) are plugged into one line the current exceeds the permitted value and the breaker cuts the circuit. This is not a fault but protection: without it the wire would heat up according to the Joule–Lenz law.</p>'),
 lab3)

tasks = [
 task(1, 'Лампочка', 'A bulb', 'Лампа мощностью 60 Вт включена в сеть 220 В. Какой ток через неё идёт?', 'A 60 W lamp is plugged into the 220 V mains. What current flows through it?',
  'P = 60 Вт, U = 220 В', 'P = 60 W, U = 220 V', 'I = P / U = 60 / 220 ≈ 0,27 А.', 'I = P / U = 60 / 220 ≈ 0.27 A.',
  'около 0,27 А.', 'about 0.27 A.', True),
 task(2, 'Энергия чайника', 'A kettle’s energy', 'Чайник мощностью 2 кВт работал 15 минут. Сколько энергии он потребил в киловатт-часах и в мегаджоулях?', 'A 2 kW kettle ran for 15 minutes. How much energy did it use in kilowatt-hours and in megajoules?',
  'P = 2 кВт, t = 0,25 ч', 'P = 2 kW, t = 0.25 h', 'A = P·t = 2 · 0,25 = 0,5 кВт·ч.<br>В МДж: 0,5 · 3,6 = 1,8 МДж.', 'A = P·t = 2 · 0.25 = 0.5 kWh.<br>In MJ: 0.5 · 3.6 = 1.8 MJ.',
  '0,5 кВт·ч, то есть 1,8 МДж.', '0.5 kWh, that is 1.8 MJ.'),
 task(3, 'Что показывает счётчик', 'What the meter shows', 'Лампа накаливания 60 Вт и светодиодная лампа 9 Вт дают одинаковый свет. Сколько энергии сэкономит светодиодная за 1000 часов?', 'A 60 W incandescent lamp and a 9 W LED lamp give the same light. How much energy does the LED save in 1,000 hours?',
  'P₁ = 60 Вт, P₂ = 9 Вт, t = 1000 ч', 'P₁ = 60 W, P₂ = 9 W, t = 1,000 h', 'A₁ = 0,06 · 1000 = 60 кВт·ч.<br>A₂ = 0,009 · 1000 = 9 кВт·ч.<br>Разница: 51 кВт·ч.', 'A₁ = 0.06 · 1,000 = 60 kWh.<br>A₂ = 0.009 · 1,000 = 9 kWh.<br>Difference: 51 kWh.',
  '51 кВт·ч, то есть светодиодная лампа расходует в 6,7 раза меньше.', '51 kWh, that is, the LED lamp uses 6.7 times less.'),
 task(4, 'Тепло утюга', 'The iron’s heat', 'Нагревательный элемент сопротивлением 55 Ом пропускает ток 4 А в течение 10 минут. Сколько тепла выделилось?', 'A heating element of 55 Ω carries a current of 4 A for 10 minutes. How much heat is released?',
  'R = 55 Ом, I = 4 А, t = 600 с', 'R = 55 Ω, I = 4 A, t = 600 s', 'Q = I²·R·t = 16 · 55 · 600 = 528 000 Дж.', 'Q = I²·R·t = 16 · 55 · 600 = 528,000 J.',
  '528 кДж. Мощность P = I²R = 880 Вт, как у U·I = 220 · 4.', '528 kJ. The power P = I²R = 880 W, the same as U·I = 220 · 4.'),
 task(5, 'Спираль и шнур', 'The coil and the cord', 'Чайник 2 кВт при 220 В. Сопротивление его спирали R = U²/P. Сопротивление шнура 0,05 Ом. Во сколько раз спираль выделяет больше тепла, чем шнур?', 'A 2 kW kettle at 220 V. The resistance of its coil is R = U²/P. The cord’s resistance is 0.05 Ω. How many times more heat does the coil release than the cord?',
  'P = 2000 Вт, U = 220 В, R<sub>ш</sub> = 0,05 Ом', 'P = 2,000 W, U = 220 V, R<sub>c</sub> = 0.05 Ω', 'R = U² / P = 48 400 / 2000 = 24,2 Ом.<br>Ток один и тот же, поэтому Q ~ R.<br>Отношение: 24,2 / 0,05 = 484.', 'R = U² / P = 48,400 / 2,000 = 24.2 Ω.<br>The current is the same, so Q ~ R.<br>Ratio: 24.2 / 0.05 = 484.',
  'в 484 раза: спираль раскаляется, шнур остаётся почти холодным.', '484 times: the coil glows while the cord stays almost cold.'),
 task(6, 'Хватит ли автомата', 'Is the breaker enough', 'Автомат рассчитан на 16 А. Можно ли включить в одну линию два чайника по 2 кВт? Сеть 220 В.', 'A breaker is rated at 16 A. Can two 2 kW kettles be plugged into one line? Mains 220 V.',
  'P = 4000 Вт, U = 220 В, I<sub>доп</sub> = 16 А', 'P = 4,000 W, U = 220 V, I<sub>max</sub> = 16 A', 'I = P / U = 4000 / 220 ≈ 18,2 А.<br>18,2 А > 16 А.', 'I = P / U = 4,000 / 220 ≈ 18.2 A.<br>18.2 A > 16 A.',
  'Нет: автомат отключит линию. Допустимая мощность 16 · 220 = 3520 Вт.', 'No: the breaker will cut the line. The permitted power is 16 · 220 = 3,520 W.'),
]

quiz = [
 ('По какой формуле находят мощность тока?', [('P = U · I', 'Верно.'), ('P = U / I', 'Это сопротивление.'), ('P = I / U', 'Это не мощность.')],
  'By which formula is the power of current found?', [('P = U · I', 'Correct.'), ('P = U / I', 'That is resistance.'), ('P = I / U', 'That is not power.')], 0),
 ('1 кВт·ч — это…', [('Единица мощности', 'Мощность измеряют в ваттах.'), ('Единица энергии (3,6 МДж)', 'Верно.'), ('Единица напряжения', 'Напряжение — в вольтах.')],
  '1 kWh is…', [('A unit of power', 'Power is measured in watts.'), ('A unit of energy (3.6 MJ)', 'Correct.'), ('A unit of voltage', 'Voltage is in volts.')], 1),
 ('Прибор 500 Вт работает 4 часа. Потребление:', [('2 кВт·ч', 'Верно: 0,5 · 4 = 2.'), ('125 кВт·ч', 'Вы разделили вместо умножения.'), ('0,5 кВт·ч', 'Время не учтено.')],
  'A 500 W appliance runs for 4 hours. The consumption:', [('2 kWh', 'Correct: 0.5 · 4 = 2.'), ('125 kWh', 'You divided instead of multiplying.'), ('0.5 kWh', 'The time is not accounted for.')], 0),
 ('Как изменится тепло в проводнике, если ток увеличить вдвое?', [('Увеличится вдвое', 'Q зависит от квадрата тока.'), ('Увеличится в 4 раза', 'Верно: Q ~ I².'), ('Не изменится', 'Тепло зависит от тока.')],
  'How does heat in a conductor change if the current is doubled?', [('It doubles', 'Q depends on the square of the current.'), ('It grows 4 times', 'Correct: Q ~ I².'), ('It does not change', 'Heat depends on the current.')], 1),
 ('Почему спираль чайника раскаляется, а шнур нет?', [('Через спираль идёт больший ток', 'Ток один и тот же.'), ('У спирали сопротивление намного больше', 'Верно: Q = I²Rt при том же токе.'), ('Шнур толще, поэтому не проводит ток', 'Шнур проводит тот же ток.')],
  'Why does the kettle coil glow while the cord does not?', [('A larger current flows through the coil', 'The current is the same.'), ('The coil has a much greater resistance', 'Correct: Q = I²Rt at the same current.'), ('The cord is thicker so it does not conduct', 'The cord carries the same current.')], 1),
 ('Для чего нужны предохранители?', [('Для увеличения тока', 'Они ограничивают ток.'), ('Чтобы размыкать цепь при опасной перегрузке', 'Верно.'), ('Для понижения напряжения', 'Они не меняют напряжение.')],
  'What are fuses for?', [('To increase the current', 'They limit the current.'), ('To open the circuit at a dangerous overload', 'Correct.'), ('To lower the voltage', 'They do not change the voltage.')], 1),
 ('Автомат на 16 А, сеть 220 В. Какую наибольшую мощность можно включить?', [('Около 3,5 кВт', 'Верно: 16 · 220 = 3520 Вт.'), ('Около 14 Вт', 'Вы поделили 220 на 16.'), ('Около 35 кВт', 'Это в 10 раз больше допустимого.')],
  'A 16 A breaker, 220 V mains. What is the greatest power that can be switched on?', [('About 3.5 kW', 'Correct: 16 · 220 = 3,520 W.'), ('About 14 W', 'You divided 220 by 16.'), ('About 35 kW', 'That is 10 times more than allowed.')], 0),
 ('Для чего для нагревателей используют нихром, а не медь?', [('У него большее удельное сопротивление', 'Верно: больше тепла при том же токе и размерах.'), ('Он лучше проводит ток', 'Медь проводит лучше.'), ('Он тяжелее', 'Дело не в массе.')],
  'Why is nichrome rather than copper used for heaters?', [('It has a greater resistivity', 'Correct: more heat at the same current and size.'), ('It conducts current better', 'Copper conducts better.'), ('It is heavier', 'It is not a matter of mass.')], 0),
]

js = r'''
const T={ru:{
 apLabel:"Прибор: мощность и энергия",jlLabel:"Проводник, ток и выделяющееся тепло",fsLabel:"Автомат и общая мощность приборов",
 apps:["Светодиодная лампа, 9 Вт","Лампа накаливания, 60 Вт","Зарядка телефона, 10 Вт","Телевизор, 100 Вт","Утюг, 1500 Вт","Электрочайник, 2000 Вт"],
 brk:["Автомат на 10 А","Автомат на 16 А","Автомат на 25 А"],
 ok:"в норме",off:"автомат отключил",
 apFb:"Мощные приборы расходуют много энергии, даже если включены ненадолго.",
 jlFb:"Тепло растёт как квадрат тока: удвойте ток — тепла вчетверо.",
 fsFb:["Ток ниже допустимого: цепь работает.","Ток выше допустимого: автомат размыкает цепь."]},
 en:{
 apLabel:"An appliance: power and energy",jlLabel:"A conductor, current and the heat released",fsLabel:"A breaker and the total power of appliances",
 apps:["LED lamp, 9 W","Incandescent lamp, 60 W","Phone charger, 10 W","TV, 100 W","Iron, 1,500 W","Electric kettle, 2,000 W"],
 brk:["10 A breaker","16 A breaker","25 A breaker"],
 ok:"normal",off:"breaker tripped",
 apFb:"Powerful appliances use a lot of energy even if switched on briefly.",
 jlFb:"Heat grows as the square of the current: double the current — four times the heat.",
 fsFb:["The current is below the permitted value: the circuit works.","The current exceeds the permitted value: the breaker opens the circuit."]}};
const PW=[9,60,10,100,1500,2000],AMP=[10,16,25];
function drawAp(){const t=tt(),i=+$("as").value,P=PW[i],h=+$("ah").value,c=+$("ac").value,E=P*h/1000;
 const w=Math.min(500,20+Math.log10(1+P)*130);
 let g='<rect x="60" y="60" width="'+w+'" height="40" fill="#b6533f" stroke="#18181a"/>'+svgText(60,50,P+(lang==="ru"?" Вт":" W"),"#18181a","start",13);
 const w2=Math.min(500,20+Math.log10(1+E*1000)*100);
 g+='<rect x="60" y="140" width="'+w2+'" height="40" fill="#2f6f5d" stroke="#18181a"/>'+svgText(60,130,fmt(E,2)+(lang==="ru"?" кВт·ч":" kWh"),"#18181a","start",13);
 $("apSvg").innerHTML=g;
 $("ahOut").textContent=fmt(h,1)+UN[lang].h;$("acOut").textContent=fmt(c,1);
 $("aI").textContent=fmt(P/220,2)+(lang==="ru"?" А":" A");$("aE").textContent=fmt(E,2)+(lang==="ru"?" кВт·ч":" kWh");$("aM").textContent=fmt(E*c,2);$("apFb").textContent=t.apFb}
["as","ah","ac"].forEach(id=>$(id).addEventListener("input",drawAp));
function drawJl(){const t=tt(),I=+$("ji").value,R=+$("jr").value,s=+$("jt").value,P=I*I*R,Q=P*s,dT=Q/4186;
 const col=Math.min(1,P/3000);
 let g='<rect x="80" y="90" width="440" height="40" rx="20" fill="rgb('+Math.round(150+col*100)+','+Math.round(140-col*90)+','+Math.round(120-col*80)+')" stroke="#18181a" stroke-width="2"/>';
 g+=arrow(30,110,75,110,"#18181a",3)+arrow(525,110,570,110,"#18181a",3)+svgText(300,170,"I = "+fmt(I,1)+" A,  R = "+fmt(R,1)+" Ω","#18181a","middle",13);
 $("jlSvg").innerHTML=g;
 $("jiOut").textContent=fmt(I,1)+" A";$("jrOut").textContent=fmt(R,1)+" Ω";$("jtOut").textContent=s+UN[lang].s;
 $("jQ").textContent=Q>=1e6?fmt(Q/1e6,2)+(lang==="ru"?" МДж":" MJ"):fmt(Q/1000,1)+(lang==="ru"?" кДж":" kJ");$("jP").textContent=P>=1000?fmt(P/1000,2)+(lang==="ru"?" кВт":" kW"):fmt(P,0)+(lang==="ru"?" Вт":" W");$("jT").textContent=fmt(dT,1)+UN[lang].K;$("jlFb").textContent=t.jlFb}
["ji","jr","jt"].forEach(id=>$(id).addEventListener("input",drawJl));
function drawFs(){const t=tt(),i=+$("fr").value,P=+$("fl").value,I=P/220,lim=AMP[i],tr=I>lim;
 const X=v=>60+v/30*480;
 let g='<rect x="60" y="80" width="480" height="30" fill="#e8e4d8" stroke="#18181a"/><rect x="60" y="80" width="'+Math.min(480,X(I)-60)+'" height="30" fill="'+(tr?"#b6533f":"#2f6f5d")+'"/>';
 g+='<line x1="'+X(lim)+'" y1="65" x2="'+X(lim)+'" y2="125" stroke="#18181a" stroke-width="3"/>'+svgText(X(lim),58,lim+" A","#18181a","middle",12);
 for(let k=0;k<=30;k+=5)g+=svgText(X(k),140,k,"#66666b","middle",10);
 g+=svgText(60,190,tr?t.off.toUpperCase():t.ok,tr?"#b6533f":"#2f6f5d","start",20);
 $("fsSvg").innerHTML=g;
 $("flOut").textContent=num(P)+(lang==="ru"?" Вт":" W");
 $("fI").textContent=fmt(I,1)+(lang==="ru"?" А":" A");$("fS").textContent=tr?t.off:t.ok;$("fsFb").textContent=t.fsFb[tr?1:0]}
["fr","fl"].forEach(id=>$(id).addEventListener("input",drawFs));
const LAB={ru:{apSvg:T.ru.apLabel,jlSvg:T.ru.jlLabel,fsSvg:T.ru.fsLabel},en:{apSvg:T.en.apLabel,jlSvg:T.en.jlLabel,fsSvg:T.en.fsLabel}};
function drawAll(){fillSel("as",T[lang].apps,5);fillSel("fr",T[lang].brk,1);drawAp();drawJl();drawFs()}
'''

c = dict(n='18', slug='18-electric-power.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Работа и мощность тока', 'Work and power of current'),
 desc='Глава 18 Атласа физики: работа и мощность тока, киловатт-час, закон Джоуля — Ленца, предохранители.',
 lead=('Спираль чайника раскаляется, а шнур остаётся холодным, хотя ток один. Мощность тока, киловатт-часы, закон Джоуля — Ленца и предохранители.',
       'The kettle’s coil glows while the cord stays cold even though the current is the same. Power of current, kilowatt-hours, the Joule–Lenz law and fuses.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('power', 'Мощность', 'Power'), ('joule', 'Джоуль — Ленц', 'Joule–Lenz'), ('fuse', 'Предохранитель', 'The fuse'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Электрочайник кипятит воду за считанные минуты: его спираль раскалена докрасна. Но шнур, по которому идёт тот же самый ток, едва тёплый — его можно спокойно держать в руке.</p><p>Почему ток нагревает одно и не нагревает другое?</p>',
         '<p>An electric kettle boils water in a few minutes: its coil is red-hot. But the cord carrying the very same current is barely warm — you can hold it in your hand.</p><p>Why does the current heat one thing and not the other?</p>'),
 hint=('Подсказку даст модель «Тепло в проводнике». Разгадка — в конце главы.', 'The “Heat in a conductor” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему греется спираль, а не шнур', 'The answer: why the coil heats and the cord does not'),
 answer=('<p>Тепло, которое выделяется в проводнике, равно <em>Q = I²·R·t</em>. Ток у спирали и шнура одинаковый, значит, всё решает сопротивление. У спирали из нихрома оно около 24 Ом, у медного шнура — сотые доли ома. Поэтому в спирали тепла выделяется примерно в 500 раз больше (задача 5): она раскаляется, а шнур почти не нагревается.</p><p>Если же включить слишком мощные приборы в один тонкий шнур или удлинитель, ток вырастет, а тепло — как квадрат тока, и провод может перегреться. Для этого и нужны автоматы и предохранители.</p>',
         '<p>The heat released in a conductor is <em>Q = I²·R·t</em>. The current through the coil and the cord is the same, so the resistance decides. The nichrome coil has about 24 Ω, the copper cord only hundredths of an ohm. So about 500 times more heat is released in the coil (problem 5): it glows while the cord hardly warms.</p><p>If too powerful appliances are plugged into one thin cord or extension lead, the current rises, and the heat as the square of it, and the wire may overheat. That is what breakers and fuses are for.</p>'),
 sources=[
  ('Работа и мощность тока, закон Джоуля — Ленца —', 'Work and power of current, the Joule–Lenz law —', LINK('https://openstax.org/books/university-physics-volume-2/pages/9-4-electrical-energy-and-power', 'OpenStax University Physics, Vol. 2: Electrical energy and power')),
  ('1 кВт·ч = 3,6 МДж —', '1 kWh = 3.6 MJ —', LINK('https://w.astro.berkeley.edu/~wright/fuel_energy.html', 'Berkeley: Useful conversion factors')),
  ('Напряжение сети 220 В —', 'Mains voltage 220 V —', LINK('https://www.cia.gov/the-world-factbook/countries/kyrgyzstan/travel-facts', 'CIA World Factbook: Kyrgyzstan travel facts'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Мощности приборов — типичные, цена киловатт-часа в модели — условная, а не тариф.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The appliance powers are typical; the price of a kilowatt-hour in the model is assumed, not a tariff.'),
 prev=('17-ohms-law.html', 'Глава 17 · Закон Ома', 'Chapter 17 · Ohm’s law'),
 next=('19-conduction-in-media.html', 'Глава 19 · Ток в жидкостях и газах', 'Chapter 19 · Current in liquids and gases'),
 js=js)
build(c)
