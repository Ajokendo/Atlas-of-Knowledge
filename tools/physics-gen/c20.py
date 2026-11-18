# -*- coding: utf-8 -*-
from gen import *
LINK = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

lab1 = model(1, 'ТОК ЧЕРЕЗ ТЕЛО', 'CURRENT THROUGH THE BODY', 'bdSvg', '0 0 600 250',
  select('bs', 'Кожа', 'Skin') + select('bu', 'Напряжение', 'Voltage'),
  stats([('bI', 'Ток через тело I = U/R', 'Current through the body I = U/R'), ('bZ', 'Что чувствует человек', 'What a person feels')]),
  'bdFb', 'Схема условная: тело между двумя точками касания, сопротивление условное (сухая кожа 100 кОм, влажная 10 кОм, мокрая 1 кОм). Реальные значения сильно различаются.',
  'A schematic drawing: the body between two contact points, the resistance is assumed (dry skin 100 kΩ, damp 10 kΩ, wet 1 kΩ). Real values vary widely.')
s1 = section('body', 'Опасен ток, а не напряжение', 'It is the current that is dangerous, not the voltage',
 bd('<p>Тело человека проводит ток, потому что внутри него солёные жидкости с ионами (глава 19). Ток через тело определяет закон Ома: <em>I = U / R</em>, где <em>R</em> — сопротивление тела между точками касания. Главную часть сопротивления создаёт кожа: сухая — десятки и сотни килоомов, мокрая — около килоома, а повреждённая — ещё меньше.</p><p>Опасность определяет сила тока, текущего через тело, и путь тока (особенно через сердце):</p>',
    '<p>The human body conducts current because inside it there are salty fluids with ions (chapter 19). The current through the body is given by Ohm’s law: <em>I = U / R</em>, where <em>R</em> is the resistance of the body between the touch points. Most of the resistance is made by the skin: dry skin tens or hundreds of kilo-ohms, wet skin about a kilo-ohm, and broken skin still less.</p><p>The danger depends on the current through the body and the path of the current (especially through the heart):</p>')
 + table(['ТОК, мА', 'ДЕЙСТВИЕ (ПРИБЛИЗИТЕЛЬНО)'], ['CURRENT, mA', 'EFFECT (APPROXIMATE)'],
     [['≈ 1', ('порог ощущения', 'threshold of perception')], ['≈ 10–16', ('не отпустить провод — мышцы сводит', 'cannot let go — muscles lock')], ['≈ 30', ('затруднено дыхание', 'breathing impaired')], ['≈ 50–100 и более', ('фибрилляция сердца, смертельная опасность', 'heart fibrillation, mortal danger')]])
 + bd('<p>Эти границы ориентировочные и зависят от человека, пути тока и времени. Поэтому правило одно: любой удар током — повод обратиться за медицинской помощью.</p>',
      '<p>These boundaries are approximate and depend on the person, the path and the time. So there is one rule: any electric shock is a reason to seek medical help.</p>'),
 lab1)

lab2 = model(2, 'УЗО: УСТРОЙСТВО ЗАЩИТНОГО ОТКЛЮЧЕНИЯ', 'THE RCD: RESIDUAL-CURRENT DEVICE', 'rcSvg', '0 0 600 230',
  select('rk', 'УЗО', 'RCD') + slider('rl', 'Ток утечки', 'Leakage current', 0, 100, 1, 10),
  stats([('rS', 'Состояние', 'State'), ('rZ', 'Ток утечки для человека', 'The leakage current for a person')]),
  'rcFb', 'Схема условная: УЗО на 30 мА отключает цепь, когда «ушедший» мимо нагрузки ток превышает 30 мА.', 'A schematic drawing: a 30 mA RCD cuts the circuit when the current “leaking” past the load exceeds 30 mA.')
