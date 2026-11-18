# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ТЕМПЕРАТУРА И ВЫСОТА', 'TEMPERATURE AND ALTITUDE', 'laSvg', '0 0 600 290',
  slider('lh', 'Высота', 'Altitude', 0, 5000, 50, 1607) + slider('lt', 'Температура на уровне моря', 'Temperature at sea level', -10, 40, 1, 15),
  stats([('lT', 'Температура на высоте', 'Temperature at altitude'), ('lD', 'Холоднее, чем внизу', 'Colder than below')]),
  'laFb', 'Схема условная: в среднем воздух остывает на 6,5 К на каждый километр подъёма (стандартная атмосфера); в реальный день разница другая.',
  'A schematic drawing: on average the air cools by 6.5 K for every kilometre of ascent (standard atmosphere); on a real day the difference varies.')
s1 = section('altitude', 'Почему в горах холоднее', 'Why it is colder in the mountains',
 bd('<p>С высотой атмосферное давление падает (глава 4). Поднимающийся воздух расширяется, а расширяясь, он совершает работу и охлаждается (первый закон термодинамики, глава 12). В среднем температура воздуха снижается примерно на 6,5 К на каждый километр подъёма:</p>',
    '<p>With altitude the atmospheric pressure falls (chapter 4). Rising air expands, and as it expands it does work and cools (the first law of thermodynamics, chapter 12). On average the air temperature falls by about 6.5 K for every kilometre of ascent:</p>')
 + formula('t(h) ≈ t₀ − 6,5 · h', 'h в километрах; значение 6,5 К/км — среднее для стандартной атмосферы', 'h in kilometres; 6.5 K/km is the mean for the standard atmosphere')
 + bd('<p>Так, если на уровне моря +15 °C, то на перевале Төө-Ашуу (3586 м) по этой модели около −8 °C. Поэтому на вершинах Тянь-Шаня лежат ледники и снег, даже когда в долинах лето.</p>',
      '<p>So if it is +15 °C at sea level, the Töö-Ashuu pass (3,586 m) is, by this model, about −8 °C. That is why glaciers and snow lie on the Tien Shan peaks even when it is summer in the valleys.</p>'),
 lab1)

lab2 = model(2, 'ВЕТЕР С ОЗЕРА', 'WIND FROM THE LAKE', 'brSvg', '0 0 600 270',
  select('bt', 'Время суток', 'Time of day') + slider('be', 'Энергия Солнца за период', 'Solar energy over the period', 100, 1000, 50, 500),
  stats([('bL', 'Нагрев суши', 'Land warms by'), ('bW', 'Нагрев воды', 'Water warms by'), ('bV', 'Ветер дует', 'Wind blows')]),
  'brFb', 'Схема условная: считаем слои одинаковой массы на 1 м² — 100 кг песка (c = 830) и 100 кг воды (c = 4186 Дж/(кг·К)); энергия — в кДж на слой. Значения — учебные.',
  'A schematic drawing: assume layers of equal mass per m² — 100 kg of sand (c = 830) and 100 kg of water (c = 4,186 J/(kg·K)); the energy is in kJ per layer. The values are illustrative.')
s2 = section('breeze', 'Бриз и теплоёмкость', 'Breeze and heat capacity',
 bd('<p>Днём Солнце греет сушу сильнее, чем воду (глава 10): у песка теплоёмкость меньше. Тёплый воздух над сушей поднимается, а на его место приходит прохладный воздух с воды — это дневной <strong>бриз</strong> с озера на берег. Ночью суша остывает быстрее, и ветер меняет направление.</p>',
    '<p>In the day the Sun warms land more than water (chapter 10): sand has a smaller heat capacity. Warm air above the land rises and cool air from the water comes in its place — this is the daytime <strong>breeze</strong> from the lake to the shore. At night the land cools faster, and the wind changes direction.</p>')
 + bd('<p>Такие ветры хорошо знакомы на берегу Иссык-Куля. Они работают за счёт конвекции (глава 9): холодный воздух тяжелее, тёплый — легче.</p>',
      '<p>Such winds are familiar on the Issyk-Kul shore. They work through convection (chapter 9): cold air is heavier, warm air is lighter.</p>'),
 lab2)

