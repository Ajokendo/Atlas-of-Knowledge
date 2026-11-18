# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ЭЛЕКТРОЛИЗ: ПОКРЫТИЕ МЕТАЛЛОМ', 'ELECTROLYSIS: METAL PLATING', 'elSvg', '0 0 600 260',
  select('em', 'Металл', 'Metal') + slider('ei', 'Сила тока', 'Current', 0.1, 5, 0.1, 2) + slider('et', 'Время', 'Time', 1, 120, 1, 30),
  stats([('eQ', 'Прошёл заряд', 'Charge passed'), ('eM', 'Осело металла', 'Metal deposited'), ('eD', 'Слой на 100 см²', 'Layer on 100 cm²')]),
  'elFb', 'Схема условная: масса m = M·I·t/(z·F), F = 96 485 Кл/моль; слой считается равномерным по площади 100 см².',
  'A schematic drawing: the mass m = M·I·t/(z·F), F = 96,485 C/mol; the layer is taken as uniform over an area of 100 cm².')
s1 = section('electrolysis', 'Ток в растворах: электролиз', 'Current in solutions: electrolysis',
 bd('<p>В растворах солей, кислот и щелочей ток создают <strong>ионы</strong> — заряженные частицы, на которые распадаются молекулы при растворении. Такие растворы называют <strong>электролитами</strong>. Положительные ионы идут к отрицательному электроду, отрицательные — к положительному. На электродах вещество выделяется: этот процесс называют <strong>электролизом</strong>.</p><p>Масса вещества, выделившегося на электроде, пропорциональна прошедшему заряду (закон Фарадея):</p>',
    '<p>In solutions of salts, acids and alkalis the current is made by <strong>ions</strong> — charged particles into which molecules break up when they dissolve. Such solutions are called <strong>electrolytes</strong>. Positive ions go to the negative electrode, negative ones to the positive electrode. Substance is deposited on the electrodes: this process is called <strong>electrolysis</strong>.</p><p>The mass of a substance deposited on an electrode is proportional to the charge passed (Faraday’s law):</p>')
 + formula('m = k · I · t,   k = M / (z · F)', 'M — молярная масса, z — заряд иона, F = 96 485 Кл/моль — постоянная Фарадея', 'M is the molar mass, z the ion’s charge, F = 96,485 C/mol the Faraday constant')
 + bd('<p>Электролиз используют для нанесения защитных и декоративных покрытий (никелирование, меднение, серебрение), получения алюминия и очистки меди.</p>',
      '<p>Electrolysis is used for protective and decorative coatings (nickel, copper and silver plating), for producing aluminium and for refining copper.</p>'),
 lab1)

lab2 = model(2, 'ПРОВОДИМОСТЬ РАСТВОРА', 'CONDUCTIVITY OF A SOLUTION', 'cdSvg', '0 0 600 240',
  slider('cs', 'Соли в воде', 'Salt in the water', 0, 35, 1, 10),
  stats([('cG', 'Удельная проводимость', 'Conductivity'), ('cR', 'Сопротивление ячейки', 'Cell resistance'), ('cI', 'Ток от 12 В', 'Current from 12 V')]),
  'cdFb', 'Схема условная: ячейка 5 см × 10 см². Проводимость взята приблизительно пропорциональной концентрации (морская вода, 35 г/л, около 5 См/м; чистая вода около 5,5·10⁻⁶ См/м).',
  'A schematic drawing: a cell 5 cm × 10 cm². The conductivity is taken approximately proportional to the concentration (seawater, 35 g/L, about 5 S/m; pure water about 5.5·10⁻⁶ S/m).')
s2 = section('solutions', 'Почему вода проводит ток', 'Why water conducts current',
 bd('<p>Чистая вода почти не проводит ток: в ней мало ионов. Стоит растворить соль — и проводимость вырастает в сотни тысяч раз, потому что появляются свободные ионы. Обычная водопроводная вода тоже содержит растворённые соли, поэтому проводит ток достаточно хорошо — этим объясняется опасность электроприборов рядом с водой (глава 20).</p>',
    '<p>Pure water hardly conducts current: it has few ions. Dissolve some salt and the conductivity rises hundreds of thousands of times because free ions appear. Ordinary tap water also contains dissolved salts, so it conducts well enough — this explains the danger of electrical appliances near water (chapter 20).</p>'),
 lab2)

