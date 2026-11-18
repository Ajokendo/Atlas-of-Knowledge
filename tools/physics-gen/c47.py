# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ПЕРЕМЕННОЕ НАПРЯЖЕНИЕ', 'ALTERNATING VOLTAGE', 'acSvg', '0 0 600 250',
  slider('au', 'Действующее напряжение', 'RMS voltage', 12, 500, 1, 220) + slider('af', 'Частота', 'Frequency', 10, 100, 1, 50) + slider('at', 'Момент времени', 'Moment of time', 0, 40, 0.5, 5),
  stats([('aM', 'Амплитуда U_m = √2·U', 'Amplitude U_m = √2·U'), ('aT', 'Период T = 1/f', 'Period T = 1/f'), ('aW', 'Угловая частота ω = 2πf', 'Angular frequency ω = 2πf'), ('aI', 'Мгновенное значение в этот момент', 'Instantaneous value at this moment')]),
  'acFb', 'Схема условная: показаны около двух периодов; время отсчитывается в миллисекундах; напряжение синусоидальное.',
  'A schematic drawing: about two periods are shown; the time is in milliseconds; the voltage is sinusoidal.')
s1 = section('rms', 'Что значит «220 вольт»', 'What “220 volts” means',
 bd('<p>В розетке напряжение меняется по синусоиде: <em>u = U<sub>m</sub>·sin(ωt)</em>, где <em>ω = 2πf</em>. Частота сети <em>f = 50 Гц</em> — 50 полных колебаний в секунду. Число «220 В» — не максимум, а <strong>действующее значение</strong>: такое постоянное напряжение выделяло бы на резисторе столько же тепла. Для синусоиды <em>U = U<sub>m</sub>/√2</em>, значит амплитуда <em>U<sub>m</sub> = √2·220 ≈ 311 В</em>.</p>',
    '<p>In a socket the voltage varies sinusoidally: <em>u = U<sub>m</sub>·sin(ωt)</em> where <em>ω = 2πf</em>. The mains frequency is <em>f = 50 Hz</em> — 50 full oscillations per second. The number “220 V” is not the maximum but the <strong>root-mean-square (RMS) value</strong>: a constant voltage of that value would release the same heat in a resistor. For a sinusoid <em>U = U<sub>m</sub>/√2</em> so the amplitude is <em>U<sub>m</sub> = √2·220 ≈ 311 V</em>.</p>')
 + formula('U = U_m / √2,   ω = 2π·f', 'мощность лампы P = U²/R считается по действующему значению', 'the power of a lamp P = U²/R is calculated from the RMS value')
 + bd('<p>Переменный ток удобен тем, что его напряжение легко менять трансформатором (глава 24). Поэтому по линиям высокого напряжения — например, по линии Датка–Кемин длиной около 450 км, которая соединила юг и север Кыргызстана в обход соседних стран, — энергию передают при очень высоком напряжении, а у потребителя понижают до 220 В.</p>',
      '<p>Alternating current is convenient because its voltage is easily changed by a transformer (chapter 24). That is why along high-voltage lines — for example the Datka–Kemin line of about 450 km that linked the south and north of Kyrgyzstan bypassing neighbouring countries — energy is sent at a very high voltage and stepped down to 220 V at the consumer.</p>'),
 lab1)

lab2 = model(2, 'КОНДЕНСАТОР И КАТУШКА В ЦЕПИ', 'A CAPACITOR AND A COIL IN THE CIRCUIT', 'xcSvg', '0 0 600 250',
  slider('xf', 'Частота', 'Frequency', 1, 1000, 1, 50) + slider('xc', 'Ёмкость', 'Capacitance', 1, 100, 1, 10) + slider('xl', 'Индуктивность', 'Inductance', 1, 1000, 1, 100),
  stats([('xC', 'Сопротивление конденсатора X_C = 1/(ω·C)', 'Capacitor reactance X_C = 1/(ω·C)'), ('xL', 'Сопротивление катушки X_L = ω·L', 'Coil reactance X_L = ω·L'), ('xI', 'Ток через конденсатор при 220 В', 'Current through the capacitor at 220 V')]),
  'xcFb', 'Схема условная: ёмкость в микрофарадах, индуктивность в миллигенри; идеальные элементы без активного сопротивления.',
  'A schematic drawing: the capacitance in microfarads, the inductance in millihenries; ideal elements without resistance.')