s2 = section('rcd', 'УЗО и автомат', 'The RCD and the breaker',
 bd('<p>Автомат (глава 18) защищает от перегрузки и короткого замыкания, но он не заметит, что ток в 50 мА идёт через человека: для него это мелочь. Для этого есть <strong>УЗО</strong> (устройство защитного отключения). Оно сравнивает ток, который пришёл в прибор по одному проводу, с током, который вернулся по другому. Если часть тока «ушла» мимо — например, через тело человека, — УЗО быстро отключает цепь. Обычно такие устройства рассчитывают на 30 мА, потому что ниже этого значения ток считают не смертельным.</p>',
    '<p>The breaker (chapter 18) protects against overload and short circuit, but it does not notice 50 mA flowing through a person: that is a trifle for it. For this there is the <strong>RCD</strong> (residual-current device). It compares the current that entered the appliance along one wire with the current that returned along the other. If part of the current “leaked” elsewhere — for example through a person’s body — the RCD cuts the circuit quickly. Such devices are usually rated at 30 mA, because below that value the current is considered not lethal.</p>'),
 lab2)

lab3 = model(3, 'ЗАЗЕМЛЕНИЕ: ДВА ПУТИ ДЛЯ ТОКА', 'EARTHING: TWO PATHS FOR THE CURRENT', 'grSvg', '0 0 600 250',
  slider('gl', 'Ток утечки на корпус', 'Leakage current to the case', 0.1, 10, 0.1, 5) + slider('gr', 'Сопротивление заземления', 'Earthing resistance', 0.1, 100, 0.1, 0.5),
  stats([('gB', 'Ток через человека (1 кОм)', 'Current through a person (1 kΩ)'), ('gE', 'Ток через заземление', 'Current through the earth wire')]),
  'grFb', 'Схема условная: человек (1 кОм) и заземляющий провод включены параллельно, ток делится обратно пропорционально сопротивлениям.', 'A schematic drawing: the person (1 kΩ) and the earth wire are in parallel and the current splits inversely to the resistances.')
s3 = section('earth', 'Заземление и двойная изоляция', 'Earthing and double insulation',
 bd('<p>Если провод под напряжением случайно коснётся металлического корпуса стиральной машины или чайника, на корпусе появляется опасное напряжение. <strong>Заземление</strong> соединяет корпус с землёй проводом очень малого сопротивления. Ток утечки идёт по двум параллельным путям: через заземляющий провод и через человека, если он коснётся корпуса. Параллельно, как мы помним, ток делится обратно пропорционально сопротивлениям (глава 17), так что почти весь ток идёт по заземлению, а во многих случаях срабатывает автомат или УЗО.</p><p>Вилка типа F (европейская, с заземляющими контактами) нужна именно для этого. Многие бытовые приборы имеют <strong>двойную изоляцию</strong>: корпус из пластика, который не может оказаться под напряжением.</p>',
    '<p>If a live wire accidentally touches the metal case of a washing machine or kettle, a dangerous voltage appears on the case. <strong>Earthing</strong> connects the case to the ground with a wire of very small resistance. The leakage current takes two parallel paths: through the earth wire and through a person if they touch the case. In parallel, as we remember, the current splits inversely to the resistances (chapter 17), so almost all of the current goes through the earthing, and in most cases the breaker or RCD trips.</p><p>The type F plug (European, with earthing contacts) is needed exactly for this. Many household appliances have <strong>double insulation</strong>: a plastic case that cannot become live.</p>'),
 lab3)

