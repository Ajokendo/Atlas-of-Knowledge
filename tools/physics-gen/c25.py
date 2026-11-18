# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'МАЯТНИК', 'THE PENDULUM', 'pdSvg', '0 0 600 250',
  slider('pl', 'Длина нити', 'String length', 0.1, 10, 0.1, 1) + select('pg', 'Где качается', 'Where it swings') + slider('pt', 'Момент времени', 'Moment in time', 0, 10, 0.1, 0),
  stats([('pT', 'Период T = 2π√(l/g)', 'Period T = 2π√(l/g)'), ('pF', 'Частота f = 1/T', 'Frequency f = 1/T'), ('pA', 'Отклонение в этот момент', 'Deflection at this moment')]),
  'pdFb', 'Схема условная: начальное отклонение 10°, трения нет. Ускорение свободного падения: Земля 9,8; Луна 1,62; Марс 3,71 Н/кг.',
  'A schematic drawing: initial deflection 10°, no friction. Free-fall acceleration: Earth 9.8; Moon 1.62; Mars 3.71 N/kg.')
s1 = section('pend', 'Колебания и маятник', 'Oscillations and the pendulum',
 bd('<p><strong>Колебания</strong> — движения, которые повторяются через равные промежутки времени: качели, струна, поршень двигателя, сердце. Время одного полного колебания — <strong>период</strong> <em>T</em> (секунды), число колебаний в секунду — <strong>частота</strong> <em>f = 1/T</em> (герцы, Гц). Наибольшее отклонение от положения равновесия — <strong>амплитуда</strong>.</p><p>Груз на нити — <strong>математический маятник</strong>. При малых углах его период не зависит ни от массы груза, ни от амплитуды, а только от длины нити и от <em>g</em>:</p>',
    '<p><strong>Oscillations</strong> are motions that repeat at equal intervals of time: a swing, a string, an engine piston, the heart. The time of one full oscillation is the <strong>period</strong> <em>T</em> (seconds), the number of oscillations per second is the <strong>frequency</strong> <em>f = 1/T</em> (hertz, Hz). The greatest deviation from the equilibrium position is the <strong>amplitude</strong>.</p><p>A weight on a string is a <strong>simple pendulum</strong>. For small angles its period depends neither on the mass nor on the amplitude, only on the length of the string and on <em>g</em>:</p>')
 + formula('T = 2π · √(l / g)', 'чтобы период вырос вдвое, нить надо удлинить вчетверо', 'to double the period the string must be made four times longer'),
 lab1)

lab2 = model(2, 'ГРУЗ НА ПРУЖИНЕ', 'A WEIGHT ON A SPRING', 'spSvg', '0 0 600 250',
  slider('sm', 'Масса груза', 'Mass of the weight', 0.1, 5, 0.1, 0.5) + slider('sk', 'Жёсткость пружины', 'Spring stiffness', 10, 500, 10, 50) + slider('sa', 'Амплитуда', 'Amplitude', 1, 10, 1, 5) + slider('st', 'Момент времени', 'Moment in time', 0, 5, 0.05, 0),
  stats([('sT', 'Период T = 2π√(m/k)', 'Period T = 2π√(m/k)'), ('sF', 'Частота', 'Frequency'), ('sV', 'Наибольшая скорость v = Aω', 'Greatest speed v = Aω')]),
  'spFb', 'Схема условная: гладкий стол, пружина подчиняется закону Гука; амплитуда в сантиметрах.',
  'A schematic drawing: a smooth table, the spring obeys Hooke’s law; the amplitude in centimetres.')
