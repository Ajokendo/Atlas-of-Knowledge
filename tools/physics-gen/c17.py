# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ЗАКОН ОМА', 'OHM’S LAW', 'omSvg', '0 0 600 260',
  slider('ou', 'Напряжение', 'Voltage', 0, 24, 0.5, 12) + slider('or', 'Сопротивление', 'Resistance', 1, 100, 1, 40),
  stats([('oI', 'Сила тока I = U/R', 'Current I = U/R'), ('oP', 'Наклон графика', 'Slope of the graph')]),
  'omFb', 'Схема условная: график показывает, как сила тока зависит от напряжения при выбранном сопротивлении (линия прямая).',
  'A schematic drawing: the graph shows how current depends on voltage for the chosen resistance (the line is straight).')
s1 = section('ohm', 'Сопротивление и закон Ома', 'Resistance and Ohm’s law',
 bd('<p>Одно и то же напряжение даёт в разных проводниках разный ток. Свойство проводника препятствовать току называют <strong>электрическим сопротивлением</strong> <em>R</em> (единица — ом, Ом). Георг Ом установил: сила тока на участке цепи прямо пропорциональна напряжению и обратно пропорциональна сопротивлению:</p>',
    '<p>The same voltage gives different currents in different conductors. The property of a conductor to hinder current is called <strong>electrical resistance</strong> <em>R</em> (the unit is the ohm, Ω). Georg Ohm established that the current in a part of a circuit is directly proportional to the voltage and inversely proportional to the resistance:</p>')
 + formula('I = U / R', 'U = I · R,  R = U / I;  1 Ом = 1 В / 1 А', 'U = I · R,  R = U / I;  1 Ω = 1 V / 1 A')
 + bd('<p>Для металлических проводников при постоянной температуре график <em>I(U)</em> — прямая линия. Чем больше сопротивление, тем более пологая прямая. Лампочка накаливания не подчиняется этому закону точно: при нагреве нити её сопротивление растёт.</p>',
      '<p>For metallic conductors at constant temperature the graph <em>I(U)</em> is a straight line. The greater the resistance, the flatter the line. An incandescent bulb does not obey the law exactly: its resistance grows as the filament heats up.</p>'),
 lab1)

lab2 = model(2, 'СОПРОТИВЛЕНИЕ ПРОВОДА', 'RESISTANCE OF A WIRE', 'wrSvg', '0 0 600 240',
  select('wm', 'Материал', 'Material') + slider('wl', 'Длина', 'Length', 1, 1000, 1, 100) + slider('ws', 'Сечение', 'Cross-section', 0.5, 10, 0.5, 1.5),
  stats([('wR', 'Сопротивление R = ρl/S', 'Resistance R = ρl/S'), ('wC', 'Против меди', 'Against copper')]),
  'wrFb', 'Схема условная: провод показан не в масштабе; ρ — удельные сопротивления при 20 °C.', 'A schematic drawing: the wire is not to scale; ρ are the resistivities at 20 °C.')
s2 = section('wire', 'От чего зависит сопротивление провода', 'What a wire’s resistance depends on',
 bd('<p>Сопротивление проводника тем больше, чем он длиннее и тоньше, и зависит от материала:</p>',
    '<p>A conductor’s resistance is greater the longer and thinner it is, and it depends on the material:</p>')
 + formula('R = ρ · l / S', 'ρ — удельное сопротивление (Ом·м), l — длина, S — площадь сечения', 'ρ is the resistivity (Ω·m), l the length, S the cross-sectional area')
 + table(['МАТЕРИАЛ', 'ρ, ОМ·М (20 °C)'], ['MATERIAL', 'ρ, Ω·m (20 °C)'], [[('Медь', 'Copper'), '1,7·10⁻⁸'], [('Алюминий', 'Aluminium'), '2,8·10⁻⁸'], [('Железо', 'Iron'), '1,0·10⁻⁷'], [('Нихром', 'Nichrome'), '1,1·10⁻⁶']])
 + bd('<p>Поэтому для проводов выбирают медь или алюминий, а для нагревательных спиралей — нихром: у него сопротивление в десятки раз больше и он не окисляется при нагреве.</p>',
      '<p>That is why copper or aluminium is chosen for wires, and nichrome for heating coils: its resistivity is dozens of times greater and it does not oxidize on heating.</p>'),
 lab2)

