# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'БЕГУЩАЯ ВОЛНА', 'A TRAVELLING WAVE', 'wvSvg', '0 0 600 250',
  slider('wl', 'Длина волны', 'Wavelength', 0.5, 4, 0.1, 2) + slider('wf', 'Частота', 'Frequency', 0.5, 10, 0.5, 2) + slider('wt', 'Момент времени', 'Moment in time', 0, 2, 0.02, 0),
  stats([('wV', 'Скорость v = λ·f', 'Speed v = λ·f'), ('wT', 'Период T = 1/f', 'Period T = 1/f'), ('wP', 'Гребней на отрезке 6 м', 'Crests on a 6 m stretch')]),
  'wvFb', 'Схема условная: волна на верёвке, отрезок 6 м; красная точка — один и тот же участок среды, он лишь качается вверх и вниз.',
  'A schematic drawing: a wave on a rope, a 6 m stretch; the red dot is one fixed piece of the medium — it only moves up and down.')
s1 = section('wave', 'Что такое волна', 'What a wave is',
 bd('<p><strong>Механическая волна</strong> — это распространение колебаний в среде (в верёвке, воде, воздухе, земле). Главное: <strong>волна переносит энергию, но не переносит вещество</strong>. Каждый участок среды лишь качается около своего места, а передаётся состояние колебания от соседа к соседу.</p><p>Волну описывают тремя величинами. <strong>Длина волны</strong> <em>λ</em> — расстояние между соседними гребнями. <strong>Частота</strong> <em>f</em> — сколько гребней проходит мимо точки за секунду. <strong>Скорость</strong> <em>v</em> — как быстро гребень перемещается:</p>',
    '<p>A <strong>mechanical wave</strong> is the spread of oscillations in a medium (a rope, water, air, the ground). The main point: <strong>a wave carries energy but not matter</strong>. Each piece of the medium only swings about its own place and the state of oscillation is passed from neighbour to neighbour.</p><p>A wave is described by three quantities. The <strong>wavelength</strong> <em>λ</em> is the distance between neighbouring crests. The <strong>frequency</strong> <em>f</em> is how many crests pass a point per second. The <strong>speed</strong> <em>v</em> is how fast a crest moves:</p>')
 + formula('v = λ · f', 'при смене среды скорость меняется; частоту задаёт источник и она остаётся прежней', 'when the medium changes the speed changes; the frequency is set by the source and stays the same'),
 lab1)

lab2 = model(2, 'ПОПЕРЕЧНАЯ И ПРОДОЛЬНАЯ', 'TRANSVERSE AND LONGITUDINAL', 'tlSvg', '0 0 600 250',
  select('tk', 'Вид волны', 'Type of wave') + slider('tt', 'Момент времени', 'Moment in time', 0, 2, 0.02, 0),
  stats([('tD', 'Колебания частиц', 'Motion of the particles'), ('tM', 'Где в природе', 'Where in nature')]),
  'tlFb', 'Схема условная: ряд частиц среды; смещения увеличены для наглядности.',
  'A schematic drawing: a row of particles of the medium; the displacements are exaggerated for clarity.')
s2 = section('types', 'Поперечные и продольные волны', 'Transverse and longitudinal waves',
 bd('<p>Если частицы среды колеблются <em>поперёк</em> направления распространения волны, она <strong>поперечная</strong> (волна на верёвке, на струне комуза, S-волна землетрясения). Если <em>вдоль</em> — <strong>продольная</strong>: области сжатия и разрежения бегут по среде (звук в воздухе, P-волна землетрясения, волна в пружине).</p><p>Поперечные волны возможны только в твёрдых телах и на поверхности жидкостей — в жидкости и газе нет силы упругости при сдвиге. А продольные идут в любой среде.</p>',
    '<p>If the particles of the medium oscillate <em>across</em> the direction in which the wave travels it is <strong>transverse</strong> (a wave on a rope, on a komuz string, the S-wave of an earthquake). If <em>along</em> it — <strong>longitudinal</strong>: regions of compression and rarefaction run through the medium (sound in air, the P-wave of an earthquake, a wave in a spring).</p><p>Transverse waves are possible only in solids and on the surface of liquids — a liquid or a gas has no elastic force against shear. Longitudinal waves travel in any medium.</p>'),
 lab2)

