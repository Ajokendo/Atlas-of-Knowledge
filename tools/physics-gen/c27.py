# -*- coding: utf-8 -*-
from h5 import *

lab1 = model(1, 'ЭХО В УЩЕЛЬЕ', 'AN ECHO IN A GORGE', 'ecSvg', '0 0 600 250',
  slider('et', 'Температура воздуха', 'Air temperature', -20, 40, 1, 20) + slider('ed', 'Расстояние до скалы', 'Distance to the cliff', 5, 500, 5, 100),
  stats([('eV', 'Скорость звука v ≈ 331 + 0,6·t', 'Speed of sound v ≈ 331 + 0.6·t'), ('eT', 'Эхо вернётся через', 'The echo returns after'), ('eK', 'Эхо слышно отдельно?', 'Is the echo heard separately?')]),
  'ecFb', 'Схема условная. Формула скорости звука в воздухе — приближённая. Раздельное эхо слышно, если пауза не короче примерно 0,1 с.',
  'A schematic drawing. The formula for the speed of sound in air is approximate. A separate echo is heard if the pause is not shorter than about 0.1 s.')
s1 = section('speed', 'Звук и его скорость', 'Sound and its speed',
 bd('<p><strong>Звук</strong> — продольная механическая волна в упругой среде: области сжатия и разрежения бегут по воздуху от источника (струны, голосовых связок, мембраны). В пустоте звука нет — нужна среда. Скорость звука зависит от среды и температуры: в воздухе при 20 °C около 343 м/с, в воде около 1500 м/с, в стали около 5000 м/с. Для воздуха удобна приближённая формула:</p>',
    '<p><strong>Sound</strong> is a longitudinal mechanical wave in an elastic medium: regions of compression and rarefaction run through the air from the source (a string, vocal cords, a membrane). There is no sound in a vacuum — a medium is needed. The speed of sound depends on the medium and the temperature: in air at 20 °C about 343 m/s, in water about 1,500 m/s, in steel about 5,000 m/s. For air an approximate formula is handy:</p>')
 + formula('v ≈ 331 + 0,6 · t   (м/с, t в °C)', 'чем теплее воздух, тем быстрее звук', 'the warmer the air, the faster the sound')
 + bd('<p>Звук отражается от преград — так возникает <strong>эхо</strong>. Звук проходит до преграды и обратно, то есть путь равен <em>2d</em>, и эхо возвращается через <em>t = 2d / v</em>. Так работают и эхолоты, которыми измеряют глубину озера, и ультразвуковое исследование в медицине.</p>',
      '<p>Sound is reflected by obstacles — that gives an <strong>echo</strong>. Sound goes to the obstacle and back so the path is <em>2d</em> and the echo returns after <em>t = 2d / v</em>. That is how echo sounders measure the depth of a lake and how medical ultrasound works.</p>'),
 lab1)

lab2 = model(2, 'СТРУНА КОМУЗА', 'A KOMUZ STRING', 'kzSvg', '0 0 600 250',
  slider('kl', 'Длина колеблющейся части струны', 'Length of the vibrating part of the string', 0.3, 0.7, 0.01, 0.55) + slider('kt', 'Сила натяжения', 'Tension', 10, 80, 1, 40) + slider('km', 'Масса одного метра струны', 'Mass of one metre of string', 0.3, 1.5, 0.05, 0.6) + slider('kf', 'Прижата ли струна (доля длины)', 'How far the string is fretted (fraction of length)', 0.5, 1, 0.05, 1),
  stats([('kF', 'Основная частота', 'Fundamental frequency'), ('kN', 'Ближайшая нота', 'Nearest note'), ('kH', 'Первые обертоны', 'The first overtones')]),
  'kzFb', 'Схема условная: параметры струны выбраны для модели (струна из жилы или лески); масса метра — в граммах.',
  'A schematic drawing: the string parameters are chosen for the model (a gut or fishing-line string); the mass of a metre is in grams.')
