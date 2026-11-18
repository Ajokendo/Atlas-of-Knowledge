# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'СКОЛЬКО ТЕПЛА НУЖНО ДЛЯ НАГРЕВА', 'HOW MUCH HEAT HEATING NEEDS', 'hcSvg', '0 0 600 270',
  select('hs', 'Вещество', 'Substance') + slider('hm', 'Масса', 'Mass', 0.5, 10, 0.5, 2) + slider('hd', 'Нагрев', 'Temperature rise', 5, 100, 5, 50),
  stats([('hQ', 'Нужное тепло', 'Heat needed'), ('hT', 'Время при 1 кВт', 'Time at 1 kW'), ('hR', 'Против воды', 'Against water')]),
  'hcFb', 'Схема условная: длина полосок пропорциональна удельной теплоёмкости вещества. Значения c — приближённые, для комнатных температур.',
  'A schematic drawing: the length of each bar is proportional to the substance’s specific heat capacity. The c values are approximate, for room temperatures.')
s1 = section('heat', 'Количество теплоты и удельная теплоёмкость', 'Amount of heat and specific heat capacity',
 bd('<p>Когда тело нагревается, оно получает энергию — <strong>количество теплоты</strong> <em>Q</em> (измеряют в джоулях). Чем больше масса и чем сильнее нагрев, тем больше энергии нужно. Но нужное количество зависит и от вещества. <strong>Удельная теплоёмкость</strong> <em>c</em> показывает, сколько энергии нужно, чтобы нагреть 1 кг вещества на 1 К:</p>',
    '<p>When a body warms up it receives energy — the <strong>amount of heat</strong> <em>Q</em> (measured in joules). The greater the mass and the stronger the heating, the more energy is needed. But the required amount depends on the substance too. The <strong>specific heat capacity</strong> <em>c</em> shows how much energy is needed to warm 1 kg of the substance by 1 K:</p>')
 + formula('Q = c · m · Δt', 'c в Дж/(кг·К); при остывании Δt < 0 и тело отдаёт тепло', 'c in J/(kg·K); when cooling Δt < 0 and the body gives heat away')
 + bd('<p>Вода имеет очень большую теплоёмкость: около 4186 Дж/(кг·К). У песка около 830, у стали 490, у меди 385, у воздуха около 1005. Это значит, что вода нагревается и остывает медленно, а песок или металл — быстро. Лёд (≈ 2090) нагревается легче воды.</p>',
      '<p>Water has a very large heat capacity: about 4186 J/(kg·K). Sand has about 830, steel 490, copper 385 and air about 1005. This means water heats and cools slowly, while sand or metal heat and cool quickly. Ice (≈ 2090) warms more easily than water.</p>'),
 lab1)

lab2 = model(2, 'СМЕШИВАНИЕ ВОДЫ', 'MIXING WATER', 'mxSvg', '0 0 600 270',
  slider('m1', 'Горячая вода: масса', 'Hot water: mass', 0.5, 10, 0.5, 3) + slider('t1', 'Горячая вода: температура', 'Hot water: temperature', 40, 100, 1, 80) + slider('m2', 'Холодная вода: масса', 'Cold water: mass', 0.5, 10, 0.5, 6) + slider('t2', 'Холодная вода: температура', 'Cold water: temperature', 0, 40, 1, 20),
  stats([('xT', 'Итоговая температура', 'Final temperature'), ('xQ1', 'Горячая отдала', 'Hot water gave'), ('xQ2', 'Холодная получила', 'Cold water received')]),
  'mxFb', 'Схема условная: потерь тепла в окружающую среду нет.', 'A schematic drawing: there is no heat loss to the surroundings.')
