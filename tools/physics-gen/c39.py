# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'УРОВНИ ЭНЕРГИИ ВОДОРОДА', 'HYDROGEN ENERGY LEVELS', 'lvSvg', '0 0 600 250',
  slider('an', 'Верхний уровень n', 'Upper level n', 2, 7, 1, 3) + slider('am', 'Нижний уровень n', 'Lower level n', 1, 6, 1, 2),
  stats([('aE', 'Энергия фотона ΔE = 13,6·(1/m² − 1/n²)', 'Photon energy ΔE = 13.6·(1/m² − 1/n²)'), ('aL', 'Длина волны', 'Wavelength'), ('aS', 'Серия линий', 'Line series')]),
  'lvFb', 'Схема условная: упрощённая модель Бора; E_n = −13,6 эВ / n²; уровни нарисованы без точного масштаба.',
  'A schematic drawing: the simplified Bohr model; E_n = −13.6 eV / n²; the levels are not drawn to exact scale.')
s1 = section('levels', 'Атом излучает порциями', 'An atom emits in portions',
 bd('<p>Электрон в атоме может иметь только определённые значения энергии — <strong>уровни</strong>. У водорода (по модели Бора) <em>E<sub>n</sub> = −13,6 эВ / n²</em>: основное состояние <em>n = 1</em> (−13,6 эВ), затем −3,4; −1,51; −0,85 эВ… Знак минус означает, что электрон связан с ядром. При переходе вниз атом испускает один фотон, энергия которого равна разности уровней.</p>',
    '<p>An electron in an atom can have only certain values of energy — <strong>levels</strong>. For hydrogen (by the Bohr model) <em>E<sub>n</sub> = −13.6 eV / n²</em>: the ground state <em>n = 1</em> (−13.6 eV), then −3.4; −1.51; −0.85 eV… The minus sign means the electron is bound to the nucleus. In a downward transition the atom emits one photon whose energy equals the difference of the levels.</p>')
 + formula('hf = E_n − E_m,   λ = 1240 эВ·нм / ΔE', 'переходы на n = 2 дают видимые линии серии Бальмера, на n = 1 — ультрафиолет (серия Лаймана)', 'transitions to n = 2 give the visible lines of the Balmer series, to n = 1 — ultraviolet (the Lyman series)'),
 lab1)

lab2 = model(2, 'РАЗМЕРЫ АТОМА И ЯДРА', 'THE SIZES OF THE ATOM AND THE NUCLEUS', 'szSvg', '0 0 600 250',
  slider('zn', 'Уровень n атома водорода', 'Level n of the hydrogen atom', 1, 6, 1, 1) + slider('zp', 'Ядро — горошина диаметром', 'The nucleus is a pea of diameter', 2, 10, 1, 5),
  stats([('zR', 'Радиус орбиты r = 0,0529·n² нм', 'Orbit radius r = 0.0529·n² nm'), ('zD', 'Диаметр атома, если ядро — горошина', 'Atom diameter if the nucleus is a pea')]),
  'szFb', 'Схема условная, без масштаба. Отношение диаметров атома и ядра принято равным 10⁵ — порядок величины.',
  'A schematic drawing, not to scale. The ratio of the atom’s to the nucleus’s diameter is taken as 10⁵ — an order of magnitude.')
