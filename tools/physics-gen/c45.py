# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ПЛОСКИЙ КОНДЕНСАТОР', 'A PARALLEL-PLATE CAPACITOR', 'cpSvg', '0 0 600 250',
  select('cd', 'Диэлектрик между обкладками', 'Dielectric between the plates') + slider('cs', 'Площадь обкладки', 'Area of a plate', 10, 1000, 10, 100) + slider('cg', 'Расстояние между обкладками', 'Distance between the plates', 0.1, 5, 0.1, 1) + slider('cu', 'Напряжение', 'Voltage', 1, 5000, 1, 100),
  stats([('cC', 'Ёмкость C = ε₀·ε·S/d', 'Capacitance C = ε₀·ε·S/d'), ('cQ', 'Заряд Q = C·U', 'Charge Q = C·U'), ('cW', 'Энергия W = C·U²/2', 'Energy W = C·U²/2'), ('cE', 'Напряжённость поля E = U/d', 'Field strength E = U/d')]),
  'cpFb', 'Схема условная: ε₀ = 8,85·10⁻¹² Ф/м; значения ε округлены и условны (воздух 1, бумага 3, стекло 7, вода 80); пробой воздуха — около 3 МВ/м.',
  'A schematic drawing: ε₀ = 8.85·10⁻¹² F/m; the ε values are rounded and assumed (air 1, paper 3, glass 7, water 80); the breakdown of air is about 3 MV/m.')
s1 = section('capacitance', 'Конденсатор накапливает заряд и энергию', 'A capacitor stores charge and energy',
 bd('<p><strong>Конденсатор</strong> — две проводящие пластины (обкладки) с изолятором между ними. Подключив его к источнику напряжения <em>U</em>, получаем на обкладках заряды <em>+Q</em> и <em>−Q</em>. Отношение <em>C = Q/U</em> — <strong>ёмкость</strong> (единица — фарад, Ф; чаще мкФ, нФ, пФ). Для плоского конденсатора ёмкость тем больше, чем больше площадь пластин <em>S</em>, чем меньше расстояние <em>d</em> и чем выше диэлектрическая проницаемость <em>ε</em> вещества между пластинами.</p><p>Энергия заряженного конденсатора хранится в электрическом поле между пластинами: <em>W = C·U²/2</em>. Если напряжённость поля <em>E = U/d</em> превысит предел для изолятора (воздух — около 3 МВ/м), происходит <strong>пробой</strong> — проскакивает искра.</p>',
    '<p>A <strong>capacitor</strong> is two conducting plates with an insulator between them. Connected to a voltage source <em>U</em> it gets charges <em>+Q</em> and <em>−Q</em> on the plates. The ratio <em>C = Q/U</em> is the <strong>capacitance</strong> (unit — the farad, F; more often µF, nF, pF). For a parallel-plate capacitor the capacitance is greater the larger the plate area <em>S</em>, the smaller the distance <em>d</em> and the higher the dielectric constant <em>ε</em> of the material between the plates.</p><p>The energy of a charged capacitor is stored in the electric field between the plates: <em>W = C·U²/2</em>. If the field strength <em>E = U/d</em> exceeds the limit for the insulator (air — about 3 MV/m) a <strong>breakdown</strong> occurs — a spark jumps.</p>')
 + formula('C = ε₀ · ε · S / d,   W = C·U² / 2', 'сжать пластины вдвое ближе — ёмкость вдвое больше', 'bring the plates twice as close — twice the capacitance'),
 lab1)