tasks = [
 task(1, 'Аккумулятор и сухие руки', 'A battery and dry hands', 'Какой ток пройдёт через человека с сухой кожей (100 кОм), если он коснётся контактов автомобильного аккумулятора 12 В?', 'What current passes through a person with dry skin (100 kΩ) touching the terminals of a 12 V car battery?',
  'U = 12 В, R = 100 000 Ом', 'U = 12 V, R = 100,000 Ω', 'I = U / R = 12 / 100 000 = 0,00012 А.', 'I = U / R = 12 / 100,000 = 0.00012 A.',
  '0,12 мА — ниже порога ощущения. Хотя сам аккумулятор может дать сотни ампер.', '0.12 mA — below the threshold of perception, although the battery itself can deliver hundreds of amperes.', True),
 task(2, 'Сеть и мокрые руки', 'Mains and wet hands', 'Какой ток пройдёт через человека с мокрой кожей (1 кОм) при касании провода под напряжением 220 В?', 'What current passes through a person with wet skin (1 kΩ) touching a live wire at 220 V?',
  'U = 220 В, R = 1000 Ом', 'U = 220 V, R = 1,000 Ω', 'I = U / R = 220 / 1000 = 0,22 А = 220 мА.', 'I = U / R = 220 / 1,000 = 0.22 A = 220 mA.',
  '220 мА — это в несколько раз больше порога фибрилляции. Опасность смертельна.', '220 mA — several times the fibrillation threshold. Deadly danger.'),
 task(3, 'Безопасное напряжение', 'Safe voltage', 'При каком напряжении через тело сопротивлением 1 кОм пойдёт ток 30 мА?', 'At what voltage does a current of 30 mA flow through a body of resistance 1 kΩ?',
  'I = 0,03 А, R = 1000 Ом', 'I = 0.03 A, R = 1,000 Ω', 'U = I·R = 0,03 · 1000 = 30 В.', 'U = I·R = 0.03 · 1,000 = 30 V.',
  '30 В. Поэтому в сырых помещениях применяют пониженное напряжение (12–36 В).', '30 V. That is why reduced voltage (12–36 V) is used in damp places.'),
 task(4, 'Сработает ли УЗО', 'Will the RCD trip', 'УЗО рассчитано на 30 мА. Какое из значений тока утечки его отключит: 5 мА, 20 мА, 50 мА?', 'An RCD is rated at 30 mA. Which of the leakage currents will trip it: 5 mA, 20 mA, 50 mA?',
  'I<sub>отк</sub> = 30 мА', 'I<sub>trip</sub> = 30 mA', 'УЗО срабатывает, если ток утечки больше 30 мА.<br>5 мА < 30 мА — не отключит.<br>20 мА < 30 мА — не отключит.<br>50 мА > 30 мА — отключит.', 'The RCD trips if the leakage exceeds 30 mA.<br>5 mA < 30 mA — will not trip.<br>20 mA < 30 mA — will not trip.<br>50 mA > 30 mA — will trip.',
  'Отключит только 50 мА. Ток 20 мА ещё ощутим, но в среднем не смертелен.', 'Only 50 mA will trip it. 20 mA is still felt but on average is not fatal.'),
 task(5, 'Заземление', 'Earthing', 'Из-за пробоя на корпус стиральной машины ушёл ток 5 А. Заземляющий провод имеет сопротивление 0,5 Ом. Какой ток пойдёт через человека (1000 Ом), коснувшегося корпуса?', 'A fault sends 5 A to a washing machine’s case. The earth wire has a resistance of 0.5 Ω. What current goes through a person (1,000 Ω) touching the case?',
  'I = 5 А, R<sub>з</sub> = 0,5 Ом, R<sub>ч</sub> = 1000 Ом', 'I = 5 A, R<sub>e</sub> = 0.5 Ω, R<sub>p</sub> = 1,000 Ω', 'Параллельные ветви делят ток обратно пропорционально сопротивлениям.<br>I<sub>ч</sub> = I · R<sub>з</sub> / (R<sub>з</sub> + R<sub>ч</sub>) = 5 · 0,5 / 1000,5 ≈ 2,5·10⁻³ А.', 'Parallel branches split the current inversely to resistances.<br>I<sub>p</sub> = I · R<sub>e</sub> / (R<sub>e</sub> + R<sub>p</sub>) = 5 · 0.5 / 1,000.5 ≈ 2.5·10⁻³ A.',
  'около 2,5 мА: почти весь ток уходит в заземление, и человек в безопасности.', 'about 2.5 mA: almost all the current goes into the earth and the person is safe.'),
 task(6, 'Тонкий удлинитель', 'A thin extension lead', 'К удлинителю подключён обогреватель 3,5 кВт (220 В). Сопротивление тонкого скрученного провода 1 Ом. Какая мощность выделяется в проводе?', 'A 3.5 kW heater (220 V) is connected to an extension lead. The resistance of the thin coiled wire is 1 Ω. What power is released in the wire?',
  'P = 3500 Вт, U = 220 В, R = 1 Ом', 'P = 3,500 W, U = 220 V, R = 1 Ω', 'I = P / U = 3500 / 220 ≈ 15,9 А.<br>P<sub>пр</sub> = I²·R = 15,9² · 1 ≈ 253 Вт.', 'I = P / U = 3,500 / 220 ≈ 15.9 A.<br>P<sub>w</sub> = I²·R = 15.9² · 1 ≈ 253 W.',
  'около 250 Вт тепла в тонком проводе — как у небольшого утюга. Провод может перегреться и вызвать пожар; для мощных приборов нужен провод подходящего сечения.', 'about 250 W of heat in the thin wire — like a small iron. The wire may overheat and cause a fire; powerful appliances need a wire of suitable cross-section.'),
]

