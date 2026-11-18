# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ПОЛЕ ТОЧЕЧНОГО ЗАРЯДА', 'THE FIELD OF A POINT CHARGE', 'pfSvg', '0 0 600 260',
  slider('pq', 'Заряд', 'Charge', -10, 10, 1, 5) + slider('pr', 'Расстояние до точки', 'Distance to the point', 0.1, 3, 0.1, 1),
  stats([('pE', 'Напряжённость поля E', 'Field strength E'), ('pF', 'Сила на заряд 1 нКл', 'Force on a 1 nC charge')]),
  'pfFb', 'Схема условная: заряд в микрокулонах (мкКл); стрелки показывают направление силы на положительный пробный заряд.',
  'A schematic drawing: the charge is in microcoulombs (µC); the arrows show the direction of the force on a positive test charge.')
s1 = section('field', 'Электрическое поле и напряжённость', 'The electric field and field strength',
 bd('<p>Заряды действуют друг на друга на расстоянии. Это объясняют так: каждый заряд создаёт вокруг себя <strong>электрическое поле</strong>, и оно действует на любой другой заряд. Поле характеризуют <strong>напряжённостью</strong> <em>E</em> — это сила, действующая на единичный положительный заряд в данной точке:</p>',
    '<p>Charges act on each other at a distance. This is explained as follows: each charge creates an <strong>electric field</strong> around itself, and the field acts on any other charge. The field is characterized by its <strong>strength</strong> <em>E</em> — the force on a unit positive charge at a given point:</p>')
 + formula('E = F / q', 'единица — ньютон на кулон (Н/Кл), она же вольт на метр (В/м)', 'the unit is the newton per coulomb (N/C), which is also the volt per metre (V/m)')
 + bd('<p>Для точечного заряда <em>q</em> на расстоянии <em>r</em>: <em>E = k·q / r²</em>. Направление поля — от положительного заряда и к отрицательному. Чем ближе к заряду, тем поле сильнее.</p>',
      '<p>For a point charge <em>q</em> at distance <em>r</em>: <em>E = k·q / r²</em>. The field points away from a positive charge and towards a negative one. The closer to the charge, the stronger the field.</p>'),
 lab1)

lab2 = model(2, 'ПОЛЕ МЕЖДУ ПЛАСТИНАМИ', 'THE FIELD BETWEEN PLATES', 'plSvg', '0 0 600 260',
  slider('pu', 'Напряжение', 'Voltage', 100, 30000, 100, 3000) + slider('pd', 'Зазор', 'Gap', 1, 100, 1, 10),
  stats([('plE', 'Напряжённость E = U/d', 'Field E = U/d'), ('plF', 'Ускорение электрона', 'Electron acceleration'), ('plS', 'Воздух пробивается?', 'Does the air break down?')]),
  'plFb', 'Схема условная: однородное поле. Воздух пробивается искрой, когда E больше примерно 3·10⁶ В/м (в сухом воздухе).',
  'A schematic drawing: a uniform field. Air breaks down with a spark when E exceeds roughly 3·10⁶ V/m (in dry air).')
s2 = section('voltage', 'Напряжение и однородное поле', 'Voltage and a uniform field',
 bd('<p>Между двумя параллельными заряженными пластинами поле почти одинаково во всех точках — <strong>однородное</strong>. Работа поля по перемещению заряда <em>q</em> между пластинами равна <em>A = q·U</em>, где <strong>напряжение</strong> <em>U</em> — это работа на единицу заряда (измеряется в вольтах: 1 В = 1 Дж/Кл). Для однородного поля связь простая:</p>',
    '<p>Between two parallel charged plates the field is almost the same everywhere — a <strong>uniform</strong> field. The work of the field in moving a charge <em>q</em> between the plates is <em>A = q·U</em>, where the <strong>voltage</strong> <em>U</em> is the work per unit charge (measured in volts: 1 V = 1 J/C). For a uniform field the relation is simple:</p>')
 + formula('E = U / d,   A = q · U', 'd — расстояние между пластинами', 'd is the distance between the plates')
 + bd('<p>Воздух — диэлектрик, но если поле очень сильное (около 3 млн В/м, то есть примерно 3 кВ на каждый миллиметр), молекулы воздуха ионизуются и проскакивает <strong>искра</strong>. Так происходит и в молнии, и когда вы касаетесь дверной ручки после ходьбы по ковру.</p>',
      '<p>Air is an insulator, but if the field is very strong (about 3 million V/m, that is roughly 3 kV for every millimetre) air molecules become ionized and a <strong>spark</strong> jumps. That is what happens in lightning and when you touch a doorknob after walking across a carpet.</p>'),
 lab2)

