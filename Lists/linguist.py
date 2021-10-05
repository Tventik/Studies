words_list = []
for _ in range(3):
    print('Введите', _ + 1, 'слово: ', end='')
    word = input()
    words_list.append(word)
words_count = [0, 0, 0]

text = input('\nСлово из текста: ')
while text != 'end':
    for i in range(3):
        if text == words_list[i]:
            words_count[i] += 1
    text = input('Слово из текста: ')

print('\nПодсчет слов в тексте:')
for word in range(3):
    print('Слово', words_list[word], ':', words_count[word])
