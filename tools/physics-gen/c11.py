# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ОТ ЛЬДА К ПАРУ', 'FROM ICE TO STEAM', 'phSvg', '0 0 600 290',
  slider('pm', 'Масса воды', 'Mass of water', 0.1, 2, 0.1, 1) + slider('pq', 'Подведено тепла (доля от нужного)', 'Heat supplied (share of the total needed)', 0, 100, 1, 30),
  stats([('pQ', 'Подведено', 'Supplied'), ('pT', 'Температура', 'Temperature'), ('pS', 'Состояние', 'State')]),
  'phFb', 'Схема условная: лёд при −20 °C нагревают до пара при 120 °C при нормальном давлении, без потерь. c льда ≈ 2090, воды ≈ 4186, пара ≈ 2010 Дж/(кг·К).',
  'A schematic drawing: ice at −20 °C is heated to steam at 120 °C at normal pressure, with no losses. c of ice ≈ 2090, of water ≈ 4186, of steam ≈ 2010 J/(kg·K).')
s1 = section('melt', 'Плавление и кристаллизация', 'Melting and crystallization',
 bd('<p>Лёд, нагреваясь, доходит до 0 °C и начинает таять. Пока лёд не растает полностью, его температура не растёт, хотя тепло продолжает поступать: энергия уходит на разрушение кристаллической решётки. У кристаллических веществ плавление идёт при определённой температуре плавления. Когда вещество застывает (кристаллизуется), оно отдаёт столько же тепла.</p><p>Тепло, нужное для плавления при температуре плавления, пропорционально массе:</p>',
    '<p>Warming ice reaches 0 °C and starts to melt. Until all the ice has melted its temperature does not rise, although heat keeps coming in: the energy goes into breaking the crystal lattice. Crystalline substances melt at a definite melting temperature. When a substance solidifies (crystallizes) it gives away the same amount of heat.</p><p>The heat needed for melting at the melting temperature is proportional to the mass:</p>')
 + formula('Q = λ · m', 'λ — удельная теплота плавления (Дж/кг); для льда λ ≈ 334 кДж/кг', 'λ is the specific heat of fusion (J/kg); for ice λ ≈ 334 kJ/kg')
 + table(['ВЕЩЕСТВО', 'λ, КДЖ/КГ'], ['SUBSTANCE', 'λ, kJ/kg'], [[('Лёд (вода)', 'Ice (water)'), '334'], [('Алюминий', 'Aluminium'), '380'], [('Медь', 'Copper'), '134'], [('Свинец', 'Lead'), '24,5']])
 + bd('<p>Чтобы растопить 1 кг льда, нужно столько же тепла, сколько нужно, чтобы нагреть 1 кг воды почти на 80 К. Поэтому лёд в напитке охлаждает его так хорошо.</p>',
      '<p>Melting 1 kg of ice takes as much heat as warming 1 kg of water by almost 80 K. That is why ice cools a drink so well.</p>'),
 lab1)

lab2 = model(2, 'ЛЁД В СТАКАНЕ', 'ICE IN A GLASS', 'icSvg', '0 0 600 250',
  slider('wm', 'Масса воды', 'Mass of water', 0.1, 1, 0.05, 0.3) + slider('wt', 'Температура воды', 'Water temperature', 0, 80, 1, 25) + slider('im', 'Масса льда (0 °C)', 'Mass of ice (0 °C)', 0.02, 0.5, 0.01, 0.1),
  stats([('iT', 'Итоговая температура', 'Final temperature'), ('iM', 'Растаяло', 'Melted'), ('iL', 'Осталось льда', 'Ice left')]),
  'icFb', 'Схема условная: потерь тепла нет; лёд берётся при 0 °C.', 'A schematic drawing: there are no heat losses; the ice is taken at 0 °C.')