s2 = section('size', 'Модель Резерфорда: атом почти пуст', 'Rutherford’s model: the atom is almost empty',
 bd('<p>В опытах Резерфорда (1909–1911) альфа-частицы пролетали сквозь тонкую золотую фольгу почти без отклонения, но изредка отскакивали назад. Вывод: весь положительный заряд и почти вся масса сосредоточены в крошечном <strong>ядре</strong>, а электроны движутся вокруг на огромных, по сравнению с ядром, расстояниях. Радиус первой орбиты водорода по Бору <em>0,0529 нм</em>, а размер ядра около <em>10⁻¹⁵ м</em> — меньше в сотни тысяч раз.</p>',
    '<p>In Rutherford’s experiments (1909–1911) alpha particles passed through thin gold foil almost undeflected but rarely bounced straight back. The conclusion: all the positive charge and almost all the mass are concentrated in a tiny <strong>nucleus</strong> while electrons move around at distances huge compared with the nucleus. The radius of the first Bohr orbit of hydrogen is <em>0.0529 nm</em> and the nucleus is about <em>10⁻¹⁵ m</em> — hundreds of thousands of times smaller.</p>')
 + formula('r_n = 0,0529 · n² нм', 'радиус орбиты растёт как квадрат номера уровня', 'the orbit radius grows as the square of the level number'),
 lab2)

lab3 = model(3, 'СПЕКТРЫ ГАЗОВ', 'SPECTRA OF GASES', 'spSvg', '0 0 600 250',
  select('sg', 'Газ', 'Gas') + slider('sb', 'Нечёткость прибора', 'Blur of the instrument', 0, 12, 0.5, 1),
  stats([('sN', 'Число линий в выбранной области', 'Number of lines in the chosen range'), ('sM', 'Самая яркая (условно)', 'The brightest (assumed)')]),
  'spFb', 'Схема условная: длины волн основных линий взяты из справочника; яркость линий условная.',
  'A schematic drawing: the wavelengths of the main lines come from a reference; the brightness of the lines is assumed.')
s3 = section('spectra', 'Спектр — «отпечаток пальцев» атома', 'A spectrum is an atom’s “fingerprint”',
 bd('<p>Каждый элемент излучает свет только на своих длинах волн — у каждого свой набор уровней. Разложив свет призмой, получают <strong>линейчатый спектр</strong>. По нему узнают состав звёзд, пламени и лампы: натрий даёт жёлтую линию 589 нм (улицы, освещённые натриевыми лампами, жёлтые), водород — красную 656 нм и голубую 486 нм, гелий — набор линий от синей до красной.</p>',
    '<p>Each element emits light only at its own wavelengths — each has its own set of levels. Splitting light with a prism gives a <strong>line spectrum</strong>. It reveals the composition of stars, a flame or a lamp: sodium gives a yellow line at 589 nm (streets lit by sodium lamps are yellow), hydrogen — red 656 nm and blue-green 486 nm, helium — a set of lines from blue to red.</p>')
 + formula('ΔE = hf', 'каждая линия — переход между двумя уровнями', 'each line is a transition between two levels'),
 lab3)

