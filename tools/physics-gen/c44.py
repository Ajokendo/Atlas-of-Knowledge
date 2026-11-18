# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'УРАВНЕНИЕ СОСТОЯНИЯ p·V = n·R·T', 'THE EQUATION OF STATE p·V = n·R·T', 'gsSvg', '0 0 600 250',
  slider('gn', 'Количество газа', 'Amount of gas', 0.1, 5, 0.1, 1) + slider('gt', 'Температура', 'Temperature', 200, 600, 5, 300) + slider('gv', 'Объём сосуда', 'Volume of the vessel', 5, 100, 1, 25),
  stats([('gP', 'Давление p = nRT/V', 'Pressure p = nRT/V'), ('gA', 'В атмосферах (1 атм = 101,3 кПа)', 'In atmospheres (1 atm = 101.3 kPa)'), ('gN', 'Число молекул N = n·N_A', 'Number of molecules N = n·N_A')]),
  'gsFb', 'Схема условная: идеальный газ; R = 8,314 Дж/(моль·К), N_A = 6,02·10²³ 1/моль; температура в кельвинах (T = t + 273).',
  'A schematic drawing: an ideal gas; R = 8.314 J/(mol·K), N_A = 6.02·10²³ 1/mol; temperature in kelvins (T = t + 273).')
s1 = section('state', 'Уравнение состояния идеального газа', 'The equation of state of an ideal gas',
 bd('<p>Газ при небольшом давлении ведёт себя как <strong>идеальный</strong>: молекулы — точки, которые не притягиваются, а только упруго сталкиваются со стенками. Четыре величины — давление <em>p</em>, объём <em>V</em>, температура <em>T</em> (в кельвинах!) и количество вещества <em>n</em> (в молях) — связаны одним уравнением. Один моль содержит <em>N<sub>A</sub> = 6,02·10²³</em> молекул.</p>',
    '<p>A gas at modest pressure behaves as an <strong>ideal</strong> one: the molecules are points that do not attract each other and only collide elastically with the walls. Four quantities — the pressure <em>p</em>, volume <em>V</em>, temperature <em>T</em> (in kelvins!) and the amount of substance <em>n</em> (in moles) — are tied by one equation. One mole holds <em>N<sub>A</sub> = 6.02·10²³</em> molecules.</p>')
 + formula('p · V = n · R · T', 'при n = const: p·V/T = const; при T = const (закон Бойля–Мариотта) p·V = const', 'for n = const: p·V/T = const; at T = const (Boyle’s law) p·V = const')
 + bd('<p>Один моль газа при 0 °C (273 К) и 101,3 кПа занимает около 22,4 л — это можно проверить в модели 1.</p>',
      '<p>One mole of gas at 0 °C (273 K) and 101.3 kPa occupies about 22.4 L — you can check it in model 1.</p>'),
 lab1)

lab2 = model(2, 'ШИНА И ТЕМПЕРАТУРА', 'A TYRE AND TEMPERATURE', 'tySvg', '0 0 600 250',
  slider('yp', 'Давление при 20 °C (абсолютное)', 'Pressure at 20 °C (absolute)', 150, 400, 5, 300) + slider('yt', 'Температура воздуха', 'Air temperature', -30, 50, 1, -20),
  stats([('yP', 'Давление в шине p₂ = p₁·T₂/T₁', 'Tyre pressure p₂ = p₁·T₂/T₁'), ('yD', 'Изменение давления', 'Change in pressure')]),
  'tyFb', 'Схема условная: объём шины считается постоянным, воздух — идеальным газом; T = t + 273.',
  'A schematic drawing: the tyre volume is taken as constant, the air as an ideal gas; T = t + 273.')