lab2 = model(2, 'СОЕДИНЕНИЕ КОНДЕНСАТОРОВ', 'COMBINING CAPACITORS', 'cbSvg', '0 0 600 250',
  select('bm', 'Соединение', 'Connection') + slider('b1', 'Ёмкость C₁', 'Capacitance C₁', 1, 100, 1, 2) + slider('b2', 'Ёмкость C₂', 'Capacitance C₂', 1, 100, 1, 3) + slider('bu', 'Напряжение источника', 'Source voltage', 1, 50, 1, 12),
  stats([('bC', 'Общая ёмкость', 'Total capacitance'), ('bQ', 'Общий заряд, взятый от источника', 'Total charge taken from the source'), ('bW', 'Запасённая энергия', 'Stored energy')]),
  'cbFb', 'Схема условная: ёмкости в микрофарадах; у конденсаторов при последовательном соединении одинаковый заряд.',
  'A schematic drawing: the capacitances are in microfarads; in series the capacitors carry the same charge.')
s2 = section('combine', 'Параллельно и последовательно', 'In parallel and in series',
 bd('<p>При <strong>параллельном</strong> соединении площади как бы складываются: <em>C = C₁ + C₂</em>. При <strong>последовательном</strong> расстояния складываются, а ёмкость меньше любой из частей: <em>1/C = 1/C₁ + 1/C₂</em>. (Для резисторов всё наоборот — глава 16.) Последовательно соединяют конденсаторы, чтобы выдержать большее суммарное напряжение.</p>',
    '<p>In a <strong>parallel</strong> connection the areas effectively add: <em>C = C₁ + C₂</em>. In a <strong>series</strong> connection the distances add and the capacitance is less than either part: <em>1/C = 1/C₁ + 1/C₂</em>. (For resistors it is the other way round — chapter 16.) Capacitors are connected in series to withstand a larger total voltage.</p>')
 + formula('параллельно: C = C₁ + C₂;   последовательно: 1/C = 1/C₁ + 1/C₂', 'проверьте: 2 мкФ и 3 мкФ дают 5 мкФ или 1,2 мкФ', 'check: 2 µF and 3 µF give 5 µF or 1.2 µF'),
 lab2)

lab3 = model(3, 'ЗАРЯДКА КОНДЕНСАТОРА ЧЕРЕЗ РЕЗИСТОР', 'CHARGING A CAPACITOR THROUGH A RESISTOR', 'rcSvg', '0 0 600 250',
  slider('rr', 'Сопротивление', 'Resistance', 1, 100, 1, 10) + slider('rc', 'Ёмкость', 'Capacitance', 1, 1000, 1, 100) + slider('rt', 'Прошло времени', 'Time elapsed', 0, 5, 0.05, 1),
  stats([('rT', 'Постоянная времени τ = R·C', 'Time constant τ = R·C'), ('rV', 'Напряжение на конденсаторе U(t) = U₀·(1 − e^(−t/τ))', 'Voltage on the capacitor U(t) = U₀·(1 − e^(−t/τ))')]),
  'rcFb', 'Схема условная: сопротивление в килоомах, ёмкость в микрофарадах; τ = R·C в секундах (кОм · мкФ = мс); время в секундах; U₀ принято за 100%.',
  'A schematic drawing: the resistance in kilohms, the capacitance in microfarads; τ = R·C in seconds (kΩ · µF = ms); the time in seconds; U₀ is taken as 100%.')
s3 = section('charging', 'Конденсатор заряжается не мгновенно', 'A capacitor does not charge instantly',
 bd('<p>Через резистор заряд накапливается постепенно: ток сначала большой, затем падает по мере роста напряжения на конденсаторе. Напряжение растёт по закону <em>U(t) = U₀·(1 − e<sup>−t/τ</sup>)</em>, где <strong>постоянная времени</strong> <em>τ = R·C</em>. За время τ конденсатор заряжается примерно на 63%, за 3τ — на 95%, за 5τ — более чем на 99%. На этом основаны таймеры, реле времени, вспышки фотоаппарата и сенсорные экраны: экран определяет, где палец, по изменению ёмкости участка поверхности.</p>',
    '<p>Through a resistor the charge builds up gradually: the current is large at first then falls as the voltage on the capacitor grows. The voltage grows as <em>U(t) = U₀·(1 − e<sup>−t/τ</sup>)</em> where the <strong>time constant</strong> is <em>τ = R·C</em>. In time τ the capacitor charges to about 63%, in 3τ — to 95%, in 5τ — to over 99%. Timers, time relays, camera flashes and touch screens are based on this: the screen finds where the finger is by the change in capacitance of a patch of the surface.</p>')
 + formula('τ = R · C', 'кОм · мкФ = мс; 10 кОм · 100 мкФ = 1 с', 'kΩ · µF = ms; 10 kΩ · 100 µF = 1 s'),
 lab3)

