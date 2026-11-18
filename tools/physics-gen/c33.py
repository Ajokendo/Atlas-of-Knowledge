# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ВТОРОЙ ЗАКОН НЬЮТОНА: САНИ', 'NEWTON’S SECOND LAW: A SLEDGE', 'nsSvg', '0 0 600 250',
  slider('nm', 'Масса саней с грузом', 'Mass of the sledge with load', 10, 200, 5, 40) + slider('nf', 'Сила тяги', 'Pulling force', 0, 400, 10, 120) + select('nu', 'Поверхность', 'Surface') + slider('nt', 'Время движения', 'Time of motion', 0, 10, 0.5, 5),
  stats([('nR', 'Сила трения', 'Friction force'), ('nA', 'Ускорение a = F(равн.)/m', 'Acceleration a = F(net)/m'), ('nV', 'Скорость и путь за это время', 'Speed and distance in this time')]),
  'nsFb', 'Схема условная: коэффициенты трения (снег 0,1; земля 0,4; лёд 0,03) выбраны для модели; g = 9,8 Н/кг.',
  'A schematic drawing: the friction coefficients (snow 0.1; ground 0.4; ice 0.03) are chosen for the model; g = 9.8 N/kg.')
s1 = section('second', 'Второй закон Ньютона', 'Newton’s second law',
 bd('<p>Три закона Ньютона — основа механики. <strong>Первый закон</strong> (закон инерции): тело сохраняет скорость, если силы на него не действуют или уравновешены. <strong>Второй закон</strong> связывает силу и ускорение: ускорение тела прямо пропорционально <em>равнодействующей</em> силе и обратно пропорционально массе.</p>',
    '<p>The three laws of Newton are the foundation of mechanics. The <strong>first law</strong> (the law of inertia): a body keeps its velocity if no forces act on it or they are balanced. The <strong>second law</strong> links force and acceleration: the acceleration of a body is directly proportional to the <em>net</em> force and inversely proportional to the mass.</p>')
 + formula('a = F / m   или   F = m · a', 'F — равнодействующая всех сил (векторная сумма); 1 Н = 1 кг·м/с²', 'F is the net force (the vector sum of all forces); 1 N = 1 kg·m/s²')
 + bd('<p>Если тянуть сани с силой <em>F</em>, а трение равно <em>μ·m·g</em>, то равнодействующая <em>F − μmg</em>. Пока тяга меньше трения, сани стоят; больше — разгоняются.</p>',
      '<p>If a sledge is pulled with force <em>F</em> and friction is <em>μ·m·g</em> the net force is <em>F − μmg</em>. While the pull is less than the friction the sledge stands; beyond it, it accelerates.</p>'),
 lab1)

lab2 = model(2, 'ВЕС В ЛИФТЕ', 'WEIGHT IN A LIFT', 'lfSvg', '0 0 600 250',
  slider('lm', 'Ваша масса', 'Your mass', 30, 100, 1, 60) + slider('la', 'Ускорение лифта (вверх +)', 'Acceleration of the lift (up +)', -9.8, 5, 0.1, 0),
  stats([('lP', 'Вес P = m(g + a)', 'Weight P = m(g + a)'), ('lK', 'Показание весов', 'The scale reading'), ('lS', 'Ощущение', 'The feeling')]),
  'lfFb', 'Схема условная: весы показывают силу давления на них; g = 9,8 Н/кг.',
  'A schematic drawing: a scale shows the force of pressure on it; g = 9.8 N/kg.')
s2 = section('lift', 'Вес и невесомость', 'Weight and weightlessness',
 bd('<p><strong>Вес</strong> тела — сила, с которой оно давит на опору или растягивает подвес. В покое он равен силе тяжести <em>mg</em>, но когда опора движется с ускорением, вес меняется. В лифте, едущем с ускорением <em>a</em> вверх: <em>N − mg = ma</em>, поэтому</p>',
    '<p>The <strong>weight</strong> of a body is the force with which it presses on a support or stretches a suspension. At rest it equals the force of gravity <em>mg</em> but when the support moves with an acceleration the weight changes. In a lift going with an acceleration <em>a</em> upward: <em>N − mg = ma</em>, so</p>')
 + formula('P = m · (g + a)', 'при a = −g (свободное падение) вес равен нулю — невесомость', 'at a = −g (free fall) the weight is zero — weightlessness')
 + bd('<p>Космонавты на орбите находятся в невесомости не потому, что гравитации нет (на высоте станции она почти такая же), а потому, что станция и они вместе всё время <em>свободно падают</em> вокруг Земли (глава 36).</p>',
      '<p>Astronauts in orbit are weightless not because there is no gravity (at the station’s height it is almost as strong) but because the station and they together are constantly <em>in free fall</em> around the Earth (chapter 36).</p>'),
 lab2)