s2 = section('mixing', 'Лёд и вода: баланс с плавлением', 'Ice and water: a balance with melting',
 bd('<p>Если бросить лёд в тёплую воду, вода отдаёт тепло, а лёд сначала плавится при 0 °C, потом получившаяся вода нагревается. Хватит ли тепла, чтобы растопить весь лёд, показывает сравнение: может ли вода, остывая до 0 °C, отдать <em>c·m·t</em> джоулей, не меньше, чем нужно на плавление <em>λ·m<sub>л</sub></em>. Если хватает, лёд растает весь, а смесь нагреется выше 0 °C. Если не хватает, часть льда останется, и температура будет 0 °C.</p>',
    '<p>If ice is dropped into warm water, the water gives heat; the ice first melts at 0 °C, then the resulting water warms up. Whether there is enough heat to melt all the ice is shown by a comparison: can the water, cooling to 0 °C, give <em>c·m·t</em> joules, not less than <em>λ·m<sub>ice</sub></em> needed for melting? If so, all the ice melts and the mixture warms above 0 °C. If not, some ice remains and the temperature is 0 °C.</p>'),
 lab2)

lab3 = model(3, 'КИПЕНИЕ НА ВЫСОТЕ', 'BOILING AT ALTITUDE', 'blSvg', '0 0 600 280',
  slider('bh', 'Высота над уровнем моря', 'Altitude above sea level', 0, 5000, 1, 1607),
  stats([('bP', 'Давление воздуха', 'Air pressure'), ('bT', 'Вода кипит при', 'Water boils at'), ('bD', 'Ниже, чем на уровне моря', 'Lower than at sea level')]),
  'blFb', 'Схема условная. Давление — по модели стандартной атмосферы, температура кипения — по уравнению Антуана. Метки: поверхность Иссык-Куля (1607 м) и перевал Төө-Ашуу (3586 м).',
  'A schematic drawing. The pressure follows the standard-atmosphere model, the boiling temperature the Antoine equation. Marks: the surface of Issyk-Kul (1607 m) and the Töö-Ashuu pass (3586 m).')
s3 = section('boil', 'Испарение и кипение', 'Evaporation and boiling',
 bd('<p>Жидкость переходит в пар двумя способами. <strong>Испарение</strong> идёт с поверхности при любой температуре: самые быстрые частицы вырываются наружу. <strong>Кипение</strong> идёт по всему объёму при определённой температуре кипения: внутри жидкости образуются пузырьки пара.</p><p>Как и при плавлении, во время кипения температура не растёт, а тепло идёт на превращение жидкости в пар:</p>',
    '<p>A liquid turns into vapour in two ways. <strong>Evaporation</strong> occurs at the surface at any temperature: the fastest particles break out. <strong>Boiling</strong> occurs throughout the volume at a definite boiling temperature: bubbles of vapour form inside the liquid.</p><p>As with melting, the temperature does not rise during boiling; the heat goes into turning liquid into vapour:</p>')
 + formula('Q = L · m', 'L — удельная теплота парообразования; для воды при 100 °C L ≈ 2256 кДж/кг', 'L is the specific heat of vaporization; for water at 100 °C L ≈ 2,256 kJ/kg')
 + bd('<p>Это очень много: чтобы выкипятить 1 кг воды, нужно примерно в 5,4 раза больше тепла, чем чтобы нагреть её от 20 до 100 °C. Когда пар конденсируется, он отдаёт столько же тепла — поэтому ожог паром опаснее ожога кипятком.</p><p>Испарение отнимает тепло у того, что остаётся, и охлаждает его. На коже при температуре тела на испарение килограмма воды уходит около 2428 кДж, так что пот охлаждает нас, а в мокрой одежде на ветру холодно.</p><p><strong>Температура кипения зависит от давления.</strong> На высоте давление воздуха ниже (глава 4), поэтому вода закипает при температуре ниже 100 °C: на поверхности Иссык-Куля примерно при 95 °C, а на перевале Төө-Ашуу около 88 °C. В такой воде продукты варятся дольше.</p>',
      '<p>That is a lot: to boil away 1 kg of water takes about 5.4 times more heat than to warm it from 20 to 100 °C. When vapour condenses it gives away the same heat — which is why a steam burn is more dangerous than one from boiling water.</p><p>Evaporation takes heat from what remains and cools it. On skin at body temperature about 2,428 kJ go into evaporating a kilogram of water, so sweat cools us and in wet clothes on a wind it is cold.</p><p><strong>The boiling point depends on pressure.</strong> At altitude the air pressure is lower (chapter 4), so water boils below 100 °C: at the surface of Issyk-Kul at about 95 °C, and at the Töö-Ashuu pass at about 88 °C. Food cooks more slowly in such water.</p>'),
 lab3)

