# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'МАГНИТ ВХОДИТ В КАТУШКУ', 'A MAGNET ENTERS A COIL', 'mcSvg', '0 0 600 240',
  slider('mn', 'Число витков', 'Number of turns', 50, 2000, 50, 500) + slider('mb', 'Индукция поля магнита', 'Flux density of the magnet', 0.01, 1, 0.01, 0.2) + slider('ms', 'Площадь витка', 'Area of a turn', 5, 100, 5, 20) + slider('mt', 'Время внесения', 'Time of insertion', 0.01, 1, 0.01, 0.1),
  stats([('mF', 'Изменение потока ΔΦ', 'Change of flux ΔΦ'), ('mE', 'ЭДС индукции ε = NΔΦ/Δt', 'Induced EMF ε = NΔΦ/Δt')]),
  'mcFb', 'Схема условная: магнит вдвигается в катушку, поток меняется от 0 до B·S за время Δt; площадь в см².',
  'A schematic drawing: a magnet is pushed into the coil, the flux changes from 0 to B·S in time Δt; the area is in cm².')
s1 = section('faraday', 'Явление электромагнитной индукции', 'The phenomenon of electromagnetic induction',
 bd('<p>В 1831 году Майкл Фарадей обнаружил: если магнитное поле, пронизывающее замкнутый контур, меняется, в контуре возникает электрический ток. Это <strong>электромагнитная индукция</strong>. Постоянное поле тока не вызывает. Нужно, чтобы менялся <strong>магнитный поток</strong> <em>Φ = B·S</em> (единица — вебер, Вб): магнит вдвигают или выдвигают, контур поворачивают, меняют ток в соседней катушке.</p><p>Возникающая <strong>ЭДС индукции</strong> тем больше, чем быстрее меняется поток и чем больше витков:</p>',
    '<p>In 1831 Michael Faraday discovered that if the magnetic field through a closed loop changes, an electric current arises in the loop. This is <strong>electromagnetic induction</strong>. A constant field causes no current. It is the <strong>magnetic flux</strong> <em>Φ = B·S</em> (unit — the weber, Wb) that must change: the magnet is pushed in or out, the loop is turned, the current in a neighbouring coil is changed.</p><p>The resulting <strong>induced EMF</strong> is greater the faster the flux changes and the more turns there are:</p>')
 + formula('ε = N · ΔΦ / Δt', 'знак «минус» в законе (правило Ленца): индукционный ток своим полем противодействует изменению потока', 'the “minus” sign in the law (Lenz’s rule): the induced current opposes the change of flux with its own field')
 + bd('<p>Правило Ленца — это закон сохранения энергии: чтобы вдвинуть магнит в катушку с током, надо совершить работу против его отталкивания. Эта работа и превращается в энергию тока.</p>',
      '<p>Lenz’s rule is the law of conservation of energy: to push a magnet into a coil carrying current one must do work against its repulsion. That work turns into the energy of the current.</p>'),
 lab1)

lab2 = model(2, 'ПРОВОДНИК ДВИЖЕТСЯ В ПОЛЕ', 'A CONDUCTOR MOVES IN A FIELD', 'rdSvg', '0 0 600 250',
  slider('rb', 'Индукция', 'Flux density', 0.1, 1, 0.05, 0.5) + slider('rl', 'Длина проводника', 'Length of the conductor', 0.1, 1, 0.05, 0.4) + slider('rv', 'Скорость', 'Speed', 0.5, 20, 0.5, 5),
  stats([('rE', 'ЭДС ε = B·L·v', 'EMF ε = B·L·v'), ('rI', 'Ток (цепь 0,5 Ом)', 'Current (circuit 0.5 Ω)'), ('rF', 'Тормозящая сила', 'The braking force')]),
  'rdFb', 'Схема условная: проводник скользит по шинам, замкнутым через сопротивление 0,5 Ом; трения нет.',
  'A schematic drawing: the conductor slides on rails closed through a resistance of 0.5 Ω; there is no friction.')
