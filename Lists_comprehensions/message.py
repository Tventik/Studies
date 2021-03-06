some_text = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

double_letters = [i_letter * 2 for i_letter in some_text]
double_plus_symbol = [el + symbol for el in double_letters]

print('Список удвоенных символов:', double_letters)
print('Склейка с дополнительным символом:', double_plus_symbol)

# Задача 2. Сообщение
#
# Илья решил безобидно подшутить над другом и написал программу для смартфона,
# которая при отправке сообщения удваивает каждый символ строки и заодно к каждому
# удвоенному добавляет ещё один дополнительный.
#
# Пользователь вводит строку и дополнительный символ. Напишите программу, которая
# генерирует два списка: в первом списке каждый элемент — удвоенная буква первой строки,
# во втором списке каждый элемент — конкатенация элемента первого списка и дополнительного символа.
#
#
# Пример:
#
# Введите строку: привет
# Введите дополнительный символ: !
#
#
# Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
# Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']