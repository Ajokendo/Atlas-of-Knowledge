# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Разряды после запятой', 'Places after the point'),
 [('r', 'x', 'Число × 1000', 'The number × 1000', 1, 9999, 1, 2345)],
 [('Запись', 'Notation'), ('Дробью', 'As a fraction'), ('Разряды', 'Places')],
 'Цифры после запятой — десятые, сотые, тысячные доли. Каждый следующий разряд в 10 раз мельче.', 'Digits after the point are tenths, hundredths, thousandths. Each next place is 10 times smaller.', ('Таблица разрядов', 'A place-value table'),
 r'''const x=v.x,ip=Math.floor(x/1000),f=x%1000,fs=String(f).padStart(3,"0"),names=[U("единицы","ones"),U("десятые","tenths"),U("сотые","hundredths"),U("тысячные","thousandths")],dg=[String(ip%10),fs[0],fs[1],fs[2]];let g="";
 for(let i=0;i<4;i++){g+=R(60+i*120,40,110,60,i?COL.bg:"#f4dfd8",COL.ink,1.5,4)+TX(115+i*120,82,dg[i],COL.ink,30,"middle",700)+TX(115+i*120,125,names[i],COL.mut,13,"middle")}
 g+=TX(305,82,",",COL.a,36,"middle",700);
 const s=ip+","+fs,gg=gcd(f,1000);return {svg:g,st:[s.replace(/0+$/,"").replace(/,$/,""),(ip*1000+f)+"/1000"+(gcd(ip*1000+f,1000)>1?" = "+(ip*1000+f)/gcd(ip*1000+f,1000)+"/"+1000/gcd(ip*1000+f,1000):""),U("целая часть "+ip+", дробная 0,"+fs,"whole part "+ip+", fractional 0,"+fs)],fb:U("Читаем: "+ip+" целых "+f+" тысячных.",ip+" and "+f+" thousandths.")}''')

m2 = M(('Сравнение и округление', 'Comparing and rounding'),
 [('r', 'x', 'Число × 1000', 'The number × 1000', 0, 9999, 1, 3476), ('s', 'to', 'Округлить до', 'Round to', ['целых', 'десятых', 'сотых'], ['ones', 'tenths', 'hundredths'], 1)],
 [('Число', 'Number'), ('Округлённое', 'Rounded'), ('Первая отброшенная цифра', 'First dropped digit')],
 'Смотрим на первую отбрасываемую цифру: 5 и больше — округляем вверх, меньше 5 — оставляем.', 'We look at the first dropped digit: 5 or more — round up; less than 5 — keep.', ('Число на числовой прямой между двумя округлениями', 'A number on the line between two roundings'),
 r'''const x=v.x/1000,st=[1,0.1,0.01][v.to],lo=Math.floor(x/st+1e-9)*st,hi=lo+st,r=(x-lo)>=st/2-1e-9?hi:lo,d=Math.round(((x-lo)/st)*10);
 const X=t=>60+(t-lo)/st*480;let g=L(60,130,540,130,COL.ink,3)+L(60,115,60,145,COL.ink,2)+L(540,115,540,145,COL.ink,2)+L(300,120,300,140,COL.mut,2)+TX(60,170,fnum(lo,2),COL.ink,15)+TX(540,170,fnum(hi,2),COL.ink,15)+TX(300,170,U("середина","midpoint"),COL.mut,12);
 g+=C(X(x),130,10,COL.a)+TX(X(x),100,fnum(x,3),COL.a,15,"middle",600)+C(X(r),130,16,"none",COL.c,3);
 return {svg:g,st:[fnum(x,3),fnum(r,2),Math.floor((x-lo)/st*10+1e-9)%10],fb:U("Число "+(r===hi?"ближе к "+fnum(hi,2):"ближе к "+fnum(lo,2))+": округляем до "+fnum(r,2)+".","The number is closer to "+(r===hi?fnum(hi,2):fnum(lo,2))+": rounding to "+fnum(r,2)+".")}''')

