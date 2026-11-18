# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ТЕПЛОПРОВОДНОСТЬ СТЕНКИ', 'CONDUCTION THROUGH A WALL', 'conSvg', '0 0 600 250',
  select('cm', 'Материал стенки', 'Wall material') + slider('cd', 'Толщина', 'Thickness', 5, 200, 5, 50) + slider('ct', 'Разность температур', 'Temperature difference', 5, 50, 1, 30),
  stats([('cP', 'Тепловой поток', 'Heat flow'), ('cE', 'Энергия за час', 'Energy per hour'), ('cR', 'Против меди', 'Against copper')]),
  'conFb', 'Схема условная: площадь стенки 1 м². Значения k — типичные, для расчёта; у дерева и бетона они зависят от породы и состава.',
  'A schematic drawing: the wall area is 1 m². The k values are typical ones for calculation; for wood and concrete they depend on the kind and composition.')
s1 = section('conduction', 'Теплопроводность', 'Conduction',
 bd('<p>Тепло может передаваться тремя способами. Первый — <strong>теплопроводность</strong>: энергия переходит от более нагретых частиц к менее нагретым при их столкновениях, а само вещество при этом не перемещается. Так нагревается ручка ложки в горячем чае.</p><p>Тепловой поток через плоскую стенку зависит от материала, площади, толщины и разности температур:</p>',
    '<p>Heat can be transferred in three ways. The first is <strong>conduction</strong>: energy passes from hotter particles to cooler ones in collisions, while the substance itself does not move. That is how the handle of a spoon warms up in hot tea.</p><p>The heat flow through a flat wall depends on the material, the area, the thickness and the temperature difference:</p>')
 + formula('P = k · S · Δt / d', 'P — тепловой поток (Вт), k — теплопроводность (Вт/(м·К)), S — площадь, d — толщина, Δt — разность температур', 'P is the heat flow (W), k the thermal conductivity (W/(m·K)), S the area, d the thickness, Δt the temperature difference')
 + bd('<p>Металлы проводят тепло очень хорошо: для меди k ≈ 401 Вт/(м·К), для алюминия ≈ 237. Стекло — гораздо хуже (≈ 1,1), дерево — ещё хуже, воздух — очень плохо (≈ 0,025). Материалы с воздухом в порах — войлок, вата, пенопласт, мех — плохо проводят тепло. Ими утепляют жильё и одежду (юрты, например, покрывают войлоком).</p>',
      '<p>Metals conduct heat very well: for copper k ≈ 401 W/(m·K), for aluminium ≈ 237. Glass is much worse (≈ 1.1), wood worse still, and air very poor (≈ 0.025). Materials with air in their pores — felt, wool, foam, fur — conduct heat badly. They are used to insulate homes and clothes (yurts, for example, are covered with felt).</p>')
 + table(['МАТЕРИАЛ', 'k, ВТ/(М·К)'], ['MATERIAL', 'k, W/(m·K)'], [[('Медь', 'Copper'), '401'], [('Алюминий', 'Aluminium'), '237'], [('Железо', 'Iron'), '≈ 80'], [('Бетон', 'Concrete'), '≈ 1,7'], [('Стекло', 'Glass'), '≈ 1,1'], [('Вода', 'Water'), '≈ 0,6'], [('Войлок', 'Felt'), '≈ 0,06'], [('Воздух', 'Air'), '≈ 0,025']]),
 lab1)

lab2 = model(2, 'КОНВЕКЦИЯ В СОСУДЕ', 'CONVECTION IN A VESSEL', 'cvSvg', '0 0 600 250',
  select('cv', 'Где нагреватель', 'Where the heater is'), '', 'cvFb',
  'Схема условная: стрелки показывают движение воды в сосуде.', 'A schematic drawing: the arrows show the motion of the water in the vessel.')