lab3 = model(3, 'ИСКРА В ГОРАХ', 'A SPARK IN THE MOUNTAINS', 'gsSvg', '0 0 600 250',
  slider('gh', 'Высота над уровнем моря', 'Altitude above sea level', 0, 5000, 100, 0) + slider('gd', 'Искровой промежуток', 'Spark gap', 1, 20, 1, 5),
  stats([('gP', 'Давление воздуха', 'Air pressure'), ('gE', 'Пробой при E', 'Breakdown at E'), ('gU', 'Пробивное напряжение', 'Breakdown voltage')]),
  'gsFb', 'Схема условная: считаем, что напряжённость пробоя воздуха пропорциональна давлению (E ≈ 3 МВ/м при 101,3 кПа). Закон Пашена точнее, но сложнее.',
  'A schematic drawing: the breakdown field of air is taken proportional to pressure (E ≈ 3 MV/m at 101.3 kPa). Paschen’s law is more exact but more complicated.')
s3 = section('gas', 'Ток в газах: разряд', 'Current in gases: discharge',
 bd('<p>Газы в обычных условиях — изоляторы: ионов в них очень мало. Но если поле сильное, газ <strong>ионизуется</strong>: ионы и электроны разгоняются и выбивают новые, возникает самостоятельный <strong>газовый разряд</strong>. Это искра, молния, свечение в неоновых трубках и лампах дневного света, электрическая дуга сварки.</p><p>Чем меньше давление газа, тем легче его ионизовать. На высоте воздух разрежен, и пробой наступает при меньшем напряжении, чем у моря. Поэтому высоковольтное оборудование в горах требует большего зазора и особой изоляции.</p>',
    '<p>Gases are insulators under ordinary conditions: there are very few ions in them. But if the field is strong the gas becomes <strong>ionized</strong>: ions and electrons are accelerated and knock out new ones, and a self-sustained <strong>gas discharge</strong> appears. This is a spark, lightning, the glow of neon tubes and fluorescent lamps, a welding arc.</p><p>The lower the gas pressure, the easier it is to ionize. At altitude the air is thin, and breakdown occurs at a lower voltage than at sea level. That is why high-voltage equipment in the mountains needs a larger gap and special insulation.</p>'),
 lab3)