tasks = [
 task(1, 'Растопить лёд', 'Melting ice', 'Сколько тепла нужно, чтобы растопить 0,5 кг льда, взятого при 0 °C? λ = 334 кДж/кг.', 'How much heat is needed to melt 0.5 kg of ice taken at 0 °C? λ = 334 kJ/kg.',
  'm = 0,5 кг, λ = 334 000 Дж/кг', 'm = 0.5 kg, λ = 334,000 J/kg', 'Q = λ·m = 334 000 · 0,5 = 167 000 Дж.', 'Q = λ·m = 334,000 · 0.5 = 167,000 J.',
  '167 кДж. Это столько же, сколько нужно, чтобы нагреть 0,5 кг воды почти на 80 К.', '167 kJ. That is as much as it takes to warm 0.5 kg of water by almost 80 K.', True),
 task(2, 'Лёд в напитке', 'Ice in a drink', 'В 0,2 кг воды при 25 °C бросили лёд при 0 °C. Сколько льда растает, пока вода остынет до 0 °C?', 'Ice at 0 °C was dropped into 0.2 kg of water at 25 °C. How much ice melts while the water cools to 0 °C?',
  'm = 0,2 кг, t = 25 °C, c = 4186, λ = 334 000', 'm = 0.2 kg, t = 25 °C, c = 4,186, λ = 334,000', 'Вода отдаст: Q = c·m·t = 4186 · 0,2 · 25 = 20 930 Дж.<br>Растает: m<sub>л</sub> = Q / λ = 20 930 / 334 000 ≈ 0,063 кг.',
  'Water will give: Q = c·m·t = 4,186 · 0.2 · 25 = 20,930 J.<br>Melted: m<sub>ice</sub> = Q / λ = 20,930 / 334,000 ≈ 0.063 kg.', 'около 63 г льда.', 'about 63 g of ice.'),
 task(3, 'Выкипятить воду', 'Boiling water away', 'Сколько тепла нужно, чтобы превратить в пар 0,5 кг кипящей воды при 100 °C? L = 2256 кДж/кг. Сколько времени это займёт у нагревателя мощностью 2 кВт без потерь?', 'How much heat is needed to turn 0.5 kg of boiling water at 100 °C into steam? L = 2,256 kJ/kg. How long will it take with a 2 kW heater with no losses?',
  'm = 0,5 кг, L = 2 256 000 Дж/кг, P = 2000 Вт', 'm = 0.5 kg, L = 2,256,000 J/kg, P = 2,000 W', 'Q = L·m = 2 256 000 · 0,5 = 1 128 000 Дж.<br>t = Q / P = 1 128 000 / 2000 = 564 с.', 'Q = L·m = 2,256,000 · 0.5 = 1,128,000 J.<br>t = Q / P = 1,128,000 / 2,000 = 564 s.',
  'около 1,13 МДж; 564 с, то есть 9,4 мин.', 'about 1.13 MJ; 564 s, that is 9.4 min.'),
 task(4, 'Из воды в пар', 'From water to steam', 'Сколько тепла нужно, чтобы 1 кг воды при 20 °C полностью превратить в пар при 100 °C?', 'How much heat is needed to turn 1 kg of water at 20 °C completely into steam at 100 °C?',
  'm = 1 кг, t₁ = 20 °C, t₂ = 100 °C', 'm = 1 kg, t₁ = 20 °C, t₂ = 100 °C', '1) Нагрев: Q₁ = c·m·Δt = 4186 · 1 · 80 = 334 880 Дж.<br>2) Парообразование: Q₂ = L·m = 2 256 000 Дж.<br>3) Всего: Q = Q₁ + Q₂ = 2 590 880 Дж.', '1) Warming: Q₁ = c·m·Δt = 4,186 · 1 · 80 = 334,880 J.<br>2) Vaporization: Q₂ = L·m = 2,256,000 J.<br>3) Total: Q = Q₁ + Q₂ = 2,590,880 J.',
  'примерно 2,59 МДж; на парообразование уходит около 87 % всего тепла.', 'about 2.59 MJ; about 87 % of the heat goes into vaporization.'),
 task(5, 'Пот', 'Sweat', 'Сколько тепла отнимает у тела испарение 100 г пота? При температуре тела L ≈ 2428 кДж/кг.', 'How much heat does the evaporation of 100 g of sweat take from the body? At body temperature L ≈ 2,428 kJ/kg.',
  'm = 0,1 кг, L = 2 428 000 Дж/кг', 'm = 0.1 kg, L = 2,428,000 J/kg', 'Q = L·m = 2 428 000 · 0,1 = 242 800 Дж.', 'Q = L·m = 2,428,000 · 0.1 = 242,800 J.',
  'около 243 кДж. Так тело охлаждается в жару.', 'about 243 kJ. That is how the body cools in the heat.'),
 task(6, 'Расплавить алюминий', 'Melting aluminium', 'Сколько тепла нужно, чтобы расплавить 2 кг алюминия, уже нагретого до температуры плавления? λ = 380 кДж/кг.', 'How much heat is needed to melt 2 kg of aluminium already heated to its melting temperature? λ = 380 kJ/kg.',
  'm = 2 кг, λ = 380 000 Дж/кг', 'm = 2 kg, λ = 380,000 J/kg', 'Q = λ·m = 380 000 · 2 = 760 000 Дж.', 'Q = λ·m = 380,000 · 2 = 760,000 J.',
  '760 кДж. Металл при этом остаётся при температуре плавления.', '760 kJ. The metal stays at its melting temperature all the while.'),
]

