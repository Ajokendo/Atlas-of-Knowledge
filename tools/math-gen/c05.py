# -*- coding: utf-8 -*-
from h5 import *
from MJS import MJS

def colmodel(n, t_ru, t_en, sid, pre, a_lo, a_hi, a_def, b_lo, b_hi, b_def, a_ru, b_ru, a_en, b_en, fbid, cap_ru, cap_en, stats3):
    return model(n, t_ru, t_en, sid + 'Svg', '0 0 600 250',
      slider(pre + 'a', a_ru, a_en, a_lo, a_hi, 1, a_def) + slider(pre + 'b', b_ru, b_en, b_lo, b_hi, 1, b_def) + slider(pre + 's', 'Шаг', 'Step', 0, 5, 1, 5),
      stats(stats3), fbid, cap_ru, cap_en)

lab1 = colmodel(1, 'СЛОЖЕНИЕ В СТОЛБИК', 'COLUMN ADDITION', 'ad', 'ad', 0, 9999, 3478, 0, 9999, 2659, 'Первое слагаемое', 'Второе слагаемое', 'First addend', 'Second addend', 'adFb',
  'Пишем числа друг под другом: единицы под единицами. Складываем по разрядам справа налево. Если в разряде вышло 10 или больше — единицу переносим в следующий разряд.',
  'We write numbers one under another: ones under ones. We add place by place from right to left. If a place gives 10 or more, we carry one to the next place.',
  [('adSum', 'Сумма', 'Sum'), ('adCar', 'Переносов', 'Carries'), ('adChk', 'Проверка', 'Check')])
s1 = section('add', 'Сложение в столбик', 'Column addition',
 bd('<p>Большие числа складывают по разрядам. Начинаем с <strong>единиц</strong>: 8 + 9 = 17. Это 7 единиц и 1 десяток. Семь пишем, а один десяток «запоминаем» — переносим в разряд десятков. Дальше так же с десятками, сотнями и тысячами.</p>',
    '<p>Large numbers are added place by place. We start with the <strong>ones</strong>: 8 + 9 = 17. That is 7 ones and 1 ten. We write the seven and “remember” the ten — carry it to the tens place. Then we do the same with tens, hundreds and thousands.</p>')
 + formula('8 + 9 = 17 → пишем 7, переносим 1', '17 единиц = 1 десяток и 7 единиц', '17 ones = 1 ten and 7 ones').replace('→ пишем 7, переносим 1', '').replace('8 + 9 = 17 ', bi('8 + 9 = 17: пишем 7, переносим 1', '8 + 9 = 17: write 7, carry 1')),
 lab1)

lab2 = colmodel(2, 'ВЫЧИТАНИЕ В СТОЛБИК', 'COLUMN SUBTRACTION', 'sb', 'sb', 0, 9999, 5203, 0, 9999, 1874, 'Уменьшаемое', 'Вычитаемое', 'Minuend', 'Subtrahend', 'sbFb',
  'Если в разряде вычесть нельзя, «занимаем» один десяток у соседнего разряда слева: он превращается в 10 единиц.',
  'If you cannot subtract in a place, you “borrow” one ten from the neighbouring place on the left: it turns into 10 ones.',
  [('sbDif', 'Разность', 'Difference'), ('sbBor', 'Заёмов', 'Borrows'), ('sbChk', 'Проверка', 'Check')])
s2 = section('sub', 'Вычитание в столбик', 'Column subtraction',
 bd('<p>Вычитаем тоже по разрядам, справа налево. Если сверху цифра меньше, чем снизу (например, 3 − 4), <strong>занимаем</strong> единицу у следующего разряда: там остаётся на 1 меньше, а у нас становится на 10 больше: 13 − 4 = 9. Проверка: к разности прибавляем вычитаемое — должно получиться уменьшаемое.</p>',
    '<p>We also subtract place by place, from right to left. If the top digit is smaller than the bottom one (for example 3 − 4), we <strong>borrow</strong> one from the next place: it has 1 less, and ours becomes 10 more: 13 − 4 = 9. Check: add the subtrahend to the difference — you must get the minuend.</p>')
 + formula('5203 − 1874 = 3329', 'проверка: 3329 + 1874 = 5203', 'check: 3329 + 1874 = 5203'),
 lab2)