lab3 = model(3, 'НАЛОЖЕНИЕ ВОЛН', 'SUPERPOSITION OF WAVES', 'ifSvg', '0 0 600 250',
  slider('ia', 'Амплитуда каждой волны', 'Amplitude of each wave', 1, 5, 0.5, 3) + slider('ip', 'Сдвиг фаз между волнами', 'Phase shift between the waves', 0, 360, 15, 0),
  stats([('iS', 'Амплитуда суммы', 'Amplitude of the sum'), ('iK', 'Результат', 'Result')]),
  'ifFb', 'Схема условная: две волны одной частоты; тонкие линии — каждая волна, толстая — их сумма.',
  'A schematic drawing: two waves of the same frequency; thin lines are the individual waves, the thick one is their sum.')
s3 = section('sup', 'Наложение и интерференция', 'Superposition and interference',
 bd('<p>Когда две волны встречаются, смещения просто складываются — это <strong>принцип суперпозиции</strong>. Если гребни совпадают (сдвиг фаз 0°), волны усиливают друг друга; если гребень одной попадает на впадину другой (180°), они гасят друг друга. Сложение волн называют <strong>интерференцией</strong>. Для одинаковых амплитуд <em>A</em> и сдвига фаз <em>Δφ</em> амплитуда суммы равна <em>2A·|cos(Δφ/2)|</em>.</p><p>Бегущая и отражённая волны, складываясь, образуют <strong>стоячую волну</strong>: в ней есть неподвижные узлы и места наибольших колебаний. Именно так «поёт» струна комуза и труба чооро.</p>',
    '<p>When two waves meet the displacements simply add — this is the <strong>principle of superposition</strong>. If the crests coincide (phase shift 0°) the waves strengthen each other; if the crest of one meets the trough of the other (180°) they cancel. The adding of waves is called <strong>interference</strong>. For equal amplitudes <em>A</em> and phase shift <em>Δφ</em> the amplitude of the sum is <em>2A·|cos(Δφ/2)|</em>.</p><p>A travelling wave and its reflection add to form a <strong>standing wave</strong>: it has motionless nodes and places of greatest oscillation. That is how a komuz string and a choor pipe “sing”.</p>'),
 lab3)

tasks = [
 task(1, 'Скорость волны', 'Speed of a wave', 'Длина волны 2 м, частота 3 Гц. Найдите скорость.', 'The wavelength is 2 m and the frequency 3 Hz. Find the speed.',
  'λ = 2 м, f = 3 Гц', 'λ = 2 m, f = 3 Hz', 'v = λ·f = 2 · 3 = 6 м/с.', 'v = λ·f = 2 · 3 = 6 m/s.', '6 м/с.', '6 m/s.', True),
 task(2, 'Длина волны на воде', 'Wavelength on water', 'Волна на воде бежит со скоростью 3 м/с, период 2 с. Найдите длину волны.', 'A water wave travels at 3 m/s with a period of 2 s. Find the wavelength.',
  'v = 3 м/с, T = 2 с', 'v = 3 m/s, T = 2 s', 'f = 1/T = 0,5 Гц.<br>λ = v/f = 3 / 0,5 = 6 м.', 'f = 1/T = 0.5 Hz.<br>λ = v/f = 3 / 0.5 = 6 m.', '6 м.', '6 m.'),
 task(3, 'Волна на верёвке', 'A wave on a rope', 'Конец верёвки колеблют с частотой 5 Гц, длина волны 0,4 м. Найдите скорость волны.', 'The end of a rope is shaken at 5 Hz and the wavelength is 0.4 m. Find the wave speed.',
  'f = 5 Гц, λ = 0,4 м', 'f = 5 Hz, λ = 0.4 m', 'v = λ·f = 0,4 · 5 = 2 м/с.', 'v = λ·f = 0.4 · 5 = 2 m/s.', '2 м/с.', '2 m/s.'),
 task(4, 'Поплавок на воде', 'A float on the water', 'Волна идёт со скоростью 2 м/с, период 4 с. Сколько гребней пройдёт мимо поплавка за минуту и на какое расстояние уйдёт волна? Куда унесёт поплавок?', 'A wave travels at 2 m/s with a period of 4 s. How many crests pass a float in a minute and how far does the wave go? Where is the float carried?',
  'v = 2 м/с, T = 4 с, t = 60 с', 'v = 2 m/s, T = 4 s, t = 60 s', 'Гребней: 60 / 4 = 15.<br>Путь волны: 2 · 60 = 120 м.<br>Поплавок лишь качается на месте: волна переносит энергию, а не воду.', 'Crests: 60 / 4 = 15.<br>The wave’s path: 2 · 60 = 120 m.<br>The float only bobs in place: the wave carries energy, not water.',
  '15 гребней; 120 м; поплавок остаётся на месте.', '15 crests; 120 m; the float stays in place.'),
 task(5, 'Сложение волн', 'Adding waves', 'Две волны с амплитудой 3 см каждая складываются. Какова амплитуда суммы при сдвиге фаз 0° и 180°?', 'Two waves of amplitude 3 cm add. What is the amplitude of the sum for phase shifts of 0° and 180°?',
  'A = 3 см', 'A = 3 cm', 'Δφ = 0°: 2A·|cos 0°| = 6 см.<br>Δφ = 180°: 2A·|cos 90°| = 0.', 'Δφ = 0°: 2A·|cos 0°| = 6 cm.<br>Δφ = 180°: 2A·|cos 90°| = 0.', '6 см (усиление) и 0 (гашение).', '6 cm (strengthening) and 0 (cancelling).'),
 task(6, 'Какая волна', 'Which kind of wave', 'Груз на длинной пружине толкнули вдоль её оси — по пружине побежало сжатие. Поперечная это волна или продольная? А если качнуть конец пружины в сторону?', 'A weight on a long spring is pushed along its axis and a compression runs along the spring. Is this wave transverse or longitudinal? And if the end is swung sideways?',
  '—', '—', 'Сжатие вдоль оси: частицы колеблются вдоль направления распространения — продольная.<br>Качнули в сторону: частицы колеблются поперёк — поперечная.', 'Compression along the axis: the particles oscillate along the direction of travel — longitudinal.<br>Swung sideways: the particles oscillate across — transverse.',
  'сначала продольная, потом поперечная.', 'first longitudinal, then transverse.'),
]

