# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

lab1 = model(1, 'РЯДЫ И СТОЛБЦЫ', 'ROWS AND COLUMNS', 'arSvg', '0 0 600 250',
  slider('ar', 'Рядов', 'Rows', 1, 10, 1, 7) + slider('ac', 'В каждом ряду', 'In each row', 1, 10, 1, 8),
  stats([('aP', 'Умножение', 'Multiplication'), ('aS', 'Сложение', 'Addition'), ('aSw', 'Переставили', 'Swapped')]),
  'arFb', 'Умножение — это быстрое сложение одинаковых чисел. Ряды и столбцы можно поменять местами.',
  'Multiplication is a fast way to add equal numbers. Rows and columns can swap places.')
s1 = section('array', 'Умножение — сложение одинаковых', 'Multiplication is adding equal numbers',
 bd('<p>Если ящиков 7, а в каждом по 8 яблок, то всего <em>8 + 8 + 8 + 8 + 8 + 8 + 8</em>. Записывать так долго, поэтому придумали <strong>умножение</strong>: 8 · 7 = 56. Числа, которые умножают, — <strong>множители</strong>, а результат — <strong>произведение</strong>.</p><p>Если выложить яблоки рядами, видно: 7 рядов по 8 — то же самое, что 8 рядов по 7. От перемены мест множителей произведение не меняется.</p>',
    '<p>If there are 7 crates with 8 apples in each, the total is <em>8 + 8 + 8 + 8 + 8 + 8 + 8</em>. Writing that is long, so <strong>multiplication</strong> was invented: 8 · 7 = 56. The numbers we multiply are the <strong>factors</strong>, the result is the <strong>product</strong>.</p><p>Lay the apples out in rows and you can see: 7 rows of 8 is the same as 8 rows of 7. Swapping the factors does not change the product.</p>')
 + formula('a · b = b · a', 'множители можно менять местами', 'the factors can swap places'),
 lab1)

lab2 = model(2, 'ДЕЛИМ ПОРОВНУ', 'SHARING EQUALLY', 'dvSvg', '0 0 600 250',
  slider('dn', 'Сколько всего', 'How many in all', 1, 50, 1, 23) + slider('dg', 'На сколько частей', 'Into how many groups', 2, 10, 1, 4),
  stats([('dQ', 'В каждой части', 'In each group'), ('dR', 'Осталось', 'Left over'), ('dC', 'Проверка', 'Check')]),
  'dvFb', 'Раздаём по одному, пока хватает на всех. Если осталось меньше, чем частей, — это остаток.',
  'We hand out one at a time while there is enough for everyone. What is left, fewer than the groups, is the remainder.')
s2 = section('divide', 'Деление и остаток', 'Division and remainder',
 bd('<p><strong>Деление</strong> — это раздать поровну или узнать, сколько раз одно число «помещается» в другом. 24 : 6 = 4, потому что 6 · 4 = 24. Если поровну не получается, остаётся <strong>остаток</strong>, и он всегда меньше делителя: 23 : 4 = 5 (остаток 3), потому что 4 · 5 + 3 = 23.</p>',
    '<p><strong>Division</strong> means sharing equally or finding how many times one number “fits” into another. 24 : 6 = 4 because 6 · 4 = 24. If it does not share equally, a <strong>remainder</strong> is left, and it is always smaller than the divisor: 23 : 4 = 5 (remainder 3) because 4 · 5 + 3 = 23.</p>')
 + formula(bi('делимое = делитель · частное + остаток', 'dividend = divisor · quotient + remainder'), '23 = 4 · 5 + 3', '23 = 4 · 5 + 3'),
 lab2)

lab3 = model(3, 'ТАБЛИЦА УМНОЖЕНИЯ', 'THE MULTIPLICATION TABLE', 'mtSvg', '0 0 600 250',
  select('mn', 'Выделить число', 'Highlight number'),
  stats([('mRow', 'Ответы', 'Answers'), ('mRule', 'Секрет', 'Pattern')]),
  'mtFb', 'Таблица симметрична: 3 · 7 и 7 · 3 стоят по разные стороны от диагонали, а числа в них одинаковы.',
  'The table is symmetric: 3 · 7 and 7 · 3 stand on opposite sides of the diagonal and the numbers are equal.')