tasks = [
 task(1, 'Энергия уровней', 'Level energies', 'Найдите энергию атома водорода на уровнях n = 1, 2, 3 по формуле Бора.', 'Find the energy of a hydrogen atom at levels n = 1, 2, 3 by the Bohr formula.',
  'E_n = −13,6 / n²', 'E_n = −13.6 / n²', 'n = 1: −13,6 эВ.<br>n = 2: −13,6 / 4 = −3,4 эВ.<br>n = 3: −13,6 / 9 ≈ −1,51 эВ.', 'n = 1: −13.6 eV.<br>n = 2: −13.6 / 4 = −3.4 eV.<br>n = 3: −13.6 / 9 ≈ −1.51 eV.', '−13,6; −3,4; −1,51 эВ.', '−13.6; −3.4; −1.51 eV.', True),
 task(2, 'Красная линия водорода', 'The red line of hydrogen', 'Найдите длину волны фотона при переходе n = 3 → 2.', 'Find the wavelength of the photon in the transition n = 3 → 2.',
  'E₃ = −1,51 эВ, E₂ = −3,4 эВ', 'E₃ = −1.51 eV, E₂ = −3.4 eV', 'ΔE = −1,51 − (−3,4) = 1,89 эВ.<br>λ = 1240 / 1,89 ≈ 656 нм.', 'ΔE = −1.51 − (−3.4) = 1.89 eV.<br>λ = 1240 / 1.89 ≈ 656 nm.', '656 нм — красная линия.', '656 nm — the red line.'),
 task(3, 'Ионизация', 'Ionisation', 'Какая энергия нужна, чтобы оторвать электрон от атома водорода в основном состоянии, и какова наибольшая длина волны фотона, способного это сделать?', 'What energy is needed to tear the electron from a hydrogen atom in the ground state and what is the longest wavelength of a photon that can do it?',
  'E₁ = −13,6 эВ', 'E₁ = −13.6 eV', 'Нужно 13,6 эВ.<br>λ = 1240 / 13,6 ≈ 91 нм.', '13.6 eV is needed.<br>λ = 1240 / 13.6 ≈ 91 nm.', '13,6 эВ; 91 нм — глубокий ультрафиолет.', '13.6 eV; 91 nm — deep ultraviolet.'),
 task(4, 'Радиус третьей орбиты', 'The radius of the third orbit', 'Найдите радиус орбиты водорода при n = 3.', 'Find the radius of the hydrogen orbit at n = 3.',
  'r_n = 0,0529·n² нм', 'r_n = 0.0529·n² nm', 'r₃ = 0,0529 · 9 ≈ 0,476 нм.', 'r₃ = 0.0529 · 9 ≈ 0.476 nm.', '≈ 0,48 нм — в 9 раз больше первой.', '≈ 0.48 nm — 9 times the first.'),
 task(5, 'Ядро — горошина', 'The nucleus as a pea', 'Если бы ядро атома было горошиной диаметром 5 мм, каков был бы диаметр атома (отношение 10⁵)?', 'If the nucleus of an atom were a pea 5 mm across what would the atom’s diameter be (ratio 10⁵)?',
  'D / d ≈ 10⁵', 'D / d ≈ 10⁵', 'D = 5 мм · 10⁵ = 5·10⁵ мм = 500 м.', 'D = 5 mm · 10⁵ = 5·10⁵ mm = 500 m.', 'около 500 м — пять футбольных полей.', 'about 500 m — five football pitches.'),
 task(6, 'Жёлтая линия натрия', 'The yellow line of sodium', 'Натриевая лампа излучает линию 589 нм. Найдите энергию фотона.', 'A sodium lamp emits a line at 589 nm. Find the photon energy.',
  'λ = 589 нм', 'λ = 589 nm', 'E = 1240 / 589 ≈ 2,11 эВ.', 'E = 1240 / 589 ≈ 2.11 eV.', '≈ 2,11 эВ.', '≈ 2.11 eV.'),
]

