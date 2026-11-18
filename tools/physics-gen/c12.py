# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ПЕРВЫЙ ЗАКОН: ТЕПЛО, РАБОТА, ЭНЕРГИЯ', 'FIRST LAW: HEAT, WORK, ENERGY', 'flSvg', '0 0 600 250',
  slider('fQ', 'Газу передано тепло Q', 'Heat Q given to the gas', 0, 1000, 10, 600) + slider('fA', 'Газ совершил работу A', 'Work A done by the gas', 0, 1000, 10, 250),
  stats([('fU', 'Изменение внутренней энергии ΔU', 'Change of internal energy ΔU'), ('fS', 'Что с газом', 'What the gas does')]),
  'flFb', 'Схема условная: энергия в джоулях; ΔU = Q − A.', 'A schematic drawing: energy in joules; ΔU = Q − A.')
s1 = section('law', 'Первый закон термодинамики', 'The first law of thermodynamics',
 bd('<p>Тепло можно превратить в работу, например, когда горячий газ толкает поршень. Закон сохранения энергии для таких процессов называется <strong>первым законом термодинамики</strong>: полученное газом тепло идёт на увеличение его внутренней энергии и на работу, которую газ совершает над окружающими телами.</p>',
    '<p>Heat can be turned into work, for example when hot gas pushes a piston. The law of conservation of energy for such processes is called the <strong>first law of thermodynamics</strong>: the heat received by a gas goes to increase its internal energy and to the work the gas does on its surroundings.</p>')
 + formula('Q = ΔU + A', 'ΔU = Q − A; если A > Q, газ охлаждается, отдавая внутреннюю энергию', 'ΔU = Q − A; if A > Q the gas cools, giving up internal energy')
 + bd('<p>Закон не запрещает ничего «за бесплатно», но и не позволяет получить работу из ничего: вечный двигатель первого рода, который работает без источника энергии, невозможен.</p>',
      '<p>The law gives nothing “for free”: work cannot be obtained from nothing — a perpetual motion machine of the first kind, running without any energy source, is impossible.</p>'),
 lab1)

lab2 = model(2, 'ТЕПЛОВОЙ ДВИГАТЕЛЬ', 'A HEAT ENGINE', 'enSvg', '0 0 600 270',
  slider('eQ1', 'Тепло от нагревателя Q₁', 'Heat from the heater Q₁', 100, 1000, 10, 1000) + slider('eE', 'КПД двигателя', 'Engine efficiency', 5, 60, 1, 30),
  stats([('eA', 'Полезная работа A', 'Useful work A'), ('eQ2', 'Отдано холодильнику Q₂', 'Rejected to the cooler Q₂'), ('eK', 'КПД', 'Efficiency')]),
  'enFb', 'Схема условная: показано, куда уходит энергия топлива. Значения КПД — типичные; реальные зависят от двигателя.',
  'A schematic drawing: it shows where the fuel’s energy goes. The efficiency values are typical; real ones depend on the engine.')
s2 = section('engine', 'Тепловой двигатель и КПД', 'The heat engine and efficiency',
 bd('<p><strong>Тепловой двигатель</strong> превращает часть тепла от нагревателя в работу, а остальное отдаёт холодильнику (обычно окружающему воздуху). Так работают двигатели автомобилей, паровые турбины электростанций, реактивные двигатели. <strong>КПД</strong> показывает, какая доля полученного тепла стала полезной работой:</p>',
    '<p>A <strong>heat engine</strong> turns part of the heat from a heater into work and gives the rest to a cooler (usually the surrounding air). Car engines, steam turbines of power stations and jet engines work like this. The <strong>efficiency</strong> shows what share of the received heat became useful work:</p>')
 + formula('η = A / Q₁ = (Q₁ − Q₂) / Q₁', 'КПД всегда меньше 1 (меньше 100 %): часть тепла обязательно уходит холодильнику', 'The efficiency is always below 1 (below 100 %): some heat must always go to the cooler')
 + bd('<p>Типичный бензиновый двигатель автомобиля превращает в работу около 25–30 % энергии топлива, дизельный — около 35–40 %. Остальное уходит в выхлопные газы и систему охлаждения. Поэтому машина нагревается и нужен радиатор.</p>',
      '<p>A typical petrol car engine turns about 25–30 % of the fuel energy into work, a diesel about 35–40 %. The rest goes into the exhaust and the cooling system. That is why the engine heats up and a radiator is needed.</p>'),
 lab2)