s2 = section('convection', 'Конвекция', 'Convection',
 bd('<p>В жидкостях и газах тепло переносится самим движением вещества — это <strong>конвекция</strong>. Нагретый слой расширяется, его плотность падает, и он поднимается вверх, а более холодный и плотный слой опускается вниз. Возникает циркуляция.</p><p>Поэтому нагреватель в сосуде ставят снизу (чайник на плите), а батарею в комнате размещают под окном: тёплый воздух поднимается, холодный стекает вниз. В твёрдом теле конвекции нет, потому что частицы не могут перемещаться.</p><p>Такая же конвекция создаёт ветры. В главе 13 мы увидим, как нагретый солнцем склон порождает горный ветер.</p>',
    '<p>In liquids and gases heat is carried by the motion of the substance itself — this is <strong>convection</strong>. A heated layer expands, its density falls and it rises, while colder, denser fluid sinks. A circulation arises.</p><p>That is why a heater is put at the bottom of a vessel (a kettle on the stove) and a radiator in a room goes under the window: warm air rises, cold air flows down. There is no convection in a solid because its particles cannot move about.</p><p>The same convection creates winds. In chapter 13 we will see how a sun-warmed slope produces a mountain wind.</p>'),
 lab2)

lab3 = model(3, 'ИЗЛУЧЕНИЕ НАГРЕТОГО ТЕЛА', 'RADIATION FROM A HOT BODY', 'raSvg', '0 0 600 250',
  slider('rT', 'Температура', 'Temperature', 250, 1000, 10, 300) + slider('rE', 'Излучательная способность ε', 'Emissivity ε', 0.05, 1, 0.05, 1),
  stats([('rP', 'Мощность с 1 м²', 'Power per 1 m²'), ('rX', 'Против 300 К', 'Against 300 K'), ('rC', 'В градусах Цельсия', 'In degrees Celsius')]),
  'raFb', 'Схема условная: чёрное тело (ε = 1) излучает больше всех. Показано только излучение; тело ещё и поглощает излучение окружающих тел.',
  'A schematic drawing: a black body (ε = 1) radiates the most. Only the emission is shown; the body also absorbs radiation from its surroundings.')
s3 = section('radiation', 'Излучение', 'Radiation',
 bd('<p>Третий способ — <strong>излучение</strong>: энергия передаётся электромагнитными волнами и может идти даже через пустоту. Так к нам приходит тепло от Солнца. Излучает любое тело, температура которого выше абсолютного нуля. Чем тело горячее, тем больше излучение, и растёт оно очень быстро — пропорционально четвёртой степени температуры в кельвинах:</p>',
    '<p>The third way is <strong>radiation</strong>: energy is carried by electromagnetic waves and can pass even through a vacuum. That is how the heat of the Sun reaches us. Every body whose temperature is above absolute zero radiates. The hotter the body, the more it radiates, and the growth is very fast — proportional to the fourth power of the temperature in kelvins:</p>')
 + formula('P = ε · σ · S · T⁴', 'σ ≈ 5,67·10⁻⁸ Вт/(м²·К⁴) — постоянная Стефана — Больцмана; ε от 0 до 1 — излучательная способность поверхности', 'σ ≈ 5.67·10⁻⁸ W/(m²·K⁴) is the Stefan–Boltzmann constant; ε from 0 to 1 is the emissivity of the surface')
 + bd('<p>Тёмные шероховатые поверхности излучают и поглощают сильнее, блестящие — слабее. Поэтому у термоса двойные стенки с откачанным воздухом (нет теплопроводности и конвекции) и блестящее покрытие (мало излучения).</p><p>В реальных предметах обычно работают все три способа сразу.</p>',
      '<p>Dark, rough surfaces radiate and absorb more strongly; shiny ones, less. That is why a thermos flask has double walls with the air pumped out (no conduction or convection) and a shiny coating (little radiation).</p><p>In real objects all three ways usually act at once.</p>'),
 lab3)