tasks = [
 task(1, 'Воздушный конденсатор', 'An air capacitor', 'Площадь пластин 100 см², расстояние 1 мм, между ними воздух (ε = 1). Найдите ёмкость. (ε₀ = 8,85·10⁻¹² Ф/м.)', 'The plate area is 100 cm², the distance 1 mm, with air between (ε = 1). Find the capacitance. (ε₀ = 8.85·10⁻¹² F/m.)',
  'S = 0,01 м², d = 10⁻³ м', 'S = 0.01 m², d = 10⁻³ m', 'C = ε₀·ε·S/d = 8,85·10⁻¹² · 0,01 / 10⁻³ ≈ 8,85·10⁻¹¹ Ф.', 'C = ε₀·ε·S/d = 8.85·10⁻¹² · 0.01 / 10⁻³ ≈ 8.85·10⁻¹¹ F.', '≈ 88,5 пФ.', '≈ 88.5 pF.', True),
 task(2, 'Со стеклом', 'With glass', 'Между пластинами из задачи 1 поместили стекло (ε = 7). Какова ёмкость?', 'Glass (ε = 7) is placed between the plates of problem 1. What is the capacitance?',
  'ε = 7', 'ε = 7', 'C = 7 · 88,5 пФ ≈ 620 пФ.', 'C = 7 · 88.5 pF ≈ 620 pF.', '≈ 620 пФ — в 7 раз больше.', '≈ 620 pF — 7 times greater.'),
 task(3, 'Заряд и энергия', 'Charge and energy', 'Конденсатор 470 мкФ заряжен до 12 В. Найдите заряд и энергию.', 'A 470 µF capacitor is charged to 12 V. Find the charge and the energy.',
  'C = 470·10⁻⁶ Ф, U = 12 В', 'C = 470·10⁻⁶ F, U = 12 V', 'Q = C·U = 470·10⁻⁶ · 12 = 5,64·10⁻³ Кл.<br>W = C·U²/2 = 470·10⁻⁶ · 144 / 2 ≈ 3,38·10⁻² Дж.', 'Q = C·U = 470·10⁻⁶ · 12 = 5.64·10⁻³ C.<br>W = C·U²/2 = 470·10⁻⁶ · 144 / 2 ≈ 3.38·10⁻² J.', '5,64 мКл; 33,8 мДж.', '5.64 mC; 33.8 mJ.'),
 task(4, 'Параллельно и последовательно', 'In parallel and in series', 'Конденсаторы 2 мкФ и 3 мкФ соединили параллельно, затем последовательно. Найдите общую ёмкость в каждом случае.', 'Capacitors of 2 µF and 3 µF are connected in parallel and then in series. Find the total capacitance in each case.',
  'C₁ = 2 мкФ, C₂ = 3 мкФ', 'C₁ = 2 µF, C₂ = 3 µF', 'Параллельно: 2 + 3 = 5 мкФ.<br>Последовательно: C = C₁·C₂/(C₁ + C₂) = 6 / 5 = 1,2 мкФ.', 'Parallel: 2 + 3 = 5 µF.<br>Series: C = C₁·C₂/(C₁ + C₂) = 6 / 5 = 1.2 µF.', '5 мкФ и 1,2 мкФ.', '5 µF and 1.2 µF.'),
 task(5, 'Постоянная времени', 'The time constant', 'R = 10 кОм, C = 100 мкФ. Найдите τ и напряжение (в долях U₀) через 3 с.', 'R = 10 kΩ, C = 100 µF. Find τ and the voltage (as a fraction of U₀) after 3 s.',
  'R = 10⁴ Ом, C = 10⁻⁴ Ф', 'R = 10⁴ Ω, C = 10⁻⁴ F', 'τ = R·C = 10⁴ · 10⁻⁴ = 1 с.<br>t = 3τ: U/U₀ = 1 − e⁻³ = 1 − 0,0498 ≈ 0,95.', 'τ = R·C = 10⁴ · 10⁻⁴ = 1 s.<br>t = 3τ: U/U₀ = 1 − e⁻³ = 1 − 0.0498 ≈ 0.95.', 'τ = 1 с; 95% от U₀.', 'τ = 1 s; 95% of U₀.'),
 task(6, 'Пробой воздуха', 'Air breakdown', 'При каком напряжении проскочит искра в воздушном зазоре 1 мм (предельное поле около 3 МВ/м)?', 'At what voltage will a spark jump across a 1 mm air gap (limiting field about 3 MV/m)?',
  'd = 10⁻³ м, E = 3·10⁶ В/м', 'd = 10⁻³ m, E = 3·10⁶ V/m', 'U = E·d = 3·10⁶ · 10⁻³ = 3000 В.', 'U = E·d = 3·10⁶ · 10⁻³ = 3,000 V.', 'около 3 кВ.', 'about 3 kV.'),
]

