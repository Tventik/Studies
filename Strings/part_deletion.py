# Задача 3. Удаление части
#
# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы.
# Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных.
# Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.
#
# Подсказка: используйте методы islower() и/или isupper().
#
#
# Пример:
#
# Введите строку: ПитоН - этО хорошО
# Результат: питон - это хорошо
#
#
# Пример 2:
#
# Введите строку: ПиТоН - ЭтО УДоБнО
# Результат: ПИТОН - ЭТО УДОБНО

some_text = input('Введите строку: ').split()
output_text = ' '.join(some_text)

small_letters_counter = 0
big_letters_counter = 0

for letter in output_text:
    if letter.islower():
        small_letters_counter += 1
    elif letter.isupper():
        big_letters_counter += 1

if small_letters_counter > big_letters_counter:
    print(output_text.lower())
elif big_letters_counter > small_letters_counter:
    print(output_text.upper())