quiz = [
 ('Что происходит с температурой кристаллического вещества во время плавления?', [('Растёт', 'Пока вещество плавится, температура остаётся постоянной.'), ('Остаётся постоянной', 'Верно: энергия идёт на разрушение кристаллической решётки.'), ('Падает', 'Вещество получает тепло, температура не падает.')],
  'What happens to the temperature of a crystalline substance during melting?', [('It rises', 'While the substance melts the temperature stays constant.'), ('It stays constant', 'Correct: the energy goes into breaking the crystal lattice.'), ('It falls', 'The substance receives heat; the temperature does not fall.')], 1),
 ('В каких единицах измеряют удельную теплоту плавления λ?', [('Дж/кг', 'Верно: энергия на килограмм вещества.'), ('Дж/(кг·К)', 'Это единицы удельной теплоёмкости.'), ('Вт', 'Это единица мощности.')],
  'In which units is the specific heat of fusion λ measured?', [('J/kg', 'Correct: energy per kilogram of the substance.'), ('J/(kg·K)', 'Those are the units of specific heat capacity.'), ('W', 'That is a unit of power.')], 0),
 ('Что требует больше тепла: растопить 1 кг льда при 0 °C или превратить 1 кг кипящей воды в пар?', [('Растопить лёд', 'Для льда нужно 334 кДж, для пара — 2256 кДж.'), ('Превратить воду в пар', 'Верно: L ≈ 2256 кДж/кг, это около 7 λ.'), ('Одинаково', 'Значения сильно различаются.')],
  'Which takes more heat: melting 1 kg of ice at 0 °C or turning 1 kg of boiling water into steam?', [('Melting the ice', 'Ice needs 334 kJ, steam needs 2,256 kJ.'), ('Turning the water into steam', 'Correct: L ≈ 2,256 kJ/kg, about 7 times λ.'), ('The same', 'The values are very different.')], 1),
 ('Чем кипение отличается от испарения?', [('Кипение идёт при любой температуре', 'При любой температуре идёт испарение.'), ('Кипение идёт по всему объёму при определённой температуре', 'Верно: внутри жидкости образуются пузырьки пара.'), ('Ничем', 'Это разные процессы.')],
  'How does boiling differ from evaporation?', [('Boiling occurs at any temperature', 'It is evaporation that occurs at any temperature.'), ('Boiling occurs throughout the volume at a definite temperature', 'Correct: bubbles of vapour form inside the liquid.'), ('There is no difference', 'They are different processes.')], 1),
 ('Почему после купания на ветру становится холодно?', [('Вода испаряется с кожи и отнимает тепло', 'Верно: испарение охлаждает.'), ('Вода тяжёлая', 'Дело не в массе воды.'), ('Ветер нагревает воду', 'Ветер лишь ускоряет испарение.')],
  'Why does one feel cold after swimming in the wind?', [('Water evaporates from the skin and takes heat away', 'Correct: evaporation cools.'), ('Water is heavy', 'It is not a matter of the water’s mass.'), ('The wind heats the water', 'The wind only speeds up evaporation.')], 0),
 ('Почему в горах вода кипит при температуре ниже 100 °C?', [('Там холоднее и вода не греется сильнее', 'Дело в давлении, а не в холоде воздуха.'), ('Там меньше атмосферное давление', 'Верно: температура кипения зависит от давления.'), ('Там вода другая', 'Вода та же; меняется давление.')],
  'Why does water boil below 100 °C in the mountains?', [('It is colder and the water cannot get hotter', 'It is a matter of pressure, not the cold air.'), ('The atmospheric pressure is lower there', 'Correct: the boiling temperature depends on pressure.'), ('The water is different there', 'The water is the same; the pressure changes.')], 1),
 ('Что происходит при конденсации пара?', [('Пар поглощает тепло', 'Поглощает тепло пар при образовании, а не при конденсации.'), ('Пар отдаёт тепло', 'Верно: столько же, сколько поглотилось при парообразовании.'), ('Температура пара растёт', 'Вещество отдаёт тепло, температура не растёт.')],
  'What happens when vapour condenses?', [('The vapour absorbs heat', 'It absorbs heat when forming, not when condensing.'), ('The vapour gives away heat', 'Correct: as much as was absorbed on vaporization.'), ('The vapour’s temperature rises', 'The substance gives away heat; the temperature does not rise.')], 1),
 ('Вода кипит на сильном огне, но её температура не растёт. Куда уходит тепло?', [('Исчезает', 'Энергия не исчезает: она сохраняется.'), ('Идёт на превращение воды в пар', 'Верно: L ≈ 2256 кДж/кг.'), ('Идёт на нагрев воздуха, а не воды', 'Часть тепла теряется, но главное — парообразование.')],
  'Water boils on a strong fire, but its temperature does not rise. Where does the heat go?', [('It disappears', 'Energy does not disappear: it is conserved.'), ('It turns the water into steam', 'Correct: L ≈ 2,256 kJ/kg.'), ('It heats the air, not the water', 'Some heat is lost, but the main thing is vaporization.')], 1),
]

