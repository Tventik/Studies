# Задача 1. Пунктуация
#
# Напишите программу, которая считает количество знаков пунктуации в символьной строке.
# К знакам пунктуации относятся символы из набора ".,;:!?". Набор должен храниться в виде множества.
#
#
# Пример:
#
# Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
#
# Количество знаков пунктуации: 6

syms = '.,;:!?'
sym_list = list(syms)

symbols = set()
for i_sym in sym_list:
    symbols.add(i_sym)

some_text = input('Введите текст: ')

sym_count = 0
for i_elem in some_text:
    if i_elem in symbols:
        sym_count += 1

print('Количество знаков пунктуации:', sym_count)