s2 = section('balance', 'Уравнение теплового баланса', 'The heat balance equation',
 bd('<p>Если смешать горячую и холодную воду в закрытом сосуде без потерь, горячая отдаёт столько тепла, сколько получает холодная. Это <strong>уравнение теплового баланса</strong>: <em>Q<sub>отд</sub> = Q<sub>пол</sub></em>. Для воды, у которой c одинакова, оно приводит к формуле итоговой температуры:</p>',
    '<p>If hot and cold water are mixed in a closed vessel without losses, the hot water gives away as much heat as the cold water receives. This is the <strong>heat balance equation</strong>: <em>Q<sub>given</sub> = Q<sub>received</sub></em>. For water, where c is the same, it leads to the formula for the final temperature:</p>')
 + formula('t = (m₁·t₁ + m₂·t₂) / (m₁ + m₂)', 'итоговая температура лежит между t₁ и t₂ и ближе к температуре той порции, масса которой больше', 'the final temperature lies between t₁ and t₂ and is closer to the temperature of the portion with the greater mass')
 + bd('<p>Так же считают, когда смешиваются разные вещества: нужно учесть разные c. Например, горячий камень в холодной воде отдаёт тепло воде, пока их температуры не сравняются.</p>',
      '<p>The same approach works when different substances are mixed: the different values of c must be accounted for. For example, a hot stone in cold water gives heat to the water until their temperatures become equal.</p>'),
 lab2)

lab3 = model(3, 'ТЕПЛОТА СГОРАНИЯ ТОПЛИВА', 'HEAT OF COMBUSTION', 'fuSvg', '0 0 600 250',
  select('fs', 'Топливо', 'Fuel') + slider('fm', 'Масса топлива', 'Mass of fuel', 0.1, 10, 0.1, 1) + slider('fe', 'КПД нагрева', 'Heating efficiency', 10, 100, 5, 30),
  stats([('fQ', 'Выделится тепла', 'Heat released'), ('fK', 'То же в кВт·ч', 'The same in kWh'), ('fW', 'Нагреет воды с 15 до 100 °C', 'Water heated from 15 to 100 °C')]),
  'fuFb', 'Схема условная. Значения q — типичные для воздушно-сухого топлива; реальные зависят от сорта и влажности. Вода нагревается без кипения.',
  'A schematic drawing. The q values are typical for air-dry fuel; real ones depend on the grade and moisture. The water is heated without boiling.')
s3 = section('fuel', 'Теплота сгорания топлива', 'Heat of combustion of fuel',
 bd('<p>При сгорании топлива его химическая энергия превращается в тепло. <strong>Удельная теплота сгорания</strong> <em>q</em> показывает, сколько энергии выделяется при полном сгорании 1 кг топлива:</p>',
    '<p>When fuel burns its chemical energy turns into heat. The <strong>specific heat of combustion</strong> <em>q</em> shows how much energy is released when 1 kg of fuel burns completely:</p>')
 + formula('Q = q · m', 'q в Дж/кг; на нагрев обычно идёт лишь часть: Q<sub>пол</sub> = η · q · m', 'q in J/kg; usually only part goes into heating: Q<sub>useful</sub> = η · q · m')
 + table(['ТОПЛИВО', 'q, МДЖ/КГ'], ['FUEL', 'q, MJ/kg'], [[('Метан (природный газ)', 'Methane (natural gas)'), '≈ 55'], [('Бензин', 'Petrol'), '≈ 46'], [('Уголь', 'Coal'), '≈ 27'], [('Сухие дрова', 'Dry wood'), '≈ 15']])
 + bd('<p>Для сравнения: 1 кВт·ч = 3,6 МДж. На открытом костре на нагрев воды идёт лишь небольшая доля тепла, а в хорошей печи или котле — гораздо больше.</p>',
      '<p>For comparison: 1 kWh = 3.6 MJ. On an open fire only a small share of the heat goes into heating water, while in a good stove or boiler much more does.</p>'),
 lab3)