lab3 = colmodel(3, 'УМНОЖЕНИЕ НА ОДНУ ЦИФРУ', 'MULTIPLYING BY ONE DIGIT', 'mu', 'mu', 10, 9999, 2648, 2, 9, 7, 'Число', 'Множитель', 'Number', 'Multiplier', 'muFb',
  'Умножаем каждую цифру на множитель, начиная с единиц. Лишние десятки переносим влево.',
  'We multiply each digit by the multiplier, starting with the ones. Extra tens are carried to the left.',
  [('muPr', 'Произведение', 'Product'), ('muCar', 'Переносов', 'Carries'), ('muChk', 'Проверка (приблизительно)', 'Check (approximate)')])
s3 = section('mul', 'Умножение на однозначное число', 'Multiplying by a one-digit number',
 bd('<p>2 648 · 7: 8 · 7 = 56 — пишем 6, переносим 5. 4 · 7 = 28, и ещё 5 — 33: пишем 3, переносим 3. 6 · 7 = 42 и 3 — 45: пишем 5, переносим 4. 2 · 7 = 14 и 4 — 18. Ответ: 18 536. Чтобы проверить, прикиньте: 2 648 ≈ 2 600, 2 600 · 7 = 18 200 — ответ близок.</p>',
    '<p>2,648 · 7: 8 · 7 = 56 — write 6, carry 5. 4 · 7 = 28, plus 5 — 33: write 3, carry 3. 6 · 7 = 42 and 3 — 45: write 5, carry 4. 2 · 7 = 14 and 4 — 18. Answer: 18,536. To check, estimate: 2,648 ≈ 2,600, 2,600 · 7 = 18,200 — the answer is close.</p>')
 + formula('2 648 · 7 = 18 536', 'прикидка: 2 600 · 7 = 18 200', 'estimate: 2,600 · 7 = 18,200'),
 lab3)