s2 = section('moving', 'Движущийся проводник', 'A moving conductor',
 bd('<p>Если проводник длиной <em>L</em> движется со скоростью <em>v</em> перпендикулярно линиям поля <em>B</em>, в нём возникает ЭДС:</p>',
    '<p>If a conductor of length <em>L</em> moves at speed <em>v</em> perpendicular to the field lines <em>B</em>, an EMF arises in it:</p>')
 + formula('ε = B · L · v', 'в замкнутой цепи с сопротивлением R пойдёт ток I = ε / R', 'in a closed circuit of resistance R a current I = ε / R will flow')
 + bd('<p>Ток в проводнике, находящемся в магнитном поле, испытывает силу Ампера (глава 22), и по правилу Ленца она направлена <em>против</em> движения. Поэтому электрическую энергию получают, только совершая механическую работу.</p>',
      '<p>A current in a conductor in a magnetic field experiences the Ampère force (chapter 22), and by Lenz’s rule it is directed <em>against</em> the motion. So electric energy is obtained only by doing mechanical work.</p>'),
 lab2)

lab3 = model(3, 'ГЕНЕРАТОР ПЕРЕМЕННОГО ТОКА', 'AN ALTERNATING-CURRENT GENERATOR', 'gnSvg', '0 0 600 250',
  slider('gf', 'Частота вращения', 'Rotation frequency', 1, 60, 1, 50) + slider('gn', 'Число витков', 'Number of turns', 10, 200, 10, 50) + slider('gb', 'Индукция', 'Flux density', 0.05, 1, 0.05, 0.3) + slider('gs', 'Площадь рамки', 'Area of the frame', 100, 1000, 50, 500),
  stats([('gE', 'Амплитуда ЭДС', 'Amplitude of the EMF'), ('gR', 'Действующее значение', 'The rms value'), ('gM', 'Оборотов в минуту', 'Revolutions per minute')]),
  'gnFb', 'Схема условная: рамка вращается в однородном поле, ε = N·B·S·ω·sin ωt; площадь в см²; одна пара полюсов.',
  'A schematic drawing: a frame rotates in a uniform field, ε = N·B·S·ω·sin ωt; the area in cm²; one pair of poles.')
s3 = section('generator', 'Генератор', 'The generator',
 bd('<p>Если рамку вращать в магнитном поле, поток через неё непрерывно меняется, и в ней возникает ЭДС, которая меняется по закону синуса. Так устроен <strong>генератор переменного тока</strong>:</p>',
    '<p>If a frame is rotated in a magnetic field the flux through it changes continuously, and an EMF arises in it which changes as a sine. This is the principle of an <strong>alternating-current generator</strong>:</p>')
 + formula('ε = N · B · S · ω · sin(ωt),   ω = 2π · f', 'амплитуда ε₀ = N·B·S·ω; действующее значение ε₀ / √2', 'the amplitude ε₀ = N·B·S·ω; the rms value ε₀ / √2')
 + bd('<p>Переменный ток в розетке имеет частоту 50 Гц: 50 полных колебаний в секунду (100 смен направления). Генератор с одной парой полюсов для этого должен делать 50 оборотов в секунду, то есть 3000 оборотов в минуту. Действующее значение сетевого напряжения 220 В соответствует амплитуде около 311 В.</p>',
      '<p>The alternating current in a socket has a frequency of 50 Hz: 50 full oscillations per second (the direction changes 100 times a second). A generator with one pair of poles must for this make 50 revolutions per second, that is 3,000 revolutions per minute. The rms mains voltage of 220 V corresponds to an amplitude of about 311 V.</p>'),
 lab3)