tasks = [
 task(1, 'Чайник', 'A kettle', 'Сколько тепла нужно, чтобы нагреть 1,5 кг воды от 20 °C до 100 °C? За какое время это сделает нагреватель мощностью 2 кВт без потерь? c = 4186 Дж/(кг·К).', 'How much heat is needed to warm 1.5 kg of water from 20 °C to 100 °C? How long will a 2 kW heater take with no losses? c = 4186 J/(kg·K).',
  'm = 1,5 кг, Δt = 80 К, P = 2000 Вт', 'm = 1.5 kg, Δt = 80 K, P = 2,000 W', 'Q = c·m·Δt = 4186 · 1,5 · 80 = 502 320 Дж.<br>t = Q / P = 502 320 / 2000 ≈ 251 с.', 'Q = c·m·Δt = 4186 · 1.5 · 80 = 502,320 J.<br>t = Q / P = 502,320 / 2,000 ≈ 251 s.',
  'около 502 кДж и 251 с (≈ 4,2 мин).', 'about 502 kJ and 251 s (≈ 4.2 min).', True),
 task(2, 'Песок и вода', 'Sand and water', 'Каждому из тел — 2 кг песка (c = 830) и 2 кг воды (c = 4186 Дж/(кг·К)) — передали по 100 кДж. На сколько нагреется каждое?', 'Each of the two bodies — 2 kg of sand (c = 830) and 2 kg of water (c = 4186 J/(kg·K)) — was given 100 kJ. By how much does each warm up?',
  'Q = 100 000 Дж, m = 2 кг', 'Q = 100,000 J, m = 2 kg', 'Δt = Q / (c·m).<br>Песок: 100 000 / (830 · 2) ≈ 60 К.<br>Вода: 100 000 / (4186 · 2) ≈ 11,9 К.', 'Δt = Q / (c·m).<br>Sand: 100,000 / (830 · 2) ≈ 60 K.<br>Water: 100,000 / (4,186 · 2) ≈ 11.9 K.',
  'песок — на 60 К, вода — всего на 12 К. Песок нагревается в 5 раз сильнее.', 'sand by 60 K, water by only 12 K. The sand warms 5 times more.'),
 task(3, 'Стальная сковорода', 'A steel pan', 'Сколько тепла нужно, чтобы нагреть стальную сковороду массой 0,8 кг от 20 °C до 220 °C? c = 490 Дж/(кг·К).', 'How much heat is needed to warm a 0.8 kg steel pan from 20 °C to 220 °C? c = 490 J/(kg·K).',
  'm = 0,8 кг, Δt = 200 К', 'm = 0.8 kg, Δt = 200 K', 'Q = 490 · 0,8 · 200 = 78 400 Дж.', 'Q = 490 · 0.8 · 200 = 78,400 J.',
  '78,4 кДж. Это в 6,4 раза меньше, чем для такой же массы воды при том же нагреве.', '78.4 kJ. That is 6.4 times less than for the same mass of water with the same heating.'),
 task(4, 'Смешиваем воду', 'Mixing water', 'В 3 кг воды при 80 °C влили 6 кг воды при 20 °C. Какая температура установится?', '6 kg of water at 20 °C was poured into 3 kg of water at 80 °C. What temperature will result?',
  'm₁ = 3 кг, t₁ = 80 °C, m₂ = 6 кг, t₂ = 20 °C', 'm₁ = 3 kg, t₁ = 80 °C, m₂ = 6 kg, t₂ = 20 °C', 't = (m₁t₁ + m₂t₂) / (m₁ + m₂) = (3 · 80 + 6 · 20) / 9 = 360 / 9 = 40 °C.<br>Проверка: горячая отдала c·3·40, холодная получила c·6·20 — оба раза 120·c.', 't = (m₁t₁ + m₂t₂) / (m₁ + m₂) = (3 · 80 + 6 · 20) / 9 = 360 / 9 = 40 °C.<br>Check: the hot water gave c·3·40, the cold water received c·6·20 — both 120·c.',
  '40 °C. Итог ближе к температуре холодной воды, потому что её больше.', '40 °C. The result is closer to the cold water’s temperature because there is more of it.'),
 task(5, 'Уголь для печи', 'Coal for a stove', 'Сколько энергии выделится при полном сгорании 2 кг угля (q = 27 МДж/кг)? Выразите в киловатт-часах.', 'How much energy is released when 2 kg of coal (q = 27 MJ/kg) burn completely? Give it in kilowatt-hours.',
  'm = 2 кг, q = 27 МДж/кг', 'm = 2 kg, q = 27 MJ/kg', 'Q = q·m = 27 · 2 = 54 МДж.<br>В киловатт-часах: 54 / 3,6 = 15 кВт·ч.', 'Q = q·m = 27 · 2 = 54 MJ.<br>In kilowatt-hours: 54 / 3.6 = 15 kWh.',
  '54 МДж, то есть 15 кВт·ч.', '54 MJ, that is 15 kWh.'),
 task(6, 'Чай на костре', 'Tea on a campfire', 'На костре сожгли 1 кг сухих дров (q = 15 МДж/кг). На нагрев воды пошло 20 % тепла. Сколько воды можно нагреть от 15 °C до 100 °C?', 'On a campfire 1 kg of dry wood (q = 15 MJ/kg) was burnt. 20 % of the heat went into heating water. How much water can be heated from 15 °C to 100 °C?',
  'm = 1 кг, q = 15 МДж/кг, η = 0,2, Δt = 85 К', 'm = 1 kg, q = 15 MJ/kg, η = 0.2, Δt = 85 K', 'Полезное тепло: η·q·m = 0,2 · 15 000 000 = 3 000 000 Дж.<br>Масса воды: m = Q / (c·Δt) = 3 000 000 / (4186 · 85) ≈ 8,4 кг.', 'Useful heat: η·q·m = 0.2 · 15,000,000 = 3,000,000 J.<br>Mass of water: m = Q / (c·Δt) = 3,000,000 / (4,186 · 85) ≈ 8.4 kg.',
  'около 8,4 кг (≈ 8,4 л) воды.', 'about 8.4 kg (≈ 8.4 L) of water.'),
]