s2 = section('string', 'Высота звука и струна комуза', 'Pitch and the komuz string',
 bd('<p><strong>Высота звука</strong> определяется частотой: чем она больше, тем звук выше. Человек слышит примерно от 20 Гц до 20 000 Гц; выше — ультразвук, ниже — инфразвук.</p><p>Струна комуза закреплена на концах, поэтому на ней возникает стоячая волна (глава 26). Основная частота струны длиной <em>L</em> с силой натяжения <em>F</em> и массой метра <em>μ</em>:</p>',
    '<p>The <strong>pitch</strong> of a sound is set by its frequency: the greater the frequency, the higher the sound. A person hears from about 20 Hz to 20,000 Hz; above is ultrasound, below infrasound.</p><p>A komuz string is fixed at its ends so a standing wave arises on it (chapter 26). The fundamental frequency of a string of length <em>L</em> with tension <em>F</em> and mass per metre <em>μ</em> is:</p>')
 + formula('f = (1 / 2L) · √(F / μ)', 'короче струна, туже натяжение, легче струна — выше звук', 'a shorter string, a tighter tension, a lighter string — a higher sound')
 + bd('<p>У комуза нет ладов: исполнитель сам прижимает струну пальцем, меняя длину колеблющейся части. Если прижать струну посередине (<em>L/2</em>), звук станет ровно на октаву выше — частота вырастет вдвое. Деревянный корпус работает как резонатор (глава 25) и усиливает звук струны.</p>',
      '<p>The komuz has no frets: the player presses the string with a finger himself, changing the length of the vibrating part. If the string is pressed in the middle (<em>L/2</em>) the sound becomes exactly an octave higher — the frequency doubles. The wooden body works as a resonator (chapter 25) and amplifies the sound of the string.</p>'),
 lab2)

lab3 = model(3, 'ГРОМКОСТЬ В ДЕЦИБЕЛАХ', 'LOUDNESS IN DECIBELS', 'dbSvg', '0 0 600 250',
  slider('bl', 'Уровень на расстоянии 1 м', 'Level at a distance of 1 m', 40, 110, 1, 80) + slider('br', 'Расстояние до источника', 'Distance to the source', 1, 100, 1, 1) + slider('bn', 'Число одинаковых источников', 'Number of identical sources', 1, 100, 1, 1),
  stats([('bL', 'Уровень звука', 'Sound level'), ('bR', 'Сравнение', 'Comparison')]),
  'dbFb', 'Схема условная: точечный источник в свободном пространстве, L = L₁ − 20·lg(r) + 10·lg(N); отражения не учитываются.',
  'A schematic drawing: a point source in free space, L = L₁ − 20·lg(r) + 10·lg(N); reflections are ignored.')
s3 = section('loud', 'Громкость и децибелы', 'Loudness and decibels',
 bd('<p>Громкость измеряют в <strong>децибелах</strong> (дБ) — по логарифмической шкале: рост на 10 дБ означает рост мощности звука в 10 раз, на 20 дБ — в 100 раз. Шёпот — около 30 дБ, разговор — 60 дБ, шумная улица — 80 дБ, концерт рядом с колонками — свыше 100 дБ. Длительный шум выше примерно 85 дБ повреждает слух.</p><p>Звук слабеет с расстоянием: при удалении вдвое мощность в точке падает вчетверо, то есть уровень снижается на 6 дБ. Десять одинаковых источников вместе громче одного всего на 10 дБ, а не в десять раз «на слух».</p>',
    '<p>Loudness is measured in <strong>decibels</strong> (dB) on a logarithmic scale: a rise of 10 dB means a tenfold rise in sound power, 20 dB — a hundredfold. A whisper is about 30 dB, a conversation 60 dB, a noisy street 80 dB, a concert next to the speakers over 100 dB. Prolonged noise above about 85 dB damages hearing.</p><p>Sound weakens with distance: when the distance doubles the power at the point falls four times, that is the level drops by 6 dB. Ten identical sources together are louder than one by only 10 dB, not ten times “by ear”.</p>'),
 lab3)

