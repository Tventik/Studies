S = input('Введите строку: ')
N = int(input('Введите номер символа: '))
sym_list = list(S)
sym_count = 0

print('\nСимвол слева: ', sym_list[N-2])
print('Символ справа: ', sym_list[N])
print()

for i in sym_list:
    if i == sym_list[N-1]:
        sym_count += 1
if sym_count == 2:
    print('Есть ровно один такой же символ.')
elif sym_count == 3:
    print('Есть два таких же символа.')
else:
    print('Таких же символов нет.')


