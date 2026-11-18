# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Единицы длины', 'Units of length'),
 [('s', 'u', 'Единица', 'Unit', ['миллиметры', 'сантиметры', 'дециметры', 'метры', 'километры'], ['millimetres', 'centimetres', 'decimetres', 'metres', 'kilometres'], 3), ('r', 'x', 'Значение', 'Value', 1, 100, 1, 3)],
 [('В метрах', 'In metres'), ('В сантиметрах', 'In centimetres'), ('В километрах', 'In kilometres')],
 '1 км = 1000 м, 1 м = 10 дм = 100 см = 1000 мм. Выберите единицу и число — остальные значения найдутся сами.', '1 km = 1000 m, 1 m = 10 dm = 100 cm = 1000 mm. Choose a unit and a number — the other values appear by themselves.', ('Одна длина в разных единицах', 'One length in different units'),
 r'''const f=[0.001,0.01,0.1,1,1000],m=v.x*f[v.u];const show=x=>{if(Math.abs(x-Math.round(x))<1e-9)return num(Math.round(x));return fnum(x,6)};
 const nm=U(["мм","см","дм","м","км"],["mm","cm","dm","m","km"]);let g="";
 for(let i=0;i<5;i++){const y=40+i*40,val=m/f[i],hit=i===v.u;g+=R(60,y-24,480,34,hit?"#f4dfd8":COL.bg,hit?COL.a:COL.line,hit?2:1,4)+TX(80,y-2,nm[i],COL.mut,16,"start",600)+TX(520,y-2,show(val),COL.ink,18,"end",hit?700:400)}
 return {svg:g,st:[show(m)+U(" м"," m"),show(m*100)+U(" см"," cm"),show(m/1000)+U(" км"," km")],fb:U("Чем крупнее единица, тем меньше число: "+v.x+" "+nm[v.u]+" = "+show(m)+" м.",
 "The bigger the unit, the smaller the number: "+v.x+" "+nm[v.u]+" = "+show(m)+" m.")}''')

m2 = M(('Время', 'Time'),
 [('r', 'h', 'Час начала', 'Start hour', 0, 23, 1, 8), ('r', 'mi', 'Минуты начала', 'Start minutes', 0, 55, 5, 30), ('r', 'd', 'Длительность (мин)', 'Duration (min)', 5, 300, 5, 45)],
 [('Начало', 'Start'), ('Конец', 'End'), ('Длительность', 'Duration'), ('День', 'Day')],
 'В часе 60 минут, в сутках 24 часа. Если время перевалило за 24:00, наступил следующий день.', 'An hour has 60 minutes and a day has 24 hours. If the time passes 24:00, the next day has begun.', ('Два циферблата: начало и конец', 'Two clock faces: start and end'),
 r'''const s=v.h*60+v.mi,e=s+v.d,eh=Math.floor(e/60)%24,em=e%60,pad=n=>(n<10?"0":"")+n;let g="";
 const clock=(cx,h,m,col)=>{let c=C(cx,120,85,"#fff",COL.ink,3);for(let i=0;i<12;i++){const a=i*Math.PI/6;c+=L(cx+75*Math.sin(a),120-75*Math.cos(a),cx+85*Math.sin(a),120-85*Math.cos(a),COL.ink,2)}
  const ah=((h%12)+m/60)*Math.PI/6,am=m*Math.PI/30;c+=L(cx,120,cx+48*Math.sin(ah),120-48*Math.cos(ah),col,6)+L(cx,120,cx+72*Math.sin(am),120-72*Math.cos(am),col,3)+C(cx,120,4,COL.ink);return c};
 g+=clock(150,v.h,v.mi,COL.a)+clock(450,eh,em,COL.b)+TX(150,235,pad(v.h)+":"+pad(v.mi),COL.a,22,"middle",600)+TX(450,235,pad(eh)+":"+pad(em),COL.b,22,"middle",600)+arrow(260,120,340,120,COL.mut,3)+TX(300,105,"+"+v.d+U(" мин"," min"),COL.mut,13);
 const hh=Math.floor(v.d/60),mm=v.d%60,next=e>=1440;
 return {svg:g,st:[pad(v.h)+":"+pad(v.mi),pad(eh)+":"+pad(em),hh+U(" ч "," h ")+mm+U(" мин"," min"),next?U("следующий","next day"):U("тот же","same day")],
 fb:U("К "+pad(v.h)+":"+pad(v.mi)+" прибавляем "+hh+" ч "+mm+" мин — получаем "+pad(eh)+":"+pad(em)+".","To "+pad(v.h)+":"+pad(v.mi)+" add "+hh+" h "+mm+" min — we get "+pad(eh)+":"+pad(em)+".")}''')