tasks = [
 task(1, 'ЭДС в катушке', 'EMF in a coil', 'Катушка из 200 витков. Магнитный поток через неё за 0,1 с вырос на 0,005 Вб. Найдите ЭДС индукции.', 'A coil of 200 turns. The magnetic flux through it grew by 0.005 Wb in 0.1 s. Find the induced EMF.',
  'N = 200, ΔΦ = 0,005 Вб, Δt = 0,1 с', 'N = 200, ΔΦ = 0.005 Wb, Δt = 0.1 s', 'ε = N·ΔΦ / Δt = 200 · 0,005 / 0,1 = 10 В.', 'ε = N·ΔΦ / Δt = 200 · 0.005 / 0.1 = 10 V.',
  '10 В.', '10 V.', True),
 task(2, 'Проводник на шинах', 'A conductor on rails', 'Проводник длиной 0,4 м движется со скоростью 5 м/с перпендикулярно полю 0,5 Тл. Найдите ЭДС.', 'A 0.4 m conductor moves at 5 m/s perpendicular to a 0.5 T field. Find the EMF.',
  'L = 0,4 м, v = 5 м/с, B = 0,5 Тл', 'L = 0.4 m, v = 5 m/s, B = 0.5 T', 'ε = B·L·v = 0,5 · 0,4 · 5 = 1 В.', 'ε = B·L·v = 0.5 · 0.4 · 5 = 1 V.',
  '1 В.', '1 V.'),
 task(3, 'Ток и торможение', 'Current and braking', 'Цепь из предыдущей задачи имеет сопротивление 0,5 Ом. Найдите ток и силу Ампера, тормозящую проводник.', 'The circuit of the previous problem has a resistance of 0.5 Ω. Find the current and the Ampère force braking the conductor.',
  'ε = 1 В, R = 0,5 Ом, B = 0,5 Тл, L = 0,4 м', 'ε = 1 V, R = 0.5 Ω, B = 0.5 T, L = 0.4 m', 'I = ε / R = 1 / 0,5 = 2 А.<br>F = B·I·L = 0,5 · 2 · 0,4 = 0,4 Н.', 'I = ε / R = 1 / 0.5 = 2 A.<br>F = B·I·L = 0.5 · 2 · 0.4 = 0.4 N.',
  '2 А и 0,4 Н. Мощность тока: ε·I = 2 Вт; та же мощность, что нужна, чтобы тянуть проводник: F·v = 0,4 · 5 = 2 Вт.', '2 A and 0.4 N. The electric power: ε·I = 2 W; the same as needed to pull the conductor: F·v = 0.4 · 5 = 2 W.'),
 task(4, 'Амплитуда генератора', 'A generator’s amplitude', 'Рамка из 50 витков площадью 0,05 м² вращается с частотой 50 Гц в поле 0,3 Тл. Найдите амплитуду ЭДС.', 'A frame of 50 turns of area 0.05 m² rotates at 50 Hz in a 0.3 T field. Find the amplitude of the EMF.',
  'N = 50, S = 0,05 м², f = 50 Гц, B = 0,3 Тл', 'N = 50, S = 0.05 m², f = 50 Hz, B = 0.3 T', 'ω = 2π·f = 314 рад/с.<br>ε₀ = N·B·S·ω = 50 · 0,3 · 0,05 · 314 ≈ 236 В.', 'ω = 2π·f = 314 rad/s.<br>ε₀ = N·B·S·ω = 50 · 0.3 · 0.05 · 314 ≈ 236 V.',
  'около 236 В, действующее значение 236 / √2 ≈ 167 В.', 'about 236 V, the rms value 236 / √2 ≈ 167 V.'),
 task(5, 'Сколько оборотов', 'How many revolutions', 'Сколько оборотов в минуту делает ротор генератора с одной парой полюсов для получения 50 Гц? А с двумя парами?', 'How many revolutions per minute does the rotor of a generator with one pair of poles make for 50 Hz? And with two pairs?',
  'f = 50 Гц', 'f = 50 Hz', 'Одна пара полюсов: 1 оборот — 1 период, значит 50 об/с = 3000 об/мин.<br>Две пары: за оборот 2 периода, значит 25 об/с = 1500 об/мин.', 'One pair of poles: 1 revolution — 1 period, so 50 rev/s = 3,000 rpm.<br>Two pairs: 2 periods per revolution, so 25 rev/s = 1,500 rpm.',
  '3000 и 1500 об/мин.', '3,000 and 1,500 rpm.'),
 task(6, 'Правило Ленца', 'Lenz’s rule', 'Северный полюс магнита вдвигают в катушку. Каким будет конец катушки со стороны магнита — северным или южным?', 'The north pole of a magnet is pushed into a coil. What will the end of the coil nearer the magnet be — north or south?',
  '—', '—', 'Поток растёт. По правилу Ленца индукционный ток противодействует росту, значит создаёт поле навстречу магниту.<br>Одноимённые полюса отталкиваются.', 'The flux grows. By Lenz’s rule the induced current opposes the growth, so it creates a field against the magnet.<br>Like poles repel.',
  'Северным: катушка отталкивает магнит.', 'North: the coil repels the magnet.'),
]