tasks = [
 task(1, 'Меднение', 'Copper plating', 'Какая масса меди выделится при токе 2 А за 30 минут? M = 63,5 г/моль, z = 2, F = 96 485 Кл/моль.', 'What mass of copper is deposited by a current of 2 A in 30 minutes? M = 63.5 g/mol, z = 2, F = 96,485 C/mol.',
  'I = 2 А, t = 1800 с', 'I = 2 A, t = 1,800 s', 'q = I·t = 2 · 1800 = 3600 Кл.<br>m = M·q / (z·F) = 63,5 · 3600 / (2 · 96 485) ≈ 1,18 г.', 'q = I·t = 2 · 1,800 = 3,600 C.<br>m = M·q / (z·F) = 63.5 · 3,600 / (2 · 96,485) ≈ 1.18 g.',
  'около 1,2 г меди.', 'about 1.2 g of copper.', True),
 task(2, 'Толщина слоя', 'Thickness of the layer', 'Эти 1,18 г меди равномерно покрыли площадь 100 см². Какова толщина слоя? Плотность меди 8,96 г/см³.', 'These 1.18 g of copper uniformly covered an area of 100 cm². What is the layer’s thickness? The density of copper is 8.96 g/cm³.',
  'm = 1,18 г, S = 100 см², ρ = 8,96 г/см³', 'm = 1.18 g, S = 100 cm², ρ = 8.96 g/cm³', 'V = m / ρ = 1,18 / 8,96 ≈ 0,132 см³.<br>d = V / S = 0,132 / 100 = 1,3·10⁻³ см = 13 мкм.', 'V = m / ρ = 1.18 / 8.96 ≈ 0.132 cm³.<br>d = V / S = 0.132 / 100 = 1.3·10⁻³ cm = 13 µm.',
  'около 13 мкм — тоньше человеческого волоса.', 'about 13 µm — thinner than a human hair.'),
 task(3, 'Серебрение', 'Silver plating', 'Сколько времени нужно, чтобы выделить 1 г серебра при токе 0,5 А? M = 107,9 г/моль, z = 1.', 'How long does it take to deposit 1 g of silver at 0.5 A? M = 107.9 g/mol, z = 1.',
  'm = 1 г, I = 0,5 А', 'm = 1 g, I = 0.5 A', 't = m·z·F / (M·I) = 1 · 1 · 96 485 / (107,9 · 0,5) ≈ 1788 с.', 't = m·z·F / (M·I) = 1 · 1 · 96,485 / (107.9 · 0.5) ≈ 1,788 s.',
  'около 30 минут.', 'about 30 minutes.'),
 task(4, 'Солёная ячейка', 'A salty cell', 'Ячейка длиной 5 см и площадью сечения 10 см² заполнена раствором с удельной проводимостью 1,43 См/м. Найдите её сопротивление и ток при 12 В.', 'A cell 5 cm long with a cross-section of 10 cm² is filled with a solution of conductivity 1.43 S/m. Find its resistance and the current at 12 V.',
  'l = 0,05 м, S = 10⁻³ м², σ = 1,43 См/м, U = 12 В', 'l = 0.05 m, S = 10⁻³ m², σ = 1.43 S/m, U = 12 V', 'R = l / (σ·S) = 0,05 / (1,43 · 10⁻³) ≈ 35 Ом.<br>I = U / R = 12 / 35 ≈ 0,34 А.', 'R = l / (σ·S) = 0.05 / (1.43 · 10⁻³) ≈ 35 Ω.<br>I = U / R = 12 / 35 ≈ 0.34 A.',
  '35 Ом и 0,34 А.', '35 Ω and 0.34 A.'),
 task(5, 'Пробой на перевале', 'Breakdown at a pass', 'На перевале Төө-Ашуу давление воздуха около 65 кПа. Оцените, при каком напряжении пробьётся зазор 1 мм, если у моря (101,3 кПа) пробой при E = 3 МВ/м.', 'At the Töö-Ashuu pass the air pressure is about 65 kPa. Estimate the voltage at which a 1 mm gap breaks down, if at sea level (101.3 kPa) breakdown occurs at E = 3 MV/m.',
  'p = 65 кПа, d = 1 мм', 'p = 65 kPa, d = 1 mm', 'E ≈ 3 · 65 / 101,3 ≈ 1,9 МВ/м.<br>U = E·d = 1,9·10⁶ · 0,001 ≈ 1900 В.', 'E ≈ 3 · 65 / 101.3 ≈ 1.9 MV/m.<br>U = E·d = 1.9·10⁶ · 0.001 ≈ 1,900 V.',
  'около 1,9 кВ, на треть меньше, чем у моря (3 кВ).', 'about 1.9 kV, a third less than at sea level (3 kV).'),
 task(6, 'Моль меди', 'A mole of copper', 'Сколько времени нужно при токе 10 А, чтобы выделить один моль меди (63,5 г)? Для Cu²⁺ нужно 2 моль электронов.', 'How long does it take at 10 A to deposit one mole of copper (63.5 g)? For Cu²⁺ 2 moles of electrons are needed.',
  'z = 2, I = 10 А', 'z = 2, I = 10 A', 'q = z·F = 2 · 96 485 = 192 970 Кл.<br>t = q / I = 192 970 / 10 ≈ 19 300 с ≈ 5,4 ч.', 'q = z·F = 2 · 96,485 = 192,970 C.<br>t = q / I = 192,970 / 10 ≈ 19,300 s ≈ 5.4 h.',
  'около 5,4 часа.', 'about 5.4 hours.'),
]

