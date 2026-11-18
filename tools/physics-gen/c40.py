# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'ПЕРИОД ПОЛУРАСПАДА', 'THE HALF-LIFE', 'hlSvg', '0 0 600 250',
  select('hi', 'Изотоп', 'Isotope') + slider('hk', 'Прошло периодов полураспада', 'Half-lives elapsed', 0, 8, 0.5, 3),
  stats([('hT', 'Период полураспада', 'Half-life'), ('hP', 'Прошедшее время', 'Elapsed time'), ('hF', 'Осталось ядер N/N₀ = ½ᵏ', 'Nuclei remaining N/N₀ = ½ᵏ')]),
  'hlFb', 'Схема условная: показано среднее поведение большого числа ядер; периоды полураспада — справочные значения (округлены).',
  'A schematic drawing: the average behaviour of a large number of nuclei is shown; the half-lives are reference values (rounded).')
s1 = section('halflife', 'Распад и период полураспада', 'Decay and half-life',
 bd('<p>Ядро атома состоит из <strong>протонов</strong> и <strong>нейтронов</strong>. Одни ядра устойчивы, другие самопроизвольно распадаются, испуская излучение (альфа- и бета-частицы, гамма-кванты). Предсказать, когда распадётся <em>одно</em> ядро, невозможно, но для большого числа ядер действует точный закон: за равные промежутки времени распадается одна и та же <em>доля</em> ядер. Время, за которое распадается половина, — <strong>период полураспада T</strong>.</p>',
    '<p>The nucleus of an atom consists of <strong>protons</strong> and <strong>neutrons</strong>. Some nuclei are stable, others decay spontaneously emitting radiation (alpha and beta particles, gamma rays). It is impossible to predict when <em>one</em> nucleus will decay but for a large number of nuclei there is an exact law: in equal intervals of time the same <em>fraction</em> of nuclei decays. The time in which half decay is the <strong>half-life T</strong>.</p>')
 + formula('N = N₀ · (1/2)^(t / T)', 'через 1 период остаётся ½, через 2 — ¼, через 3 — ⅛', 'after 1 half-life ½ remains, after 2 — ¼, after 3 — ⅛')
 + bd('<p>Периоды сильно различаются: йод-131 — 8 суток, цезий-137 — 30 лет, углерод-14 — 5730 лет, уран-238 — 4,5 млрд лет.</p>',
      '<p>Half-lives differ enormously: iodine-131 — 8 days, caesium-137 — 30 years, carbon-14 — 5,730 years, uranium-238 — 4.5 billion years.</p>'),
 lab1)

lab2 = model(2, 'РАДИОУГЛЕРОДНЫЙ ВОЗРАСТ', 'RADIOCARBON DATING', 'rcSvg', '0 0 600 250',
  slider('rf', 'Осталось углерода-14 от исходного', 'Carbon-14 remaining of the original', 1, 100, 1, 25),
  stats([('rA', 'Возраст t = T·log₂(N₀/N)', 'Age t = T·log₂(N₀/N)'), ('rK', 'Периодов полураспада', 'Half-lives')]),
  'rcFb', 'Схема условная: период полураспада углерода-14 принят 5730 лет; датировка пригодна примерно до 50 000 лет.',
  'A schematic drawing: the half-life of carbon-14 is taken as 5,730 years; dating is usable up to about 50,000 years.')
s2 = section('carbon', 'Как узнают возраст находки', 'How the age of a find is determined',
 bd('<p>Пока живое существо питается, доля радиоактивного углерода-14 в нём постоянна. После смерти новый углерод не поступает, а старый распадается. Измерив, какая доля осталась, находят возраст: <em>t = T · log₂(N₀/N)</em>. Так датируют остатки дерева, костей и ткани — в том числе находки археологов из курганов и древних стоянок Центральной Азии.</p>',
    '<p>While a living thing feeds, the share of radioactive carbon-14 in it is constant. After death no new carbon arrives while the old decays. Measuring the share that remains gives the age: <em>t = T · log₂(N₀/N)</em>. This is how the remains of wood, bone and cloth are dated — including finds of archaeologists from burial mounds and ancient sites of Central Asia.</p>')
 + formula('t = T · log₂(N₀ / N)', 'осталось ¼ — прошло два периода: 11 460 лет', 'a quarter remains — two half-lives have passed: 11,460 years'),
 lab2)