lab3 = model(3, 'ПРЕДЕЛ КАРНО', 'THE CARNOT LIMIT', 'caSvg', '0 0 600 250',
  slider('cH', 'Температура нагревателя', 'Heater temperature', 400, 1500, 10, 800) + slider('cC', 'Температура холодильника', 'Cooler temperature', 250, 500, 5, 300),
  stats([('cE', 'Наибольший возможный КПД', 'Greatest possible efficiency'), ('cD', 'Минимум тепла холодильнику', 'Least heat to the cooler (per 100 J)')]),
  'caFb', 'Температуры — абсолютные, в кельвинах. Предел КПД = 1 − T₂/T₁.', 'The temperatures are absolute, in kelvins. The efficiency limit is 1 − T₂/T₁.')
s3 = section('carnot', 'Предел КПД: цикл Карно', 'The efficiency limit: the Carnot cycle',
 bd('<p>Можно ли сделать КПД равным 100 %? Второй закон термодинамики говорит: нельзя. Тепло само не переходит от холодного тела к горячему, и двигатель не может превратить в работу всё полученное тепло. Французский инженер Сади Карно показал, что наибольший КПД зависит только от температур нагревателя <em>T₁</em> и холодильника <em>T₂</em> (в кельвинах):</p>',
    '<p>Can an efficiency of 100 % be reached? The second law of thermodynamics says no. Heat does not pass by itself from a cold body to a hot one, and an engine cannot turn all the heat received into work. The French engineer Sadi Carnot showed that the greatest efficiency depends only on the temperatures of the heater <em>T₁</em> and cooler <em>T₂</em> (in kelvins):</p>')
 + formula('η<sub>max</sub> = 1 − T₂ / T₁', 'реальный двигатель всегда имеет КПД ниже этого предела', 'a real engine always has an efficiency below this limit')
 + bd('<p>Чтобы КПД был выше, нужна как можно более высокая температура нагревателя и низкая — холодильника. Поэтому в турбинах стремятся к высокой температуре пара, а в холодном воздухе тепловой двигатель работает чуть лучше, чем в жарком.</p>',
      '<p>To raise the efficiency, the heater should be as hot as possible and the cooler as cold as possible. That is why turbines aim for a high steam temperature, and a heat engine works slightly better in cold air than in hot.</p>'),
 lab3)