m3 = M(('Деньги: сомы', 'Money: soms'),
 [('r', 'a', 'Купюр по 20 сом', 'Notes of 20 soms', 0, 9, 1, 2), ('r', 'b', 'Купюр по 50 сом', 'Notes of 50 soms', 0, 9, 1, 1), ('r', 'c', 'Купюр по 100 сом', 'Notes of 100 soms', 0, 9, 1, 2), ('r', 'd', 'Купюр по 200 сом', 'Notes of 200 soms', 0, 9, 1, 0)],
 [('Всего денег', 'Total money'), ('Всего купюр', 'Number of notes'), ('Хватит на покупку за 350 сом?', 'Enough for a 350-som purchase?')],
 'Считаем: количество купюр умножаем на номинал и складываем.', 'We multiply the number of notes by the value and add.', ('Стопки купюр разного достоинства', 'Stacks of notes of different values'),
 r'''const vals=[20,50,100,200],cnt=[v.a,v.b,v.c,v.d],cols=["#c9b48f","#9ec3b0","#b9a7d9","#e0a28f"];let g="",tot=0,n=0;
 for(let i=0;i<4;i++){const x=45+i*140;tot+=vals[i]*cnt[i];n+=cnt[i];for(let j=0;j<cnt[i];j++)g+=R(x,185-j*17,110,15,cols[i],COL.ink,1.2,3)+TX(x+55,185-j*17+12,String(vals[i]),COL.ink,11);g+=TX(x+55,212,vals[i]+" × "+cnt[i]+" = "+vals[i]*cnt[i],COL.ink,13);}
 return {svg:g,st:[tot+U(" сом"," soms"),n,tot>=350?U("да","yes"):U("нет, не хватает "+(350-tot),"no, short by "+(350-tot))],fb:U("Складываем: "+vals.map((x,i)=>x*cnt[i]).join(" + ")+" = "+tot+" сом.","Adding: "+vals.map((x,i)=>x*cnt[i]).join(" + ")+" = "+tot+" soms.")}''')