lab3 = model(3, 'РАБОТА ПРИ ПЕРЕНОСЕ ЗАРЯДА', 'WORK IN MOVING A CHARGE', 'wkSvg', '0 0 600 240',
  select('wu', 'Источник напряжения', 'Voltage source') + slider('wq', 'Прошедший заряд', 'Charge passed', 0.1, 10, 0.1, 1),
  stats([('wA', 'Работа поля A = qU', 'Work of the field A = qU'), ('wH', 'Подняло бы груз 1 кг на', 'Would lift a 1 kg load by')]),
  'wkFb', 'Схема условная: напряжение — типичное для источника; груз поднимается без потерь, g = 9,8 Н/кг.',
  'A schematic drawing: the voltage is typical for the source; the load is lifted without losses, g = 9.8 N/kg.')
s3 = section('work', 'Напряжение и энергия заряда', 'Voltage and the energy of a charge',
 bd('<p>Напряжение показывает, сколько энергии получает или отдаёт каждый кулон заряда. На батарейке АА — 1,5 В: каждый кулон, пройдя через лампочку, отдаёт ей 1,5 Дж. В розетке — 220 В (в Кыргызстане стандарт 220 В, 50 Гц): тот же кулон отдаёт 220 Дж. Поэтому напряжение сети опаснее.</p>',
    '<p>Voltage shows how much energy each coulomb of charge gains or gives up. A AA battery gives 1.5 V: every coulomb passing through a bulb gives it 1.5 J. A wall socket gives 220 V (the standard in Kyrgyzstan is 220 V, 50 Hz): the same coulomb gives 220 J. That is why mains voltage is more dangerous.</p>'),
 lab3)

