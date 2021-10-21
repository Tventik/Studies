# Задача 2. Вредоносное ПО
#
# Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт,
# который после двух сообщений отправляет ещё одно на основе первых двух.
#
# Пользователь вводит две строки. В каждой из них есть какое-то количество
# специальных символов ! и ?. Напишите программу, которая считает количество
# этих символов отдельно в первой строке и отдельно во второй. Если в первой
# строке их больше, чем во второй, то на экран выводится первая строчка, объединённая
# со второй, а иначе — вторая с первой. При равном количестве символов в строках выводится «Ой».

def symbols(string):
    count = 0
    count += string.count('!')
    count += string.count('?')
    return count


first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')
elements = ['!', '?']

firstCount = symbols(first_string)
secondCount = symbols(second_string)

if firstCount > secondCount:
    print(first_string + ' ' + second_string)
elif secondCount > firstCount:
    print(second_string + ' ' + first_string)
else:
    print('Ой')