tasks = [
 task(1, 'Бутылки для переработки', 'Bottles for recycling', 'Одна школа собрала 3 478 бутылок, другая — 2 659. Сколько бутылок собрали вместе?', 'One school collected 3,478 bottles, another 2,659. How many bottles did they collect together?',
  '3 478 и 2 659', '3,478 and 2,659', 'Единицы: 8 + 9 = 17 — пишем 7, 1 переносим. Десятки: 7 + 5 + 1 = 13 — пишем 3, 1 переносим. Сотни: 4 + 6 + 1 = 11 — пишем 1, 1 переносим. Тысячи: 3 + 2 + 1 = 6.', 'Ones: 8 + 9 = 17 — write 7, carry 1. Tens: 7 + 5 + 1 = 13 — write 3, carry 1. Hundreds: 4 + 6 + 1 = 11 — write 1, carry 1. Thousands: 3 + 2 + 1 = 6.', '6 137 бутылок.', '6,137 bottles.', True),
 task(2, 'Остаток на складе', 'Stock in the warehouse', 'На складе было 5 203 кг муки, продали 1 874 кг. Сколько осталось?', 'A warehouse had 5,203 kg of flour and 1,874 kg were sold. How much is left?',
  '5 203 − 1 874', '5,203 − 1,874', 'Единицы: 3 − 4 нельзя; занимаем у десятков, но там 0, а у сотен 2. Берём 1 сотню: десятков 10, потом 1 десяток отдаём единицам. Получаем: единицы 13 − 4 = 9; десятки 9 − 7 = 2; сотни 1 − 8 нельзя — занимаем тысячу: 11 − 8 = 3; тысячи 4 − 1 = 3.', 'Ones: 3 − 4 is not possible; borrow from the tens, but there is 0, so go to the hundreds which has 2. Take 1 hundred: the tens become 10, then 1 ten goes to the ones. Ones: 13 − 4 = 9; tens: 9 − 7 = 2; hundreds: 1 − 8 is not possible — borrow a thousand: 11 − 8 = 3; thousands: 4 − 1 = 3.', '3 329 кг. Проверка: 3 329 + 1 874 = 5 203.', '3,329 kg. Check: 3,329 + 1,874 = 5,203.'),
 task(3, 'Умножение в столбик', 'Column multiplication', 'В одном вагоне 2 648 литров воды. Сколько в 7 таких вагонах?', 'One tank holds 2,648 litres of water. How much do 7 such tanks hold?',
  '2 648 · 7', '2,648 · 7', '8 · 7 = 56 → 6, перенос 5. 4 · 7 + 5 = 33 → 3, перенос 3. 6 · 7 + 3 = 45 → 5, перенос 4. 2 · 7 + 4 = 18.', '8 · 7 = 56 → 6, carry 5. 4 · 7 + 5 = 33 → 3, carry 3. 6 · 7 + 3 = 45 → 5, carry 4. 2 · 7 + 4 = 18.', '18 536 л.', '18,536 L.'),
 task(4, 'Проверка прикидкой', 'Checking by estimating', 'Ученик получил 4 892 + 3 975 = 7 867. Похоже ли это на правду? Проверьте округлением.', 'A pupil got 4,892 + 3,975 = 7,867. Does that look right? Check by rounding.',
  '4 892 + 3 975', '4,892 + 3,975', 'Округлим до сотен: 4 900 + 4 000 = 8 900. Ответ 7 867 далёк от 8 900 — ошибка. Верно: 8 867.', 'Round to hundreds: 4,900 + 4,000 = 8,900. The answer 7,867 is far from 8,900 — a mistake. Correct: 8,867.', 'Неверно; правильный ответ 8 867.', 'Wrong; the correct answer is 8,867.'),
 task(5, 'Перенос', 'Carrying', 'Почему при сложении 8 + 9 = 17 мы пишем 7 и «переносим 1»?', 'Why, when adding 8 + 9 = 17, do we write 7 and “carry 1”?',
  '8 + 9 = 17', '8 + 9 = 17', '17 единиц — это 1 десяток и 7 единиц. В разряде единиц помещается только одна цифра — 7. Десяток надо записать в разряде десятков, поэтому он «переезжает» туда.', '17 ones are 1 ten and 7 ones. Only one digit fits in the ones place — 7. The ten must be written in the tens place, so it “moves” there.', 'Потому что 10 единиц = 1 десяток.', 'Because 10 ones = 1 ten.'),
]
quiz = [
 qz('Сколько будет 8 + 9, и что надо перенести в следующий разряд?', '17, перенести 1', '17, перенести 7', '16, перенести 1', '17 = 1 десяток + 7 единиц.',
    'What is 8 + 9, and what is carried to the next place?', '17, carry 1', '17, carry 7', '16, carry 1', '17 = 1 ten + 7 ones.'),
 qz('Как проверить вычитание?', 'Прибавить вычитаемое к разности', 'Вычесть ещё раз', 'Умножить на 2', 'Разность + вычитаемое = уменьшаемое.',
    'How do you check a subtraction?', 'Add the subtrahend to the difference', 'Subtract again', 'Multiply by 2', 'Difference + subtrahend = minuend.'),
 qz('Чему равно 3 478 + 2 659?', '6 137', '5 137', '6 037', 'Единицы 17, десятки 13, сотни 11, тысячи 6.',
    'What is 3,478 + 2,659?', '6,137', '5,137', '6,037', 'Ones 17, tens 13, hundreds 11, thousands 6.'),
 qz('Что делают, когда сверху цифра меньше, чем снизу?', 'Занимают единицу у соседнего разряда', 'Меняют цифры местами', 'Ставят нуль', 'Один десяток = 10 единиц.',
    'What do you do when the top digit is smaller than the bottom one?', 'Borrow one from the next place', 'Swap the digits', 'Write zero', 'One ten = 10 ones.'),
 qz('Чему равно 1 000 − 1?', '999', '1 001', '990', 'Занимаем по цепочке: 10 − 1 = 9, и так три раза.',
    'What is 1,000 − 1?', '999', '1,001', '990', 'We borrow down the chain: 10 − 1 = 9, three times.'),
 qz('Чему равно 25 · 4?', '100', '90', '29', '20 · 4 = 80, 5 · 4 = 20, вместе 100.',
    'What is 25 · 4?', '100', '90', '29', '20 · 4 = 80, 5 · 4 = 20, together 100.'),
 qz('В каком порядке складывают в столбик?', 'Справа налево, начиная с единиц', 'Слева направо', 'Как хочешь', 'Перенос идёт в старший разряд, поэтому начинаем с младшего.',
    'In which order do we add in a column?', 'Right to left, starting with the ones', 'Left to right', 'Any way you like', 'The carry goes to the higher place, so we start from the lowest.'),
 qz('Прикидка: примерно сколько будет 4 892 + 3 975?', 'около 8 900', 'около 7 000', 'около 12 000', '4 900 + 4 000 = 8 900.',
    'Estimate: about how much is 4,892 + 3,975?', 'about 8,900', 'about 7,000', 'about 12,000', '4,900 + 4,000 = 8,900.'),
]
js = MJS + r'''
const T={ru:{adLabel:"Сложение в столбик по шагам",sbLabel:"Вычитание в столбик по шагам",muLabel:"Умножение в столбик по шагам",ones:"единицы",tens:"десятки",hun:"сотни",tho:"тысячи",tt:"десятки тысяч"},
 en:{adLabel:"Column addition step by step",sbLabel:"Column subtraction step by step",muLabel:"Column multiplication step by step",ones:"ones",tens:"tens",hun:"hundreds",tho:"thousands",tt:"ten-thousands"}};
function dg(n,k){return Math.floor(n/Math.pow(10,k))%10}
function nd(n){return String(n).length}
function calc(kind,a,b){const rows=[];let carry=0,res=[],marks=[],cnt=0;const N=5;
 for(let k=0;k<N;k++){let v;
  if(kind==="ad"){v=dg(a,k)+dg(b,k)+carry;res[k]=v%10;carry=Math.floor(v/10);if(carry)cnt++;marks[k+1]=carry}
  else if(kind==="sb"){v=dg(a,k)-carry-dg(b,k);if(v<0){v+=10;carry=1;cnt++}else carry=0;res[k]=v;marks[k+1]=carry}
  else{v=dg(a,k)*b+carry;res[k]=v%10;carry=Math.floor(v/10);if(carry)cnt++;marks[k+1]=carry}}
 return {res:res,marks:marks,cnt:cnt}}
function drawCol(kind,pre,svgId,fbId,sumId,carId,chkId,lbl){const t=T[lang];const a=+$(pre+"a").value;let b=+$(pre+"b").value;
 if(kind==="sb"&&b>a){b=a;$(pre+"b").value=b}
 const ans=kind==="ad"?a+b:kind==="sb"?a-b:a*b,R_=calc(kind,a,b);const len=Math.max(nd(a),kind==="mu"?1:nd(b),nd(ans));
 const s=Math.min(+$(pre+"s").value,len);const colX=k=>470-k*62;let g="";const op=kind==="ad"?"+":kind==="sb"?"−":"×";
 const bs=kind==="mu"?String(b):String(b);
 for(let k=0;k<len;k++){
  const da=k<nd(a)?String(dg(a,k)):"";g+=TX(colX(k),85,da,COL.ink,36,"middle",600);
  if(kind==="mu"){if(k===0)g+=TX(colX(0),135,bs,COL.ink,36,"middle",600)}else{const db=k<nd(b)?String(dg(b,k)):"";g+=TX(colX(k),135,db,COL.ink,36,"middle",600)}
  if(R_.marks[k]&&k>0&&k-1<s&&(kind!=="mu"||true)){g+=TX(colX(k),50,(kind==="sb"?"−":"+")+R_.marks[k],COL.a,16,"middle",600)}
  if(k<s){const show=!(k>=nd(ans)&&R_.res[k]===0);if(show)g+=TX(colX(k),200,String(R_.res[k]),COL.b,40,"middle",600)}
  g+=R(colX(k)-28,k===s-1?170:0,56,k===s-1?42:0,"none",COL.d,k===s-1?3:0)}
 g+=TX(colX(len-1)-50,135,op,COL.ink,32,"middle")+L(colX(len-1)-70,152,500,152,COL.ink,2);
 if(s>=len&&nd(ans)>len)g+=TX(colX(len),200,String(R_.res[len]),COL.b,40,"middle",600);
 const names=[t.ones,t.tens,t.hun,t.tho,t.tt];
 $(svgId).innerHTML=g;$(pre+"aOut").textContent=a;$(pre+"bOut").textContent=b;$(pre+"sOut").textContent=s+" / "+len;
 $(sumId).textContent=ans;$(carId).textContent=R_.cnt;
 $(chkId).textContent=kind==="ad"?(ans-b)+" + "+b+" = "+ans:kind==="sb"?(ans+b)+" − "+b+" = "+ans:"≈ "+(Math.round(a/100)*100*b);
 $(fbId).textContent=s===0?U("Нажмите на ползунок «Шаг»: покажем действие по разрядам.","Move the “Step” slider: we show the work place by place."):U("Шаг "+s+": разряд «"+names[s-1]+"» — цифра ответа "+R_.res[s-1]+(R_.marks[s]?(kind==="sb"?", занимаем 1.":", переносим "+R_.marks[s]+"."):"."),"Step "+s+": the “"+names[s-1]+"” place — answer digit "+R_.res[s-1]+(R_.marks[s]?(kind==="sb"?", we borrow 1.":", we carry "+R_.marks[s]+"."):"."))}
["ada","adb","ads"].forEach(id=>$(id).addEventListener("input",()=>drawCol("ad","ad","adSvg","adFb","adSum","adCar","adChk")));
["sba","sbb","sbs"].forEach(id=>$(id).addEventListener("input",()=>drawCol("sb","sb","sbSvg","sbFb","sbDif","sbBor","sbChk")));
["mua","mub","mus"].forEach(id=>$(id).addEventListener("input",()=>drawCol("mu","mu","muSvg","muFb","muPr","muCar","muChk")));
const LAB={ru:{adSvg:T.ru.adLabel,sbSvg:T.ru.sbLabel,muSvg:T.ru.muLabel},en:{adSvg:T.en.adLabel,sbSvg:T.en.sbLabel,muSvg:T.en.muLabel}};
function drawAll(){drawCol("ad","ad","adSvg","adFb","adSum","adCar","adChk");drawCol("sb","sb","sbSvg","sbFb","sbDif","sbBor","sbChk");drawCol("mu","mu","muSvg","muFb","muPr","muCar","muChk")}
'''
c = dict(n='05', slug='05-column-arithmetic.html', block='I', level_ru='ОСНОВЫ · 3–4 КЛАССЫ', level_en='BASICS · GRADES 3–4',
 title=('Действия в столбик', 'Column arithmetic'),
 desc='Глава 5 Атласа математики: сложение, вычитание и умножение многозначных чисел в столбик, перенос и заём, проверка прикидкой.',
 lead=('Как складывать, вычитать и умножать большие числа без ошибок: по разрядам, справа налево, с переносом.',
       'How to add, subtract and multiply big numbers without mistakes: place by place, right to left, with carrying.'),
 toc=[('riddle', 'Загадка', 'Puzzle'), ('add', 'Сложение', 'Addition'), ('sub', 'Вычитание', 'Subtraction'), ('mul', 'Умножение', 'Multiplication'), ('tasks', 'Задачи', 'Worked problems'), ('quiz', 'Тест', 'Quiz')],
 riddle=('<p>Две школы собирали пластиковые бутылки на переработку: одна собрала 3 478, другая 2 659. Ученик складывает в столбик и говорит: «8 плюс 9 — это 17. Семь пишу, а один… запоминаю». Учитель просит объяснить, куда же девается этот «запомненный» один.</p><p>Почему при сложении мы пишем только 7, а единицу «переносим»?</p>',
         '<p>Two schools collected plastic bottles for recycling: one collected 3,478, the other 2,659. A pupil adds them in a column and says: “8 plus 9 is 17. I write seven and… remember one.” The teacher asks where this “remembered” one goes.</p><p>Why do we write only 7 and “carry” the one?</p>'),
 hint=stdhint('Сложение в столбик', 'Column addition'),
 sections=[s1, s2, s3], tasks=tasks, quiz=quiz,
 answer_h=('Разгадка: 6 137 бутылок', 'The answer: 6,137 bottles'),
 answer=('<p>17 единиц — это не 17 «штучек», а 1 десяток и 7 единиц. В разряде единиц помещается одна цифра — 7. А десяток надо записать там, где стоят десятки, — вот зачем его «переносят». Так по очереди: 17 единиц, 13 десятков, 11 сотен и 6 тысяч дают 6 137.</p>',
         '<p>17 ones are not 17 “bits”, but 1 ten and 7 ones. Only one digit fits in the ones place — 7. The ten must be written where tens stand — that is why it is “carried”. In turn: 17 ones, 13 tens, 11 hundreds and 6 thousands give 6,137.</p>'),
 sources=[('Алгоритмы вычислений в столбик —', 'Column algorithms —', LINK('https://en.wikipedia.org/wiki/Carry_(arithmetic)', 'Wikipedia: Carry') + ', ' + LINK('https://en.wikipedia.org/wiki/Subtraction', 'Wikipedia: Subtraction')),
  ('Учебник арифметики —', 'An arithmetic textbook —', LINK('https://openstax.org/books/prealgebra-2e/pages/1-introduction', 'OpenStax Prealgebra 2e'))],
 note=stdnote('Сюжет придуман для атласа.', 'The story was invented for the atlas.'),
 prev=('04-multiply-divide.html', 'Глава 4 · Умножение и деление', 'Chapter 4 · Multiplication and division'),
 next=('06-order-of-operations.html', 'Глава 6 · Порядок действий', 'Chapter 6 · Order of operations'),
 js=js)
build(c)
