# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'ЛЕПЁШКА И ПОЛОСКА: ДОЛИ', 'A FLATBREAD AND A STRIP: PARTS', 'fcSvg', '0 0 600 250',
  slider('fd', 'На сколько равных частей разделили', 'Into how many equal parts', 2, 12, 1, 4) + slider('fk', 'Сколько частей закрасили', 'How many parts are shaded', 0, 12, 1, 3),
  stats([('fF', 'Дробь', 'Fraction'), ('fS', 'Закрашено', 'Shaded'), ('fN', 'Не закрашено', 'Not shaded')]),
  'fcFb', 'Знаменатель (внизу) говорит, на сколько равных частей разделили целое. Числитель (вверху) — сколько частей взяли.',
  'The denominator (bottom) tells into how many equal parts the whole is divided. The numerator (top) tells how many parts are taken.')
s1 = section('parts', 'Доли и дроби', 'Parts and fractions',
 bd('<p>Если целое (лепёшку, отрезок) разделить на <strong>равные</strong> части, каждая часть — <strong>доля</strong>. Одна из четырёх равных частей — <em>четверть</em>, то есть 1/4. Три таких части — 3/4. Дробь пишут двумя числами: <strong>числитель</strong> — сколько частей взяли, <strong>знаменатель</strong> — сколько всего равных частей.</p>',
    '<p>If a whole (a flatbread, a bar) is divided into <strong>equal</strong> parts, each part is a <strong>fraction</strong> of the whole. One of four equal parts is a <em>quarter</em>, that is 1/4. Three such parts are 3/4. A fraction is written with two numbers: the <strong>numerator</strong> — how many parts are taken, the <strong>denominator</strong> — how many equal parts there are in all.</p>')
 + formula('3/4', 'три части из четырёх равных', 'three parts out of four equal ones'),
 lab1)

lab2 = model(2, 'КАКАЯ ДРОБЬ БОЛЬШЕ', 'WHICH FRACTION IS GREATER', 'fmSvg', '0 0 600 250',
  slider('f1n', 'Первая дробь: числитель', 'First fraction: numerator', 1, 12, 1, 1) + slider('f1d', 'Первая дробь: знаменатель', 'First fraction: denominator', 2, 12, 1, 3) + slider('f2n', 'Вторая дробь: числитель', 'Second fraction: numerator', 1, 12, 1, 1) + slider('f2d', 'Вторая дробь: знаменатель', 'Second fraction: denominator', 2, 12, 1, 4),
  stats([('gC', 'Сравнение', 'Comparison'), ('gW', 'К общему знаменателю', 'To a common denominator')]),
  'fmFb', 'Чем больше знаменатель, тем мельче доли: 1/3 больше, чем 1/4. Числитель не может быть больше знаменателя в этой главе.',
  'The larger the denominator, the smaller the parts: 1/3 is greater than 1/4. In this chapter the numerator cannot exceed the denominator.')
s2 = section('compare', 'Сравнение долей', 'Comparing fractions',
 bd('<p>У дробей с одинаковым знаменателем больше та, у которой больше числитель: 3/8 &gt; 2/8. Если одинаковые числители, больше та, у которой <strong>знаменатель меньше</strong>: 1/3 &gt; 1/4, ведь на 3 части режут крупнее, чем на 4. Ещё есть равные дроби: 1/2 = 2/4 = 3/6.</p>',
    '<p>For fractions with the same denominator the one with the greater numerator is greater: 3/8 &gt; 2/8. If the numerators are equal, the one with the <strong>smaller denominator</strong> is greater: 1/3 &gt; 1/4, because cutting into 3 gives bigger pieces than into 4. There are also equal fractions: 1/2 = 2/4 = 3/6.</p>')
 + formula('1/3 &gt; 1/4', 'меньше частей — они крупнее', 'fewer parts — they are bigger'),
 lab2)

