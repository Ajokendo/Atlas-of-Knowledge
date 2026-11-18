# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Синус: амплитуда, период, сдвиг', 'Sine: amplitude, period, shift'),
 [('r', 'A', 'Амплитуда A', 'Amplitude A', 0.5, 4, 0.5, 2), ('r', 'B', 'Частота B', 'Frequency B', 0.5, 3, 0.5, 1), ('r', 'c', 'Сдвиг вправо c', 'Shift right c', -3, 3, 0.5, 0), ('r', 'd', 'Сдвиг вверх d', 'Shift up d', -3, 3, 0.5, 0)],
 [('Формула', 'Formula'), ('Период 2π/B', 'Period 2π/B'), ('Наибольшее и наименьшее', 'Maximum and minimum')],
 'В y = A·sin(B(x − c)) + d амплитуда A — высота «волны», период T = 2π/B — длина одного колебания, c и d — сдвиги.', 'In y = A·sin(B(x − c)) + d the amplitude A is the height of the “wave”, the period T = 2π/B is the length of one oscillation, c and d are shifts.', ('График синусоиды', 'A sinusoid'),
 r'''const G=Gr({x0:-7,x1:7,y0:-7,y1:7,L:80,T:10,W:460,H:210});let g=G.grid(Math.PI/2,1,false);
 g+=G.fn(x=>v.A*Math.sin(v.B*(x-v.c))+v.d,COL.a,3.5);const T=2*Math.PI/v.B;return {svg:g,st:["y = "+(v.A===1?"":v.A+"·")+"sin("+(v.B===1?"":v.B)+(v.c===0?"x":"(x "+(v.c<0?"+ "+(-v.c):"− "+v.c)+")")+")"+(v.d===0?"":(v.d<0?" − "+(-v.d):" + "+v.d)),fnum(T,3)+" ≈ "+fnum(T/Math.PI,2)+"π",fnum(v.d+v.A,1)+" и "+fnum(v.d-v.A,1)],fb:U("Чем больше B, тем чаще колебания (период короче).","The larger B, the more frequent the oscillations (a shorter period).")}''', '0 0 600 250')

m2 = M(('Синус, косинус, тангенс', 'Sine, cosine, tangent'),
 [('s', 'f', 'Функция', 'Function', ['sin x', 'cos x', 'tan x'], ['sin x', 'cos x', 'tan x'], 0), ('r', 'x', 'Угол x (рад)', 'Angle x (rad)', -6.2, 6.2, 0.1, 1)],
 [('Значение', 'Value'), ('Период', 'Period'), ('Область значений', 'Range')],
 'Синус и косинус — волны с периодом 2π и значениями от −1 до 1; тангенс — с периодом π, не определён в точках π/2 + πk.', 'Sine and cosine are waves with period 2π and values between −1 and 1; tangent has period π and has no value at π/2 + πk.', ('Графики тригонометрических функций', 'Graphs of trigonometric functions'),
 r'''const F=[Math.sin,Math.cos,Math.tan][v.f],G=Gr({x0:-7,x1:7,y0:-3,y1:3,L:80,T:10,W:460,H:210});let g=G.grid(1,1)+G.fn(F,COL.a,3.5,-7,7);const y=F(v.x);if(isFinite(y)&&Math.abs(y)<3)g+=G.seg(v.x,0,v.x,y,COL.mut,1.5)+G.pt(v.x,y,COL.b,8);
 return {svg:g,st:[Math.abs(y)>1e3?U("не определено","undefined"):fnum(y,4),["2π ≈ 6,28","2π ≈ 6,28","π ≈ 3,14"][v.f],["[−1; 1]","[−1; 1]",U("все числа","all numbers")][v.f]],fb:U("Чётность: cos x чётна (симметрична относительно оси y), sin x и tan x нечётны.","Parity: cos x is even (symmetric about the y-axis); sin x and tan x are odd.")}''', '0 0 600 250')

