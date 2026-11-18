# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'МОЩНОСТЬ ГЭС', 'POWER OF A HYDROPOWER PLANT', 'hpSvg', '0 0 600 250',
  slider('hq', 'Расход воды', 'Water flow', 10, 600, 10, 200) + slider('hh', 'Напор (перепад высот)', 'Head (height difference)', 10, 215, 5, 100) + slider('he', 'КПД', 'Efficiency', 0.5, 0.95, 0.01, 0.9),
  stats([('hP', 'Мощность P = ρgQHη', 'Power P = ρgQHη'), ('hT', 'Сколько таких турбин по 300 МВт', 'How many 300 MW turbines')]),
  'hpFb', 'Схема условная: плотина и водохранилище; значения напора и расхода выбраны для модели. Высота плотины Токтогульской ГЭС — 215 м, но рабочий напор зависит от уровня воды. ρ = 1000 кг/м³, g = 9,8 Н/кг.',
  'A schematic drawing: a dam and reservoir; the head and flow values are chosen for the model. The Toktogul dam is 215 m high but the working head depends on the water level. ρ = 1000 kg/m³, g = 9.8 N/kg.')
s1 = section('hydro', 'Как ГЭС превращает воду в ток', 'How a hydropower plant turns water into current',
 bd('<p>Вода на высоте обладает потенциальной энергией. Падая по трубам, она раскручивает турбину, а турбина — ротор генератора (глава 23). Цепочка превращений: <strong>потенциальная энергия воды → кинетическая → вращение → электрическая энергия</strong>. Мощность станции:</p>',
    '<p>Water at a height has potential energy. Falling through pipes it spins a turbine, and the turbine spins the generator rotor (chapter 23). The chain of conversions: <strong>potential energy of water → kinetic → rotation → electrical energy</strong>. The power of the plant:</p>')
 + formula('P = ρ · g · Q · H · η', 'ρ — плотность воды, Q — расход (м³/с), H — напор (м), η — КПД; результат в ваттах', 'ρ is the density of water, Q the flow (m³/s), H the head (m), η the efficiency; the result is in watts')
 + bd('<p>Токтогульская ГЭС на реке Нарын — самая мощная в Кыргызстане: плотина высотой 215 м, четыре агрегата, установленная мощность 1200 МВт (после модернизации — до 1440 МВт). Водохранилище служит запасом энергии на зиму: его полезный объём 14 км³.</p>',
      '<p>The Toktogul plant on the Naryn River is the most powerful in Kyrgyzstan: a dam 215 m high, four units, installed capacity 1,200 MW (up to 1,440 MW after modernisation). The reservoir serves as a store of energy for winter: its active volume is 14 km³.</p>'),
 lab1)

lab2 = model(2, 'ЛИНИЯ ЭЛЕКТРОПЕРЕДАЧИ', 'A POWER LINE', 'plSvg', '0 0 600 250',
  slider('lp', 'Передаваемая мощность', 'Power transmitted', 10, 500, 10, 100) + slider('lu', 'Напряжение в линии', 'Line voltage', 35, 500, 5, 220) + slider('lr', 'Сопротивление линии', 'Line resistance', 1, 30, 1, 10),
  stats([('lI', 'Ток в линии I = P/U', 'Line current I = P/U'), ('lL', 'Потери ΔP = I²R', 'Losses ΔP = I²R'), ('lK', 'Доля потерь', 'Share of losses')]),
  'plFb', 'Схема условная: мощность в мегаваттах, напряжение в киловольтах, сопротивление всей линии в омах.',
  'A schematic drawing: the power in megawatts, the voltage in kilovolts, the resistance of the whole line in ohms.')
