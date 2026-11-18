# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'РАЗРЯДНЫЕ БЛОКИ', 'PLACE-VALUE BLOCKS', 'pvSvg', '0 0 600 250',
  slider('vh', 'Сотни', 'Hundreds', 0, 9, 1, 7) + slider('vt', 'Десятки', 'Tens', 0, 9, 1, 0) + slider('vu', 'Единицы', 'Ones', 0, 9, 1, 5),
  stats([('vN', 'Число', 'Number'), ('vW', 'Словами', 'In words'), ('vE', 'Разрядные слагаемые', 'Expanded form')]),
  'pvFb', 'Большой квадрат — сотня, палочка — десяток, кубик — единица. Нуль в разряде значит, что таких блоков нет.',
  'A big square is a hundred, a rod is a ten, a cube is a one. A zero in a place means there are no such blocks.')
s1 = section('blocks', 'Сотни, десятки, единицы', 'Hundreds, tens, ones',
 bd('<p>Десять единиц — это один десяток, десять десятков — одна <strong>сотня</strong>. Число из трёх цифр читается слева направо: сначала сотни, потом десятки, потом единицы. В числе 705 семь сотен, <strong>нуль десятков</strong> и пять единиц. Нуль нужен, чтобы пять не «съехало» в разряд десятков: 75 — совсем другое число.</p>',
    '<p>Ten ones make one ten, ten tens make one <strong>hundred</strong>. A three-digit number is read from left to right: hundreds first, then tens, then ones. The number 705 has seven hundreds, <strong>zero tens</strong> and five ones. The zero is needed so the five does not slide into the tens place: 75 is a very different number.</p>')
 + formula('705 = 700 + 0 + 5', 'каждая цифра стоит в своём разряде', 'every digit stands in its own place'),
 lab1)

lab2 = model(2, 'КТО БОЛЬШЕ: СРАВНИВАЕМ ПО РАЗРЯДАМ', 'WHO IS GREATER: COMPARING PLACE BY PLACE', 'cmSvg', '0 0 600 250',
  slider('mx', 'Первое число', 'First number', 0, 999, 1, 538) + slider('my', 'Второе число', 'Second number', 0, 999, 1, 583),
  stats([('mS', 'Сравнение', 'Comparison'), ('mP', 'Решает разряд', 'Decided by'), ('mD', 'Разница', 'Difference')]),
  'cmFb', 'Сравнивайте с самого старшего разряда — слева. Как только цифры разные, ответ уже известен.',
  'Compare from the highest place — the left one. As soon as the digits differ, the answer is known.')
s2 = section('compare', 'Сравнение чисел', 'Comparing numbers',
 bd('<p>Чем больше цифр, тем больше число: 120 &gt; 99. Если цифр поровну, сравниваем <strong>слева направо</strong>. У 538 и 583 сотни равны (5 и 5), десятки разные: 3 &lt; 8. Значит, 538 &lt; 583.</p>',
    '<p>The more digits, the greater the number: 120 &gt; 99. If the digit count is equal, compare <strong>from left to right</strong>. For 538 and 583 the hundreds are equal (5 and 5) and the tens differ: 3 &lt; 8. So 538 &lt; 583.</p>')
 + formula('538 &lt; 583', 'сотни равны, 3 десятка &lt; 8 десятков', 'hundreds equal, 3 tens &lt; 8 tens'),
 lab2)

lab3 = model(3, 'ОКРУГЛЕНИЕ', 'ROUNDING', 'rdSvg', '0 0 600 250',
  select('rp', 'Округлить до', 'Round to') + slider('rn', 'Число', 'Number', 0, 999, 1, 346),
  stats([('rLo', 'Круглое число слева', 'Round number to the left'), ('rHi', 'Круглое число справа', 'Round number to the right'), ('rAns', 'Ближайшее', 'Nearest')]),
  'rdFb', 'Круглое число — то, что оканчивается нулями: 340, 350, 400. Ближайшее — к которому на луче ближе.',
  'A round number ends in zeros: 340, 350, 400. The nearest one is the one closer on the line.')