tasks = [
 task(1, 'Поле заряда', 'Field of a charge', 'Найдите напряжённость поля точечного заряда 2 мкКл на расстоянии 0,3 м. k = 9·10⁹ Н·м²/Кл².', 'Find the field strength of a 2 µC point charge at a distance of 0.3 m. k = 9·10⁹ N·m²/C².',
  'q = 2·10⁻⁶ Кл, r = 0,3 м', 'q = 2·10⁻⁶ C, r = 0.3 m', 'E = k·q / r² = 9·10⁹ · 2·10⁻⁶ / 0,09 = 18 000 / 0,09 = 200 000 Н/Кл.', 'E = k·q / r² = 9·10⁹ · 2·10⁻⁶ / 0.09 = 18,000 / 0.09 = 200,000 N/C.',
  '2·10⁵ Н/Кл (В/м).', '2·10⁵ N/C (V/m).', True),
 task(2, 'Сила в поле', 'Force in a field', 'В точку с E = 2·10⁵ Н/Кл помещён заряд 5 нКл. Какая сила действует на него?', 'A charge of 5 nC is placed at a point where E = 2·10⁵ N/C. What force acts on it?',
  'E = 2·10⁵ Н/Кл, q = 5·10⁻⁹ Кл', 'E = 2·10⁵ N/C, q = 5·10⁻⁹ C', 'F = q·E = 5·10⁻⁹ · 2·10⁵ = 10⁻³ Н.', 'F = q·E = 5·10⁻⁹ · 2·10⁵ = 10⁻³ N.',
  '1 мН (одна тысячная ньютона).', '1 mN (one thousandth of a newton).'),
 task(3, 'Поле между пластинами', 'Field between plates', 'К пластинам, расположенным на расстоянии 2 см, приложено напряжение 500 В. Найдите напряжённость однородного поля.', 'A voltage of 500 V is applied to plates 2 cm apart. Find the strength of the uniform field.',
  'U = 500 В, d = 0,02 м', 'U = 500 V, d = 0.02 m', 'E = U / d = 500 / 0,02 = 25 000 В/м.', 'E = U / d = 500 / 0.02 = 25,000 V/m.',
  '25 000 В/м (25 кВ/м) — до пробоя воздуха далеко.', '25,000 V/m (25 kV/m) — far from air breakdown.'),
 task(4, 'Работа тока', 'Work of the current', 'Через автомобильный аккумулятор 12 В прошёл заряд 2 Кл. Какую работу совершило электрическое поле?', 'A charge of 2 C passed through a 12 V car battery. How much work was done by the electric field?',
  'U = 12 В, q = 2 Кл', 'U = 12 V, q = 2 C', 'A = q·U = 2 · 12 = 24 Дж.', 'A = q·U = 2 · 12 = 24 J.',
  '24 Дж.', '24 J.'),
 task(5, 'Искра', 'A spark', 'Какой наибольший зазор в воздухе может пробить напряжение 15 000 В, если воздух пробивается при E = 3·10⁶ В/м?', 'What is the largest air gap that 15,000 V can break down, if air breaks down at E = 3·10⁶ V/m?',
  'U = 15 000 В, E = 3·10⁶ В/м', 'U = 15,000 V, E = 3·10⁶ V/m', 'd = U / E = 15 000 / 3·10⁶ = 0,005 м.', 'd = U / E = 15,000 / 3·10⁶ = 0.005 m.',
  '5 мм. Так работает свеча зажигания: промежуток около миллиметра пробивается искрой.', '5 mm. That is how a spark plug works: a gap of about a millimetre is broken down by the spark.'),
 task(6, 'Электрон в поле', 'An electron in a field', 'Электрон разгоняется от покоя напряжением 100 В. Найдите его кинетическую энергию и скорость. e = 1,6·10⁻¹⁹ Кл, m = 9,1·10⁻³¹ кг.', 'An electron is accelerated from rest by 100 V. Find its kinetic energy and speed. e = 1.6·10⁻¹⁹ C, m = 9.1·10⁻³¹ kg.',
  'U = 100 В', 'U = 100 V', 'E<sub>к</sub> = e·U = 1,6·10⁻¹⁹ · 100 = 1,6·10⁻¹⁷ Дж.<br>v = √(2E<sub>к</sub>/m) = √(3,2·10⁻¹⁷ / 9,1·10⁻³¹) ≈ 5,9·10⁶ м/с.', 'E<sub>k</sub> = e·U = 1.6·10⁻¹⁹ · 100 = 1.6·10⁻¹⁷ J.<br>v = √(2E<sub>k</sub>/m) = √(3.2·10⁻¹⁷ / 9.1·10⁻³¹) ≈ 5.9·10⁶ m/s.',
  'около 6·10⁶ м/с, то есть 2 % скорости света.', 'about 6·10⁶ m/s, that is 2 % of the speed of light.'),
]