s3 = section('table', 'Таблица умножения и её секреты', 'The multiplication table and its secrets',
 bd('<p>Таблицу умножения не нужно зубрить целиком. Умножение на 1 не меняет число, умножение на 0 даёт 0, умножение на 10 — приписывает нуль. Числа на 2 — чётные, на 5 — оканчиваются на 0 или 5. А у чисел в строке «на 9» сумма цифр всегда 9: 18 → 1 + 8, 27 → 2 + 7, 36 → 3 + 6.</p>',
    '<p>There is no need to memorise the whole table. Multiplying by 1 leaves the number as it is, by 0 gives 0, by 10 adds a zero. Products of 2 are even, products of 5 end in 0 or 5. And in the “times 9” row the digits always add up to 9: 18 → 1 + 8, 27 → 2 + 7, 36 → 3 + 6.</p>')
 + formula('9 · 4 = 36', '3 + 6 = 9', '3 + 6 = 9'),
 lab3)

tasks = [
 task(1, 'Боорсоки', 'Fried dough', 'Мама поставила 6 тарелок, на каждой по 4 боорсока. Сколько всего боорсоков?', 'Mother put out 6 plates with 4 pieces of fried dough on each. How many pieces are there in all?',
  '6 тарелок по 4', '6 plates of 4', '4 · 6 = 4 + 4 + 4 + 4 + 4 + 4 = 24.', '4 · 6 = 4 + 4 + 4 + 4 + 4 + 4 = 24.', '24 боорсока.', '24 pieces.', True),
 task(2, 'Раздать поровну', 'Share equally', '24 карандаша раздали поровну 6 детям. Сколько карандашей у каждого?', '24 pencils were shared equally among 6 children. How many pencils does each get?',
  '24 : 6', '24 : 6', 'Ищем число, которое при умножении на 6 даёт 24: 6 · 4 = 24.', 'We look for the number that gives 24 when multiplied by 6: 6 · 4 = 24.', 'по 4 карандаша.', '4 pencils each.'),
 task(3, 'С остатком', 'With a remainder', '35 орехов разложили по 4 в мешочек. Сколько полных мешочков и сколько орехов останется?', '35 nuts were packed 4 to a bag. How many full bags and how many nuts are left?',
  '35 : 4', '35 : 4', '4 · 8 = 32, а 4 · 9 = 36 — уже больше 35. Значит, 8 мешочков, и 35 − 32 = 3 ореха остаётся.', '4 · 8 = 32, and 4 · 9 = 36 is already more than 35. So 8 bags, and 35 − 32 = 3 nuts are left.', '8 мешочков и 3 ореха в остатке.', '8 bags and 3 nuts left over.'),
 task(4, '7 · 8 без таблицы', '7 · 8 without the table', 'Забыли, сколько будет 7 · 8. Но помним, что 7 · 7 = 49. Как найти ответ?', 'You forgot what 7 · 8 is, but you remember 7 · 7 = 49. How do you find the answer?',
  '7 · 7 = 49', '7 · 7 = 49', '8 ящиков — это 7 ящиков и ещё один: 7 · 8 = 7 · 7 + 7 = 49 + 7 = 56.', '8 crates are 7 crates plus one more: 7 · 8 = 7 · 7 + 7 = 49 + 7 = 56.', '56.', '56.'),
 task(5, 'В несколько раз больше', 'Several times as many', 'У Азата 5 орехов, а у Бека в 3 раза больше. Сколько орехов у Бека?', 'Azat has 5 nuts and Bek has 3 times as many. How many nuts does Bek have?',
  '5 и «в 3 раза больше»', '5 and “3 times as many”', '«В 3 раза больше» — это 3 раза по 5: 5 · 3 = 15.', '“3 times as many” means 3 times 5: 5 · 3 = 15.', '15 орехов.', '15 nuts.'),
]
quiz = [
 qz('Чему равно 6 · 7?', '42', '36', '48', '6 · 7 = 6 · 6 + 6 = 36 + 6 = 42.',
    'What is 6 · 7?', '42', '36', '48', '6 · 7 = 6 · 6 + 6 = 36 + 6 = 42.'),
 qz('Как называется результат умножения?', 'Произведение', 'Частное', 'Сумма', 'Результат умножения — произведение.',
    'What is the result of a multiplication called?', 'The product', 'The quotient', 'The sum', 'The result of a multiplication is the product.'),
 qz('Чему равно 54 : 9?', '6', '5', '45', '9 · 6 = 54.',
    'What is 54 : 9?', '6', '5', '45', '9 · 6 = 54.'),
 qz('Чему равно любое число, умноженное на 0?', '0', 'Самому числу', '1', 'Нуль групп — ничего нет.',
    'What is any number multiplied by 0?', '0', 'The number itself', '1', 'Zero groups — nothing at all.'),
 qz('Какое утверждение верно?', '3 · 8 = 8 · 3', '3 · 8 = 8 + 3', '24 : 3 = 3 · 8', 'Множители можно менять местами.',
    'Which statement is true?', '3 · 8 = 8 · 3', '3 · 8 = 8 + 3', '24 : 3 = 3 · 8', 'Factors can swap places.'),
 qz('Какой остаток при делении 29 на 5?', '4', '5', '6', '5 · 5 = 25, 29 − 25 = 4.',
    'What is the remainder when 29 is divided by 5?', '4', '5', '6', '5 · 5 = 25, 29 − 25 = 4.'),
 qz('Может ли остаток при делении на 4 быть равен 4?', 'Нет, остаток меньше делителя', 'Да', 'Только при делении на 2', 'Если осталось 4, можно положить ещё один полный мешочек.',
    'Can the remainder when dividing by 4 be 4?', 'No, the remainder is smaller than the divisor', 'Yes', 'Only when dividing by 2', 'If 4 are left, one more full group can be made.'),
 qz('У чисел в строке «на 9» (18, 27, 36…) сумма цифр равна', '9', '10', '18', '1 + 8 = 9, 2 + 7 = 9, 3 + 6 = 9.',
    'In the “times 9” row (18, 27, 36…) the digits add up to', '9', '10', '18', '1 + 8 = 9, 2 + 7 = 9, 3 + 6 = 9.'),
]
js = MJS + r'''
const T={ru:{arLabel:"Яблоки, выложенные рядами",dvLabel:"Предметы, разложенные в группы",mtLabel:"Таблица умножения 10 на 10",
 rules:{1:"число не меняется",2:"все ответы чётные",3:"сумма цифр делится на 3",4:"удвой дважды",5:"оканчиваются на 0 или 5",6:"чётные, сумма цифр делится на 3",7:"7 · 7 = 49 — опорный пример",8:"удвой три раза",9:"сумма цифр всегда 9 (9 · 1…9 · 9, кроме 9 · 10)",10:"к числу приписывается нуль"}},
 en:{arLabel:"Apples laid out in rows",dvLabel:"Objects sorted into groups",mtLabel:"A 10 by 10 multiplication table",
 rules:{1:"the number stays the same",2:"all answers are even",3:"the digit sum is divisible by 3",4:"double twice",5:"they end in 0 or 5",6:"even, the digit sum is divisible by 3",7:"7 · 7 = 49 is the anchor",8:"double three times",9:"the digit sum is always 9 (9 · 1 … 9 · 9)",10:"a zero is added to the number"}}};
function drawAr(){const r=+$("ar").value,c=+$("ac").value,p=r*c;const s=Math.min(24,Math.floor(300/r),Math.floor(520/c));let g="";const x0=300-c*s/2,y0=125-r*s/2;
 for(let i=0;i<r;i++)for(let j=0;j<c;j++)g+=C(x0+j*s+s/2,y0+i*s+s/2,s*0.38,i%2?COL.a:COL.d,"none");
 $("arSvg").innerHTML=g;$("arOut").textContent=r;$("acOut").textContent=c;
 $("aP").textContent=c+" · "+r+" = "+p;$("aS").textContent=(r<=6?Array(r).fill(c).join(" + "):c+" + "+c+" + … ("+r+U(" раз)"," times)"))+" = "+p;$("aSw").textContent=r+" · "+c+" = "+p;
 $("arFb").textContent=U(r+(r===1?" ряд":r<5?" ряда":" рядов")+" по "+c+" — это всего "+p+".",r+" row"+(r===1?"":"s")+" of "+c+" — "+p+" in all.")}
["ar","ac"].forEach(id=>$(id).addEventListener("input",drawAr));
function drawDv(){const n=+$("dn").value,k=+$("dg").value,q=Math.floor(n/k),rem=n%k;let g="";const w=Math.min(110,560/k);
 for(let i=0;i<k;i++){const x=300-k*w/2+i*w;g+=R(x+4,40,w-8,110,COL.bg,COL.ink,2,6);for(let j=0;j<q;j++){g+=C(x+14+(j%5)*((w-28)/5)+6,58+Math.floor(j/5)*16,5,COL.b)}g+=TX(x+w/2,170,String(q),COL.ink,18,"middle",600)}
 for(let j=0;j<rem;j++)g+=C(40+j*16,215,6,COL.a);
 g+=TX(300,238,rem?U("остаток: "+rem,"remainder: "+rem):U("остатка нет","no remainder"),COL.mut,13);
 $("dvSvg").innerHTML=g;$("dnOut").textContent=n;$("dgOut").textContent=k;
 $("dQ").textContent=q;$("dR").textContent=rem;$("dC").textContent=k+" · "+q+" + "+rem+" = "+n;
 $("dvFb").textContent=U(n+" : "+k+" = "+q+(rem?" (ост. "+rem+")":"")+".",n+" : "+k+" = "+q+(rem?" (remainder "+rem+")":"")+".")}
["dn","dg"].forEach(id=>$(id).addEventListener("input",drawDv));
function drawMt(){const t=T[lang],h=+$("mn").value;let g="";const w=46,ht=22,x0=70,y0=22;
 for(let j=1;j<=10;j++)g+=TX(x0+(j-1)*w+w/2,15,String(j),COL.mut,11,"middle",600);
 for(let i=1;i<=10;i++){g+=TX(40,y0+(i-1)*ht+15,String(i),COL.mut,11,"middle",600);for(let j=1;j<=10;j++){const hit=(i===h||j===h);g+=R(x0+(j-1)*w,y0+(i-1)*ht,w,ht,hit?(i===h&&j===h?COL.a:"#f4dfd8"):COL.bg,COL.line,1)+TX(x0+(j-1)*w+w/2,y0+(i-1)*ht+15,String(i*j),hit&&i===h&&j===h?"#fff":COL.ink,12)}}
 $("mtSvg").innerHTML=g;
 const row=[];for(let j=1;j<=10;j++)row.push(h*j);$("mRow").textContent=row.join(", ");$("mRule").textContent=t.rules[h];$("mtFb").textContent=U("Строка и столбец числа "+h+" подсвечены; в клетке пересечения — "+h+" · "+h+" = "+h*h+".","The row and column of "+h+" are highlighted; at their crossing — "+h+" · "+h+" = "+h*h+".")}
$("mn").addEventListener("input",drawMt);
const LAB={ru:{arSvg:T.ru.arLabel,dvSvg:T.ru.dvLabel,mtSvg:T.ru.mtLabel},en:{arSvg:T.en.arLabel,dvSvg:T.en.dvLabel,mtSvg:T.en.mtLabel}};
function drawAll(){fillSel("mn",["1","2","3","4","5","6","7","8","9","10"],6);drawAr();drawDv();drawMt()}
'''
c = dict(n='04', slug='04-multiply-divide.html', block='I', level_ru='ОСНОВЫ · 2–3 КЛАССЫ', level_en='BASICS · GRADES 2–3',
 title=('Умножение и деление', 'Multiplication and division'),
 desc='Глава 4 Атласа математики: умножение как сложение одинаковых, деление поровну и с остатком, таблица умножения и её секреты.',
 lead=('Как не зубрить таблицу умножения: ряды и столбцы, деление поровну, остаток и несколько секретов.',
       'How not to cram the multiplication table: rows and columns, sharing equally, the remainder and a few secrets.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('array', 'Умножение', 'Multiplication'), ('divide', 'Деление', 'Division'), ('table', 'Таблица', 'The table'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>На базаре у продавца 7 ящиков яблок, в каждом ящике по 8 яблок. Покупатель торопится и просит быстро назвать, сколько всего яблок. Продавец забыл, сколько будет 7 · 8, но помнит, что 7 · 7 = 49.</p><p>Как ему найти ответ, не считая яблоки по одному?</p>',
         '<p>At the bazaar a seller has 7 crates of apples with 8 apples in each. A buyer is in a hurry and asks how many apples there are in all. The seller forgot what 7 · 8 is, but he remembers that 7 · 7 = 49.</p><p>How can he find the answer without counting the apples one by one?</p>'),
 hint=stdhint('Ряды и столбцы', 'Rows and columns'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 56 яблок', 'The answer: 56 apples'),
 answer=('<p>8 ящиков — это 7 ящиков и ещё один. Значит, 7 · 8 = 7 · 7 + 7 = 49 + 7 = 56. Можно иначе: 7 · 8 = 7 · 5 + 7 · 3 = 35 + 21 = 56. Если знать несколько «опорных» примеров, остальные таблицы получаются сами — и никакой зубрёжки.</p>',
         '<p>8 crates are 7 crates plus one more. So 7 · 8 = 7 · 7 + 7 = 49 + 7 = 56. Or another way: 7 · 8 = 7 · 5 + 7 · 3 = 35 + 21 = 56. If you know a few “anchor” facts, the rest of the table follows by itself — and there is no cramming.</p>'),
 sources=[('Умножение и деление —', 'Multiplication and division —', LINK('https://en.wikipedia.org/wiki/Multiplication_table', 'Wikipedia: Multiplication table') + ', ' + LINK('https://en.wikipedia.org/wiki/Division_(mathematics)', 'Wikipedia: Division')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Сюжет про продавца придуман для атласа.', 'The story of the seller was invented for the atlas.'),
 prev=('03-place-value.html', 'Глава 3 · Разряды и числа до 1000', 'Chapter 3 · Place value and numbers to 1000'),
 next=('05-column-arithmetic.html', 'Глава 5 · Действия в столбик', 'Chapter 5 · Column arithmetic'),
 js=js)
build(c)