quiz = [
 qz('Что переносит волна?', 'Энергию, но не вещество', 'Вещество, но не энергию', 'И то и другое', 'Частицы среды лишь колеблются на месте.',
    'What does a wave carry?', 'Energy but not matter', 'Matter but not energy', 'Both', 'The particles of the medium only oscillate in place.'),
 qz('Формула связи скорости, длины волны и частоты:', 'v = λ·f', 'v = λ / f', 'v = f / λ²', 'Скорость — это длина волны, умноженная на частоту.',
    'The relation of speed, wavelength and frequency:', 'v = λ·f', 'v = λ / f', 'v = f / λ²', 'Speed is the wavelength times the frequency.'),
 qz('Что такое длина волны?', 'Расстояние между соседними гребнями', 'Высота гребня', 'Время одного колебания', 'Длина волны — пространственный период.',
    'What is the wavelength?', 'The distance between neighbouring crests', 'The height of a crest', 'The time of one oscillation', 'The wavelength is the spatial period.'),
 qz('Как колеблются частицы в поперечной волне?', 'Поперёк направления распространения', 'Вдоль направления распространения', 'Не колеблются', 'Так определяется поперечная волна.',
    'How do particles move in a transverse wave?', 'Across the direction of travel', 'Along the direction of travel', 'They do not oscillate', 'That is the definition of a transverse wave.'),
 qz('Какой волной является звук в воздухе?', 'Продольной', 'Поперечной', 'Электромагнитной', 'В воздухе нет упругости сдвига, поэтому звук — продольная волна сжатий и разрежений.',
    'What kind of wave is sound in air?', 'Longitudinal', 'Transverse', 'Electromagnetic', 'Air has no shear elasticity, so sound is a longitudinal wave of compressions and rarefactions.'),
 qz('Что получится, если сложить две волны со сдвигом фаз 180° и равными амплитудами?', 'Они погасят друг друга', 'Амплитуда удвоится', 'Амплитуда не изменится', 'Гребень одной приходится на впадину другой.',
    'What results from adding two equal-amplitude waves with a 180° phase shift?', 'They cancel each other', 'The amplitude doubles', 'The amplitude does not change', 'The crest of one meets the trough of the other.'),
 qz('Что остаётся неизменным при переходе волны из одной среды в другую?', 'Частота', 'Длина волны', 'Скорость', 'Частоту задаёт источник; скорость и длина волны меняются.',
    'What stays the same when a wave passes from one medium to another?', 'The frequency', 'The wavelength', 'The speed', 'The frequency is set by the source; the speed and wavelength change.'),
 qz('Волна на воде имеет период 4 с и скорость 2 м/с. Какова длина волны?', '8 м', '2 м', '0,5 м', 'λ = v·T = 2 · 4 = 8 м.',
    'A water wave has a period of 4 s and a speed of 2 m/s. What is the wavelength?', '8 m', '2 m', '0.5 m', 'λ = v·T = 2 · 4 = 8 m.'),
]