s2 = section('grid', 'Трансформатор и линия электропередачи', 'The transformer and the power line',
 bd('<p>Генератор даёт десятки киловольт, а в розетке 220 В. Между ними — <strong>трансформаторы</strong>: две катушки на общем железном сердечнике. Переменный ток первой катушки создаёт меняющийся поток, и во второй возникает ЭДС индукции. Напряжения относятся как числа витков:</p>',
    '<p>The generator gives tens of kilovolts and a socket 220 V. Between them are <strong>transformers</strong>: two coils on a common iron core. The alternating current of the first coil creates a changing flux and an induced EMF arises in the second. The voltages are in the ratio of the numbers of turns:</p>')
 + formula('U₁ / U₂ = N₁ / N₂', 'работает только с переменным током; мощность почти не меняется: U₁I₁ ≈ U₂I₂', 'works only with alternating current; the power hardly changes: U₁I₁ ≈ U₂I₂')
 + bd('<p>Зачем повышать напряжение перед линией? Мощность <em>P = U·I</em>. При том же <em>P</em> чем больше <em>U</em>, тем меньше ток. А потери на нагрев проводов <em>ΔP = I²·R</em>, то есть они зависят от квадрата тока: напряжение выше вдвое — потери меньше в четыре раза.</p>',
      '<p>Why raise the voltage before the line? The power is <em>P = U·I</em>. At the same <em>P</em> the greater the <em>U</em>, the smaller the current. And the heating loss in the wires is <em>ΔP = I²·R</em>, which depends on the square of the current: twice the voltage — four times smaller losses.</p>'),
 lab2)

lab3 = model(3, 'КАСКАД НА НАРЫНЕ', 'THE NARYN CASCADE', 'caSvg', '0 0 600 250',
  slider('cn', 'Сколько станций включено (сверху вниз)', 'How many plants are on (from the top)', 1, 5, 1, 5),
  stats([('cS', 'Суммарная мощность', 'Total capacity'), ('cT', 'Доля Токтогульской', 'Share of Toktogul'), ('cW', 'Тот же поток воды работает на', 'The same stream of water works at')]),
  'caFb', 'Схема условная, без масштаба. Мощности станций: Токтогульская 1200, Курпсайская 800, Таш-Кумырская 450, Шамалды-Сайская 240, Учкурганская 180 МВт (проектные значения).',
  'A schematic drawing, not to scale. Plant capacities: Toktogul 1,200, Kurpsai 800, Tash-Kumyr 450, Shamaldy-Sai 240, Uch-Kurgan 180 MW (design values).')
s3 = section('cascade', 'Каскад: одна вода — много станций', 'A cascade: one water — many plants',
 bd('<p>Нарын течёт с гор вниз, и на нём построена цепочка станций — <strong>Нарынский каскад</strong>: Токтогульская, Курпсайская, Таш-Кумырская, Шамалды-Сайская, Учкурганская. Одна и та же вода, пройдя через верхнюю станцию, попадает на следующую и снова вращает турбины. Верхнее водохранилище накапливает воду летом, чтобы зимой, когда в стране больше всего нужно света и тепла, станции вырабатывали ток.</p><p>Около 90% электричества Кыргызстана вырабатывают ГЭС. Это очень чистая энергия, но она зависит от воды: в маловодные годы запас в Токтогульском водохранилище падает, и зимой приходится экономить.</p>',
    '<p>The Naryn flows down from the mountains and a chain of plants is built on it — the <strong>Naryn cascade</strong>: Toktogul, Kurpsai, Tash-Kumyr, Shamaldy-Sai, Uch-Kurgan. The same water, having passed through the upper plant, reaches the next and spins turbines again. The upper reservoir stores water in summer so that in winter, when the country most needs light and heat, the plants produce current.</p><p>About 90% of Kyrgyzstan’s electricity is produced by hydropower plants. It is very clean energy but depends on water: in dry years the stock in the Toktogul reservoir falls and in winter people have to economise.</p>'),
 lab3)