quiz = [
 ('Что такое электромагнитная индукция?', [('Возникновение тока в контуре при изменении магнитного потока', 'Верно.'), ('Нагрев проводника током', 'Это закон Джоуля — Ленца.'), ('Выделение вещества на электродах', 'Это электролиз.')],
  'What is electromagnetic induction?', [('The arising of a current in a loop when the magnetic flux changes', 'Correct.'), ('Heating of a conductor by current', 'That is the Joule–Lenz law.'), ('Deposition of substance on electrodes', 'That is electrolysis.')], 0),
 ('Возникнет ли ток в катушке, если рядом лежит неподвижный магнит?', [('Нет, поток не меняется', 'Верно.'), ('Да, всегда', 'Нужно изменение потока.'), ('Да, если магнит сильный', 'Сила магнита не заменяет изменения.')],
  'Will a current arise in a coil near which a stationary magnet lies?', [('No, the flux does not change', 'Correct.'), ('Yes, always', 'A change of flux is needed.'), ('Yes, if the magnet is strong', 'The strength does not replace a change.')], 0),
 ('От чего зависит ЭДС индукции в катушке?', [('От скорости изменения потока и числа витков', 'Верно.'), ('От цвета провода', 'Цвет не влияет.'), ('От массы катушки', 'Масса не влияет.')],
  'What does the induced EMF in a coil depend on?', [('The rate of change of flux and the number of turns', 'Correct.'), ('The colour of the wire', 'Colour has no effect.'), ('The mass of the coil', 'Mass has no effect.')], 0),
 ('Что утверждает правило Ленца?', [('Индукционный ток противодействует изменению потока', 'Верно.'), ('Ток всегда усиливает изменение потока', 'Наоборот.'), ('Ток не зависит от потока', 'Он определяется потоком.')],
  'What does Lenz’s rule state?', [('The induced current opposes the change of flux', 'Correct.'), ('The current always strengthens the change of flux', 'It is the opposite.'), ('The current does not depend on flux', 'It is determined by the flux.')], 0),
 ('Формула ЭДС проводника, движущегося в поле:', [('ε = B·L·v', 'Верно.'), ('ε = B / (L·v)', 'Такой формулы нет.'), ('ε = L·v / B', 'Такой формулы нет.')],
  'The formula of the EMF of a conductor moving in a field:', [('ε = B·L·v', 'Correct.'), ('ε = B / (L·v)', 'There is no such formula.'), ('ε = L·v / B', 'There is no such formula.')], 0),
 ('Зачем нужен генератор?', [('Превращает механическую энергию в электрическую', 'Верно.'), ('Превращает электрическую в тепловую', 'Это нагреватель.'), ('Создаёт энергию из ничего', 'Закон сохранения энергии это запрещает.')],
  'What is a generator for?', [('It converts mechanical energy into electrical', 'Correct.'), ('It converts electrical into thermal', 'That is a heater.'), ('It creates energy from nothing', 'The law of conservation of energy forbids it.')], 0),
 ('Частота сети в Кыргызстане:', [('50 Гц', 'Верно.'), ('60 Гц', 'Это стандарт США.'), ('220 Гц', '220 — это вольты.')],
  'The mains frequency in Kyrgyzstan:', [('50 Hz', 'Correct.'), ('60 Hz', 'That is the US standard.'), ('220 Hz', '220 is the voltage in volts.')], 0),
 ('Как изменится амплитуда ЭДС генератора при удвоении частоты вращения?', [('Удвоится', 'Верно: ε₀ ~ ω.'), ('Станет вдвое меньше', 'Она растёт.'), ('Не изменится', 'ε₀ ~ ω.')],
  'How does a generator’s EMF amplitude change when the rotation frequency is doubled?', [('It doubles', 'Correct: ε₀ ~ ω.'), ('It halves', 'It grows.'), ('It does not change', 'ε₀ ~ ω.')], 0),
]