quiz = [
 ('В каких единицах измеряют удельную теплоёмкость?', [('Дж/(кг·К)', 'Верно: энергия на килограмм и на кельвин.'), ('Вт', 'Это единица мощности.'), ('Дж/кг', 'Это единица теплоты сгорания (удельной теплоты), но не теплоёмкости.')],
  'In which units is specific heat capacity measured?', [('J/(kg·K)', 'Correct: energy per kilogram per kelvin.'), ('W', 'That is a unit of power.'), ('J/kg', 'That is the unit of the heat of combustion (specific heat), not heat capacity.')], 0),
 ('Что означает c = 4186 Дж/(кг·К) для воды?', [('1 кг воды нагревается на 1 К, получив 4186 Дж', 'Верно.'), ('1 кг воды нагревается на 4186 К', 'Это чудовищная температура: такого нагрева нет.'), ('4186 кг воды нагревается на 1 К, получив 1 Дж', 'Условие перепутано: 4186 Дж на 1 кг и 1 К.')],
  'What does c = 4186 J/(kg·K) mean for water?', [('1 kg of water warms by 1 K when it receives 4186 J', 'Correct.'), ('1 kg of water warms by 4186 K', 'That would be an enormous temperature: there is no such heating.'), ('4186 kg of water warms by 1 K when it receives 1 J', 'The condition is muddled: 4186 J per 1 kg and 1 K.')], 0),
 ('Одинаковые массы песка и воды получили одинаковое тепло. Что нагреется сильнее?', [('Вода', 'У воды теплоёмкость больше — она нагреется меньше.'), ('Песок', 'Верно: у песка c ≈ 830, у воды ≈ 4186; песок нагреется примерно в 5 раз сильнее.'), ('Одинаково', 'Нагрев зависит от теплоёмкости вещества.')],
  'Equal masses of sand and water receive the same heat. Which warms more?', [('Water', 'Water has the larger heat capacity — it warms less.'), ('Sand', 'Correct: sand has c ≈ 830 and water ≈ 4186; sand warms about 5 times more.'), ('Equally', 'The warming depends on the substance’s heat capacity.')], 1),
 ('2 кг вещества с c = 1000 Дж/(кг·К) нагрели на 10 К. Сколько тепла потребовалось?', [('20 кДж', 'Верно: Q = 1000 · 2 · 10 = 20 000 Дж.'), ('200 Дж', 'Проверьте степень десяти: c = 1000, а не 10.'), ('5 кДж', 'Это 1000 / (2·10) · 100 — формула перепутана; нужно умножить c, m и Δt.')],
  '2 kg of a substance with c = 1000 J/(kg·K) were warmed by 10 K. How much heat was needed?', [('20 kJ', 'Correct: Q = 1000 · 2 · 10 = 20,000 J.'), ('200 J', 'Check the power of ten: c = 1000, not 10.'), ('5 kJ', 'The formula is muddled: multiply c, m and Δt.')], 0),
 ('Что выражает уравнение теплового баланса?', [('Тепло, отданное горячим телом, равно теплу, полученному холодным (без потерь)', 'Верно: энергия сохраняется.'), ('Температуры тел всегда равны', 'Они выравниваются лишь в конце.'), ('Масса горячего тела равна массе холодного', 'Массы могут быть любыми.')],
  'What does the heat balance equation express?', [('The heat given by the hot body equals the heat received by the cold one (no losses)', 'Correct: energy is conserved.'), ('The temperatures of the bodies are always equal', 'They only become equal at the end.'), ('The mass of the hot body equals the mass of the cold one', 'The masses can be anything.')], 0),
 ('Смешали 1 кг воды при 80 °C и 1 кг воды при 20 °C. Какая температура установится?', [('100 °C', 'Температуры не складываются.'), ('50 °C', 'Верно: массы равны, итог посередине.'), ('60 °C', 'Для итога 60 °C горячей воды должно быть больше.')],
  '1 kg of water at 80 °C and 1 kg of water at 20 °C were mixed. What temperature results?', [('100 °C', 'Temperatures do not add up.'), ('50 °C', 'Correct: the masses are equal, so the result is halfway.'), ('60 °C', 'For a result of 60 °C there would have to be more hot water.')], 1),
 ('У какого топлива из перечисленных самая большая теплота сгорания?', [('Сухие дрова (≈ 15 МДж/кг)', 'Это самое малое значение из перечисленных.'), ('Уголь (≈ 27 МДж/кг)', 'Больше, чем у дров, но меньше, чем у бензина.'), ('Бензин (≈ 46 МДж/кг)', 'Верно: у бензина самая большая теплота сгорания.')],
  'Which of these fuels has the greatest heat of combustion?', [('Dry wood (≈ 15 MJ/kg)', 'This is the smallest value of those listed.'), ('Coal (≈ 27 MJ/kg)', 'More than wood but less than petrol.'), ('Petrol (≈ 46 MJ/kg)', 'Correct: petrol has the greatest heat of combustion.')], 2),
 ('Почему вода в озере остывает осенью медленнее суши?', [('У воды большая удельная теплоёмкость', 'Верно: она отдаёт много тепла при небольшом остывании.'), ('Вода не излучает тепло', 'Вода излучает, как любое тело.'), ('Вода всегда тёплая', 'Это не так: теплоёмкость определяет скорость изменения температуры.')],
  'Why does lake water cool more slowly in autumn than the land?', [('Water has a large specific heat capacity', 'Correct: it gives away a lot of heat for a small drop in temperature.'), ('Water does not radiate heat', 'Water radiates like any body.'), ('Water is always warm', 'That is not so: heat capacity sets how fast the temperature changes.')], 0),
]

