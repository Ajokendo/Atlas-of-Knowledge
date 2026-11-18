# -*- coding: utf-8 -*-
"""Реестр глав и блоков математики. Дополняется при добавлении новых глав."""
BLOCKS = [
 dict(id='I', ru='Числа и счёт', en='Numbers and counting',
      note_ru='Начальная школа: язык проще, больше интерактива. Темы, а не классы: учитель сам выбирает, когда давать тему по программе. Уровень — основы.',
      note_en='Primary school: simpler language, more interactivity. Organised by topic, not by grade: teachers choose when to use each topic. Level — basics.'),
]
# n, slug, ru, en, descRu, descEn, block
CHAPTERS = [
 ('01', '01-numbers-to-20.html', 'Числа до 20: счёт и состав числа', 'Numbers to 20: counting and parts of a number',
  'Счёт до 20, десяток и единицы, состав числа, сравнение на числовом луче.', 'Counting to 20, tens and ones, parts of a number, comparing on the number line.', 'I'),
 ('02', '02-add-subtract.html', 'Сложение и вычитание', 'Addition and subtraction',
  'Прыжки по лучу, переход через десяток, связь сложения и вычитания.', 'Jumps on the line, crossing the ten, addition and subtraction as a family.', 'I'),
 ('03', '03-place-value.html', 'Разряды и числа до 1000', 'Place value and numbers to 1000',
  'Сотни, десятки, единицы; сравнение трёхзначных чисел; округление.', 'Hundreds, tens, ones; comparing three-digit numbers; rounding.', 'I'),
 ('04', '04-multiply-divide.html', 'Умножение и деление', 'Multiplication and division',
  'Умножение как сложение одинаковых, деление с остатком, таблица умножения.', 'Multiplication as repeated addition, division with remainder, the multiplication table.', 'I'),
 ('05', '05-column-arithmetic.html', 'Действия в столбик', 'Column arithmetic',
  'Сложение, вычитание и умножение многозначных чисел, перенос и заём, прикидка.', 'Adding, subtracting and multiplying big numbers, carrying and borrowing, estimating.', 'I'),
 ('06', '06-order-of-operations.html', 'Порядок действий и скобки', 'Order of operations and brackets',
  'Почему 2 + 2 · 2 = 6, скобки, вычисление по шагам, подбор знаков.', 'Why 2 + 2 · 2 = 6, brackets, step-by-step evaluation, finding signs.', 'I'),
 ('07', '07-word-problems.html', 'Текстовые задачи', 'Word problems',
  'Схемы из отрезков, «на сколько» и «во сколько раз», покупка и сдача в сомах.', 'Bar diagrams, “by how much” and “how many times”, shopping and change in soms.', 'I'),
 ('08', '08-fractions-intro.html', 'Доли и дроби', 'Parts and fractions',
  'Числитель и знаменатель, сравнение долей, доля от числа, равные дроби.', 'Numerator and denominator, comparing fractions, a fraction of a number, equal fractions.', 'I'),
]
