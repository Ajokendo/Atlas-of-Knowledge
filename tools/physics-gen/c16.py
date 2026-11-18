# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'СИЛА ТОКА', 'ELECTRIC CURRENT', 'cuSvg', '0 0 600 220',
  slider('cq', 'Заряд через сечение провода', 'Charge through the wire’s cross-section', 1, 600, 1, 120) + slider('ct', 'Время', 'Time', 1, 120, 1, 60),
  stats([('cI', 'Сила тока I = q/t', 'Current I = q/t'), ('cN', 'Электронов в секунду', 'Electrons per second')]),
  'cuFb', 'Схема условная: точки — электроны, плотность точек пропорциональна току. Электроны движутся от «−» к «+», а условное направление тока — от «+» к «−».',
  'A schematic drawing: dots are electrons, their density is proportional to the current. Electrons move from “−” to “+”, while the conventional direction of current is from “+” to “−”.')
s1 = section('current', 'Электрический ток', 'Electric current',
 bd('<p><strong>Электрический ток</strong> — это упорядоченное движение заряженных частиц. В металлах это электроны, в растворах — ионы. Чтобы ток шёл непрерывно, нужны <strong>источник тока</strong> (батарейка, аккумулятор, генератор), <strong>проводники</strong> и замкнутая <strong>цепь</strong>. Источник создаёт в цепи электрическое поле (напряжение), и оно гонит заряды.</p><p><strong>Сила тока</strong> <em>I</em> показывает, какой заряд проходит через сечение проводника за 1 секунду:</p>',
    '<p><strong>Electric current</strong> is the ordered motion of charged particles. In metals these are electrons, in solutions ions. For current to flow continuously you need a <strong>source</strong> (a battery, an accumulator, a generator), <strong>conductors</strong> and a closed <strong>circuit</strong>. The source creates an electric field (voltage) in the circuit, and it drives the charges.</p><p>The <strong>current</strong> <em>I</em> shows what charge passes through the cross-section of a conductor in 1 second:</p>')
 + formula('I = q / t', 'единица — ампер: 1 А = 1 Кл/с; q = I · t', 'the unit is the ampere: 1 A = 1 C/s; q = I · t')
 + bd('<p>Силу тока измеряют <strong>амперметром</strong>, включая его в цепь последовательно. Напряжение измеряют <strong>вольтметром</strong>, подключая его параллельно участку цепи.</p>',
      '<p>Current is measured with an <strong>ammeter</strong>, placed in the circuit in series. Voltage is measured with a <strong>voltmeter</strong>, connected in parallel across a part of the circuit.</p>'),
 lab1)

lab2 = model(2, 'ГИРЛЯНДА: ПОСЛЕДОВАТЕЛЬНО И ПАРАЛЛЕЛЬНО', 'A GARLAND: SERIES AND PARALLEL', 'grSvg', '0 0 600 260',
  select('gt', 'Соединение', 'Connection') + slider('gn', 'Число лампочек', 'Number of bulbs', 2, 5, 1, 4) + select('gb', 'Лампочка 2', 'Bulb 2'),
  stats([('gL', 'Горят лампочек', 'Bulbs lit'), ('gC', 'Ток в цепи', 'Current flows')]),
  'grFb', 'Схема условная: все лампочки одинаковые, источник исправен.', 'A schematic drawing: all bulbs are identical and the source works.')