m3 = M(('Умножение и деление на 10, 100, 1000', 'Multiplying and dividing by 10, 100, 1000'),
 [('r', 'x', 'Число × 100', 'The number × 100', 1, 99999, 1, 345), ('s', 'k', 'Степень десяти', 'Power of ten', ['10', '100', '1000'], ['10', '100', '1000'], 1), ('s', 'op', 'Действие', 'Operation', ['умножить', 'разделить'], ['multiply', 'divide'], 0)],
 [('Результат', 'Result'), ('Запятая сдвинулась', 'The point moved'), ('Как', 'How')],
  'Умножаем на 10, 100, 1000 — запятая сдвигается вправо на 1, 2, 3 знака. Делим — влево.', 'Multiply by 10, 100, 1000 — the point moves right by 1, 2, 3 places. Divide — left.', ('Запятая и цифры', 'The point and the digits'),
 r'''const x=v.x/100,k=v.k+1,f=Math.pow(10,k),r=v.op===0?x*f:x/f,xs=fnum(x,2),dg=xs.replace(",","").replace(".","");
 let g="",pos=(xs.indexOf(",")>=0?xs.indexOf(","):xs.indexOf(".")>=0?xs.indexOf("."):xs.length);const np=pos+(v.op===0?k:-k);
 g+=TX(300,60,xs,COL.ink,26,"middle",600)+TX(300,95,"↓ "+(v.op===0?"× ":": ")+f,COL.a,18,"middle",600)+TX(300,150,fnum(r,5),COL.ink,34,"middle",700);
 return {svg:g,st:[fnum(r,5),(v.op===0?U("вправо","right"):U("влево","left"))+" "+k,v.op===0?U("запятая вправо, при нехватке цифр дописываем нули","point right, add zeros if digits run out"):U("запятая влево, спереди дописываем нули","point left, add zeros in front")],fb:U(xs+(v.op===0?" · ":" : ")+f+" = "+fnum(r,5)+".",xs+(v.op===0?" · ":" : ")+f+" = "+fnum(r,5)+".")}''')