quiz = [
 ('От чего в первую очередь зависит опасность удара током?', [('От силы тока через тело и пути тока', 'Верно.'), ('Только от цвета провода', 'Цвет не влияет.'), ('Только от мощности лампочки в доме', 'Не связано.')],
  'What does the danger of an electric shock depend on first of all?', [('The current through the body and its path', 'Correct.'), ('Only the colour of the wire', 'Colour has no effect.'), ('Only the power of the bulb at home', 'Unrelated.')], 0),
 ('Почему мокрые руки опаснее сухих?', [('У мокрой кожи сопротивление намного меньше', 'Верно: ток I = U/R больше.'), ('Вода обладает зарядом', 'Дело в сопротивлении.'), ('Мокрые руки тяжелее', 'Дело не в массе.')],
  'Why are wet hands more dangerous than dry?', [('Wet skin has a much smaller resistance', 'Correct: the current I = U/R is greater.'), ('Water carries charge', 'It is a matter of resistance.'), ('Wet hands are heavier', 'Mass is not the point.')], 0),
 ('Примерно с какого тока человек не может отпустить провод?', [('С 1 мкА', 'Это слишком мало.'), ('С 10–16 мА', 'Верно.'), ('Со 100 А', 'Намного выше смертельного.')],
  'At roughly what current can a person not let go of a wire?', [('From 1 µA', 'That is far too small.'), ('From 10–16 mA', 'Correct.'), ('From 100 A', 'Far above lethal.')], 1),
 ('Для чего нужно УЗО?', [('Отключает цепь при утечке тока мимо нагрузки, например через человека', 'Верно.'), ('Увеличивает напряжение', 'Оно не меняет напряжение.'), ('Считает электроэнергию', 'Это функция счётчика.')],
  'What is the RCD for?', [('It cuts the circuit when current leaks past the load, for example through a person', 'Correct.'), ('It increases the voltage', 'It does not change the voltage.'), ('It counts the electricity', 'That is the meter’s function.')], 0),
 ('Чем автомат отличается от УЗО?', [('Автомат реагирует на перегрузку и короткое замыкание, УЗО — на утечку тока', 'Верно.'), ('Ничем', 'Они защищают от разного.'), ('Автомат защищает от утечки, УЗО — от перегрузки', 'Всё наоборот.')],
  'How does a breaker differ from an RCD?', [('The breaker reacts to overload and short circuit, the RCD to leakage', 'Correct.'), ('No difference', 'They protect against different things.'), ('The breaker protects from leakage, the RCD from overload', 'It is the other way round.')], 0),
 ('Зачем заземляют корпус стиральной машины?', [('Чтобы ток утечки уходил в землю, а не через человека', 'Верно.'), ('Чтобы машина стирала лучше', 'Не связано.'), ('Чтобы увеличить напряжение', 'Заземление не повышает напряжение.')],
  'Why is a washing machine’s case earthed?', [('So the leakage current goes into the ground and not through a person', 'Correct.'), ('So the machine washes better', 'Unrelated.'), ('To raise the voltage', 'Earthing does not raise the voltage.')], 0),
 ('Что нужно сделать, если человека бьёт током?', [('Сразу взяться за него голыми руками', 'Нельзя: вы сами попадёте под ток.'), ('Сначала отключить напряжение (выключатель, автомат), потом оказывать помощь и вызвать скорую', 'Верно: сначала безопасность.'), ('Облить водой', 'Вода проводит ток и усугубит ситуацию.')],
  'What should be done if a person is being shocked?', [('Grab them with bare hands at once', 'No: you would get shocked yourself.'), ('First cut off the voltage (switch, breaker), then give help and call an ambulance', 'Correct: safety first.'), ('Pour water on them', 'Water conducts and makes it worse.')], 1),
 ('Почему мощные приборы нельзя включать через тонкий удлинитель?', [('Большой ток нагревает тонкий провод по закону Джоуля — Ленца', 'Верно.'), ('Прибор будет светить слабее', 'Дело в нагреве провода.'), ('Напряжение вырастет', 'Напряжение не вырастет.')],
  'Why must powerful appliances not be plugged into a thin extension lead?', [('A large current heats the thin wire by the Joule–Lenz law', 'Correct.'), ('The appliance will shine weaker', 'It is a matter of the wire heating.'), ('The voltage will rise', 'The voltage will not rise.')], 0),
]