lab3 = model(3, 'ПАРНИКОВЫЙ ЭФФЕКТ', 'THE GREENHOUSE EFFECT', 'ghSvg', '0 0 600 270',
  slider('ga', 'Отражает Солнце (альбедо)', 'Reflects sunlight (albedo)', 0, 0.8, 0.05, 0.3) + slider('gg', 'Добавка от парниковых газов', 'Warming from greenhouse gases', 0, 50, 1, 33),
  stats([('gE', 'Температура без атмосферы', 'Temperature without atmosphere'), ('gT', 'Средняя температура с газами', 'Mean temperature with gases')]),
  'ghFb', 'Схема условная: эффективная температура T = [S(1−a)/(4σ)]^¼, S = 1361 Вт/м². Добавка парниковых газов в среднем ≈ 33 К.',
  'A schematic drawing: the effective temperature is T = [S(1−a)/(4σ)]^¼, S = 1,361 W/m². The greenhouse contribution is on average ≈ 33 K.')
s3 = section('climate', 'Баланс энергии Земли и парниковый эффект', 'Earth’s energy balance and the greenhouse effect',
 bd('<p>Земля получает от Солнца энергию и излучает такую же в космос (глава 9). Если бы атмосферы не было, из баланса следовало бы, что средняя температура поверхности около −18 °C. На самом деле она около +15 °C. Разницу создают <strong>парниковые газы</strong> (водяной пар, углекислый газ, метан): они пропускают солнечный свет, но задерживают часть теплового излучения поверхности.</p>',
    '<p>The Earth receives energy from the Sun and radiates the same into space (chapter 9). With no atmosphere the balance would give a mean surface temperature of about −18 °C. In reality it is about +15 °C. The difference is made by <strong>greenhouse gases</strong> (water vapour, carbon dioxide, methane): they let sunlight through but hold back part of the surface’s thermal radiation.</p>')
 + formula('T = [ S (1 − a) / (4σ) ]^(1/4)', 'S ≈ 1361 Вт/м² — поток солнечной энергии; a ≈ 0,3 — доля отражённого света (альбедо); σ = 5,67·10⁻⁸ Вт/(м²·К⁴)', 'S ≈ 1,361 W/m² — solar flux; a ≈ 0.3 — the share of reflected light (albedo); σ = 5.67·10⁻⁸ W/(m²·K⁴)')
 + bd('<p>Парниковый эффект — естественное и нужное явление: без него Земля была бы покрыта льдом. Но рост содержания углекислого газа от сжигания топлива усиливает его, поэтому климат теплеет. Ледники Кыргызстана, например, за последние десятилетия сокращаются.</p>',
      '<p>The greenhouse effect is a natural and necessary phenomenon: without it the Earth would be covered with ice. But the growth of carbon dioxide from burning fuel strengthens it, which is why the climate is warming. Kyrgyzstan’s glaciers, for example, have been shrinking in recent decades.</p>'),
 lab3)