lab3 = model(3, 'ВРЕМЯ, РАССТОЯНИЕ, ЗАЩИТА', 'TIME, DISTANCE, SHIELDING', 'dsSvg', '0 0 600 250',
  slider('dr', 'Расстояние до источника', 'Distance from the source', 0.5, 10, 0.5, 1) + slider('dt', 'Время рядом', 'Time nearby', 1, 600, 1, 60) + slider('dx', 'Свинцовая защита', 'Lead shielding', 0, 5, 0.1, 0),
  stats([('dD', 'Полученная доза', 'Dose received'), ('dB', 'Сравнение с естественным фоном за сутки', 'Compared with the natural background per day')]),
  'dsFb', 'Схема условная: учебный источник (на расстоянии 1 м даёт 100 мкЗв/ч), слой половинного ослабления свинца 0,65 см — условные значения; естественный фон 2,4 мЗв/год — мировое среднее.',
  'A schematic drawing: a teaching source (100 µSv/h at 1 m), a half-value layer of lead 0.65 cm — assumed values; the natural background 2.4 mSv/yr is the world average.')
s3 = section('safety', 'Защита от излучения', 'Protection from radiation',
 bd('<p>Излучение измеряют в зивертах (Зв); обычно используют микро- и миллизиверты. Человек всегда получает <strong>естественный фон</strong> (космические лучи, породы, радон) — в среднем около 2,4 мЗв в год. Защита строится на трёх вещах: <em>время</em> (меньше времени — меньше доза), <em>расстояние</em> (доза от точечного источника падает как 1/r²) и <em>экран</em> (слой вещества ослабляет излучение, каждый «слой половинного ослабления» вдвое).</p>',
    '<p>Radiation is measured in sieverts (Sv); micro- and millisieverts are commonly used. A person always receives the <strong>natural background</strong> (cosmic rays, rocks, radon) — on average about 2.4 mSv a year. Protection rests on three things: <em>time</em> (less time — less dose), <em>distance</em> (the dose from a point source falls as 1/r²) and a <em>shield</em> (a layer of material attenuates the radiation, each “half-value layer” by half).</p>')
 + formula('D = D₁ · t / r² · (1/2)^(x / x½)', 'вдвое дальше — вчетверо меньше; ещё слой x½ — ещё вдвое меньше', 'twice as far — four times less; one more layer x½ — half again')
 + bd('<p>В Кыргызстане эта тема не абстрактна: в Майлуу-Суу в 1946–1968 годах добывали и перерабатывали урановую руду, а отходы остались в 23 хвостохранилищах и 13 отвалах. Их безопасное хранение и перенос — большая международная работа.</p>',
      '<p>In Kyrgyzstan this topic is not abstract: in Mailuu-Suu uranium ore was mined and processed in 1946–1968 and the waste remained in 23 tailings dumps and 13 waste-rock dumps. Keeping them safe and relocating them is large international work.</p>'),
 lab3)

