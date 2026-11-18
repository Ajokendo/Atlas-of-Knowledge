# -*- coding: utf-8 -*-
from h5 import *
from JSLIB import JSL

lab1 = model(1, 'МАССА И ЭНЕРГИЯ: E = mc²', 'MASS AND ENERGY: E = mc²', 'mcSvg', '0 0 600 250',
  slider('em', 'Масса, превращённая в энергию', 'Mass turned into energy', 0.001, 10, 0.001, 1),
  stats([('eJ', 'Энергия E = m·c²', 'Energy E = m·c²'), ('eH', 'Столько энергии в киловатт-часах', 'That energy in kilowatt-hours'), ('eT', 'Токтогульская ГЭС при полной мощности 1200 МВт даст её за', 'Toktogul HPP at full power of 1,200 MW would give it in')]),
  'mcFb', 'Схема условная: масса в граммах, c = 3·10⁸ м/с; полностью превратить массу в энергию на практике нельзя — это верхняя граница.',
  'A schematic drawing: the mass in grams, c = 3·10⁸ m/s; turning mass entirely into energy is not possible in practice — this is an upper bound.')
s1 = section('emc2', 'Масса — это тоже энергия', 'Mass is energy too',
 bd('<p>Эйнштейн показал, что масса и энергия связаны: покоящемуся телу массой <em>m</em> соответствует энергия <em>E = m·c²</em>. Множитель <em>c² = 9·10¹⁶ м²/с²</em> огромен, поэтому даже миллиграммы массы — гигантская энергия. В ядерных реакциях часть массы ядер «пропадает» (<strong>дефект массы</strong>) и выходит в виде энергии излучения и движения осколков.</p>',
    '<p>Einstein showed that mass and energy are connected: a body at rest of mass <em>m</em> has energy <em>E = m·c²</em>. The factor <em>c² = 9·10¹⁶ m²/s²</em> is enormous so even milligrams of mass are a gigantic amount of energy. In nuclear reactions part of the mass of the nuclei “disappears” (the <strong>mass defect</strong>) and emerges as radiation and motion of fragments.</p>')
 + formula('E = m · c²', '1 г массы ≈ 9·10¹³ Дж ≈ 25 млн кВт·ч', '1 g of mass ≈ 9·10¹³ J ≈ 25 million kWh'),
 lab1)

lab2 = model(2, 'ЦЕПНАЯ РЕАКЦИЯ', 'THE CHAIN REACTION', 'chSvg', '0 0 600 250',
  slider('ck', 'Коэффициент размножения нейтронов k', 'Neutron multiplication factor k', 0.7, 1.3, 0.01, 1.1) + slider('cn', 'Поколений нейтронов', 'Neutron generations', 0, 20, 1, 10),
  stats([('cN', 'Нейтронов в поколении (если в начале 1) N = kⁿ', 'Neutrons in the generation (1 at the start) N = kⁿ'), ('cS', 'Режим', 'Regime')]),
  'chFb', 'Схема условная: упрощённая модель поколений; в реакторе k поддерживают равным 1 управляющими стержнями.',
  'A schematic drawing: a simplified model of generations; in a reactor k is held at 1 by control rods.')