tasks = [
 task(1, 'Мощность станции', 'Plant power', 'Расход воды 200 м³/с, напор 100 м, КПД 0,9. Найдите мощность. ρ = 1000 кг/м³, g = 9,8 Н/кг.', 'Water flow 200 m³/s, head 100 m, efficiency 0.9. Find the power. ρ = 1000 kg/m³, g = 9.8 N/kg.',
  'Q = 200 м³/с, H = 100 м, η = 0,9', 'Q = 200 m³/s, H = 100 m, η = 0.9', 'P = ρ·g·Q·H·η = 1000 · 9,8 · 200 · 100 · 0,9 = 1,764·10⁸ Вт.', 'P = ρ·g·Q·H·η = 1000 · 9.8 · 200 · 100 · 0.9 = 1.764·10⁸ W.',
  'около 176 МВт.', 'about 176 MW.', True),
 task(2, 'Какой нужен расход', 'The flow needed', 'Какой расход воды нужен для мощности 300 МВт при напоре 130 м и КПД 0,9?', 'What water flow is needed for 300 MW at a head of 130 m and efficiency 0.9?',
  'P = 3·10⁸ Вт, H = 130 м, η = 0,9', 'P = 3·10⁸ W, H = 130 m, η = 0.9', 'Q = P / (ρ·g·H·η) = 3·10⁸ / (1000 · 9,8 · 130 · 0,9) = 3·10⁸ / 1,1466·10⁶ ≈ 262 м³/с.', 'Q = P / (ρ·g·H·η) = 3·10⁸ / (1000 · 9.8 · 130 · 0.9) = 3·10⁸ / 1.1466·10⁶ ≈ 262 m³/s.',
  'около 262 м³/с — это почти 262 тонн воды каждую секунду через один агрегат.', 'about 262 m³/s — almost 262 tonnes of water every second through one unit.'),
 task(3, 'Трансформатор', 'A transformer', 'Первичная обмотка повышающего трансформатора имеет 500 витков, напряжение 10 кВ. Сколько витков во вторичной обмотке для 220 кВ?', 'The primary winding of a step-up transformer has 500 turns and 10 kV. How many turns must the secondary have for 220 kV?',
  'N₁ = 500, U₁ = 10 кВ, U₂ = 220 кВ', 'N₁ = 500, U₁ = 10 kV, U₂ = 220 kV', 'N₂ = N₁ · U₂ / U₁ = 500 · 220 / 10 = 11 000.', 'N₂ = N₁ · U₂ / U₁ = 500 · 220 / 10 = 11,000.',
  '11 000 витков.', '11,000 turns.'),
 task(4, 'Потери в линии', 'Losses in the line', 'По линии сопротивлением 10 Ом передают 100 МВт при напряжении 220 кВ. Найдите ток, потери и их долю.', 'A line of resistance 10 Ω carries 100 MW at 220 kV. Find the current, the losses and their share.',
  'P = 10⁸ Вт, U = 2,2·10⁵ В, R = 10 Ом', 'P = 10⁸ W, U = 2.2·10⁵ V, R = 10 Ω', 'I = P / U = 10⁸ / 2,2·10⁵ ≈ 455 А.<br>ΔP = I²·R = 455² · 10 ≈ 2,07·10⁶ Вт.<br>Доля: 2,07 / 100 ≈ 2,1%.', 'I = P / U = 10⁸ / 2.2·10⁵ ≈ 455 A.<br>ΔP = I²·R = 455² · 10 ≈ 2.07·10⁶ W.<br>Share: 2.07 / 100 ≈ 2.1%.',
  '455 А; 2,1 МВт; 2,1%.', '455 A; 2.1 MW; 2.1%.'),
 task(5, 'Выше напряжение', 'Higher voltage', 'Во сколько раз уменьшатся потери в задаче 4, если поднять напряжение до 500 кВ (мощность и сопротивление те же)?', 'By what factor do the losses of problem 4 fall if the voltage is raised to 500 kV (the same power and resistance)?',
  'U = 5·10⁵ В', 'U = 5·10⁵ V', 'I = 10⁸ / 5·10⁵ = 200 А.<br>ΔP = 200² · 10 = 4·10⁵ Вт = 0,4 МВт.<br>2,07 / 0,4 ≈ 5,2 (то есть (500/220)² ≈ 5,2).', 'I = 10⁸ / 5·10⁵ = 200 A.<br>ΔP = 200² · 10 = 4·10⁵ W = 0.4 MW.<br>2.07 / 0.4 ≈ 5.2 (that is (500/220)² ≈ 5.2).',
  'примерно в 5 раз: потери падают как квадрат напряжения.', 'about 5 times: losses fall as the square of the voltage.'),
 task(6, 'Коэффициент использования', 'Capacity factor', 'Токтогульская ГЭС мощностью 1200 МВт вырабатывает в среднем 4400 ГВт·ч в год. Какую долю года она работает на полную мощность?', 'The 1,200 MW Toktogul plant produces on average 4,400 GWh a year. For what fraction of the year would it need to run at full power?',
  'P = 1200 МВт, E = 4400 ГВт·ч, год ≈ 8760 ч', 'P = 1,200 MW, E = 4,400 GWh, year ≈ 8,760 h', 'При полной мощности за год: 1200 МВт · 8760 ч = 10 512 ГВт·ч.<br>Доля: 4400 / 10 512 ≈ 0,42.', 'At full power over a year: 1,200 MW · 8,760 h = 10,512 GWh.<br>Share: 4,400 / 10,512 ≈ 0.42.',
  'около 42%: станция работает не всё время на полную мощность, а подстраивается под воду и потребление.', 'about 42%: the plant does not run at full power all the time but adjusts to water and demand.'),
]

