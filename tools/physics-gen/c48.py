# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ШКАЛА ЭЛЕКТРОМАГНИТНЫХ ВОЛН', 'THE ELECTROMAGNETIC SPECTRUM', 'emSvg', '0 0 600 250',
  slider('ef', 'Частота (степень десяти, Гц)', 'Frequency (power of ten, Hz)', 4, 22, 0.1, 8),
  stats([('eF', 'Частота', 'Frequency'), ('eL', 'Длина волны λ = c/f', 'Wavelength λ = c/f'), ('eE', 'Энергия фотона E = h·f', 'Photon energy E = h·f'), ('eB', 'Диапазон', 'Range')]),
  'emFb', 'Схема условная: границы диапазонов приблизительны; c = 3·10⁸ м/с; h = 4,14·10⁻¹⁵ эВ·с; шкала логарифмическая.',
  'A schematic drawing: the boundaries of ranges are approximate; c = 3·10⁸ m/s; h = 4.14·10⁻¹⁵ eV·s; the scale is logarithmic.')
s1 = section('spectrum', 'Свет, радио и рентген — одно и то же', 'Light, radio and X-rays are the same thing',
 bd('<p>Максвелл показал: меняющееся электрическое поле порождает магнитное, а меняющееся магнитное — электрическое (глава 23). Так в пространстве может бежать волна из двух связанных полей — <strong>электромагнитная волна</strong>. Её скорость в вакууме получилась равной скорости света <em>c ≈ 3·10⁸ м/с</em>, и Максвелл понял, что свет — тоже такая волна. Все электромагнитные волны распространяются в вакууме с одной скоростью и отличаются <em>частотой</em> (и длиной волны): <em>c = λ·f</em>. От частоты зависят энергия фотона и то, как волна взаимодействует с веществом.</p>',
    '<p>Maxwell showed: a changing electric field produces a magnetic one and a changing magnetic field produces an electric one (chapter 23). So a wave of two linked fields can run through space — an <strong>electromagnetic wave</strong>. Its speed in a vacuum turned out to equal the speed of light <em>c ≈ 3·10⁸ m/s</em> and Maxwell understood that light is also such a wave. All electromagnetic waves travel in a vacuum at one speed and differ in <em>frequency</em> (and wavelength): <em>c = λ·f</em>. The photon energy and how the wave interacts with matter depend on the frequency.</p>')
 + formula('c = λ · f,   E = h · f', 'радио — километры и метры; свет — доли микрометра; рентген — доли нанометра', 'radio — kilometres and metres; light — fractions of a micrometre; X-rays — fractions of a nanometre'),
 lab1)

lab2 = model(2, 'РАДИОСВЯЗЬ: АНТЕННА И ЗАДЕРЖКА', 'RADIO COMMUNICATION: ANTENNA AND DELAY', 'raSvg', '0 0 600 250',
  select('rs', 'Служба', 'Service') + slider('rd', 'Расстояние до передатчика', 'Distance to the transmitter', 1, 400000, 1, 35786),
  stats([('rL', 'Длина волны', 'Wavelength'), ('rA', 'Четвертьволновая антенна λ/4', 'Quarter-wave antenna λ/4'), ('rT', 'Время сигнала в одну сторону', 'One-way signal time')]),
  'raFb', 'Схема условная: рабочие частоты службы округлены; расстояние в километрах; сигнал идёт по прямой со скоростью света.',
  'A schematic drawing: the operating frequencies of the service are rounded; the distance in kilometres; the signal goes in a straight line at the speed of light.')
s2 = section('radio', 'Радио: длина волны, антенна, задержка', 'Radio: wavelength, antenna, delay',
 bd('<p>Эффективная антенна по размеру сравнима с длиной волны: простейшая — штырь длиной <em>λ/4</em>. Для FM-радио (около 100 МГц) λ = 3 м, значит антенна около 75 см; для Wi-Fi (2,4 ГГц) λ ≈ 12,5 см — антенну прячут внутрь роутера. Радиоволны идут со скоростью света, поэтому у далёких объектов появляется задержка: сигнал до геостационарного спутника на высоте 35 786 км идёт около 0,12 с, туда и обратно — около 0,24 с. Так же радиосигналом управляют и спутником, запущенным Кыргызстаном (глава 36), из центра управления в Бишкеке.</p>',
    '<p>An efficient antenna is comparable in size to the wavelength: the simplest is a rod of length <em>λ/4</em>. For FM radio (about 100 MHz) λ = 3 m so the antenna is about 75 cm; for Wi-Fi (2.4 GHz) λ ≈ 12.5 cm — the antenna is hidden inside the router. Radio waves travel at the speed of light so distant objects introduce a delay: a signal to a geostationary satellite at a height of 35,786 km takes about 0.12 s, there and back about 0.24 s. Radio signals are also used to control the satellite launched by Kyrgyzstan (chapter 36) from the control centre in Bishkek.</p>')
 + formula('λ = c / f,   t = d / c', 'сигнал до Луны (384 400 км) идёт около 1,28 с', 'a signal to the Moon (384,400 km) takes about 1.28 s'),
 lab2)

