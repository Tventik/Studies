scores = []
N = int(input('Кол-во собак, участвующих в забеге: '))

for dog in range(1, N + 1):
    print('У собаки под номером', dog, 'кол-во очков: ', end='')
    score = int(input())
    scores.append(score)

max_score = scores[0]
min_score = scores[0]

for score in range(N):
    if scores[score] > max_score:
        max_score = scores[score]
    elif scores[score] < min_score:
        min_score = scores[score]

correct_scores = []
for el in scores:
    if el == max_score:
        correct_scores.append(min_score)
    elif el == min_score:
        correct_scores.append(max_score)
    else:
        correct_scores.append(el)

print('Изначальный список', scores)
print('Наибольший элемент в списке: ', max_score, '\nНаименьший элемент в списке:', min_score)
print('Измененный список', correct_scores)