quiz = [
 ('Какие превращения энергии происходят на ГЭС?', [('Потенциальная энергия воды → вращение → электричество', 'Верно.'), ('Тепло топлива → пар → электричество', 'Это тепловая станция.'), ('Свет → электричество', 'Это солнечная батарея.')],
  'What energy conversions occur at a hydropower plant?', [('Potential energy of water → rotation → electricity', 'Correct.'), ('Fuel heat → steam → electricity', 'That is a thermal plant.'), ('Light → electricity', 'That is a solar panel.')], 0),
 ('От чего зависит мощность ГЭС?', [('От расхода воды, напора и КПД', 'Верно.'), ('Только от цвета воды', 'Цвет не влияет.'), ('Только от времени суток', 'Нет.')],
  'What does the power of a hydropower plant depend on?', [('Water flow, head and efficiency', 'Correct.'), ('Only on the colour of the water', 'Colour has no effect.'), ('Only on the time of day', 'No.')], 0),
 ('Что делает трансформатор?', [('Меняет напряжение переменного тока', 'Верно.'), ('Превращает переменный ток в постоянный', 'Это выпрямитель.'), ('Создаёт энергию', 'Закон сохранения энергии запрещает.')],
  'What does a transformer do?', [('Changes the voltage of alternating current', 'Correct.'), ('Turns alternating current into direct', 'That is a rectifier.'), ('Creates energy', 'The law of conservation of energy forbids it.')], 0),
 ('Почему трансформатор не работает на постоянном токе?', [('Нужен меняющийся магнитный поток', 'Верно.'), ('Постоянный ток слишком слабый', 'Дело в потоке.'), ('Сердечник плавится', 'Нет.')],
  'Why does a transformer not work on direct current?', [('A changing magnetic flux is needed', 'Correct.'), ('Direct current is too weak', 'It is about the flux.'), ('The core melts', 'No.')], 0),
 ('Зачем в линиях электропередачи применяют высокое напряжение?', [('Чтобы уменьшить ток и потери на нагрев проводов', 'Верно.'), ('Чтобы провода были красивее', 'Нет.'), ('Чтобы увеличить сопротивление', 'Цель обратная.')],
  'Why is high voltage used in power lines?', [('To reduce the current and heating losses in the wires', 'Correct.'), ('To make the wires prettier', 'No.'), ('To increase the resistance', 'The purpose is the opposite.')], 0),
 ('Как изменятся потери в линии при удвоении напряжения (та же мощность)?', [('Уменьшатся в 4 раза', 'Верно: ΔP ~ 1/U².'), ('Уменьшатся в 2 раза', 'Зависимость квадратичная.'), ('Не изменятся', 'Они меняются.')],
  'How do the line losses change when the voltage is doubled (the same power)?', [('Fall 4 times', 'Correct: ΔP ~ 1/U².'), ('Fall 2 times', 'The dependence is quadratic.'), ('Do not change', 'They change.')], 0),
 ('Что такое каскад ГЭС?', [('Цепочка станций на одной реке', 'Верно.'), ('Одна станция с одним агрегатом', 'Это не каскад.'), ('Линия электропередачи', 'Это другое.')],
  'What is a cascade of hydropower plants?', [('A chain of plants on one river', 'Correct.'), ('One plant with one unit', 'That is not a cascade.'), ('A power line', 'That is something else.')], 0),
 ('Какая доля электроэнергии Кыргызстана вырабатывается на ГЭС?', [('Около 90%', 'Верно.'), ('Около 10%', 'Намного больше.'), ('Около 50%', 'Намного больше.')],
  'What share of Kyrgyzstan’s electricity is produced by hydropower plants?', [('About 90%', 'Correct.'), ('About 10%', 'Much more.'), ('About 50%', 'Much more.')], 0),
]