js = r'''
const T={ru:{
 mcLabel:"Магнит вдвигается в катушку",rdLabel:"Проводник скользит по шинам в магнитном поле",gnLabel:"График ЭДС генератора за два периода",
 mcFb:"Чем быстрее меняется поток и чем больше витков, тем больше ЭДС.",rdFb:"Тормозящая сила — расплата за полученную электрическую энергию.",gnFb:"Частота ЭДС равна частоте вращения рамки."},
 en:{
 mcLabel:"A magnet pushed into a coil",rdLabel:"A conductor sliding on rails in a magnetic field",gnLabel:"A graph of a generator’s EMF over two periods",
 mcFb:"The faster the flux changes and the more turns, the greater the EMF.",rdFb:"The braking force is the price of the electric energy obtained.",gnFb:"The EMF frequency equals the rotation frequency of the frame."}};
function drawMc(){const t=tt(),N=+$("mn").value,B=+$("mb").value,S=+$("ms").value*1e-4,dt=+$("mt").value,dF=B*S,E=N*dF/dt;
 let g='<rect x="260" y="80" width="120" height="70" rx="6" fill="#f1efe8" stroke="#18181a" stroke-width="2"/>';
 for(let k=0;k<8;k++)g+='<path d="M'+(270+k*14)+' 72 Q'+(274+k*14)+' 115 '+(270+k*14+8)+' 158" fill="none" stroke="#b87333" stroke-width="3"/>';
 g+='<rect x="90" y="95" width="70" height="40" fill="#3f5f8f" stroke="#18181a"/><rect x="160" y="95" width="70" height="40" fill="#b6533f" stroke="#18181a"/>'+svgText(125,120,"S","#fff","middle",14)+svgText(195,120,"N","#fff","middle",14);
 g+=arrow(60,115,85,115,"#18181a",3);
 const lit=Math.min(1,E/20);
 g+='<circle cx="480" cy="115" r="24" fill="rgb('+Math.round(214+lit*29)+','+Math.round(211+lit*0)+','+Math.round(200-lit*120)+')" stroke="#18181a" stroke-width="2"/><line x1="380" y1="100" x2="456" y2="115" stroke="#18181a"/>'+svgText(480,170,fmt(E,1)+" V","#18181a","middle",14);
 $("mcSvg").innerHTML=g;
 $("mnOut").textContent=N;$("mbOut").textContent=fmt(B,2)+(lang==="ru"?" Тл":" T");$("msOut").textContent=+$("ms").value+(lang==="ru"?" см²":" cm²");$("mtOut").textContent=fmt(dt,2)+UN[lang].s;
 $("mF").textContent=fmt(dF*1e3,2)+(lang==="ru"?" мВб":" mWb");$("mE").textContent=fmt(E,1)+(lang==="ru"?" В":" V");$("mcFb").textContent=t.mcFb}
["mn","mb","ms","mt"].forEach(id=>$(id).addEventListener("input",drawMc));
function drawRd(){const t=tt(),B=+$("rb").value,L=+$("rl").value,v=+$("rv").value,E=B*L*v,I=E/0.5,F=B*I*L;
 const x=100+Math.min(1,v/20)*250;
 let g='<line x1="60" y1="80" x2="540" y2="80" stroke="#18181a" stroke-width="3"/><line x1="60" y1="190" x2="540" y2="190" stroke="#18181a" stroke-width="3"/><rect x="60" y="100" width="22" height="70" fill="#e8e4d8" stroke="#18181a"/>'+svgText(71,140,"R","#18181a","middle",12);
 g+='<line x1="'+(120+x/3)+'" y1="72" x2="'+(120+x/3)+'" y2="198" stroke="#b6533f" stroke-width="6"/>';
 for(let i=0;i<5;i++)for(let j=0;j<3;j++)g+=svgText(180+i*70,110+j*35,"×","#c9c2b0","middle",14);
 g+=arrow(120+x/3,135,120+x/3+60,135,"#18181a",3)+arrow(120+x/3,100,120+x/3-Math.min(60,F*60),100,"#2f6f5d",3);
 $("rdSvg").innerHTML=g;
 $("rbOut").textContent=fmt(B,2)+(lang==="ru"?" Тл":" T");$("rlOut").textContent=fmt(L,2)+(lang==="ru"?" м":" m");$("rvOut").textContent=fmt(v,1)+UN[lang].ms;
 $("rE").textContent=fmt(E,2)+(lang==="ru"?" В":" V");$("rI").textContent=fmt(I,2)+(lang==="ru"?" А":" A");$("rF").textContent=fmt(F,2)+(lang==="ru"?" Н":" N");$("rdFb").textContent=t.rdFb}
["rb","rl","rv"].forEach(id=>$(id).addEventListener("input",drawRd));
function drawGn(){const t=tt(),f=+$("gf").value,N=+$("gn").value,B=+$("gb").value,S=+$("gs").value*1e-4,w=2*Math.PI*f,E0=N*B*S*w;
 const X=x=>50+x*500,Y=e=>125-e/600*100;
 let g='<line x1="50" y1="125" x2="550" y2="125" stroke="#18181a"/><line x1="50" y1="20" x2="50" y2="230" stroke="#18181a"/>';
 [-400,-200,200,400].forEach(v=>g+='<line x1="50" y1="'+Y(v)+'" x2="550" y2="'+Y(v)+'" stroke="#e3e1da"/>'+svgText(44,Y(v)+4,v,"#66666b","end",10));
 const T0=1/f,pts=[];for(let k=0;k<=200;k++){const x=k/200,tm=x*2*T0;pts.push(X(x)+","+Math.max(10,Math.min(240,Y(E0*Math.sin(w*tm)))))}
 g+='<polyline fill="none" stroke="#b6533f" stroke-width="2.5" points="'+pts.join(" ")+'"/>'+svgText(50,14,"ε, V","#18181a","start",11)+svgText(550,245,"2T = "+fmt(2*T0*1000,0)+" ms","#66666b","end",11);
 $("gnSvg").innerHTML=g;
 $("gfOut").textContent=f+(lang==="ru"?" Гц":" Hz");$("gnOut").textContent=N;$("gbOut").textContent=fmt(B,2)+(lang==="ru"?" Тл":" T");$("gsOut").textContent=+$("gs").value+(lang==="ru"?" см²":" cm²");
 $("gE").textContent=fmt(E0,0)+(lang==="ru"?" В":" V");$("gR").textContent=fmt(E0/Math.SQRT2,0)+(lang==="ru"?" В":" V");$("gM").textContent=num(f*60)+(lang==="ru"?" об/мин":" rpm");$("gnFb").textContent=t.gnFb}
["gf","gn","gb","gs"].forEach(id=>$(id).addEventListener("input",drawGn));
const LAB={ru:{mcSvg:T.ru.mcLabel,rdSvg:T.ru.rdLabel,gnSvg:T.ru.gnLabel},en:{mcSvg:T.en.mcLabel,rdSvg:T.en.rdLabel,gnSvg:T.en.gnLabel}};
function drawAll(){drawMc();drawRd();drawGn()}
'''