s2 = section('circuits', 'Последовательное и параллельное соединение', 'Series and parallel connection',
 bd('<p>Участки цепи можно соединять двумя способами.</p><p><strong>Последовательно</strong> (друг за другом): ток один и тот же во всех лампочках, напряжения складываются, а если одна перегорела — цепь разорвана и гаснут все.</p><p><strong>Параллельно</strong> (каждая на своей ветви): напряжение на всех одинаково, токи ветвей складываются, а если одна перегорела — остальные продолжают гореть.</p>',
    '<p>Parts of a circuit can be joined in two ways.</p><p><strong>In series</strong> (one after another): the current is the same in all bulbs, the voltages add up, and if one burns out the circuit is broken and all go dark.</p><p><strong>In parallel</strong> (each on its own branch): the voltage across all is the same, the currents of the branches add up, and if one burns out the others keep burning.</p>')
 + formula('Последовательно: I = I₁ = I₂,  U = U₁ + U₂<br>Параллельно: U = U₁ = U₂,  I = I₁ + I₂', 'так устроена проводка квартиры: все приборы включены параллельно', 'this is how a flat’s wiring works: all appliances are connected in parallel'),
 lab2)

lab3 = model(3, 'ПРАВИЛА ДЛЯ ТОКОВ И НАПРЯЖЕНИЙ', 'THE RULES FOR CURRENTS AND VOLTAGES', 'ruSvg', '0 0 600 250',
  slider('i1', 'Ток 1-й ветви', 'Current in branch 1', 0.1, 5, 0.1, 1.5) + slider('i2', 'Ток 2-й ветви', 'Current in branch 2', 0.1, 5, 0.1, 2.5) + slider('u1', 'Напряжение на 1-й лампе', 'Voltage on bulb 1', 0.5, 12, 0.5, 4.5) + slider('u2', 'Напряжение на 2-й лампе', 'Voltage on bulb 2', 0.5, 12, 0.5, 3),
  stats([('rI', 'Параллельно: общий ток', 'In parallel: total current'), ('rU', 'Последовательно: общее напряжение', 'In series: total voltage')]),
  'ruFb', 'Схема условная: слева — две ветви, подключённые параллельно; справа — две лампы последовательно.', 'A schematic drawing: on the left, two branches connected in parallel; on the right, two bulbs in series.')
s3 = section('rules', 'Складываем токи и напряжения', 'Adding currents and voltages',
 bd('<p>В параллельных ветвях заряд, пришедший в узел, расходится по ветвям: сколько втекает, столько и вытекает, поэтому общий ток равен сумме токов ветвей. При последовательном соединении работа по переносу единичного заряда складывается из работ на каждом участке, поэтому напряжения тоже складываются. Эти правила нужны при расчёте любой цепи.</p>',
    '<p>In parallel branches the charge arriving at a junction splits among the branches: as much flows in as flows out, so the total current equals the sum of the branch currents. In series the work in carrying a unit charge is the sum of the works on each part, so the voltages also add. These rules are needed in calculating any circuit.</p>'),
 lab3)