s2 = section('reactance', 'Конденсатор и катушка: реактивное сопротивление', 'The capacitor and the coil: reactance',
 bd('<p>Постоянный ток конденсатор не пропускает, а переменный — пропускает: он то заряжается, то разряжается. Чем выше частота и ёмкость, тем легче току: <em>X<sub>C</sub> = 1/(ω·C)</em>. Катушка ведёт себя наоборот: переменный ток создаёт в ней меняющийся магнитный поток, и ЭДС индукции (глава 23) сопротивляется изменению тока: <em>X<sub>L</sub> = ω·L</em>; постоянный ток она пропускает почти свободно. Эти «сопротивления» не выделяют тепла — энергия то запасается в поле, то возвращается в цепь.</p>',
    '<p>A capacitor does not pass direct current but passes alternating current: it charges and discharges in turn. The higher the frequency and capacitance the easier for the current: <em>X<sub>C</sub> = 1/(ω·C)</em>. A coil behaves the opposite way: alternating current creates a changing magnetic flux in it and the induced emf (chapter 23) opposes the change of current: <em>X<sub>L</sub> = ω·L</em>; direct current it passes almost freely. These “resistances” release no heat — energy is stored in the field then returned to the circuit.</p>')
 + formula('X_C = 1 / (2π·f·C),   X_L = 2π·f·L', 'с ростом частоты X_C убывает, X_L растёт', 'as the frequency grows X_C decreases and X_L increases'),
 lab2)

lab3 = model(3, 'РЕЗОНАНС В КОНТУРЕ', 'RESONANCE IN A CIRCUIT', 'rzSvg', '0 0 600 250',
  slider('zr', 'Сопротивление R', 'Resistance R', 1, 100, 1, 10) + slider('zl', 'Индуктивность L', 'Inductance L', 10, 500, 10, 100) + slider('zc', 'Ёмкость C', 'Capacitance C', 1, 100, 1, 10) + slider('zf', 'Частота источника', 'Source frequency', 20, 600, 1, 50),
  stats([('zF', 'Резонансная частота f₀ = 1/(2π·√(LC))', 'Resonant frequency f₀ = 1/(2π·√(LC))'), ('zZ', 'Полное сопротивление Z = √(R² + (X_L − X_C)²)', 'Impedance Z = √(R² + (X_L − X_C)²)'), ('zI', 'Ток при напряжении 10 В', 'Current at a voltage of 10 V')]),
  'rzFb', 'Схема условная: последовательный контур R–L–C; R — в омах, L — в миллигенри, C — в микрофарадах; кривая — ток в зависимости от частоты при 10 В.',
  'A schematic drawing: a series R–L–C circuit; R in ohms, L in millihenries, C in microfarads; the curve is the current against frequency at 10 V.')
