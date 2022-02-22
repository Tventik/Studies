# Задача 2. Словари из списков
#
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита
# (могут повторяться). Затем для каждого списка создайте словарь из пар
# «индекс — значение» и выведите оба словаря на экран.
#
# Подсказка: random
#
#
# Пример:
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
#
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
#
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
import random
sym_list_1 = []
sym_list_2 = []
for i_sym in range(10):
    sym_list_1.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    sym_list_2.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
print()
sym_dict_1 = {i_index: i_sym for i_index, i_sym in enumerate(sym_list_1)}
print('Первый список символов:', sym_list_1)
print('Первый словарь из символов:', sym_dict_1)
print()
sym_dict_2 = {i_index: i_sym for i_index, i_sym in enumerate(sym_list_2)}
print('Второй список символов:', sym_list_2)
print('Второй словарь из символов:', sym_dict_2)