s2 = section('processes', 'Газовые процессы', 'Gas processes',
 bd('<p>Три простых процесса — частные случаи уравнения состояния. <strong>Изотермический</strong> (T = const): сжимаем газ вдвое — давление вдвое больше (шприц с закрытым носиком). <strong>Изобарный</strong> (p = const): V/T = const — нагретый воздух расширяется и в воздушном шаре становится «легче». <strong>Изохорный</strong> (V = const): p/T = const — поэтому зимой давление в шинах падает, а в закрытой банке на огне растёт.</p>',
    '<p>Three simple processes are special cases of the equation of state. <strong>Isothermal</strong> (T = const): compress a gas to half the volume — the pressure doubles (a syringe with the nozzle closed). <strong>Isobaric</strong> (p = const): V/T = const — heated air expands and in a balloon becomes “lighter”. <strong>Isochoric</strong> (V = const): p/T = const — so in winter the tyre pressure drops while in a closed can over a fire it rises.</p>')
 + formula('p₁/T₁ = p₂/T₂ (V = const)', 'температуру обязательно переводить в кельвины: 20 °C = 293 К', 'the temperature must be converted to kelvins: 20 °C = 293 K'),
 lab2)

lab3 = model(3, 'ГАЗ ИЗНУТРИ: СКОРОСТЬ МОЛЕКУЛ', 'A GAS FROM INSIDE: MOLECULE SPEED', 'kiSvg', '0 0 600 250',
  select('kg', 'Газ', 'Gas') + slider('kt', 'Температура', 'Temperature', 100, 1000, 10, 300),
  stats([('kV', 'Средняя квадратичная скорость v = √(3RT/M)', 'Root-mean-square speed v = √(3RT/M)'), ('kE', 'Средняя кинетическая энергия молекулы 3kT/2', 'Mean kinetic energy of a molecule 3kT/2')]),
  'kiFb', 'Схема условная: стрелки показывают скорость молекул, их длина — условна; k = 1,38·10⁻²³ Дж/К.',
  'A schematic drawing: the arrows show the speed of molecules, their length is schematic; k = 1.38·10⁻²³ J/K.')
s3 = section('kinetic', 'Давление и температура — это движение молекул', 'Pressure and temperature are molecular motion',
 bd('<p>Давление газа — результат ударов молекул о стенку: <em>p = (1/3)·n·m·v²</em> (<em>n</em> — число молекул в единице объёма). Сравнив с <em>p·V = N·k·T</em>, получаем смысл температуры: средняя кинетическая энергия поступательного движения молекулы <em>E = 3kT/2</em> зависит только от температуры, а не от сорта газа. Лёгкие молекулы при той же энергии быстрее: водород при 300 К — около 1,9 км/с, азот — около 0,5 км/с.</p>',
    '<p>Gas pressure results from molecules hitting the wall: <em>p = (1/3)·n·m·v²</em> (<em>n</em> is the number of molecules per unit volume). Comparing with <em>p·V = N·k·T</em> gives the meaning of temperature: the mean kinetic energy of translational motion of a molecule <em>E = 3kT/2</em> depends only on temperature, not on the kind of gas. Light molecules at the same energy are faster: hydrogen at 300 K — about 1.9 km/s, nitrogen — about 0.5 km/s.</p>')
 + formula('E = 3kT/2,   v = √(3RT / M)', 'M — молярная масса в кг/моль (азот 0,028)', 'M is the molar mass in kg/mol (nitrogen 0.028)'),
 lab3)