js = r'''
const T={ru:{
 hpLabel:"Плотина, водохранилище и турбина",plLabel:"Электростанция, повышающий трансформатор, линия и потребитель",caLabel:"Цепочка станций на реке Нарын",
 names:["Токтогульская","Курпсайская","Таш-Кумырская","Шамалды-Сайская","Учкурганская"],
 hpFb:"Больше воды и выше напор — больше мощность.",plFb:"Выше напряжение — меньше ток и меньше потери.",caFb:"Одна и та же вода работает на каждой следующей станции."},
 en:{
 hpLabel:"A dam, a reservoir and a turbine",plLabel:"A power station, a step-up transformer, a line and a consumer",caLabel:"A chain of plants on the Naryn River",
 names:["Toktogul","Kurpsai","Tash-Kumyr","Shamaldy-Sai","Uch-Kurgan"],
 hpFb:"More water and a higher head — more power.",plFb:"A higher voltage — a smaller current and smaller losses.",caFb:"The same water works at each following plant."}};
const CAP=[1200,800,450,240,180];
function drawHp(){const t=tt(),Q=+$("hq").value,H=+$("hh").value,e=+$("he").value,P=1000*9.8*Q*H*e;
 const h=20+H/215*140;
 let g='<polygon points="150,'+(230-h)+' 230,230 150,230" fill="#c9c2b0" stroke="#18181a" stroke-width="2"/><rect x="60" y="'+(230-h)+'" width="90" height="'+h+'" fill="#bcd4e6" stroke="#3f5f8f"/>';
 g+=svgText(105,230-h/2,"H = "+H+(lang==="ru"?" м":" m"),"#18181a","middle",12);
 g+='<rect x="230" y="215" width="70" height="25" fill="#9a9a9a" stroke="#18181a"/><circle cx="265" cy="228" r="9" fill="#b6533f"/>';
 const wq=2+Q/600*12;g+='<line x1="230" y1="'+(230-h/3)+'" x2="265" y2="215" stroke="#3f5f8f" stroke-width="'+wq+'"/>';
 g+='<line x1="300" y1="228" x2="470" y2="228" stroke="#18181a" stroke-width="2"/>'+svgText(400,215,fmt(P/1e6,0)+(lang==="ru"?" МВт":" MW"),"#2f6f5d","middle",15);
 $("hpSvg").innerHTML=g;
 $("hqOut").textContent=Q+UN[lang].m+"³/"+(lang==="ru"?"с":"s");$("hhOut").textContent=H+(lang==="ru"?" м":" m");$("heOut").textContent=fmt(e,2);
 $("hP").textContent=fmt(P/1e6,0)+(lang==="ru"?" МВт":" MW");$("hT").textContent=fmt(P/300e6,1);$("hpFb").textContent=t.hpFb}
["hq","hh","he"].forEach(id=>$(id).addEventListener("input",drawHp));
function drawPl(){const t=tt(),P=+$("lp").value*1e6,U=+$("lu").value*1e3,R=+$("lr").value,I=P/U,L=I*I*R,k=L/P;
 const bad=k>=1;
 let g='<rect x="30" y="90" width="70" height="70" fill="#e8e4d8" stroke="#18181a"/>'+svgText(65,130,"G","#18181a","middle",20);
 g+='<rect x="130" y="100" width="40" height="50" fill="#9a9a9a" stroke="#18181a"/><line x1="100" y1="125" x2="130" y2="125" stroke="#18181a" stroke-width="2"/>';
 g+='<line x1="170" y1="125" x2="430" y2="125" stroke="#b87333" stroke-width="'+(2+Math.min(8,I/1500))+'"/>';
 g+='<rect x="430" y="100" width="40" height="50" fill="#9a9a9a" stroke="#18181a"/><rect x="500" y="90" width="70" height="70" fill="#e8e4d8" stroke="#18181a"/>'+svgText(535,130,"220 V","#18181a","middle",14);
 g+='<line x1="470" y1="125" x2="500" y2="125" stroke="#18181a" stroke-width="2"/>'+svgText(300,100,"U = "+(U/1e3)+" kV","#18181a","middle",13);
 g+='<rect x="170" y="190" width="260" height="14" fill="#e3e1da"/><rect x="170" y="190" width="'+(260*Math.min(1,k))+'" height="14" fill="#b6533f"/>'+svgText(300,222,(bad?">100%":fmt(k*100,1)+"%"),"#18181a","middle",12);
 $("plSvg").innerHTML=g;
 $("lpOut").textContent=(P/1e6)+(lang==="ru"?" МВт":" MW");$("luOut").textContent=(U/1e3)+" kV";$("lrOut").textContent=R+(lang==="ru"?" Ом":" Ω");
 $("lI").textContent=num(Math.round(I))+(lang==="ru"?" А":" A");$("lL").textContent=bad?(lang==="ru"?"больше мощности — невозможно":"more than the power — impossible"):fmt(L/1e6,2)+(lang==="ru"?" МВт":" MW");$("lK").textContent=bad?"> 100%":fmt(k*100,1)+"%";$("plFb").textContent=t.plFb}
["lp","lu","lr"].forEach(id=>$(id).addEventListener("input",drawPl));
function drawCa(){const t=tt(),n=+$("cn").value;let sum=0;
 let g='<path d="M30 40 C150 50 200 110 300 130 S470 190 570 220" fill="none" stroke="#3f5f8f" stroke-width="4"/>';
 for(let i=0;i<5;i++){const x=70+i*115,y=48+i*34,on=i<n;if(on)sum+=CAP[i];
  g+='<rect x="'+(x-16)+'" y="'+(y-16)+'" width="32" height="32" fill="'+(on?"#2f6f5d":"#d8d5cb")+'" stroke="#18181a"/>'+svgText(x,y+4,CAP[i],on?"#fff":"#66666b","middle",10)+svgText(x,y+34,t.names[i],"#18181a","middle",10)}
 $("caSvg").innerHTML=g;
 $("cnOut").textContent=n;
 $("cS").textContent=num(sum)+(lang==="ru"?" МВт":" MW");$("cT").textContent=fmt(1200/sum*100,0)+"%";$("cW").textContent=n+(lang==="ru"?" станциях":" plants");$("caFb").textContent=t.caFb}
$("cn").addEventListener("input",drawCa);
const LAB={ru:{hpSvg:T.ru.hpLabel,plSvg:T.ru.plLabel,caSvg:T.ru.caLabel},en:{hpSvg:T.en.hpLabel,plSvg:T.en.plLabel,caSvg:T.en.caLabel}};
function drawAll(){drawHp();drawPl();drawCa()}
'''