lab3 = model(3, 'ОСЛАБЛЕНИЕ СИГНАЛА С РАССТОЯНИЕМ', 'SIGNAL WEAKENING WITH DISTANCE', 'inSvg', '0 0 600 250',
  slider('ip', 'Мощность передатчика', 'Transmitter power', 0.1, 1000, 0.1, 10) + slider('ir', 'Расстояние до передатчика', 'Distance to the transmitter', 1, 100, 1, 10),
  stats([('iI', 'Плотность потока энергии I = P/(4πr²)', 'Energy flux density I = P/(4πr²)'), ('iE', 'Действующая напряжённость поля E = √(I·377)', 'RMS field strength E = √(I·377)'), ('iR', 'Во сколько раз слабее, чем на расстоянии 1 км', 'How many times weaker than at 1 km')]),
  'inFb', 'Схема условная: ненаправленный излучатель в свободном пространстве (без поглощения и отражений); 377 Ом — волновое сопротивление вакуума.',
  'A schematic drawing: an isotropic radiator in free space (no absorption or reflections); 377 Ω is the impedance of free space.')
s3 = section('intensity', 'Почему сигнал слабеет с расстоянием', 'Why a signal weakens with distance',
 bd('<p>Передатчик излучает энергию во все стороны, и она распределяется по сфере площадью <em>4πr²</em>. Поэтому плотность потока энергии убывает как <em>1/r²</em>: на расстоянии вдвое большем сигнал в 4 раза слабее — так же, как свет лампы (глава 29) и звук. Напряжённость поля падает как <em>1/r</em>. В горах и ущельях к этому добавляются тени и отражения от скал — поэтому мобильная связь пропадает в узких долинах.</p>',
    '<p>A transmitter radiates energy in all directions and it spreads over a sphere of area <em>4πr²</em>. So the energy flux density falls as <em>1/r²</em>: at twice the distance the signal is 4 times weaker — like the light of a lamp (chapter 29) and sound. The field strength falls as <em>1/r</em>. In the mountains and gorges shadows and reflections from rocks are added — so mobile coverage disappears in narrow valleys.</p>')
 + formula('I = P / (4π·r²),   E ~ 1/r', 'передатчик 10 кВт на 10 км: ≈ 8 мкВт/м²', 'a 10 kW transmitter at 10 km: ≈ 8 µW/m²'),
 lab3)