m3 = M(('Сезонные колебания (условная модель)', 'Seasonal oscillations (an illustrative model)'),
 [('r', 'mean', 'Средняя температура, °C', 'Mean temperature, °C', -5, 20, 1, 8), ('r', 'amp', 'Размах колебаний, °C', 'Amplitude, °C', 2, 20, 1, 14), ('r', 'mo', 'Месяц', 'Month', 1, 12, 1, 7)],
 [('Температура в выбранном месяце', 'Temperature in the chosen month'), ('Самый тёплый месяц', 'The warmest month'), ('Самый холодный месяц', 'The coldest month')],
 'Периодические процессы описывают синусоидой: T(m) = среднее + амплитуда · sin(2π(m − 4)/12). Параметры условные, это не данные наблюдений.', 'Periodic processes are described by a sinusoid: T(m) = mean + amplitude · sin(2π(m − 4)/12). The parameters are illustrative, not observations.', ('Годовой ход температуры (условная модель)', 'The annual course of temperature (illustrative model)'),
 r'''const T=m=>v.mean+v.amp*Math.sin(2*Math.PI*(m-4)/12),G=Gr({x0:1,x1:13,y0:-30,y1:40,L:80,T:10,W:460,H:210});let g=G.grid(1,10)+G.fn(T,COL.b,3,1,13);for(let m=1;m<=12;m++)g+=G.pt(m,T(m),m===v.mo?COL.a:COL.b,m===v.mo?8:4);
 return {svg:g,st:[fnum(T(v.mo),1)+" °C",U("июль (7)","July (7)")+": "+fnum(v.mean+v.amp,1)+" °C",U("январь (1)","January (1)")+": "+fnum(v.mean-v.amp,1)+" °C"],fb:U("Период — 12 месяцев; амплитуда — половина разности лета и зимы.","The period is 12 months; the amplitude is half the difference between summer and winter.")}''', '0 0 600 250')