tasks = [
 task(1, 'Давление в баллоне', 'Pressure in a cylinder', 'В сосуде объёмом 50 л находится 2 моль газа при 300 К. Найдите давление. (R = 8,314 Дж/(моль·К).)', 'A vessel of 50 L contains 2 mol of gas at 300 K. Find the pressure. (R = 8.314 J/(mol·K).)',
  'n = 2 моль, T = 300 К, V = 0,05 м³', 'n = 2 mol, T = 300 K, V = 0.05 m³', 'p = nRT / V = 2 · 8,314 · 300 / 0,05 = 4988 / 0,05 ≈ 99 800 Па.', 'p = nRT / V = 2 · 8.314 · 300 / 0.05 = 4,988 / 0.05 ≈ 99,800 Pa.', '≈ 100 кПа — около одной атмосферы.', '≈ 100 kPa — about one atmosphere.', True),
 task(2, 'Закон Бойля–Мариотта', 'Boyle’s law', 'Газ при 100 кПа занимал 6 л. Его сжали до 3 л при постоянной температуре. Каково давление?', 'A gas at 100 kPa occupied 6 L. It was compressed to 3 L at constant temperature. What is the pressure?',
  'p₁ = 100 кПа, V₁ = 6 л, V₂ = 3 л', 'p₁ = 100 kPa, V₁ = 6 L, V₂ = 3 L', 'p₁V₁ = p₂V₂, p₂ = 100 · 6 / 3 = 200 кПа.', 'p₁V₁ = p₂V₂, p₂ = 100 · 6 / 3 = 200 kPa.', '200 кПа.', '200 kPa.'),
 task(3, 'Шина зимой', 'A tyre in winter', 'Абсолютное давление в шине 300 кПа при 20 °C. Каким оно станет при −20 °C (объём не меняется)?', 'The absolute pressure in a tyre is 300 kPa at 20 °C. What will it be at −20 °C (the volume does not change)?',
  'T₁ = 293 К, T₂ = 253 К', 'T₁ = 293 K, T₂ = 253 K', 'p₂ = p₁ · T₂ / T₁ = 300 · 253 / 293 ≈ 259 кПа.', 'p₂ = p₁ · T₂ / T₁ = 300 · 253 / 293 ≈ 259 kPa.', '≈ 259 кПа — на 14% меньше.', '≈ 259 kPa — 14% less.'),
 task(4, 'Бутылка с перевала', 'A bottle from the pass', 'Пустую пластиковую бутылку закрыли на высоте, где давление 66 кПа, и привезли в Бишкек (92 кПа). Изотермически: во сколько раз изменился объём воздуха в ней?', 'An empty plastic bottle was closed at a height where the pressure is 66 kPa and brought to Bishkek (92 kPa). Isothermally: how did the volume of air in it change?',
  'p₁ = 66 кПа, p₂ = 92 кПа', 'p₁ = 66 kPa, p₂ = 92 kPa', 'V₂ / V₁ = p₁ / p₂ = 66 / 92 ≈ 0,72.', 'V₂ / V₁ = p₁ / p₂ = 66 / 92 ≈ 0.72.', 'объём уменьшился до 72% — бутылка сморщится.', 'the volume fell to 72% — the bottle crumples.'),
 task(5, 'Скорость молекул', 'Molecule speed', 'Найдите среднюю квадратичную скорость молекул азота (M = 0,028 кг/моль) и водорода (M = 0,002 кг/моль) при 300 К.', 'Find the rms speed of nitrogen (M = 0.028 kg/mol) and hydrogen (M = 0.002 kg/mol) molecules at 300 K.',
  'T = 300 К', 'T = 300 K', 'v = √(3RT/M).<br>N₂: √(3 · 8,314 · 300 / 0,028) = √(267 000) ≈ 517 м/с.<br>H₂: √(3 · 8,314 · 300 / 0,002) = √(3,74·10⁶) ≈ 1934 м/с.', 'v = √(3RT/M).<br>N₂: √(3 · 8.314 · 300 / 0.028) = √(267,000) ≈ 517 m/s.<br>H₂: √(3 · 8.314 · 300 / 0.002) = √(3.74·10⁶) ≈ 1,934 m/s.', '517 м/с и 1934 м/с.', '517 m/s and 1,934 m/s.'),
 task(6, 'Молекул в литре', 'Molecules in a litre', 'Сколько молекул в 1 л воздуха при 101,3 кПа и 293 К? (k = 1,38·10⁻²³ Дж/К.)', 'How many molecules are there in 1 L of air at 101.3 kPa and 293 K? (k = 1.38·10⁻²³ J/K.)',
  'p = 101 300 Па, V = 10⁻³ м³', 'p = 101,300 Pa, V = 10⁻³ m³', 'N = p·V / (k·T) = 101 300 · 10⁻³ / (1,38·10⁻²³ · 293) = 101,3 / 4,04·10⁻²¹ ≈ 2,5·10²² .', 'N = p·V / (k·T) = 101,300 · 10⁻³ / (1.38·10⁻²³ · 293) = 101.3 / 4.04·10⁻²¹ ≈ 2.5·10²².', 'около 2,5·10²² молекул.', 'about 2.5·10²² molecules.'),
]