quiz = [
 qz('Что такое ёмкость конденсатора?', 'C = Q/U — заряд на единицу напряжения', 'Сила тока в нём', 'Его масса', 'Единица — фарад.',
    'What is the capacitance of a capacitor?', 'C = Q/U — charge per unit voltage', 'The current in it', 'Its mass', 'The unit is the farad.'),
 qz('Как увеличить ёмкость плоского конденсатора?', 'Увеличить площадь или уменьшить расстояние', 'Увеличить расстояние', 'Уменьшить площадь', 'C = ε₀εS/d.',
    'How to increase the capacitance of a parallel-plate capacitor?', 'Increase the area or decrease the distance', 'Increase the distance', 'Decrease the area', 'C = ε₀εS/d.'),
 qz('Где хранится энергия заряженного конденсатора?', 'В электрическом поле между обкладками', 'В проводах', 'В изоляторе как тепло', 'W = CU²/2.',
    'Where is the energy of a charged capacitor stored?', 'In the electric field between the plates', 'In the wires', 'In the insulator as heat', 'W = CU²/2.'),
 qz('Чему равна ёмкость двух параллельных конденсаторов?', 'Сумме ёмкостей', 'Произведению', 'Меньшей из них', 'Площади складываются.',
    'What is the capacitance of two capacitors in parallel?', 'The sum of the capacitances', 'The product', 'The smaller of them', 'The areas add.'),
 qz('Общая ёмкость двух одинаковых конденсаторов C при последовательном соединении?', 'C/2', '2C', 'C', '1/C′ = 2/C.',
    'The total capacitance of two identical capacitors C in series?', 'C/2', '2C', 'C', '1/C′ = 2/C.'),
 qz('Что такое постоянная времени τ?', 'R·C', 'R/C', 'C/R', 'За τ заряд достигает ≈ 63%.',
    'What is the time constant τ?', 'R·C', 'R/C', 'C/R', 'In τ the charge reaches ≈ 63%.'),
 qz('Какую долю конечного напряжения конденсатор достигает за 3τ?', 'Около 95%', 'Около 63%', '100%', '1 − e⁻³ ≈ 0,95.',
    'What fraction of the final voltage does a capacitor reach in 3τ?', 'About 95%', 'About 63%', '100%', '1 − e⁻³ ≈ 0.95.'),
 qz('Что происходит при пробое конденсатора?', 'Проскакивает искра через изолятор', 'Заряд растёт', 'Ёмкость растёт', 'Поле превысило предел изолятора.',
    'What happens in the breakdown of a capacitor?', 'A spark jumps through the insulator', 'The charge grows', 'The capacitance grows', 'The field exceeded the limit of the insulator.'),
]