tasks = [
 task(1, 'Сила тока', 'Current', 'Через сечение проводника за 1 минуту прошёл заряд 120 Кл. Найдите силу тока.', 'A charge of 120 C passed through a conductor’s cross-section in 1 minute. Find the current.',
  'q = 120 Кл, t = 60 с', 'q = 120 C, t = 60 s', 'I = q / t = 120 / 60 = 2 А.', 'I = q / t = 120 / 60 = 2 A.',
  '2 А.', '2 A.', True),
 task(2, 'Заряд за время', 'Charge over time', 'Какой заряд пройдёт через лампочку за 5 минут при токе 0,5 А?', 'What charge passes through a bulb in 5 minutes at a current of 0.5 A?',
  'I = 0,5 А, t = 300 с', 'I = 0.5 A, t = 300 s', 'q = I·t = 0,5 · 300 = 150 Кл.', 'q = I·t = 0.5 · 300 = 150 C.',
  '150 Кл.', '150 C.'),
 task(3, 'Электроны в секунду', 'Electrons per second', 'Сколько электронов проходит через сечение проводника за 1 с при токе 1 А? e = 1,6·10⁻¹⁹ Кл.', 'How many electrons pass through a conductor’s cross-section in 1 s at a current of 1 A? e = 1.6·10⁻¹⁹ C.',
  'I = 1 А, t = 1 с', 'I = 1 A, t = 1 s', 'q = I·t = 1 Кл.<br>N = q / e = 1 / (1,6·10⁻¹⁹) ≈ 6,25·10¹⁸.', 'q = I·t = 1 C.<br>N = q / e = 1 / (1.6·10⁻¹⁹) ≈ 6.25·10¹⁸.',
  'около 6·10¹⁸ электронов каждую секунду.', 'about 6·10¹⁸ electrons every second.'),
 task(4, 'Параллельные ветви', 'Parallel branches', 'В две параллельные ветви идут токи 0,3 А и 0,5 А. Каков ток в неразветвлённой части цепи?', 'Currents of 0.3 A and 0.5 A flow in two parallel branches. What is the current in the unbranched part of the circuit?',
  'I₁ = 0,3 А, I₂ = 0,5 А', 'I₁ = 0.3 A, I₂ = 0.5 A', 'I = I₁ + I₂ = 0,3 + 0,5 = 0,8 А.', 'I = I₁ + I₂ = 0.3 + 0.5 = 0.8 A.',
  '0,8 А.', '0.8 A.'),
 task(5, 'Лампочки подряд', 'Bulbs in a row', 'Две лампочки включены последовательно. Напряжения на них 4,5 В и 3 В. Каково напряжение источника?', 'Two bulbs are connected in series. The voltages across them are 4.5 V and 3 V. What is the source voltage?',
  'U₁ = 4,5 В, U₂ = 3 В', 'U₁ = 4.5 V, U₂ = 3 V', 'U = U₁ + U₂ = 4,5 + 3 = 7,5 В.', 'U = U₁ + U₂ = 4.5 + 3 = 7.5 V.',
  '7,5 В.', '7.5 V.'),
 task(6, 'Скорость электронов', 'Speed of the electrons', 'Медный провод сечением 1 мм² несёт ток 1 А. Концентрация свободных электронов в меди n = 8,5·10²⁸ м⁻³. Найдите скорость дрейфа электронов v = I / (n·e·S).', 'A copper wire of 1 mm² cross-section carries a current of 1 A. The concentration of free electrons in copper is n = 8.5·10²⁸ m⁻³. Find the drift velocity v = I / (n·e·S).',
  'I = 1 А, S = 10⁻⁶ м², n = 8,5·10²⁸ м⁻³', 'I = 1 A, S = 10⁻⁶ m², n = 8.5·10²⁸ m⁻³', 'v = 1 / (8,5·10²⁸ · 1,6·10⁻¹⁹ · 10⁻⁶) = 1 / (1,36·10⁴) ≈ 7,4·10⁻⁵ м/с.', 'v = 1 / (8.5·10²⁸ · 1.6·10⁻¹⁹ · 10⁻⁶) = 1 / (1.36·10⁴) ≈ 7.4·10⁻⁵ m/s.',
  'около 0,07 мм/с: электроны еле ползут. Лампочка загорается сразу, потому что поле распространяется по цепи почти со скоростью света.', 'about 0.07 mm/s: the electrons barely crawl. A bulb lights at once because the field spreads through the circuit at almost the speed of light.'),
]