s2 = section('spring', 'Пружинный маятник', 'The spring pendulum',
 bd('<p>Груз массой <em>m</em> на пружине жёсткостью <em>k</em> тоже колеблется. Сила упругости всегда направлена к положению равновесия и растёт с отклонением — такие колебания называют <strong>гармоническими</strong>: смещение меняется по закону косинуса, <em>x = A·cos(ωt)</em>, где <em>ω = 2πf</em>.</p>',
    '<p>A weight of mass <em>m</em> on a spring of stiffness <em>k</em> also oscillates. The elastic force always points toward the equilibrium position and grows with the displacement — such oscillations are called <strong>harmonic</strong>: the displacement changes as a cosine, <em>x = A·cos(ωt)</em>, where <em>ω = 2πf</em>.</p>')
 + formula('T = 2π · √(m / k)', 'тяжёлый груз и мягкая пружина — медленные колебания; период не зависит от амплитуды', 'a heavy weight and a soft spring give slow oscillations; the period does not depend on the amplitude')
 + bd('<p>Колебания идут за счёт обмена энергией: в крайних точках она потенциальная (энергия пружины), в середине — кинетическая. Из-за трения амплитуда постепенно уменьшается — колебания <strong>затухают</strong>.</p>',
      '<p>The oscillations run by an exchange of energy: at the extremes it is potential (the energy of the spring), in the middle — kinetic. Because of friction the amplitude gradually decreases — the oscillations are <strong>damped</strong>.</p>'),
 lab2)

lab3 = model(3, 'РЕЗОНАНС', 'RESONANCE', 'rsSvg', '0 0 600 250',
  slider('rf', 'Собственная частота системы', 'Natural frequency of the system', 1, 5, 0.1, 2) + slider('rd', 'Частота толчков', 'Frequency of the pushes', 0.2, 8, 0.1, 1) + select('rz', 'Трение', 'Friction'),
  stats([('rA', 'Амплитуда относительно толчка', 'Amplitude relative to a static push'), ('rR', 'Отношение частот толчков и собственной', 'Ratio of the push frequency to the natural one')]),
  'rsFb', 'Схема условная: кривая резонанса для системы с трением; «1» — амплитуда при очень медленных толчках.',
  'A schematic drawing: the resonance curve of a system with friction; “1” is the amplitude for very slow pushes.')
s3 = section('res', 'Вынужденные колебания и резонанс', 'Forced oscillations and resonance',
 bd('<p>Если систему периодически подталкивать, она совершает <strong>вынужденные колебания</strong> с частотой толчков. Но амплитуда зависит от того, насколько частота толчков близка к собственной частоте системы. Когда они совпадают, амплитуда резко возрастает — это <strong>резонанс</strong>. Чем меньше трение, тем выше и уже пик.</p><p>Резонанс полезен (настройка радиоприёмника, звучание струны и корпуса комуза) и опасен: ритмичная ходьба по мосту, раскачка здания землетрясением с «неудачной» частотой, вибрация мотора на частоте деталей.</p>',
    '<p>If a system is pushed periodically it performs <strong>forced oscillations</strong> at the frequency of the pushes. But the amplitude depends on how close the push frequency is to the natural frequency of the system. When they coincide the amplitude grows sharply — this is <strong>resonance</strong>. The smaller the friction, the higher and narrower the peak.</p><p>Resonance is useful (tuning a radio, the sound of a komuz string and body) and dangerous: rhythmic walking over a bridge, a building shaken by an earthquake at an “unlucky” frequency, a motor’s vibration at the frequency of its parts.</p>'),
 lab3)