quiz = [
 ('Что создаёт ток в растворе соли?', [('Свободные электроны', 'В растворах переносчики — ионы.'), ('Ионы', 'Верно.'), ('Молекулы воды', 'Нейтральные молекулы ток не переносят.')],
  'What makes the current in a salt solution?', [('Free electrons', 'In solutions the carriers are ions.'), ('Ions', 'Correct.'), ('Water molecules', 'Neutral molecules do not carry current.')], 1),
 ('Что такое электролиз?', [('Выделение вещества на электродах при прохождении тока через раствор', 'Верно.'), ('Нагревание раствора', 'Нагрев — побочный эффект.'), ('Растворение соли в воде', 'Это просто растворение.')],
  'What is electrolysis?', [('Deposition of substance on electrodes when current passes through a solution', 'Correct.'), ('Heating a solution', 'Heating is a side effect.'), ('Dissolving salt in water', 'That is mere dissolving.')], 0),
 ('Как масса выделившегося вещества зависит от прошедшего заряда?', [('Прямо пропорциональна', 'Верно: m = k·q.'), ('Обратно пропорциональна', 'С ростом заряда масса растёт.'), ('Не зависит', 'Зависит прямо.')],
  'How does the deposited mass depend on the charge passed?', [('Directly proportional', 'Correct: m = k·q.'), ('Inversely proportional', 'The mass grows as the charge grows.'), ('Independent', 'It depends directly.')], 0),
 ('Для чего применяют электролиз?', [('Для нанесения металлических покрытий', 'Верно: никелирование, серебрение, меднение.'), ('Для охлаждения воздуха', 'Это не связано с электролизом.'), ('Для измерения скорости', 'Не связано.')],
  'What is electrolysis used for?', [('For applying metal coatings', 'Correct: nickel, silver, copper plating.'), ('For cooling air', 'Unrelated to electrolysis.'), ('For measuring speed', 'Unrelated.')], 0),
 ('Почему дистиллированная вода почти не проводит ток?', [('В ней очень мало ионов', 'Верно.'), ('Она слишком холодная', 'Дело в числе ионов.'), ('Она слишком тяжёлая', 'Дело не в массе.')],
  'Why does distilled water hardly conduct current?', [('It has very few ions', 'Correct.'), ('It is too cold', 'It is a matter of the number of ions.'), ('It is too heavy', 'Mass is not the point.')], 0),
 ('Что такое газовый разряд?', [('Прохождение тока через ионизованный газ', 'Верно: искра, молния, неоновая трубка.'), ('Остывание газа', 'Не связано с током.'), ('Сжатие газа', 'Не связано.')],
  'What is a gas discharge?', [('Passage of current through an ionized gas', 'Correct: a spark, lightning, a neon tube.'), ('Cooling of a gas', 'Unrelated to current.'), ('Compression of a gas', 'Unrelated.')], 0),
 ('Как давление влияет на пробой воздуха?', [('Чем меньше давление, тем ниже напряжение пробоя', 'Верно: в разреженном воздухе пробой легче.'), ('Чем меньше давление, тем выше напряжение пробоя', 'Всё наоборот (в рассматриваемом диапазоне).'), ('Не влияет', 'Давление влияет.')],
  'How does pressure affect the breakdown of air?', [('The lower the pressure, the lower the breakdown voltage', 'Correct: breakdown is easier in thin air.'), ('The lower the pressure, the higher the breakdown voltage', 'It is the other way round (in the range considered).'), ('It does not affect', 'Pressure does affect it.')], 0),
 ('Что светится в неоновой трубке?', [('Ионизованный газ при разряде', 'Верно.'), ('Раскалённая нить', 'Это лампа накаливания.'), ('Жидкость', 'Это газ.')],
  'What glows in a neon tube?', [('Ionized gas during a discharge', 'Correct.'), ('A hot filament', 'That is an incandescent lamp.'), ('A liquid', 'It is a gas.')], 0),
]

