import random

nums = [random.randint(0, 100) for i_num in range(10)]
print('Исходный список:', nums)

start = int(random.randint(0, 10))
while True:
    finish = int(random.randint(0, 10))
    if finish > start:
        break

print('Начальный индекс среза:', start, '\nКонечный индекс среза:', finish)
nums = [nums[el] for el in range(len(nums)) if el < start or el >= finish]
print('Список без срезанных чисел', nums)


# Задача 3. Удаление части
#
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B).
# Напишите программу, которая удаляет элементы списка с индексами от А до В.
# Не используйте дополнительные переменные и методы списков.