quiz = [
 qz('В каких единицах температура входит в уравнение состояния?', 'В кельвинах', 'В градусах Цельсия', 'В градусах Фаренгейта', 'T = t + 273.',
    'In what units does temperature enter the equation of state?', 'Kelvins', 'Degrees Celsius', 'Degrees Fahrenheit', 'T = t + 273.'),
 qz('Что утверждает закон Бойля–Мариотта?', 'При T = const p·V = const', 'При V = const p ~ V', 'p не зависит от V', 'Сжали вдвое — давление вдвое больше.',
    'What does Boyle’s law state?', 'At T = const p·V = const', 'At V = const p ~ V', 'p does not depend on V', 'Compress to half — twice the pressure.'),
 qz('Что происходит с давлением газа в закрытом сосуде при нагревании?', 'Растёт', 'Падает', 'Не меняется', 'p/T = const при V = const.',
    'What happens to the pressure of a gas in a closed vessel when heated?', 'It rises', 'It falls', 'It does not change', 'p/T = const at V = const.'),
 qz('Чему примерно равен объём 1 моль газа при 0 °C и 101,3 кПа?', '22,4 л', '2,24 л', '224 л', 'V = RT/p ≈ 22,4 л.',
    'About what volume does 1 mol of gas occupy at 0 °C and 101.3 kPa?', '22.4 L', '2.24 L', '224 L', 'V = RT/p ≈ 22.4 L.'),
 qz('От чего зависит средняя кинетическая энергия молекулы газа?', 'Только от температуры', 'От сорта газа', 'От объёма сосуда', 'E = 3kT/2.',
    'What does the mean kinetic energy of a gas molecule depend on?', 'Temperature only', 'The kind of gas', 'The volume of the vessel', 'E = 3kT/2.'),
 qz('Какие молекулы при той же температуре быстрее?', 'Лёгкие (водород)', 'Тяжёлые (CO₂)', 'Все одинаково', 'v = √(3RT/M).',
    'Which molecules are faster at the same temperature?', 'Light ones (hydrogen)', 'Heavy ones (CO₂)', 'All equally', 'v = √(3RT/M).'),
 qz('Чему равно число Авогадро N_A?', '6,02·10²³ 1/моль', '6,02·10⁻²³ 1/моль', '602 1/моль', 'Столько молекул в одном моле.',
    'What is Avogadro’s number N_A?', '6.02·10²³ 1/mol', '6.02·10⁻²³ 1/mol', '602 1/mol', 'This many molecules in one mole.'),
 qz('Закрытую бутылку с гор привезли вниз. Что произойдёт?', 'Она сожмётся: наружное давление больше', 'Она раздуется', 'Ничего', 'Внизу давление выше, объём воздуха уменьшается.',
    'A closed bottle is brought down from the mountains. What happens?', 'It crumples: the outside pressure is greater', 'It swells', 'Nothing', 'Below the pressure is higher and the volume of air decreases.'),
]

