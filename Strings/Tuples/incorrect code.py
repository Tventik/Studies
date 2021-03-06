# Задача 3. Неправильный код
#
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный
# индекс и случайное значение, а затем по этим индексу и значению меняет сам кортеж.
# Функция должна возвращать кортеж и случайное значение.
#
# В основном коде функция используется два раза, и на экран два раза выводится новый кортеж
# и случайное значение. Причём второй раз выводится сумма первого случайного значения и второго.
#
# Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.
#


import random


def change(nums):
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums_list = list(nums)
    nums_list[index] = value
    nums_tuple = tuple(nums_list)
    return nums_tuple, value


my_nums = 1, 2, 3, 4, 5
new_nums_1, rand_val_1 = change(my_nums)
print(new_nums_1, rand_val_1)

new_nums_2, rand_val_2 = change(my_nums)
print(new_nums_2, rand_val_1 + rand_val_2)