tasks = [
 task(1, 'КПД двигателя', 'Engine efficiency', 'Двигатель получил от нагревателя 40 МДж тепла и отдал холодильнику 30 МДж. Найдите полезную работу и КПД.', 'An engine received 40 MJ of heat from the heater and gave 30 MJ to the cooler. Find the useful work and the efficiency.',
  'Q₁ = 40 МДж, Q₂ = 30 МДж', 'Q₁ = 40 MJ, Q₂ = 30 MJ', 'A = Q₁ − Q₂ = 10 МДж.<br>η = A / Q₁ = 10 / 40 = 0,25.', 'A = Q₁ − Q₂ = 10 MJ.<br>η = A / Q₁ = 10 / 40 = 0.25.',
  'A = 10 МДж, КПД 25 %.', 'A = 10 MJ, efficiency 25 %.', True),
 task(2, 'Работа двигателя', 'Engine work', 'Двигатель с КПД 30 % получил за цикл 2000 Дж тепла. Сколько работы он совершил и сколько тепла отдал холодильнику?', 'An engine with an efficiency of 30 % received 2,000 J of heat per cycle. How much work did it do and how much heat did it give to the cooler?',
  'η = 0,3, Q₁ = 2000 Дж', 'η = 0.3, Q₁ = 2,000 J', 'A = η·Q₁ = 0,3 · 2000 = 600 Дж.<br>Q₂ = Q₁ − A = 1400 Дж.', 'A = η·Q₁ = 0.3 · 2,000 = 600 J.<br>Q₂ = Q₁ − A = 1,400 J.',
  '600 Дж работы, 1400 Дж холодильнику.', '600 J of work, 1,400 J to the cooler.'),
 task(3, 'Первый закон', 'The first law', 'Газу передали 800 Дж тепла, и он совершил работу 300 Дж. Как изменилась его внутренняя энергия?', 'A gas was given 800 J of heat and did 300 J of work. How did its internal energy change?',
  'Q = 800 Дж, A = 300 Дж', 'Q = 800 J, A = 300 J', 'ΔU = Q − A = 800 − 300 = 500 Дж.', 'ΔU = Q − A = 800 − 300 = 500 J.',
  'увеличилась на 500 Дж (газ нагрелся).', 'increased by 500 J (the gas warmed).'),
 task(4, 'Предел Карно', 'The Carnot limit', 'Нагреватель имеет температуру 527 °C, холодильник — 27 °C. Каков наибольший возможный КПД?', 'The heater is at 527 °C and the cooler at 27 °C. What is the greatest possible efficiency?',
  't₁ = 527 °C, t₂ = 27 °C', 't₁ = 527 °C, t₂ = 27 °C', 'T₁ = 527 + 273 = 800 К, T₂ = 27 + 273 = 300 К.<br>η = 1 − 300/800 = 1 − 0,375 = 0,625.', 'T₁ = 527 + 273 = 800 K, T₂ = 27 + 273 = 300 K.<br>η = 1 − 300/800 = 1 − 0.375 = 0.625.',
  '62,5 %. Реальный двигатель при этих температурах будет заметно хуже.', '62.5 %. A real engine at these temperatures will be noticeably worse.'),
 task(5, 'Бензин и работа', 'Petrol and work', 'При сгорании 1 кг бензина выделяется 46 МДж. Двигатель с КПД 25 % сжёг 2 кг. Какую работу он совершил? Сколько это в кВт·ч?', 'Burning 1 kg of petrol releases 46 MJ. An engine with an efficiency of 25 % burnt 2 kg. How much work did it do? How many kWh is that?',
  'q = 46 МДж/кг, m = 2 кг, η = 0,25', 'q = 46 MJ/kg, m = 2 kg, η = 0.25', 'Q₁ = q·m = 92 МДж.<br>A = η·Q₁ = 0,25 · 92 = 23 МДж.<br>23 / 3,6 ≈ 6,4 кВт·ч.', 'Q₁ = q·m = 92 MJ.<br>A = η·Q₁ = 0.25 · 92 = 23 MJ.<br>23 / 3.6 ≈ 6.4 kWh.',
  '23 МДж, то есть около 6,4 кВт·ч.', '23 MJ, that is about 6.4 kWh.'),
 task(6, 'Возможно ли?', 'Is it possible?', 'Изобретатель утверждает, что его двигатель работает между 400 К и 300 К с КПД 30 %. Возможно ли это?', 'An inventor claims his engine works between 400 K and 300 K with an efficiency of 30 %. Is this possible?',
  'T₁ = 400 К, T₂ = 300 К, η = 0,3', 'T₁ = 400 K, T₂ = 300 K, η = 0.3', 'η<sub>max</sub> = 1 − 300/400 = 0,25.<br>0,30 > 0,25.', 'η<sub>max</sub> = 1 − 300/400 = 0.25.<br>0.30 > 0.25.',
  'Невозможно: заявленный КПД выше предела Карно 25 %.', 'Impossible: the claimed efficiency exceeds the Carnot limit of 25 %.'),
]