tasks = [
 task(1, 'Бетонная стена', 'A concrete wall', 'Бетонная стена площадью 10 м² и толщиной 30 см разделяет комнату (20 °C) и улицу (−10 °C). Какой тепловой поток идёт через стену? Для бетона k ≈ 1,7 Вт/(м·К).', 'A concrete wall of area 10 m² and thickness 30 cm separates a room (20 °C) from the street (−10 °C). What heat flow passes through the wall? For concrete k ≈ 1.7 W/(m·K).',
  'S = 10 м², d = 0,3 м, Δt = 30 К, k = 1,7 Вт/(м·К)', 'S = 10 m², d = 0.3 m, Δt = 30 K, k = 1.7 W/(m·K)', 'P = k·S·Δt / d = 1,7 · 10 · 30 / 0,3 = 1700 Вт.<br>За час: 1700 Вт · 3600 с = 6 120 000 Дж ≈ 6,1 МДж.', 'P = k·S·Δt / d = 1.7 · 10 · 30 / 0.3 = 1,700 W.<br>Per hour: 1,700 W · 3,600 s = 6,120,000 J ≈ 6.1 MJ.',
  'около 1,7 кВт (≈ 6,1 МДж за час). Такую мощность нужно возмещать отоплением.', 'about 1.7 kW (≈ 6.1 MJ per hour). Heating must make up this power.', True),
 task(2, 'Войлок вместо бетона', 'Felt instead of concrete', 'Во сколько раз уменьшится тепловой поток, если бетонную стену заменить войлочной той же толщины? Для войлока k ≈ 0,06 Вт/(м·К).', 'By what factor would the heat flow fall if the concrete wall were replaced by a felt wall of the same thickness? For felt k ≈ 0.06 W/(m·K).',
  'k₁ = 1,7, k₂ = 0,06 Вт/(м·К); S, d и Δt те же', 'k₁ = 1.7, k₂ = 0.06 W/(m·K); S, d and Δt are the same', 'P пропорционален k, значит P₁ / P₂ = k₁ / k₂ = 1,7 / 0,06 ≈ 28.', 'P is proportional to k, so P₁ / P₂ = k₁ / k₂ = 1.7 / 0.06 ≈ 28.',
  'примерно в 28 раз меньше.', 'about 28 times smaller.'),
 task(3, 'Металл и дерево на морозе', 'Metal and wood in the frost', 'У медной ручки k ≈ 401, у деревянной ≈ 0,15 Вт/(м·К). Во сколько раз быстрее медь отбирает тепло у руки при одинаковых условиях?', 'A copper handle has k ≈ 401, a wooden one ≈ 0.15 W/(m·K). How many times faster does copper draw heat from the hand under the same conditions?',
  'k₁ = 401, k₂ = 0,15 Вт/(м·К)', 'k₁ = 401, k₂ = 0.15 W/(m·K)', 'Отношение потоков равно отношению k: 401 / 0,15 ≈ 2670.', 'The ratio of flows equals the ratio of k: 401 / 0.15 ≈ 2,670.',
  'в тысячи раз. Поэтому на морозе металл «обжигает» холодом, хотя температура ручек одинакова. На деле поток меньше, так как у кожи тоже есть сопротивление, но порядок разницы велик.', 'by a factor of thousands. That is why metal “burns” with cold in a frost even though both handles have the same temperature. In practice the flow is smaller because skin also resists, but the difference is large.'),
 task(4, 'Излучение тела', 'Radiation from a body', 'Сколько энергии излучает в секунду каждый квадратный метр поверхности абсолютно чёрного тела при 300 К (ε = 1)? σ ≈ 5,67·10⁻⁸ Вт/(м²·К⁴).', 'How much energy per second does each square metre of the surface of a perfectly black body at 300 K (ε = 1) radiate? σ ≈ 5.67·10⁻⁸ W/(m²·K⁴).',
  'T = 300 К, ε = 1, S = 1 м²', 'T = 300 K, ε = 1, S = 1 m²', 'P = σ·T⁴ = 5,67·10⁻⁸ · 300⁴ = 5,67·10⁻⁸ · 8,1·10⁹ ≈ 459 Вт.', 'P = σ·T⁴ = 5.67·10⁻⁸ · 300⁴ = 5.67·10⁻⁸ · 8.1·10⁹ ≈ 459 W.',
  'около 459 Вт с каждого м². Тело при этом и поглощает излучение окружающих предметов, поэтому остывает гораздо медленнее.', 'about 459 W from each m². The body also absorbs radiation from its surroundings, so it cools much more slowly.'),
 task(5, 'Нагрев вдвое', 'Doubling the temperature', 'Как изменится излучаемая мощность чёрного тела, если его температура вырастет с 300 К до 600 К?', 'How does the power radiated by a black body change if its temperature rises from 300 K to 600 K?',
  'T₁ = 300 К, T₂ = 600 К', 'T₁ = 300 K, T₂ = 600 K', 'P пропорциональна T⁴: P₂ / P₁ = (600 / 300)⁴ = 2⁴ = 16.', 'P is proportional to T⁴: P₂ / P₁ = (600 / 300)⁴ = 2⁴ = 16.',
  'вырастет в 16 раз (с 459 до ≈ 7350 Вт/м²).', 'it grows 16 times (from 459 to ≈ 7,350 W/m²).'),
 task(6, 'Оконное стекло', 'A window pane', 'Оценим поток через оконное стекло 1,5 м² толщиной 4 мм при разности температур 20 К. Для стекла k ≈ 1,1 Вт/(м·К).', 'Estimate the flow through a 1.5 m² window pane 4 mm thick for a temperature difference of 20 K. For glass k ≈ 1.1 W/(m·K).',
  'S = 1,5 м², d = 0,004 м, Δt = 20 К, k = 1,1 Вт/(м·К)', 'S = 1.5 m², d = 0.004 m, Δt = 20 K, k = 1.1 W/(m·K)', 'P = k·S·Δt / d = 1,1 · 1,5 · 20 / 0,004 = 8250 Вт.', 'P = k·S·Δt / d = 1.1 · 1.5 · 20 / 0.004 = 8,250 W.',
  'около 8 кВт — для «идеальной» стекляшки, которая держит всю разность температур. В реальности около стекла с обеих сторон есть слои воздуха, а в стеклопакетах — ещё и воздух между стёклами. Они дают главное сопротивление, поэтому потери намного меньше.', 'about 8 kW for an “ideal” pane that holds the whole temperature difference. In reality there are layers of air on both sides of the glass, and in double glazing also air between the panes. They give the main resistance, so the losses are much smaller.'),
]