quiz = [
 ('Что показывает напряжённость электрического поля?', [('Силу, действующую на единичный положительный заряд', 'Верно: E = F/q.'), ('Работу по перемещению заряда', 'Это связано с напряжением.'), ('Массу заряда', 'Масса здесь не при чём.')],
  'What does the electric field strength show?', [('The force on a unit positive charge', 'Correct: E = F/q.'), ('The work in moving a charge', 'That is related to voltage.'), ('The mass of the charge', 'Mass is not involved.')], 0),
 ('Как направлено поле положительного точечного заряда?', [('К заряду', 'Так направлено поле отрицательного заряда.'), ('От заряда', 'Верно.'), ('По кругу вокруг заряда', 'Поле не замкнуто вокруг заряда.')],
  'How is the field of a positive point charge directed?', [('Towards the charge', 'That is the field of a negative charge.'), ('Away from the charge', 'Correct.'), ('In circles around the charge', 'The field does not circle the charge.')], 1),
 ('Как изменится поле точечного заряда при увеличении расстояния вдвое?', [('Уменьшится в 2 раза', 'E зависит от квадрата расстояния.'), ('Уменьшится в 4 раза', 'Верно: E ~ 1/r².'), ('Не изменится', 'Поле слабеет с расстоянием.')],
  'How does the field of a point charge change when the distance is doubled?', [('It decreases 2 times', 'E depends on the square of the distance.'), ('It decreases 4 times', 'Correct: E ~ 1/r².'), ('It does not change', 'The field weakens with distance.')], 1),
 ('Что такое 1 вольт?', [('1 Дж на 1 Кл', 'Верно: U = A/q.'), ('1 Н на 1 Кл', 'Это единица напряжённости.'), ('1 Кл за 1 с', 'Это ампер.')],
  'What is 1 volt?', [('1 J per 1 C', 'Correct: U = A/q.'), ('1 N per 1 C', 'That is a unit of field strength.'), ('1 C per 1 s', 'That is the ampere.')], 0),
 ('Чему равна напряжённость однородного поля между пластинами?', [('U·d', 'Так получится не та единица.'), ('U / d', 'Верно.'), ('d / U', 'Это обратная величина.')],
  'What is the strength of the uniform field between plates?', [('U·d', 'That gives the wrong unit.'), ('U / d', 'Correct.'), ('d / U', 'That is the reciprocal.')], 1),
 ('Заряд 2 Кл прошёл напряжение 5 В. Какая работа совершена?', [('10 Дж', 'Верно: A = q·U = 10 Дж.'), ('2,5 Дж', 'Это U/q, а нужно умножить.'), ('7 Дж', 'Заряд и напряжение не складывают.')],
  'A charge of 2 C passed a voltage of 5 V. How much work was done?', [('10 J', 'Correct: A = q·U = 10 J.'), ('2.5 J', 'That is U/q; the values must be multiplied.'), ('7 J', 'Charge and voltage are not added.')], 0),
 ('Что нужно, чтобы в воздухе проскочила искра?', [('Очень сильное электрическое поле', 'Верно: около 3 МВ/м.'), ('Очень сильный магнит', 'Искру вызывает поле, а не магнит.'), ('Высокая температура воздуха', 'Дело в напряжённости поля.')],
  'What is needed for a spark to jump in air?', [('A very strong electric field', 'Correct: about 3 MV/m.'), ('A very strong magnet', 'A spark is caused by a field, not a magnet.'), ('A high air temperature', 'It is a matter of field strength.')], 0),
 ('Напряжение в бытовой розетке в Кыргызстане:', [('12 В', 'Это напряжение автомобильного аккумулятора.'), ('220 В', 'Верно: 220 В, 50 Гц.'), ('1,5 В', 'Это батарейка.')],
  'The voltage of a household socket in Kyrgyzstan:', [('12 V', 'That is a car battery voltage.'), ('220 V', 'Correct: 220 V, 50 Hz.'), ('1.5 V', 'That is a battery.')], 1),
]