s2 = section('chain', 'Деление ядер и цепная реакция', 'Fission and the chain reaction',
 bd('<p>Ядро урана-235, поглотив нейтрон, делится на два осколка, выделяя около <em>200 МэВ</em> энергии и 2–3 новых нейтрона. Эти нейтроны могут разделить другие ядра — возникает <strong>цепная реакция</strong>. Важен <strong>коэффициент размножения</strong> <em>k</em> — среднее число нейтронов следующего поколения от одного нейтрона. При <em>k &lt; 1</em> реакция затухает, при <em>k = 1</em> идёт ровно (так работает реактор), при <em>k &gt; 1</em> нарастает лавиной (так устроена атомная бомба, поэтому реакторы строят с множеством систем защиты).</p>',
    '<p>A uranium-235 nucleus after absorbing a neutron splits into two fragments releasing about <em>200 MeV</em> of energy and 2–3 new neutrons. These neutrons can split other nuclei — a <strong>chain reaction</strong> arises. The <strong>multiplication factor</strong> <em>k</em> is the average number of neutrons of the next generation from one neutron. If <em>k &lt; 1</em> the reaction dies out, at <em>k = 1</em> it proceeds steadily (this is how a reactor works), at <em>k &gt; 1</em> it grows like an avalanche (this is how an atomic bomb works, so reactors are built with many protection systems).</p>')
 + formula('N = kⁿ', 'k = 1,1 даёт рост в 2,6 раза за 10 поколений, k = 0,9 — спад до 35%', 'k = 1.1 gives growth of 2.6 times in 10 generations, k = 0.9 — a fall to 35%'),
 lab2)

lab3 = model(3, 'СКОЛЬКО ТОПЛИВА НУЖНО СТАНЦИИ', 'HOW MUCH FUEL A PLANT NEEDS', 'fuSvg', '0 0 600 250',
  slider('fp', 'Электрическая мощность станции', 'Electric power of the plant', 50, 1200, 10, 330) + slider('fe', 'КПД станции', 'Efficiency of the plant', 20, 45, 1, 29),
  stats([('fT', 'Тепловая мощность реактора', 'Thermal power of the reactor'), ('fU', 'Уран-235 в сутки при полном делении', 'Uranium-235 per day at complete fission'), ('fC', 'Угля в сутки на ту же энергию', 'Coal per day for the same energy')]),
  'fuFb', 'Схема условная: 200 МэВ на одно деление, уголь 29 МДж/кг; реальный расход урана больше, так как делится лишь часть ядер топлива.',
  'A schematic drawing: 200 MeV per fission, coal 29 MJ/kg; real uranium consumption is larger since only part of the fuel nuclei fission.')
s3 = section('plant', 'Атомная станция и топливо', 'A nuclear plant and its fuel',
 bd('<p>В реакторе тепло от деления превращается в пар, пар вращает турбину (глава 12) — как на тепловых станциях, но топливо другое. Энергия килограмма урана-235 при полном делении около <em>8,2·10¹³ Дж</em> — в миллионы раз больше, чем у килограмма угля.</p><p>В Кыргызстане атомных станций нет. Россия предлагала построить малую станцию на реакторах РИТМ-200Н (мощность модуля 55 МВт электрических при 190 МВт тепловых); называлась и общая мощность около 330 МВт. Окончательного решения нет, вопрос обсуждают и допускают вынести на референдум — выбор за обществом, а физика помогает оценить масштабы.</p>',
    '<p>In a reactor the heat from fission turns water into steam and the steam spins a turbine (chapter 12) — as at thermal plants, but the fuel is different. The energy of a kilogram of uranium-235 at complete fission is about <em>8.2·10¹³ J</em> — millions of times more than a kilogram of coal.</p><p>Kyrgyzstan has no nuclear power plants. Russia has offered to build a small plant with RITM-200N reactors (a module of 55 MW electric at 190 MW thermal); a total of about 330 MW has been mentioned. No final decision has been taken and a referendum is discussed — the choice belongs to society while physics helps judge the scale.</p>')
 + formula('P_тепл = P_эл / η,   m = P_тепл · t / q', 'q = 8,2·10¹³ Дж/кг для урана-235; для угля ≈ 2,9·10⁷ Дж/кг', 'q = 8.2·10¹³ J/kg for uranium-235; for coal ≈ 2.9·10⁷ J/kg'),
 lab3)