chapter('50', '50-trig-functions.html', 'VII', ('Тригонометрические функции и графики', 'Trigonometric functions and graphs'),
 ('Как выглядят синус, косинус и тангенс как функции и почему ими описывают всё, что повторяется: волны, колебания, времена года.', 'What sine, cosine and tangent look like as functions and why they describe everything that repeats: waves, oscillations, seasons.'),
 ('Весной, летом, осенью, зимой температура воздуха в горной долине идёт «волной»: тёплые месяцы сменяются холодными и снова тёплыми.\n\nКакая функция подходит для такой повторяющейся зависимости?', 'Through spring, summer, autumn and winter the air temperature in a mountain valley goes in a “wave”: warm months give way to cold and then warm again.\n\nWhich function suits such a repeating dependence?'),
 ('Разгадка: синусоида', 'The answer: a sinusoid'),
 ('Годовой ход температуры повторяется каждые 12 месяцев — такие зависимости называют периодическими. Простейшая периодическая функция — синус. Модель T(m) = среднее + амплитуда · sin(2π(m − 4)/12) описывает «волну» с периодом 12 месяцев; подбирая среднее и амплитуду, её можно приблизить к реальному климату. Числа в модели условные.', 'The annual course of temperature repeats every 12 months — such dependences are called periodic. The simplest periodic function is the sine. The model T(m) = mean + amplitude · sin(2π(m − 4)/12) describes a “wave” with period 12 months; by choosing the mean and amplitude it can be fitted to a real climate. The numbers in the model are illustrative.'),
 [S('sin', 'Синусоида', 'The sinusoid', ('График <strong>y = sin x</strong> — волна с периодом 2π, значения от −1 до 1. <strong>y = A·sin(B(x − c)) + d</strong>: A — амплитуда, период T = 2π/B, c — сдвиг по x, d — по y. Нули синуса: x = πk; максимумы в π/2 + 2πk.', 'The graph of <strong>y = sin x</strong> is a wave with period 2π and values between −1 and 1. <strong>y = A·sin(B(x − c)) + d</strong>: A is the amplitude, the period T = 2π/B, c is the x-shift, d the y-shift. The zeros of sine: x = πk; maxima at π/2 + 2πk.'),
    ('T = 2π/B', '', 'T = 2π/B'), m1),
  S('three', 'Косинус и тангенс', 'Cosine and tangent', ('<strong>y = cos x</strong> — тот же график, сдвинутый на π/2 влево: cos x = sin(x + π/2). <strong>y = tan x = sin x / cos x</strong> имеет период π и не определён там, где cos x = 0: x = π/2 + πk (вертикальные асимптоты). Чётность: cos x — чётная функция, sin x и tan x — нечётные.', '<strong>y = cos x</strong> is the same graph shifted π/2 to the left: cos x = sin(x + π/2). <strong>y = tan x = sin x / cos x</strong> has period π and is undefined where cos x = 0: x = π/2 + πk (vertical asymptotes). Parity: cos x is an even function, sin x and tan x are odd.'),
    ('tan x = sin x / cos x', '', 'tan x = sin x / cos x'), m2),
  S('use', 'Применение', 'Applications', ('Синусоиды описывают звуковые и световые волны, переменный ток, приливы, колебания маятника, смену времён года. Любой периодический сигнал можно составить из синусоид (идея разложения Фурье).', 'Sinusoids describe sound and light waves, alternating current, tides, a pendulum’s swing and the change of seasons. Any periodic signal can be built from sinusoids (the idea of the Fourier decomposition).'),
    ('T(m) = a + A·sin(2π(m − m₀)/12)', '', 'T(m) = a + A·sin(2π(m − m₀)/12)'), m3)],
 [TK(('Период', 'Period'), ('Найдите период y = sin 2x.', 'Find the period of y = sin 2x.'), 'T = 2π/B', 'B = 2, T = π.', 'π.'),
  TK(('Амплитуда', 'Amplitude'), ('Какая амплитуда у y = 3 sin x + 1? Каков диапазон?', 'What is the amplitude of y = 3 sin x + 1? What is the range?'), '', 'A = 3; значения от 1 − 3 = −2 до 1 + 3 = 4.', ('3; [−2; 4].', '3; [−2; 4].')),
  TK(('Значение', 'Value'), ('Найдите cos π и sin(π/2).', 'Find cos π and sin(π/2).'), '', '−1 и 1.', '−1; 1.'),
  TK(('Нули', 'Zeros'), ('В каких точках sin x = 0 на [0; 2π]?', 'Where is sin x = 0 on [0; 2π]?'), '', 'x = 0, π, 2π.', '0, π, 2π.'),
  TK(('Тангенс', 'Tangent'), ('Найдите tan(π/4).', 'Find tan(π/4).'), 'sin/cos', '(√2/2)/(√2/2) = 1.', '1.')],
 [Q('Период y = sin x', 'The period of y = sin x', '2π', 'π', '1', ('Полный оборот.', 'A full turn.')),
  Q('Наибольшее значение cos x', 'The greatest value of cos x', '1', 'π', '2', ('Диапазон [−1; 1].', 'Range [−1; 1].')),
  Q('Период y = tan x', 'The period of y = tan x', 'π', '2π', 'π/2', ('tan(x + π) = tan x.', 'tan(x + π) = tan x.')),
  Q('Чётная функция', 'The even function', 'cos x', 'sin x', 'tan x', ('cos(−x) = cos x.', 'cos(−x) = cos x.')),
  Q('Амплитуда y = −4 sin x', 'The amplitude of y = −4 sin x', '4', '−4', '1', ('Амплитуда положительна: |A|.', 'The amplitude is positive: |A|.')),
  Q('Тангенс не определён при', 'Tangent is undefined at', 'x = π/2', 'x = 0', 'x = π', ('cos(π/2) = 0.', 'cos(π/2) = 0.')),
  Q('Период y = sin(x/2)', 'The period of y = sin(x/2)', '4π', 'π', '2π', ('2π : ½.', '2π : ½.')),
  Q('y = sin x + 2 — это сдвиг', 'y = sin x + 2 is a shift', ('вверх на 2', 'up by 2'), ('вправо на 2', 'right by 2'), ('вниз на 2', 'down by 2'), ('К значению прибавили 2.', '2 was added to the value.'))],
 src=[('Wikipedia: Trigonometric functions', 'https://en.wikipedia.org/wiki/Trigonometric_functions'), ('Wikipedia: Sine wave', 'https://en.wikipedia.org/wiki/Sine_wave')],
 note=('Климатическая модель условная; параметры не отражают данных наблюдений.', 'The climate model is illustrative; its parameters do not reflect observations.'))