lab3 = model(3, 'ДВА РЕЗИСТОРА', 'TWO RESISTORS', 'rsSvg', '0 0 600 260',
  slider('r1', 'Резистор 1', 'Resistor 1', 1, 100, 1, 10) + slider('r2', 'Резистор 2', 'Resistor 2', 1, 100, 1, 20),
  stats([('rS', 'Последовательно', 'In series'), ('rP', 'Параллельно', 'In parallel'), ('rC', 'Ток от 12 В: послед. / паралл.', 'Current from 12 V: series / parallel')]),
  'rsFb', 'Схема условная: источник 12 В. При параллельном соединении общее сопротивление меньше самого малого.', 'A schematic drawing: a 12 V source. In parallel the total resistance is smaller than the smallest one.')
s3 = section('resistors', 'Сопротивление цепи', 'The resistance of a circuit',
 bd('<p>Из закона Ома и правил предыдущей главы следует, как складываются сопротивления.</p><p><strong>Последовательно:</strong> ток один, напряжения складываются, поэтому сопротивления складываются.</p><p><strong>Параллельно:</strong> напряжение одно, токи складываются, поэтому складываются обратные величины. Это значит, что добавление параллельной ветви всегда <em>уменьшает</em> общее сопротивление.</p>',
    '<p>From Ohm’s law and the rules of the previous chapter follows how resistances combine.</p><p><strong>In series:</strong> the current is the same and the voltages add, so the resistances add.</p><p><strong>In parallel:</strong> the voltage is the same and the currents add, so the reciprocals add. This means adding a parallel branch always <em>reduces</em> the total resistance.</p>')
 + formula('Последовательно: R = R₁ + R₂<br>Параллельно: 1/R = 1/R₁ + 1/R₂,  R = R₁R₂ / (R₁ + R₂)', 'для двух одинаковых резисторов параллельно R = R₁/2', 'for two identical resistors in parallel R = R₁/2'),
 lab3)