quiz = [
 ('Что утверждает первый закон термодинамики?', [('Тепло идёт только от горячего к холодному', 'Это второй закон.'), ('Полученное тепло идёт на изменение внутренней энергии и на работу', 'Верно: Q = ΔU + A.'), ('КПД всегда равен 100 %', 'КПД всегда меньше 100 %.')],
  'What does the first law of thermodynamics state?', [('Heat flows only from hot to cold', 'That is the second law.'), ('The heat received goes into a change of internal energy and into work', 'Correct: Q = ΔU + A.'), ('The efficiency always equals 100 %', 'The efficiency is always below 100 %.')], 1),
 ('Газ получил 500 Дж и совершил работу 500 Дж. Что с его температурой?', [('Выросла', 'ΔU = Q − A = 0.'), ('Не изменилась', 'Верно: внутренняя энергия осталась прежней.'), ('Упала', 'Для этого работа должна быть больше тепла.')],
  'A gas received 500 J and did 500 J of work. What about its temperature?', [('It rose', 'ΔU = Q − A = 0.'), ('It did not change', 'Correct: the internal energy stayed the same.'), ('It fell', 'For that the work would have to exceed the heat.')], 1),
 ('Как определяется КПД теплового двигателя?', [('η = A / Q₁', 'Верно: полезная работа к полученному теплу.'), ('η = Q₁ / A', 'Так получилось бы число больше 1.'), ('η = Q₂ / Q₁', 'Это доля тепла, отданного холодильнику.')],
  'How is the efficiency of a heat engine defined?', [('η = A / Q₁', 'Correct: useful work to heat received.'), ('η = Q₁ / A', 'That would give a number greater than 1.'), ('η = Q₂ / Q₁', 'That is the share of heat given to the cooler.')], 0),
 ('Может ли КПД теплового двигателя быть равен 100 %?', [('Да, у хорошего двигателя', 'Это запрещает второй закон термодинамики.'), ('Нет: часть тепла всегда уходит холодильнику', 'Верно.'), ('Да, если нет трения', 'Даже без трения часть тепла обязательно уходит холодильнику.')],
  'Can the efficiency of a heat engine be 100 %?', [('Yes, in a good engine', 'The second law of thermodynamics forbids it.'), ('No: some heat always goes to the cooler', 'Correct.'), ('Yes, if there is no friction', 'Even without friction some heat must go to the cooler.')], 1),
 ('Двигатель получил 1000 Дж и отдал холодильнику 700 Дж. Каков КПД?', [('30 %', 'Верно: A = 300 Дж, η = 0,3.'), ('70 %', 'Это доля тепла, отданного холодильнику.'), ('130 %', 'КПД не может превышать 100 %.')],
  'An engine received 1,000 J and gave 700 J to the cooler. What is its efficiency?', [('30 %', 'Correct: A = 300 J, η = 0.3.'), ('70 %', 'That is the share of heat given to the cooler.'), ('130 %', 'Efficiency cannot exceed 100 %.')], 0),
 ('В каких температурах подставляют в формулу КПД Карно?', [('В градусах Цельсия', 'Тогда формула даст неверный результат.'), ('В кельвинах', 'Верно: нужна абсолютная шкала.'), ('В градусах Фаренгейта', 'Формула требует абсолютной температуры.')],
  'In which temperatures are values inserted into the Carnot efficiency formula?', [('In degrees Celsius', 'The formula would give a wrong result.'), ('In kelvins', 'Correct: the absolute scale is needed.'), ('In degrees Fahrenheit', 'The formula requires the absolute temperature.')], 1),
 ('Как повысить предельный КПД Карно?', [('Повысить температуру нагревателя', 'Верно: η = 1 − T₂/T₁ растёт, когда T₁ больше.'), ('Повысить температуру холодильника', 'Тогда предел снизится.'), ('Увеличить массу двигателя', 'Предел от массы не зависит.')],
  'How can the Carnot efficiency limit be raised?', [('Raise the heater temperature', 'Correct: η = 1 − T₂/T₁ grows when T₁ is greater.'), ('Raise the cooler temperature', 'That would lower the limit.'), ('Increase the engine mass', 'The limit does not depend on mass.')], 0),
 ('Почему двигатель автомобиля нужно охлаждать?', [('Из-за плохого КПД часть тепла топлива остаётся в двигателе', 'Верно: большая часть энергии топлива уходит в тепло.'), ('Чтобы увеличить скорость', 'Охлаждение скорость не повышает.'), ('Тепла в двигателе нет', 'Тепла много: КПД около 25–30 %.')],
  'Why does a car engine need cooling?', [('Because of the low efficiency part of the fuel heat stays in the engine', 'Correct: most of the fuel’s energy ends up as heat.'), ('To increase the speed', 'Cooling does not raise the speed.'), ('There is no heat in the engine', 'There is a lot: the efficiency is about 25–30 %.')], 0),
]

