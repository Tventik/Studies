left_border = int(input('Левая граница: '))
right_border = int(input('Правая граница: '))

even_numbers = [i_num for i_num in range(left_border, right_border + 1) if i_num % 2 == 0]
print('Список из четных чисел:', even_numbers)

# Задача 1. Список чётных чисел
#
# Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список
# из чётных чисел в диапазоне от А до B. Используйте list comprehensions (как и в следующих задачах).
#
