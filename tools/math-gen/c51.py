# -*- coding: utf-8 -*-
from gen2 import *

m1 = M(('Основное тождество', 'The basic identity'),
 [('r', 'a', 'Угол, °', 'Angle, °', 0, 360, 5, 40)],
 [('sin²α', 'sin²α'), ('cos²α', 'cos²α'), ('Сумма', 'The sum')],
 'Для любого угла квадраты координат точки на единичной окружности в сумме дают 1 — это теорема Пифагора для радиуса, равного 1.', 'For any angle the squares of the coordinates of a point on the unit circle add to 1 — the Pythagorean theorem for a radius equal to 1.', ('Квадраты синуса и косинуса', 'Squares of sine and cosine'),
 r'''const a=deg(v.a),s2=Math.pow(Math.sin(a),2),c2=Math.pow(Math.cos(a),2);let g=R(60,40,480*s2+0.01,40,COL.a,COL.ink,1.5,2)+R(60+480*s2,40,480*c2+0.01,40,COL.b,COL.ink,1.5,2)+TX(60+240*s2,66,"sin²",COL.bg,14,"middle",700)+TX(60+480*s2+240*c2,66,"cos²",COL.bg,14,"middle",700)+R(60,100,480,24,"none",COL.ink,2,2)+TX(300,150,fnum(s2,3)+" + "+fnum(c2,3)+" = 1",COL.ink,22,"middle",700);
 return {svg:g,st:[fnum(s2,4),fnum(c2,4),fnum(s2+c2,4)],fb:U("Полоса всегда заполнена целиком: часть синуса и часть косинуса дополняют друг друга до 1.","The bar is always filled: the sine part and the cosine part complete each other to 1.")}''', '0 0 600 170')

m2 = M(('Формулы сложения', 'Addition formulas'),
 [('r', 'a', 'Угол α, °', 'Angle α, °', 0, 180, 5, 50), ('r', 'b', 'Угол β, °', 'Angle β, °', 0, 180, 5, 25)],
 [('sin(α + β) напрямую', 'sin(α + β) directly'), ('sin α cos β + cos α sin β', 'sin α cos β + cos α sin β'), ('cos(α + β) = cos α cos β − sin α sin β', 'cos(α + β) = cos α cos β − sin α sin β')],
 'Синус суммы нельзя заменить суммой синусов. Правильная формула — перекрёстная. Проверьте равенство на любых углах.', 'The sine of a sum cannot be replaced by the sum of sines. The right formula is cross-wise. Check the equality at any angles.', ('Угол α + β на единичной окружности', 'The angle α + β on the unit circle'),
 r'''const a=deg(v.a),b=deg(v.b),R0=85,cx=300,cy=110;let g=L(cx-110,cy,cx+110,cy,COL.mut,1.5)+L(cx,cy-100,cx,cy+100,COL.mut,1.5)+C(cx,cy,R0,"none",COL.ink,2.5);
 [[a,COL.a],[a+b,COL.b]].forEach(p=>g+=L(cx,cy,cx+R0*Math.cos(p[0]),cy-R0*Math.sin(p[0]),p[1],3)+C(cx+R0*Math.cos(p[0]),cy-R0*Math.sin(p[0]),6,p[1]));
 const d=Math.sin(a+b),f=Math.sin(a)*Math.cos(b)+Math.cos(a)*Math.sin(b),dc=Math.cos(a+b),fc=Math.cos(a)*Math.cos(b)-Math.sin(a)*Math.sin(b);
 return {svg:g,st:[fnum(d,5),fnum(f,5),fnum(dc,5)+" = "+fnum(fc,5)],fb:U("Сумма sin α + sin β = "+fnum(Math.sin(a)+Math.sin(b),4)+" не равна sin(α + β) = "+fnum(d,4)+".","The sum sin α + sin β = "+fnum(Math.sin(a)+Math.sin(b),4)+" does not equal sin(α + β) = "+fnum(d,4)+".")}''', '0 0 600 225')