lab3 = model(3, 'ПАДЕНИЕ С СОПРОТИВЛЕНИЕМ ВОЗДУХА', 'FALLING WITH AIR RESISTANCE', 'ptSvg', '0 0 600 250',
  slider('pm', 'Масса парашютиста с снаряжением', 'Mass of the parachutist with equipment', 50, 120, 5, 80) + select('pk', 'Положение', 'Position') + slider('pt', 'Время падения', 'Time of the fall', 0, 20, 0.5, 20),
  stats([('pV', 'Предельная скорость', 'Terminal speed'), ('pC', 'Скорость в выбранный момент', 'Speed at the chosen moment')]),
  'ptFb', 'Схема условная: сила сопротивления F = ½·ρ·CdA·v²; плотность воздуха 1,2 кг/м³ (на высоте меньше); эффективные площади выбраны для модели.',
  'A schematic drawing: drag force F = ½·ρ·CdA·v²; air density 1.2 kg/m³ (lower at altitude); the effective areas are chosen for the model.')
s3 = section('drag', 'Сопротивление воздуха и предельная скорость', 'Air resistance and terminal speed',
 bd('<p>Падающее тело разгоняется силой тяжести, но воздух сопротивляется, причём сила сопротивления растёт со скоростью (примерно как квадрат скорости). Когда она сравнивается с силой тяжести, равнодействующая становится нулевой, ускорение пропадает и тело падает с <strong>постоянной (предельной) скоростью</strong>. Это просто первый закон Ньютона в действии.</p>',
    '<p>A falling body is accelerated by gravity but air resists, and the drag grows with speed (roughly as the square of speed). When it equals gravity the net force becomes zero, the acceleration vanishes and the body falls at a <strong>constant (terminal) speed</strong>. This is simply Newton’s first law in action.</p>')
 + formula('mg = ½ · ρ · CdA · v²   →   v = √(2mg / (ρ · CdA))', 'чем больше «эффективная площадь» CdA, тем меньше предельная скорость', 'the larger the “effective area” CdA the smaller the terminal speed')
 + bd('<p>Парашют увеличивает эффективную площадь в десятки раз, и предельная скорость падает с десятков метров в секунду до безопасных нескольких.</p>',
      '<p>A parachute increases the effective area by tens of times and the terminal speed falls from tens of metres per second to a safe few.</p>'),
 lab3)