chapter('18', '18-decimals.html', 'III', ('Десятичные дроби', 'Decimal fractions'),
 ('Как устроена запись числа с запятой, как сравнивать и округлять такие числа и как быстро умножать на 10, 100, 1000.', 'How a number with a decimal point is written, how to compare and round such numbers and how to multiply by 10, 100, 1000 quickly.'),
 ('На базаре 1 кг картофеля стоит 32,5 сома, а 1 кг моркови — 32,05 сома.\n\nЧто дороже? Многие ошибаются, потому что 32,05 «длиннее».', 'At a market 1 kg of potatoes costs 32.5 som and 1 kg of carrots costs 32.05 som.\n\nWhich is more expensive? Many people err because 32.05 looks “longer”.'),
 ('Разгадка: картофель дороже', 'The answer: potatoes are more expensive'),
 ('Сравниваем разряд за разрядом. Целые части одинаковы — 32. Десятые: у 32,5 это 5, у 32,05 это 0. 5 &gt; 0, значит 32,5 &gt; 32,05. Удобно дописать нуль: 32,50 и 32,05 — тогда сравниваются как 3250 и 3205 сотых. Длина записи ничего не решает.', 'We compare place by place. The whole parts are the same — 32. Tenths: 32.5 has 5, 32.05 has 0. 5 &gt; 0, so 32.5 &gt; 32.05. It helps to append a zero: 32.50 and 32.05 compare as 3250 and 3205 hundredths. The length of the notation decides nothing.'),
 [S('places', 'Разряды после запятой', 'Places after the point', ('Десятичная дробь — это дробь со знаменателем 10, 100, 1000…: 0,7 = 7/10, 0,07 = 7/100, 2,345 = 2345/1000. Цифры после запятой — десятые, сотые, тысячные. Приписать нуль справа в конце дробной части можно: 0,5 = 0,50.', 'A decimal fraction is a fraction with denominator 10, 100, 1000…: 0.7 = 7/10, 0.07 = 7/100, 2.345 = 2345/1000. The digits after the point are tenths, hundredths, thousandths. A zero may be appended at the end of the fractional part: 0.5 = 0.50.'),
    ('0,7 = 7/10; 0,07 = 7/100', '', '0.7 = 7/10; 0.07 = 7/100'), m1),
  S('round', 'Сравнение и округление', 'Comparing and rounding', ('Сравнивают сначала целые части, потом десятые, сотые и так далее. Округляя до нужного разряда, смотрят на следующую цифру: 0–4 — отбрасываем, 5–9 — увеличиваем предыдущую на 1. Например, 3,476 до десятых — 3,5; до сотых — 3,48.', 'We compare the whole parts first, then tenths, hundredths and so on. When rounding to a place we look at the next digit: 0–4 — drop it; 5–9 — increase the previous digit by 1. For example, 3.476 to tenths is 3.5; to hundredths 3.48.'),
    ('5 и больше — вверх', '', '5 or more — round up'), m2),
  S('shift', 'Умножение и деление на 10, 100, 1000', 'Multiplying and dividing by 10, 100, 1000', ('При умножении на 10, 100, 1000 запятая переносится вправо на 1, 2, 3 знака; при делении — влево. Если цифр не хватает, дописывают нули: 3,45 · 1000 = 3450; 3,45 : 1000 = 0,00345. Так переходят от метров к сантиметрам, от килограммов к граммам.', 'When multiplying by 10, 100, 1000 the point moves right by 1, 2, 3 places; when dividing — left. If digits run out we add zeros: 3.45 · 1000 = 3450; 3.45 : 1000 = 0.00345. This is how we go from metres to centimetres, from kilograms to grams.'),
    ('3,45 · 100 = 345', '', '3.45 · 100 = 345'), m3)],
 [TK(('Сравнить', 'Compare'), ('Сравните 0,6 и 0,58.', 'Compare 0.6 and 0.58.'), '0,60 и 0,58', 'Дописываем нуль: 0,60 &gt; 0,58.', ('0,6 &gt; 0,58.', '0.6 &gt; 0.58.')),
  TK(('В дробь', 'To a fraction'), ('Запишите 0,35 обыкновенной дробью.', 'Write 0.35 as a common fraction.'), '35/100', '35/100 : 5 = 7/20.', '7/20.'),
  TK(('Округлить', 'Round'), ('Округлите 7,846 до сотых и до десятых.', 'Round 7.846 to hundredths and tenths.'), '7,846', 'До сотых: третья цифра 6 ≥ 5 → 7,85. До десятых: вторая цифра 4 &lt; 5 → 7,8.', ('7,85 и 7,8.', '7.85 and 7.8.')),
  TK(('Сдвиг запятой', 'Shifting the point'), ('Найдите 2,7 · 100 и 45 : 1000.', 'Find 2.7 · 100 and 45 : 1000.'), '2,7 · 100; 45 : 1000', 'Вправо на 2 знака: 270. Влево на 3: 0,045.', '270; 0,045.'),
  TK(('Покупка', 'A purchase'), ('Килограмм яблок стоит 85,5 сома. Сколько стоят 2 кг?', 'A kilogram of apples costs 85.5 som. How much do 2 kg cost?'), '85,5 · 2', '85,5 · 2 = 171.', ('171 сом.', '171 som.'))],
 [Q('0,07 =', '0.07 =', '7/100', '7/10', '70/100', ('Два знака после запятой — сотые.', 'Two places after the point — hundredths.')),
  Q('Что больше?', 'Which is greater?', '0,5', '0,45', ('Равны', 'Equal'), ('0,50 &gt; 0,45.', '0.50 &gt; 0.45.')),
  Q('3,456 округлить до сотых', 'Round 3.456 to hundredths', '3,46', '3,45', '3,5', ('Третья цифра 6.', 'The third digit is 6.')),
  Q('2,5 · 10 =', '2.5 · 10 =', '25', '0,25', '250', ('Запятая вправо на 1 знак.', 'The point moves right by 1.')),
  Q('45 : 100 =', '45 : 100 =', '0,45', '4,5', '4500', ('Запятая влево на 2 знака.', 'The point moves left by 2.')),
  Q('Равно ли 0,5 числу 0,50?', 'Is 0.5 equal to 0.50?', ('Да', 'Yes'), ('Нет', 'No'), ('Только при округлении', 'Only after rounding'), ('Нуль в конце дробной части ничего не меняет.', 'A trailing zero changes nothing.')),
  Q('3/5 в виде десятичной дроби', '3/5 as a decimal', '0,6', '0,35', '3,5', ('3/5 = 6/10.', '3/5 = 6/10.')),
  Q('Какая цифра стоит в разряде сотых числа 4,317?', 'Which digit is in the hundredths place of 4.317?', '1', '3', '7', ('4, затем десятые 3, сотые 1, тысячные 7.', '4, then tenths 3, hundredths 1, thousandths 7.'))],
 src=[('Wikipedia: Decimal', 'https://en.wikipedia.org/wiki/Decimal'), ('Wikipedia: Rounding', 'https://en.wikipedia.org/wiki/Rounding')],
 note=('Цены и сюжет про базар придуманы для атласа.', 'The prices and the market story are invented for the atlas.'))