tasks = [
 task(1, 'Эхо от стены', 'An echo from a wall', 'Звук хлопка отражается от стены в 85 м. Через какое время вернётся эхо? Скорость звука 340 м/с.', 'The sound of a clap is reflected from a wall 85 m away. After what time does the echo return? The speed of sound is 340 m/s.',
  'd = 85 м, v = 340 м/с', 'd = 85 m, v = 340 m/s', 't = 2d / v = 2 · 85 / 340 = 0,5 с.', 't = 2d / v = 2 · 85 / 340 = 0.5 s.', '0,5 с — эхо слышно отдельно.', '0.5 s — the echo is heard separately.', True),
 task(2, 'Расстояние до скалы', 'Distance to a cliff', 'Крикнули в ущелье, эхо вернулось через 3 с. Как далеко скала? v = 340 м/с.', 'Someone shouted into a gorge and the echo returned after 3 s. How far is the cliff? v = 340 m/s.',
  't = 3 с, v = 340 м/с', 't = 3 s, v = 340 m/s', 'Звук прошёл путь 2d = v·t = 340 · 3 = 1020 м.<br>d = 510 м.', 'The sound covered 2d = v·t = 340 · 3 = 1,020 m.<br>d = 510 m.', '510 м.', '510 m.'),
 task(3, 'Звук на морозе', 'Sound in frost', 'Какова скорость звука в воздухе при −10 °C по формуле v ≈ 331 + 0,6·t?', 'What is the speed of sound in air at −10 °C by the formula v ≈ 331 + 0.6·t?',
  't = −10 °C', 't = −10 °C', 'v = 331 + 0,6 · (−10) = 331 − 6 = 325 м/с.', 'v = 331 + 0.6 · (−10) = 331 − 6 = 325 m/s.', '325 м/с.', '325 m/s.'),
 task(4, 'Частота струны', 'Frequency of a string', 'Струна длиной 0,6 м, масса 1 м струны 1 г (0,001 кг), сила натяжения 36 Н. Найдите основную частоту.', 'A string of length 0.6 m, mass of 1 m of string 1 g (0.001 kg), tension 36 N. Find the fundamental frequency.',
  'L = 0,6 м, μ = 0,001 кг/м, F = 36 Н', 'L = 0.6 m, μ = 0.001 kg/m, F = 36 N', 'f = (1 / 2L) · √(F/μ) = (1 / 1,2) · √36000 = (1 / 1,2) · 189,7 ≈ 158 Гц.', 'f = (1 / 2L) · √(F/μ) = (1 / 1.2) · √36,000 = (1 / 1.2) · 189.7 ≈ 158 Hz.', 'около 158 Гц.', 'about 158 Hz.'),
 task(5, 'Октава', 'An octave', 'Струну из задачи 4 прижали посередине. Какова теперь частота?', 'The string of problem 4 is pressed in the middle. What is the frequency now?',
  'L′ = 0,3 м', 'L′ = 0.3 m', 'f′ = (1 / 0,6) · 189,7 ≈ 316 Гц — вдвое выше (L вдвое короче).', 'f′ = (1 / 0.6) · 189.7 ≈ 316 Hz — twice as high (L is half as long).', '316 Гц — октава вверх.', '316 Hz — an octave up.'),
 task(6, 'Децибелы и расстояние', 'Decibels and distance', 'На расстоянии 1 м уровень звука 80 дБ. Каков уровень на расстоянии 10 м и 100 м?', 'At a distance of 1 m the sound level is 80 dB. What is the level at 10 m and at 100 m?',
  'L₁ = 80 дБ', 'L₁ = 80 dB', 'L = L₁ − 20·lg(r).<br>r = 10 м: 80 − 20 = 60 дБ.<br>r = 100 м: 80 − 40 = 40 дБ.', 'L = L₁ − 20·lg(r).<br>r = 10 m: 80 − 20 = 60 dB.<br>r = 100 m: 80 − 40 = 40 dB.', '60 дБ и 40 дБ.', '60 dB and 40 dB.'),
]