js = r'''
const T={ru:{
 flLabel:"Столбики тепла, работы и изменения внутренней энергии",enLabel:"Потоки энергии теплового двигателя",caLabel:"Шкала КПД: предел Карно",
 heat:"тепло Q",work:"работа A",du:"ΔU",heater:"нагреватель",cooler:"холодильник",useful:"работа",
 warm:"нагревается",cool:"охлаждается",same:"температура не меняется",
 flFb:["Газ нагревается: часть тепла осталась внутри.","Газ охлаждается: работа больше полученного тепла.","Внутренняя энергия не изменилась."],
 enFb:"Чем меньше КПД, тем больше энергии уходит холодильнику (в окружающую среду).",
 caFb:"Реальный двигатель всегда хуже предела Карно.",
 nl:"предел"},
 en:{
 flLabel:"Bars of heat, work and the change of internal energy",enLabel:"Energy flows of a heat engine",caLabel:"An efficiency scale: the Carnot limit",
 heat:"heat Q",work:"work A",du:"ΔU",heater:"heater",cooler:"cooler",useful:"work",
 warm:"warms up",cool:"cools down",same:"temperature unchanged",
 flFb:["The gas warms: some heat stayed inside.","The gas cools: the work exceeds the heat received.","The internal energy did not change."],
 enFb:"The lower the efficiency, the more energy goes to the cooler (the surroundings).",
 caFb:"A real engine is always below the Carnot limit.",
 nl:"limit"}};
function drawFl(){const t=tt(),Q=+$("fQ").value,A=+$("fA").value,U=Q-A,k=400/1000;
 const row=(y,lab,v,col)=>svgText(150,y+20,lab,"#18181a","end",12)+'<rect x="'+(v>=0?160:160+v*k)+'" y="'+y+'" width="'+Math.abs(v)*k+'" height="30" fill="'+col+'" stroke="#18181a"/>'+svgText(v>=0?166+v*k:154+v*k,y+20,fmt(v,0)+(lang==="ru"?" Дж":" J"),"#18181a",v>=0?"start":"end",12);
 let g='<line x1="160" y1="40" x2="160" y2="210" stroke="#18181a"/>'+row(50,t.heat,Q,"#b6533f")+row(100,t.work,A,"#3f5f8f")+row(150,t.du,U,"#2f6f5d");
 $("flSvg").innerHTML=g;
 $("fQOut").textContent=Q+(lang==="ru"?" Дж":" J");$("fAOut").textContent=A+(lang==="ru"?" Дж":" J");
 $("fU").textContent=(U>0?"+":"")+U+(lang==="ru"?" Дж":" J");
 const s=U>0?0:U<0?1:2;$("fS").textContent=[t.warm,t.cool,t.same][s];$("flFb").textContent=t.flFb[s]}
["fQ","fA"].forEach(id=>$(id).addEventListener("input",drawFl));
function drawEn(){const t=tt(),Q1=+$("eQ1").value,e=+$("eE").value/100,A=Q1*e,Q2=Q1-A;
 const H=Q1/1000*150+20,ha=A/Q1*H,hq=H-ha;
 let g='<rect x="40" y="'+(230-H)+'" width="120" height="'+H+'" fill="#b6533f" stroke="#18181a"/>'+svgText(100,246,t.heater,"#18181a","middle",11)+svgText(100,222-H,fmt(Q1,0)+" "+(lang==="ru"?"Дж":"J"),"#18181a","middle",11);
 g+='<rect x="230" y="110" width="140" height="90" rx="8" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/>'+svgText(300,162,"η = "+Math.round(e*100)+" %","#18181a","middle",18);
 g+='<line x1="160" y1="155" x2="230" y2="155" stroke="#18181a" stroke-width="2"/>';
 g+='<rect x="440" y="'+(230-ha)+'" width="120" height="'+ha+'" fill="#2f6f5d" stroke="#18181a"/>'+svgText(500,246,t.useful,"#2f6f5d","middle",11)+svgText(500,222-ha,fmt(A,0)+" "+(lang==="ru"?"Дж":"J"),"#18181a","middle",11);
 g+='<rect x="440" y="'+(230-H)+'" width="120" height="'+hq+'" fill="#c9c2b0" stroke="#18181a"/>'+svgText(500,222-H,fmt(Q2,0)+" "+(lang==="ru"?"Дж":"J")+" → "+t.cooler,"#66666b","middle",11);
 $("enSvg").innerHTML=g;
 $("eQ1Out").textContent=Q1+(lang==="ru"?" Дж":" J");$("eEOut").textContent=Math.round(e*100)+" %";
 $("eA").textContent=fmt(A,0)+(lang==="ru"?" Дж":" J");$("eQ2").textContent=fmt(Q2,0)+(lang==="ru"?" Дж":" J");$("eK").textContent=Math.round(e*100)+" %";$("enFb").textContent=t.enFb}
["eQ1","eE"].forEach(id=>$(id).addEventListener("input",drawEn));
function drawCa(){const t=tt(),Th=+$("cH").value,Tc=+$("cC").value,lim=Math.max(0,1-Tc/Th);
 const X=v=>60+v*480;
 let g='<rect x="60" y="90" width="480" height="40" fill="#e8e4d8" stroke="#18181a"/><rect x="60" y="90" width="'+lim*480+'" height="40" fill="#2f6f5d" stroke="#18181a"/>';
 for(let k=0;k<=10;k++)g+=svgText(X(k/10),152,k*10+" %","#66666b","middle",10);
 g+=svgText(60+lim*480,80,Math.round(lim*100)+" % ("+t.nl+")","#2f6f5d",lim>0.8?"end":"start",12);
 g+=svgText(60,200,"T₁ = "+Th+" K, T₂ = "+Tc+" K","#18181a","start",13)+svgText(60,224,"η = 1 − "+Tc+" / "+Th,"#18181a","start",13);
 $("caSvg").innerHTML=g;
 $("cHOut").textContent=Th+" K";$("cCOut").textContent=Tc+" K";
 $("cE").textContent=fmt(lim*100,1)+" %";$("cD").textContent=fmt((1-lim)*100,1)+(lang==="ru"?" Дж":" J");$("caFb").textContent=t.caFb}
["cH","cC"].forEach(id=>$(id).addEventListener("input",drawCa));
const LAB={ru:{flSvg:T.ru.flLabel,enSvg:T.ru.enLabel,caSvg:T.ru.caLabel},en:{flSvg:T.en.flLabel,enSvg:T.en.enLabel,caSvg:T.en.caLabel}};
function drawAll(){drawFl();drawEn();drawCa()}
'''