js = r'''
const T={ru:{
 elLabel:"Ванна с раствором, два электрода и слой металла",cdLabel:"Ячейка с раствором соли",gsLabel:"График пробивного напряжения против высоты",
 mets:["Медь","Серебро","Никель","Алюминий"],
 elFb:"Больше тока и времени — больше металла. Масса пропорциональна заряду.",
 cdFb:"Чем больше соли, тем больше ионов и тем выше проводимость.",
 gsFb:"Чем выше, тем разреженнее воздух и тем легче пробой."},
 en:{
 elLabel:"A bath with solution, two electrodes and a layer of metal",cdLabel:"A cell with a salt solution",gsLabel:"A graph of the breakdown voltage against altitude",
 mets:["Copper","Silver","Nickel","Aluminium"],
 elFb:"More current and time — more metal. The mass is proportional to the charge.",
 cdFb:"The more salt, the more ions and the higher the conductivity.",
 gsFb:"The higher up, the thinner the air and the easier the breakdown."}};
const MM=[63.55,107.87,58.69,26.98],ZZ=[2,1,2,3],DN=[8.96,10.49,8.91,2.70],FA=96485,COL=["#b87333","#c0c0c0","#8f9aa5","#b5b5b5"];
function drawEl(){const t=tt(),i=+$("em").value,I=+$("ei").value,s=+$("et").value*60,q=I*s,m=MM[i]*q/(ZZ[i]*FA),d=m/DN[i]/100*1e4;
 let g='<path d="M120 60 L130 220 L470 220 L480 60" fill="none" stroke="#18181a" stroke-width="3"/><rect x="132" y="110" width="336" height="108" fill="#cfe3ef"/>';
 g+='<rect x="190" y="50" width="16" height="140" fill="#9a9a9a" stroke="#18181a"/><rect x="394" y="50" width="16" height="140" fill="#9a9a9a" stroke="#18181a"/>';
 const th=Math.min(14,1+d/4);
 g+='<rect x="'+(394-th)+'" y="70" width="'+th+'" height="120" fill="'+COL[i]+'" stroke="#18181a"/>';
 g+=svgText(198,40,"+","#b6533f","middle",18)+svgText(402,40,"−","#3f5f8f","middle",18);
 for(let k=0;k<10;k++){const x=225+k*16;g+='<circle cx="'+(x+(k%2)*80)+'" cy="'+(130+(k*17)%70)+'" r="4" fill="'+COL[i]+'"/>'}
 g+=arrow(240,100,380,100,"#18181a",2);
 $("elSvg").innerHTML=g;
 $("eiOut").textContent=fmt(I,1)+" A";$("etOut").textContent=+$("et").value+UN[lang].min;
 $("eQ").textContent=num(Math.round(q))+(lang==="ru"?" Кл":" C");
 $("eM").textContent=fmt(m,2)+UN[lang].g;
 $("eD").textContent=fmt(d,1)+(lang==="ru"?" мкм":" µm");$("elFb").textContent=t.elFb}
["em","ei","et"].forEach(id=>$(id).addEventListener("input",drawEl));
function drawCd(){const t=tt(),c=+$("cs").value,sg=5.5e-6+0.143*c,R=0.05/(sg*1e-3),I=12/R;
 let g='<rect x="150" y="60" width="300" height="130" fill="#cfe3ef" stroke="#18181a" stroke-width="3"/><rect x="170" y="40" width="14" height="140" fill="#9a9a9a" stroke="#18181a"/><rect x="416" y="40" width="14" height="140" fill="#9a9a9a" stroke="#18181a"/>';
 const n=Math.round(c*1.2)+1;
 for(let k=0;k<n;k++){const x=195+((k*53)%210),y=75+((k*37)%100);g+='<circle cx="'+x+'" cy="'+y+'" r="4" fill="'+(k%2?"#b6533f":"#3f5f8f")+'"/>'}
 g+=svgText(300,215,c+(lang==="ru"?" г/л":" g/L"),"#66666b","middle",12);
 $("cdSvg").innerHTML=g;
 $("csOut").textContent=c+(lang==="ru"?" г/л":" g/L");
 $("cG").textContent=sg<0.01?(sg*1e6).toFixed(1).replace(".",lang==="ru"?",":".")+(lang==="ru"?" мкСм/м":" µS/m"):fmt(sg,2)+(lang==="ru"?" См/м":" S/m");
 $("cR").textContent=R>=1e6?fmt(R/1e6,1)+(lang==="ru"?" МОм":" MΩ"):R>=1000?fmt(R/1000,1)+(lang==="ru"?" кОм":" kΩ"):fmt(R,1)+(lang==="ru"?" Ом":" Ω");
 $("cI").textContent=I<1e-3?fmt(I*1e6,1)+(lang==="ru"?" мкА":" µA"):I<1?fmt(I*1e3,1)+(lang==="ru"?" мА":" mA"):fmt(I,2)+(lang==="ru"?" А":" A");
 $("cdFb").textContent=t.cdFb}
$("cs").addEventListener("input",drawCd);
function Pair(h){return 101325*Math.pow(1-2.25577e-5*h,5.25588)}
function drawGs(){const t=tt(),h=+$("gh").value,d=+$("gd").value/1000,p=Pair(h),Eb=3e6*p/101325,U=Eb*d;
 const X=v=>60+v/5000*480,Y=u=>230-u/60*190;
 let g='<line x1="60" y1="230" x2="540" y2="230" stroke="#18181a"/><line x1="60" y1="230" x2="60" y2="40" stroke="#18181a"/>';
 for(let k=0;k<=5;k++)g+='<line x1="'+X(k*1000)+'" y1="230" x2="'+X(k*1000)+'" y2="40" stroke="#e3e1da"/>'+svgText(X(k*1000),246,k*1000,"#66666b","middle",10);
 for(let u=0;u<=60;u+=10)g+='<line x1="60" y1="'+Y(u)+'" x2="540" y2="'+Y(u)+'" stroke="#e3e1da"/>'+svgText(54,Y(u)+4,u,"#66666b","end",10);
 g+='<polyline fill="none" stroke="#2f6f5d" stroke-width="3" points="'+Array.from({length:51},(_,k)=>X(k*100)+","+Y(3e6*Pair(k*100)/101325*d/1000)).join(" ")+'"/>';
 g+='<circle cx="'+X(h)+'" cy="'+Y(U/1000)+'" r="6" fill="#b6533f"/>'+svgText(60,30,"U, kV","#18181a","start",11)+svgText(540,262,"h, "+(lang==="ru"?"м":"m"),"#18181a","end",11);
 $("gsSvg").innerHTML=g;
 $("ghOut").textContent=num(h)+(lang==="ru"?" м":" m");$("gdOut").textContent=+$("gd").value+(lang==="ru"?" мм":" mm");
 $("gP").textContent=fmt(p/1000,1)+(lang==="ru"?" кПа":" kPa");$("gE").textContent=fmt(Eb/1e6,2)+(lang==="ru"?" МВ/м":" MV/m");$("gU").textContent=fmt(U/1000,1)+(lang==="ru"?" кВ":" kV");$("gsFb").textContent=t.gsFb}
["gh","gd"].forEach(id=>$(id).addEventListener("input",drawGs));
const LAB={ru:{elSvg:T.ru.elLabel,cdSvg:T.ru.cdLabel,gsSvg:T.ru.gsLabel},en:{elSvg:T.en.elLabel,cdSvg:T.en.cdLabel,gsSvg:T.en.gsLabel}};
function drawAll(){fillSel("em",T[lang].mets,0);drawEl();drawCd();drawGs()}
'''