tasks = [
 task(1, 'Йод-131', 'Iodine-131', 'Период полураспада йода-131 — 8 суток. Какая доля ядер останется через 24 суток?', 'The half-life of iodine-131 is 8 days. What fraction of nuclei remains after 24 days?',
  'T = 8 сут, t = 24 сут', 'T = 8 d, t = 24 d', 'k = t/T = 3 периода.<br>N/N₀ = (1/2)³ = 1/8 = 12,5%.', 'k = t/T = 3 half-lives.<br>N/N₀ = (1/2)³ = 1/8 = 12.5%.', '12,5%.', '12.5%.', True),
 task(2, 'Возраст находки', 'The age of a find', 'В деревянной балке осталась четверть исходного углерода-14. Каков возраст (T = 5730 лет)?', 'A wooden beam retains a quarter of its original carbon-14. What is its age (T = 5,730 years)?',
  'N/N₀ = ¼', 'N/N₀ = ¼', '¼ = (½)², значит k = 2.<br>t = 2 · 5730 = 11 460 лет.', '¼ = (½)², so k = 2.<br>t = 2 · 5,730 = 11,460 years.', '11 460 лет.', '11,460 years.'),
 task(3, 'Цезий-137', 'Caesium-137', 'T = 30,1 года. Какая доля цезия-137 останется через 60,2 года?', 'T = 30.1 years. What fraction of caesium-137 remains after 60.2 years?',
  't = 60,2 года', 't = 60.2 years', 'k = 60,2 / 30,1 = 2.<br>N/N₀ = ¼ = 25%.', 'k = 60.2 / 30.1 = 2.<br>N/N₀ = ¼ = 25%.', '25%.', '25%.'),
 task(4, 'Расстояние', 'Distance', 'На расстоянии 1 м мощность дозы 100 мкЗв/ч. Какова она на расстоянии 2 м и 4 м?', 'At 1 m the dose rate is 100 µSv/h. What is it at 2 m and at 4 m?',
  'D₁ = 100 мкЗв/ч', 'D₁ = 100 µSv/h', 'D ~ 1/r².<br>2 м: 100 / 4 = 25 мкЗв/ч.<br>4 м: 100 / 16 = 6,25 мкЗв/ч.', 'D ~ 1/r².<br>2 m: 100 / 4 = 25 µSv/h.<br>4 m: 100 / 16 = 6.25 µSv/h.', '25 и 6,25 мкЗв/ч.', '25 and 6.25 µSv/h.'),
 task(5, 'Расстояние и экран', 'Distance and a shield', 'Источник из задачи 4 стоит в 4 м, между ним и человеком слой свинца 1,3 см (слой половинного ослабления 0,65 см). Какова мощность дозы?', 'The source of problem 4 is at 4 m with 1.3 cm of lead (half-value layer 0.65 cm) between it and a person. What is the dose rate?',
  'r = 4 м, x = 1,3 см', 'r = 4 m, x = 1.3 cm', 'Без экрана: 6,25 мкЗв/ч.<br>1,3 / 0,65 = 2 слоя, ослабление ½² = ¼.<br>D = 6,25 / 4 ≈ 1,56 мкЗв/ч.', 'Without a shield: 6.25 µSv/h.<br>1.3 / 0.65 = 2 layers, attenuation ½² = ¼.<br>D = 6.25 / 4 ≈ 1.56 µSv/h.', '≈ 1,56 мкЗв/ч.', '≈ 1.56 µSv/h.'),
 task(6, 'Естественный фон', 'The natural background', 'Сколько мкЗв в сутки даёт естественный фон 2,4 мЗв в год?', 'How many µSv per day does the natural background of 2.4 mSv a year give?',
  '2,4 мЗв/год', '2.4 mSv/yr', '2,4 мЗв = 2400 мкЗв.<br>2400 / 365 ≈ 6,6 мкЗв в сутки.', '2.4 mSv = 2,400 µSv.<br>2,400 / 365 ≈ 6.6 µSv per day.', '≈ 6,6 мкЗв в сутки.', '≈ 6.6 µSv per day.'),
]