tasks = [
 task(1, 'Температура на перевале', 'Temperature at a pass', 'В долине на высоте 1000 м температура +20 °C. Какова она на перевале на высоте 3500 м, если воздух остывает на 6,5 К на километр?', 'In a valley at 1,000 m the temperature is +20 °C. What is it at a pass at 3,500 m if the air cools by 6.5 K per kilometre?',
  'Δh = 2,5 км, градиент 6,5 К/км', 'Δh = 2.5 km, gradient 6.5 K/km', 'Падение: 6,5 · 2,5 = 16,25 К.<br>t = 20 − 16,25 = 3,75 °C.', 'Drop: 6.5 · 2.5 = 16.25 K.<br>t = 20 − 16.25 = 3.75 °C.',
  'около +3,8 °C.', 'about +3.8 °C.', True),
 task(2, 'Где снег?', 'Where is the snow?', 'На уровне моря +15 °C. На какой высоте температура по модели опустится до 0 °C?', 'At sea level it is +15 °C. At what altitude does the model temperature fall to 0 °C?',
  't₀ = 15 °C, градиент 6,5 К/км', 't₀ = 15 °C, gradient 6.5 K/km', 'h = (t₀ − 0) / 6,5 = 15 / 6,5 ≈ 2,31 км.', 'h = (t₀ − 0) / 6.5 = 15 / 6.5 ≈ 2.31 km.',
  'примерно 2300 м. Выше — ниже нуля.', 'about 2,300 m. Above that it is below zero.'),
 task(3, 'Песок и вода на берегу', 'Sand and water on a shore', 'Слой песка (100 кг, c = 830 Дж/(кг·К)) и слой воды (100 кг, c = 4186) получили по 500 кДж. На сколько нагреется каждый?', 'A sand layer (100 kg, c = 830 J/(kg·K)) and a water layer (100 kg, c = 4,186) each received 500 kJ. By how much does each warm?',
  'm = 100 кг, Q = 500 000 Дж', 'm = 100 kg, Q = 500,000 J', 'Δt = Q / (c·m).<br>Песок: 500 000 / (830 · 100) ≈ 6,0 К.<br>Вода: 500 000 / (4186 · 100) ≈ 1,2 К.', 'Δt = Q / (c·m).<br>Sand: 500,000 / (830 · 100) ≈ 6.0 K.<br>Water: 500,000 / (4,186 · 100) ≈ 1.2 K.',
  'песок — на 6 К, вода — на 1,2 К. Поэтому днём суша теплее, и возникает бриз с воды.', 'sand by 6 K, water by 1.2 K. So in the day the land is warmer, and a breeze from the water arises.'),
 task(4, 'Земля без атмосферы', 'Earth without an atmosphere', 'Найдите эффективную температуру Земли без парниковых газов: S = 1361 Вт/м², a = 0,3, σ = 5,67·10⁻⁸ Вт/(м²·К⁴).', 'Find the Earth’s effective temperature without greenhouse gases: S = 1,361 W/m², a = 0.3, σ = 5.67·10⁻⁸ W/(m²·K⁴).',
  'S = 1361, a = 0,3', 'S = 1,361, a = 0.3', 'S(1 − a)/4 = 1361 · 0,7 / 4 ≈ 238,2 Вт/м².<br>T⁴ = 238,2 / 5,67·10⁻⁸ ≈ 4,2·10⁹ К⁴.<br>T ≈ 254,6 К ≈ −18,6 °C.', 'S(1 − a)/4 = 1,361 · 0.7 / 4 ≈ 238.2 W/m².<br>T⁴ = 238.2 / 5.67·10⁻⁸ ≈ 4.2·10⁹ K⁴.<br>T ≈ 254.6 K ≈ −18.6 °C.',
  'около −18 °C. Фактическая средняя температура +15 °C — на 33 К выше за счёт парникового эффекта.', 'about −18 °C. The actual mean temperature of +15 °C is 33 K higher thanks to the greenhouse effect.'),
 task(4+1, 'Белая Земля', 'A white Earth', 'Как изменится эффективная температура, если альбедо вырастет с 0,3 до 0,6 (например, из-за льда)?', 'How does the effective temperature change if the albedo rises from 0.3 to 0.6 (for example because of ice)?',
  'a = 0,6', 'a = 0.6', 'S(1 − a)/4 = 1361 · 0,4 / 4 = 136,1 Вт/м².<br>T⁴ = 136,1 / 5,67·10⁻⁸ ≈ 2,4·10⁹.<br>T ≈ 221,4 К ≈ −51,8 °C.', 'S(1 − a)/4 = 1,361 · 0.4 / 4 = 136.1 W/m².<br>T⁴ = 136.1 / 5.67·10⁻⁸ ≈ 2.4·10⁹.<br>T ≈ 221.4 K ≈ −51.8 °C.',
  'температура упадёт примерно на 33 К — до −52 °C. Чем больше отражающей поверхности, тем холоднее.', 'the temperature falls by about 33 K — to −52 °C. The more reflecting surface, the colder.'),
 task(6, 'Вершина', 'A summit', 'Ледник лежит на высоте 4500 м. Какая там температура, если на 1500 м она +14 °C? Градиент 6,5 К/км.', 'A glacier lies at 4,500 m. What is the temperature there if at 1,500 m it is +14 °C? Gradient 6.5 K/km.',
  'Δh = 3 км', 'Δh = 3 km', 'Падение: 6,5 · 3 = 19,5 К.<br>t = 14 − 19,5 = −5,5 °C.', 'Drop: 6.5 · 3 = 19.5 K.<br>t = 14 − 19.5 = −5.5 °C.',
  '−5,5 °C: ниже нуля, лёд не тает.', '−5.5 °C: below zero, so the ice does not melt.'),
]