tasks = [
 task(1, '1 грамм массы', '1 gram of mass', 'Какая энергия соответствует массе 1 г? Выразите в джоулях и киловатт-часах.', 'What energy corresponds to a mass of 1 g? Give it in joules and kilowatt-hours.',
  'm = 10⁻³ кг, c = 3·10⁸ м/с', 'm = 10⁻³ kg, c = 3·10⁸ m/s', 'E = m·c² = 10⁻³ · 9·10¹⁶ = 9·10¹³ Дж.<br>1 кВт·ч = 3,6·10⁶ Дж, значит 9·10¹³ / 3,6·10⁶ = 2,5·10⁷ кВт·ч.', 'E = m·c² = 10⁻³ · 9·10¹⁶ = 9·10¹³ J.<br>1 kWh = 3.6·10⁶ J so 9·10¹³ / 3.6·10⁶ = 2.5·10⁷ kWh.', '9·10¹³ Дж = 25 млн кВт·ч.', '9·10¹³ J = 25 million kWh.', True),
 task(2, 'Энергия килограмма урана', 'Energy of a kilogram of uranium', 'При делении одного ядра выделяется 200 МэВ (3,2·10⁻¹¹ Дж). Сколько энергии даст полное деление 1 кг урана-235? (В 1 кг: 1000/235 · 6,02·10²³ ≈ 2,56·10²⁴ ядер.)', 'One fission releases 200 MeV (3.2·10⁻¹¹ J). How much energy does complete fission of 1 kg of uranium-235 give? (1 kg holds 1000/235 · 6.02·10²³ ≈ 2.56·10²⁴ nuclei.)',
  'N = 2,56·10²⁴', 'N = 2.56·10²⁴', 'E = N · 3,2·10⁻¹¹ = 2,56·10²⁴ · 3,2·10⁻¹¹ ≈ 8,2·10¹³ Дж.', 'E = N · 3.2·10⁻¹¹ = 2.56·10²⁴ · 3.2·10⁻¹¹ ≈ 8.2·10¹³ J.', '≈ 8,2·10¹³ Дж.', '≈ 8.2·10¹³ J.'),
 task(3, 'Уголь для сравнения', 'Coal for comparison', 'Сколько угля (29 МДж/кг) нужно, чтобы получить столько же энергии, сколько даёт 1 кг урана-235?', 'How much coal (29 MJ/kg) is needed to get as much energy as 1 kg of uranium-235 gives?',
  'E = 8,2·10¹³ Дж, q = 2,9·10⁷ Дж/кг', 'E = 8.2·10¹³ J, q = 2.9·10⁷ J/kg', 'm = E / q = 8,2·10¹³ / 2,9·10⁷ ≈ 2,8·10⁶ кг.', 'm = E / q = 8.2·10¹³ / 2.9·10⁷ ≈ 2.8·10⁶ kg.', '≈ 2800 т угля.', '≈ 2,800 tonnes of coal.'),
 task(4, 'Размножение нейтронов', 'Neutron multiplication', 'Сколько нейтронов будет в 10-м поколении при k = 1,1 и при k = 0,9 (в начале 1)?', 'How many neutrons will there be in the 10th generation at k = 1.1 and at k = 0.9 (1 at the start)?',
  'n = 10', 'n = 10', 'k = 1,1: 1,1¹⁰ ≈ 2,59.<br>k = 0,9: 0,9¹⁰ ≈ 0,35.', 'k = 1.1: 1.1¹⁰ ≈ 2.59.<br>k = 0.9: 0.9¹⁰ ≈ 0.35.', '≈ 2,6 раза больше и ≈ 0,35 от начала.', '≈ 2.6 times more and ≈ 0.35 of the start.'),
 task(5, 'Станция 330 МВт', 'A 330 MW plant', 'Электрическая мощность 330 МВт, КПД 29%. Найдите тепловую мощность и расход урана-235 в сутки при полном делении.', 'Electric power 330 MW, efficiency 29%. Find the thermal power and the daily consumption of uranium-235 at complete fission.',
  'P_эл = 330 МВт, η = 0,29', 'P_el = 330 MW, η = 0.29', 'P_тепл = 330 / 0,29 ≈ 1138 МВт.<br>За сутки: 1,138·10⁹ · 86 400 ≈ 9,83·10¹³ Дж.<br>m = 9,83·10¹³ / 8,2·10¹³ ≈ 1,2 кг.', 'P_th = 330 / 0.29 ≈ 1,138 MW.<br>Per day: 1.138·10⁹ · 86,400 ≈ 9.83·10¹³ J.<br>m = 9.83·10¹³ / 8.2·10¹³ ≈ 1.2 kg.', '≈ 1,2 кг урана-235 в сутки (на практике больше).', '≈ 1.2 kg of uranium-235 per day (more in practice).'),
 task(6, 'Дефект массы', 'The mass defect', 'При делении выделяется 200 МэВ. Какая масса «пропадает» (1 а.е.м. = 931,5 МэВ) и какая это доля массы ядра урана-235 (235 а.е.м.)?', 'Fission releases 200 MeV. What mass “disappears” (1 u = 931.5 MeV) and what share is that of the mass of a uranium-235 nucleus (235 u)?',
  '200 МэВ, 931,5 МэВ/а.е.м.', '200 MeV, 931.5 MeV/u', 'Δm = 200 / 931,5 ≈ 0,215 а.е.м.<br>Доля: 0,215 / 235 ≈ 0,0009 = 0,09%.', 'Δm = 200 / 931.5 ≈ 0.215 u.<br>Share: 0.215 / 235 ≈ 0.0009 = 0.09%.', '≈ 0,215 а.е.м., около 0,09% массы ядра.', '≈ 0.215 u, about 0.09% of the nuclear mass.'),
]