quiz = [
 ('Что такое электрический ток?', [('Упорядоченное движение заряженных частиц', 'Верно.'), ('Хаотичное движение молекул', 'Это тепловое движение.'), ('Статический заряд на теле', 'Заряд сам по себе не ток.')],
  'What is electric current?', [('The ordered motion of charged particles', 'Correct.'), ('The chaotic motion of molecules', 'That is thermal motion.'), ('A static charge on a body', 'Charge alone is not current.')], 0),
 ('Какие условия нужны для существования тока?', [('Только проводник', 'Нужен ещё источник и замкнутая цепь.'), ('Источник тока, проводники и замкнутая цепь', 'Верно.'), ('Только лампочка', 'Лампочка — потребитель.')],
  'What conditions are needed for a current?', [('Just a conductor', 'A source and a closed circuit are also needed.'), ('A source, conductors and a closed circuit', 'Correct.'), ('Just a bulb', 'A bulb is a consumer.')], 1),
 ('Единица силы тока:', [('Вольт', 'Вольт — единица напряжения.'), ('Ампер', 'Верно: 1 А = 1 Кл/с.'), ('Ом', 'Ом — единица сопротивления.')],
  'The unit of current:', [('Volt', 'The volt is a unit of voltage.'), ('Ampere', 'Correct: 1 A = 1 C/s.'), ('Ohm', 'The ohm is a unit of resistance.')], 1),
 ('Как включают амперметр в цепь?', [('Последовательно', 'Верно: через него идёт весь измеряемый ток.'), ('Параллельно', 'Так включают вольтметр.'), ('Как угодно', 'Способ включения важен.')],
  'How is an ammeter placed in a circuit?', [('In series', 'Correct: all the measured current flows through it.'), ('In parallel', 'That is how a voltmeter is connected.'), ('Any way', 'The way of connection matters.')], 0),
 ('В гирлянде из последовательно соединённых лампочек перегорела одна. Что с остальными?', [('Продолжают гореть', 'Так бывает при параллельном соединении.'), ('Гаснут', 'Верно: цепь разорвана.'), ('Горят ярче', 'Тока в разорванной цепи нет.')],
  'One bulb has burnt out in a garland of bulbs in series. What about the others?', [('They keep burning', 'That happens in a parallel connection.'), ('They go out', 'Correct: the circuit is broken.'), ('They burn brighter', 'There is no current in a broken circuit.')], 1),
 ('Как соединены приборы в квартире?', [('Последовательно', 'Тогда один выключенный прибор отключал бы все.'), ('Параллельно', 'Верно: на каждый прибор одно и то же напряжение 220 В.'), ('По-разному в каждой комнате', 'Это всегда параллельное соединение.')],
  'How are the appliances in a flat connected?', [('In series', 'Then one switched-off appliance would turn off all.'), ('In parallel', 'Correct: each appliance gets the same 220 V.'), ('Differently in each room', 'It is always a parallel connection.')], 1),
 ('Две ветви с токами 2 А и 3 А соединены параллельно. Общий ток:', [('1 А', 'Токи ветвей складываются, а не вычитаются.'), ('5 А', 'Верно: I = I₁ + I₂.'), ('6 А', 'Токи не перемножаются.')],
  'Two branches with currents of 2 A and 3 A are connected in parallel. The total current:', [('1 A', 'The branch currents add, not subtract.'), ('5 A', 'Correct: I = I₁ + I₂.'), ('6 A', 'Currents are not multiplied.')], 1),
 ('Почему лампочка загорается сразу, хотя электроны движутся медленно?', [('Электроны движутся со скоростью света', 'Дрейф электронов очень медленный.'), ('Поле в цепи устанавливается почти со скоростью света и приводит в движение все электроны сразу', 'Верно.'), ('В лампочке свои электроны', 'Движение электронов во всей цепи начинается одновременно.')],
  'Why does a bulb light at once although the electrons move slowly?', [('The electrons move at the speed of light', 'The drift of electrons is very slow.'), ('The field in the circuit is established almost at the speed of light and sets all electrons moving at once', 'Correct.'), ('The bulb has its own electrons', 'Electrons throughout the circuit start moving simultaneously.')], 1),
]