quiz = [
 qz('Что означает «уровень энергии» атома?', 'Допустимое значение энергии электрона', 'Высоту над землёй', 'Температуру атома', 'Энергия электрона в атоме принимает только определённые значения.',
    'What does an “energy level” of an atom mean?', 'An allowed value of the electron’s energy', 'A height above the ground', 'The temperature of the atom', 'The electron energy in an atom takes only certain values.'),
 qz('Когда атом излучает фотон?', 'При переходе электрона на нижний уровень', 'При переходе на верхний уровень', 'Никогда', 'Энергия фотона равна разности уровней.',
    'When does an atom emit a photon?', 'When the electron drops to a lower level', 'When it rises to a higher level', 'Never', 'The photon energy equals the difference of levels.'),
 qz('Чему равна энергия основного состояния водорода?', '−13,6 эВ', '+13,6 эВ', '0', 'Знак минус — электрон связан с ядром.',
    'What is the energy of the hydrogen ground state?', '−13.6 eV', '+13.6 eV', '0', 'The minus sign means the electron is bound.'),
 qz('Что показал опыт Резерфорда?', 'Атом имеет крошечное плотное ядро', 'Атом — сплошной шар', 'Электрон неделим', 'Большинство частиц пролетало насквозь.',
    'What did Rutherford’s experiment show?', 'The atom has a tiny dense nucleus', 'The atom is a solid ball', 'The electron is indivisible', 'Most particles passed straight through.'),
 qz('Во сколько раз атом примерно больше ядра?', 'Примерно в 10⁵ раз', 'Примерно в 10 раз', 'Они равны', 'Атом ~10⁻¹⁰ м, ядро ~10⁻¹⁵ м.',
    'About how many times is an atom larger than its nucleus?', 'About 10⁵ times', 'About 10 times', 'They are equal', 'Atom ~10⁻¹⁰ m, nucleus ~10⁻¹⁵ m.'),
 qz('Как растёт радиус орбиты водорода с номером уровня n?', 'Как n²', 'Как n', 'Не меняется', 'r_n = 0,0529·n² нм.',
    'How does the hydrogen orbit radius grow with the level number n?', 'As n²', 'As n', 'It does not change', 'r_n = 0.0529·n² nm.'),
 qz('Что такое линейчатый спектр?', 'Набор линий на длинах волн, характерных для элемента', 'Непрерывная радуга', 'Один цвет для всех элементов', 'По линиям узнают состав вещества.',
    'What is a line spectrum?', 'A set of lines at wavelengths characteristic of an element', 'A continuous rainbow', 'One colour for all elements', 'The lines reveal the composition of a substance.'),
 qz('Почему натриевые лампы светят жёлтым?', 'Натрий излучает линию около 589 нм', 'Лампа покрашена', 'Это тепловое излучение', 'Яркая жёлтая линия натрия.',
    'Why do sodium lamps glow yellow?', 'Sodium emits a line near 589 nm', 'The lamp is painted', 'It is thermal radiation', 'The bright yellow line of sodium.'),
]