s3 = section('round', 'Круглые числа и округление', 'Round numbers and rounding',
 bd('<p>Когда точное число не нужно, его <strong>округляют</strong>: заменяют ближайшим круглым. Смотрим на цифру справа от того разряда, до которого округляем. Если она 0, 1, 2, 3, 4 — число остаётся «внизу», если 5, 6, 7, 8, 9 — поднимается «вверх». 346 до десятков — 350, до сотен — 300.</p>',
    '<p>When the exact number is not needed, we <strong>round</strong> it: replace it by the nearest round number. Look at the digit to the right of the place we round to. If it is 0, 1, 2, 3, 4 the number stays “down”; if it is 5, 6, 7, 8, 9 it goes “up”. 346 to tens is 350, to hundreds 300.</p>')
 + formula('346 ≈ 350 ≈ 300', 'до десятков, до сотен', 'to tens, to hundreds'),
 lab3)

tasks = [
 task(1, 'Цена на бумажке', 'A price on a slip of paper', 'Продавец написал цену словами: «семьсот пять сомов». Как записать число цифрами?', 'The seller wrote a price in words: “seven hundred five soms”. How do you write the number with digits?',
  '7 сотен, 0 десятков, 5 единиц', '7 hundreds, 0 tens, 5 ones', 'Семь сотен — 700. Десятков нет — пишем 0 в разряде десятков. Пять единиц. Получаем 7 0 5.', 'Seven hundreds — 700. There are no tens — we write 0 in the tens place. Five ones. We get 7 0 5.', '705.', '705.', True),
 task(2, 'Разрядные слагаемые', 'Expanded form', 'Запишите число 482 суммой разрядных слагаемых.', 'Write the number 482 as a sum of its place values.',
  '482', '482', '4 сотни = 400, 8 десятков = 80, 2 единицы = 2.', '4 hundreds = 400, 8 tens = 80, 2 ones = 2.', '482 = 400 + 80 + 2.', '482 = 400 + 80 + 2.'),
 task(3, 'Сравните', 'Compare', 'Сравните числа 538 и 583.', 'Compare the numbers 538 and 583.',
  '538 и 583', '538 and 583', 'Сотни равны: 5 и 5. Десятки: 3 и 8, а 3 &lt; 8.', 'The hundreds are equal: 5 and 5. The tens: 3 and 8, and 3 &lt; 8.', '538 &lt; 583.', '538 &lt; 583.'),
 task(4, 'Округлите', 'Round it', 'Округлите 346 до десятков и до сотен.', 'Round 346 to tens and to hundreds.',
  '346', '346', 'До десятков: цифра единиц 6 ≥ 5, поэтому 346 поднимается до 350. До сотен: цифра десятков 4 &lt; 5, поэтому остаётся 300.', 'To tens: the ones digit is 6 ≥ 5, so 346 goes up to 350. To hundreds: the tens digit is 4 &lt; 5, so it stays at 300.', '350 и 300.', '350 and 300.'),
 task(5, 'Сколько десятков', 'How many tens', 'Сколько всего десятков в числе 340?', 'How many tens are there in the number 340 altogether?',
  '340', '340', '340 = 300 + 40. В трёх сотнях по 10 десятков: 3 · 10 = 30. Ещё 4 десятка: 30 + 4 = 34.', '340 = 300 + 40. Three hundreds hold 10 tens each: 3 · 10 = 30. 4 more tens: 30 + 4 = 34.', '34 десятка.', '34 tens.'),
]
quiz = [
 qz('Сколько десятков в числе 705?', 'Нуль десятков', '7 десятков', '5 десятков', 'В записи 705 на месте десятков стоит 0.',
    'How many tens does 705 have (as a digit)?', 'Zero tens', '7 tens', '5 tens', 'In 705 the digit in the tens place is 0.'),
 qz('Как записать «триста сорок»?', '340', '304', '3400', '3 сотни, 4 десятка, 0 единиц.',
    'How do you write “three hundred forty”?', '340', '304', '3400', '3 hundreds, 4 tens, 0 ones.'),
 qz('Что больше: 99 или 120?', '120', '99', 'Они равны', 'У 120 три цифры — это больше, чем у 99.',
    'Which is greater: 99 or 120?', '120', '99', 'They are equal', '120 has three digits — more than 99.'),
 qz('Сравните: 472 ? 427.', '472 &gt; 427', '472 &lt; 427', '472 = 427', 'Сотни равны, десятков 7 &gt; 2.',
    'Compare: 472 ? 427.', '472 &gt; 427', '472 &lt; 427', '472 = 427', 'The hundreds are equal, 7 tens &gt; 2 tens.'),
 qz('Чему равно 600 + 40 + 9?', '649', '694', '6049', '6 сотен, 4 десятка, 9 единиц.',
    'What is 600 + 40 + 9?', '649', '694', '6049', '6 hundreds, 4 tens, 9 ones.'),
 qz('Округлите 78 до десятков.', '80', '70', '100', 'Цифра единиц 8 ≥ 5 — вверх.',
    'Round 78 to tens.', '80', '70', '100', 'The ones digit 8 ≥ 5 — up.'),
 qz('Округлите 530 до сотен.', '500', '600', '530', 'Цифра десятков 3 &lt; 5 — вниз.',
    'Round 530 to hundreds.', '500', '600', '530', 'The tens digit 3 &lt; 5 — down.'),
 qz('Сколько единиц в одной сотне?', '100', '10', '1000', '1 сотня = 10 десятков = 100 единиц.',
    'How many ones are in one hundred?', '100', '10', '1000', '1 hundred = 10 tens = 100 ones.'),
]
js = MJS + r'''
const H=["","сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот"],D=["","","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"],TN=["десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"],O=["","один","два","три","четыре","пять","шесть","семь","восемь","девять"];
const EO=["","one","two","three","four","five","six","seven","eight","nine"],ETN=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"],ED=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];
function wRu(n){if(n===0)return"нуль";const h=Math.floor(n/100),r=n%100,p=[];if(h)p.push(H[h]);if(r>=10&&r<20)p.push(TN[r-10]);else{const d=Math.floor(r/10),o=r%10;if(d)p.push(D[d]);if(o)p.push(O[o])}return p.join(" ")}
function wEn(n){if(n===0)return"zero";const h=Math.floor(n/100),r=n%100,p=[];if(h)p.push(EO[h]+" hundred");if(r>=10&&r<20)p.push(ETN[r-10]);else{const d=Math.floor(r/10),o=r%10;if(d&&o)p.push(ED[d]+"-"+EO[o]);else if(d)p.push(ED[d]);else if(o)p.push(EO[o])}return p.join(" ")}
const T={ru:{pvLabel:"Разрядные блоки: сотни, десятки, единицы",cmLabel:"Сравнение двух трёхзначных чисел",rdLabel:"Число на луче между двумя круглыми числами",pl:["десятков","сотен"],hn:"сотни",tn:"десятки",on:"единицы"},
 en:{pvLabel:"Place-value blocks: hundreds, tens, ones",cmLabel:"Comparing two three-digit numbers",rdLabel:"A number on a line between two round numbers",pl:["tens","hundreds"],hn:"hundreds",tn:"tens",on:"ones"}};
function drawPv(){const t=T[lang],h=+$("vh").value,te=+$("vt").value,u=+$("vu").value,n=h*100+te*10+u;let g="";
 for(let i=0;i<h;i++)g+=R(40+(i%3)*42,30+Math.floor(i/3)*42,38,38,COL.a,COL.ink,1);
 for(let i=0;i<te;i++)g+=R(235+i*17,30,13,120,COL.d,COL.ink,1);
 for(let i=0;i<u;i++)g+=R(430+(i%3)*30,30+Math.floor(i/3)*30,24,24,COL.b,COL.ink,1);
 [[100,h,t.hn],[300,te,t.tn],[500,u,t.on]].forEach(a=>{g+=TX(a[0],185,a[2],COL.mut,13)+TX(a[0],228,String(a[1]),COL.ink,36,"middle",600)});
 $("pvSvg").innerHTML=g;$("vhOut").textContent=h;$("vtOut").textContent=te;$("vuOut").textContent=u;
 $("vN").textContent=n;$("vW").textContent=lang==="ru"?wRu(n):wEn(n);
 const parts=[];if(h)parts.push(h*100);if(te)parts.push(te*10);if(u||!parts.length)parts.push(u);$("vE").textContent=parts.join(" + ");
 $("pvFb").textContent=(te===0&&h>0)?U("Нуль десятков: в записи числа стоит 0, чтобы цифры не съехали.","Zero tens: the 0 stands in the number so the digits do not slide."):U("Читаем слева направо: сотни, десятки, единицы.","We read left to right: hundreds, tens, ones.")}
["vh","vt","vu"].forEach(id=>$(id).addEventListener("input",drawPv));
function drawCm(){const t=T[lang],x=+$("mx").value,y=+$("my").value;const dg=n=>[Math.floor(n/100),Math.floor(n/10)%10,n%10];const a=dg(x),b=dg(y),names=[t.hn,t.tn,t.on];let dec=-1;
 for(let i=0;i<3;i++){if(a[i]!==b[i]){dec=i;break}}
 const wide=n=>n>=100?3:n>=10?2:1;let g="";
 [[x,a,70,COL.a],[y,b,150,COL.b]].forEach(row=>{for(let i=0;i<3;i++){const cx=170+i*130;g+=R(cx-45,row[2]-34,90,48,i===dec?"#fff4e0":COL.bg,i===dec?COL.d:COL.line,i===dec?3:1)+TX(cx,row[2]+2,String(row[1][i]),row[3],34,"middle",600)}g+=TX(60,row[2]+2,String(row[0]),COL.ink,22,"middle",600)});
 for(let i=0;i<3;i++)g+=TX(170+i*130,30,names[i],COL.mut,12);
 const sign=x<y?"&lt;":x>y?"&gt;":"=";g+=TX(300,215,x+" "+sign+" "+y,COL.ink,28);
 $("cmSvg").innerHTML=g;$("mxOut").textContent=x;$("myOut").textContent=y;
 $("mS").innerHTML=x+" "+sign+" "+y;$("mP").textContent=dec<0?U("цифры совпали","all digits equal"):names[dec];$("mD").textContent=Math.abs(x-y);
 $("cmFb").textContent=dec<0?U("Числа одинаковы.","The numbers are the same."):U("Первое различие — в разряде «"+names[dec]+"»: "+a[dec]+" и "+b[dec]+". "+(a[dec]>b[dec]?"Первое число больше.":"Второе число больше."),"The first difference is in the “"+names[dec]+"” place: "+a[dec]+" and "+b[dec]+". "+(a[dec]>b[dec]?"The first number is greater.":"The second number is greater."))}
["mx","my"].forEach(id=>$(id).addEventListener("input",drawCm));
function drawRd(){const t=T[lang],k=+$("rp").value,p=k===0?10:100,n=+$("rn").value,lo=Math.floor(n/p)*p,hi=lo+p,near=(n-lo)>=p/2?hi:lo;
 let g=numLine(50,550,140,lo,hi,p/10,1);const X=px(n,50,550,lo,hi);
 g+=C(X,140,10,COL.b)+TX(X,100,String(n),COL.b,22,"middle",600)+L(X,108,X,130,COL.b,2);
 g+=C(px(near,50,550,lo,hi),140,13,"none",COL.a,4)+TX(300,215,n+" ≈ "+near,COL.ink,26);
 $("rdSvg").innerHTML=g;$("rnOut").textContent=n;
 $("rLo").textContent=lo;$("rHi").textContent=hi;$("rAns").textContent=near;
 const dgt=p===10?n%10:Math.floor(n/10)%10;
 $("rdFb").textContent=U("Смотрим на цифру "+dgt+": "+(dgt>=5?"она 5 или больше — вверх, до "+hi+".":"она меньше 5 — вниз, до "+lo+"."),"Look at the digit "+dgt+": "+(dgt>=5?"it is 5 or more — up, to "+hi+".":"it is less than 5 — down, to "+lo+"."))}
["rp","rn"].forEach(id=>$(id).addEventListener("input",drawRd));
const LAB={ru:{pvSvg:T.ru.pvLabel,cmSvg:T.ru.cmLabel,rdSvg:T.ru.rdLabel},en:{pvSvg:T.en.pvLabel,cmSvg:T.en.cmLabel,rdSvg:T.en.rdLabel}};
function drawAll(){fillSel("rp",T[lang].pl,0);drawPv();drawCm();drawRd()}
'''
c = dict(n='03', slug='03-place-value.html', block='I', level_ru='ОСНОВЫ · 2–3 КЛАССЫ', level_en='BASICS · GRADES 2–3',
 title=('Разряды и числа до 1000', 'Place value and numbers to 1000'),
 desc='Глава 3 Атласа математики: сотни, десятки и единицы, запись и чтение трёхзначных чисел, сравнение и округление.',
 lead=('Почему 705 — не то же, что 75: разряды, сравнение трёхзначных чисел и округление.',
       'Why 705 is not the same as 75: place value, comparing three-digit numbers and rounding.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('blocks', 'Разряды', 'Place value'), ('compare', 'Сравнение', 'Comparing'), ('round', 'Округление', 'Rounding'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Продавец написал цену на бумажке словами: «семьсот пять сомов». Покупатели записали число цифрами по-разному: один написал 75, другой 750, третий 705.</p><p>Кто записал правильно и почему остальные ошиблись?</p>',
         '<p>A seller wrote a price in words on a slip of paper: “seven hundred five soms”. Buyers wrote the number with digits in different ways: one wrote 75, another 750, a third 705.</p><p>Who wrote it correctly and why were the others wrong?</p>'),
 hint=stdhint('Разрядные блоки', 'Place-value blocks'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 705', 'The answer: 705'),
 answer=('<p>Правильно 705: семь сотен, нуль десятков, пять единиц. В числе 75 всего 7 десятков и 5 единиц — это гораздо меньше. А в 750 — семь сотен и пять десятков, единиц нет. Цифра значит не только «сколько», но и «где стоит»: поэтому нуль — не пустое место, а знак, что в разряде ничего нет.</p>',
         '<p>The correct one is 705: seven hundreds, zero tens, five ones. The number 75 has only 7 tens and 5 ones — much less. And 750 has seven hundreds and five tens, no ones. A digit means not only “how many” but also “where it stands”: so zero is not an empty gap but a sign that the place holds nothing.</p>'),
 sources=[('Позиционная запись чисел —', 'Positional notation —', LINK('https://en.wikipedia.org/wiki/Positional_notation', 'Wikipedia: Positional notation') + ', ' + LINK('https://en.wikipedia.org/wiki/Rounding', 'Wikipedia: Rounding')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Цены и сюжет придуманы для атласа.', 'The prices and the story were invented for the atlas.'),
 prev=('02-add-subtract.html', 'Глава 2 · Сложение и вычитание', 'Chapter 2 · Addition and subtraction'),
 next=('04-multiply-divide.html', 'Глава 4 · Умножение и деление', 'Chapter 4 · Multiplication and division'),
 js=js)
build(c)