tasks = [
 task(1, 'Ток в цепи', 'Current in a circuit', 'К резистору 40 Ом подключили напряжение 12 В. Найдите силу тока.', 'A voltage of 12 V is applied to a 40 Ω resistor. Find the current.',
  'U = 12 В, R = 40 Ом', 'U = 12 V, R = 40 Ω', 'I = U / R = 12 / 40 = 0,3 А.', 'I = U / R = 12 / 40 = 0.3 A.',
  '0,3 А.', '0.3 A.', True),
 task(2, 'Напряжение на лампе', 'Voltage on a bulb', 'Через лампочку сопротивлением 22 Ом идёт ток 0,5 А. Каково напряжение на ней?', 'A current of 0.5 A flows through a 22 Ω bulb. What is the voltage across it?',
  'R = 22 Ом, I = 0,5 А', 'R = 22 Ω, I = 0.5 A', 'U = I·R = 0,5 · 22 = 11 В.', 'U = I·R = 0.5 · 22 = 11 V.',
  '11 В.', '11 V.'),
 task(3, 'Сопротивление утюга', 'Resistance of an iron', 'Утюг, включённый в сеть 220 В, потребляет ток 4 А. Каково его сопротивление в рабочем состоянии?', 'An iron plugged into the 220 V mains draws 4 A. What is its resistance in operation?',
  'U = 220 В, I = 4 А', 'U = 220 V, I = 4 A', 'R = U / I = 220 / 4 = 55 Ом.', 'R = U / I = 220 / 4 = 55 Ω.',
  '55 Ом.', '55 Ω.'),
 task(4, 'Медный провод', 'A copper wire', 'Найдите сопротивление медного провода длиной 100 м и сечением 1,5 мм². ρ = 1,7·10⁻⁸ Ом·м.', 'Find the resistance of a copper wire 100 m long with a 1.5 mm² cross-section. ρ = 1.7·10⁻⁸ Ω·m.',
  'l = 100 м, S = 1,5·10⁻⁶ м², ρ = 1,7·10⁻⁸ Ом·м', 'l = 100 m, S = 1.5·10⁻⁶ m², ρ = 1.7·10⁻⁸ Ω·m', 'R = ρ·l / S = 1,7·10⁻⁸ · 100 / 1,5·10⁻⁶ = 1,7·10⁻⁶ / 1,5·10⁻⁶ ≈ 1,13 Ом.', 'R = ρ·l / S = 1.7·10⁻⁸ · 100 / 1.5·10⁻⁶ = 1.7·10⁻⁶ / 1.5·10⁻⁶ ≈ 1.13 Ω.',
  'около 1,1 Ом.', 'about 1.1 Ω.'),
 task(5, 'Два резистора', 'Two resistors', 'Резисторы 10 Ом и 20 Ом соединили сначала последовательно, потом параллельно. Найдите общее сопротивление в каждом случае.', 'Resistors of 10 Ω and 20 Ω are connected first in series, then in parallel. Find the total resistance in each case.',
  'R₁ = 10 Ом, R₂ = 20 Ом', 'R₁ = 10 Ω, R₂ = 20 Ω', 'Последовательно: 10 + 20 = 30 Ом.<br>Параллельно: 10 · 20 / (10 + 20) = 200 / 30 ≈ 6,7 Ом.', 'In series: 10 + 20 = 30 Ω.<br>In parallel: 10 · 20 / (10 + 20) = 200 / 30 ≈ 6.7 Ω.',
  '30 Ом и 6,7 Ом; параллельное — меньше меньшего из резисторов.', '30 Ω and 6.7 Ω; the parallel value is smaller than the smaller resistor.'),
 task(6, 'Птица на проводе', 'A bird on a wire', 'По алюминиевому проводу сечением 70 мм² идёт ток 500 А. Птица сидит так, что её лапы на проводе на расстоянии 10 см. Найдите напряжение между лапами и ток через птицу, если её сопротивление условно 1000 Ом. ρ = 2,8·10⁻⁸ Ом·м.', 'A current of 500 A flows through an aluminium wire of 70 mm² cross-section. A bird sits with its feet 10 cm apart on the wire. Find the voltage between its feet and the current through the bird if its resistance is, say, 1,000 Ω. ρ = 2.8·10⁻⁸ Ω·m.',
  'I = 500 А, S = 7·10⁻⁵ м², l = 0,1 м, R<sub>п</sub> = 1000 Ом', 'I = 500 A, S = 7·10⁻⁵ m², l = 0.1 m, R<sub>b</sub> = 1,000 Ω', 'Сопротивление участка: R = ρ·l / S = 2,8·10⁻⁸ · 0,1 / 7·10⁻⁵ = 4·10⁻⁵ Ом.<br>Напряжение: U = I·R = 500 · 4·10⁻⁵ = 0,02 В.<br>Ток через птицу: I = U / R<sub>п</sub> = 0,02 / 1000 = 2·10⁻⁵ А.', 'Resistance of the section: R = ρ·l / S = 2.8·10⁻⁸ · 0.1 / 7·10⁻⁵ = 4·10⁻⁵ Ω.<br>Voltage: U = I·R = 500 · 4·10⁻⁵ = 0.02 V.<br>Current through the bird: I = U / R<sub>b</sub> = 0.02 / 1,000 = 2·10⁻⁵ A.',
  '0,02 В и 20 мкА — безопасно: между лапами почти нет напряжения.', '0.02 V and 20 µA — harmless: there is almost no voltage between its feet.'),
]