js = r'''
const T={ru:{
 wvLabel:"Бегущая волна на верёвке в выбранный момент",tlLabel:"Ряд частиц среды при прохождении волны",ifLabel:"Две волны и их сумма",
 kinds:["Поперечная","Продольная"],mot:["поперёк движения волны","вдоль движения волны"],nat:["верёвка, струна, S-волна землетрясения","звук, P-волна землетрясения"],
 res:["усиление","частичное гашение","гашение"],
 wvFb:"Красная точка качается на месте, а гребни бегут вправо.",tlFb:"Частицы колеблются около своих мест, а волна бежит вправо.",ifFb:"При сдвиге 180° волны гасят друг друга."},
 en:{
 wvLabel:"A travelling wave on a rope at the chosen moment",tlLabel:"A row of particles of the medium as a wave passes",ifLabel:"Two waves and their sum",
 kinds:["Transverse","Longitudinal"],mot:["across the wave’s motion","along the wave’s motion"],nat:["a rope, a string, the S-wave of an earthquake","sound, the P-wave of an earthquake"],
 res:["strengthening","partial cancelling","cancelling"],
 wvFb:"The red dot bobs in place while the crests run to the right.",tlFb:"The particles oscillate about their places while the wave runs to the right.",ifFb:"At a 180° shift the waves cancel each other."}};
function drawWv(){const t=tt(),lam=+$("wl").value,f=+$("wf").value,tm=+$("wt").value,v=lam*f;
 const X=x=>40+x/6*520,Y=(x)=>125-70*Math.sin(2*Math.PI*(x/lam-f*tm));
 const pts=[];for(let i=0;i<=300;i++){const x=i/300*6;pts.push(X(x)+","+Y(x))}
 let g='<line x1="40" y1="125" x2="560" y2="125" stroke="#c9c2b0"/><polyline fill="none" stroke="#3f5f8f" stroke-width="3" points="'+pts.join(" ")+'"/>';
 const px=2;g+='<circle cx="'+X(px)+'" cy="'+Y(px)+'" r="7" fill="#b6533f"/><line x1="'+X(px)+'" y1="125" x2="'+X(px)+'" y2="'+Y(px)+'" stroke="#b6533f" stroke-dasharray="3 3"/>';
 g+=arrow(60,230,150,230,"#18181a",2)+svgText(160,234,"v","#18181a","start",12)+svgText(560,20,"λ = "+fmt(lam,1)+UN[lang].m,"#66666b","end",12);
 $("wvSvg").innerHTML=g;
 $("wlOut").textContent=fmt(lam,1)+UN[lang].m;$("wfOut").textContent=fmt(f,1)+(lang==="ru"?" Гц":" Hz");$("wtOut").textContent=fmt(tm,2)+UN[lang].s;
 $("wV").textContent=fmt(v,1)+UN[lang].ms;$("wT").textContent=fmt(1/f,2)+UN[lang].s;$("wP").textContent=fmt(6/lam,1);$("wvFb").textContent=t.wvFb}
["wl","wf","wt"].forEach(id=>$(id).addEventListener("input",drawWv));
function drawTl(){const t=tt(),k=+$("tk").value,tm=+$("tt").value,lam=150,w=2*Math.PI;let g='';
 for(let row=0;row<3;row++){for(let i=0;i<36;i++){const x0=40+i*14.4,ph=2*Math.PI*(x0/lam)-w*tm;
  let x=x0,y=70+row*55;if(k===0)y+=22*Math.sin(-ph);else x+=7*Math.sin(-ph);
  g+='<circle cx="'+x+'" cy="'+y+'" r="'+(row===1&&i===12?6:4)+'" fill="'+(row===1&&i===12?"#b6533f":"#3f5f8f")+'"/>'}}
 g+=arrow(60,230,150,230,"#18181a",2)+svgText(160,234,"→","#18181a","start",12);
 $("tlSvg").innerHTML=g;
 $("ttOut").textContent=fmt(tm,2)+UN[lang].s;$("tD").textContent=t.mot[k];$("tM").textContent=t.nat[k];$("tlFb").textContent=t.tlFb}
["tk","tt"].forEach(id=>$(id).addEventListener("input",drawTl));
function drawIf(){const t=tt(),A=+$("ia").value,ph=+$("ip").value*Math.PI/180,S=2*A*Math.abs(Math.cos(ph/2));
 const X=x=>30+x*540,Y=v=>125-v*18;let p1=[],p2=[],p3=[];
 for(let i=0;i<=240;i++){const x=i/240,a=2*Math.PI*2*x;p1.push(X(x)+","+Y(A*Math.sin(a)));p2.push(X(x)+","+Y(A*Math.sin(a+ph)));p3.push(X(x)+","+Y(A*Math.sin(a)+A*Math.sin(a+ph)))}
 let g='<line x1="30" y1="125" x2="570" y2="125" stroke="#c9c2b0"/><polyline fill="none" stroke="#3f5f8f" stroke-width="1.5" points="'+p1.join(" ")+'"/><polyline fill="none" stroke="#2f6f5d" stroke-width="1.5" points="'+p2.join(" ")+'"/><polyline fill="none" stroke="#b6533f" stroke-width="3.5" points="'+p3.join(" ")+'"/>';
 $("ifSvg").innerHTML=g;
 $("iaOut").textContent=fmt(A,1)+(lang==="ru"?" см":" cm");$("ipOut").textContent=Math.round(ph*180/Math.PI)+"°";
 $("iS").textContent=fmt(S,1)+(lang==="ru"?" см":" cm");const r=S>1.9*A?0:(S<0.1*A?2:1);$("iK").textContent=t.res[r];$("ifFb").textContent=t.ifFb}
["ia","ip"].forEach(id=>$(id).addEventListener("input",drawIf));
const LAB={ru:{wvSvg:T.ru.wvLabel,tlSvg:T.ru.tlLabel,ifSvg:T.ru.ifLabel},en:{wvSvg:T.en.wvLabel,tlSvg:T.en.tlLabel,ifSvg:T.en.ifLabel}};
function drawAll(){fillSel("tk",T[lang].kinds,0);drawWv();drawTl();drawIf()}
'''