tasks = [
 task(1, 'Разгон автомобиля', 'Accelerating a car', 'Автомобиль массой 1200 кг разгоняется под действием равнодействующей силы 3000 Н. Найдите ускорение.', 'A 1,200 kg car accelerates under a net force of 3,000 N. Find the acceleration.',
  'm = 1200 кг, F = 3000 Н', 'm = 1,200 kg, F = 3,000 N', 'a = F / m = 3000 / 1200 = 2,5 м/с².', 'a = F / m = 3000 / 1200 = 2.5 m/s².', '2,5 м/с².', '2.5 m/s².', True),
 task(2, 'Сани на снегу', 'A sledge on snow', 'Сани массой 40 кг тянут с силой 120 Н. Коэффициент трения 0,1. Найдите ускорение (g = 9,8 Н/кг).', 'A 40 kg sledge is pulled with a force of 120 N. The friction coefficient is 0.1. Find the acceleration (g = 9.8 N/kg).',
  'm = 40 кг, F = 120 Н, μ = 0,1', 'm = 40 kg, F = 120 N, μ = 0.1', 'Трение: μ·m·g = 0,1 · 40 · 9,8 = 39,2 Н.<br>Равнодействующая: 120 − 39,2 = 80,8 Н.<br>a = 80,8 / 40 ≈ 2,0 м/с².', 'Friction: μ·m·g = 0.1 · 40 · 9.8 = 39.2 N.<br>Net force: 120 − 39.2 = 80.8 N.<br>a = 80.8 / 40 ≈ 2.0 m/s².', 'около 2,0 м/с².', 'about 2.0 m/s².'),
 task(3, 'Лифт', 'A lift', 'Человек массой 70 кг стоит на весах в лифте. Что покажут весы в килограммах, если лифт разгоняется вверх с ускорением 2 м/с²? А вниз с 2 м/с²?', 'A 70 kg person stands on a scale in a lift. What does the scale show in kilograms if the lift accelerates upward at 2 m/s²? And downward at 2 m/s²?',
  'm = 70 кг, a = ±2 м/с²', 'm = 70 kg, a = ±2 m/s²', 'Вверх: P = m(g + a) = 70 · 11,8 = 826 Н, то есть 826 / 9,8 ≈ 84 кг.<br>Вниз: P = 70 · 7,8 = 546 Н ≈ 56 кг.', 'Up: P = m(g + a) = 70 · 11.8 = 826 N, that is 826 / 9.8 ≈ 84 kg.<br>Down: P = 70 · 7.8 = 546 N ≈ 56 kg.', '≈ 84 кг при разгоне вверх, ≈ 56 кг при разгоне вниз.', '≈ 84 kg accelerating up, ≈ 56 kg accelerating down.'),
 task(4, 'Третий закон: яблоко и Земля', 'The third law: apple and Earth', 'Земля притягивает яблоко с силой 1 Н. С какой силой яблоко притягивает Землю? Какое ускорение получает Земля? m(Земли) = 6·10²⁴ кг.', 'The Earth attracts an apple with a force of 1 N. With what force does the apple attract the Earth? What acceleration does the Earth get? m(Earth) = 6·10²⁴ kg.',
  'F = 1 Н, M = 6·10²⁴ кг', 'F = 1 N, M = 6·10²⁴ kg', 'Третий закон: тоже 1 Н (силы равны и противоположны, но приложены к разным телам).<br>a = F / M = 1 / 6·10²⁴ ≈ 1,7·10⁻²⁵ м/с².', 'The third law: also 1 N (the forces are equal and opposite but act on different bodies).<br>a = F / M = 1 / 6·10²⁴ ≈ 1.7·10⁻²⁵ m/s².', '1 Н; около 2·10⁻²⁵ м/с² — незаметно мало.', '1 N; about 2·10⁻²⁵ m/s² — unnoticeably small.'),
 task(5, 'Предельная скорость', 'Terminal speed', 'Найдите предельную скорость парашютиста массой 80 кг, падающего «лёжа» (CdA = 0,5 м²). ρ = 1,2 кг/м³.', 'Find the terminal speed of an 80 kg parachutist falling spread-eagle (CdA = 0.5 m²). ρ = 1.2 kg/m³.',
  'm = 80 кг, CdA = 0,5 м²', 'm = 80 kg, CdA = 0.5 m²', 'v = √(2mg / (ρ·CdA)) = √(2·80·9,8 / (1,2·0,5)) = √(1568 / 0,6) = √2613 ≈ 51 м/с.', 'v = √(2mg / (ρ·CdA)) = √(2·80·9.8 / (1.2·0.5)) = √(1568 / 0.6) = √2613 ≈ 51 m/s.', 'около 51 м/с (≈ 184 км/ч).', 'about 51 m/s (≈ 184 km/h).'),
 task(6, 'С парашютом', 'With a parachute', 'Та же масса, но парашют раскрыт: CdA = 30 м². Найдите предельную скорость.', 'The same mass but with the parachute open: CdA = 30 m². Find the terminal speed.',
  'CdA = 30 м²', 'CdA = 30 m²', 'v = √(1568 / (1,2 · 30)) = √(1568 / 36) = √43,6 ≈ 6,6 м/с.', 'v = √(1568 / (1.2 · 30)) = √(1568 / 36) = √43.6 ≈ 6.6 m/s.', 'около 6,6 м/с — как прыжок с высоты 2,2 м.', 'about 6.6 m/s — like a jump from a height of 2.2 m.'),
]