js = r'''
const T={ru:{
 bdLabel:"Человек между двумя точками касания",rcLabel:"УЗО и ток, ушедший мимо нагрузки",grLabel:"Человек и заземляющий провод: два пути тока",
 skins:["Сухая (100 кОм)","Влажная (10 кОм)","Мокрая (1 кОм)"],
 vols:["Батарейка АА, 1,5 В","Автомобильный аккумулятор, 12 В","Безопасное напряжение, 36 В","Бытовая розетка, 220 В","Линия 380 В"],
 zones:["не ощущается","ощущается лёгкое покалывание","болезненно, трудно отпустить","опасно: затруднено дыхание","смертельная опасность: возможна фибрилляция"],
 rcs:["Автомата без УЗО","УЗО на 30 мА","УЗО на 10 мА"],
 ok:"цепь работает",tripped:"УЗО отключило",
 bdFb:"Опасность зависит от тока, а ток — от напряжения и сопротивления: I = U/R.",
 rcFb:["Ток утечки мал или УЗО нет: цепь не отключается.","Ток утечки превысил порог: УЗО отключило цепь."],
 grFb:"Чем меньше сопротивление заземления, тем меньшая доля тока пройдёт через человека.",
 pers:["не опасен","ощутим","может быть опасен"]},
 en:{
 bdLabel:"A person between two touch points",rcLabel:"An RCD and the current leaking past the load",grLabel:"A person and an earth wire: two paths for the current",
 skins:["Dry (100 kΩ)","Damp (10 kΩ)","Wet (1 kΩ)"],
 vols:["AA battery, 1.5 V","Car battery, 12 V","Safe voltage, 36 V","Wall socket, 220 V","380 V line"],
 zones:["not felt","a slight tingling is felt","painful, hard to let go","dangerous: breathing impaired","mortal danger: fibrillation possible"],
 rcs:["A breaker without RCD","30 mA RCD","10 mA RCD"],
 ok:"circuit works",tripped:"RCD tripped",
 bdFb:"The danger depends on the current, and the current on voltage and resistance: I = U/R.",
 rcFb:["The leakage is small or there is no RCD: the circuit does not trip.","The leakage exceeded the threshold: the RCD cut the circuit."],
 grFb:"The smaller the earthing resistance, the smaller the share of current through the person.",
 pers:["not dangerous","felt","may be dangerous"]}};
const RS=[1e5,1e4,1e3],VV=[1.5,12,36,220,380],TH=[1e9,30,10];
function zone(mA){return mA<1?0:mA<10?1:mA<30?2:mA<75?3:4}
function drawBd(){const t=tt(),R=RS[+$("bs").value],U=VV[+$("bu").value],I=U/R*1000,z=zone(I);
 const col=["#2f6f5d","#8fb34a","#e0b82f","#d9822b","#b6533f"][z];
 let g='<circle cx="300" cy="55" r="22" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/><rect x="278" y="80" width="44" height="80" rx="8" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/><line x1="278" y1="95" x2="230" y2="150" stroke="#18181a" stroke-width="5"/><line x1="322" y1="95" x2="370" y2="150" stroke="#18181a" stroke-width="5"/>';
 g+='<rect x="180" y="150" width="60" height="26" fill="'+col+'" stroke="#18181a"/><rect x="360" y="150" width="60" height="26" fill="'+col+'" stroke="#18181a"/>';
 g+=svgText(300,215,"I = "+(I<1?fmt(I*1000,1)+" µA":fmt(I,1)+" mA"),col,"middle",18);
 $("bdSvg").innerHTML=g;
 $("bI").textContent=I<1?fmt(I*1000,1)+(lang==="ru"?" мкА":" µA"):fmt(I,1)+(lang==="ru"?" мА":" mA");$("bZ").textContent=t.zones[z];$("bdFb").textContent=t.bdFb}
["bs","bu"].forEach(id=>$(id).addEventListener("input",drawBd));
function drawRc(){const t=tt(),k=+$("rk").value,l=+$("rl").value,tr=l>TH[k];
 const X=v=>60+v/100*480;
 let g='<rect x="60" y="80" width="480" height="30" fill="#e8e4d8" stroke="#18181a"/><rect x="60" y="80" width="'+(X(l)-60)+'" height="30" fill="'+(tr?"#b6533f":"#2f6f5d")+'"/>';
 if(k>0)g+='<line x1="'+X(TH[k])+'" y1="65" x2="'+X(TH[k])+'" y2="125" stroke="#18181a" stroke-width="3"/>'+svgText(X(TH[k]),58,TH[k]+" mA","#18181a","middle",12);
 for(let v=0;v<=100;v+=20)g+=svgText(X(v),140,v,"#66666b","middle",10);
 g+=svgText(60,190,tr?t.tripped:t.ok,tr?"#b6533f":"#2f6f5d","start",20);
 $("rcSvg").innerHTML=g;
 $("rlOut").textContent=l+(lang==="ru"?" мА":" mA");
 $("rS").textContent=tr?t.tripped:t.ok;$("rZ").textContent=t.pers[l<10?0:l<30?1:2];$("rcFb").textContent=t.rcFb[tr?1:0]}
["rk","rl"].forEach(id=>$(id).addEventListener("input",drawRc));
function drawGr(){const t=tt(),I=+$("gl").value,Rg=+$("gr").value,Rb=1000,Ib=I*Rg/(Rg+Rb),Ig=I-Ib;
 let g='<rect x="60" y="40" width="120" height="70" rx="8" fill="#e8e4d8" stroke="#18181a" stroke-width="2"/>'+svgText(120,80,lang==="ru"?"корпус":"case","#18181a","middle",13);
 g+='<line x1="180" y1="65" x2="540" y2="65" stroke="#18181a" stroke-width="2"/><line x1="180" y1="65" x2="260" y2="65" stroke="#18181a"/>';
 g+='<line x1="300" y1="65" x2="300" y2="110" stroke="#18181a" stroke-width="2"/><rect x="284" y="110" width="32" height="40" fill="#e8e4d8" stroke="#18181a"/>'+svgText(300,135,"1k","#18181a","middle",11)+svgText(300,172,fmt(Ib*1000,2)+" mA","#b6533f","middle",12);
 g+='<line x1="460" y1="65" x2="460" y2="110" stroke="#18181a" stroke-width="2"/><rect x="444" y="110" width="32" height="40" fill="#e8e4d8" stroke="#18181a"/>'+svgText(460,135,fmt(Rg,1),"#18181a","middle",10)+svgText(460,172,fmt(Ig,2)+" A","#2f6f5d","middle",12);
 g+='<line x1="300" y1="150" x2="300" y2="195" stroke="#18181a"/><line x1="460" y1="150" x2="460" y2="195" stroke="#18181a"/><line x1="280" y1="195" x2="480" y2="195" stroke="#18181a" stroke-width="3"/>'+svgText(380,220,lang==="ru"?"земля":"ground","#66666b","middle",12);
 $("grSvg").innerHTML=g;
 $("glOut").textContent=fmt(I,1)+" A";$("grOut").textContent=fmt(Rg,1)+(lang==="ru"?" Ом":" Ω");
 $("gB").textContent=Ib<0.01?fmt(Ib*1000,2)+(lang==="ru"?" мА":" mA"):fmt(Ib*1000,1)+(lang==="ru"?" мА":" mA");$("gE").textContent=fmt(Ig,2)+(lang==="ru"?" А":" A");$("grFb").textContent=t.grFb}
["gl","gr"].forEach(id=>$(id).addEventListener("input",drawGr));
const LAB={ru:{bdSvg:T.ru.bdLabel,rcSvg:T.ru.rcLabel,grSvg:T.ru.grLabel},en:{bdSvg:T.en.bdLabel,rcSvg:T.en.rcLabel,grSvg:T.en.grLabel}};
function drawAll(){fillSel("bs",T[lang].skins,2);fillSel("bu",T[lang].vols,3);fillSel("rk",T[lang].rcs,1);drawBd();drawRc();drawGr()}
'''