js = r'''
const T={ru:{
 phLabel:"График температуры воды при нагревании от льда до пара",icLabel:"Стакан с водой и льдом",blLabel:"График температуры кипения воды в зависимости от высоты",
 states:["лёд","плавление","вода","кипение","пар"],
 phFb:["Лёд нагревается: температура растёт.","Лёд тает при 0 °C: температура не меняется, пока не растает весь лёд.","Вода нагревается.","Вода кипит при 100 °C: тепло идёт на парообразование, температура не растёт.","Пар нагревается."],
 icFb:["Тепла воды не хватает, чтобы растопить весь лёд: часть остаётся, температура смеси 0 °C.","Тепла хватает: весь лёд растаял, температура смеси выше 0 °C."],
 blFb:"Чем выше, тем ниже давление и температура кипения. Нормальное давление и 100 °C — на уровне моря.",
 ice:"лёд",wat:"вода",lake:"Иссык-Куль",pass:"Төө-Ашуу"},
 en:{
 phLabel:"A graph of water temperature when heated from ice to steam",icLabel:"A glass of water with ice",blLabel:"A graph of the boiling temperature of water against altitude",
 states:["ice","melting","water","boiling","steam"],
 phFb:["The ice warms: the temperature rises.","The ice melts at 0 °C: the temperature stays the same until all the ice has melted.","The water warms.","The water boils at 100 °C: heat goes into vaporization and the temperature does not rise.","The steam warms."],
 icFb:["The water’s heat is not enough to melt all the ice: some remains and the mixture is at 0 °C.","The heat is enough: all the ice has melted and the mixture is above 0 °C."],
 blFb:"The higher, the lower the pressure and the boiling temperature. Normal pressure and 100 °C are at sea level.",
 ice:"ice",wat:"water",lake:"Issyk-Kul",pass:"Töö-Ashuu"}};
const CI=2090,CWA=4186,CST=2010,LF=334000,LV=2256000;
function drawPh(){const t=tt(),m=+$("pm").value,pct=+$("pq").value/100;
 const Q1=CI*m*20,Q2=LF*m,Q3=CWA*m*100,Q4=LV*m,Q5=CST*m*20,Qt=Q1+Q2+Q3+Q4+Q5,Q=pct*Qt;
 let T0,st;
 if(Q<=Q1){T0=-20+Q/(CI*m);st=0}else if(Q<=Q1+Q2){T0=0;st=1}else if(Q<=Q1+Q2+Q3){T0=(Q-Q1-Q2)/(CWA*m);st=2}else if(Q<=Q1+Q2+Q3+Q4){T0=100;st=3}else{T0=100+(Q-Q1-Q2-Q3-Q4)/(CST*m);st=4}
 const X=q=>60+q/Qt*500,Y=v=>250-(v+20)/140*200;
 let g=axes(100,140,5,7,60,560,250,50,0,0).replace(/>(\d+)</g,function(a,b){return a});
 let pts=[[0,-20],[Q1,0],[Q1+Q2,0],[Q1+Q2+Q3,100],[Q1+Q2+Q3+Q4,100],[Qt,120]];
 g='';for(let k=0;k<=5;k++){const x=60+k/5*500;g+='<line x1="'+x+'" y1="250" x2="'+x+'" y2="50" stroke="#e3e1da"/>'+svgText(x,266,fmt(k*20,0)+" %","#66666b","middle",10)}
 [-20,0,20,40,60,80,100,120].forEach(v=>{g+='<line x1="60" y1="'+Y(v)+'" x2="560" y2="'+Y(v)+'" stroke="#e3e1da"/>'+svgText(54,Y(v)+4,v,"#66666b","end",10)});
 g+='<line x1="60" y1="250" x2="560" y2="250" stroke="#18181a"/><line x1="60" y1="250" x2="60" y2="50" stroke="#18181a"/>';
 g+='<polyline points="'+pts.map(p=>X(p[0])+","+Y(p[1])).join(" ")+'" fill="none" stroke="#c9c2b0" stroke-width="2" stroke-dasharray="4 3"/>';
 const part=[[0,-20]];[[Q1,0],[Q1+Q2,0],[Q1+Q2+Q3,100],[Q1+Q2+Q3+Q4,100],[Qt,120]].forEach(p=>{if(Q>=p[0])part.push(p)});part.push([Q,T0]);
 g+='<polyline points="'+part.map(p=>X(p[0])+","+Y(p[1])).join(" ")+'" fill="none" stroke="#b6533f" stroke-width="3"/><circle cx="'+X(Q)+'" cy="'+Y(T0)+'" r="5" fill="#b6533f"/>';
 g+=svgText(60,40,"t, °C","#18181a","start",11)+svgText(560,282,"Q","#18181a","end",11);
 $("phSvg").innerHTML=g;
 $("pmOut").textContent=fmt(m,1)+t.kg;$("pqOut").textContent=Math.round(pct*100)+" %";
 $("pQ").textContent=fmt(Q/1e6,2)+t.MJ;$("pT").textContent=fmt(T0,1)+t.C;$("pS").textContent=t.states[st];$("phFb").textContent=t.phFb[st]}
["pm","pq"].forEach(id=>$(id).addEventListener("input",drawPh));
function drawIc(){const t=tt(),mw=+$("wm").value,tw=+$("wt").value,mi=+$("im").value,Qa=CWA*mw*tw,Qm=LF*mi;
 let tf,melted,left;
 if(Qa>=Qm){melted=mi;left=0;tf=(Qa-Qm)/(CWA*(mw+mi))}else{melted=Qa/LF;left=mi-melted;tf=0}
 const wh=40+mw*110,ih=Math.min(110,left*220),col=v=>{const f=Math.max(0,Math.min(1,v/80));return "rgb("+Math.round(110+f*100)+","+Math.round(170-f*60)+","+Math.round(220-f*130)+")"};
 let g='<path d="M200 40 L215 215 L385 215 L400 40" fill="none" stroke="#18181a" stroke-width="3"/><path d="M'+(200+(215-200)*(1-wh/175))+' '+(215-wh)+' L215 215 L385 215 L'+(400-(400-385)*(1-wh/175))+' '+(215-wh)+' Z" fill="'+col(tf)+'" fill-opacity="0.75"/>';
 g+='<rect x="255" y="'+(215-wh-ih+6)+'" width="'+Math.min(90,40+left*140)+'" height="'+ih+'" rx="6" fill="#e8f2f8" stroke="#8eb8d1" stroke-width="2"/>';
 g+=svgText(300,236,fmt(tf,1)+t.C,"#18181a","middle",13);
 $("icSvg").innerHTML=g;
 $("wmOut").textContent=fmt(mw,2)+t.kg;$("wtOut").textContent=tw+t.C;$("imOut").textContent=fmt(mi,2)+t.kg;
 $("iT").textContent=fmt(tf,1)+t.C;$("iM").textContent=fmt(melted*1000,0)+t.g;$("iL").textContent=fmt(left*1000,0)+t.g;
 $("icFb").textContent=t.icFb[left>1e-9?0:1]}
["wm","wt","im"].forEach(id=>$(id).addEventListener("input",drawIc));
function Pair(h){return 101325*Math.pow(1-2.25577e-5*h,5.25588)}
function Tb(p){return 1730.63/(8.07131-Math.log10(p/133.322387415))-233.426}
function drawBl(){const t=tt(),h=+$("bh").value,p=Pair(h),tb=Tb(p),X=v=>60+v/5000*500,Y=v=>250-(v-80)/22*200;
 let g='';for(let k=0;k<=5;k++){const x=60+k/5*500;g+='<line x1="'+x+'" y1="250" x2="'+x+'" y2="50" stroke="#e3e1da"/>'+svgText(x,266,k*1000,"#66666b","middle",10)}
 [80,85,90,95,100].forEach(v=>{g+='<line x1="60" y1="'+Y(v)+'" x2="560" y2="'+Y(v)+'" stroke="#e3e1da"/>'+svgText(54,Y(v)+4,v,"#66666b","end",10)});
 g+='<line x1="60" y1="250" x2="560" y2="250" stroke="#18181a"/><line x1="60" y1="250" x2="60" y2="50" stroke="#18181a"/>';
 let pts=[];for(let k=0;k<=50;k++){const hh=k*100;pts.push(X(hh)+","+Y(Tb(Pair(hh))))}
 g+='<polyline points="'+pts.join(" ")+'" fill="none" stroke="#2f6f5d" stroke-width="3"/>';
 [[1607,t.lake],[3586,t.pass]].forEach(pp=>{const tt2=Tb(Pair(pp[0]));g+='<line x1="'+X(pp[0])+'" y1="250" x2="'+X(pp[0])+'" y2="'+Y(tt2)+'" stroke="#c9c2b0" stroke-dasharray="3 3"/>'+svgText(X(pp[0])+4,Y(tt2)-8,pp[1]+" "+fmt(tt2,0)+" °C","#66666b","start",10)});
 g+='<line x1="'+X(h)+'" y1="250" x2="'+X(h)+'" y2="'+Y(tb)+'" stroke="#b6533f" stroke-dasharray="3 3"/><circle cx="'+X(h)+'" cy="'+Y(tb)+'" r="5" fill="#b6533f"/>';
 g+=svgText(60,40,"t, °C","#18181a","start",11)+svgText(560,282,"h, "+(lang==="ru"?"м":"m"),"#18181a","end",11);
 $("blSvg").innerHTML=g;
 $("bhOut").textContent=num(h)+t.m;
 $("bP").textContent=fmt(p/1000,1)+(lang==="ru"?" кПа":" kPa");$("bT").textContent=fmt(tb,1)+t.C;$("bD").textContent=fmt(Tb(101325)-tb,1)+t.K;$("blFb").textContent=t.blFb}
$("bh").addEventListener("input",drawBl);
const LAB={ru:{phSvg:T.ru.phLabel,icSvg:T.ru.icLabel,blSvg:T.ru.blLabel},en:{phSvg:T.en.phLabel,icSvg:T.en.icLabel,blSvg:T.en.blLabel}};
function drawAll(){drawPh();drawIc();drawBl()}
'''