c = dict(n='23', slug='23-induction.html', block='IV', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Электромагнитная индукция', 'Electromagnetic induction'),
 desc='Глава 23 Атласа физики: опыты Фарадея, ЭДС индукции, правило Ленца, генератор переменного тока.',
 lead=('Велосипедная лампа светит без батарейки, пока крутятся колёса. Электромагнитная индукция, правило Ленца и принцип генератора.',
       'A bicycle lamp shines without a battery as long as the wheels turn. Electromagnetic induction, Lenz’s rule and the principle of the generator.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('faraday', 'Индукция', 'Induction'), ('moving', 'Движущийся проводник', 'A moving conductor'), ('generator', 'Генератор', 'The generator'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На велосипеде стоит динамо-фара. Батареек в ней нет, а лампа светит — но только пока вы едете: остановились — свет гаснет, поехали быстрее — светит ярче. Внутри динамо только катушка и маленький магнит.</p><p>Откуда берётся энергия и почему нужно движение?</p>',
         '<p>A bicycle has a dynamo lamp. It has no batteries yet the lamp shines — but only while you ride: stop and the light goes out, ride faster and it shines brighter. Inside the dynamo there is only a coil and a small magnet.</p><p>Where does the energy come from and why is motion needed?</p>'),
 hint=('Подсказку даст модель «Магнит входит в катушку». Разгадка — в конце главы.', 'The “A magnet enters a coil” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: откуда ток в динамо', 'The answer: where the dynamo’s current comes from'),
 answer=('<p>Колесо вращает магнит рядом с катушкой, и магнитный поток через катушку непрерывно меняется. Меняющийся поток создаёт в катушке ЭДС индукции (закон Фарадея), и по цепи с лампой идёт ток. Остановили колесо — поток перестал меняться, ЭДС нет. Быстрее едете — поток меняется быстрее, ЭДС больше, лампа ярче (модель 1: чем меньше Δt, тем больше ε).</p><p>Энергию даёт ваша мышечная работа: по правилу Ленца ток тормозит магнит, и приходится крутить педали сильнее (модель 2). То же происходит в гигантском генераторе гидроэлектростанции — следующая глава.</p>',
         '<p>The wheel turns a magnet next to a coil and the magnetic flux through the coil changes continuously. A changing flux creates an induced EMF in the coil (Faraday’s law) and current flows through the circuit with the lamp. Stop the wheel and the flux stops changing, so there is no EMF. Ride faster and the flux changes faster, the EMF is greater and the lamp brighter (model 1: the smaller Δt, the greater ε).</p><p>The energy comes from your muscle work: by Lenz’s rule the current brakes the magnet and you have to pedal harder (model 2). The same happens in the giant generator of a hydroelectric station — the next chapter.</p>'),
 sources=[
  ('Закон индукции Фарадея, правило Ленца, ЭДС движущегося проводника —', 'Faraday’s law of induction, Lenz’s rule, the EMF of a moving conductor —', LINK('https://openstax.org/books/university-physics-volume-2/pages/13-introduction', 'OpenStax University Physics, Vol. 2, гл. 13') + ', ' + LINK('https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction', 'Wikipedia: Faraday’s law of induction')),
  ('Частота сети 50 Гц и напряжение 220 В в Кыргызстане —', 'Mains frequency 50 Hz and voltage 220 V in Kyrgyzstan —', LINK('https://www.cia.gov/the-world-factbook/countries/kyrgyzstan/travel-facts', 'CIA World Factbook: Kyrgyzstan travel facts')),
  ('Генератор переменного тока —', 'The alternating-current generator —', LINK('https://en.wikipedia.org/wiki/Electric_generator', 'Wikipedia: Electric generator'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Сопротивление цепи 0,5 Ом и значения параметров моделей — условные.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. The circuit resistance of 0.5 Ω and the model parameters are assumed.'),
 prev=('22-magnetic-field-of-current.html', 'Глава 22 · Магнитное поле тока', 'Chapter 22 · The magnetic field of a current'),
 next=('24-power-grid.html', 'Глава 24 · ГЭС и электросеть', 'Chapter 24 · Hydropower and the grid'),
 js=js)
build(c)