quiz = [
 ('Как сила тока зависит от напряжения при постоянном сопротивлении?', [('Прямо пропорциональна', 'Верно: I = U/R.'), ('Обратно пропорциональна', 'Обратно пропорциональна сопротивлению.'), ('Не зависит', 'Зависит прямо.')],
  'How does current depend on voltage at constant resistance?', [('Directly proportional', 'Correct: I = U/R.'), ('Inversely proportional', 'It is inversely proportional to resistance.'), ('Independent', 'It depends directly.')], 0),
 ('Напряжение 6 В, сопротивление 3 Ом. Какой ток?', [('2 А', 'Верно: 6 / 3 = 2 А.'), ('0,5 А', 'Вы разделили наоборот.'), ('18 А', 'Не нужно умножать.')],
  'Voltage 6 V, resistance 3 Ω. What current?', [('2 A', 'Correct: 6 / 3 = 2 A.'), ('0.5 A', 'You divided the other way round.'), ('18 A', 'There is no multiplication here.')], 0),
 ('Во сколько раз изменится сопротивление провода, если длину увеличить вдвое?', [('Уменьшится вдвое', 'С ростом длины сопротивление растёт.'), ('Увеличится вдвое', 'Верно: R ~ l.'), ('Не изменится', 'R зависит от длины.')],
  'How does a wire’s resistance change if its length is doubled?', [('It halves', 'Resistance grows with length.'), ('It doubles', 'Correct: R ~ l.'), ('It does not change', 'R depends on the length.')], 1),
 ('Как изменится сопротивление провода, если его сечение увеличить вдвое?', [('Уменьшится вдвое', 'Верно: R ~ 1/S.'), ('Увеличится вдвое', 'Толстый провод проводит лучше.'), ('Не изменится', 'R зависит от сечения.')],
  'How does a wire’s resistance change if its cross-section is doubled?', [('It halves', 'Correct: R ~ 1/S.'), ('It doubles', 'A thicker wire conducts better.'), ('It does not change', 'R depends on the cross-section.')], 0),
 ('Почему нагревательные спирали делают из нихрома?', [('Он дёшев', 'Главное — не цена.'), ('У него большое удельное сопротивление и он стоек при нагреве', 'Верно.'), ('Он не проводит ток', 'Он проводит, но плохо.')],
  'Why are heating coils made of nichrome?', [('It is cheap', 'Price is not the main thing.'), ('It has a large resistivity and is stable when heated', 'Correct.'), ('It does not conduct', 'It conducts, but poorly.')], 1),
 ('Два резистора по 10 Ом соединили последовательно. Общее сопротивление:', [('5 Ом', 'Это параллельное соединение.'), ('20 Ом', 'Верно: R = R₁ + R₂.'), ('100 Ом', 'Сопротивления складываются, а не перемножаются.')],
  'Two 10 Ω resistors are connected in series. The total resistance:', [('5 Ω', 'That is the parallel connection.'), ('20 Ω', 'Correct: R = R₁ + R₂.'), ('100 Ω', 'Resistances add, they are not multiplied.')], 1),
 ('Два резистора по 10 Ом соединили параллельно. Общее сопротивление:', [('5 Ом', 'Верно: R = R₁/2.'), ('20 Ом', 'Это последовательное соединение.'), ('10 Ом', 'Параллельное соединение уменьшает сопротивление.')],
  'Two 10 Ω resistors are connected in parallel. The total resistance:', [('5 Ω', 'Correct: R = R₁/2.'), ('20 Ω', 'That is the series connection.'), ('10 Ω', 'A parallel connection reduces the resistance.')], 0),
 ('Почему птица на одном проводе под высоким напряжением в безопасности?', [('Лапы на одном проводе, напряжение между ними ничтожно', 'Верно: ток через птицу очень мал.'), ('Птицы не проводят ток', 'Тело птицы проводит ток.'), ('Провод не под напряжением', 'Провод под напряжением относительно земли.')],
  'Why is a bird on a single high-voltage wire safe?', [('Its feet are on one wire and the voltage between them is negligible', 'Correct: the current through the bird is very small.'), ('Birds do not conduct current', 'A bird’s body conducts.'), ('The wire is not live', 'The wire is live relative to the ground.')], 0),
]