js = r'''
const T={ru:{
 cuLabel:"Провод с электронами: плотность точек показывает ток",grLabel:"Гирлянда из лампочек и батарейка",ruLabel:"Параллельные ветви и последовательные лампы",
 types:["Последовательно","Параллельно"],states:["Исправна","Перегорела"],
 yes:"идёт",no:"нет (цепь разорвана)",
 cuFb:"Чем больше заряда за секунду, тем больше ток: 1 А = 1 Кл/с.",
 grFb:["В последовательной цепи один обрыв гасит все лампочки.","В параллельной цепи у каждой лампочки своя ветвь, и обрыв в одной не влияет на другие."]},
 en:{
 cuLabel:"A wire with electrons: the dot density shows the current",grLabel:"A garland of bulbs and a battery",ruLabel:"Parallel branches and bulbs in series",
 types:["In series","In parallel"],states:["Works","Burnt out"],
 yes:"flows",no:"no (circuit broken)",
 cuFb:"The more charge per second, the greater the current: 1 A = 1 C/s.",
 grFb:["In a series circuit one break turns off all the bulbs.","In a parallel circuit each bulb has its own branch, and a break in one does not affect the others."]}};
const EL=1.602e-19;
function drawCu(){const t=tt(),q=+$("cq").value,s=+$("ct").value,I=q/s;
 let g='<rect x="40" y="70" width="520" height="70" rx="35" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/>';
 const n=Math.max(1,Math.min(60,Math.round(I*4)));
 for(let i=0;i<n;i++){const x=70+((i*97)%440),y=88+((i*41)%36);g+='<circle cx="'+x+'" cy="'+y+'" r="4" fill="#3f5f8f"/>'}
 g+=arrow(500,170,200,170,"#3f5f8f",3)+svgText(350,196,(lang==="ru"?"движение электронов":"electron motion"),"#3f5f8f","middle",11);
 g+=arrow(100,40,400,40,"#b6533f",3)+svgText(250,30,(lang==="ru"?"условное направление тока":"conventional current direction"),"#b6533f","middle",11);
 $("cuSvg").innerHTML=g;
 $("cqOut").textContent=q+(lang==="ru"?" Кл":" C");$("ctOut").textContent=s+UN[lang].s;
 $("cI").textContent=fmt(I,2)+(lang==="ru"?" А":" A");
 const N=I/EL;$("cN").textContent=N.toExponential(1).replace(/e\+(\d+)/,function(m,k){return "·10"+k.split("").map(function(c){return "⁰¹²³⁴⁵⁶⁷⁸⁹"[+c]}).join("")}).replace(".",lang==="ru"?",":".");
 $("cuFb").textContent=t.cuFb}
["cq","ct"].forEach(id=>$(id).addEventListener("input",drawCu));
function bulb(x,y,on){return '<circle cx="'+x+'" cy="'+y+'" r="16" fill="'+(on?"#f3d34a":"#d6d3c8")+'" stroke="#18181a" stroke-width="2"/>'+(on?'<g stroke="#e0b82f" stroke-width="2"><line x1="'+x+'" y1="'+(y-24)+'" x2="'+x+'" y2="'+(y-30)+'"/><line x1="'+(x-22)+'" y1="'+(y-12)+'" x2="'+(x-27)+'" y2="'+(y-16)+'"/><line x1="'+(x+22)+'" y1="'+(y-12)+'" x2="'+(x+27)+'" y2="'+(y-16)+'"/></g>':'')+'<line x1="'+(x-10)+'" y1="'+(y-10)+'" x2="'+(x+10)+'" y2="'+(y+10)+'" stroke="#18181a"/><line x1="'+(x+10)+'" y1="'+(y-10)+'" x2="'+(x-10)+'" y2="'+(y+10)+'" stroke="#18181a"/>'}
function drawGr(){const t=tt(),ty=+$("gt").value,n=+$("gn").value,bad=+$("gb").value===1;
 let g='';let lit=0,cur=true;
 if(ty===0){
  cur=!bad;const sp=480/(n+1);
  g+='<line x1="50" y1="180" x2="550" y2="180" stroke="#18181a" stroke-width="2"/><line x1="50" y1="60" x2="550" y2="60" stroke="#18181a" stroke-width="2"/><line x1="50" y1="60" x2="50" y2="180" stroke="#18181a" stroke-width="2"/><line x1="550" y1="60" x2="550" y2="180" stroke="#18181a" stroke-width="2"/>';
  g+='<rect x="30" y="100" width="40" height="40" fill="#e8e4d8" stroke="#18181a"/>'+svgText(50,125,"+ −","#18181a","middle",12);
  for(let i=0;i<n;i++){const on=cur;g+=bulb(90+i*sp+sp/2*0.6+20,60,on&&true);if(on)lit++}
  if(!cur){g+=svgText(300,220,"×","#b6533f","middle",24)}
 }else{
  const sp=420/n;
  g+='<line x1="50" y1="40" x2="550" y2="40" stroke="#18181a" stroke-width="2"/><line x1="50" y1="220" x2="550" y2="220" stroke="#18181a" stroke-width="2"/><line x1="50" y1="40" x2="50" y2="220" stroke="#18181a" stroke-width="2"/>';
  g+='<rect x="30" y="100" width="40" height="40" fill="#e8e4d8" stroke="#18181a"/>'+svgText(50,125,"+ −","#18181a","middle",12);
  for(let i=0;i<n;i++){const x=110+i*sp+sp/2-20,on=!(bad&&i===1);g+='<line x1="'+x+'" y1="40" x2="'+x+'" y2="220" stroke="#18181a" stroke-width="2"/>'+bulb(x,130,on);if(on)lit++}
  g+='<line x1="550" y1="40" x2="550" y2="220" stroke="#18181a" stroke-width="2"/>';
 }
 $("grSvg").innerHTML=g;
 $("gnOut").textContent=n;
 $("gL").textContent=lit+" / "+n;$("gC").textContent=ty===0?(cur?t.yes:t.no):t.yes;$("grFb").textContent=t.grFb[ty];}
["gt","gn","gb"].forEach(id=>$(id).addEventListener("input",drawGr));
function drawRu(){const t=tt(),a=+$("i1").value,b=+$("i2").value,c=+$("u1").value,d=+$("u2").value;
 let g='<line x1="40" y1="125" x2="110" y2="125" stroke="#18181a" stroke-width="2"/><line x1="110" y1="60" x2="110" y2="190" stroke="#18181a" stroke-width="2"/><line x1="110" y1="60" x2="230" y2="60" stroke="#18181a" stroke-width="2"/><line x1="110" y1="190" x2="230" y2="190" stroke="#18181a" stroke-width="2"/><line x1="230" y1="60" x2="230" y2="190" stroke="#18181a" stroke-width="2"/><line x1="230" y1="125" x2="290" y2="125" stroke="#18181a" stroke-width="2"/>';
 g+=svgText(170,52,"I₁ = "+fmt(a,1)+" A","#b6533f","middle",12)+svgText(170,210,"I₂ = "+fmt(b,1)+" A","#b6533f","middle",12)+svgText(55,118,"I = "+fmt(a+b,1)+" A","#18181a","start",12);
 g+='<line x1="330" y1="125" x2="560" y2="125" stroke="#18181a" stroke-width="2"/>'+bulb(400,125,true)+bulb(500,125,true)+svgText(400,170,fmt(c,1)+" V","#3f5f8f","middle",12)+svgText(500,170,fmt(d,1)+" V","#3f5f8f","middle",12)+svgText(450,90,"U = "+fmt(c+d,1)+" V","#18181a","middle",13);
 $("ruSvg").innerHTML=g;
 $("i1Out").textContent=fmt(a,1)+" A";$("i2Out").textContent=fmt(b,1)+" A";$("u1Out").textContent=fmt(c,1)+" V";$("u2Out").textContent=fmt(d,1)+" V";
 $("rI").textContent=fmt(a+b,1)+(lang==="ru"?" А":" A");$("rU").textContent=fmt(c+d,1)+(lang==="ru"?" В":" V");$("ruFb").textContent=lang==="ru"?"Токи параллельных ветвей складываются; напряжения последовательных участков тоже.":"Currents of parallel branches add; so do voltages of series parts."}
["i1","i2","u1","u2"].forEach(id=>$(id).addEventListener("input",drawRu));
const LAB={ru:{cuSvg:T.ru.cuLabel,grSvg:T.ru.grLabel,ruSvg:T.ru.ruLabel},en:{cuSvg:T.en.cuLabel,grSvg:T.en.grLabel,ruSvg:T.en.ruLabel}};
function drawAll(){fillSel("gt",T[lang].types,0);fillSel("gb",T[lang].states,0);drawCu();drawGr();drawRu()}
'''