js = JSL + r'''
const T={ru:{
 gsLabel:"Газ в сосуде",tyLabel:"Давление в шине при разной температуре",kiLabel:"Молекулы газа движутся быстрее при нагревании",
 gases:["Водород H₂","Гелий He","Азот N₂","Кислород O₂","Углекислый газ CO₂"],
 gsFb:"Больше газа или выше температура — больше давление; больше объём — меньше.",tyFb:"На холоде давление в шине падает.",kiFb:"Лёгкие молекулы быстрее тяжёлых."},
 en:{
 gsLabel:"A gas in a vessel",tyLabel:"Tyre pressure at different temperatures",kiLabel:"Gas molecules move faster when heated",
 gases:["Hydrogen H₂","Helium He","Nitrogen N₂","Oxygen O₂","Carbon dioxide CO₂"],
 gsFb:"More gas or a higher temperature — more pressure; a larger volume — less.",tyFb:"In the cold the tyre pressure drops.",kiFb:"Light molecules are faster than heavy ones."}};
const MM=[0.002,0.004,0.028,0.032,0.044];
function drawGs(){const t=tt(),n=+$("gn").value,Tk=+$("gt").value,V=+$("gv").value/1000,p=n*8.314*Tk/V;
 const h=40+(+$("gv").value)/100*140;let g='<rect x="150" y="'+(215-h)+'" width="300" height="'+h+'" fill="none" stroke="#18181a" stroke-width="3"/>';
 const N=Math.min(60,Math.round(n*12));for(let i=0;i<N;i++){const x=160+((i*73)%280),y=215-h+8+((i*47)%Math.max(10,h-16));g+='<circle cx="'+x+'" cy="'+y+'" r="3.5" fill="#3f5f8f"/>'}
 g+=svgText(300,238,"p = "+fmt(p/1000,1)+" "+U("кПа","kPa"),"#18181a","middle",13);
 $("gsSvg").innerHTML=g;$("gnOut").textContent=fmt(n,1)+" "+U("моль","mol");$("gtOut").textContent=Tk+" "+U("К","K")+" ("+(Tk-273)+" °C)";$("gvOut").textContent=Math.round(V*1000)+" "+U("л","L");
 $("gP").textContent=fmt(p/1000,1)+" "+U("кПа","kPa");$("gA").textContent=fmt(p/101325,2)+" "+U("атм","atm");$("gN").textContent=sci(n*6.022e23,2);$("gsFb").textContent=t.gsFb}
["gn","gt","gv"].forEach(id=>$(id).addEventListener("input",drawGs));
function drawTy(){const t=tt(),p1=+$("yp").value,tc=+$("yt").value,p2=p1*(tc+273)/293;
 const r=60+p2/400*35;let g='<circle cx="300" cy="125" r="100" fill="#2a2a2e"/><circle cx="300" cy="125" r="'+r*0.9+'" fill="#e6dfcd" stroke="#18181a"/><circle cx="300" cy="125" r="20" fill="#9a9a9a"/>'+svgText(300,125,fmt(p2,0),"#18181a","middle",16)+svgText(300,236,U("кПа","kPa")+" @ "+tc+" °C","#66666b","middle",12);
 $("tySvg").innerHTML=g;$("ypOut").textContent=p1+" "+U("кПа","kPa");$("ytOut").textContent=tc+" °C";
 $("yP").textContent=fmt(p2,0)+" "+U("кПа","kPa");$("yD").textContent=(p2>=p1?"+":"")+fmt((p2-p1)/p1*100,1)+"%";$("tyFb").textContent=t.tyFb}
["yp","yt"].forEach(id=>$(id).addEventListener("input",drawTy));
function drawKi(){const t=tt(),k=+$("kg").value,Tk=+$("kt").value,v=Math.sqrt(3*8.314*Tk/MM[k]),E=1.5*1.380649e-23*Tk;
 let g='<rect x="100" y="40" width="400" height="170" fill="none" stroke="#18181a" stroke-width="3"/>';
 for(let i=0;i<14;i++){const x=120+((i*89)%360),y=60+((i*53)%130),a=i*2.4,L=Math.min(38,v/60);g+='<circle cx="'+x+'" cy="'+y+'" r="5" fill="#3f5f8f"/>'+arrow(x,y,x+Math.cos(a)*L,y+Math.sin(a)*L,"#b6533f",2)}
 $("kiSvg").innerHTML=g;$("ktOut").textContent=Tk+" "+U("К","K");
 $("kV").textContent=fmt(v,0)+" "+U("м/с","m/s");$("kE").textContent=sci(E,2)+" "+U("Дж","J")+" ("+fmt(E/1.602e-19,3)+" "+U("эВ","eV")+")";$("kiFb").textContent=t.kiFb}
["kg","kt"].forEach(id=>$(id).addEventListener("input",drawKi));
const LAB={ru:{gsSvg:T.ru.gsLabel,tySvg:T.ru.tyLabel,kiSvg:T.ru.kiLabel},en:{gsSvg:T.en.gsLabel,tySvg:T.en.tyLabel,kiSvg:T.en.kiLabel}};
function drawAll(){fillSel("kg",T[lang].gases,2);drawGs();drawTy();drawKi()}
'''

