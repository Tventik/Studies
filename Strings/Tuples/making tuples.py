# Задача 1. Создание кортежей
#
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа,
# создав тем самым третий кортеж. С помощью метода кортежа определите в нём количество нулей.
# Выведите на экран третий кортеж и количество нулей в нём.
import random

numbers = list()
for i_num in range(10):
    numbers.append(random.randint(0, 5))
first_tuple = tuple(numbers)
print(first_tuple)

numbers = list()
for i_num in range(10):
    numbers.append(random.randint(-5, 0))
second_tuple = tuple(numbers)
print(second_tuple)

third_tuple = sorted(list(first_tuple) + list(second_tuple))
print(third_tuple)
print('Кол-во нулей в третьем кортеже:', third_tuple.count(0))