tasks = [
 task(1, 'Антенна для FM', 'An antenna for FM', 'Станция вещает на частоте 100 МГц. Найдите длину волны и длину четвертьволновой антенны.', 'A station broadcasts at 100 MHz. Find the wavelength and the length of a quarter-wave antenna.',
  'f = 10⁸ Гц, c = 3·10⁸ м/с', 'f = 10⁸ Hz, c = 3·10⁸ m/s', 'λ = c/f = 3·10⁸ / 10⁸ = 3 м.<br>λ/4 = 0,75 м.', 'λ = c/f = 3·10⁸ / 10⁸ = 3 m.<br>λ/4 = 0.75 m.', '3 м; 75 см.', '3 m; 75 cm.', True),
 task(2, 'Wi-Fi', 'Wi-Fi', 'Найдите длину волны Wi-Fi на частоте 2,4 ГГц.', 'Find the wavelength of Wi-Fi at 2.4 GHz.',
  'f = 2,4·10⁹ Гц', 'f = 2.4·10⁹ Hz', 'λ = 3·10⁸ / 2,4·10⁹ = 0,125 м.', 'λ = 3·10⁸ / 2.4·10⁹ = 0.125 m.', '12,5 см.', '12.5 cm.'),
 task(3, 'Задержка до спутника', 'The delay to a satellite', 'Найдите время прохождения сигнала до геостационарного спутника (35 786 км) в одну сторону и туда и обратно.', 'Find the signal travel time to a geostationary satellite (35,786 km) one way and there and back.',
  'd = 3,58·10⁷ м', 'd = 3.58·10⁷ m', 't = d/c = 3,5786·10⁷ / 3·10⁸ ≈ 0,119 с.<br>Туда и обратно: ≈ 0,24 с.', 't = d/c = 3.5786·10⁷ / 3·10⁸ ≈ 0.119 s.<br>There and back: ≈ 0.24 s.', '≈ 0,12 с и ≈ 0,24 с.', '≈ 0.12 s and ≈ 0.24 s.'),
 task(4, 'До Луны', 'To the Moon', 'Сколько идёт радиосигнал до Луны (384 400 км)?', 'How long does a radio signal take to the Moon (384,400 km)?',
  'd = 3,844·10⁸ м', 'd = 3.844·10⁸ m', 't = 3,844·10⁸ / 3·10⁸ ≈ 1,28 с.', 't = 3.844·10⁸ / 3·10⁸ ≈ 1.28 s.', '≈ 1,3 с.', '≈ 1.3 s.'),
 task(5, 'Энергия фотона радио', 'The energy of a radio photon', 'Сравните энергию фотона Wi-Fi (2,45 ГГц) с энергией фотона видимого света (≈ 2 эВ). (h = 4,14·10⁻¹⁵ эВ·с.)', 'Compare the energy of a Wi-Fi photon (2.45 GHz) with the energy of a visible-light photon (≈ 2 eV). (h = 4.14·10⁻¹⁵ eV·s.)',
  'f = 2,45·10⁹ Гц', 'f = 2.45·10⁹ Hz', 'E = h·f = 4,14·10⁻¹⁵ · 2,45·10⁹ ≈ 1,0·10⁻⁵ эВ.<br>Отношение: 2 / 10⁻⁵ = 2·10⁵.', 'E = h·f = 4.14·10⁻¹⁵ · 2.45·10⁹ ≈ 1.0·10⁻⁵ eV.<br>Ratio: 2 / 10⁻⁵ = 2·10⁵.', '≈ 10⁻⁵ эВ — в 200 000 раз меньше, чем у света; не способен разрывать молекулы.', '≈ 10⁻⁵ eV — 200,000 times less than light; it cannot break molecules.'),
 task(6, 'Плотность потока', 'The flux density', 'Передатчик мощностью 10 кВт излучает во все стороны. Найдите плотность потока энергии на расстоянии 10 км и действующую напряжённость поля.', 'A 10 kW transmitter radiates in all directions. Find the energy flux density at a distance of 10 km and the RMS field strength.',
  'P = 10⁴ Вт, r = 10⁴ м', 'P = 10⁴ W, r = 10⁴ m', 'I = P / (4πr²) = 10⁴ / (12,57 · 10⁸) ≈ 7,96·10⁻⁶ Вт/м².<br>E = √(I · 377) = √(3,0·10⁻³) ≈ 0,055 В/м.', 'I = P / (4πr²) = 10⁴ / (12.57 · 10⁸) ≈ 7.96·10⁻⁶ W/m².<br>E = √(I · 377) = √(3.0·10⁻³) ≈ 0.055 V/m.', '≈ 8 мкВт/м²; ≈ 0,055 В/м.', '≈ 8 µW/m²; ≈ 0.055 V/m.'),
]