tasks = [
 task(1, 'Период маятника', 'Period of a pendulum', 'Найдите период маятника длиной 1 м на Земле. g = 9,8 Н/кг.', 'Find the period of a 1 m pendulum on Earth. g = 9.8 N/kg.',
  'l = 1 м, g = 9,8 Н/кг', 'l = 1 m, g = 9.8 N/kg', 'T = 2π·√(l/g) = 6,283 · √(1/9,8) = 6,283 · 0,3194 ≈ 2,0 с.', 'T = 2π·√(l/g) = 6.283 · √(1/9.8) = 6.283 · 0.3194 ≈ 2.0 s.',
  'около 2,0 с (полпериода — почти ровно секунда).', 'about 2.0 s (half a period is almost exactly one second).', True),
 task(2, 'Секундный маятник', 'A one-second pendulum', 'Какой длины нужен маятник, чтобы его период был 1 с?', 'How long must a pendulum be for its period to be 1 s?',
  'T = 1 с, g = 9,8 Н/кг', 'T = 1 s, g = 9.8 N/kg', 'l = g·T² / (4π²) = 9,8 · 1 / 39,48 ≈ 0,248 м.', 'l = g·T² / (4π²) = 9.8 · 1 / 39.48 ≈ 0.248 m.',
  'около 25 см.', 'about 25 cm.'),
 task(3, 'На Луне', 'On the Moon', 'Каков период того же маятника длиной 1 м на Луне (g = 1,62 Н/кг)?', 'What is the period of the same 1 m pendulum on the Moon (g = 1.62 N/kg)?',
  'l = 1 м, g = 1,62 Н/кг', 'l = 1 m, g = 1.62 N/kg', 'T = 2π·√(1 / 1,62) = 6,283 · 0,7857 ≈ 4,9 с.', 'T = 2π·√(1 / 1.62) = 6.283 · 0.7857 ≈ 4.9 s.',
  'около 4,9 с — в 2,5 раза медленнее, чем на Земле.', 'about 4.9 s — 2.5 times slower than on Earth.'),
 task(4, 'Груз на пружине', 'A weight on a spring', 'Груз 0,5 кг на пружине жёсткостью 50 Н/м. Найдите период и частоту.', 'A 0.5 kg weight on a spring of stiffness 50 N/m. Find the period and frequency.',
  'm = 0,5 кг, k = 50 Н/м', 'm = 0.5 kg, k = 50 N/m', 'T = 2π·√(m/k) = 6,283 · √(0,01) = 0,628 с.<br>f = 1/T ≈ 1,59 Гц.', 'T = 2π·√(m/k) = 6.283 · √(0.01) = 0.628 s.<br>f = 1/T ≈ 1.59 Hz.',
  'T ≈ 0,63 с, f ≈ 1,6 Гц.', 'T ≈ 0.63 s, f ≈ 1.6 Hz.'),
 task(5, 'Груз потяжелее', 'A heavier weight', 'Груз в задаче 4 заменили на 2 кг. Как изменится период?', 'The weight in problem 4 is replaced by 2 kg. How does the period change?',
  'm = 2 кг (в 4 раза больше)', 'm = 2 kg (4 times more)', 'T = 2π·√(2 / 50) = 6,283 · 0,2 = 1,257 с.<br>Масса выросла в 4 раза, период — в √4 = 2 раза.', 'T = 2π·√(2 / 50) = 6.283 · 0.2 = 1.257 s.<br>The mass grew 4 times, the period 2 times (√4).',
  'вырос вдвое: 1,26 с.', 'doubled: 1.26 s.'),
 task(6, 'Как раскачивать качели', 'How to push a swing', 'Качели имеют подвес длиной 3 м (считайте их маятником). Сколько толчков в минуту надо делать, чтобы раскачать их в резонанс?', 'A swing has a 3 m hanger (treat it as a pendulum). How many pushes per minute are needed to build up the swing in resonance?',
  'l = 3 м', 'l = 3 m', 'T = 2π·√(3 / 9,8) = 6,283 · 0,5533 ≈ 3,48 с.<br>f = 1/T ≈ 0,288 Гц, то есть 0,288 · 60 ≈ 17 толчков в минуту.', 'T = 2π·√(3 / 9.8) = 6.283 · 0.5533 ≈ 3.48 s.<br>f = 1/T ≈ 0.288 Hz, that is 0.288 · 60 ≈ 17 pushes per minute.',
  'около 17 толчков в минуту, по одному за каждый период.', 'about 17 pushes per minute, one per period.'),
]