quiz = [
 ('Каким способом тепло от Солнца доходит до Земли?', [('Теплопроводностью', 'Между Солнцем и Землёй почти пустота: частицы для передачи при столкновениях отсутствуют.'), ('Конвекцией', 'Конвекция требует жидкости или газа.'), ('Излучением', 'Верно: излучение может идти через пустоту.')],
  'By which way does the Sun’s heat reach the Earth?', [('Conduction', 'Between the Sun and the Earth there is almost a vacuum: there are no particles to pass energy on in collisions.'), ('Convection', 'Convection needs a liquid or a gas.'), ('Radiation', 'Correct: radiation can pass through a vacuum.')], 2),
 ('Почему на морозе железная ручка кажется холоднее деревянной при одной температуре?', [('Металл холоднее', 'Температуры равны.'), ('Металл быстрее отводит тепло от руки', 'Верно: у металла большая теплопроводность.'), ('Дерево излучает тепло', 'Дело в теплопроводности, а не в излучении.')],
  'Why does an iron handle feel colder than a wooden one at the same temperature in a frost?', [('The metal is colder', 'The temperatures are equal.'), ('Metal draws heat from the hand faster', 'Correct: metal has a high thermal conductivity.'), ('Wood radiates heat', 'It is a matter of conductivity, not radiation.')], 1),
 ('У какого вещества самая малая теплопроводность?', [('Медь', 'Медь — один из лучших проводников тепла.'), ('Стекло', 'У стекла k около 1,1 — заметно больше, чем у воздуха.'), ('Воздух', 'Верно: k ≈ 0,025 Вт/(м·К).')],
  'Which substance has the smallest thermal conductivity?', [('Copper', 'Copper is one of the best conductors of heat.'), ('Glass', 'Glass has k of about 1.1, much more than air.'), ('Air', 'Correct: k ≈ 0.025 W/(m·K).')], 2),
 ('Где происходит конвекция?', [('В металлическом стержне', 'В твёрдых телах частицы не могут перемещаться по объёму.'), ('В жидкостях и газах', 'Верно: нагретое вещество поднимается и переносит тепло.'), ('Только в вакууме', 'В вакууме вещества нет.')],
  'Where does convection occur?', [('In a metal rod', 'In solids the particles cannot move about the body.'), ('In liquids and gases', 'Correct: the heated substance rises and carries heat.'), ('Only in a vacuum', 'There is no substance in a vacuum.')], 1),
 ('Чтобы быстро нагреть воду в кастрюле, нагреватель нужно расположить…', [('снизу', 'Верно: нагретая вода поднимается, а холодная опускается — вода прогревается вся.'), ('сверху', 'Нагретая у поверхности вода остаётся наверху, глубокие слои прогреваются плохо.'), ('сбоку, без разницы', 'Расположение важно: оно определяет циркуляцию.')],
  'To heat water in a pot quickly, the heater should be placed…', [('at the bottom', 'Correct: the heated water rises and the cold water sinks, so all the water warms.'), ('on top', 'Water heated at the surface stays on top and the deep layers warm poorly.'), ('at the side, no difference', 'The position matters: it sets the circulation.')], 0),
 ('Разность температур по обе стороны стенки удвоили. Как изменится тепловой поток через неё?', [('Не изменится', 'Поток пропорционален разности температур.'), ('Вырастет вдвое', 'Верно: P = k·S·Δt/d, значит P растёт пропорционально Δt.'), ('Вырастет вчетверо', 'Четвёртая степень относится к излучению, не к теплопроводности.')],
  'The temperature difference across a wall was doubled. How does the heat flow through it change?', [('It does not change', 'The flow is proportional to the temperature difference.'), ('It doubles', 'Correct: P = k·S·Δt/d, so P grows in proportion to Δt.'), ('It quadruples', 'The fourth power belongs to radiation, not to conduction.')], 1),
 ('Толщину стенки увеличили вдвое. Как изменится тепловой поток?', [('Уменьшится вдвое', 'Верно: поток обратно пропорционален толщине d.'), ('Увеличится вдвое', 'Наоборот: толстая стена хуже пропускает тепло.'), ('Не изменится', 'Толщина входит в формулу.')],
  'The thickness of a wall was doubled. How does the heat flow change?', [('It halves', 'Correct: the flow is inversely proportional to the thickness d.'), ('It doubles', 'The opposite: a thick wall lets heat through less.'), ('It does not change', 'The thickness is in the formula.')], 0),
 ('Температуру чёрного тела в кельвинах увеличили вдвое. Во сколько раз вырастет его излучение?', [('В 2 раза', 'Мощность излучения пропорциональна T⁴, а не T.'), ('В 4 раза', 'Это был бы квадрат температуры.'), ('В 16 раз', 'Верно: 2⁴ = 16.')],
  'The temperature of a black body in kelvins was doubled. How many times does its radiation grow?', [('2 times', 'The radiated power is proportional to T⁴, not to T.'), ('4 times', 'That would be the square of the temperature.'), ('16 times', 'Correct: 2⁴ = 16.')], 2),
]