c = dict(n='44', slug='44-ideal-gas.html', block='VIII', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Идеальный газ и газовые законы', 'The ideal gas and gas laws'),
 desc='Глава 44 Атласа физики: уравнение состояния идеального газа pV = nRT, изотермический, изобарный и изохорный процессы, скорость молекул и температура.',
 lead=('Почему бутылка, закрытая в горах, сморщивается внизу, а шины зимой «садятся». Давление и температура как движение молекул.',
       'Why a bottle closed in the mountains crumples below and tyres “go flat” in winter. Pressure and temperature as molecular motion.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('state', 'Уравнение состояния', 'Equation of state'), ('processes', 'Процессы', 'Processes'), ('kinetic', 'Молекулы', 'Molecules'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Вы пьёте воду на высоком перевале и закручиваете пустую пластиковую бутылку. В Бишкеке, внизу, бутылка оказывается сморщенной, хотя никто её не сжимал. А если оставить её в жаркой машине, она, наоборот, раздувается и «стреляет» крышкой.</p><p>Что происходит с воздухом внутри бутылки?</p>',
         '<p>You drink water on a high pass and screw the cap onto the empty plastic bottle. In Bishkek, below, the bottle is crumpled though nobody squeezed it. And if it is left in a hot car it swells instead and “fires” its cap.</p><p>What happens to the air inside the bottle?</p>'),
 hint=stdhint('Шина и температура', 'A tyre and temperature'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: p·V/T = const', 'The answer: p·V/T = const'),
 answer=('<p>В закрытой бутылке количество воздуха не меняется, поэтому <em>p·V/T</em> постоянно. На перевале давление снаружи около 66 кПа, внизу — около 92 кПа. Стенки у бутылки тонкие, и давление внутри быстро сравнивается с наружным: объём воздуха падает примерно до 72% (задача 4) — бутылка сминается.</p><p>В жаркой машине растёт температура — при почти постоянном объёме растёт и давление: <em>p₂ = p₁·T₂/T₁</em>. Нагрев с 20 до 60 °C даёт рост примерно на 14%.</p>',
         '<p>In a closed bottle the amount of air does not change so <em>p·V/T</em> is constant. On the pass the outside pressure is about 66 kPa, below — about 92 kPa. The bottle’s walls are thin and the inside pressure quickly matches the outside: the volume of air falls to about 72% (problem 4) — the bottle is crushed.</p><p>In a hot car the temperature rises — at almost constant volume the pressure rises too: <em>p₂ = p₁·T₂/T₁</em>. Heating from 20 to 60 °C gives a rise of about 14%.</p>'),
 sources=[
  ('Идеальный газ, газовые законы, кинетическая теория —', 'The ideal gas, gas laws, kinetic theory —', LINK('https://openstax.org/books/university-physics-volume-2/pages/2-introduction', 'OpenStax University Physics, Vol. 2, гл. 2') + ', ' + LINK('https://en.wikipedia.org/wiki/Ideal_gas_law', 'Wikipedia: Ideal gas law')),
  ('Давление и высота (стандартная атмосфера) —', 'Pressure and altitude (the standard atmosphere) —', LINK('https://en.wikipedia.org/wiki/Atmospheric_pressure', 'Wikipedia: Atmospheric pressure'))],
 note=stdnote('Давление на перевале (66 кПа) и в Бишкеке (92 кПа) — оценки по стандартной атмосфере; реальное давление зависит от погоды.', 'The pressures at the pass (66 kPa) and in Bishkek (92 kPa) are estimates from the standard atmosphere; the real pressure depends on the weather.'),
 prev=('43-stars-telescopes.html', 'Глава 43 · Звёзды и обсерватории', 'Chapter 43 · Stars and observatories'),
 next=('45-capacitor.html', 'Глава 45 · Конденсатор', 'Chapter 45 · The capacitor'),
 js=js)
build(c)