js = r'''
const T={ru:{
 omLabel:"График зависимости силы тока от напряжения",wrLabel:"Провод заданной длины и толщины",rsLabel:"Два резистора: последовательно и параллельно",
 mats:["Медь","Алюминий","Железо","Нихром"],
 omFb:"Чем больше сопротивление, тем меньше ток при том же напряжении.",
 wrFb:"Длиннее и тоньше — сопротивление больше.",rsFb:"Параллельное сопротивление меньше самого малого резистора."},
 en:{
 omLabel:"A graph of current against voltage",wrLabel:"A wire of the chosen length and thickness",rsLabel:"Two resistors: in series and in parallel",
 mats:["Copper","Aluminium","Iron","Nichrome"],
 omFb:"The greater the resistance, the smaller the current at the same voltage.",
 wrFb:"Longer and thinner — more resistance.",rsFb:"The parallel resistance is smaller than the smallest resistor."}};
const RHO=[1.68e-8,2.82e-8,1.0e-7,1.1e-6];
function drawOm(){const t=tt(),U=+$("ou").value,R=+$("or").value,I=U/R;
 const X=u=>60+u/24*480,Imax=24/1,Y=i=>230-Math.min(i,3)/3*190;
 let g='<line x1="60" y1="230" x2="540" y2="230" stroke="#18181a"/><line x1="60" y1="230" x2="60" y2="40" stroke="#18181a"/>';
 for(let u=0;u<=24;u+=4)g+='<line x1="'+X(u)+'" y1="230" x2="'+X(u)+'" y2="40" stroke="#e3e1da"/>'+svgText(X(u),246,u,"#66666b","middle",10);
 for(let i=0;i<=3;i++)g+='<line x1="60" y1="'+Y(i)+'" x2="540" y2="'+Y(i)+'" stroke="#e3e1da"/>'+svgText(54,Y(i)+4,i,"#66666b","end",10);
 const iEnd=24/R;let xe=540,ye=Y(iEnd);if(iEnd>3){xe=X(3*R);ye=Y(3)}
 g+='<line x1="60" y1="230" x2="'+xe+'" y2="'+ye+'" stroke="#2f6f5d" stroke-width="3"/>';
 g+='<line x1="'+X(U)+'" y1="230" x2="'+X(U)+'" y2="'+Y(I)+'" stroke="#c9c2b0" stroke-dasharray="3 3"/><circle cx="'+X(U)+'" cy="'+Y(I)+'" r="6" fill="#b6533f"/>';
 g+=svgText(60,30,"I, A","#18181a","start",11)+svgText(540,262,"U, V","#18181a","end",11);
 $("omSvg").innerHTML=g;
 $("ouOut").textContent=fmt(U,1)+(lang==="ru"?" В":" V");$("orOut").textContent=R+(lang==="ru"?" Ом":" Ω");
 $("oI").textContent=fmt(I,2)+(lang==="ru"?" А":" A");$("oP").textContent=fmt(1/R,3)+(lang==="ru"?" А/В":" A/V");$("omFb").textContent=t.omFb}
["ou","or"].forEach(id=>$(id).addEventListener("input",drawOm));
function drawWr(){const t=tt(),i=+$("wm").value,l=+$("wl").value,S=+$("ws").value*1e-6,R=RHO[i]*l/S,Rc=RHO[0]*l/S;
 const w=6+Math.sqrt(+$("ws").value)*5,len=100+Math.log10(l)*140;
 let g='<rect x="60" y="'+(115-w/2)+'" width="'+len+'" height="'+w+'" rx="'+(w/2)+'" fill="'+["#b87333","#b5b5b5","#6b6b6b","#8a6a5a"][i]+'" stroke="#18181a"/>';
 g+=svgText(60,190,"l = "+num(l)+(lang==="ru"?" м":" m")+", S = "+fmt(+$("ws").value,1)+(lang==="ru"?" мм²":" mm²"),"#66666b","start",12);
 $("wrSvg").innerHTML=g;
 $("wlOut").textContent=num(l)+(lang==="ru"?" м":" m");$("wsOut").textContent=fmt(+$("ws").value,1)+(lang==="ru"?" мм²":" mm²");
 $("wR").textContent=R<1?fmt(R*1000,1)+(lang==="ru"?" мОм":" mΩ"):fmt(R,2)+(lang==="ru"?" Ом":" Ω");$("wC").textContent=i===0?"1":(RHO[i]/RHO[0]).toFixed(1).replace(".",lang==="ru"?",":".")+"×";$("wrFb").textContent=t.wrFb}
["wm","wl","ws"].forEach(id=>$(id).addEventListener("input",drawWr));
function drawRs(){const t=tt(),a=+$("r1").value,b=+$("r2").value,Rs=a+b,Rp=a*b/(a+b);
 const bx=(x,y,v)=>'<rect x="'+x+'" y="'+y+'" width="'+(20+v*0.8)+'" height="22" fill="#e8e4d8" stroke="#18181a"/>'+svgText(x+(20+v*0.8)/2,y+15,v+"Ω","#18181a","middle",11);
 let g='<line x1="40" y1="80" x2="560" y2="80" stroke="#18181a"/>'+bx(120,69,a)+bx(300,69,b)+svgText(300,40,lang==="ru"?"последовательно":"in series","#66666b","middle",12);
 g+='<line x1="40" y1="200" x2="80" y2="200" stroke="#18181a"/><line x1="80" y1="160" x2="80" y2="240" stroke="#18181a"/><line x1="80" y1="160" x2="560" y2="160" stroke="#18181a"/><line x1="80" y1="240" x2="560" y2="240" stroke="#18181a"/><line x1="560" y1="160" x2="560" y2="240" stroke="#18181a"/>'+bx(250,149,a)+bx(250,229,b);
 $("rsSvg").innerHTML=g;
 $("r1Out").textContent=a+(lang==="ru"?" Ом":" Ω");$("r2Out").textContent=b+(lang==="ru"?" Ом":" Ω");
 $("rS").textContent=fmt(Rs,1)+(lang==="ru"?" Ом":" Ω");$("rP").textContent=fmt(Rp,2)+(lang==="ru"?" Ом":" Ω");
 $("rC").textContent=fmt(12/Rs,2)+" / "+fmt(12/Rp,2)+(lang==="ru"?" А":" A");$("rsFb").textContent=t.rsFb}
["r1","r2"].forEach(id=>$(id).addEventListener("input",drawRs));
const LAB={ru:{omSvg:T.ru.omLabel,wrSvg:T.ru.wrLabel,rsSvg:T.ru.rsLabel},en:{omSvg:T.en.omLabel,wrSvg:T.en.wrLabel,rsSvg:T.en.rsLabel}};
function drawAll(){fillSel("wm",T[lang].mats,0);drawOm();drawWr();drawRs()}
'''