quiz = [
 qz('Что такое звук?', 'Продольная механическая волна в среде', 'Электромагнитная волна', 'Поток частиц света', 'Звуку нужна упругая среда (воздух, вода, твёрдое тело).',
    'What is sound?', 'A longitudinal mechanical wave in a medium', 'An electromagnetic wave', 'A stream of light particles', 'Sound needs an elastic medium (air, water, a solid).'),
 qz('Может ли звук распространяться в вакууме?', 'Нет', 'Да, но медленно', 'Да, быстрее, чем в воздухе', 'В пустоте нет частиц, чтобы передавать колебания.',
    'Can sound travel in a vacuum?', 'No', 'Yes but slowly', 'Yes, faster than in air', 'There are no particles in a void to pass the oscillations on.'),
 qz('Где звук идёт быстрее всего?', 'В стали', 'В воздухе', 'В воде', 'В твёрдых телах упругость больше, и скорость звука выше.',
    'Where does sound travel fastest?', 'In steel', 'In air', 'In water', 'Solids are more elastic so the speed of sound is higher.'),
 qz('Что определяет высоту звука?', 'Частота колебаний', 'Амплитуда колебаний', 'Скорость ветра', 'Чем больше частота, тем выше тон; амплитуда определяет громкость.',
    'What determines the pitch of a sound?', 'The frequency of oscillations', 'The amplitude of oscillations', 'The wind speed', 'The greater the frequency the higher the tone; the amplitude sets the loudness.'),
 qz('Что произойдёт со звуком струны, если её укоротить вдвое?', 'Частота вырастет вдвое', 'Частота уменьшится вдвое', 'Не изменится', 'f = (1/2L)√(F/μ): при L вдвое меньше f вдвое больше.',
    'What happens to the sound of a string if it is shortened by half?', 'The frequency doubles', 'The frequency halves', 'It does not change', 'f = (1/2L)√(F/μ): with L halved, f doubles.'),
 qz('Какова скорость звука в воздухе при 20 °C (примерно)?', '343 м/с', '3 000 м/с', '30 м/с', 'При 20 °C скорость звука в воздухе около 343 м/с.',
    'What is the speed of sound in air at 20 °C (approximately)?', '343 m/s', '3,000 m/s', '30 m/s', 'At 20 °C the speed of sound in air is about 343 m/s.'),
 qz('Как работает эхо?', 'Звук отражается от преграды и возвращается', 'Звук ускоряется в ущелье', 'Звук превращается в свет', 'Отражённая волна возвращается к источнику.',
    'How does an echo work?', 'The sound is reflected by an obstacle and returns', 'The sound speeds up in a gorge', 'The sound turns into light', 'The reflected wave returns to the source.'),
 qz('Во сколько раз вырастет мощность звука при увеличении уровня на 20 дБ?', 'В 100 раз', 'В 20 раз', 'В 2 раза', 'Каждые 10 дБ — рост мощности в 10 раз.',
    'By how much does sound power grow when the level rises by 20 dB?', '100 times', '20 times', '2 times', 'Each 10 dB is a tenfold rise in power.'),
]