c = dict(n='20', slug='20-electrical-safety.html', block='III', level_ru='ОСНОВЫ', level_en='BASICS',
 title=('Электробезопасность', 'Electrical safety'),
 desc='Глава 20 Атласа физики: ток через тело, УЗО, заземление, безопасное напряжение, правила электробезопасности.',
 lead=('Автомобильный аккумулятор может дать сотни ампер, а касаться его безопасно. Розетка даёт ток в доли ампера, а смертельно опасна. Как это объясняется и как защититься.',
       'A car battery can deliver hundreds of amperes, yet touching it is safe. A socket gives a fraction of an ampere, yet is deadly. How this is explained and how to protect yourself.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('body', 'Ток и тело', 'Current and the body'), ('rcd', 'УЗО', 'The RCD'), ('earth', 'Заземление', 'Earthing'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Автомобильный аккумулятор способен дать ток в сотни ампер, чтобы провернуть двигатель, но мы без опаски касаемся его контактов. От розетки же достаточно тока в десятую долю ампера, чтобы человек погиб. Получается, что «сильный» ток безопасен, а «слабый» опасен.</p><p>Как это возможно и чего же в действительности надо бояться?</p>',
         '<p>A car battery can deliver hundreds of amperes to turn the engine, yet we touch its terminals without fear. From a socket a tenth of an ampere is enough to kill a person. So a “strong” current is safe and a “weak” one dangerous.</p><p>How is this possible and what should we really fear?</p>'),
 hint=('Подсказку даст модель «Ток через тело». Разгадка — в конце главы.', 'The “Current through the body” model gives a hint. The answer is at the end of the chapter.'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: что определяет опасность', 'The answer: what determines the danger'),
 answer=('<p>Аккумулятор «может дать» сотни ампер только если цепь имеет малое сопротивление. Какой ток пойдёт через человека, определяет закон Ома: <em>I = U / R</em>. При 12 В и сухой коже (100 кОм) это всего 0,12 мА (задача 1) — человек не почувствует. При 220 В и мокрой коже (1 кОм) — уже 220 мА (задача 2), что смертельно.</p><p>То есть опасен не «сильный источник», а <em>ток через тело</em>, а он зависит от напряжения и сопротивления. Поэтому в сырых помещениях применяют низкое напряжение, в приборах — УЗО, заземление и двойную изоляцию, а мокрыми руками к розеткам не прикасаются.</p>',
         '<p>A battery “can deliver” hundreds of amperes only if the circuit has a small resistance. What current passes through a person is determined by Ohm’s law: <em>I = U / R</em>. At 12 V and dry skin (100 kΩ) it is only 0.12 mA (problem 1) — the person feels nothing. At 220 V and wet skin (1 kΩ) it is already 220 mA (problem 2), which is lethal.</p><p>So it is not a “strong source” that is dangerous but the <em>current through the body</em>, and it depends on voltage and resistance. That is why low voltage is used in damp rooms, appliances are fitted with RCDs, earthing and double insulation, and sockets are not touched with wet hands.</p>'),
 sources=[
  ('Действие тока на человека: пороги и сопротивление тела —', 'Effects of current on people: thresholds and body resistance —', LINK('https://www.elcosh.org/document/1624/888/d000543/section2.html', 'eLCOSH: Electrical Safety — Student Manual') + ', ' + LINK('https://web.physics.ucsb.edu/~phys13BH/w2014/electrical_safety.pdf', 'UCSB: Electrical Safety Information') + ', ' + LINK('https://standards.iteh.ai/catalog/standards/iec/148397ec-5007-4232-9e06-3c3e10853fcc/iec-ts-60479-1', 'IEC/TS 60479-1: Effects of current on human beings')),
  ('УЗО на 30 мА, пороги отпускания и фибрилляции —', 'The 30 mA RCD, let-go and fibrillation thresholds —', LINK('https://open-exam-prep.com/study-guides/uk-city-guilds-2365-l2/electrical-safety-safe-isolation/electrical-hazards-electric-shock', 'Electric shock physiology and RCDs') + ', ' + LINK('https://www.scienceabc.com/eyeopeners/how-does-electricity-kill', 'ScienceABC: How does electricity kill')),
  ('Розетки типа C и F, напряжение 220 В в Кыргызстане —', 'Type C and F sockets, 220 V in Kyrgyzstan —', LINK('https://www.cia.gov/the-world-factbook/countries/kyrgyzstan/travel-facts', 'CIA World Factbook: Kyrgyzstan travel facts') + ', ' + LINK('https://www.worldstandards.eu/?p=13756', 'World Standards: Kyrgyzstan'))],
 note=('Все схемы и модели главы нарисованы для атласа (SVG). Тексты, загадка и задачи — оригинальные. Сопротивления кожи и пороги тока — приблизительные, у разных людей и в разных условиях они различаются. Глава не заменяет инструктаж по электробезопасности: при поражении током сначала обесточьте цепь, затем вызывайте скорую помощь.', 'All diagrams and models in this chapter were drawn for the atlas (SVG). The texts, puzzle and problems are original. Skin resistances and current thresholds are approximate and differ between people and conditions. The chapter does not replace safety instruction: if someone is shocked, first cut off the power, then call an ambulance.'),
 prev=('19-conduction-in-media.html', 'Глава 19 · Ток в жидкостях и газах', 'Chapter 19 · Current in liquids and gases'),
 next=('21-magnets.html', 'Глава 21 · Магниты', 'Chapter 21 · Magnets'),
 js=js)
build(c)