quiz = [
 qz('Из чего состоит ядро атома?', 'Из протонов и нейтронов', 'Только из электронов', 'Только из протонов', 'Электроны движутся вокруг ядра.',
    'What does the nucleus of an atom consist of?', 'Protons and neutrons', 'Electrons only', 'Protons only', 'The electrons move around the nucleus.'),
 qz('Что такое период полураспада?', 'Время, за которое распадается половина ядер', 'Время полного распада', 'Время жизни одного ядра', 'Для одного ядра момент распада предсказать нельзя.',
    'What is the half-life?', 'The time in which half of the nuclei decay', 'The time of complete decay', 'The lifetime of one nucleus', 'For one nucleus the moment of decay cannot be predicted.'),
 qz('Какая доля ядер останется через 3 периода полураспада?', '1/8', '1/6', '1/3', '(1/2)³ = 1/8.',
    'What fraction of nuclei remains after 3 half-lives?', '1/8', '1/6', '1/3', '(1/2)³ = 1/8.'),
 qz('Углерод-14 в находке: осталась ¼. Сколько прошло периодов?', 'Два', 'Четыре', 'Один', '(1/2)² = 1/4.',
    'Carbon-14 in a find: ¼ remains. How many half-lives have passed?', 'Two', 'Four', 'One', '(1/2)² = 1/4.'),
 qz('Как меняется доза от точечного источника при увеличении расстояния вдвое?', 'Уменьшается в 4 раза', 'Уменьшается в 2 раза', 'Не меняется', 'D ~ 1/r².',
    'How does the dose from a point source change when the distance doubles?', 'It falls 4 times', 'It falls 2 times', 'It does not change', 'D ~ 1/r².'),
 qz('Что НЕ уменьшает дозу?', 'Увеличение времени рядом с источником', 'Увеличение расстояния', 'Экран из свинца', 'Больше времени — больше доза.',
    'What does NOT reduce the dose?', 'Increasing the time near the source', 'Increasing the distance', 'A lead shield', 'More time means a greater dose.'),
 qz('Что такое естественный радиационный фон?', 'Излучение от космических лучей, пород и радона', 'Только излучение АЭС', 'Излучение мобильного телефона', 'Он есть всегда, в среднем около 2,4 мЗв в год.',
    'What is the natural radiation background?', 'Radiation from cosmic rays, rocks and radon', 'Only the radiation from nuclear plants', 'The radiation of a mobile phone', 'It is always present, on average about 2.4 mSv a year.'),
 qz('Почему отходы урана хранят десятилетиями и дольше?', 'У урана-238 очень большой период полураспада', 'Уран распадается за день', 'Он не излучает', 'Распад идёт миллиарды лет.',
    'Why must uranium waste be kept safe for decades and longer?', 'Uranium-238 has a very long half-life', 'Uranium decays in a day', 'It does not radiate', 'Decay takes billions of years.'),
]