c = dict(n='16', slug='16-electric-circuits.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Электрический ток и цепи', 'Electric current and circuits'),
 desc='Глава 16 Атласа физики: электрический ток, сила тока, ампер, последовательное и параллельное соединение.',
 lead=('Почему в новогодней гирлянде гаснет всё сразу, а лампочки в квартире горят независимо. Ток, цепи, последовательное и параллельное соединение.',
       'Why a whole New Year garland goes out at once while bulbs in a flat burn independently. Current, circuits, series and parallel connection.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('current', 'Ток', 'Current'), ('circuits', 'Соединения', 'Connections'), ('rules', 'Правила', 'The rules'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>В старой новогодней гирлянде одна лампочка перегорела — и погасла вся гирлянда. Приходится по очереди проверять каждую. А в квартире, если перегорела лампа в люстре, остальные светят как ни в чём не бывало, и холодильник продолжает работать.</p><p>Чем отличается подключение гирлянды от проводки квартиры?</p>',
         '<p>In an old New Year garland one bulb burnt out — and the whole garland went dark. You have to check every one in turn. But in a flat, if one lamp in a chandelier burns out the others shine as before, and the fridge keeps running.</p><p>How does the wiring of the garland differ from that of a flat?</p>'),
 hint=('Подсказку даст модель «Гирлянда: последовательно и параллельно». Разгадка — в конце главы.', 'The “A garland: series and parallel” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: почему гаснет вся гирлянда', 'The answer: why the whole garland goes out'),
 answer=('<p>Лампочки старой гирлянды соединены последовательно: ток идёт по одному пути через все лампочки подряд. Когда нить одной перегорает, цепь разрывается, и ток пропадает везде. Приходится искать неисправную.</p><p>В квартире все приборы включены параллельно: у каждого свой путь к сети, и на каждом одно и то же напряжение 220 В. Если один прибор выключен или сломан, остальные его «не замечают» (модель 2).</p>',
         '<p>The bulbs of an old garland are connected in series: the current takes a single path through all the bulbs one after another. When one filament burns out the circuit is broken and the current stops everywhere. You have to search for the faulty one.</p><p>In a flat all appliances are connected in parallel: each has its own path to the mains and the same 220 V across it. If one is off or broken the others “do not notice” (model 2).</p>'),
 sources=[
  ('Электрический ток, сила тока, ампер, последовательное и параллельное соединение —', 'Electric current, the ampere, series and parallel connection —', LINK('https://openstax.org/books/university-physics-volume-2/pages/9-introduction', 'OpenStax University Physics, Vol. 2, гл. 9–10')),
  ('Скорость дрейфа электронов, концентрация электронов в меди 8,5·10²⁸ м⁻³ —', 'Drift velocity, electron density in copper 8.5·10²⁸ m⁻³ —', LINK('https://en.wikipedia.org/wiki/Drift_velocity', 'Wikipedia: Drift velocity')),
  ('Напряжение сети в Кыргызстане 220 В —', 'Mains voltage in Kyrgyzstan 220 V —', LINK('https://www.cia.gov/the-world-factbook/countries/kyrgyzstan/travel-facts', 'CIA World Factbook: Kyrgyzstan travel facts'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original.'),
 prev=('15-electric-field.html', 'Глава 15 · Электрическое поле', 'Chapter 15 · The electric field'),
 next=('17-ohms-law.html', 'Глава 17 · Закон Ома', 'Chapter 17 · Ohm’s law'),
 js=js)
build(c)