m3 = M(('Двойной угол', 'The double angle'),
 [('r', 'a', 'Угол α, °', 'Angle α, °', 0, 180, 5, 35)],
 [('sin 2α', 'sin 2α'), ('2·sin α·cos α', '2·sin α·cos α'), ('cos 2α = cos²α − sin²α', 'cos 2α = cos²α − sin²α')],
 'Формулы двойного угла — частный случай формул сложения при β = α: sin 2α = 2 sin α cos α; cos 2α = cos²α − sin²α.', 'The double-angle formulas are the special case of addition formulas at β = α: sin 2α = 2 sin α cos α; cos 2α = cos²α − sin²α.', ('Графики sin 2x и 2 sin x cos x', 'Graphs of sin 2x and 2 sin x cos x'),
 r'''const a=deg(v.a),G=Gr({x0:0,x1:Math.PI*2,y0:-1.3,y1:1.3,L:80,T:10,W:460,H:210});let g=G.grid(Math.PI/2,0.5,false)+G.fn(x=>Math.sin(2*x),COL.a,5,0,Math.PI*2)+G.fn(x=>2*Math.sin(x)*Math.cos(x),COL.b,2,0,Math.PI*2,true)+G.pt(a,Math.sin(2*a),COL.c,8);
 return {svg:g,st:[fnum(Math.sin(2*a),5),fnum(2*Math.sin(a)*Math.cos(a),5),fnum(Math.cos(2*a),4)+" = "+fnum(Math.pow(Math.cos(a),2)-Math.pow(Math.sin(a),2),4)],fb:U("Графики совпадают — это тождество, а не уравнение.","The graphs coincide — it is an identity, not an equation.")}''', '0 0 600 250')