quiz = [
 qz('Что говорит первый закон Ньютона?', 'Тело сохраняет скорость, если силы уравновешены или не действуют', 'Тело всегда движется с ускорением', 'Сила пропорциональна скорости', 'Это закон инерции.',
    'What does Newton’s first law say?', 'A body keeps its velocity if forces are balanced or absent', 'A body always accelerates', 'Force is proportional to speed', 'This is the law of inertia.'),
 qz('Формула второго закона Ньютона:', 'F = m·a', 'F = m / a', 'F = m·v²', 'Ускорение определяется равнодействующей силой и массой.',
    'The formula of Newton’s second law:', 'F = m·a', 'F = m / a', 'F = m·v²', 'The acceleration is set by the net force and the mass.'),
 qz('Что такое 1 ньютон?', 'Сила, сообщающая 1 кг ускорение 1 м/с²', 'Вес 1 литра воды', 'Скорость 1 м/с', '1 Н = 1 кг·м/с².',
    'What is 1 newton?', 'The force that gives 1 kg an acceleration of 1 m/s²', 'The weight of 1 litre of water', 'A speed of 1 m/s', '1 N = 1 kg·m/s².'),
 qz('Третий закон Ньютона утверждает, что…', 'Силы действия и противодействия равны и приложены к разным телам', 'Силы действия и противодействия уравновешивают друг друга', 'Сила действия больше', 'Они равны по модулю и противоположны, но не уравновешиваются, ведь действуют на разные тела.',
    'Newton’s third law states that…', 'Action and reaction forces are equal and act on different bodies', 'Action and reaction forces balance each other', 'The action force is greater', 'They are equal in magnitude and opposite but do not balance because they act on different bodies.'),
 qz('Лифт разгоняется вверх. Вес человека…', 'Больше, чем в покое', 'Меньше, чем в покое', 'Такой же', 'P = m(g + a) > mg.',
    'A lift accelerates upward. The person’s weight is…', 'Greater than at rest', 'Less than at rest', 'The same', 'P = m(g + a) > mg.'),
 qz('Чему равен вес в свободном падении?', 'Нулю', 'mg', '2mg', 'При a = −g получаем P = 0 — невесомость.',
    'What is the weight in free fall?', 'Zero', 'mg', '2mg', 'At a = −g we get P = 0 — weightlessness.'),
 qz('Почему парашютист падает с постоянной скоростью?', 'Сопротивление воздуха уравновесило силу тяжести', 'Сила тяжести исчезла', 'Воздух толкает его вверх с растущей силой навсегда', 'Равнодействующая нулевая, значит ускорения нет.',
    'Why does a parachutist fall at a constant speed?', 'Air resistance has balanced gravity', 'Gravity disappeared', 'Air pushes him up with a forever growing force', 'The net force is zero so there is no acceleration.'),
 qz('Как раскрытие парашюта влияет на предельную скорость?', 'Резко уменьшает её', 'Увеличивает', 'Не влияет', 'v ~ 1/√(CdA): площадь выросла — скорость упала.',
    'How does opening a parachute affect the terminal speed?', 'It sharply reduces it', 'It increases it', 'It has no effect', 'v ~ 1/√(CdA): the area grew — the speed fell.'),
]