chapter('10', '10-quantities.html', 'II', ('Длина, масса, время, деньги', 'Length, mass, time, money'),
 ('Как не запутаться в единицах: километры и метры, часы и минуты, сомы.', 'How not to get tangled in units: kilometres and metres, hours and minutes, soms.'),
 ('Айдай живёт в 1 км 300 м от школы, а Бек — в 1200 м.\n\nКто живёт дальше и на сколько метров?', 'Aidai lives 1 km 300 m from school and Bek lives 1200 m away.\n\nWho lives farther and by how many metres?'),
 ('Разгадка: Айдай, на 100 м', 'The answer: Aidai, by 100 m'),
 ('Сравнивать можно только числа в одинаковых единицах. 1 км 300 м = 1000 м + 300 м = 1300 м. Теперь 1300 м &gt; 1200 м, и разница 1300 − 1200 = 100 м. Привычка: сначала привести всё к одной единице, потом считать.', 'We can only compare numbers in the same units. 1 km 300 m = 1000 m + 300 m = 1300 m. Now 1300 m &gt; 1200 m and the difference is 1300 − 1200 = 100 m. The habit: first bring everything to one unit, then calculate.'),
 [S('len', 'Единицы длины', 'Units of length', ('Длину измеряют в миллиметрах, сантиметрах, дециметрах, метрах и километрах. Каждая следующая единица в 10 (дальше в 100, в 1000) раз крупнее. Чтобы перейти к более мелкой единице, число <strong>умножают</strong>; к более крупной — <strong>делят</strong>.\n\nМассу измеряют в граммах, килограммах и тоннах: 1 кг = 1000 г, 1 т = 1000 кг.', 'Length is measured in millimetres, centimetres, decimetres, metres and kilometres. Each next unit is 10 (then 100, 1000) times bigger. To go to a smaller unit we <strong>multiply</strong> the number; to a bigger unit we <strong>divide</strong>.\n\nMass is measured in grams, kilograms and tonnes: 1 kg = 1000 g, 1 t = 1000 kg.'),
    ('1 км = 1000 м', '1 м = 100 см = 1000 мм', '1 km = 1000 m; 1 m = 100 cm = 1000 mm'), m1),
  S('time', 'Время', 'Time', ('1 час = 60 минут, 1 минута = 60 секунд, 1 сутки = 24 часа. Чтобы найти конец события, к началу прибавляют длительность. Если минут стало 60 и больше, 60 минут превращаются в час: 8:30 + 45 мин = 8 ч 75 мин = 9:15.', '1 hour = 60 minutes, 1 minute = 60 seconds, 1 day = 24 hours. To find the end of an event we add the duration to the start. If minutes reach 60 or more, 60 minutes turn into an hour: 8:30 + 45 min = 8 h 75 min = 9:15.'),
    ('8:30 + 45 мин = 9:15', '30 + 45 = 75 мин = 1 ч 15 мин', '30 + 45 = 75 min = 1 h 15 min'), m2),
  S('money', 'Деньги', 'Money', ('Деньги Кыргызстана — <strong>сом</strong>. Есть купюры в 20, 50, 100, 200, 500, 1000, 2000 и 5000 сомов. Чтобы узнать сумму, умножаем число купюр на номинал и складываем. Чтобы узнать сдачу — вычитаем стоимость из внесённой суммы.', 'The money of Kyrgyzstan is the <strong>som</strong>. There are notes of 20, 50, 100, 200, 500, 1000, 2000 and 5000 soms. To find the total we multiply the number of notes by the value and add. To find the change we subtract the cost from the money handed over.'),
    ('2 · 20 + 1 · 50 + 2 · 100 = 290', 'сумма = число купюр · номинал', 'total = number of notes · value'), m3)],
 [TK(('Километры в метры', 'Kilometres to metres'), ('Переведите 2 км 350 м в метры.', 'Convert 2 km 350 m to metres.'), '2 км 350 м', '2 км = 2000 м, 2000 + 350 = 2350.', ('2350 м.', '2350 m.')),
  TK(('Масса', 'Mass'), ('Мешок муки весит 25 кг. Сколько граммов в 3 таких мешках?', 'A sack of flour weighs 25 kg. How many grams are in 3 such sacks?'), '25 кг · 3', '25 · 3 = 75 кг = 75 · 1000 = 75 000 г.', ('75 000 г.', '75,000 g.')),
  TK(('Конец урока', 'End of the lesson'), ('Урок начался в 8:30 и идёт 45 минут. Когда он закончится?', 'A lesson starts at 8:30 and lasts 45 minutes. When does it end?'), '8:30 + 45 мин', '30 + 45 = 75 мин = 1 ч 15 мин. 8 ч + 1 ч 15 мин = 9:15.', '9:15.'),
  TK(('Сколько длилось', 'How long it lasted'), ('Автобус вышел в 7:50 и приехал в 10:20. Сколько времени он был в пути?', 'A bus left at 7:50 and arrived at 10:20. How long was it on the road?'), '7:50 → 10:20', 'До 8:00 — 10 мин, от 8:00 до 10:00 — 2 ч, до 10:20 — ещё 20 мин: 10 + 120 + 20 = 150 мин.', ('2 ч 30 мин.', '2 h 30 min.')),
  TK(('Сдача', 'Change'), ('Хлеб стоит 35 сом. Сколько сдачи со 100 сомов, если купить 2 хлеба?', 'A loaf costs 35 soms. How much change from 100 soms for 2 loaves?'), '2 · 35 сом, 100 сом', '2 · 35 = 70, 100 − 70 = 30.', ('30 сом.', '30 soms.'))],
 [Q('Сколько метров в 1 км?', 'How many metres are in 1 km?', '1000', '100', '10', ('Приставка «кило» значит 1000.', 'The prefix “kilo” means 1000.')),
  Q('Сколько сантиметров в 1 м?', 'How many centimetres are in 1 m?', '100', '10', '1000', '1 м = 100 см.'),
  Q('Сколько минут в 2,5 часах (2 ч 30 мин)?', 'How many minutes are in 2 h 30 min?', '150', '230', '130', '2 · 60 + 30 = 150.'),
  Q('8:30 + 45 мин =', '8:30 + 45 min =', '9:15', '8:75', '9:30', ('75 минут = 1 ч 15 мин.', '75 minutes = 1 h 15 min.')),
  Q('Сколько граммов в 3 кг?', 'How many grams are in 3 kg?', '3000', '300', '30', '3 · 1000 = 3000.'),
  Q('Что больше: 1 км 100 м или 1050 м?', 'Which is more: 1 km 100 m or 1050 m?', ('1 км 100 м', '1 km 100 m'), ('1050 м', '1050 m'), ('Они равны', 'They are equal'), ('1 км 100 м = 1100 м &gt; 1050 м.', '1 km 100 m = 1100 m &gt; 1050 m.')),
  Q('Сколько сдачи со 100 сом, если купили на 64 сома?', 'How much change from 100 soms for 64 soms of goods?', '36', '46', '164', '100 − 64 = 36.'),
  Q('Как перейти от метров к сантиметрам?', 'How do you go from metres to centimetres?', ('Умножить на 100', 'Multiply by 100'), ('Разделить на 100', 'Divide by 100'), ('Прибавить 100', 'Add 100'), ('Сантиметр мельче, значит чисел больше.', 'A centimetre is smaller, so the number is greater.'))],
 src=[('Wikipedia: International System of Units', 'https://en.wikipedia.org/wiki/International_System_of_Units'), ('Wikipedia: Kyrgyzstani som', 'https://en.wikipedia.org/wiki/Kyrgyzstani_som')])