c = dict(n='26', slug='26-mechanical-waves.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Механические волны', 'Mechanical waves'),
 desc='Глава 26 Атласа физики: распространение колебаний, длина волны и скорость, поперечные и продольные волны, интерференция, стоячая волна.',
 lead=('Волны на Иссык-Куле, на верёвке и в земле. Длина волны, скорость, виды волн и интерференция.',
       'Waves on Issyk-Kul, on a rope and in the ground. Wavelength, speed, kinds of waves and interference.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('wave', 'Что такое волна', 'What a wave is'), ('types', 'Виды волн', 'Kinds of waves'), ('sup', 'Интерференция', 'Interference'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На озере Иссык-Куль в ветреный день к берегу катятся волны. Чайка спит на воде и качается вверх-вниз, а волны идут мимо неё к берегу. Через час чайка по-прежнему почти на том же месте, хотя волны давно дошли до пляжа.</p><p>Что же тогда «бежит» к берегу, если сама вода и чайка остаются на месте?</p>',
         '<p>On Lake Issyk-Kul on a windy day waves roll toward the shore. A gull sleeps on the water and bobs up and down while the waves pass it on their way to the beach. An hour later the gull is still nearly in the same place although waves have long reached the shore.</p><p>So what “runs” to the shore if the water and the gull stay in place?</p>'),
 hint=stdhint('Бегущая волна', 'A travelling wave'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: бежит колебание', 'The answer: the oscillation runs'),
 answer=('<p>К берегу бежит не вода, а <strong>колебание</strong> — форма волны и её энергия. Каждая частица воды описывает небольшой круг или качается вверх-вниз, передавая движение соседней. Чайка делает то же и остаётся на месте (модель 1: красная точка). У берега энергия волны отдаётся песку и камням — поэтому волны размывают пляж.</p><p>Скорость волны задаётся формулой v = λ·f: длинные волны бегут быстрее.</p>',
         '<p>What runs to the shore is not the water but the <strong>oscillation</strong> — the shape of the wave and its energy. Each particle of water traces a small circle or bobs up and down, passing the motion to its neighbour. The gull does the same and stays in place (model 1: the red dot). At the shore the energy of the wave is given to sand and stones — that is why waves wear away a beach.</p><p>The speed of a wave is set by v = λ·f: long waves travel faster.</p>'),
 sources=[
  ('Механические волны, v = λf, поперечные и продольные волны, суперпозиция —', 'Mechanical waves, v = λf, transverse and longitudinal waves, superposition —', LINK('https://openstax.org/books/university-physics-volume-1/pages/16-introduction', 'OpenStax University Physics, Vol. 1, гл. 16') + ', ' + LINK('https://en.wikipedia.org/wiki/Wave', 'Wikipedia: Wave')),
  ('Стоячие волны и интерференция —', 'Standing waves and interference —', LINK('https://en.wikipedia.org/wiki/Standing_wave', 'Wikipedia: Standing wave'))],
 note=stdnote('Значения ползунков — условные.', 'The slider values are assumed.'),
 prev=('25-oscillations.html', 'Глава 25 · Колебания', 'Chapter 25 · Oscillations'),
 next=('27-sound.html', 'Глава 27 · Звук', 'Chapter 27 · Sound'),
 js=js)
build(c)