c = dict(n='11', slug='11-phase-changes.html', block='II', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Плавление, испарение, кипение', 'Melting, evaporation, boiling'),
 desc='Глава 11 Атласа физики: плавление и кристаллизация, удельная теплота плавления, испарение и кипение, теплота парообразования, кипение в горах.',
 lead=('Лёд тает, но не нагревается, вода кипит, но температура не растёт, а в горах чайник закипает раньше. Эта глава — о переходах вещества из одного состояния в другое и о тепле, которое на них уходит.',
       'Ice melts but does not warm, water boils but its temperature does not rise, and in the mountains a kettle boils sooner. This chapter is about the changes of a substance from one state to another and the heat they take.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('melt', 'Плавление', 'Melting'), ('mixing', 'Лёд в воде', 'Ice in water'), ('boil', 'Кипение', 'Boiling'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На сильном огне стоит чайник с холодной водой. Вода нагревается, потом закипает — и вот тут странность. Огонь не слабее, чайник по-прежнему получает тепло, а температура воды уже не растёт: градусник показывает всё те же 100 °C, сколько бы мы ни ждали.</p><p>Куда уходит тепло, если вода уже не нагревается?</p>',
         '<p>A kettle of cold water stands on a strong fire. The water warms, then boils — and here is the oddity. The fire is no weaker and the kettle keeps receiving heat, yet the temperature of the water no longer rises: the thermometer shows the same 100 °C however long we wait.</p><p>Where does the heat go if the water is no longer warming?</p>'),
 hint=('Подсказку даст модель «От льда к пару». Разгадка — в конце главы.', 'The “From ice to steam” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: куда уходит тепло при кипении', 'The answer: where the heat goes in boiling'),
 answer=('<p>Тепло идёт на превращение воды в пар. Частицам нужна энергия, чтобы разорвать связи между собой и улететь из жидкости: на каждый килограмм воды — около 2256 кДж (L ≈ 2256 кДж/кг). Пока вода не выкипит, вся поступающая энергия тратится на парообразование, а средняя энергия частиц — то есть температура — остаётся постоянной. Это та самая горизонтальная площадка на графике нагрева в модели 1.</p><p>Если же включить огонь сильнее, температура не станет выше 100 °C (при нормальном давлении) — вода просто выкипит быстрее. А в горах давление ниже, поэтому вода закипает раньше, при температуре ниже 100 °C: на перевале Төө-Ашуу — около 88 °C. Продукты в такой воде варятся дольше.</p>',
         '<p>The heat goes into turning water into vapour. The particles need energy to break the bonds between them and leave the liquid: about 2,256 kJ for every kilogram of water (L ≈ 2,256 kJ/kg). Until the water boils away, all the incoming energy is spent on vaporization, and the average energy of the particles — that is, the temperature — stays constant. This is the same horizontal plateau on the heating graph in model 1.</p><p>If the fire is made stronger the temperature will not exceed 100 °C (at normal pressure) — the water will just boil away faster. In the mountains the pressure is lower, so water boils sooner, below 100 °C: at the Töö-Ashuu pass about 88 °C. Food cooks more slowly in such water.</p>'),
 sources=[
  ('Удельные теплоты плавления и парообразования (вода 334 и 2256 кДж/кг; алюминий, медь, свинец) —', 'Specific heats of fusion and vaporization (water 334 and 2,256 kJ/kg; aluminium, copper, lead) —', LINK('https://openbooks.lib.msu.edu/collegephysics1/chapter/phase-change-and-latent-heat-2', 'OpenStax College Physics: Phase change and latent heat') + ', ' + LINK('https://courses.lumenlearning.com/suny-physics/chapter/14-3-phase-change-and-latent-heat/', 'Lumen Learning: Phase change and latent heat (пот при 37 °C)') + ', ' + LINK('https://engineeringtoolbox.com/water-thermal-properties--d_162.html', 'Engineering ToolBox: Water thermal properties')),
  ('Теплоёмкости льда, воды и пара —', 'Heat capacities of ice, water and steam —', LINK('https://engineeringtoolbox.com/specific-heat-capacity-d_391.html', 'Engineering ToolBox: Specific heat') + ', ' + LINK('https://alchemical.org/thermo/specificheattable.html', 'Specific heat capacities table')),
  ('Модель давления и температуры кипения на высоте (стандартная атмосфера, уравнение Антуана) — как в главе 4;', 'The model of pressure and boiling temperature with altitude (standard atmosphere, Antoine equation) — as in chapter 4;', LINK('https://aty.sdsu.edu/explain/thermal/std_atm.html', 'The Standard Atmosphere') + ', ' + LINK('https://en.wikipedia.org/wiki/Issyk-Kul', 'Wikipedia: Issyk-Kul (высота 1607 м / elevation 1,607 m)'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Значения L и λ — табличные; температуры кипения на высоте — расчётные.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The L and λ values are from tables; the boiling temperatures at altitude are calculated.'),
 prev=('10-heat-capacity.html', 'Глава 10 · Количество теплоты', 'Chapter 10 · Amount of heat'),
 next=('12-heat-engines.html', 'Глава 12 · Тепловые двигатели', 'Chapter 12 · Heat engines'),
 js=js)
build(c)
