# Задача 3. Контакты
#
# Энтузиаст Степан, купив новый телефон, решил написать для него свою
# собственную операционную систему. И, конечно же, первое, что он
# захотел в ней реализовать, — это телефонная книга.
#
# Напишите программу, которая запрашивает у пользователя имя контакта
# и номер телефона, добавляет их в словарь и выводит на экран текущий
# словарь контактов. Запрос на добавление идёт бесконечно (но можно
# задать своё условие для завершения программы). Обеспечьте контроль
# ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.
#
# Пример:
# Текущие контакты на телефоне:
# <Пусто>
#
# Введите имя: Иван
# Введите номер телефона: 100200300
#
# Текущие контакты на телефоне:
# Иван  100200300
#
# Введите имя: Лена
# Введите номер телефона: 8005555522
#
# Текущие контакты на телефоне:
# Иван  100200300
# Лена  8005555522
#
# Введите имя: Иван
# Ошибка: такое имя уже существует.

phonebook = dict()

while True:
    print('\nТекущие контакты на телефоне: ')
    if len(phonebook) < 1:
        print('<Пусто>')
    else:
        for i_name in phonebook:
            print(i_name, ' ', phonebook[i_name])
    name = input('\nВведите имя: ')
    if name in phonebook:
        print('Ошибка: такое имя уже существует')
    else:
        phone_number = int(input('Введите номер телефона: '))
        phonebook[name] = phone_number