js = JSL + r'''
const T={ru:{
 lvLabel:"Уровни энергии атома водорода и переход",szLabel:"Атом и ядро: сравнение размеров",spLabel:"Линейчатый спектр газа",
 gases:["Водород","Гелий","Натрий"],none:"перехода вниз нет",lyman:"Лаймана (ультрафиолет)",balmer:"Бальмера (видимый свет)",paschen:"Пашена (инфракрасное)",other:"ближний инфракрасный и дальше",
 lvFb:"Атом излучает фотон, когда электрон переходит на нижний уровень.",szFb:"Атом почти пуст: ядро в сотни тысяч раз меньше.",spFb:"У каждого элемента свои линии."},
 en:{
 lvLabel:"Energy levels of the hydrogen atom and a transition",szLabel:"Atom and nucleus: comparing sizes",spLabel:"A line spectrum of a gas",
 gases:["Hydrogen","Helium","Sodium"],none:"no downward transition",lyman:"Lyman (ultraviolet)",balmer:"Balmer (visible light)",paschen:"Paschen (infrared)",other:"near infrared and beyond",
 lvFb:"The atom emits a photon when the electron drops to a lower level.",szFb:"The atom is almost empty: the nucleus is hundreds of thousands of times smaller.",spFb:"Each element has its own lines."}};
const GAS=[[410,434,486,656],[447,502,588,668],[589,590]];
function drawLv(){const t=tt(),n=+$("an").value,m=+$("am").value,ok=n>m;
 const Y=e=>30+ (-e/13.6)*180*0+ (1-Math.pow(1,0))*0; const yy=k=>210-(1-1/(k*k))*180;
 let g='';for(let k=1;k<=7;k++){const y=yy(k);g+='<line x1="120" y1="'+y+'" x2="360" y2="'+y+'" stroke="#18181a" stroke-width="2"/>'+(k<=4?svgText(110,y+4,"n="+k,"#66666b","end",11)+svgText(370,y+4,fmt(-13.6/(k*k),2)+" "+U("эВ","eV"),"#66666b","start",11):"")}
 let dE=0,l=0,ser="—";
 if(ok){dE=13.6*(1/(m*m)-1/(n*n));l=1240/dE;g+=arrow(240,yy(n),240,yy(m)+4,hue(l)==="#7a1f1f"?"#7a1f1f":hue(l),4);ser=m===1?t.lyman:m===2?t.balmer:m===3?t.paschen:t.other;
  g+='<path d="M250 '+((yy(n)+yy(m))/2)+' q 15 -12 30 0 t 30 0 t 30 0" fill="none" stroke="'+hue(l)+'" stroke-width="3"/>'}
 else g+=svgText(450,125,t.none,"#b6533f","start",14);
 $("lvSvg").innerHTML=g;$("anOut").textContent=n;$("amOut").textContent=m;
 $("aE").textContent=ok?fmt(dE,2)+" "+U("эВ","eV"):"—";$("aL").textContent=ok?fmt(l,0)+" "+U("нм","nm"):"—";$("aS").textContent=ok?ser:"—";$("lvFb").textContent=t.lvFb}
["an","am"].forEach(id=>$(id).addEventListener("input",drawLv));
function drawSz(){const t=tt(),n=+$("zn").value,d=+$("zp").value,r=0.0529*n*n,D=d*1e5/1000;
 const R=20+n*n*3.2;let g='<circle cx="300" cy="125" r="'+R+'" fill="none" stroke="#c9c2b0" stroke-dasharray="4 4" stroke-width="2"/><circle cx="300" cy="125" r="3" fill="#b6533f"/><circle cx="'+(300+R)+'" cy="125" r="5" fill="#3f5f8f"/>'+svgText(300,235,U("ядро — точка в центре","the nucleus is the dot in the centre"),"#66666b","middle",12);
 $("szSvg").innerHTML=g;$("znOut").textContent=n;$("zpOut").textContent=d+" "+U("мм","mm");
 $("zR").textContent=fmt(r,3)+" "+U("нм","nm");$("zD").textContent=D>=1000?fmt(D/1000,2)+" "+U("км","km"):fmt(D,0)+" "+U("м","m");$("szFb").textContent=t.szFb}
["zn","zp"].forEach(id=>$(id).addEventListener("input",drawSz));
function drawSp(){const t=tt(),k=+$("sg").value,b=+$("sb").value,L=GAS[k];
 let g='<rect x="30" y="80" width="540" height="90" fill="#18181a"/>';const X=l=>30+(l-380)/370*540;
 L.forEach((l,i)=>{const w=Math.max(2,b*2);g+='<rect x="'+(X(l)-w/2)+'" y="80" width="'+w+'" height="90" fill="'+hue(l)+'" opacity="'+(1/(1+b/6))+'"/>'+(b<3?svgText(X(l),70,String(l),"#66666b","middle",10):"")});
 g+=svgText(30,195,"380","#66666b","start",10)+svgText(570,195,"750 "+U("нм","nm"),"#66666b","end",10);
 $("spSvg").innerHTML=g;$("sbOut").textContent=fmt(b,1)+" "+U("нм","nm");
 const merged=k===2&&b>=1.5;$("sN").textContent=merged?"1 ("+U("слились","merged")+")":String(L.length);$("sM").textContent=(k===0?656:k===1?588:589)+" "+U("нм","nm");$("spFb").textContent=t.spFb}
["sg","sb"].forEach(id=>$(id).addEventListener("input",drawSp));
const LAB={ru:{lvSvg:T.ru.lvLabel,szSvg:T.ru.szLabel,spSvg:T.ru.spLabel},en:{lvSvg:T.en.lvLabel,szSvg:T.en.szLabel,spSvg:T.en.spLabel}};
function drawAll(){fillSel("sg",T[lang].gases,0);drawLv();drawSz();drawSp()}
'''