quiz = [
 qz('Что такое период колебаний?', 'Время одного полного колебания', 'Число колебаний в секунду', 'Наибольшее отклонение', 'Период — время одного колебания; число колебаний в секунду — частота.',
    'What is the period of oscillation?', 'The time of one full oscillation', 'The number of oscillations per second', 'The greatest deviation', 'The period is the time of one oscillation; the number per second is the frequency.'),
 qz('От чего зависит период маятника на нити (малые углы)?', 'От длины нити и g', 'От массы груза', 'От амплитуды', 'T = 2π√(l/g): масса и амплитуда не влияют.',
    'What does the period of a string pendulum depend on (small angles)?', 'The string length and g', 'The mass of the weight', 'The amplitude', 'T = 2π√(l/g): mass and amplitude do not matter.'),
 qz('Как изменится период маятника при увеличении длины нити в 4 раза?', 'Вырастет вдвое', 'Вырастет в 4 раза', 'Не изменится', 'Период пропорционален √l, а √4 = 2.',
    'How does a pendulum’s period change when the string is made 4 times longer?', 'It doubles', 'It grows 4 times', 'It does not change', 'The period is proportional to √l and √4 = 2.'),
 qz('На Луне тот же маятник качается…', 'Медленнее, чем на Земле', 'Быстрее, чем на Земле', 'Так же', 'На Луне g меньше, поэтому период T = 2π√(l/g) больше.',
    'On the Moon the same pendulum swings…', 'More slowly than on Earth', 'Faster than on Earth', 'The same', 'On the Moon g is smaller so the period T = 2π√(l/g) is larger.'),
 qz('Как зависит период пружинного маятника от жёсткости пружины?', 'Чем жёстче пружина, тем меньше период', 'Чем жёстче пружина, тем больше период', 'Не зависит', 'T = 2π√(m/k): растёт k — период уменьшается.',
    'How does the period of a spring pendulum depend on the spring stiffness?', 'The stiffer the spring, the shorter the period', 'The stiffer the spring, the longer the period', 'It does not depend', 'T = 2π√(m/k): as k grows the period shrinks.'),
 qz('Что такое резонанс?', 'Резкий рост амплитуды при совпадении частот', 'Остановка колебаний', 'Уменьшение периода', 'При частоте толчков, близкой к собственной, амплитуда растёт.',
    'What is resonance?', 'A sharp growth of amplitude when frequencies coincide', 'The stopping of oscillations', 'A reduction of the period', 'When the push frequency is near the natural one the amplitude grows.'),
 qz('Что делает трение с колебаниями?', 'Они затухают', 'Они усиливаются', 'Период становится нулевым', 'Из-за трения энергия колебаний уходит в тепло.',
    'What does friction do to oscillations?', 'They die away', 'They grow', 'The period becomes zero', 'Because of friction the oscillation energy goes into heat.'),
 qz('Как нужно толкать качели, чтобы раскачать их сильнее всего?', 'В такт их собственным колебаниям', 'Как можно чаще', 'Как можно сильнее, но редко и беспорядочно', 'Нужно подталкивать с частотой, равной собственной частоте качелей.',
    'How should a swing be pushed to build it up most?', 'In time with its own oscillations', 'As often as possible', 'As hard as possible but rarely and at random', 'The pushes must have a frequency equal to the swing’s natural frequency.'),
]