s3 = section('resonance', 'Резонанс — основа настройки радио', 'Resonance — the basis of radio tuning',
 bd('<p>В последовательной цепи с R, L и C полное сопротивление <em>Z = √(R² + (X<sub>L</sub> − X<sub>C</sub>)²)</em>. На частоте <strong>резонанса</strong> <em>f₀ = 1/(2π·√(LC))</em> реактивные сопротивления катушки и конденсатора равны и компенсируют друг друга: <em>Z = R</em> — минимум, а ток максимален. Меняя ёмкость, радиоприёмник настраивают так, чтобы <em>f₀</em> совпала с частотой нужной станции — остальные станции подавляются.</p>',
    '<p>In a series circuit with R, L and C the impedance is <em>Z = √(R² + (X<sub>L</sub> − X<sub>C</sub>)²)</em>. At the <strong>resonance</strong> frequency <em>f₀ = 1/(2π·√(LC))</em> the reactances of the coil and the capacitor are equal and cancel: <em>Z = R</em> — the minimum and the current is greatest. By changing the capacitance a radio receiver is tuned so that <em>f₀</em> matches the frequency of the wanted station — the other stations are suppressed.</p>')
 + formula('f₀ = 1 / (2π · √(L·C))', 'L = 0,1 Гн, C = 10 мкФ → f₀ ≈ 159 Гц', 'L = 0.1 H, C = 10 µF → f₀ ≈ 159 Hz'),
 lab3)

tasks = [
 task(1, 'Амплитуда напряжения сети', 'The amplitude of the mains voltage', 'Действующее напряжение 220 В. Найдите амплитуду.', 'The RMS voltage is 220 V. Find the amplitude.',
  'U = 220 В', 'U = 220 V', 'U_m = √2 · U = 1,414 · 220 ≈ 311 В.', 'U_m = √2 · U = 1.414 · 220 ≈ 311 V.', '≈ 311 В.', '≈ 311 V.', True),
 task(2, 'Период и угловая частота', 'Period and angular frequency', 'Частота сети 50 Гц. Найдите период и угловую частоту.', 'The mains frequency is 50 Hz. Find the period and the angular frequency.',
  'f = 50 Гц', 'f = 50 Hz', 'T = 1/f = 1/50 = 0,02 с = 20 мс.<br>ω = 2πf = 6,283 · 50 ≈ 314 рад/с.', 'T = 1/f = 1/50 = 0.02 s = 20 ms.<br>ω = 2πf = 6.283 · 50 ≈ 314 rad/s.', '20 мс; 314 рад/с.', '20 ms; 314 rad/s.'),
 task(3, 'Конденсатор в сети', 'A capacitor on the mains', 'Конденсатор 10 мкФ включён в сеть 220 В, 50 Гц. Найдите его сопротивление и ток.', 'A 10 µF capacitor is connected to the 220 V, 50 Hz mains. Find its reactance and the current.',
  'C = 10⁻⁵ Ф, f = 50 Гц', 'C = 10⁻⁵ F, f = 50 Hz', 'X_C = 1/(2πfC) = 1 / (314 · 10⁻⁵) ≈ 318 Ом.<br>I = U/X_C = 220 / 318 ≈ 0,69 А.', 'X_C = 1/(2πfC) = 1 / (314 · 10⁻⁵) ≈ 318 Ω.<br>I = U/X_C = 220 / 318 ≈ 0.69 A.', '≈ 318 Ом; ≈ 0,69 А.', '≈ 318 Ω; ≈ 0.69 A.'),
 task(4, 'Катушка в сети', 'A coil on the mains', 'Катушка 0,1 Гн (без активного сопротивления) при 50 Гц. Найдите сопротивление и ток при 220 В.', 'A 0.1 H coil (without resistance) at 50 Hz. Find the reactance and the current at 220 V.',
  'L = 0,1 Гн', 'L = 0.1 H', 'X_L = 2πfL = 314 · 0,1 ≈ 31,4 Ом.<br>I = 220 / 31,4 ≈ 7,0 А.', 'X_L = 2πfL = 314 · 0.1 ≈ 31.4 Ω.<br>I = 220 / 31.4 ≈ 7.0 A.', '≈ 31,4 Ом; ≈ 7,0 А.', '≈ 31.4 Ω; ≈ 7.0 A.'),
 task(5, 'Резонансная частота', 'The resonant frequency', 'Контур: L = 0,1 Гн, C = 10 мкФ. Найдите резонансную частоту.', 'A circuit: L = 0.1 H, C = 10 µF. Find the resonant frequency.',
  'L = 0,1 Гн, C = 10⁻⁵ Ф', 'L = 0.1 H, C = 10⁻⁵ F', 'LC = 10⁻⁶, √(LC) = 10⁻³ с.<br>f₀ = 1 / (2π · 10⁻³) ≈ 159 Гц.', 'LC = 10⁻⁶, √(LC) = 10⁻³ s.<br>f₀ = 1 / (2π · 10⁻³) ≈ 159 Hz.', '≈ 159 Гц.', '≈ 159 Hz.'),
 task(6, 'Ток в контуре', 'Current in the circuit', 'Для контура задачи 5 с R = 10 Ом и напряжением 10 В найдите ток при резонансе и при 50 Гц.', 'For the circuit of problem 5 with R = 10 Ω and a voltage of 10 V find the current at resonance and at 50 Hz.',
  'R = 10 Ом, U = 10 В', 'R = 10 Ω, U = 10 V', 'Резонанс: Z = R = 10 Ом, I = 10/10 = 1,0 А.<br>50 Гц: X_L = 31,4; X_C = 318,3; Z = √(100 + 287²) ≈ 287 Ом; I = 10/287 ≈ 0,035 А.', 'Resonance: Z = R = 10 Ω, I = 10/10 = 1.0 A.<br>50 Hz: X_L = 31.4; X_C = 318.3; Z = √(100 + 287²) ≈ 287 Ω; I = 10/287 ≈ 0.035 A.', '1,0 А и ≈ 35 мА — в 29 раз меньше.', '1.0 A and ≈ 35 mA — 29 times less.'),
]

