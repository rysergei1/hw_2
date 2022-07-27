from math import *

'''1 часть обязательной домашки. Можно весь код в один файл, но разбить красивыми комментами, чтобы было понятно 
где какая формула. Ввод и вывод по желанию оформите красиво, мне в этих заданиях важно, чтобы вы умели работать 
с формулами. Корни квадратные, синусы и косинусы можете импортировать из модуля math. Во втором задании хочу, чтобы
 вы нашли (или вывели) формулу тангенса через синус и косинус и котангенс через них же.'''

'''Можете как доп задание здесь поиграться с тригонометрией. Сделайте красиво оформленную таблицу принтами, где по 
горизонтали углы в градусах (0, 30, 45, 60, 90, 180, 270, 360), а по вертикали тригонометрические функции
 (sin, cos, tg, ctg). В ячейках таблицы - значение функции для соответсвующего угла. 

Спойлер: можно чекать таблицу синусов например, такая же есть для тангенсов и всех прочих. 

Напоминание: тригонометрические функции из модуля math (sin, cos и так далее) принимают значение угла в радианах, 
то есть выраженное через pi. В градусах не принимают. Но в модуле math есть функции для перевода значений из градусов
 в радианы и наоборот. Можете их юзать 😉'''

print('*** *** ***')
print('task 2.1')
a = 1
y = round(a ** 2 / 3 + (a ** 2 + 4) / 6 + sqrt(a ** 2 + 4) / 4 + sqrt((a ** 2 + 4) ** 3) / 4, 2)
print(f'y = {y}')
print()
print('*** *** ***')

print('task 2.2')
x = pi / 6
y = round(cos(x) + sin(x), 6)
print(f'При х = {x}, \ny = cos(x) + sin(x) = {y}')
print(f'tg(x) = sin(x)/cos(x) = ', sin(x) / cos(x))
print(f'ctg(x) = cos(x)/sin(x) = ', cos(x) / sin(x))
print()
print(f'Угол   0\xb0   30\xb0   45\xb0   60\xb0   90\xb0   180\xb0   270\xb0   360\xb0')
print(f'sin   ', sin(0), '', round(sin(pi / 6), 2), '', round(sin(pi / 4), 2), '', round(sin(pi / 3), 2), ' ',
      round(sin(pi / 2), 2), ' ', round(sin(pi), 2), ' ', round(sin(3 * pi / 2), 2), ' ', round(sin(2 * pi), 2))
print(f'cos   ', cos(0), '', round(cos(pi / 6), 2), '', round(cos(pi / 4), 2), '', round(cos(pi / 3), 2), ' ',
      round(cos(pi / 2), 2), ' ', round(cos(pi), 2), ' ', round(cos(3 * pi / 2), 2), ' ', round(cos(2 * pi), 2))
print(f'tg   ', tan(0), '', round(tan(pi / 6), 2), '', round(tan(pi / 4), 2), '', round(tan(pi / 3), 2), ' ',
      '-', ' ', round(tan(pi), 2), ' ', "-", ' ', round(tan(2 * pi), 2))
print(f'ctg   ', '-', ' ', round(1 / tan(pi / 6), 2), '', round(1 / tan(pi / 4), 2), '',
      round(1 / tan(pi / 3), 2), ' ',
      round((1 / tan(pi / 2)), 2), ' ', '-', ' ', round(1 / tan(3 * pi / 2), 2), ' ',
      '-')