js = JSL + r'''
const T={ru:{
 cpLabel:"Заряженный плоский конденсатор",cbLabel:"Два конденсатора",rcLabel:"График зарядки через резистор",
 dies:["Воздух (ε = 1)","Бумага (ε = 3)","Стекло (ε = 7)","Вода (ε = 80)"],modes:["Параллельно","Последовательно"],
 ok:"поле в норме",boom:"ПРОБОЙ воздуха!",
 cpFb:"Ближе пластины и больше диэлектрик — больше ёмкость.",cbFb:"Параллельно ёмкости складываются, последовательно — уменьшаются.",rcFb:"Через τ — 63%, через 3τ — 95%."},
 en:{
 cpLabel:"A charged parallel-plate capacitor",cbLabel:"Two capacitors",rcLabel:"A charging curve through a resistor",
 dies:["Air (ε = 1)","Paper (ε = 3)","Glass (ε = 7)","Water (ε = 80)"],modes:["In parallel","In series"],
 ok:"field is within limits",boom:"AIR BREAKDOWN!",
 cpFb:"Closer plates and a stronger dielectric — more capacitance.",cbFb:"In parallel the capacitances add, in series they decrease.",rcFb:"After τ — 63%, after 3τ — 95%."}};
const EPS=[1,3,7,80];
function capStr(C){if(C>=1e-6)return fmt(C*1e6,2)+" "+U("мкФ","µF");if(C>=1e-9)return fmt(C*1e9,2)+" "+U("нФ","nF");return fmt(C*1e12,1)+" "+U("пФ","pF")}
function drawCp(){const t=tt(),k=+$("cd").value,S=+$("cs").value*1e-4,d=+$("cg").value*1e-3,Uv=+$("cu").value,C=8.854e-12*EPS[k]*S/d,Q=C*Uv,W=C*Uv*Uv/2,E=Uv/d,boom=k===0&&E>3e6;
 const gap=10+d*1000*14;let g='<rect x="150" y="60" width="300" height="10" fill="#b87333"/><rect x="150" y="'+(70+gap)+'" width="300" height="10" fill="#b87333"/><rect x="150" y="70" width="300" height="'+gap+'" fill="'+(k===0?"#f4f1e8":"#cfe2ff")+'" opacity="0.7"/>';
 for(let i=0;i<8;i++){g+=svgText(165+i*38,56,"+","#b6533f","middle",14)+svgText(165+i*38,(70+gap+26),"−","#3f5f8f","middle",14)}
 if(boom)g+='<path d="M300 70 l-12 '+(gap/3)+' l16 '+(gap/3)+' l-10 '+(gap/3)+'" fill="none" stroke="#f1c40f" stroke-width="4"/>';
 $("cpSvg").innerHTML=g;$("csOut").textContent=Math.round(S*1e4)+" "+U("см²","cm²");$("cgOut").textContent=fmt(d*1000,1)+" "+U("мм","mm");$("cuOut").textContent=Uv+" "+U("В","V");
 $("cC").textContent=capStr(C);$("cQ").textContent=sci(Q,2)+" "+U("Кл","C");$("cW").textContent=sci(W,2)+" "+U("Дж","J");$("cE").textContent=sci(E,2)+" "+U("В/м","V/m")+" — "+(boom?t.boom:t.ok);$("cpFb").textContent=t.cpFb}
["cd","cs","cg","cu"].forEach(id=>$(id).addEventListener("input",drawCp));
function drawCb(){const t=tt(),m=+$("bm").value,c1=+$("b1").value,c2=+$("b2").value,Uv=+$("bu").value,C=m===0?c1+c2:c1*c2/(c1+c2),Q=C*Uv,W=C*Uv*Uv/2;
 let g='';const y=m===0?[70,170]:[125,125];
 if(m===0){g+='<line x1="150" y1="70" x2="450" y2="70" stroke="#18181a"/><line x1="150" y1="170" x2="450" y2="170" stroke="#18181a"/>'+'<rect x="230" y="60" width="8" height="20" fill="#b87333"/><rect x="240" y="60" width="8" height="20" fill="#b87333"/><rect x="330" y="160" width="8" height="20" fill="#b87333"/><rect x="340" y="160" width="8" height="20" fill="#b87333"/>'+svgText(240,50,"C₁","#18181a","middle",13)+svgText(340,205,"C₂","#18181a","middle",13)}
 else{g+='<line x1="100" y1="125" x2="500" y2="125" stroke="#18181a"/><rect x="220" y="110" width="8" height="30" fill="#b87333"/><rect x="232" y="110" width="8" height="30" fill="#b87333"/><rect x="360" y="110" width="8" height="30" fill="#b87333"/><rect x="372" y="110" width="8" height="30" fill="#b87333"/>'+svgText(230,95,"C₁","#18181a","middle",13)+svgText(370,95,"C₂","#18181a","middle",13)}
 $("cbSvg").innerHTML=g;$("b1Out").textContent=c1+" "+U("мкФ","µF");$("b2Out").textContent=c2+" "+U("мкФ","µF");$("buOut").textContent=Uv+" "+U("В","V");
 $("bC").textContent=fmt(C,2)+" "+U("мкФ","µF");$("bQ").textContent=fmt(Q,1)+" "+U("мкКл","µC");$("bW").textContent=fmt(W,1)+" "+U("мкДж","µJ");$("cbFb").textContent=t.cbFb}
["bm","b1","b2","bu"].forEach(id=>$(id).addEventListener("input",drawCb));
function drawRc(){const t=tt(),R=+$("rr").value,C=+$("rc").value,tm=+$("rt").value,tau=R*C/1000,Uf=1-Math.exp(-tm/tau);
 let g='<line x1="60" y1="210" x2="560" y2="210" stroke="#18181a"/><line x1="60" y1="210" x2="60" y2="30" stroke="#18181a"/>';let p="";const tmax=Math.max(5*tau,5);for(let i=0;i<=100;i++){const x=i/100*tmax;p+=(i?" L":"M")+(60+i/100*500)+" "+(210-(1-Math.exp(-x/tau))*170)}
 g+='<path d="'+p+'" fill="none" stroke="#3f5f8f" stroke-width="3"/><circle cx="'+(60+Math.min(tm/tmax,1)*500)+'" cy="'+(210-Uf*170)+'" r="6" fill="#b6533f"/>'+svgText(560,228,U("время, с","time, s"),"#66666b","end",11)+svgText(66,30,"100%","#66666b","start",11)+svgText(60+tau/tmax*500,226,"τ","#66666b","middle",11);
 $("rcSvg").innerHTML=g;$("rrOut").textContent=R+" "+U("кОм","kΩ");$("rcOut").textContent=C+" "+U("мкФ","µF");$("rtOut").textContent=fmt(tm,2)+" "+U("с","s");
 $("rT").textContent=fmt(tau,2)+" "+U("с","s");$("rV").textContent=fmt(Uf*100,1)+"%";$("rcFb").textContent=t.rcFb}
["rr","rc","rt"].forEach(id=>$(id).addEventListener("input",drawRc));
const LAB={ru:{cpSvg:T.ru.cpLabel,cbSvg:T.ru.cbLabel,rcSvg:T.ru.rcLabel},en:{cpSvg:T.en.cpLabel,cbSvg:T.en.cbLabel,rcSvg:T.en.rcLabel}};
function drawAll(){fillSel("cd",T[lang].dies,0);fillSel("bm",T[lang].modes,0);drawCp();drawCb();drawRc()}
'''