quiz = [
 qz('Что означает 220 В в розетке?', 'Действующее значение напряжения', 'Максимальное значение', 'Среднее значение за период', 'Амплитуда 311 В.',
    'What does 220 V in a socket mean?', 'The RMS value of the voltage', 'The maximum value', 'The average over a period', 'The amplitude is 311 V.'),
 qz('Как связаны амплитуда и действующее значение для синусоиды?', 'U = U_m/√2', 'U = U_m', 'U = 2·U_m', 'Действующее меньше амплитуды в √2 раз.',
    'How are the amplitude and the RMS value related for a sinusoid?', 'U = U_m/√2', 'U = U_m', 'U = 2·U_m', 'The RMS value is √2 times less than the amplitude.'),
 qz('Чему равен период сети 50 Гц?', '0,02 с', '0,5 с', '50 с', 'T = 1/f.',
    'What is the period of 50 Hz mains?', '0.02 s', '0.5 s', '50 s', 'T = 1/f.'),
 qz('Как сопротивление конденсатора зависит от частоты?', 'Убывает с ростом частоты', 'Растёт с ростом частоты', 'Не зависит', 'X_C = 1/(ωC).',
    'How does the reactance of a capacitor depend on frequency?', 'It decreases as the frequency grows', 'It grows with frequency', 'It does not depend', 'X_C = 1/(ωC).'),
 qz('Как сопротивление катушки зависит от частоты?', 'Растёт с ростом частоты', 'Убывает', 'Не зависит', 'X_L = ωL.',
    'How does the reactance of a coil depend on frequency?', 'It grows with frequency', 'It decreases', 'It does not depend', 'X_L = ωL.'),
 qz('Выделяют ли конденсатор и идеальная катушка тепло в цепи переменного тока?', 'Нет, энергия возвращается в цепь', 'Да, как резистор', 'Только катушка', 'Реактивные сопротивления не греют.',
    'Do a capacitor and an ideal coil release heat in an AC circuit?', 'No, the energy returns to the circuit', 'Yes, like a resistor', 'Only the coil', 'Reactances do not heat.'),
 qz('Что происходит на резонансной частоте последовательного контура?', 'X_L = X_C, ток максимален', 'Ток равен нулю', 'Z максимально', 'Z = R — минимум.',
    'What happens at the resonant frequency of a series circuit?', 'X_L = X_C and the current is greatest', 'The current is zero', 'Z is greatest', 'Z = R — the minimum.'),
 qz('Как настраивают радиоприёмник на станцию?', 'Подбирают ёмкость или индуктивность так, чтобы f₀ совпала с частотой станции', 'Увеличивают громкость', 'Меняют R', 'Резонанс усиливает нужный сигнал.',
    'How is a radio receiver tuned to a station?', 'The capacitance or inductance is chosen so that f₀ equals the station frequency', 'The volume is increased', 'R is changed', 'Resonance strengthens the wanted signal.'),
]