js = r'''
const T={ru:{
 conLabel:"Стенка с горячей и холодной сторонами и стрелка теплового потока",cvLabel:"Сосуд с водой, нагреватель и стрелки конвекции",raLabel:"Нагретое тело и излучение",
 mats:["Медь","Алюминий","Железо","Стекло","Вода (неподвижная)","Дерево (≈ 0,15)","Войлок","Воздух (неподвижный)"],
 modes:["Нагреватель снизу","Нагреватель сверху"],hot:"горячая",cold:"холодная",
 conFb:"Чем меньше теплопроводность и больше толщина, тем меньше тепла проходит через стенку.",
 cvFb:["Нагретая вода у дна поднимается, холодная опускается: возникает циркуляция, и вода прогревается вся.","Нагретая у поверхности вода остаётся наверху, и циркуляции нет. Глубина прогревается лишь за счёт слабой теплопроводности воды."],
 raFb:"Мощность растёт как T⁴: при удвоении температуры в кельвинах излучение вырастает в 16 раз. Блестящая поверхность (малая ε) излучает меньше."},
 en:{
 conLabel:"A wall with hot and cold sides and an arrow of heat flow",cvLabel:"A vessel of water, a heater and convection arrows",raLabel:"A hot body and its radiation",
 mats:["Copper","Aluminium","Iron","Glass","Water (still)","Wood (≈ 0.15)","Felt","Air (still)"],
 modes:["Heater at the bottom","Heater at the top"],hot:"hot",cold:"cold",
 conFb:"The smaller the conductivity and the greater the thickness, the less heat passes through the wall.",
 cvFb:["Heated water at the bottom rises and cold water sinks: a circulation arises and all the water warms.","Water heated at the surface stays on top and there is no circulation. The depth warms only through the weak conductivity of water."],
 raFb:"The power grows as T⁴: doubling the temperature in kelvins makes the radiation 16 times greater. A shiny surface (small ε) radiates less."}};
const K=[401,237,80,1.1,0.6,0.15,0.06,0.025],SIG=5.670374e-8;
function drawCon(){const t=tt(),i=+$("cm").value,k=K[i],d=+$("cd").value/1000,dt=+$("ct").value,P=k*1*dt/d,E=P*3600,w=Math.max(10,Math.min(240,20+d*1000/200*220));
 const x0=150,w0=Math.max(20,d*1000/200*220),sw=2+7*Math.log10(1+P)/Math.log10(1+401*50/0.005),
 hotCol="#b6533f",coldCol="#8eb8d1";
 let g='<rect x="40" y="50" width="'+(x0-40)+'" height="150" fill="'+hotCol+'" fill-opacity="0.25"/><rect x="'+(x0+w0)+'" y="50" width="'+(520-x0-w0)+'" height="150" fill="'+coldCol+'" fill-opacity="0.35"/>';
 g+='<rect x="'+x0+'" y="50" width="'+w0+'" height="150" fill="#c9c2b0" stroke="#18181a" stroke-width="2"/>';
 g+=svgText(45,45,t.hot+" "+fmt(dt,0)+t.K,"#b6533f","start",11)+svgText(515,45,t.cold,"#3f5f8f","end",11);
 g+=arrow(60,125,x0-4,125,hotCol,sw)+arrow(x0+w0+4,125,500,125,"#3f5f8f",sw);
 g+=svgText(x0+w0/2,222,"d = "+fmt(d*1000,0)+t.mm,"#66666b","middle",11);
 $("conSvg").innerHTML=g;
 $("cdOut").textContent=fmt(d*1000,0)+t.mm;$("ctOut").textContent=dt+t.K;
 $("cP").textContent=P>=1e4?num(Math.round(P))+t.W:fmt(P,P<10?2:0)+t.W;
 $("cE").textContent=E>=1e9?num(Math.round(E/1e6))+t.MJ:(E>=1e6?fmt(E/1e6,2)+t.MJ:fmt(E/1e3,1)+t.kJ);
 const rr=401/k;$("cR").textContent=k===401?"1":"1 : "+(rr>=100?num(Math.round(rr)):fmt(rr,1));
 $("conFb").textContent=t.conFb}
["cm","cd","ct"].forEach(id=>$(id).addEventListener("input",drawCon));
function drawCv(){const t=tt(),m=+$("cv").value;
 let g='<path d="M170 40 L170 200 Q170 215 185 215 L415 215 Q430 215 430 200 L430 40" fill="#8eb8d1" fill-opacity="0.35" stroke="#18181a" stroke-width="3"/>';
 const hy=m===0?228:36;g+='<rect x="210" y="'+(hy-6)+'" width="180" height="12" rx="5" fill="#b6533f"/>'+svgText(300,m===0?246:26,t.modes[m],"#b6533f","middle",11);
 if(m===0){g+=arrow(255,190,255,70,"#b6533f",4)+arrow(345,190,345,70,"#b6533f",4)+arrow(200,80,200,170,"#3f5f8f",3)+arrow(400,80,400,170,"#3f5f8f",3)+arrow(215,60,385,60,"#b6533f",2)}
 else{g+='<circle cx="300" cy="62" r="18" fill="#b6533f" fill-opacity="0.35"/><line x1="300" y1="86" x2="300" y2="100" stroke="#b6533f" stroke-dasharray="3 3"/>'}
 $("cvSvg").innerHTML=g;$("cvFb").textContent=t.cvFb[m]}
$("cv").addEventListener("input",drawCv);
function drawRa(){const t=tt(),T0=+$("rT").value,e=+$("rE").value,P=e*SIG*Math.pow(T0,4),P0=e*SIG*Math.pow(300,4),r=Math.min(1,P/(SIG*Math.pow(1000,4)));
 const tc=T0>1000?"#f2c14e":T0>800?"#d9602d":T0>600?"#b6533f":"#8a8a8f";
 let g='<rect x="60" y="80" width="130" height="100" rx="8" fill="'+tc+'" stroke="#18181a" stroke-width="2"/>'+svgText(125,135,fmt(T0,0)+t.K,"#fff","middle",14);
 for(let k=0;k<5;k++){const y=90+k*20,L=20+r*180;g+=arrow(200,y,200+L,y,"#b6533f",2+r*3)}
 g+=svgText(125,205,"ε = "+fmt(e,2),"#66666b","middle",11);
 $("raSvg").innerHTML=g;
 $("rTOut").textContent=fmt(T0,0)+t.K;$("rEOut").textContent=fmt(e,2);
 $("rP").textContent=num(Math.round(P))+(lang==="ru"?" Вт":" W");$("rX").textContent="× "+fmt(P/P0,1);$("rC").textContent=fmt(T0-273.15,0)+" °C";
 $("raFb").textContent=t.raFb}
["rT","rE"].forEach(id=>$(id).addEventListener("input",drawRa));
const LAB={ru:{conSvg:T.ru.conLabel,cvSvg:T.ru.cvLabel,raSvg:T.ru.raLabel},en:{conSvg:T.en.conLabel,cvSvg:T.en.cvLabel,raSvg:T.en.raLabel}};
function drawAll(){fillSel("cm",T[lang].mats,3);fillSel("cv",T[lang].modes,0);drawCon();drawCv();drawRa()}
'''