c = dict(n='24', slug='24-power-grid.html', block='IV', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('ГЭС и электросеть', 'Hydropower and the power grid'),
 desc='Глава 24 Атласа физики: как ГЭС превращает воду в ток, мощность станции, трансформатор, потери в линиях, Токтогульская ГЭС и Нарынский каскад.',
 lead=('Вода в горах Кыргызстана становится светом в наших домах. Мощность ГЭС, трансформатор, высокое напряжение и Нарынский каскад.',
       'Water in the mountains of Kyrgyzstan becomes light in our homes. The power of a hydropower plant, the transformer, high voltage and the Naryn cascade.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('hydro', 'ГЭС', 'Hydropower'), ('grid', 'Трансформатор и линия', 'Transformer and line'), ('cascade', 'Каскад', 'Cascade'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>В розетке 220 вольт, а на огромных опорах вдоль дорог, на проводах с гирляндами изоляторов, — сотни тысяч вольт. Провода такие тонкие по сравнению с мощностью, которую они несут от далёкой ГЭС до города. Казалось бы, высокое напряжение опаснее, зачем его применять?</p><p>Почему электричество везут на большое расстояние именно при высоком напряжении?</p>',
         '<p>A socket has 220 volts but on huge pylons along roads, on wires with strings of insulators, there are hundreds of thousands of volts. The wires are so thin compared with the power they carry from a distant hydropower plant to a city. High voltage seems more dangerous, so why use it?</p><p>Why is electricity carried over long distances at high voltage?</p>'),
 hint=('Подсказку даст модель «Линия электропередачи». Разгадка — в конце главы.', 'The “A power line” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: как уменьшить потери', 'The answer: how to reduce losses'),
 answer=('<p>Провода греются, и часть энергии теряется: ΔP = I²·R. Передаваемая мощность P = U·I, поэтому при высоком напряжении тот же P передают при гораздо меньшем токе, а потери падают как квадрат тока. При 220 кВ потери в модели около 2%, а при низком напряжении линия съела бы почти всю мощность (поэкспериментируйте в модели 2).</p><p>Поэтому у станции напряжение повышают трансформатором, а у города — понижают в несколько ступеней до 220 В. Опасность высокого напряжения устраняют высотой опор и изоляторами.</p>',
         '<p>Wires heat and part of the energy is lost: ΔP = I²·R. The transmitted power is P = U·I, so at high voltage the same P is sent at a much smaller current and the losses fall as the square of the current. At 220 kV the losses in the model are about 2% while at low voltage the line would eat almost all the power (experiment in model 2).</p><p>That is why a transformer raises the voltage at the plant and several steps lower it to 220 V near the city. The danger of high voltage is dealt with by the height of the pylons and the insulators.</p>'),
 sources=[
  ('Токтогульская ГЭС: плотина 215 м, 1200 МВт, объём водохранилища, выработка 4400 ГВт·ч —', 'The Toktogul plant: dam 215 m, 1,200 MW, reservoir volume, output of 4,400 GWh —', LINK('https://en.wikipedia.org/wiki/Toktogul_Dam', 'Wikipedia: Toktogul Dam') + ', ' + LINK('https://www.cawater-info.net/bk/1-1-1-1-3-kg_e.htm', 'CAWater-Info: водохранилища и ГЭС Кыргызстана')),
  ('Модернизация до 1440 МВт и станции каскада —', 'Modernisation to 1,440 MW and the cascade plants —', LINK('https://invest.gov.kg/wp-content/uploads/2019/07/2-Hydropower.org-Kyrgyz-Republic%E2%80%99s-hydropower-overview-2017.pdf', 'Hydropower.org: Kyrgyz hydropower overview') + ', ' + LINK('https://www.waterpowermagazine.com/?p=30698', 'Water Power Magazine: Toktogul')),
  ('Около 90% электричества Кыргызстана — ГЭС —', 'About 90% of Kyrgyzstan’s electricity is hydro —', LINK('https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2022/Dec/IRENA_RRA_Kyrgyz_Republic_Summary_2022.pdf', 'IRENA: Kyrgyz Republic summary 2022') + ', ' + LINK('https://en.kabar.kg/news/hydropower-provides-90-of-kyrgyzstans-electricity/', 'Kabar, 10.12.2025')),
  ('Трансформатор, потери в линиях, P = ρgQHη —', 'The transformer, line losses, P = ρgQHη —', LINK('https://openstax.org/books/university-physics-volume-2/pages/15-introduction', 'OpenStax University Physics, Vol. 2, гл. 15') + ', ' + LINK('https://en.wikipedia.org/wiki/Hydroelectricity', 'Wikipedia: Hydroelectricity'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Напор 130 м в задаче 2, сопротивление линии и значения параметров моделей — условные; мощности станций каскада — проектные.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The 130 m head in problem 2, the line resistance and the model parameters are assumed; the cascade capacities are design values.'),
 prev=('23-induction.html', 'Глава 23 · Электромагнитная индукция', 'Chapter 23 · Electromagnetic induction'),
 next=('25-oscillations.html', 'Глава 25 · Колебания', 'Chapter 25 · Oscillations'),
 js=js)
build(c)
