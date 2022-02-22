# Задача 1. Паспортные данные
#
# В базе данных поликлиники хранятся паспортные данные людей. Хранение реализовано
# с помощью словаря, состоящего из пар «Серия и номер паспорта — фамилия и имя».
# Серия и номер — составной ключ, а фамилия и имя — составное значение.
# Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.

def is_person(passport):
    numbers = []
    for i_num in passport:
        numbers.append(int(i_num))
    numbers_tuple = tuple(numbers)
    if numbers_tuple in data:
        return data[numbers_tuple]
    else:
        return 'Нет такого', 'человека'


data = {

    (5000, 123456): ('Иванов', 'Василий'),

    (6000, 111111): ('Иванов', 'Петр'),

    (7000, 222222): ('Медведев', 'Алексей'),

    (8000, 333333): ('Алексеев', 'Георгий'),

    (9000, 444444): ('Георгиева', 'Мария')

}

user_passport = input('Введите через пробел серию и номер паспорта: ').split()
surname, name = is_person(user_passport)
print(surname, name)