js = r'''
const T={ru:{
 pfLabel:"Заряд и стрелки электрического поля вокруг него",plLabel:"Две заряженные пластины и электрон между ними",wkLabel:"Источник напряжения и поднятый груз",
 srcs:["Батарейка АА, 1,5 В","Блок питания телефона, 5 В","Автомобильный аккумулятор, 12 В","Бытовая розетка, 220 В"],
 spark:"да, искра!",nospark:"нет",
 pfFb:"Поле ослабевает по мере удаления от заряда.",
 plFb:["Поле слишком слабое: воздух не пробивается.","E больше 3·10⁶ В/м — воздух пробивается искрой."],
 wkFb:"Чем выше напряжение, тем больше энергии переносит каждый кулон.",
 plus:"+ пластина",minus:"− пластина"},
 en:{
 pfLabel:"A charge and the arrows of the electric field around it",plLabel:"Two charged plates and an electron between them",wkLabel:"A voltage source and a lifted load",
 srcs:["AA battery, 1.5 V","Phone charger, 5 V","Car battery, 12 V","Wall socket, 220 V"],
 spark:"yes, a spark!",nospark:"no",
 pfFb:"The field weakens with distance from the charge.",
 plFb:["The field is too weak: the air does not break down.","E exceeds 3·10⁶ V/m — the air breaks down with a spark."],
 wkFb:"The higher the voltage, the more energy each coulomb carries.",
 plus:"+ plate",minus:"− plate"}};
const KC=9e9,EL=1.602e-19,ME=9.109e-31,VS=[1.5,5,12,220];
function drawPf(){const t=tt(),q=+$("pq").value,r=+$("pr").value,E=KC*Math.abs(q)*1e-6/(r*r);
 const cx=300,cy=130;
 let g='';
 for(let k=0;k<12;k++){const a=k/12*2*Math.PI,x0=cx+Math.cos(a)*30,y0=cy+Math.sin(a)*30,x1=cx+Math.cos(a)*115,y1=cy+Math.sin(a)*115;
  if(q>0)g+=arrow(x0,y0,x1,y1,"#c9c2b0",2);else if(q<0)g+=arrow(x1,y1,x0,y0,"#c9c2b0",2)}
 g+='<circle cx="'+cx+'" cy="'+cy+'" r="'+(10+Math.abs(q)*1.5)+'" fill="'+(q>0?"#b6533f":q<0?"#3f5f8f":"#c9c2b0")+'" stroke="#18181a"/>'+svgText(cx,cy+5,q>0?"+":q<0?"−":"0","#fff","middle",15);
 const px=cx+Math.min(2.8,r)/3*240;
 g+='<line x1="'+cx+'" y1="'+(cy+95)+'" x2="'+px+'" y2="'+(cy+95)+'" stroke="#66666b" stroke-dasharray="3 3"/>'+svgText((cx+px)/2,cy+115,"r = "+fmt(r,1)+(lang==="ru"?" м":" m"),"#66666b","middle",11);
 g+='<circle cx="'+px+'" cy="'+(cy+95)+'" r="6" fill="#18181a"/>';
 if(q!==0){const L=Math.min(80,10+Math.log10(1+E/100)*18),d=q>0?1:-1;g+=arrow(px,cy+95,px+d*L,cy+95,"#2f6f5d",3)}
 $("pfSvg").innerHTML=g;
 $("pqOut").textContent=(q>0?"+":"")+q+(lang==="ru"?" мкКл":" µC");$("prOut").textContent=fmt(r,1)+(lang==="ru"?" м":" m");
 $("pE").textContent=E>=1e6?fmt(E/1e6,2)+(lang==="ru"?" МВ/м":" MV/m"):E>=1e3?fmt(E/1e3,1)+(lang==="ru"?" кВ/м":" kV/m"):fmt(E,0)+(lang==="ru"?" В/м":" V/m");
 const F=E*1e-9;$("pF").textContent=F>=1e-3?fmt(F*1e3,2)+(lang==="ru"?" мН":" mN"):fmt(F*1e6,1)+(lang==="ru"?" мкН":" µN");$("pfFb").textContent=t.pfFb}
["pq","pr"].forEach(id=>$(id).addEventListener("input",drawPf));
function drawPl(){const t=tt(),U=+$("pu").value,d=+$("pd").value/1000,E=U/d,a=EL*E/ME,spark=E>=3e6;
 let g='<rect x="120" y="50" width="360" height="10" fill="#b6533f" stroke="#18181a"/><rect x="120" y="190" width="360" height="10" fill="#3f5f8f" stroke="#18181a"/>'+svgText(110,60,t.plus,"#b6533f","end",11)+svgText(110,200,t.minus,"#3f5f8f","end",11);
 for(let k=0;k<8;k++){const x=150+k*45;g+=arrow(x,64,x,186,spark?"#e0b82f":"#c9c2b0",2)}
 if(spark)g+='<path d="M300 60 L285 100 L310 115 L290 150 L305 190" fill="none" stroke="#e0b82f" stroke-width="5"/>';
 else g+='<circle cx="300" cy="190" r="6" fill="#3f5f8f" stroke="#18181a" transform="translate(0,-26)"/>'+arrow(300,150,300,110,"#2f6f5d",3);
 $("plSvg").innerHTML=g;
 $("puOut").textContent=num(U)+(lang==="ru"?" В":" V");$("pdOut").textContent=fmt(d*1000,0)+(lang==="ru"?" мм":" mm");
 $("plE").textContent=E>=1e6?fmt(E/1e6,2)+(lang==="ru"?" МВ/м":" MV/m"):fmt(E/1e3,1)+(lang==="ru"?" кВ/м":" kV/m");
 $("plF").textContent=a.toExponential(1).replace(/e\+(\d+)/,function(m,n){return "·10"+n.split("").map(function(c){return "⁰¹²³⁴⁵⁶⁷⁸⁹"[+c]}).join("")}).replace(".",lang==="ru"?",":".")+(lang==="ru"?" м/с²":" m/s²");
 $("plS").textContent=spark?t.spark:t.nospark;$("plFb").textContent=t.plFb[spark?1:0]}
["pu","pd"].forEach(id=>$(id).addEventListener("input",drawPl));
function drawWk(){const t=tt(),i=+$("wu").value,U=VS[i],q=+$("wq").value,A=q*U,h=A/9.8;
 let g='<rect x="80" y="70" width="100" height="100" rx="8" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/>'+svgText(130,128,fmt(U,U<10?1:0)+(lang==="ru"?" В":" V"),"#18181a","middle",18);
 const H=Math.min(150,10+Math.log10(1+h)*45);
 g+='<line x1="400" y1="200" x2="400" y2="'+(200-H)+'" stroke="#b6533f" stroke-width="3"/><rect x="380" y="'+(200-H-30)+'" width="40" height="30" fill="#c9c2b0" stroke="#18181a"/>'+svgText(440,200-H-10,fmt(h,h<10?2:0)+(lang==="ru"?" м":" m"),"#b6533f","start",13);
 g+='<line x1="330" y1="200" x2="520" y2="200" stroke="#18181a"/>'+svgText(250,125,"q = "+fmt(q,1)+(lang==="ru"?" Кл":" C"),"#66666b","middle",13);
 $("wkSvg").innerHTML=g;
 $("wqOut").textContent=fmt(q,1)+(lang==="ru"?" Кл":" C");
 $("wA").textContent=A>=1000?fmt(A/1000,2)+(lang==="ru"?" кДж":" kJ"):fmt(A,1)+(lang==="ru"?" Дж":" J");$("wH").textContent=fmt(h,h<10?2:0)+(lang==="ru"?" м":" m");$("wkFb").textContent=t.wkFb}
["wu","wq"].forEach(id=>$(id).addEventListener("input",drawWk));
const LAB={ru:{pfSvg:T.ru.pfLabel,plSvg:T.ru.plLabel,wkSvg:T.ru.wkLabel},en:{pfSvg:T.en.pfLabel,plSvg:T.en.plLabel,wkSvg:T.en.wkLabel}};
function drawAll(){fillSel("wu",T[lang].srcs,3);drawPf();drawPl();drawWk()}
'''