js = r'''
const T={ru:{
 ecLabel:"Человек, ущелье и звук, идущий к скале и обратно",kzLabel:"Струна комуза и её стоячая волна",dbLabel:"Шкала уровня звука в децибелах",
 yes:"да",no:"нет, сливается с исходным звуком",
 cmp:["тише шёпота","шёпот","разговор","шумная улица","опасно для слуха при долгом воздействии"],
 ecFb:"Теплее воздух — звук быстрее и эхо возвращается раньше.",kzFb:"Короче и туже струна — звук выше; прижатие на половине даёт октаву.",dbFb:"Каждые 10 дБ — это мощность в 10 раз больше."},
 en:{
 ecLabel:"A person, a gorge and the sound going to the cliff and back",kzLabel:"A komuz string and its standing wave",dbLabel:"A scale of sound level in decibels",
 yes:"yes",no:"no, it merges with the original sound",
 cmp:["quieter than a whisper","a whisper","a conversation","a noisy street","dangerous for hearing under long exposure"],
 ecFb:"The warmer the air, the faster the sound and the sooner the echo returns.",kzFb:"A shorter and tighter string — a higher sound; pressing at half-length gives an octave.",dbFb:"Every 10 dB is ten times the power."}};
function drawEc(){const t=tt(),tc=+$("et").value,d=+$("ed").value,v=331+0.6*tc,e=2*d/v;
 const cx=60+Math.min(1,d/500)*380;
 let g='<polygon points="'+(cx)+',200 '+(cx+30)+',60 '+(cx+90)+',40 '+(cx+90)+',200" fill="#c9c2b0" stroke="#18181a"/><rect x="40" y="170" width="520" height="30" fill="#e8e4d8" stroke="none"/>';
 g+='<circle cx="50" cy="160" r="9" fill="#18181a"/><line x1="50" y1="169" x2="50" y2="195" stroke="#18181a" stroke-width="3"/>';
 g+=arrow(70,140,cx-8,140,"#3f5f8f",3)+arrow(cx-8,125,70,125,"#b6533f",3)+svgText((70+cx)/2,115,"d = "+d+UN[lang].m,"#18181a","middle",12);
 $("ecSvg").innerHTML=g;
 $("etOut").textContent=tc+UN[lang].C;$("edOut").textContent=d+UN[lang].m;
 $("eV").textContent=fmt(v,0)+UN[lang].ms;$("eT").textContent=fmt(e,2)+UN[lang].s;$("eK").textContent=e>=0.1?t.yes:t.no;$("ecFb").textContent=t.ecFb}
["et","ed"].forEach(id=>$(id).addEventListener("input",drawEc));
const NN=["C","C♯","D","D♯","E","F","F♯","G","G♯","A","A♯","B"];
function noteOf(f){const m=Math.round(12*Math.log2(f/440)+69),o=Math.floor(m/12)-1;return NN[((m%12)+12)%12]+o}
function drawKz(){const t=tt(),L=+$("kl").value,F=+$("kt").value,mu=+$("km").value/1000,fr=+$("kf").value,Le=L*fr,f=Math.sqrt(F/mu)/(2*Le);
 let g='<line x1="40" y1="125" x2="560" y2="125" stroke="#c9c2b0"/>';
 const x0=40,x1=40+520*fr,pts=[];for(let i=0;i<=200;i++){const x=i/200;pts.push((x0+(x1-x0)*x)+","+(125-55*Math.sin(Math.PI*x)))}
 g+='<polyline fill="none" stroke="#b6533f" stroke-width="3" points="'+pts.join(" ")+'"/><polyline fill="none" stroke="#b6533f" stroke-width="1" stroke-dasharray="4 4" points="'+pts.map(p=>{const a=p.split(",");return a[0]+","+(250-a[1])}).join(" ")+'"/>';
 g+='<circle cx="'+x0+'" cy="125" r="6" fill="#18181a"/><circle cx="'+x1+'" cy="125" r="6" fill="#18181a"/>'+svgText(300,235,"L = "+fmt(Le,2)+UN[lang].m,"#66666b","middle",12);
 $("kzSvg").innerHTML=g;
 $("klOut").textContent=fmt(L,2)+UN[lang].m;$("ktOut").textContent=F+UN[lang].N;$("kmOut").textContent=fmt(mu*1000,2)+(lang==="ru"?" г":" g");$("kfOut").textContent=fmt(fr,2);
 $("kF").textContent=fmt(f,0)+(lang==="ru"?" Гц":" Hz");$("kN").textContent=noteOf(f);$("kH").textContent=fmt(2*f,0)+", "+fmt(3*f,0)+(lang==="ru"?" Гц":" Hz");$("kzFb").textContent=t.kzFb}
["kl","kt","km","kf"].forEach(id=>$(id).addEventListener("input",drawKz));
function drawDb(){const t=tt(),L1=+$("bl").value,r=+$("br").value,n=+$("bn").value,L=L1-20*Math.log10(r)+10*Math.log10(n);
 const X=l=>40+(l+10)/140*520;let g='<rect x="40" y="90" width="520" height="30" fill="#e3e1da"/><rect x="40" y="90" width="'+Math.max(0,X(L)-40)+'" height="30" fill="'+(L>=85?"#b6533f":"#2f6f5d")+'"/>';
 [[0,"0"],[30,"30"],[60,"60"],[85,"85"],[100,"100"],[120,"120"]].forEach(a=>g+='<line x1="'+X(a[0])+'" y1="85" x2="'+X(a[0])+'" y2="125" stroke="#18181a"/>'+svgText(X(a[0]),140,a[1],"#66666b","middle",11));
 g+=svgText(300,190,fmt(L,0)+" dB","#18181a","middle",22);
 $("dbSvg").innerHTML=g;
 $("blOut").textContent=L1+" dB";$("brOut").textContent=r+UN[lang].m;$("bnOut").textContent=n;
 const k=L<25?0:L<45?1:L<70?2:L<85?3:4;$("bL").textContent=fmt(L,0)+" dB";$("bR").textContent=t.cmp[k];$("dbFb").textContent=t.dbFb}
["bl","br","bn"].forEach(id=>$(id).addEventListener("input",drawDb));
const LAB={ru:{ecSvg:T.ru.ecLabel,kzSvg:T.ru.kzLabel,dbSvg:T.ru.dbLabel},en:{ecSvg:T.en.ecLabel,kzSvg:T.en.kzLabel,dbSvg:T.en.dbLabel}};
function drawAll(){drawEc();drawKz();drawDb()}
'''