quiz = [
 qz('Какая связь между длиной волны и частотой?', 'c = λ·f', 'c = λ/f', 'c = f/λ', 'Чем выше частота, тем короче волна.',
    'What is the relation between wavelength and frequency?', 'c = λ·f', 'c = λ/f', 'c = f/λ', 'The higher the frequency the shorter the wave.'),
 qz('С какой скоростью электромагнитные волны идут в вакууме?', 'Со скоростью света ≈ 3·10⁸ м/с', 'Со скоростью звука', 'Зависит от частоты', 'Все волны идут с одной скоростью.',
    'At what speed do electromagnetic waves travel in a vacuum?', 'At the speed of light ≈ 3·10⁸ m/s', 'At the speed of sound', 'It depends on the frequency', 'All waves travel at one speed.'),
 qz('Что отличает радиоволны от видимого света?', 'Частота (длина волны)', 'Скорость', 'Ничего', 'Это одно и то же явление.',
    'What distinguishes radio waves from visible light?', 'The frequency (wavelength)', 'The speed', 'Nothing', 'It is the same phenomenon.'),
 qz('Какой фотон несёт больше энергии?', 'Рентгеновский', 'Радио', 'Инфракрасный', 'E = h·f.',
    'Which photon carries more energy?', 'An X-ray one', 'A radio one', 'An infrared one', 'E = h·f.'),
 qz('Какова длина четвертьволновой антенны для λ = 3 м?', '0,75 м', '3 м', '12 м', 'λ/4.',
    'What is the length of a quarter-wave antenna for λ = 3 m?', '0.75 m', '3 m', '12 m', 'λ/4.'),
 qz('За какое время сигнал доходит до Луны?', 'Около 1,3 с', 'Около 1 мс', 'Около минуты', 'd/c = 3,844·10⁸ / 3·10⁸.',
    'How long does a signal take to reach the Moon?', 'About 1.3 s', 'About 1 ms', 'About a minute', 'd/c = 3.844·10⁸ / 3·10⁸.'),
 qz('Во сколько раз слабее сигнал при вдвое большем расстоянии?', 'В 4 раза', 'В 2 раза', 'В 8 раз', 'I ~ 1/r².',
    'How many times weaker is the signal at twice the distance?', '4 times', '2 times', '8 times', 'I ~ 1/r².'),
 qz('Почему связь пропадает в узких горных долинах?', 'Скалы затеняют и отражают радиоволны', 'Радиоволны не идут в горах', 'Воздух там разреженный', 'Тени и отражения ослабляют сигнал.',
    'Why does coverage disappear in narrow mountain valleys?', 'Rocks shadow and reflect radio waves', 'Radio waves do not travel in mountains', 'The air is thin there', 'Shadows and reflections weaken the signal.'),
]