quiz = [
 ('На сколько в среднем остывает воздух при подъёме на 1 км?', [('На 6,5 К', 'Верно: средний градиент стандартной атмосферы.'), ('На 65 К', 'Это слишком много.'), ('Не остывает', 'С высотой температура снижается.')],
  'By how much does air cool on average when rising 1 km?', [('By 6.5 K', 'Correct: the mean gradient of the standard atmosphere.'), ('By 65 K', 'That is far too much.'), ('It does not cool', 'The temperature falls with altitude.')], 0),
 ('Почему поднимающийся воздух остывает?', [('Он расширяется и совершает работу', 'Верно: давление падает, воздух расширяется и охлаждается.'), ('Он сжимается', 'С высотой давление падает, воздух расширяется.'), ('Солнце его не греет', 'Воздух греется в основном снизу.')],
  'Why does rising air cool?', [('It expands and does work', 'Correct: pressure falls, so the air expands and cools.'), ('It is compressed', 'With altitude the pressure falls, the air expands.'), ('The Sun does not warm it', 'Air is mostly warmed from below.')], 0),
 ('Днём на берегу озера ветер обычно дует…', [('с озера на берег', 'Верно: над сушей воздух теплее и поднимается.'), ('с берега на озеро', 'Так бывает ночью, когда суша холоднее воды.'), ('вдоль берега всегда', 'Направление зависит от разницы температур.')],
  'In the day on a lake shore the wind usually blows…', [('from the lake to the shore', 'Correct: over land the air is warmer and rises.'), ('from the shore to the lake', 'That happens at night when the land is colder than the water.'), ('always along the shore', 'The direction depends on the temperature difference.')], 0),
 ('Почему суша днём нагревается сильнее воды?', [('У воды меньше масса', 'Дело в теплоёмкости, а не в массе.'), ('У суши удельная теплоёмкость меньше', 'Верно: у песка c ≈ 830, у воды ≈ 4186.'), ('Вода не получает энергии', 'Получает, но нагревается слабее.')],
  'Why does land warm more than water in the day?', [('Water has less mass', 'It is a matter of heat capacity, not of mass.'), ('Land has a smaller specific heat capacity', 'Correct: sand has c ≈ 830, water ≈ 4,186.'), ('Water receives no energy', 'It does, but warms less.')], 1),
 ('Какова средняя температура Земли без парниковых газов по простой модели?', [('Около −18 °C', 'Верно: 254 К.'), ('Около +15 °C', 'Это фактическая температура с парниковым эффектом.'), ('Около +100 °C', 'Намного выше реальной.')],
  'What is the Earth’s mean temperature without greenhouse gases in the simple model?', [('About −18 °C', 'Correct: 254 K.'), ('About +15 °C', 'That is the actual temperature with the greenhouse effect.'), ('About +100 °C', 'Far above the real value.')], 0),
 ('Что делают парниковые газы?', [('Пропускают солнечный свет и задерживают тепловое излучение поверхности', 'Верно.'), ('Блокируют весь солнечный свет', 'Свет они пропускают.'), ('Охлаждают Землю', 'Они, наоборот, повышают температуру поверхности.')],
  'What do greenhouse gases do?', [('Let sunlight through and hold back the surface’s thermal radiation', 'Correct.'), ('Block all sunlight', 'They let light through.'), ('Cool the Earth', 'On the contrary, they raise the surface temperature.')], 0),
 ('Что произойдёт с эффективной температурой, если альбедо вырастет?', [('Она вырастет', 'Больше света отражается, поглощается меньше.'), ('Она упадёт', 'Верно: поглощается меньше энергии.'), ('Не изменится', 'Альбедо входит в формулу.')],
  'What happens to the effective temperature if the albedo grows?', [('It rises', 'More light is reflected, less is absorbed.'), ('It falls', 'Correct: less energy is absorbed.'), ('It stays the same', 'Albedo enters the formula.')], 1),
 ('На уровне моря +15 °C. Какой примерно будет температура на высоте 2 км по модели?', [('+2 °C', 'Верно: 15 − 6,5 · 2 = 2 °C.'), ('+8,5 °C', 'Это подъём всего на 1 км.'), ('−15 °C', 'Это слишком сильное остывание.')],
  'At sea level it is +15 °C. About what temperature does the model give at 2 km?', [('+2 °C', 'Correct: 15 − 6.5 · 2 = 2 °C.'), ('+8.5 °C', 'That is a rise of only 1 km.'), ('−15 °C', 'That is too much cooling.')], 0),
]