quiz = [
 qz('О чём говорит формула E = mc²?', 'Масса тела соответствует энергии', 'Скорость пропорциональна массе', 'Энергия не сохраняется', 'c² очень велико, поэтому энергия огромна.',
    'What does the formula E = mc² say?', 'The mass of a body corresponds to energy', 'The speed is proportional to the mass', 'Energy is not conserved', 'c² is very large so the energy is huge.'),
 qz('Что происходит при делении ядра урана-235?', 'Оно делится на осколки, выделяя энергию и нейтроны', 'Оно становится устойчивым', 'Оно поглощает энергию', 'Выделяется около 200 МэВ.',
    'What happens in the fission of a uranium-235 nucleus?', 'It splits into fragments releasing energy and neutrons', 'It becomes stable', 'It absorbs energy', 'About 200 MeV is released.'),
 qz('Что означает k = 1 в реакторе?', 'Реакция идёт ровно', 'Реакция затухает', 'Реакция нарастает лавиной', 'В среднем один нейтрон вызывает одно новое деление.',
    'What does k = 1 mean in a reactor?', 'The reaction proceeds steadily', 'The reaction dies out', 'The reaction grows like an avalanche', 'On average one neutron causes one new fission.'),
 qz('Зачем в реакторе управляющие стержни?', 'Поглощают нейтроны и держат k около 1', 'Нагревают воду', 'Вырабатывают ток', 'Они регулируют число нейтронов.',
    'What are control rods for in a reactor?', 'They absorb neutrons and hold k near 1', 'They heat the water', 'They produce current', 'They regulate the number of neutrons.'),
 qz('Во сколько раз энергоёмкость урана-235 больше угля (по массе)?', 'В миллионы раз', 'В 2 раза', 'Они равны', '8,2·10¹³ против 2,9·10⁷ Дж/кг.',
    'How many times is the energy content of uranium-235 greater than coal (by mass)?', 'Millions of times', '2 times', 'They are equal', '8.2·10¹³ against 2.9·10⁷ J/kg.'),
 qz('Как АЭС превращает тепло в электричество?', 'Пар вращает турбину и генератор', 'Тепло прямо превращается в ток', 'Энергию даёт вода реки', 'Как и на тепловой станции.',
    'How does a nuclear plant turn heat into electricity?', 'Steam spins a turbine and a generator', 'Heat turns directly into current', 'The river water gives the energy', 'As at a thermal plant.'),
 qz('Какая часть массы ядра урана «пропадает» при делении?', 'Около 0,09%', 'Около 50%', 'Вся масса', '0,215 а.е.м. из 235.',
    'What share of the uranium nucleus mass “disappears” in fission?', 'About 0.09%', 'About 50%', 'All of it', '0.215 u out of 235.'),
 qz('Что верно о работающих в Кыргызстане атомных станциях?', 'Их пока нет, обсуждается проект малой станции', 'Их несколько', 'Одна на Иссык-Куле', 'Решение пока не принято.',
    'What is true of nuclear plants operating in Kyrgyzstan?', 'There are none yet, a small plant project is under discussion', 'There are several', 'One on Issyk-Kul', 'No decision has been taken yet.'),
]