js = JSL + r'''
const T={ru:{
 emLabel:"Диапазон электромагнитных волн (логарифмическая шкала)",raLabel:"Передатчик, антенна и сигнал",inLabel:"Энергия расходится по сфере",
 bands:["радио (в т. ч. телевидение, связь)","микроволны (Wi-Fi, печи, радары)","инфракрасное","видимый свет","ультрафиолет","рентген","гамма"],
 svc:["Радио AM (1 МГц)","Радио FM (100 МГц)","Мобильная связь (900 МГц)","Wi-Fi (2,4 ГГц)","GPS (1,575 ГГц)","Связь со спутником (4 ГГц)"],
 emFb:"Все волны — одной природы, различаются частотой.",raFb:"Антенна сравнима с длиной волны; далёкие цели дают задержку.",inFb:"Вдвое дальше — вчетверо слабее."},
 en:{
 emLabel:"The electromagnetic spectrum (logarithmic scale)",raLabel:"A transmitter, antenna and signal",inLabel:"Energy spreads over a sphere",
 bands:["radio (incl. TV, communications)","microwaves (Wi-Fi, ovens, radar)","infrared","visible light","ultraviolet","X-rays","gamma rays"],
 svc:["AM radio (1 MHz)","FM radio (100 MHz)","Mobile (900 MHz)","Wi-Fi (2.4 GHz)","GPS (1.575 GHz)","Satellite link (4 GHz)"],
 emFb:"All waves are of one nature and differ in frequency.",raFb:"The antenna is comparable to the wavelength; distant targets give a delay.",inFb:"Twice as far — four times weaker."}};
const SF=[1e6,1e8,9e8,2.4e9,1.575e9,4e9];
function lenStr(l){if(l>=1000)return fmt(l/1000,1)+" "+U("км","km");if(l>=1)return fmt(l,2)+" "+U("м","m");if(l>=1e-2)return fmt(l*100,1)+" "+U("см","cm");if(l>=1e-3)return fmt(l*1e3,2)+" "+U("мм","mm");if(l>=1e-6)return fmt(l*1e6,2)+" "+U("мкм","µm");if(l>=1e-9)return fmt(l*1e9,2)+" "+U("нм","nm");return sci(l,2)+" "+U("м","m")}
function drawEm(){const t=tt(),e=+$("ef").value,f=Math.pow(10,e),l=3e8/f,E=4.14e-15*f;
 const B=[3e9,3e11,4e14,7.9e14,3e16,3e19];let b=0;while(b<B.length&&f>=B[b])b++;
 const col=["#8a8a8a","#b87333","#7a1f1f","#2f9e44","#6a3d9a","#3f5f8f","#18181a"];
 let g='';const X=v=>40+(v-4)/18*520;const edges=[4,Math.log10(3e9),Math.log10(3e11),Math.log10(4e14),Math.log10(7.9e14),Math.log10(3e16),Math.log10(3e19),22];
 for(let i=0;i<7;i++)g+='<rect x="'+X(edges[i])+'" y="90" width="'+(X(edges[i+1])-X(edges[i]))+'" height="60" fill="'+col[i]+'" opacity="'+(i===b?1:0.35)+'" stroke="#18181a"/>';
 g+='<line x1="'+X(e)+'" y1="70" x2="'+X(e)+'" y2="170" stroke="#b6533f" stroke-width="3"/>'+svgText(X(e),62,"10^"+fmt(e,1),"#18181a","middle",12);
 for(let v=4;v<=22;v+=3)g+=svgText(X(v),190,"10^"+v,"#66666b","middle",10);
 $("emSvg").innerHTML=g;$("efOut").textContent="10^"+fmt(e,1)+" "+U("Гц","Hz");
 $("eF").textContent=sci(f,2)+" "+U("Гц","Hz");$("eL").textContent=lenStr(l);$("eE").textContent=sci(E,2)+" "+U("эВ","eV");$("eB").textContent=t.bands[b];$("emFb").textContent=t.emFb}
$("ef").addEventListener("input",drawEm);
function drawRa(){const t=tt(),k=+$("rs").value,d=+$("rd").value,f=SF[k],l=3e8/f,tm=d*1000/3e8;
 let g='<rect x="60" y="150" width="6" height="60" fill="#18181a"/><line x1="63" y1="150" x2="63" y2="110" stroke="#18181a" stroke-width="3"/>';
 for(let i=1;i<=4;i++)g+='<path d="M'+(63+i*22)+' '+(150-i*10)+' q 18 18 0 36" fill="none" stroke="#3f5f8f" stroke-width="2"/>';
 g+='<circle cx="520" cy="130" r="14" fill="#9a9a9a" stroke="#18181a"/>'+svgText(520,170,U("приёмник","receiver"),"#66666b","middle",11);
 $("raSvg").innerHTML=g;$("rdOut").textContent=num(d)+" "+U("км","km");
 const tt2=tm<1?fmt(tm*1000,tm<0.01?2:1)+" "+U("мс","ms"):fmt(tm,2)+" "+U("с","s");
 $("rL").textContent=lenStr(l);$("rA").textContent=lenStr(l/4);$("rT").textContent=tt2;$("raFb").textContent=t.raFb}
["rs","rd"].forEach(id=>$(id).addEventListener("input",drawRa));
function drawIn(){const t=tt(),P=+$("ip").value*1000,r=+$("ir").value*1000,I=P/(4*Math.PI*r*r),E=Math.sqrt(I*377),I1=P/(4*Math.PI*1e6);
 let g='<circle cx="120" cy="125" r="6" fill="#b6533f"/>';for(let i=1;i<=5;i++)g+='<circle cx="120" cy="125" r="'+(i*i*3+20)+'" fill="none" stroke="#3f5f8f" opacity="'+(1/(i*0.8))+'"/>';
 g+=svgText(300,60,"I = "+sci(I,2)+" "+U("Вт/м²","W/m²"),"#18181a","start",16)+svgText(300,95,"E = "+fmt(E,3)+" "+U("В/м","V/m"),"#18181a","start",16);
 $("inSvg").innerHTML=g;$("ipOut").textContent=fmt(P/1000,1)+" "+U("кВт","kW");$("irOut").textContent=Math.round(r/1000)+" "+U("км","km");
 $("iI").textContent=sci(I,2)+" "+U("Вт/м²","W/m²");$("iE").textContent=fmt(E,3)+" "+U("В/м","V/m");$("iR").textContent=fmt(I1/I,0)+"×";$("inFb").textContent=t.inFb}
["ip","ir"].forEach(id=>$(id).addEventListener("input",drawIn));
const LAB={ru:{emSvg:T.ru.emLabel,raSvg:T.ru.raLabel,inSvg:T.ru.inLabel},en:{emSvg:T.en.emLabel,raSvg:T.en.raLabel,inSvg:T.en.inLabel}};
function drawAll(){fillSel("rs",T[lang].svc,1);drawEm();drawRa();drawIn()}
'''