js = r'''
const T={ru:{
 nsLabel:"Сани, сила тяги и сила трения",lfLabel:"Человек на весах в лифте",ptLabel:"График скорости падающего парашютиста",
 surf:["Снег (μ = 0,1)","Земля (μ = 0,4)","Лёд (μ = 0,03)"],pos:["Лёжа, тело (CdA = 0,5 м²)","С раскрытым парашютом (CdA = 30 м²)"],
 feel:["тяжелее","как обычно","легче","невесомость"],
 nsFb:"Пока тяга меньше трения, сани стоят; потом разгоняются.",lfFb:"Вес зависит от ускорения опоры, а не только от массы.",ptFb:"Скорость растёт, пока сопротивление не уравновесит силу тяжести."},
 en:{
 nsLabel:"A sledge, the pulling force and the friction force",lfLabel:"A person on a scale in a lift",ptLabel:"A speed graph of a falling parachutist",
 surf:["Snow (μ = 0.1)","Ground (μ = 0.4)","Ice (μ = 0.03)"],pos:["Spread-eagle, body (CdA = 0.5 m²)","With the parachute open (CdA = 30 m²)"],
 feel:["heavier","as usual","lighter","weightless"],
 nsFb:"While the pull is less than the friction the sledge stands; then it accelerates.",lfFb:"Weight depends on the acceleration of the support, not only on the mass.",ptFb:"The speed grows until the drag balances gravity."}};
const MUS=[0.1,0.4,0.03],CDA=[0.5,30];
function drawNs(){const t=tt(),m=+$("nm").value,F=+$("nf").value,mu=MUS[+$("nu").value],tm=+$("nt").value;
 const Fr=mu*m*9.8,net=Math.max(0,F-Fr),a=net/m,v=a*tm,s=a*tm*tm/2;
 const x=60+Math.min(380,s*6);
 let g='<line x1="30" y1="200" x2="570" y2="200" stroke="#18181a" stroke-width="2"/><rect x="'+x+'" y="150" width="100" height="45" fill="#b87333" stroke="#18181a"/>'+svgText(x+50,178,m+UN[lang].kg,"#fff","middle",12);
 g+=arrow(x+100,170,x+100+Math.min(150,F*0.4),170,"#2f6f5d",3)+svgText(x+105+Math.min(150,F*0.4),165,"F","#2f6f5d","start",13)+arrow(x,190,x-Math.min(150,Fr*0.4),190,"#b6533f",3)+svgText(x-Math.min(150,Fr*0.4)-4,186,"Fтр","#b6533f","end",12);
 $("nsSvg").innerHTML=g;
 $("nmOut").textContent=m+UN[lang].kg;$("nfOut").textContent=F+UN[lang].N;$("ntOut").textContent=fmt(tm,1)+UN[lang].s;
 $("nR").textContent=fmt(Fr,0)+UN[lang].N;$("nA").textContent=fmt(a,2)+(lang==="ru"?" м/с²":" m/s²");$("nV").textContent=fmt(v,1)+UN[lang].ms+", "+fmt(s,1)+UN[lang].m;$("nsFb").textContent=t.nsFb}
["nm","nf","nu","nt"].forEach(id=>$(id).addEventListener("input",drawNs));
function drawLf(){const t=tt(),m=+$("lm").value,a=+$("la").value,P=m*(9.8+a);
 let g='<rect x="200" y="30" width="200" height="190" fill="#f1efe8" stroke="#18181a" stroke-width="3"/><rect x="250" y="200" width="100" height="14" fill="#9a9a9a" stroke="#18181a"/><circle cx="300" cy="95" r="16" fill="#b87333"/><line x1="300" y1="111" x2="300" y2="180" stroke="#18181a" stroke-width="5"/><line x1="300" y1="180" x2="285" y2="200" stroke="#18181a" stroke-width="4"/><line x1="300" y1="180" x2="315" y2="200" stroke="#18181a" stroke-width="4"/>';
 g+=arrow(450,125,450,125-Math.max(-80,Math.min(80,a*12)),"#2f6f5d",3)+svgText(462,128,"a","#2f6f5d","start",13)+svgText(300,242,fmt(P/9.8,1)+" kg","#18181a","middle",14);
 $("lfSvg").innerHTML=g;
 $("lmOut").textContent=m+UN[lang].kg;$("laOut").textContent=fmt(a,1)+(lang==="ru"?" м/с²":" m/s²");
 const k=P<1?3:(a>0.2?0:(a<-0.2?2:1));$("lP").textContent=fmt(P,0)+UN[lang].N;$("lK").textContent=fmt(P/9.8,1)+UN[lang].kg;$("lS").textContent=t.feel[k];$("lfFb").textContent=t.lfFb}
["lm","la"].forEach(id=>$(id).addEventListener("input",drawLf));
function drawPt(){const t=tt(),m=+$("pm").value,cda=CDA[+$("pk").value],tm=+$("pt").value,vt=Math.sqrt(2*m*9.8/(1.2*cda));
 const X=s=>50+s/20*500,Y=v=>220-v/Math.max(60,vt*1.1)*190;let v=0,pts=[X(0)+","+Y(0)],vc=0;const dt=0.02;
 for(let s=0;s<20;s+=dt){const a=9.8-0.5*1.2*cda*v*v/m;v+=a*dt;if(Math.abs(s+dt-tm)<dt/2)vc=v;if(Math.round((s+dt)/dt)%25===0)pts.push(X(s+dt)+","+Y(v))}
 if(tm===0)vc=0;
 let g='<line x1="50" y1="220" x2="550" y2="220" stroke="#18181a"/><line x1="50" y1="20" x2="50" y2="220" stroke="#18181a"/><line x1="50" y1="'+Y(vt)+'" x2="550" y2="'+Y(vt)+'" stroke="#b6533f" stroke-dasharray="5 4"/>'+svgText(545,Y(vt)-5,fmt(vt,0)+UN[lang].ms,"#b6533f","end",11);
 g+='<polyline fill="none" stroke="#3f5f8f" stroke-width="3" points="'+pts.join(" ")+'"/>'+svgText(550,236,"t, "+(lang==="ru"?"с":"s"),"#66666b","end",10)+svgText(56,14,"v","#18181a","start",11);
 $("ptSvg").innerHTML=g;
 $("pmOut").textContent=m+UN[lang].kg;$("ptOut").textContent=fmt(tm,1)+UN[lang].s;
 $("pV").textContent=fmt(vt,1)+UN[lang].ms;$("pC").textContent=fmt(vc,1)+UN[lang].ms;$("ptFb").textContent=t.ptFb}
["pm","pk","pt"].forEach(id=>$(id).addEventListener("input",drawPt));
const LAB={ru:{nsSvg:T.ru.nsLabel,lfSvg:T.ru.lfLabel,ptSvg:T.ru.ptLabel},en:{nsSvg:T.en.nsLabel,lfSvg:T.en.lfLabel,ptSvg:T.en.ptLabel}};
function drawAll(){fillSel("nu",T[lang].surf,0);fillSel("pk",T[lang].pos,0);drawNs();drawLf();drawPt()}
'''