js = r'''
const T={ru:{
 laLabel:"Склон горы и температура воздуха на высоте",brLabel:"Озеро и берег: направление ветра",ghLabel:"Шкала температур Земли без атмосферы и с парниковыми газами",
 day:"день",night:"ночь",days:["День","Ночь"],
 wLake:"с озера на берег",wShore:"с берега на озеро",lake:"озеро",shore:"суша",
 laFb:"Чем выше, тем холоднее: примерно на 6,5 К на каждый километр.",
 brFb:["Суша нагрелась сильнее: тёплый воздух над ней поднимается, с озера приходит прохладный.","Суша остыла сильнее: холодный воздух стекает с берега на тёплую воду."],
 ghFb:"Без атмосферы было бы очень холодно; парниковые газы добавляют около 33 К.",
 noA:"без атмосферы",withG:"с газами"},
 en:{
 laLabel:"A mountain slope and the air temperature at altitude",brLabel:"Lake and shore: wind direction",ghLabel:"A temperature scale of Earth without atmosphere and with greenhouse gases",
 day:"day",night:"night",days:["Day","Night"],
 wLake:"from the lake to the shore",wShore:"from the shore to the lake",lake:"lake",shore:"land",
 laFb:"The higher, the colder: about 6.5 K for every kilometre.",
 brFb:["The land warmed more: warm air above it rises and cool air comes from the lake.","The land cooled more: cold air flows from the shore over the warmer water."],
 ghFb:"Without an atmosphere it would be very cold; greenhouse gases add about 33 K.",
 noA:"no atmosphere",withG:"with gases"}};
function drawLa(){const t=tt(),h=+$("lh").value,t0=+$("lt").value,th=t0-6.5*h/1000;
 const X=x=>40+x,Y=hh=>250-hh/5000*200;
 let g='<polygon points="40,250 300,60 560,250" fill="#e3e1da" stroke="#18181a"/><polygon points="240,110 300,60 360,110 330,100 300,115 270,100" fill="#fff" stroke="#c9c2b0"/>';
 const px=40+(h/5000)*260;
 g+='<line x1="40" y1="'+Y(h)+'" x2="560" y2="'+Y(h)+'" stroke="#b6533f" stroke-dasharray="4 3"/><circle cx="'+px+'" cy="'+Y(h)+'" r="6" fill="#b6533f"/>';
 g+=svgText(52,Y(h)-6,num(h)+(lang==="ru"?" м":" m")+" · "+fmt(th,1)+" °C","#b6533f","start",13);
 g+=svgText(52,270,"0 m · "+fmt(t0,0)+" °C","#18181a","start",12);
 $("laSvg").innerHTML=g;
 $("lhOut").textContent=num(h)+(lang==="ru"?" м":" m");$("ltOut").textContent=t0+" °C";
 $("lT").textContent=fmt(th,1)+" °C";$("lD").textContent=fmt(t0-th,1)+(lang==="ru"?" К":" K");$("laFb").textContent=t.laFb}
["lh","lt"].forEach(id=>$(id).addEventListener("input",drawLa));
function drawBr(){const t=tt(),i=+$("bt").value,E=+$("be").value*1000,dl=E/(830*100),dw=E/(4186*100);
 const day=i===0,landCol=day?"#d9a35b":"#7d8fb0";
 let g='<rect x="0" y="150" width="300" height="100" fill="#3f78a8" fill-opacity="0.7"/><rect x="300" y="150" width="300" height="100" fill="'+landCol+'" fill-opacity="0.8"/>';
 g+=svgText(150,200,t.lake+" "+(day?"+":"−")+fmt(dw,1)+" K","#ffffff","middle",13)+svgText(450,200,t.shore+" "+(day?"+":"−")+fmt(dl,1)+" K","#18181a","middle",13);
 if(day){g+='<path d="M130 120 L420 120" stroke="#2f6f5d" stroke-width="3" marker-end="url(#ar)"/><path d="M450 140 L450 40" stroke="#b6533f" stroke-width="3" stroke-dasharray="5 3"/>'}
 else{g+='<path d="M470 120 L180 120" stroke="#2f6f5d" stroke-width="3" marker-end="url(#ar)"/><path d="M150 140 L150 40" stroke="#b6533f" stroke-width="3" stroke-dasharray="5 3"/>'}
 g+='<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#2f6f5d"/></marker></defs>';
 $("brSvg").innerHTML=g;
 $("beOut").textContent=num(E/1000)+(lang==="ru"?" кДж":" kJ");
 $("bL").textContent=(day?"+":"−")+fmt(dl,1)+(lang==="ru"?" К":" K");$("bW").textContent=(day?"+":"−")+fmt(dw,1)+(lang==="ru"?" К":" K");
 $("bV").textContent=day?t.wLake:t.wShore;$("brFb").textContent=t.brFb[i]}
["bt","be"].forEach(id=>$(id).addEventListener("input",drawBr));
function drawGh(){const t=tt(),a=+$("ga").value,gg=+$("gg").value,Te=Math.pow(1361*(1-a)/(4*5.670374e-8),0.25)-273.15,Tm=Te+gg;
 const X=v=>60+(v+60)/110*480;
 let g='<line x1="60" y1="110" x2="540" y2="110" stroke="#18181a"/>';
 for(let v=-60;v<=50;v+=10)g+='<line x1="'+X(v)+'" y1="106" x2="'+X(v)+'" y2="114" stroke="#18181a"/>'+svgText(X(v),130,v,"#66666b","middle",10);
 g+='<line x1="'+X(0)+'" y1="60" x2="'+X(0)+'" y2="110" stroke="#8eb8d1" stroke-dasharray="3 3"/>'+svgText(X(0),54,"0 °C","#3f78a8","middle",11);
 g+='<circle cx="'+X(Te)+'" cy="110" r="8" fill="#3f5f8f"/>'+svgText(X(Te),90,t.noA+" "+fmt(Te,1)+" °C","#3f5f8f","middle",12);
 g+='<circle cx="'+X(Tm)+'" cy="110" r="8" fill="#b6533f"/>'+svgText(X(Tm),160,t.withG+" "+fmt(Tm,1)+" °C","#b6533f","middle",12);
 $("ghSvg").innerHTML=g;
 $("gaOut").textContent=fmt(a,2);$("ggOut").textContent=gg+(lang==="ru"?" К":" K");
 $("gE").textContent=fmt(Te,1)+" °C";$("gT").textContent=fmt(Tm,1)+" °C";$("ghFb").textContent=t.ghFb}
["ga","gg"].forEach(id=>$(id).addEventListener("input",drawGh));
const LAB={ru:{laSvg:T.ru.laLabel,brSvg:T.ru.brLabel,ghSvg:T.ru.ghLabel},en:{laSvg:T.en.laLabel,brSvg:T.en.brLabel,ghSvg:T.en.ghLabel}};
function drawAll(){fillSel("bt",T[lang].days,0);drawLa();drawBr();drawGh()}
'''