js = JSL + r'''
const T={ru:{
 hlLabel:"Доля оставшихся ядер",rcLabel:"Радиоуглеродная шкала возраста",dsLabel:"Источник, человек и экран",
 iso:["Йод-131","Цезий-137","Углерод-14","Уран-238"],
 hlFb:"Каждый период полураспада оставляет половину ядер.",rcFb:"Чем меньше углерода-14, тем древнее находка.",dsFb:"Время, расстояние и экран снижают дозу."},
 en:{
 hlLabel:"The share of nuclei remaining",rcLabel:"The radiocarbon age scale",dsLabel:"A source, a person and a shield",
 iso:["Iodine-131","Caesium-137","Carbon-14","Uranium-238"],
 hlFb:"Each half-life leaves half of the nuclei.",rcFb:"The less carbon-14 the older the find.",dsFb:"Time, distance and a shield reduce the dose."}};
const HL=[8.02/365.25,30.1,5730,4.468e9];
function fmtYears(y){if(y<1/365*2)return fmt(y*365.25*24,1)+" "+U("ч","h");if(y<1)return fmt(y*365.25,1)+" "+U("сут","d");if(y<1e6)return (y<100?fmt(y,1):num(Math.round(y)))+" "+U("лет","yr");return sci(y,2)+" "+U("лет","yr")}
function drawHl(){const t=tt(),i=+$("hi").value,k=+$("hk").value,F=Math.pow(0.5,k),T0=HL[i];
 let g='<line x1="60" y1="210" x2="560" y2="210" stroke="#18181a"/><line x1="60" y1="210" x2="60" y2="30" stroke="#18181a"/>';let p="";for(let x=0;x<=8;x+=0.25){p+=(x?" L":"M")+(60+x/8*500)+" "+(210-Math.pow(0.5,x)*180)}
 g+='<path d="'+p+'" fill="none" stroke="#3f5f8f" stroke-width="3"/><circle cx="'+(60+k/8*500)+'" cy="'+(210-F*180)+'" r="7" fill="#b6533f"/>'+svgText(560,228,U("периодов","half-lives"),"#66666b","end",11)+svgText(66,30,"100%","#66666b","start",11);
 for(let j=1;j<=4;j++)g+=svgText(60+j/8*500,226,String(j),"#66666b","middle",10);
 $("hlSvg").innerHTML=g;$("hkOut").textContent=fmt(k,1);
 $("hT").textContent=fmtYears(T0);$("hP").textContent=fmtYears(T0*k);$("hF").textContent=fmt(F*100,1)+"%";$("hlFb").textContent=t.hlFb}
["hi","hk"].forEach(id=>$(id).addEventListener("input",drawHl));
function drawRc(){const t=tt(),f=+$("rf").value/100,k=Math.log2(1/f),age=5730*k;
 let g='<rect x="60" y="100" width="480" height="40" fill="#e6dfcd" stroke="#18181a"/><rect x="60" y="100" width="'+(480*f)+'" height="40" fill="#3f5f8f"/>'+svgText(300,175,U("осталось ","remaining ")+Math.round(f*100)+"%","#18181a","middle",14)+svgText(300,70,U("возраст ≈ ","age ≈ ")+num(Math.round(age))+" "+U("лет","yr"),"#18181a","middle",16);
 $("rcSvg").innerHTML=g;$("rfOut").textContent=Math.round(f*100)+"%";
 $("rA").textContent=num(Math.round(age))+" "+U("лет","yr");$("rK").textContent=fmt(k,2);$("rcFb").textContent=t.rcFb}
$("rf").addEventListener("input",drawRc);
function drawDs(){const t=tt(),r=+$("dr").value,m=+$("dt").value,x=+$("dx").value,rate=100/(r*r)*Math.pow(0.5,x/0.65),D=rate*m/60,bg=6.6;
 const px=130+Math.min(r,10)*38;let g='<circle cx="80" cy="125" r="18" fill="#b6533f"/>'+svgText(80,160,U("источник","source"),"#66666b","middle",11);
 if(x>0)g+='<rect x="'+(80+(px-80)/2-3)+'" y="90" width="'+(3+x*3)+'" height="70" fill="#5a5a60"/>';
 g+='<circle cx="'+px+'" cy="110" r="9" fill="#b87333"/><line x1="'+px+'" y1="119" x2="'+px+'" y2="150" stroke="#18181a" stroke-width="4"/>'+svgText(px,175,fmt(r,1)+" "+U("м","m"),"#66666b","middle",11);
 $("dsSvg").innerHTML=g;$("drOut").textContent=fmt(r,1)+" "+U("м","m");$("dtOut").textContent=m+" "+U("мин","min");$("dxOut").textContent=fmt(x,1)+" "+U("см","cm");
 $("dD").textContent=fmt(D,2)+" "+U("мкЗв","µSv");$("dB").textContent=fmt(D/bg,2)+"×";$("dsFb").textContent=t.dsFb}
["dr","dt","dx"].forEach(id=>$(id).addEventListener("input",drawDs));
const LAB={ru:{hlSvg:T.ru.hlLabel,rcSvg:T.ru.rcLabel,dsSvg:T.ru.dsLabel},en:{hlSvg:T.en.hlLabel,rcSvg:T.en.rcLabel,dsSvg:T.en.dsLabel}};
function drawAll(){fillSel("hi",T[lang].iso,1);drawHl();drawRc();drawDs()}
'''