lab3 = model(3, 'ДОЛЯ ОТ ЧИСЛА', 'A FRACTION OF A NUMBER', 'fnSvg', '0 0 600 250',
  slider('nn', 'Сколько всего (овец)', 'How many in all (sheep)', 4, 60, 4, 20) + select('nd', 'Делим на', 'Divide into') + slider('nk', 'Берём частей', 'Parts taken', 1, 10, 1, 3),
  stats([('nO', 'Одна часть', 'One part'), ('nR', 'Ответ', 'Answer'), ('nE', 'Запись', 'Notation')]),
  'fnFb', 'Чтобы найти долю числа: делим число на знаменатель и умножаем на числитель.',
  'To find a fraction of a number: divide the number by the denominator and multiply by the numerator.')
s3 = section('of', 'Доля от числа', 'A fraction of a number',
 bd('<p>Отара из 20 овец. Найдём <em>1/4</em> отары: 20 : 4 = 5 овец. А <em>3/4</em> — это 5 · 3 = 15 овец. Сначала находим одну долю (делим), потом берём нужное число долей (умножаем).</p>',
    '<p>A flock of 20 sheep. Let us find <em>1/4</em> of the flock: 20 : 4 = 5 sheep. And <em>3/4</em> is 5 · 3 = 15 sheep. First we find one part (divide), then take the needed number of parts (multiply).</p>')
 + formula('3/4 от 20 = 20 : 4 · 3 = 15', 'сначала делим, потом умножаем', 'first divide, then multiply'),
 lab3)