js = r'''
const T={ru:{
 hcLabel:"Полоски удельной теплоёмкости разных веществ",mxLabel:"Горячая и холодная вода, смешанная вода",fuLabel:"Доля тепла топлива, пошедшая на нагрев",
 subs:["Вода","Лёд","Песок","Сталь","Медь","Алюминий","Воздух (сухой)"],fuels:["Метан (природный газ)","Бензин","Уголь","Сухие дрова"],
 hcFb:"У воды теплоёмкость самая большая из списка, поэтому на её нагрев уходит больше всего тепла.",
 mxFb:"Тепло, отданное горячей водой, равно теплу, полученному холодной.",
 fuFb:"Чем выше КПД печи, тем больше воды нагреется. На открытом огне КПД небольшой.",
 useful:"полезно",lost:"потери",hot:"горячая",cold:"холодная",mix:"смесь"},
 en:{
 hcLabel:"Bars of the specific heat capacity of various substances",mxLabel:"Hot and cold water, mixed water",fuLabel:"The share of the fuel’s heat that goes into heating",
 subs:["Water","Ice","Sand","Steel","Copper","Aluminium","Air (dry)"],fuels:["Methane (natural gas)","Petrol","Coal","Dry wood"],
 hcFb:"Water has the largest heat capacity in the list, so heating it takes the most heat.",
 mxFb:"The heat given by the hot water equals the heat received by the cold water.",
 fuFb:"The higher the efficiency of the stove, the more water is heated. An open fire has a low efficiency.",
 useful:"useful",lost:"losses",hot:"hot",cold:"cold",mix:"mixture"}};
const CS=[4186,2090,830,490,385,900,1005],QF=[55,46,27,15],CW=4186;
function drawHc(){const t=tt(),i=+$("hs").value,m=+$("hm").value,dt=+$("hd").value;
 let g='';
 CS.forEach((c,j)=>{const y=14+j*36,w=c/4186*300,q=c*m*dt;
  g+='<rect x="130" y="'+y+'" width="'+w+'" height="24" fill="'+(j===i?"#b6533f":"#c9c2b0")+'" stroke="#18181a"/>'+svgText(124,y+16,t.subs[j],j===i?"#18181a":"#66666b","end",11)+svgText(136+w,y+16,fmt(q/1000,0)+t.kJ,"#18181a","start",11)});
 $("hcSvg").innerHTML=g;
 const Q=CS[i]*m*dt;$("hmOut").textContent=fmt(m,1)+t.kg;$("hdOut").textContent=dt+t.K;
 $("hQ").textContent=Q>=1e6?fmt(Q/1e6,2)+t.MJ:fmt(Q/1e3,1)+t.kJ;
 const sec=Q/1000;$("hT").textContent=sec>=120?fmt(sec/60,1)+t.min:fmt(sec,0)+t.s;$("hR").textContent=i===0?"1":"1 : "+fmt(CW/CS[i],1);
 $("hcFb").textContent=t.hcFb}
["hs","hm","hd"].forEach(id=>$(id).addEventListener("input",drawHc));
function drawMx(){const t=tt(),m1=+$("m1").value,t1=+$("t1").value,m2=+$("m2").value,t2=+$("t2").value,tf=(m1*t1+m2*t2)/(m1+m2),q1=CW*m1*(t1-tf),q2=CW*m2*(tf-t2);
 const col=v=>{const f=Math.max(0,Math.min(1,v/100));return "rgb("+Math.round(70+f*140)+","+Math.round(150-f*60)+","+Math.round(210-f*150)+")"};
 const bk=(x,m,v,lab)=>{const h=30+m/10*110;return '<path d="M'+x+' '+(230-150)+' L'+x+' 225 L'+(x+110)+' 225 L'+(x+110)+' '+(230-150)+'" fill="none" stroke="#18181a" stroke-width="3"/><rect x="'+(x+2)+'" y="'+(224-h)+'" width="106" height="'+h+'" fill="'+col(v)+'"/>'+svgText(x+55,244,lab,"#66666b","middle",11)+svgText(x+55,224-h-6,fmt(m,1)+t.kg+" · "+fmt(v,1)+t.C,"#18181a","middle",11)};
 let g=bk(30,m1,t1,t.hot)+bk(240,m2,t2,t.cold)+bk(450,m1+m2,tf,t.mix);
 g+=svgText(190,150,"+","#18181a","middle",28)+svgText(400,150,"=","#18181a","middle",28);
 $("mxSvg").innerHTML=g;
 $("m1Out").textContent=fmt(m1,1)+t.kg;$("t1Out").textContent=t1+t.C;$("m2Out").textContent=fmt(m2,1)+t.kg;$("t2Out").textContent=t2+t.C;
 $("xT").textContent=fmt(tf,1)+t.C;$("xQ1").textContent=fmt(q1/1000,1)+t.kJ;$("xQ2").textContent=fmt(q2/1000,1)+t.kJ;$("mxFb").textContent=t.mxFb}
["m1","t1","m2","t2"].forEach(id=>$(id).addEventListener("input",drawMx));
function drawFu(){const t=tt(),i=+$("fs").value,m=+$("fm").value,e=+$("fe").value/100,Q=QF[i]*1e6*m,Qu=Q*e,mw=Qu/(CW*85);
 const L=Math.min(480,Q/1e6/ (55*10)*480+30);
 let g=svgText(60,50,"Q = "+fmt(Q/1e6,1)+t.MJ,"#18181a","start",14);
 g+='<rect x="60" y="70" width="'+L*e+'" height="46" fill="#2f6f5d" stroke="#18181a"/><rect x="'+(60+L*e)+'" y="70" width="'+L*(1-e)+'" height="46" fill="#c9c2b0" stroke="#18181a"/>';
 g+=svgText(60,142,t.useful+": "+fmt(Qu/1e6,1)+t.MJ+" ("+Math.round(e*100)+" %)","#2f6f5d","start",12)+svgText(60,164,t.lost+": "+fmt((Q-Qu)/1e6,1)+t.MJ,"#66666b","start",12);
 g+=svgText(60,206,fmt(mw,1)+t.kg+" "+(lang==="ru"?"воды нагреется на 85 К":"of water warmed by 85 K"),"#3f5f8f","start",13);
 $("fuSvg").innerHTML=g;
 $("fmOut").textContent=fmt(m,1)+t.kg;$("feOut").textContent=Math.round(e*100)+" %";
 $("fQ").textContent=fmt(Q/1e6,1)+t.MJ;$("fK").textContent=fmt(Q/3.6e6,1)+(lang==="ru"?" кВт·ч":" kWh");$("fW").textContent=fmt(mw,1)+t.L;$("fuFb").textContent=t.fuFb}
["fs","fm","fe"].forEach(id=>$(id).addEventListener("input",drawFu));
const LAB={ru:{hcSvg:T.ru.hcLabel,mxSvg:T.ru.mxLabel,fuSvg:T.ru.fuLabel},en:{hcSvg:T.en.hcLabel,mxSvg:T.en.mxLabel,fuSvg:T.en.fuLabel}};
function drawAll(){fillSel("hs",T[lang].subs,0);fillSel("fs",T[lang].fuels,3);drawHc();drawMx();drawFu()}
'''