js = r'''
const T={ru:{
 pdLabel:"Маятник на нити с отклонением в выбранный момент",spLabel:"Груз на пружине в выбранный момент",rsLabel:"Кривая резонанса: амплитуда в зависимости от частоты толчков",
 planets:["Земля (g = 9,8)","Луна (g = 1,62)","Марс (g = 3,71)"],fr:["Малое","Среднее","Большое"],
 pdFb:"Попробуйте разные планеты: на Луне маятник качается медленнее.",spFb:"Больше масса или мягче пружина — медленнее колебания.",rsFb:"Пик на кривой — резонанс: частота толчков равна собственной."},
 en:{
 pdLabel:"A pendulum with its deflection at the chosen moment",spLabel:"A weight on a spring at the chosen moment",rsLabel:"The resonance curve: amplitude against the push frequency",
 planets:["Earth (g = 9.8)","Moon (g = 1.62)","Mars (g = 3.71)"],fr:["Low","Medium","High"],
 pdFb:"Try different planets: on the Moon the pendulum swings more slowly.",spFb:"A bigger mass or a softer spring — slower oscillations.",rsFb:"The peak is resonance: the push frequency equals the natural one."}};
const GP=[9.8,1.62,3.71],ZETA=[0.05,0.15,0.4];
function drawPd(){const t=tt(),l=+$("pl").value,g=GP[+$("pg").value],tm=+$("pt").value,T0=2*Math.PI*Math.sqrt(l/g),th=10*Math.cos(2*Math.PI*tm/T0);
 const L=40+Math.min(l,10)/10*150,r=th*Math.PI/180,bx=300+L*Math.sin(r),by=20+L*Math.cos(r);
 let g2='<line x1="240" y1="20" x2="360" y2="20" stroke="#18181a" stroke-width="3"/><line x1="300" y1="20" x2="'+bx+'" y2="'+by+'" stroke="#18181a" stroke-width="2"/><circle cx="'+bx+'" cy="'+by+'" r="12" fill="#b6533f" stroke="#18181a"/>';
 g2+='<line x1="300" y1="20" x2="300" y2="'+(20+L+30)+'" stroke="#c9c2b0" stroke-dasharray="4 3"/>'+svgText(310,'235',"t = "+fmt(tm,1)+UN[lang].s,"#66666b","start",12);
 $("pdSvg").innerHTML=g2;
 $("plOut").textContent=fmt(l,1)+UN[lang].m;$("ptOut").textContent=fmt(tm,1)+UN[lang].s;
 $("pT").textContent=fmt(T0,2)+UN[lang].s;$("pF").textContent=fmt(1/T0,2)+(lang==="ru"?" Гц":" Hz");$("pA").textContent=fmt(th,1)+"°";$("pdFb").textContent=t.pdFb}
["pl","pg","pt"].forEach(id=>$(id).addEventListener("input",drawPd));
function drawSp(){const t=tt(),m=+$("sm").value,k=+$("sk").value,A=+$("sa").value/100,tm=+$("st").value,T0=2*Math.PI*Math.sqrt(m/k),w=2*Math.PI/T0,x=A*Math.cos(w*tm);
 const px=330+x*1200,n=14;let g2='<rect x="40" y="90" width="20" height="90" fill="#9a9a9a" stroke="#18181a"/><line x1="60" y1="190" x2="560" y2="190" stroke="#18181a" stroke-width="2"/>';
 let d='M60 135';for(let i=1;i<=n;i++){const xx=60+(px-60-40)*i/n;d+=' L'+xx+' '+(135+(i%2?-18:18))}d+=' L'+(px-40)+' 135 L'+(px-40)+' 135';
 g2+='<path d="'+d+'" fill="none" stroke="#18181a" stroke-width="2"/><rect x="'+(px-40)+'" y="105" width="80" height="60" fill="#b6533f" stroke="#18181a"/>'+svgText(px,141,fmt(m,1)+UN[lang].kg,"#fff","middle",12);
 g2+='<line x1="330" y1="195" x2="330" y2="205" stroke="#18181a"/>'+svgText(330,220,"0","#66666b","middle",11);
 $("spSvg").innerHTML=g2;
 $("smOut").textContent=fmt(m,1)+UN[lang].kg;$("skOut").textContent=k+(lang==="ru"?" Н/м":" N/m");$("saOut").textContent=+$("sa").value+(lang==="ru"?" см":" cm");$("stOut").textContent=fmt(tm,2)+UN[lang].s;
 $("sT").textContent=fmt(T0,2)+UN[lang].s;$("sF").textContent=fmt(1/T0,2)+(lang==="ru"?" Гц":" Hz");$("sV").textContent=fmt(A*w,2)+UN[lang].ms;$("spFb").textContent=t.spFb}
["sm","sk","sa","st"].forEach(id=>$(id).addEventListener("input",drawSp));
function amp(r,z){return 1/Math.sqrt((1-r*r)*(1-r*r)+4*z*z*r*r)}
function drawRs(){const t=tt(),f0=+$("rf").value,fd=+$("rd").value,z=ZETA[+$("rz").value],r=fd/f0,A=amp(r,z);
 const X=f=>50+f/8*500,Y=a=>220-Math.min(a,11)/11*195;
 let g2='<line x1="50" y1="220" x2="550" y2="220" stroke="#18181a"/><line x1="50" y1="20" x2="50" y2="220" stroke="#18181a"/>';
 [2,4,6,8].forEach(f=>g2+=svgText(X(f),236,f,"#66666b","middle",10));
 [1,5,10].forEach(a=>g2+='<line x1="50" y1="'+Y(a)+'" x2="550" y2="'+Y(a)+'" stroke="#e3e1da"/>'+svgText(44,Y(a)+4,a,"#66666b","end",10));
 const pts=[];for(let k=1;k<=250;k++){const f=k/250*8;pts.push(X(f)+","+Y(amp(f/f0,z)))}
 g2+='<polyline fill="none" stroke="#2f6f5d" stroke-width="2.5" points="'+pts.join(" ")+'"/><circle cx="'+X(fd)+'" cy="'+Y(A)+'" r="6" fill="#b6533f"/>'+svgText(550,250,"f, "+(lang==="ru"?"Гц":"Hz"),"#66666b","end",10)+svgText(56,14,"A","#18181a","start",11);
 $("rsSvg").innerHTML=g2;
 $("rfOut").textContent=fmt(f0,1)+(lang==="ru"?" Гц":" Hz");$("rdOut").textContent=fmt(fd,1)+(lang==="ru"?" Гц":" Hz");
 $("rA").textContent=fmt(A,1)+"×";$("rR").textContent=fmt(r,2);$("rsFb").textContent=t.rsFb}
["rf","rd","rz"].forEach(id=>$(id).addEventListener("input",drawRs));
const LAB={ru:{pdSvg:T.ru.pdLabel,spSvg:T.ru.spLabel,rsSvg:T.ru.rsLabel},en:{pdSvg:T.en.pdLabel,spSvg:T.en.spLabel,rsSvg:T.en.rsLabel}};
function drawAll(){fillSel("pg",T[lang].planets,0);fillSel("rz",T[lang].fr,1);drawPd();drawSp();drawRs()}
'''