c = dict(n='45', slug='45-capacitor.html', block='VIII', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Конденсатор', 'The capacitor'),
 desc='Глава 45 Атласа физики: электрическая ёмкость, плоский конденсатор, энергия поля, соединение конденсаторов, зарядка через резистор, сенсорный экран.',
 lead=('Как телефон чувствует палец и как вспышка накапливает энергию. Ёмкость, энергия поля и зарядка через резистор.',
       'How a phone senses a finger and how a flash stores energy. Capacitance, field energy and charging through a resistor.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('capacitance', 'Ёмкость', 'Capacitance'), ('combine', 'Соединения', 'Combinations'), ('charging', 'Зарядка', 'Charging'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Экран смартфона реагирует на палец, но не на деревянный карандаш и не на палец в сухой перчатке. При этом палец не нажимает сильно и не замыкает никаких контактов — экран сделан из сплошного стекла.</p><p>Что именно «чувствует» экран?</p>',
         '<p>A smartphone screen reacts to a finger but not to a wooden pencil or a finger in a dry glove. The finger does not press hard or close any contacts — the screen is made of solid glass.</p><p>What exactly does the screen “feel”?</p>'),
 hint=stdhint('Плоский конденсатор', 'A parallel-plate capacitor'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: палец меняет ёмкость', 'The answer: a finger changes the capacitance'),
 answer=('<p>Под стеклом — сетка из тонких проводящих полосок, каждая пара которых образует маленький конденсатор. Палец — проводник, подключённый к земле через тело: приближаясь, он «отбирает» часть электрического поля и меняет ёмкость ближайшего участка. Электроника измеряет ёмкость (например, по времени зарядки <em>τ = R·C</em>) сотни раз в секунду и по изменению находит место касания.</p><p>Дерево — диэлектрик и почти не меняет поле, а сухая перчатка — слой изолятора, поэтому ёмкость почти не меняется.</p>',
         '<p>Under the glass there is a grid of thin conducting strips and each pair forms a small capacitor. A finger is a conductor connected to the ground through the body: approaching, it “takes” part of the electric field and changes the capacitance of the nearest patch. The electronics measures the capacitance (for example by the charging time <em>τ = R·C</em>) hundreds of times a second and finds the touch from the change.</p><p>Wood is a dielectric and barely changes the field while a dry glove is a layer of insulator so the capacitance hardly changes.</p>'),
 sources=[
  ('Ёмкость, конденсаторы, энергия поля, RC-цепи —', 'Capacitance, capacitors, field energy, RC circuits —', LINK('https://openstax.org/books/university-physics-volume-2/pages/8-introduction', 'OpenStax University Physics, Vol. 2, гл. 8') + ', ' + LINK('https://en.wikipedia.org/wiki/Capacitor', 'Wikipedia: Capacitor')),
  ('Ёмкостные сенсорные экраны —', 'Capacitive touch screens —', LINK('https://en.wikipedia.org/wiki/Touchscreen', 'Wikipedia: Touchscreen')),
  ('Электрическая прочность воздуха (≈ 3 МВ/м) —', 'The dielectric strength of air (≈ 3 MV/m) —', LINK('https://en.wikipedia.org/wiki/Dielectric_strength', 'Wikipedia: Dielectric strength'))],
 note=stdnote('Диэлектрические проницаемости округлены и условны; электрическая прочность воздуха зависит от влажности и формы электродов.', 'The dielectric constants are rounded and assumed; the dielectric strength of air depends on humidity and the shape of the electrodes.'),
 prev=('44-ideal-gas.html', 'Глава 44 · Идеальный газ', 'Chapter 44 · The ideal gas'),
 next=('46-lorentz-force.html', 'Глава 46 · Сила Лоренца', 'Chapter 46 · The Lorentz force'),
 js=js)
build(c)