js = JSL + r'''
const T={ru:{
 mcLabel:"Малая масса — большая энергия",chLabel:"Поколения нейтронов",fuLabel:"Топливо: уран против угля",
 sub:"затухает (k < 1)",crit:"ровная работа (k = 1)",sup:"лавина (k > 1)",
 mcFb:"Масса в 1 г эквивалентна почти суткам работы Токтогульской ГЭС на полной мощности.",chFb:"k решает: затухание, ровная работа или лавина.",fuFb:"Килограмм урана заменяет тысячи тонн угля."},
 en:{
 mcLabel:"A small mass — a large energy",chLabel:"Neutron generations",fuLabel:"Fuel: uranium against coal",
 sub:"dying out (k < 1)",crit:"steady (k = 1)",sup:"an avalanche (k > 1)",
 mcFb:"A mass of 1 g is equivalent to almost a day of the Toktogul plant at full power.",chFb:"k decides: dying out, steady running or an avalanche.",fuFb:"A kilogram of uranium replaces thousands of tonnes of coal."}};
function dur(s){if(s<120)return fmt(s,0)+" "+U("с","s");if(s<7200)return fmt(s/60,0)+" "+U("мин","min");if(s<172800)return fmt(s/3600,1)+" "+U("ч","h");return fmt(s/86400,1)+" "+U("сут","d")}
function drawMc(){const t=tt(),m=+$("em").value/1000,E=m*9e16,kwh=E/3.6e6,sec=E/1.2e9;
 let g='<rect x="60" y="150" width="'+Math.max(3,Math.min(80,m*1000*8))+'" height="60" fill="#b87333" stroke="#18181a"/>'+arrow(200,180,300,180,"#2f6f5d",4)+'<circle cx="440" cy="170" r="'+Math.min(80,20+Math.log10(E+1)*4)+'" fill="#e8c14a" stroke="#18181a"/>'+svgText(440,60,sci(E,2)+" "+U("Дж","J"),"#18181a","middle",18)+svgText(130,140,fmt(m*1000,3)+" "+U("г","g"),"#66666b","middle",12);
 $("mcSvg").innerHTML=g;$("emOut").textContent=fmt(m*1000,3)+" "+U("г","g");
 $("eJ").textContent=sci(E,2)+" "+U("Дж","J");$("eH").textContent=sci(kwh,2)+" "+U("кВт·ч","kWh");$("eT").textContent=dur(sec);$("mcFb").textContent=t.mcFb}
$("em").addEventListener("input",drawMc);
function drawCh(){const t=tt(),k=+$("ck").value,n=+$("cn").value,N=Math.pow(k,n);
 let g='<line x1="50" y1="210" x2="560" y2="210" stroke="#18181a"/>';let p="";const mx=Math.max(1,Math.pow(Math.max(k,1),20));for(let i=0;i<=20;i++){const v=Math.pow(k,i);p+=(i?" L":"M")+(50+i*25.5)+" "+(210-Math.min(1,v/Math.max(mx,1.01))*170)}
 g+='<path d="'+p+'" fill="none" stroke="#3f5f8f" stroke-width="3"/><circle cx="'+(50+n*25.5)+'" cy="'+(210-Math.min(1,N/Math.max(mx,1.01))*170)+'" r="6" fill="#b6533f"/>'+svgText(560,228,U("поколения","generations"),"#66666b","end",11);
 $("chSvg").innerHTML=g;$("ckOut").textContent=fmt(k,2);$("cnOut").textContent=n;
 $("cN").textContent=N>=1000?sci(N,2):fmt(N,2);$("cS").textContent=Math.abs(k-1)<0.005?t.crit:(k<1?t.sub:t.sup);$("chFb").textContent=t.chFb}
["ck","cn"].forEach(id=>$(id).addEventListener("input",drawCh));
function drawFu(){const t=tt(),Pe=+$("fp").value*1e6,eta=+$("fe").value/100,Pt=Pe/eta,Ed=Pt*86400,mu=Ed/8.2e13,mc=Ed/2.9e7;
 let g='<rect x="120" y="'+(210-Math.min(150,10+Math.log10(mu*1000+1)*20))+'" width="90" height="'+Math.min(150,10+Math.log10(mu*1000+1)*20)+'" fill="#3f5f8f" stroke="#18181a"/><rect x="330" y="60" width="90" height="150" fill="#5a5a60" stroke="#18181a"/>'+svgText(165,230,U("уран","uranium"),"#18181a","middle",12)+svgText(375,230,U("уголь","coal"),"#18181a","middle",12)+svgText(165,50,fmt(mu,2)+" "+U("кг","kg"),"#18181a","middle",13)+svgText(375,50,num(Math.round(mc/1000))+" "+U("т","t"),"#18181a","middle",13);
 $("fuSvg").innerHTML=g;$("fpOut").textContent=Math.round(Pe/1e6)+" "+U("МВт","MW");$("feOut").textContent=Math.round(eta*100)+"%";
 $("fT").textContent=num(Math.round(Pt/1e6))+" "+U("МВт","MW");$("fU").textContent=fmt(mu,2)+" "+U("кг","kg");$("fC").textContent=num(Math.round(mc/1000))+" "+U("т","t");$("fuFb").textContent=t.fuFb}
["fp","fe"].forEach(id=>$(id).addEventListener("input",drawFu));
const LAB={ru:{mcSvg:T.ru.mcLabel,chSvg:T.ru.chLabel,fuSvg:T.ru.fuLabel},en:{mcSvg:T.en.mcLabel,chSvg:T.en.chLabel,fuSvg:T.en.fuLabel}};
function drawAll(){drawMc();drawCh();drawFu()}
'''

