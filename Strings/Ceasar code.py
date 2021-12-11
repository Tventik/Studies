# Задача 1. Шифр Цезаря 2
#
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква заменяется
# на следующую по алфавиту через K позиций по кругу.
#
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
# Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.

def searching(letters, user_shift):
    new_text = [alphabet[(alphabet.index(i_letter) + user_shift) % 33]
                if i_letter != ' ' else ' ' for i_letter in letters]
    return new_text


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
income_text = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

outcome = searching(income_text, shift)
outcome_text = ''.join(outcome)

print('Зашифрованное сообщение: ', outcome_text)