c = dict(n='12', slug='12-heat-engines.html', block='II', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Тепловые двигатели', 'Heat engines'),
 desc='Глава 12 Атласа физики: первый закон термодинамики, тепловые двигатели, КПД, предел Карно.',
 lead=('Машина едет, потому что топливо горит. Но почему из каждых 100 Дж энергии бензина в движение превращаются лишь около 25–30? Первый закон термодинамики, КПД и предел Карно.',
       'A car moves because fuel burns. But why do only about 25–30 of every 100 J of petrol energy become motion? The first law of thermodynamics, efficiency and the Carnot limit.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('law', 'Первый закон', 'First law'), ('engine', 'Двигатель и КПД', 'Engine and efficiency'), ('carnot', 'Предел Карно', 'Carnot limit'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>После долгой поездки капот автомобиля горячий, а из выхлопной трубы идёт тёплый газ. Мы заплатили за бензин, чтобы ехать, а часть его энергии, похоже, просто ушла в нагрев воздуха.</p><p>Нельзя ли придумать двигатель, который превратит в движение всё тепло топлива без остатка?</p>',
         '<p>After a long drive the car’s bonnet is hot and warm gas comes out of the exhaust. We paid for petrol to travel, yet part of its energy seems simply to have heated the air.</p><p>Could an engine be invented that turns all of the fuel’s heat into motion without leftovers?</p>'),
 hint=('Подсказку даст модель «Предел Карно». Разгадка — в конце главы.', 'The “Carnot limit” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему нельзя превратить всё тепло в работу', 'The answer: why not all heat can become work'),
 answer=('<p>Нельзя. Второй закон термодинамики и результат Карно говорят, что тепловой двигатель обязан отдавать часть тепла холодильнику, и наибольший КПД равен 1 − T₂/T₁. Даже идеальный двигатель между 800 К и 300 К не поднимется выше 62,5 % (задача 4), а реальные бензиновые двигатели работают с КПД примерно 25–30 %.</p><p>Тёплый капот и выхлопные газы — не недоработка механиков, а необходимая часть работы любого теплового двигателя. Повысить КПД можно, поднимая температуру нагревателя и уменьшая потери, но до 100 % добраться нельзя.</p>',
         '<p>It cannot. The second law of thermodynamics and Carnot’s result say that a heat engine must give some heat to the cooler, and the greatest efficiency is 1 − T₂/T₁. Even an ideal engine between 800 K and 300 K cannot exceed 62.5 % (problem 4), and real petrol engines work at about 25–30 %.</p><p>The warm bonnet and exhaust gas are not a mechanic’s failure but a necessary part of the work of any heat engine. Efficiency can be improved by raising the heater temperature and cutting losses, but 100 % cannot be reached.</p>'),
 sources=[
  ('Первый и второй законы термодинамики, тепловые двигатели, КПД —', 'The first and second laws of thermodynamics, heat engines, efficiency —', LINK('https://en.wikipedia.org/wiki/Heat_engine', 'Wikipedia: Heat engine') + ', ' + LINK('https://en.wikipedia.org/wiki/Carnot%27s_theorem_(thermodynamics)', 'Wikipedia: Carnot’s theorem') + ', ' + LINK('https://physics.info/heat-engines/', 'The Physics Hypertextbook: Heat engines')),
  ('Типичный КПД бензиновых и дизельных двигателей —', 'Typical efficiency of petrol and diesel engines —', LINK('https://www.fueleconomy.gov/feg/atv.shtml', 'fueleconomy.gov: Where the energy goes')),
  ('Теплота сгорания бензина (46 МДж/кг) —', 'Heat of combustion of petrol (46 MJ/kg) —', LINK('https://www.fao.org/4/T0269E/t0269e0c.htm', 'FAO: Comparison of energy values'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Значения КПД двигателей — типичные.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The engine efficiency values are typical.'),
 prev=('11-phase-changes.html', 'Глава 11 · Плавление и кипение', 'Chapter 11 · Melting and boiling'),
 next=('13-weather-climate.html', 'Глава 13 · Погода и климат', 'Chapter 13 · Weather and climate'),
 js=js)
build(c)