c = dict(n='41', slug='41-nuclear-energy.html', block='VII', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Ядерная энергия', 'Nuclear energy'),
 desc='Глава 41 Атласа физики: E = mc², деление ядер, цепная реакция и коэффициент размножения, расход топлива АЭС, обсуждаемая малая АЭС в Кыргызстане.',
 lead=('Масса — это энергия. Как делится ядро, что такое цепная реакция и сколько топлива нужно станции.',
       'Mass is energy. How a nucleus splits, what a chain reaction is and how much fuel a plant needs.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('emc2', 'E = mc²', 'E = mc²'), ('chain', 'Цепная реакция', 'Chain reaction'), ('plant', 'АЭС и топливо', 'The plant and fuel'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Токтогульская ГЭС — крупнейшая в Кыргызстане, её мощность около 1200 МВт. Чтобы получить столько же энергии от угля, нужны поезда угля каждый день. А килограмма урана хватает станции мощностью в сотни мегаватт примерно на сутки.</p><p>Откуда в одном килограмме вещества берётся энергия тысяч тонн угля?</p>',
         '<p>The Toktogul hydro plant is the largest in Kyrgyzstan, with a capacity of about 1,200 MW. To get as much energy from coal, trainloads of coal are needed every day. But a kilogram of uranium is enough for a plant of several hundred megawatts for about a day.</p><p>Where does a kilogram of matter get the energy of thousands of tonnes of coal?</p>'),
 hint=stdhint('Ядерная энергия', 'Nuclear energy'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: энергия связи ядер', 'The answer: nuclear binding energy'),
 answer=('<p>Химическое горение перестраивает электронные оболочки атомов и даёт электронвольты на атом. Деление перестраивает ядра и даёт сотни миллионов электронвольт на ядро — в миллионы раз больше. Эта энергия приходит из дефекта массы: осколки в сумме чуть легче исходного ядра (около 0,09%), а по формуле <em>E = mc²</em> такая «потеря» даёт огромную энергию.</p><p>Поэтому килограмм урана при полном делении эквивалентен примерно 2800 т угля (задача 3). Но топливо нужно ещё безопасно хранить, а отходы — сотни и тысячи лет охранять: это цена, которую общество должно учитывать.</p>',
         '<p>Chemical burning rearranges the electron shells of atoms and gives electronvolts per atom. Fission rearranges nuclei and gives hundreds of millions of electronvolts per nucleus — millions of times more. This energy comes from the mass defect: the fragments are together slightly lighter than the original nucleus (about 0.09%) and by <em>E = mc²</em> this “loss” gives a huge energy.</p><p>So a kilogram of uranium at complete fission is equivalent to about 2,800 t of coal (problem 3). But fuel must also be stored safely and waste guarded for hundreds and thousands of years: a cost society must take into account.</p>'),
 sources=[
  ('Энергия связи, дефект массы, деление, цепная реакция —', 'Binding energy, mass defect, fission, chain reaction —', LINK('https://openstax.org/books/university-physics-volume-3/pages/10-4-nuclear-fission', 'OpenStax University Physics, Vol. 3, § 10.4') + ', ' + LINK('https://en.wikipedia.org/wiki/Nuclear_fission', 'Wikipedia: Nuclear fission')),
  ('Рассматриваемая малая АЭС в Кыргызстане (РИТМ-200Н; около 330 МВт; решение не принято) —', 'The small nuclear plant considered in Kyrgyzstan (RITM-200N; about 330 MW; no decision taken) —', LINK('https://world-nuclear-news.org/articles/kyrgyzstan-considering-possible-russian-smr-plant', 'World Nuclear News') + ', ' + LINK('https://erp.alba.az/en/news/206336/kyrgyzstan-eyes-construction-of-a-330-mw-small-nuclear-power-plant-to-offset-energy-deficit', 'ABC.az, 20 Jun 2026') + ', ' + LINK('https://www.akchabar.kg/en/news/kirgizstan-usilivaet-infrastrukturnij-potentsial-sxynhxfprrcyktxu', 'Akchabar, 20 Jun 2026') + ', ' + LINK('https://www.akchabar.kg/en/news/stroitelstvo-aes-v-kirgizstane-reshit-narod-vopros-vinesut-na-referendum-dujjgftkuwhknnxx', 'Akchabar, 4 Apr 2026'))],
 note=stdnote('Расчёт расхода топлива — для полного деления урана-235; в реальности топливо выгорает лишь частично. Теплота сгорания угля 29 МДж/кг принята как типичная.', 'The fuel calculation assumes complete fission of uranium-235; in reality fuel burns up only partly. The calorific value of coal of 29 MJ/kg is taken as typical.'),
 prev=('40-radioactivity.html', 'Глава 40 · Ядро и радиоактивность', 'Chapter 40 · The nucleus and radioactivity'),
 next=('42-solar-system.html', 'Глава 42 · Солнечная система', 'Chapter 42 · The Solar System'),
 js=js)
build(c)