js = JSL + r'''
const T={ru:{
 acLabel:"Синусоида напряжения",xcLabel:"Реактивные сопротивления на частоте источника",rzLabel:"Резонансная кривая контура",
 acFb:"220 В — действующее значение, амплитуда около 311 В.",xcFb:"Выше частота — легче проходит конденсатор, труднее катушка.",rzFb:"На резонансе ток максимален."},
 en:{
 acLabel:"A voltage sinusoid",xcLabel:"Reactances at the source frequency",rzLabel:"The resonance curve of the circuit",
 acFb:"220 V is the RMS value, the amplitude is about 311 V.",xcFb:"The higher the frequency the easier the capacitor and the harder the coil.",rzFb:"At resonance the current is greatest."}};
function drawAc(){const t=tt(),Ur=+$("au").value,f=+$("af").value,tm=+$("at").value,Um=Math.SQRT2*Ur,Tp=1/f,w=2*Math.PI*f;
 const W=Math.min(2*Tp*1000,100),sx=500/W;let g='<line x1="60" y1="125" x2="560" y2="125" stroke="#c9c2b0"/><line x1="60" y1="20" x2="60" y2="230" stroke="#c9c2b0"/>';let p="";for(let i=0;i<=300;i++){const x=i/300*W;p+=(i?" L":"M")+(60+x*sx)+" "+(125-95*Math.sin(w*x/1000))}
 const u=Um*Math.sin(w*tm/1000);
 g+='<path d="'+p+'" fill="none" stroke="#3f5f8f" stroke-width="3"/><line x1="60" y1="'+(125-95*Ur/Um)+'" x2="560" y2="'+(125-95*Ur/Um)+'" stroke="#b6533f" stroke-dasharray="5 4"/>'+svgText(566,'20',"",'#000',"start",1)+svgText(562,125-95*Ur/Um-4,U("действ.","RMS"),"#b6533f","end",11)+(tm<=W?'<circle cx="'+(60+tm*sx)+'" cy="'+(125-95*Math.sin(w*tm/1000))+'" r="6" fill="#b6533f"/>':'')+svgText(560,242,"t, "+U("мс","ms"),"#66666b","end",11);
 $("acSvg").innerHTML=g;$("auOut").textContent=Ur+" "+U("В","V");$("afOut").textContent=f+" "+U("Гц","Hz");$("atOut").textContent=fmt(tm,1)+" "+U("мс","ms");
 $("aM").textContent=fmt(Um,0)+" "+U("В","V");$("aT").textContent=fmt(Tp*1000,1)+" "+U("мс","ms");$("aW").textContent=fmt(w,0)+" "+U("рад/с","rad/s");$("aI").textContent=fmt(u,0)+" "+U("В","V");$("acFb").textContent=t.acFb}
["au","af","at"].forEach(id=>$(id).addEventListener("input",drawAc));
function drawXc(){const t=tt(),f=+$("xf").value,C=+$("xc").value*1e-6,L=+$("xl").value*1e-3,w=2*Math.PI*f,XC=1/(w*C),XL=w*L,I=220/XC;
 const mx=Math.max(XC,XL,1),h1=XC/mx*170,h2=XL/mx*170;
 let g='<rect x="150" y="'+(210-h1)+'" width="120" height="'+h1+'" fill="#3f5f8f" stroke="#18181a"/><rect x="330" y="'+(210-h2)+'" width="120" height="'+h2+'" fill="#b6533f" stroke="#18181a"/>'+svgText(210,228,"X_C","#18181a","middle",12)+svgText(390,228,"X_L","#18181a","middle",12)+svgText(210,210-h1-6,fmt(XC,1)+" Ω","#18181a","middle",12)+svgText(390,210-h2-6,fmt(XL,1)+" Ω","#18181a","middle",12);
 $("xcSvg").innerHTML=g;$("xfOut").textContent=f+" "+U("Гц","Hz");$("xcOut").textContent=Math.round(C*1e6)+" "+U("мкФ","µF");$("xlOut").textContent=Math.round(L*1e3)+" "+U("мГн","mH");
 $("xC").textContent=fmt(XC,1)+" "+U("Ом","Ω");$("xL").textContent=fmt(XL,1)+" "+U("Ом","Ω");$("xI").textContent=fmt(I,2)+" "+U("А","A");$("xcFb").textContent=t.xcFb}
["xf","xc","xl"].forEach(id=>$(id).addEventListener("input",drawXc));
function drawRz(){const t=tt(),R=+$("zr").value,L=+$("zl").value*1e-3,C=+$("zc").value*1e-6,f=+$("zf").value,f0=1/(2*Math.PI*Math.sqrt(L*C));
 const Z=ff=>{const w=2*Math.PI*ff;return Math.sqrt(R*R+Math.pow(w*L-1/(w*C),2))};const Zf=Z(f),I=10/Zf,Imax=10/R;
 let g='<line x1="60" y1="210" x2="560" y2="210" stroke="#18181a"/><line x1="60" y1="210" x2="60" y2="30" stroke="#18181a"/>';let p="";for(let i=0;i<=200;i++){const ff=20+i/200*580;p+=(i?" L":"M")+(60+i/200*500)+" "+(210-10/Z(ff)/Imax*170)}
 g+='<path d="'+p+'" fill="none" stroke="#3f5f8f" stroke-width="3"/><line x1="'+(60+(f-20)/580*500)+'" y1="30" x2="'+(60+(f-20)/580*500)+'" y2="210" stroke="#b6533f" stroke-dasharray="4 3"/><circle cx="'+(60+(f-20)/580*500)+'" cy="'+(210-I/Imax*170)+'" r="6" fill="#b6533f"/>'+svgText(560,228,U("частота, Гц","frequency, Hz"),"#66666b","end",11);
 if(f0>=20&&f0<=600)g+=svgText(60+(f0-20)/580*500,24,"f₀","#18181a","middle",12);
 $("rzSvg").innerHTML=g;$("zrOut").textContent=R+" "+U("Ом","Ω");$("zlOut").textContent=Math.round(L*1e3)+" "+U("мГн","mH");$("zcOut").textContent=Math.round(C*1e6)+" "+U("мкФ","µF");$("zfOut").textContent=f+" "+U("Гц","Hz");
 $("zF").textContent=fmt(f0,1)+" "+U("Гц","Hz");$("zZ").textContent=fmt(Zf,1)+" "+U("Ом","Ω");$("zI").textContent=fmt(I,3)+" "+U("А","A");$("rzFb").textContent=t.rzFb}
["zr","zl","zc","zf"].forEach(id=>$(id).addEventListener("input",drawRz));
const LAB={ru:{acSvg:T.ru.acLabel,xcSvg:T.ru.xcLabel,rzSvg:T.ru.rzLabel},en:{acSvg:T.en.acLabel,xcSvg:T.en.xcLabel,rzSvg:T.en.rzLabel}};
function drawAll(){drawAc();drawXc();drawRz()}
'''