c = dict(n='17', slug='17-ohms-law.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Закон Ома. Сопротивление', 'Ohm’s law. Resistance'),
 desc='Глава 17 Атласа физики: закон Ома, электрическое сопротивление, удельное сопротивление, соединение резисторов.',
 lead=('Почему птица спокойно сидит на проводе под напряжением в тысячи вольт? Закон Ома, сопротивление провода и соединение резисторов.',
       'Why does a bird sit calmly on a wire carrying thousands of volts? Ohm’s law, the resistance of a wire and combining resistors.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('ohm', 'Закон Ома', 'Ohm’s law'), ('wire', 'Сопротивление провода', 'Wire resistance'), ('resistors', 'Резисторы', 'Resistors'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>По проводам высоковольтных линий идёт ток в сотни ампер при напряжении в десятки тысяч вольт. Прикоснуться к такому проводу — смертельно. А птицы спокойно сидят на нём и поют.</p><p>Почему птицу не бьёт током?</p>',
         '<p>Current of hundreds of amperes flows through high-voltage lines at tens of thousands of volts. Touching such a wire is deadly. Yet birds sit on it calmly and sing.</p><p>Why is a bird not shocked?</p>'),
 hint=('Подсказку даст модель «Сопротивление провода». Разгадка — в конце главы.', 'The “Resistance of a wire” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему птица в безопасности', 'The answer: why the bird is safe'),
 answer=('<p>Ток течёт по проводу, потому что между его концами есть напряжение. Но между двумя соседними точками провода напряжение крошечное: сопротивление короткого куска толстого провода ничтожно (задача 6 — около 0,00004 Ом), и по закону Ома <em>U = I·R</em> между лапами птицы получается сотые доли вольта. Через тело птицы идёт лишь ничтожный ток — микроамперы.</p><p>Опасность возникает, когда тело оказывается между <em>двумя точками с большой разностью потенциалов</em>: например, между проводом и землёй или между двумя проводами. Поэтому птицу на двух разных проводах сразу, да ещё и на опоре, могло бы убить. Человеку нельзя приближаться к оборванному проводу и к линии электропередачи.</p>',
         '<p>Current flows along the wire because there is a voltage between its ends. But between two neighbouring points of the wire the voltage is tiny: the resistance of a short piece of thick wire is negligible (problem 6 — about 0.00004 Ω), and by Ohm’s law <em>U = I·R</em> the voltage between the bird’s feet comes to hundredths of a volt. Only a negligible current — microamperes — passes through the bird’s body.</p><p>Danger arises when a body is between <em>two points with a large potential difference</em>: for example between a wire and the ground or between two wires. So a bird touching two different wires at once, or a wire and a pylon, could be killed. People must not approach a fallen wire or a power line.</p>'),
 sources=[
  ('Закон Ома, сопротивление, удельное сопротивление —', 'Ohm’s law, resistance, resistivity —', LINK('https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance', 'OpenStax University Physics, Vol. 2: Resistivity and resistance')),
  ('Удельные сопротивления меди, алюминия, железа, нихрома при 20 °C —', 'Resistivities of copper, aluminium, iron and nichrome at 20 °C —', LINK('https://www.electronics-notes.com/articles/basic_concepts/resistance/electrical-resistivity-table-materials.php', 'Electronics Notes: Resistivity table') + ', ' + LINK('https://hyperphysics.gsu.edu/hbase/Tables/rstiv.html', 'HyperPhysics: Resistivity table')),
  ('Напряжение сети 220 В —', 'Mains voltage 220 V —', LINK('https://www.cia.gov/the-world-factbook/countries/kyrgyzstan/travel-facts', 'CIA World Factbook: Kyrgyzstan travel facts'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Сопротивление птицы в задаче 6 — условное.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The bird’s resistance in problem 6 is assumed.'),
 prev=('16-electric-circuits.html', 'Глава 16 · Электрический ток', 'Chapter 16 · Electric current'),
 next=('18-electric-power.html', 'Глава 18 · Работа и мощность тока', 'Chapter 18 · Work and power of current'),
 js=js)
build(c)