c = dict(n='40', slug='40-radioactivity.html', block='VII', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Ядро и радиоактивность', 'The nucleus and radioactivity'),
 desc='Глава 40 Атласа физики: строение ядра, радиоактивный распад, период полураспада, радиоуглеродная датировка, защита временем, расстоянием и экраном, урановые хвосты Майлуу-Суу.',
 lead=('Ядра распадаются по строгому закону, хотя поведение одного ядра непредсказуемо. Период полураспада, датировка находок и защита от излучения.',
       'Nuclei decay by a strict law although one nucleus is unpredictable. The half-life, dating of finds and protection from radiation.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('halflife', 'Полураспад', 'Half-life'), ('carbon', 'Возраст находки', 'Age of a find'), ('safety', 'Защита', 'Protection'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Археологи нашли на древней стоянке обугленное бревно. Никаких надписей и монет рядом нет. И всё же учёные говорят: «Дерево срубили около 11 тысяч лет назад». Откуда они знают, если никто не видел, когда это было?</p><p>Какие «часы» встроены в само дерево?</p>',
         '<p>Archaeologists found a charred log at an ancient camp site. There are no inscriptions or coins nearby. Yet scientists say: “The tree was cut about 11 thousand years ago.” How do they know if nobody saw when it was?</p><p>What “clock” is built into the wood itself?</p>'),
 hint=stdhint('Радиоактивный распад', 'Radioactive decay'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: радиоактивные часы', 'The answer: a radioactive clock'),
 answer=('<p>Пока дерево растёт, в нём поддерживается постоянная доля радиоактивного углерода-14. После того как дерево срублено, новый углерод не поступает, а старый распадается с периодом 5730 лет. Если осталась ¼ исходного количества, то прошло два периода: 2 · 5730 = 11 460 лет (модель 2).</p><p>Распад каждого отдельного ядра случаен, но у огромного числа ядер доля распавшихся подчиняется точному закону — потому такие «часы» надёжны.</p>',
         '<p>While a tree grows a constant share of radioactive carbon-14 is maintained in it. After the tree is cut no new carbon arrives and the old decays with a half-life of 5,730 years. If ¼ of the original amount remains two half-lives have passed: 2 · 5,730 = 11,460 years (model 2).</p><p>The decay of each single nucleus is random but for an enormous number of nuclei the decayed share follows an exact law — that is why such a “clock” is reliable.</p>'),
 sources=[
  ('Радиоактивность, период полураспада, радиоуглеродная датировка —', 'Radioactivity, half-life, radiocarbon dating —', LINK('https://openstax.org/books/university-physics-volume-3/pages/10-3-radioactive-decay', 'OpenStax University Physics, Vol. 3, § 10.3') + ', ' + LINK('https://en.wikipedia.org/wiki/Radiocarbon_dating', 'Wikipedia: Radiocarbon dating')),
  ('Естественный радиационный фон (в среднем около 2,4 мЗв в год) —', 'The natural background radiation (on average about 2.4 mSv a year) —', LINK('https://en.wikipedia.org/wiki/Background_radiation', 'Wikipedia: Background radiation')),
  ('Майлуу-Суу: добыча урана 1946–1968, 23 хвостохранилища и 13 отвалов —', 'Mailuu-Suu: uranium mining 1946–1968, 23 tailings dumps and 13 waste-rock dumps —', LINK('https://www.pureearth.org/project/mailuu-suu-legacy-uranium-dumps-2/', 'Pure Earth') + ', ' + LINK('https://www.bgr.bund.de/EN/Themen/Wasser/Projekte/abgeschlossen/TZ/Kirgisistan/kirgisistan_fb_en.html?nn=1542366', 'BGR') + ', ' + LINK('https://timesca.com/?p=56376', 'The Times of Central Asia, 18 Sep 2026'))],
 note=stdnote('Мощность дозы источника (100 мкЗв/ч на 1 м) и слой половинного ослабления свинца (0,65 см) — условные значения для учебной задачи, не данные о реальных источниках.', 'The dose rate of the source (100 µSv/h at 1 m) and the half-value layer of lead (0.65 cm) are assumed values for a teaching problem, not data on real sources.'),
 prev=('39-atom.html', 'Глава 39 · Атом', 'Chapter 39 · The atom'),
 next=('41-nuclear-energy.html', 'Глава 41 · Ядерная энергия', 'Chapter 41 · Nuclear energy'),
 js=js)
build(c)