c = dict(n='39', slug='39-atom.html', block='VII', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Атом', 'The atom'),
 desc='Глава 39 Атласа физики: модель Резерфорда, уровни энергии атома водорода, переходы и спектры, размеры атома и ядра.',
 lead=('Атом почти пуст, а электрон может иметь только определённую энергию. Уровни, спектры и размеры атома.',
       'The atom is almost empty and the electron can have only certain energies. Levels, spectra and the size of the atom.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('levels', 'Уровни', 'Levels'), ('size', 'Размеры', 'Sizes'), ('spectra', 'Спектры', 'Spectra'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Вечером на улице натриевые лампы светят ярко-жёлтым светом. Если пропустить этот свет через призму, радуги не получится — только две очень близкие жёлтые полоски. Лампа с водородом даст совсем другие полоски — красную, голубую, фиолетовые. Раскалённое тело, например спираль лампочки, даёт сплошную радугу.</p><p>Почему атомы излучают свет только на строго определённых длинах волн?</p>',
         '<p>In the evening sodium street lamps glow bright yellow. If this light is passed through a prism there is no rainbow — just two very close yellow stripes. A hydrogen lamp gives quite different stripes — red, blue-green and violet. A glowing solid, such as a bulb filament, gives a continuous rainbow.</p><p>Why do atoms emit light only at strictly definite wavelengths?</p>'),
 hint=stdhint('Спектры и уровни энергии', 'Spectra and energy levels'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: энергия электрона «квантована»', 'The answer: the electron’s energy is “quantised”'),
 answer=('<p>Электрон в атоме может находиться только на определённых уровнях энергии. При переходе вниз атом отдаёт ровно разность энергий одним фотоном, а энергия фотона определяет длину волны. Раз уровней немного и они у каждого элемента свои, то и линий у каждого элемента немного и они свои, как отпечаток пальца.</p><p>Раскалённое твёрдое тело излучает по-другому: в нём атомы сильно взаимодействуют и уровни «размываются» в сплошную полосу — потому его спектр непрерывен.</p>',
         '<p>An electron in an atom can occupy only certain energy levels. In a downward transition the atom gives away exactly the energy difference as one photon and the photon energy fixes the wavelength. Since the levels are few and different for each element, so are the lines — like a fingerprint.</p><p>A hot solid radiates differently: its atoms interact strongly and the levels smear into a continuous band — so its spectrum is continuous.</p>'),
 sources=[
  ('Модель Бора, уровни водорода, спектры —', 'The Bohr model, hydrogen levels, spectra —', LINK('https://openstax.org/books/university-physics-volume-3/pages/7-3-the-bohr-model-of-the-hydrogen-atom', 'OpenStax University Physics, Vol. 3, § 7.3') + ', ' + LINK('https://en.wikipedia.org/wiki/Bohr_model', 'Wikipedia: Bohr model')),
  ('Опыт Резерфорда —', 'Rutherford’s experiment —', LINK('https://en.wikipedia.org/wiki/Geiger%E2%80%93Marsden_experiment', 'Wikipedia: Geiger–Marsden experiment')),
  ('Спектральные линии водорода, гелия, натрия —', 'Spectral lines of hydrogen, helium, sodium —', LINK('https://physics.nist.gov/PhysRefData/ASD/lines_form.html', 'NIST Atomic Spectra Database'))],
 note=stdnote('Модель Бора точна только для водорода; яркость линий и отношение размеров атома и ядра (10⁵) — условные, порядок величины.', 'The Bohr model is exact only for hydrogen; the brightness of lines and the atom-to-nucleus size ratio (10⁵) are assumed, an order of magnitude.'),
 prev=('38-photons-photoelectric.html', 'Глава 38 · Фотоны и фотоэффект', 'Chapter 38 · Photons and the photoelectric effect'),
 next=('40-radioactivity.html', 'Глава 40 · Ядро и радиоактивность', 'Chapter 40 · The nucleus and radioactivity'),
 js=js)
build(c)