tasks = [
 task(1, 'Четверть отары', 'A quarter of the flock', 'В отаре 20 овец. Сколько овец составляет 1/4 отары? А 3/4?', 'A flock has 20 sheep. How many sheep make 1/4 of the flock? And 3/4?',
  '20 овец', '20 sheep', '1/4 — это 20 : 4 = 5 овец. 3/4 — это 5 · 3 = 15 овец.', '1/4 is 20 : 4 = 5 sheep. 3/4 is 5 · 3 = 15 sheep.', '5 и 15 овец.', '5 and 15 sheep.', True),
 task(2, 'Какая часть закрашена', 'What part is shaded', 'Полоску разделили на 8 равных частей, закрасили 5. Какая дробь закрашена? Какая не закрашена?', 'A strip was divided into 8 equal parts and 5 were shaded. What fraction is shaded? What fraction is not?',
  '8 частей, 5 закрашены', '8 parts, 5 shaded', 'Закрашено 5 из 8 — это 5/8. Не закрашено 8 − 5 = 3 части — это 3/8. Вместе 5/8 + 3/8 = 8/8 — целое.', '5 of 8 are shaded — that is 5/8. Not shaded: 8 − 5 = 3 parts — 3/8. Together 5/8 + 3/8 = 8/8 — the whole.', '5/8 и 3/8.', '5/8 and 3/8.'),
 task(3, 'Что больше', 'Which is greater', 'Сравните 1/3 и 1/4 лепёшки.', 'Compare 1/3 and 1/4 of a flatbread.',
  '1/3 и 1/4', '1/3 and 1/4', 'У обеих дробей числитель 1. Чем на меньшее число частей режем, тем они крупнее: на 3 части — крупнее, чем на 4.', 'Both fractions have numerator 1. The fewer parts we cut into, the bigger they are: 3 parts are bigger than 4.', '1/3 &gt; 1/4.', '1/3 &gt; 1/4.'),
 task(4, 'Половина и четверти', 'A half and quarters', 'Сколько четвертей в половине?', 'How many quarters are there in a half?',
  '1/2 = ?/4', '1/2 = ?/4', 'Разделим целое на 4 части. Половина — это две из четырёх частей: 1/2 = 2/4.', 'Divide the whole into 4 parts. A half is two of the four parts: 1/2 = 2/4.', '2 четверти.', '2 quarters.'),
 task(5, 'Задача про лепёшки', 'The flatbread problem', 'Как поровну разделить 3 лепёшки на 4 человека?', 'How do you share 3 flatbreads equally among 4 people?',
  '3 лепёшки, 4 человека', '3 flatbreads, 4 people', 'Разрежем каждую лепёшку на 4 четверти: всего 3 · 4 = 12 четвертей. На каждого — 12 : 4 = 3 четверти. Или иначе: две лепёшки разрежем пополам (4 половины — по одной на каждого), третью — на 4 четверти: у каждого 1/2 + 1/4 = 3/4.', 'Cut every flatbread into 4 quarters: 3 · 4 = 12 quarters in all. Each gets 12 : 4 = 3 quarters. Or another way: cut two flatbreads in halves (4 halves — one for each), the third into 4 quarters: everyone gets 1/2 + 1/4 = 3/4.', 'каждому по 3/4 лепёшки.', 'each gets 3/4 of a flatbread.'),
]
quiz = [
 qz('Что показывает знаменатель дроби 3/8?', 'На сколько равных частей разделили целое', 'Сколько частей взяли', 'Во сколько раз больше', 'Знаменатель — число 8 внизу.',
    'What does the denominator of 3/8 show?', 'Into how many equal parts the whole is divided', 'How many parts are taken', 'How many times greater', 'The denominator is the 8 at the bottom.'),
 qz('Что больше: 1/2 или 1/5?', '1/2', '1/5', 'Они равны', 'Половина — крупнее, чем пятая часть.',
    'Which is greater: 1/2 or 1/5?', '1/2', '1/5', 'They are equal', 'A half is bigger than a fifth.'),
 qz('Сколько будет 1/4 от 20?', '5', '4', '16', '20 : 4 = 5.',
    'What is 1/4 of 20?', '5', '4', '16', '20 : 4 = 5.'),
 qz('Сколько будет 3/4 от 20?', '15', '5', '23', '20 : 4 · 3 = 15.',
    'What is 3/4 of 20?', '15', '5', '23', '20 : 4 · 3 = 15.'),
 qz('Какая дробь равна 1/2?', '2/4', '1/4', '2/3', 'Две четверти — это половина.',
    'Which fraction equals 1/2?', '2/4', '1/4', '2/3', 'Two quarters make a half.'),
 qz('Что больше: 3/8 или 2/8?', '3/8', '2/8', 'Они равны', 'Знаменатели одинаковы — смотрим на числители.',
    'Which is greater: 3/8 or 2/8?', '3/8', '2/8', 'They are equal', 'The denominators are the same — compare numerators.'),
 qz('Целое разделили на 6 равных частей и закрасили 6. Что закрашено?', 'Всё целое', 'Половина', 'Ничего', '6/6 = 1.',
    'A whole is divided into 6 equal parts and 6 are shaded. What is shaded?', 'The whole', 'A half', 'Nothing', '6/6 = 1.'),
 qz('Части в дроби должны быть', 'Равными', 'Разными', 'Только красными', 'Доля — это одна из равных частей.',
    'The parts in a fraction must be', 'Equal', 'Different', 'Only red', 'A fraction is one of equal parts.'),
]
js = MJS + r'''
const T={ru:{fcLabel:"Круг и полоска, разделённые на равные части",fmLabel:"Две полоски с разными дробями",fnLabel:"Овцы, сгруппированные по равным долям"},
 en:{fcLabel:"A circle and a strip divided into equal parts",fmLabel:"Two strips with different fractions",fnLabel:"Sheep grouped into equal parts"}};
function frac(n,d){return n+"/"+d}
function drawFc(){const d=+$("fd").value,ks=$("fk");ks.max=d;const k=Math.min(+ks.value,d);ks.value=k;let g="";const cx=165,cy=125,r=95;
 for(let i=0;i<d;i++){const a0=-Math.PI/2+i*2*Math.PI/d,a1=-Math.PI/2+(i+1)*2*Math.PI/d;const x0=cx+r*Math.cos(a0),y0=cy+r*Math.sin(a0),x1=cx+r*Math.cos(a1),y1=cy+r*Math.sin(a1);
  g+='<path d="M'+cx+' '+cy+' L'+x0+' '+y0+' A'+r+' '+r+' 0 '+(2/d>1?1:0)+' 1 '+x1+' '+y1+' Z" fill="'+(i<k?COL.a:COL.bg)+'" stroke="'+COL.ink+'" stroke-width="1.5"/>'}
 const w=270;for(let i=0;i<d;i++)g+=R(300+i*w/d,95,w/d,60,i<k?COL.a:COL.bg,COL.ink,1.5);
 g+=TX(435,190,frac(k,d),COL.ink,34,"middle",600);
 $("fcSvg").innerHTML=g;$("fdOut").textContent=d;$("fkOut").textContent=k;
 $("fF").textContent=frac(k,d);$("fS").textContent=k+U(" из "+d," of "+d);$("fN").textContent=frac(d-k,d);
 $("fcFb").textContent=k===0?U("Ничего не закрашено: 0/"+d+".","Nothing is shaded: 0/"+d+"."):k===d?U("Закрашено всё целое: "+d+"/"+d+" = 1.","The whole is shaded: "+d+"/"+d+" = 1."):U("Закрашено "+k+" равных частей из "+d+": "+frac(k,d)+".",k+" equal parts out of "+d+" are shaded: "+frac(k,d)+".")}
["fd","fk"].forEach(id=>$(id).addEventListener("input",drawFc));
function drawFm(){const bd=+$("f1d").value,dd=+$("f2d").value;const a=Math.min(+$("f1n").value,bd),c=Math.min(+$("f2n").value,dd);let g="";
 [[a,bd,COL.a,50],[c,dd,COL.b,140]].forEach(f=>{const w=480;for(let i=0;i<f[1];i++)g+=R(60+i*w/f[1],f[3],w/f[1],55,i<f[0]?f[2]:COL.bg,COL.ink,1.5);g+=TX(30,f[3]+36,frac(f[0],f[1]),COL.ink,16,"middle",600)});
 const lhs=a*dd,rhs=c*bd,sign=lhs>rhs?"&gt;":lhs<rhs?"&lt;":"=";g+=TX(300,230,frac(a,bd)+" "+sign+" "+frac(c,dd),COL.ink,26);
 $("fmSvg").innerHTML=g;$("f1nOut").textContent=a;$("f1dOut").textContent=bd;$("f2nOut").textContent=c;$("f2dOut").textContent=dd;
 $("gC").innerHTML=frac(a,bd)+" "+sign+" "+frac(c,dd);$("gW").textContent=frac(lhs,bd*dd)+U(" и "," and ")+frac(rhs,bd*dd);
 $("fmFb").textContent=lhs===rhs?U("Это равные дроби: части разные, а закрашено поровну.","These are equal fractions: the parts differ but the shaded amount is the same."):U((lhs>rhs?"Первая":"Вторая")+" дробь больше.",(lhs>rhs?"The first":"The second")+" fraction is greater.")}
["f1n","f1d","f2n","f2d"].forEach(id=>$(id).addEventListener("input",drawFm));
function drawFn(){const n=+$("nn").value,d=+$("nd").value+2;const kk=$("nk");kk.max=d;const k=Math.min(+kk.value,d);kk.value=k;let g="";
 const ok=n%d===0,q=Math.floor(n/d);
 for(let i=0;i<n;i++){const col=i%20,row=Math.floor(i/20);const grp=ok?Math.floor(i/q):-1;const fill=ok?(grp<k?COL.a:COL.b):COL.line;g+=C(40+col*26,40+row*32,10,fill)+(ok&&i%q===0&&i>0?L(40+col*26-13,25+row*32,40+col*26-13,55+row*32,COL.ink,2):"")}
 g+=TX(300,190,ok?frac(k,d)+U(" от "," of ")+n+" = "+n+" : "+d+" · "+k+" = "+q*k:U(n+" не делится на "+d+" нацело — выберите другое число.",n+" is not divisible by "+d+" — choose another number."),COL.ink,ok?20:15);
 $("fnSvg").innerHTML=g;$("nnOut").textContent=n;$("nkOut").textContent=k;
 $("nO").textContent=ok?q:U(q+" (ост. "+(n%d)+")",q+" (rem. "+(n%d)+")");$("nR").textContent=ok?q*k:"—";$("nE").textContent=frac(k,d)+" · "+n;
 $("fnFb").textContent=ok?U("Одна часть — "+q+" овец; частей берём "+k+": "+q+" · "+k+" = "+q*k+".","One part is "+q+" sheep; we take "+k+" parts: "+q+" · "+k+" = "+q*k+"."):U("Если не делится нацело, долю целым числом овец не выразить.","If it does not divide evenly, the fraction is not a whole number of sheep.")}
["nn","nd","nk"].forEach(id=>$(id).addEventListener("input",drawFn));
const LAB={ru:{fcSvg:T.ru.fcLabel,fmSvg:T.ru.fmLabel,fnSvg:T.ru.fnLabel},en:{fcSvg:T.en.fcLabel,fmSvg:T.en.fmLabel,fnSvg:T.en.fnLabel}};
function drawAll(){fillSel("nd",["2","3","4","5","6","7","8","9","10","11","12"].map(x=>"1/"+x),2);drawFc();drawFm();drawFn()}
'''
c = dict(n='08', slug='08-fractions-intro.html', block='I', level_ru='ОСНОВЫ · 3–4 КЛАССЫ', level_en='BASICS · GRADES 3–4',
 title=('Доли и дроби', 'Parts and fractions'),
 desc='Глава 8 Атласа математики: доли, числитель и знаменатель, сравнение долей, доля от числа, равные дроби.',
 lead=('Как поровну разделить три лепёшки на четверых и что значит «три четверти»: первое знакомство с дробями.',
       'How to share three flatbreads among four and what “three quarters” means: a first look at fractions.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('parts', 'Доли', 'Parts'), ('compare', 'Сравнение', 'Comparing'), ('of', 'Доля от числа', 'Fraction of a number'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>К обеду пришли 4 человека, а лепёшек всего 3. Хозяйка хочет разделить лепёшки поровну, чтобы никому не было обидно. Но 3 на 4 нацело не делится.</p><p>Сколько лепёшки получит каждый и как её нарезать?</p>',
         '<p>Four people came to lunch, but there are only 3 flatbreads. The hostess wants to share them equally so nobody feels left out. But 3 does not divide by 4 evenly.</p><p>How much flatbread does each person get, and how should it be cut?</p>'),
 hint=stdhint('Лепёшка и полоска: доли', 'A flatbread and a strip: parts'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: по 3/4 лепёшки', 'The answer: 3/4 of a flatbread each'),
 answer=('<p>Каждому достанется 3/4 лепёшки. Чтобы это сделать, разрежем каждую лепёшку на 4 равные части: получится 12 четвертей, и каждому — по три. Можно хитрее: две лепёшки — пополам (по половине каждому), третью — на четыре четверти. Половина и четверть вместе дают 3/4: 1/2 = 2/4, и 2/4 + 1/4 = 3/4.</p>',
         '<p>Each person gets 3/4 of a flatbread. To do it, cut every flatbread into 4 equal parts: that gives 12 quarters, three for each person. Or more cleverly: cut two flatbreads in halves (a half for each person), the third into four quarters. A half and a quarter together make 3/4: 1/2 = 2/4, and 2/4 + 1/4 = 3/4.</p>'),
 sources=[('Дроби —', 'Fractions —', LINK('https://en.wikipedia.org/wiki/Fraction', 'Wikipedia: Fraction')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Сюжет про лепёшки придуман для атласа.', 'The story of the flatbreads was invented for the atlas.'),
 prev=('07-word-problems.html', 'Глава 7 · Текстовые задачи', 'Chapter 7 · Word problems'),
 next=('09-points-lines-angles.html', 'Глава 9 · Точки, линии, углы, фигуры', 'Chapter 9 · Points, lines, angles, shapes'),
 js=js)
build(c)