c = dict(n='19', slug='19-conduction-in-media.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Ток в жидкостях и газах', 'Current in liquids and gases'),
 desc='Глава 19 Атласа физики: электролиты, электролиз и закон Фарадея, проводимость растворов, газовый разряд.',
 lead=('Чистая вода почти не проводит ток, а солёная проводит хорошо; воздух изолятор, но в нём бывает молния. Ионы, электролиз и газовый разряд.',
       'Pure water hardly conducts current while salt water conducts well; air is an insulator, yet lightning occurs in it. Ions, electrolysis and gas discharge.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('electrolysis', 'Электролиз', 'Electrolysis'), ('solutions', 'Проводимость воды', 'Conductivity of water'), ('gas', 'Газовый разряд', 'Gas discharge'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Лабораторные измерения показывают: дистиллированная вода практически не проводит ток. А обычная вода из-под крана или солёная вода озера проводит так хорошо, что опасно оставлять электроприбор рядом с ванной.</p><p>Чем отличается солёная вода от чистой и почему от этого зависит ток?</p>',
         '<p>Laboratory measurements show that distilled water practically does not conduct current. Yet ordinary tap water or salt water from a lake conducts so well that it is dangerous to leave an electrical appliance near a bath.</p><p>How does salt water differ from pure water and why does the current depend on that?</p>'),
 hint=('Подсказку даст модель «Проводимость раствора». Разгадка — в конце главы.', 'The “Conductivity of a solution” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: роль ионов', 'The answer: the role of ions'),
 answer=('<p>Ток в жидкости — это движение заряженных частиц. В чистой воде их почти нет: лишь ничтожная доля молекул распадается на ионы. Когда в воду попадает соль, её кристаллы растворяются и распадаются на положительные и отрицательные ионы (например, Na⁺ и Cl⁻). Эти ионы свободно перемещаются в электрическом поле и переносят заряд, поэтому проводимость растёт в сотни тысяч раз (модель 2).</p><p>В водопроводной воде и тем более в озёрной всегда есть растворённые соли, поэтому для электробезопасности вода не считается изолятором — и человеку в воде ток передаётся легко (глава 20).</p>',
         '<p>Current in a liquid is the motion of charged particles. In pure water there are hardly any: only a tiny fraction of molecules break up into ions. When salt gets into water its crystals dissolve and split into positive and negative ions (for example Na⁺ and Cl⁻). These ions move freely in an electric field and carry charge, so the conductivity rises hundreds of thousands of times (model 2).</p><p>Tap water, and still more lake water, always contains dissolved salts, so for electrical safety water is not considered an insulator — and current passes readily to a person in water (chapter 20).</p>'),
 sources=[
  ('Электролиз, закон Фарадея, постоянная Фарадея F = 96 485 Кл/моль —', 'Electrolysis, Faraday’s law, the Faraday constant F = 96,485 C/mol —', LINK('https://physics.nist.gov/cgi-bin/cuu/Value?f', 'NIST: Faraday constant') + ', ' + LINK('https://en.wikipedia.org/wiki/Faraday%27s_laws_of_electrolysis', 'Wikipedia: Faraday’s laws of electrolysis')),
  ('Плотности металлов —', 'Densities of metals —', LINK('https://www.engineeringtoolbox.com/metal-alloys-densities-d_50.html', 'Engineering ToolBox: Metals and alloys densities')),
  ('Проводимость воды (чистая вода, морская вода) —', 'Conductivity of water (pure water, seawater) —', LINK('https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity', 'Wikipedia: Electrical resistivity and conductivity') + ', ' + LINK('https://en.wikipedia.org/wiki/Seawater', 'Wikipedia: Seawater')),
  ('Газовый разряд, закон Пашена —', 'Gas discharge, Paschen’s law —', LINK('https://en.wikipedia.org/wiki/Paschen%27s_law', 'Wikipedia: Paschen’s law')),
  ('Давление воздуха на высоте — как в главе 4 и 11 —', 'Air pressure at altitude — as in chapters 4 and 11 —', LINK('https://aty.sdsu.edu/explain/thermal/std_atm.html', 'The Standard Atmosphere'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Линейная зависимость проводимости от концентрации и пропорциональность пробоя давлению — упрощения для учебной модели.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The linear dependence of conductivity on concentration and the proportionality of breakdown to pressure are simplifications for the teaching model.'),
 prev=('18-electric-power.html', 'Глава 18 · Работа и мощность тока', 'Chapter 18 · Work and power of current'),
 next=('20-electrical-safety.html', 'Глава 20 · Электробезопасность', 'Chapter 20 · Electrical safety'),
 js=js)
build(c)