c = dict(n='15', slug='15-electric-field.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Электрическое поле и напряжение', 'The electric field and voltage'),
 desc='Глава 15 Атласа физики: электрическое поле, напряжённость, напряжение, однородное поле, пробой воздуха.',
 lead=('Воздух не проводит ток, но между облаком и землёй проскакивает молния. Электрическое поле, напряжённость, вольт и пробой воздуха.',
       'Air does not conduct current, yet lightning leaps between cloud and ground. The electric field, field strength, the volt and the breakdown of air.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('field', 'Поле', 'The field'), ('voltage', 'Напряжение', 'Voltage'), ('work', 'Энергия заряда', 'Energy of a charge'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Воздух — изолятор: по нему ток не идёт, и мы спокойно ходим между розетками и проводами. Но в грозу между облаком и землёй проскакивает молния длиной в километры, а от дверной ручки после ковра вас бьёт крошечная искра.</p><p>Как же воздух пропускает ток, если он изолятор?</p>',
         '<p>Air is an insulator: current does not flow through it, and we walk calmly among sockets and wires. But in a thunderstorm lightning kilometres long leaps between cloud and ground, and after a carpet a tiny spark stings you from a doorknob.</p><p>How can air pass current if it is an insulator?</p>'),
 hint=('Подсказку даст модель «Поле между пластинами». Разгадка — в конце главы.', 'The “The field between plates” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему воздух пробивается', 'The answer: why air breaks down'),
 answer=('<p>Изолятор не пропускает ток, пока поле в нём не слишком сильное. В воздухе всегда есть несколько свободных электронов и ионов. Когда напряжённость поля достигает примерно 3 МВ/м, такие электроны разгоняются полем настолько, что при столкновении выбивают электроны из молекул, а те — новые. Возникает лавина зарядов, воздух становится проводящим, и проскакивает искра.</p><p>Для ручки это зазор около миллиметра и несколько киловольт (задача 5). Для грозы зазоры измеряются километрами, поэтому нужны сотни миллионов вольт.</p>',
         '<p>An insulator does not conduct as long as the field in it is not too strong. Air always contains a few free electrons and ions. When the field strength reaches about 3 MV/m such electrons are accelerated enough that in collisions they knock electrons out of molecules, and those knock out new ones. An avalanche of charges arises, the air becomes conducting, and a spark jumps.</p><p>For a doorknob that is a gap of about a millimetre and a few kilovolts (problem 5). For a thunderstorm the gaps are measured in kilometres, so hundreds of millions of volts are needed.</p>'),
 sources=[
  ('Электрическое поле, напряжённость, потенциал —', 'The electric field, field strength, potential —', LINK('https://openstax.org/books/university-physics-volume-2/pages/5-introduction', 'OpenStax University Physics, Vol. 2, гл. 5–7')),
  ('Электрическая прочность воздуха ≈ 3 МВ/м —', 'Dielectric strength of air ≈ 3 MV/m —', LINK('https://en.wikipedia.org/wiki/Dielectric_strength', 'Wikipedia: Dielectric strength')),
  ('Масса и заряд электрона —', 'Mass and charge of the electron —', LINK('https://physics.nist.gov/cgi-bin/cuu/Value?me', 'NIST: electron mass') + ', ' + LINK('https://physics.nist.gov/cgi-bin/cuu/Value?e', 'NIST: elementary charge')),
  ('Напряжение сети в Кыргызстане 220 В, 50 Гц —', 'Mains voltage in Kyrgyzstan 220 V, 50 Hz —', LINK('https://www.cia.gov/the-world-factbook/countries/kyrgyzstan/travel-facts', 'CIA World Factbook: Kyrgyzstan travel facts'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Значения напряжений источников — типичные.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The voltages of the sources are typical.'),
 prev=('14-electric-charge.html', 'Глава 14 · Электрический заряд', 'Chapter 14 · Electric charge'),
 next=('16-electric-circuits.html', 'Глава 16 · Электрический ток и цепи', 'Chapter 16 · Electric current and circuits'),
 js=js)
build(c)