c = dict(n='33', slug='33-newtons-laws.html', block='VI', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Законы Ньютона', 'Newton’s laws'),
 desc='Глава 33 Атласа физики: три закона Ньютона, второй закон и трение, вес в лифте и невесомость, падение с сопротивлением воздуха.',
 lead=('Почему в лифте мы «тяжелеем», а парашютист падает с постоянной скоростью. Три закона Ньютона в действии.',
       'Why we “get heavier” in a lift and a parachutist falls at a constant speed. Newton’s three laws in action.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('second', 'Второй закон', 'Second law'), ('lift', 'Вес и невесомость', 'Weight'), ('drag', 'Сопротивление воздуха', 'Air resistance'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Вы встали на весы в лифте многоэтажного дома. Пока лифт стоял, весы показывали 60 кг. В момент, когда он тронулся вверх, стрелка на секунду прыгнула к 66 кг, потом вернулась к 60, а при остановке на мгновение показала 54.</p><p>Масса ведь не изменилась. Что же показывали весы?</p>',
         '<p>You stood on a scale in the lift of a tall building. While the lift stood the scale showed 60 kg. The moment it started upward the needle jumped for a second to 66 kg then returned to 60 and at the stop showed 54 for a moment.</p><p>Your mass did not change. So what was the scale showing?</p>'),
 hint=stdhint('Вес в лифте', 'Weight in a lift'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: весы показывают силу давления', 'The answer: the scale shows the force of pressure'),
 answer=('<p>Весы измеряют не массу, а силу, с которой вы на них давите, то есть вес. При старте вверх лифт движется с ускорением <em>a</em>, и по второму закону Ньютона опора должна давить на вас с силой <em>m(g + a)</em> — больше, чем <em>mg</em>. Весы показывают «66 кг» (ускорение около 1 м/с²). При торможении вверх ускорение направлено вниз, и вес уменьшается, «54 кг». При равномерном движении ускорения нет, и вес равен обычному (модель 2).</p>',
         '<p>The scale measures not mass but the force with which you press on it, that is the weight. At a start upward the lift moves with an acceleration <em>a</em> and by Newton’s second law the support must press on you with a force <em>m(g + a)</em> — greater than <em>mg</em>. The scale shows “66 kg” (an acceleration of about 1 m/s²). When braking on the way up the acceleration points down and the weight decreases, “54 kg”. At steady motion there is no acceleration and the weight is the usual one (model 2).</p>'),
 sources=[
  ('Законы Ньютона, вес, трение —', 'Newton’s laws, weight, friction —', LINK('https://openstax.org/books/university-physics-volume-1/pages/5-introduction', 'OpenStax University Physics, Vol. 1, гл. 5') + ', ' + LINK('https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion', 'Wikipedia: Newton’s laws of motion')),
  ('Предельная скорость и сопротивление воздуха —', 'Terminal velocity and air resistance —', LINK('https://en.wikipedia.org/wiki/Terminal_velocity', 'Wikipedia: Terminal velocity'))],
 note=stdnote('Коэффициенты трения, значения CdA и плотность воздуха 1,2 кг/м³ — условные.', 'The friction coefficients, the CdA values and the air density of 1.2 kg/m³ are assumed.'),
 prev=('32-eye-and-instruments.html', 'Глава 32 · Глаз и оптические приборы', 'Chapter 32 · The eye and optical instruments'),
 next=('34-momentum.html', 'Глава 34 · Импульс', 'Chapter 34 · Momentum'),
 js=js)
build(c)