c = dict(n='27', slug='27-sound.html', block='V', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Звук', 'Sound'),
 desc='Глава 27 Атласа физики: скорость звука, эхо в горах, высота звука и струна комуза, громкость в децибелах.',
 lead=('Эхо в горном ущелье, струны комуза и шум города. Скорость звука, высота, громкость.',
       'An echo in a mountain gorge, the strings of the komuz and the noise of a city. The speed of sound, pitch, loudness.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('speed', 'Скорость звука', 'Speed of sound'), ('string', 'Комуз', 'The komuz'), ('loud', 'Громкость', 'Loudness'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>В горном ущелье вы кричите «Эй!» и через несколько секунд слышите свой голос, вернувшийся от скалы напротив. На открытой равнине такого не бывает. А пастух по эху прикидывает, далеко ли до скалы, не измеряя ничего рулеткой.</p><p>Как по паузе между криком и эхом определить расстояние до скалы?</p>',
         '<p>In a mountain gorge you shout “Hey!” and a few seconds later hear your voice come back from the cliff opposite. On an open plain this does not happen. A shepherd judges from the echo how far the cliff is without measuring anything with a tape.</p><p>How can you find the distance to a cliff from the pause between the shout and the echo?</p>'),
 hint=stdhint('Эхо в ущелье', 'An echo in a gorge'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: звук проходит путь туда и обратно', 'The answer: sound goes there and back'),
 answer=('<p>Звук доходит до скалы и возвращается, поэтому за паузу <em>t</em> он проходит путь <em>2d = v·t</em>. Отсюда <em>d = v·t / 2</em>. Если эхо пришло через 3 с, а скорость звука около 340 м/с, то до скалы примерно 510 м (модель 1). В воздухе скорость звука растёт с температурой, так что на морозе путь по эху получится чуть короче.</p><p>На равнине звук уходит дальше и не возвращается: отражающей преграды нет. По тому же принципу работает эхолот на лодке.</p>',
         '<p>The sound reaches the cliff and comes back so in the pause <em>t</em> it covers a path of <em>2d = v·t</em>. Hence <em>d = v·t / 2</em>. If the echo came after 3 s and the speed of sound is about 340 m/s then the cliff is about 510 m away (model 1). In air the speed of sound grows with temperature, so in frost the distance judged from the echo comes out slightly shorter.</p><p>On a plain the sound goes farther and does not return: there is no reflecting obstacle. A boat’s echo sounder works on the same principle.</p>'),
 sources=[
  ('Скорость звука в воздухе, воде и стали; v ≈ 331 + 0,6·t —', 'The speed of sound in air, water and steel; v ≈ 331 + 0.6·t —', LINK('https://en.wikipedia.org/wiki/Speed_of_sound', 'Wikipedia: Speed of sound') + ', ' + LINK('https://openstax.org/books/university-physics-volume-1/pages/17-introduction', 'OpenStax University Physics, Vol. 1, гл. 17')),
  ('Колебания струны, f = (1/2L)√(F/μ) —', 'The vibrations of a string, f = (1/2L)√(F/μ) —', LINK('https://en.wikipedia.org/wiki/String_vibration', 'Wikipedia: String vibration')),
  ('Комуз: трёхструнный лютневый инструмент без ладов, корпус из абрикосового, орехового или можжевелового дерева —', 'The komuz: a three-string fretless lute with a body of apricot, walnut or juniper wood —', LINK('https://en.wikipedia.org/wiki/Komuz', 'Wikipedia: Komuz')),
  ('Децибелы и повреждение слуха при шуме выше ≈ 85 дБ —', 'Decibels and hearing damage from noise above ≈ 85 dB —', LINK('https://en.wikipedia.org/wiki/Noise-induced_hearing_loss', 'Wikipedia: Noise-induced hearing loss'))],
 note=stdnote('Параметры струны комуза (масса метра, натяжение, длина) выбраны для модели и не относятся к конкретному инструменту.', 'The komuz string parameters (mass per metre, tension, length) are chosen for the model and do not belong to a specific instrument.'),
 prev=('26-mechanical-waves.html', 'Глава 26 · Механические волны', 'Chapter 26 · Mechanical waves'),
 next=('28-earthquakes.html', 'Глава 28 · Землетрясения', 'Chapter 28 · Earthquakes'),
 js=js)
build(c)