c = dict(n='13', slug='13-weather-climate.html', block='II', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Погода и климат', 'Weather and climate'),
 desc='Глава 13 Атласа физики: температура и высота, бриз, энергетический баланс Земли и парниковый эффект.',
 lead=('Почему на Ала-Тоо лежит снег, когда в долине лето, откуда берётся ветер на берегу Иссык-Куля и почему Земля тёплая. Тепловые явления в атмосфере.',
       'Why snow lies on the Ala-Too when it is summer in the valley, where the wind on the Issyk-Kul shore comes from and why the Earth is warm. Thermal phenomena in the atmosphere.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('altitude', 'Высота и холод', 'Altitude and cold'), ('breeze', 'Бриз', 'Breeze'), ('climate', 'Парниковый эффект', 'Greenhouse effect'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Летом в Бишкеке жарко, а от города хорошо видны белые вершины Кыргызского Ала-Тоо. До них по прямой не так далеко, солнце светит и на долину, и на вершины — даже ближе к вершинам. Но снег там не тает.</p><p>Почему выше, то есть ближе к Солнцу, холоднее?</p>',
         '<p>In summer it is hot in Bishkek, yet white peaks of the Kyrgyz Ala-Too are clearly visible from the city. They are not far in a straight line, and the Sun shines on both valley and peaks — even closer to the peaks. But the snow there does not melt.</p><p>Why is it colder higher up, that is, closer to the Sun?</p>'),
 hint=('Подсказку даст модель «Температура и высота». Разгадка — в конце главы.', 'The “Temperature and altitude” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему на вершинах холоднее', 'The answer: why peaks are colder'),
 answer=('<p>Расстояние до Солнца здесь ничего не значит: несколько километров высоты по сравнению со 150 млн км до Солнца пренебрежимо малы. Воздух греется в основном от нагретой земли, а не напрямую от лучей. С высотой давление падает, воздух расширяется и охлаждается, примерно на 6,5 К на километр. Поэтому разница в 3 км высоты между долиной и вершиной — это примерно 20 К.</p><p>Так что вершины с вечным снегом — не парадокс, а следствие законов теплоты: расширение газа, совершение работы, охлаждение.</p>',
         '<p>The distance to the Sun means nothing here: a few kilometres of height compared with 150 million km to the Sun are negligible. Air is warmed mostly by the heated ground, not directly by the rays. With altitude the pressure falls, the air expands and cools, by about 6.5 K per kilometre. So a 3 km height difference between valley and peak amounts to about 20 K.</p><p>So peaks with permanent snow are not a paradox but a consequence of the laws of heat: expansion of a gas, doing work, cooling.</p>'),
 sources=[
  ('Градиент температуры в стандартной атмосфере (6,5 К/км) —', 'The temperature gradient in the standard atmosphere (6.5 K/km) —', LINK('https://aty.sdsu.edu/explain/thermal/std_atm.html', 'The Standard Atmosphere') + ', ' + LINK('https://en.wikipedia.org/wiki/Lapse_rate', 'Wikipedia: Lapse rate')),
  ('Эффективная температура Земли (около 255 К), парниковый эффект (≈ 33 К), S ≈ 1361 Вт/м² —', 'The Earth’s effective temperature (about 255 K), the greenhouse effect (≈ 33 K), S ≈ 1,361 W/m² —', LINK('https://science.nasa.gov/climate-change/causes/', 'NASA: Causes of climate change') + ', ' + LINK('https://en.wikipedia.org/wiki/Effective_temperature', 'Wikipedia: Effective temperature') + ', ' + LINK('https://en.wikipedia.org/wiki/Solar_constant', 'Wikipedia: Solar constant')),
  ('Бриз —', 'Sea and land breezes —', LINK('https://en.wikipedia.org/wiki/Sea_breeze', 'Wikipedia: Sea breeze')),
  ('Теплоёмкости песка и воды —', 'Heat capacities of sand and water —', LINK('https://engineeringtoolbox.com/specific-heat-capacity-d_391.html', 'Engineering ToolBox: Specific heat'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Масса слоёв в модели бриза — условная.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The layer masses in the breeze model are assumed.'),
 prev=('12-heat-engines.html', 'Глава 12 · Тепловые двигатели', 'Chapter 12 · Heat engines'),
 next=('14-electric-charge.html', 'Глава 14 · Электрический заряд', 'Chapter 14 · Electric charge'),
 js=js)
build(c)