c = dict(n='47', slug='47-alternating-current.html', block='VIII', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Переменный ток', 'Alternating current'),
 desc='Глава 47 Атласа физики: переменное напряжение, амплитуда и действующее значение, ёмкостное и индуктивное сопротивление, резонанс в контуре, линия Датка–Кемин.',
 lead=('Почему 220 вольт — это не максимум, как конденсатор и катушка ведут себя в цепи и как приёмник выбирает станцию.',
       'Why 220 volts is not the maximum, how a capacitor and a coil behave in a circuit and how a receiver picks a station.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('rms', 'Действующее значение', 'RMS value'), ('reactance', 'Реактивное сопротивление', 'Reactance'), ('resonance', 'Резонанс', 'Resonance'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На лампочке написано «220 В». Но напряжение в розетке не постоянно: 50 раз в секунду оно достигает максимума, 100 раз в секунду проходит через ноль и меняет знак. Вольтметр при этом показывает ровно 220 В, а лампа светит ровно, как от батарейки на 220 В.</p><p>Какое именно напряжение «220 вольт» на самом деле?</p>',
         '<p>A bulb is marked “220 V”. But the voltage in a socket is not constant: 50 times a second it reaches a maximum, 100 times a second it passes through zero and changes sign. The voltmeter shows exactly 220 V and the lamp glows steadily, as from a 220 V battery.</p><p>What voltage exactly is “220 volts”?</p>'),
 hint=stdhint('Переменное напряжение', 'Alternating voltage'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: действующее значение', 'The answer: the RMS value'),
 answer=('<p>«220 В» — действующее значение: такое постоянное напряжение выделило бы на лампе столько же тепла. Мощность пропорциональна квадрату напряжения, а среднее значение квадрата синусоиды равно <em>U<sub>m</sub>²/2</em>, отсюда <em>U = U<sub>m</sub>/√2</em>. Амплитуда сети — около 311 В.</p><p>Лампа мигает с удвоенной частотой, 100 раз в секунду, но нить не успевает остыть, а глаз не успевает заметить; при быстром движении камеры это мерцание иногда видно на видео.</p>',
         '<p>“220 V” is the RMS value: a constant voltage of that value would release as much heat in the lamp. The power is proportional to the square of the voltage and the mean of the square of a sinusoid is <em>U<sub>m</sub>²/2</em>, hence <em>U = U<sub>m</sub>/√2</em>. The amplitude of the mains is about 311 V.</p><p>The lamp flickers at twice the frequency, 100 times a second, but the filament has no time to cool and the eye cannot notice; with a fast-moving camera the flicker is sometimes seen on video.</p>'),
 sources=[
  ('Переменный ток, действующее значение, реактивное сопротивление, резонанс —', 'Alternating current, the RMS value, reactance, resonance —', LINK('https://openstax.org/books/university-physics-volume-2/pages/15-introduction', 'OpenStax University Physics, Vol. 2, гл. 15') + ', ' + LINK('https://en.wikipedia.org/wiki/Root_mean_square', 'Wikipedia: Root mean square')),
  ('Линия Датка–Кемин (около 450 км, связала юг и север Кыргызстана в обход соседей) —', 'The Datka–Kemin line (about 450 km, linked the south and north of Kyrgyzstan bypassing neighbours) —', LINK('https://thebulletin.news/?p=610', 'The Bulletin') + ', ' + LINK('https://transformer-magazine.com/news/kyrgyzstan-secures-independent-power-grid/', 'Transformer Magazine'))],
 note=stdnote('Идеальные катушка и конденсатор — упрощение; у реальных элементов есть активное сопротивление. Значения R, L, C в моделях — учебные.', 'The ideal coil and capacitor are a simplification; real elements have resistance. The values of R, L, C in the models are for teaching.'),
 prev=('46-lorentz-force.html', 'Глава 46 · Сила Лоренца', 'Chapter 46 · The Lorentz force'),
 next=('48-electromagnetic-waves.html', 'Глава 48 · Электромагнитные волны', 'Chapter 48 · Electromagnetic waves'),
 js=js)
build(c)
