# Задача 3. IP-адрес
#
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой.
# Каждое число находится в диапазоне от 0 до 255 (включительно).
#
#
# Пример правильного адреса: 192.168.1.0
#
# Пример неправильного адреса: 192.168.300.0
#
#
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес.
# Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.

numbers = []
count = 1

while count < 5:
    print('Введите', count, 'номер: ', end='')
    number = input()
    if 0 <= int(number) < 255:
        numbers.append(number)
        count += 1
    else:
        print('Ошибка ввода. Число должно быть в диапазоне от 0 до 250')
print()
ip_address = '{}.{}.{}.{}'.format(*numbers)
# ip_address = '.'.join(numbers)
#     str(numbers[0]),
#     str(numbers[1]),
#     str(numbers[2]),
#     str(numbers[3])
# )
print('IP-адрес:', ip_address)
print(numbers)
print(*numbers)  # * - распаковка списка