chapter('51', '51-trig-identities.html', 'VII', ('Формулы тригонометрии', 'Trigonometric identities'),
 ('Основное тождество, формулы сложения и двойного угла: откуда они берутся и как ими пользоваться.', 'The basic identity, addition and double-angle formulas: where they come from and how to use them.'),
 ('Зная, что sin 30° = 1/2 и cos 30° = √3/2, можно ли без калькулятора найти sin 60°?', 'Knowing that sin 30° = 1/2 and cos 30° = √3/2, can we find sin 60° without a calculator?'),
 ('Разгадка: √3/2', 'The answer: √3/2'),
 ('Да, по формуле двойного угла: sin 60° = sin(2 · 30°) = 2 · sin 30° · cos 30° = 2 · (1/2) · (√3/2) = √3/2 ≈ 0,866. Тригонометрические формулы связывают значения функций в разных точках, поэтому из небольшого набора известных значений получают много новых.', 'Yes, by the double-angle formula: sin 60° = sin(2 · 30°) = 2 · sin 30° · cos 30° = 2 · (1/2) · (√3/2) = √3/2 ≈ 0.866. Trigonometric formulas link values of the functions at different points, so from a small set of known values we get many new ones.'),
 [S('basic', 'Основное тождество', 'The basic identity', ('<strong>sin²α + cos²α = 1</strong> — следствие теоремы Пифагора на единичной окружности. Из него находят одну функцию по другой: если sin α = 0,6 и α острый, то cos α = √(1 − 0,36) = 0,8. Также tan α = sin α / cos α и 1 + tan²α = 1/cos²α.', '<strong>sin²α + cos²α = 1</strong> is a consequence of the Pythagorean theorem on the unit circle. It gives one function from another: if sin α = 0.6 and α is acute then cos α = √(1 − 0.36) = 0.8. Also tan α = sin α / cos α and 1 + tan²α = 1/cos²α.'),
    ('sin²α + cos²α = 1', '', 'sin²α + cos²α = 1'), m1),
  S('add', 'Формулы сложения', 'Addition formulas', ('<strong>sin(α ± β) = sin α cos β ± cos α sin β</strong>; <strong>cos(α ± β) = cos α cos β ∓ sin α sin β</strong>. Они позволяют вычислять, например, sin 75° = sin(45° + 30°). Ошибка «sin(α + β) = sin α + sin β» — самая частая: формулы сложения не линейны.', '<strong>sin(α ± β) = sin α cos β ± cos α sin β</strong>; <strong>cos(α ± β) = cos α cos β ∓ sin α sin β</strong>. They let us compute, for example, sin 75° = sin(45° + 30°). The mistake “sin(α + β) = sin α + sin β” is the most common: the addition formulas are not linear.'),
    ('sin(α + β) = sin α cos β + cos α sin β', '', 'sin(α + β) = sin α cos β + cos α sin β'), m2),
  S('dbl', 'Двойной угол', 'The double angle', ('Положив β = α, получаем <strong>sin 2α = 2 sin α cos α</strong> и <strong>cos 2α = cos²α − sin²α = 2cos²α − 1 = 1 − 2sin²α</strong>. Из последней формулы выражают квадраты: sin²α = (1 − cos 2α)/2, cos²α = (1 + cos 2α)/2.', 'Putting β = α we get <strong>sin 2α = 2 sin α cos α</strong> and <strong>cos 2α = cos²α − sin²α = 2cos²α − 1 = 1 − 2sin²α</strong>. From the last formula we express squares: sin²α = (1 − cos 2α)/2, cos²α = (1 + cos 2α)/2.'),
    ('sin 2α = 2 sin α cos α', '', 'sin 2α = 2 sin α cos α'), m3)],
 [TK(('Основное тождество', 'The basic identity'), ('sin α = 3/5, α острый. Найдите cos α и tan α.', 'sin α = 3/5, α acute. Find cos α and tan α.'), '', 'cos α = √(1 − 9/25) = 4/5; tan α = 3/4.', ('4/5 и 3/4.', '4/5 and 3/4.')),
  TK(('Сложение', 'Addition'), ('Найдите sin 75° = sin(45° + 30°).', 'Find sin 75° = sin(45° + 30°).'), '', '(√2/2)(√3/2) + (√2/2)(1/2) = √2(√3 + 1)/4 ≈ 0,966.', '≈ 0,966.'),
  TK(('Двойной угол', 'Double angle'), ('cos α = 0,6, sin α = 0,8. Найдите sin 2α.', 'cos α = 0.6, sin α = 0.8. Find sin 2α.'), '', '2 · 0,8 · 0,6 = 0,96.', '0,96.'),
  TK(('Упростить', 'Simplify'), ('Упростите 2 sin 15° cos 15°.', 'Simplify 2 sin 15° cos 15°.'), '', '= sin 30° = 1/2.', '1/2.'),
  TK(('Косинус двойного угла', 'Double-angle cosine'), ('Найдите cos 2α при cos α = 1/2.', 'Find cos 2α when cos α = 1/2.'), '2cos²α − 1', '2 · 1/4 − 1 = −1/2.', '−1/2.')],
 [Q('sin²α + cos²α =', 'sin²α + cos²α =', '1', 'sin 2α', '2', ('Основное тождество.', 'The basic identity.')),
  Q('sin 2α =', 'sin 2α =', '2 sin α cos α', '2 sin α', 'sin²α', ('Формула двойного угла.', 'The double-angle formula.')),
  Q('Верно ли sin(α + β) = sin α + sin β?', 'Is sin(α + β) = sin α + sin β true?', ('нет', 'no'), ('да', 'yes'), ('при любом α', 'for any α'), ('Нужна перекрёстная формула.', 'The cross-wise formula is needed.')),
  Q('cos 2α =', 'cos 2α =', 'cos²α − sin²α', 'cos²α + sin²α', '2 cos α', ('Формула двойного угла.', 'The double-angle formula.')),
  Q('tan α =', 'tan α =', 'sin α / cos α', 'cos α / sin α', 'sin α · cos α', ('Определение тангенса.', 'The definition of tangent.')),
  Q('sin 90° · cos 0° =', 'sin 90° · cos 0° =', '1', '0', '2', ('1 · 1.', '1 · 1.')),
  Q('sin α = 0,6, α острый. cos α =', 'sin α = 0.6, α acute. cos α =', '0,8', '0,4', '1', ('√(1 − 0,36).', '√(1 − 0.36).')),
  Q('Тождество — это равенство, верное', 'An identity is an equality that holds', ('при всех допустимых значениях', 'for all admissible values'), ('при одном значении', 'for one value'), ('при двух значениях', 'for two values'), ('Определение.', 'The definition.'))],
 src=[('Wikipedia: List of trigonometric identities', 'https://en.wikipedia.org/wiki/List_of_trigonometric_identities'), ('Wikipedia: Pythagorean trigonometric identity', 'https://en.wikipedia.org/wiki/Pythagorean_trigonometric_identity')])
