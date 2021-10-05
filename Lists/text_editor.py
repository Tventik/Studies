S = input('Введите строку: ')
text = list(S)
sym_count = 0
correct_text = ''

for i in text:
    if i == ':':
        i = ';'
        correct_text += i
        sym_count += 1
    else:
        correct_text += i
print('Исправленная строка: ', correct_text)
print('Кол-во замен: ', sym_count)