c = dict(n='10', slug='10-heat-capacity.html', block='II', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Количество теплоты и теплоёмкость', 'Amount of heat and heat capacity'),
 desc='Глава 10 Атласа физики: количество теплоты, удельная теплоёмкость, уравнение теплового баланса, теплота сгорания топлива.',
 lead=('Почему песок на берегу Иссык-Куля обжигает ноги, а вода рядом прохладна, сколько дров нужно, чтобы вскипятить воду, и как считать тепло. Количество теплоты, удельная теплоёмкость и теплота сгорания.',
       'Why the sand on the Issyk-Kul shore burns your feet while the water beside it is cool, how much firewood it takes to boil water and how to count heat. The amount of heat, specific heat capacity and the heat of combustion.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('heat', 'Теплоёмкость', 'Heat capacity'), ('balance', 'Тепловой баланс', 'Heat balance'), ('fuel', 'Топливо', 'Fuel'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Жарким летним днём на берегу Иссык-Куля песок раскаляется так, что по нему трудно идти босиком. Вода рядом остаётся прохладной, хотя на неё светит то же Солнце. А поздним вечером песок быстро остывает, тогда как вода ещё долго хранит тепло.</p><p>Почему вода и песок, получая от Солнца одинаковую энергию, ведут себя по-разному?</p>',
         '<p>On a hot summer day on the Issyk-Kul shore the sand gets so hot that it is hard to walk on barefoot. The water beside it stays cool even though the same Sun shines on it. Late in the evening the sand cools quickly while the water keeps its warmth for a long time.</p><p>Why do water and sand, receiving the same energy from the Sun, behave so differently?</p>'),
 hint=('Подсказку даст модель «Сколько тепла нужно для нагрева». Разгадка — в конце главы.', 'The “How much heat heating needs” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему песок горячее воды', 'The answer: why sand is hotter than water'),
 answer=('<p>У воды удельная теплоёмкость примерно 4186 Дж/(кг·К), а у песка около 830 — в 5 раз меньше (задача 2). Значит, при одной и той же энергии Солнца масса песка нагреется примерно в 5 раз сильнее, чем такая же масса воды. Вдобавок вода прозрачная и перемешивается, поэтому тепло уходит в глубину, а не копится в тонком слое, как в песке.</p><p>Тем же объясняется, почему вода остывает медленно. Озеро запасает много тепла за тёплое время года. Для большого озера вроде Иссык-Куля глубиной до 668 м это особенно заметно: летом оно накапливает огромное количество тепла, и поэтому в обычные зимы остаётся незамёрзшим. Побережья больших водоёмов поэтому и мягче по климату.</p>',
         '<p>Water’s specific heat capacity is about 4186 J/(kg·K) and sand’s about 830 — 5 times less (problem 2). So for the same solar energy a mass of sand warms about 5 times more than the same mass of water. In addition water is transparent and mixes, so heat goes into the depth instead of piling up in a thin layer as in sand.</p><p>The same explains why water cools slowly. A lake stores a lot of heat during the warm season. For a large lake like Issyk-Kul, up to 668 m deep, this is especially noticeable: in summer it accumulates a huge amount of heat, and so in ordinary winters it stays unfrozen. That is why the shores of large bodies of water have milder climates.</p>'),
 sources=[
  ('Удельные теплоёмкости веществ (вода, лёд, песок, сталь, медь, алюминий, воздух) —', 'Specific heat capacities (water, ice, sand, steel, copper, aluminium, air) —', LINK('https://engineeringtoolbox.com/specific-heat-capacity-d_391.html', 'Engineering ToolBox: Specific heat of common materials') + ', ' + LINK('https://engineeringtoolbox.com/water-thermal-properties--d_162.html', 'Engineering ToolBox: Water thermal properties')),
  ('Теплота сгорания топлива —', 'Heats of combustion of fuels —', LINK('https://eng.libretexts.org/Sandboxes/jhalpern/Energy_Alternatives/03%3A_Fossil_Fuels_and_Thermal_Engines/3.02%3A_How_much_energy_there_is_in_fossil_fuels', 'LibreTexts: How much energy there is in fossil fuels') + ', ' + LINK('https://www.fao.org/4/T0269E/t0269e0c.htm', 'FAO: Comparison of energy values') + ', ' + LINK('https://w.astro.berkeley.edu/~wright/fuel_energy.html', 'Berkeley: Useful conversion factors (1 кВт·ч = 3,6 МДж)')),
  ('Иссык-Куль: наибольшая глубина 668 м, накопление тепла летом, обычно не замерзает —', 'Issyk-Kul: maximum depth 668 m, heat accumulation in summer, usually does not freeze —', LINK('https://wldb.ilec.or.jp/Display/html/3572', 'ILEC World Lake Database: Lake Issyk-Kool') + ', ' + LINK('https://en.wikipedia.org/wiki/Issyk-Kul', 'Wikipedia: Issyk-Kul')),
  ('Уравнение теплового баланса, Q = c·m·Δt —', 'The heat balance equation, Q = c·m·Δt —', LINK('https://physics.info/heat-sensible/', 'The Physics Hypertextbook: Sensible heat'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Значения c и q — типичные, из таблиц; КПД нагрева в задачах и модели — условный.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The c and q values are typical, from tables; the heating efficiency in problems and the model is assumed.'),
 prev=('09-heat-transfer.html', 'Глава 09 · Теплопередача', 'Chapter 09 · Heat transfer'),
 next=('11-phase-changes.html', 'Глава 11 · Плавление и кипение', 'Chapter 11 · Melting and boiling'),
 js=js)
build(c)