c = dict(n='48', slug='48-electromagnetic-waves.html', block='VIII', level_ru='УГЛУБЛЁННО', level_en='ADVANCED',
 title=('Электромагнитные волны', 'Electromagnetic waves'),
 desc='Глава 48 Атласа физики: теория Максвелла, шкала электромагнитных волн, длина волны и частота, антенна, задержка сигнала, ослабление с расстоянием.',
 lead=('Свет, радио, Wi-Fi и рентген — одно и то же явление с разной частотой. Длина волны, антенна и задержка сигнала.',
       'Light, radio, Wi-Fi and X-rays are one phenomenon at different frequencies. Wavelength, antenna and signal delay.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('spectrum', 'Шкала волн', 'The spectrum'), ('radio', 'Радио', 'Radio'), ('intensity', 'Ослабление', 'Weakening'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Телефон ловит сигнал вышки, но через стену Wi-Fi идёт хуже, чем FM-радио. Лампа даёт свет, но не пролетает сквозь стену, как радиоволна, а рентген проходит сквозь мягкие ткани. Кажется, у каждого излучения свои законы — свои приборы, свои единицы, свои «характеры».</p><p>Что общего у света, радио, Wi-Fi и рентгена?</p>',
         '<p>A phone catches a signal from a tower but Wi-Fi gets through a wall worse than FM radio. A lamp gives light but does not pass through a wall as a radio wave does while X-rays pass through soft tissue. Each radiation seems to have its own laws — its own devices, units and “characters”.</p><p>What do light, radio, Wi-Fi and X-rays have in common?</p>'),
 hint=stdhint('Шкала электромагнитных волн', 'The electromagnetic spectrum'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: это одна и та же волна', 'The answer: it is one and the same wave'),
 answer=('<p>Свет, радио, Wi-Fi, инфракрасное, ультрафиолет и рентген — электромагнитные волны, которые отличаются только частотой. В вакууме все они идут со скоростью света, а связь частоты и длины волны даёт формула <em>c = λ·f</em>. Частота определяет энергию фотона <em>E = h·f</em> и взаимодействие с веществом: радиофотон слишком слаб, чтобы рвать молекулы, а рентгеновский — нет; длинные волны огибают препятствия, а короткие дают чёткие тени.</p><p>Максвелл предсказал эти волны теоретически в 1860-х годах, а Герц получил радиоволны в опыте в 1880-х — так появились радио и связь.</p>',
         '<p>Light, radio, Wi-Fi, infrared, ultraviolet and X-rays are electromagnetic waves that differ only in frequency. In a vacuum they all travel at the speed of light and the link between frequency and wavelength is <em>c = λ·f</em>. The frequency fixes the photon energy <em>E = h·f</em> and the interaction with matter: a radio photon is too weak to break molecules while an X-ray one is not; long waves bend around obstacles while short ones give sharp shadows.</p><p>Maxwell predicted these waves theoretically in the 1860s and Hertz produced radio waves in an experiment in the 1880s — so radio and communications appeared.</p>'),
 sources=[
  ('Электромагнитные волны, шкала, антенны, плотность потока энергии —', 'Electromagnetic waves, the spectrum, antennas, energy flux density —', LINK('https://openstax.org/books/university-physics-volume-2/pages/16-introduction', 'OpenStax University Physics, Vol. 2, гл. 16') + ', ' + LINK('https://en.wikipedia.org/wiki/Electromagnetic_spectrum', 'Wikipedia: Electromagnetic spectrum')),
  ('Максвелл и Герц —', 'Maxwell and Hertz —', LINK('https://en.wikipedia.org/wiki/Maxwell%27s_equations', 'Wikipedia: Maxwell’s equations') + ', ' + LINK('https://en.wikipedia.org/wiki/Heinrich_Hertz', 'Wikipedia: Heinrich Hertz')),
  ('Геостационарная орбита (35 786 км) —', 'The geostationary orbit (35,786 km) —', LINK('https://en.wikipedia.org/wiki/Geostationary_orbit', 'Wikipedia: Geostationary orbit'))],
 note=stdnote('Границы диапазонов приблизительны; рабочие частоты служб округлены; модель 3 не учитывает отражения и поглощение.', 'The boundaries of the ranges are approximate; the operating frequencies of the services are rounded; model 3 ignores reflections and absorption.'),
 prev=('47-alternating-current.html', 'Глава 47 · Переменный ток', 'Chapter 47 · Alternating current'),
 next=('49-relativity.html', 'Глава 49 · Относительность', 'Chapter 49 · Relativity'),
 js=js)
build(c)
