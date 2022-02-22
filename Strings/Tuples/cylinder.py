# Задача 2. Цилиндр
#
# Андрей однажды уже писал функции для расчёта площади сферы и объёма шара.
# И теперь для своей курсовой работы ему пришлось связаться с цилиндрами.
#
# Пользователь вводит два значения: радиус и высоту. Напишите функцию для
# расчёта площади боковой поверхности цилиндра и его полной площади.
# Функция должна возвращать два эти значения. После этого в основной
# программе выводятся оба ответа в две строки.
#
# Площадь боковой поверхности (r — радиус, h — высота):
#
# Полная площадь (S — площадь круга):

import math


def cylinder(radius, height):
    side = 2 * math.pi * radius * height
    square = math.pi * radius**2
    full = side + 2 * square
    return side, full


R = float(input('Введите радиус: '))
H = float(input('Введите высоту: '))

parameters = cylinder(R, H)
print('Площадь боковой поверхности цилиндра: ', round(parameters[0], 2))
print('Полная площадь цилиндра: ', round(parameters[1], 2))