c = dict(n='25', slug='25-oscillations.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Колебания', 'Oscillations'),
 desc='Глава 25 Атласа физики: период и частота, математический и пружинный маятник, затухание, вынужденные колебания и резонанс.',
 lead=('Качели, струна, маятниковые часы. Период, частота, амплитуда, маятник на нити и на пружине, резонанс.',
       'A swing, a string, a pendulum clock. Period, frequency, amplitude, the pendulum on a string and on a spring, resonance.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('pend', 'Маятник', 'Pendulum'), ('spring', 'Пружина', 'Spring'), ('res', 'Резонанс', 'Resonance'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Ребёнок сидит на качелях во дворе. Если толкать его как попало — то слева, то справа, то часто, то редко, — качели еле шевелятся. Но стоит толкнуть всего один раз за каждое возвращение к вам, как уже через несколько толчков он взлетает высоко.</p><p>Почему слабые толчки в нужный момент работают лучше сильных в случайный?</p>',
         '<p>A child sits on a swing in a yard. If you push at random — now left, now right, now often, now rarely — the swing hardly moves. But push just once each time it comes back to you and after a few pushes it flies high.</p><p>Why do weak pushes at the right moment work better than strong ones at random?</p>'),
 hint=stdhint('Резонанс', 'Resonance'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: толчки в такт', 'The answer: pushes in time'),
 answer=('<p>Качели — маятник с собственной частотой, которую задаёт длина подвеса. Если подталкивать в такт, каждый толчок прибавляет энергию в тот момент, когда качели движутся в ту же сторону, и амплитуда накапливается. Это резонанс (модель 3). Случайные толчки то ускоряют качели, то тормозят их — энергия не накапливается.</p><p>Поэтому раскачивают качели ритмично, а солдатам на мосту дают команду идти «не в ногу».</p>',
         '<p>A swing is a pendulum with a natural frequency set by the length of its hanger. If you push in time, every push adds energy when the swing is moving the same way and the amplitude builds up. This is resonance (model 3). Random pushes sometimes speed the swing and sometimes brake it — the energy does not accumulate.</p><p>That is why a swing is pushed rhythmically and soldiers on a bridge are told to break step.</p>'),
 sources=[
  ('Период маятника и пружины, гармонические колебания, резонанс —', 'The period of a pendulum and spring, harmonic oscillations, resonance —', LINK('https://openstax.org/books/university-physics-volume-1/pages/15-introduction', 'OpenStax University Physics, Vol. 1, гл. 15') + ', ' + LINK('https://en.wikipedia.org/wiki/Pendulum', 'Wikipedia: Pendulum')),
  ('Ускорение свободного падения на Луне и Марсе —', 'Free-fall acceleration on the Moon and Mars —', LINK('https://en.wikipedia.org/wiki/Surface_gravity', 'Wikipedia: Surface gravity'))],
 note=stdnote('Амплитуда 10°, коэффициенты трения и значения ползунков — условные.', 'The 10° amplitude, the friction values and the slider values are assumed.'),
 prev=('24-power-grid.html', 'Глава 24 · ГЭС и электросеть', 'Chapter 24 · Hydropower and the grid'),
 next=('26-mechanical-waves.html', 'Глава 26 · Механические волны', 'Chapter 26 · Mechanical waves'),
 js=js)
build(c)