c = dict(n='09', slug='09-heat-transfer.html', block='II', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Теплопередача', 'Heat transfer'),
 desc='Глава 9 Атласа физики: теплопроводность, конвекция, излучение, закон теплопроводности, излучение нагретого тела.',
 lead=('Железная ручка на морозе обжигает холодом, чайник нагревается на плите, а тепло Солнца доходит до нас сквозь пустоту. Три способа передачи тепла — теплопроводность, конвекция и излучение.',
       'An iron handle burns with cold in the frost, a kettle warms on the stove and the Sun’s heat reaches us across a vacuum. Three ways of transferring heat: conduction, convection and radiation.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('conduction', 'Теплопроводность', 'Conduction'), ('convection', 'Конвекция', 'Convection'), ('radiation', 'Излучение', 'Radiation'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Зимним утром на улице −20 °C. Вы берёте голой рукой металлическую ручку калитки — и она «обжигает» холодом. Деревянная ручка рядом кажется намного теплее, хотя она стоит на том же морозе. Градусник покажет для обеих одну и ту же температуру.</p><p>Почему металл кажется холоднее дерева, если температуры одинаковые?</p>',
         '<p>On a winter morning it is −20 °C outside. You take a metal gate handle in your bare hand and it “burns” with cold. A wooden handle beside it feels much warmer though it stands in the same frost. A thermometer would show the same temperature for both.</p><p>Why does metal feel colder than wood if the temperatures are equal?</p>'),
 hint=('Подсказку даст модель «Теплопроводность». Разгадка — в конце главы.', 'The “Conduction” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему металл кажется холоднее', 'The answer: why metal feels colder'),
 answer=('<p>Холод мы ощущаем не по температуре предмета, а по тому, как быстро он отбирает тепло у кожи. Теплопроводность меди или железа в сотни и тысячи раз больше, чем у дерева (задача 3). Рука отдаёт тепло металлу, а металл мгновенно распределяет его по всей ручке, и место контакта остаётся холодным. Дерево проводит тепло плохо: поверхность быстро нагревается до температуры кожи, и тепло почти перестаёт уходить.</p><p>Поэтому на морозе нельзя касаться металла голой рукой — кожа может примёрзнуть. А тёплую зимнюю одежду, войлок и мех делают из материалов с воздухом в порах: воздух проводит тепло очень плохо.</p>',
         '<p>We sense cold not from the temperature of an object but from how fast it draws heat from the skin. The conductivity of copper or iron is hundreds or thousands of times greater than that of wood (problem 3). The hand gives heat to the metal and the metal spreads it through the whole handle at once, so the spot of contact stays cold. Wood conducts heat poorly: its surface quickly warms to skin temperature and heat almost stops flowing out.</p><p>That is why in a frost one should not touch metal with a bare hand — the skin can stick. Warm winter clothes, felt and fur are made of materials with air in their pores: air conducts heat very poorly.</p>'),
 sources=[
  ('Значения теплопроводности (медь, алюминий, железо, стекло, вода, воздух, бетон, войлок) —', 'Values of thermal conductivity (copper, aluminium, iron, glass, water, air, concrete, felt) —', LINK('https://www.newworldencyclopedia.org/entry/Thermal_conductivity', 'New World Encyclopedia: Thermal conductivity') + ', ' + LINK('https://physics.info/conduction/', 'The Physics Hypertextbook: Conduction') + ', ' + LINK('https://energyeducation.ca/encyclopedia/Thermal_conductivity', 'Energy Education: Thermal conductivity')),
  ('Закон теплопроводности для стенки, формула с S, Δt и толщиной —', 'The law of conduction for a wall, the formula with S, Δt and thickness —', LINK('https://www.newworldencyclopedia.org/entry/Watt_per_metre-kelvin', 'New World Encyclopedia: Watt per metre-kelvin')),
  ('Закон Стефана — Больцмана, постоянная σ, излучательная способность —', 'The Stefan–Boltzmann law, the constant σ, emissivity —', LINK('https://physics.info/radiation/', 'The Physics Hypertextbook: Thermal radiation') + ', ' + LINK('https://physicsforums.com/tags/stefan-boltzmann/wiki', 'Physics Forums: Stefan–Boltzmann')),
  ('Содержание темы в программе Министерства (8 класс: вещество и тепловые явления) —', 'The topic in the Ministry’s programme (grade 8: matter and thermal phenomena) —', LINK('https://edu.gov.kg/media/files/f34d9f4a-9197-49bd-8e3e-939cb10015e1.pdf', 'Программа по физике, 7–9 классы'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Значения k для дерева и бетона — типичные (зависят от материала). Расчёты для стекла — упрощённые.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The k values for wood and concrete are typical (they depend on the material). The glass calculations are simplified.'),
 prev=('08-temperature.html', 'Глава 08 · Температура и термометры', 'Chapter 08 · Temperature and thermometers'),
 next=('10-heat-capacity.html', 'Глава 10 · Количество теплоты', 'Chapter 10 · Amount of heat'),
 js=js)
build(c)
