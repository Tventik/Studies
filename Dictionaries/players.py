# Задача 2. Игроки
#
# Есть готовый словарь игроков, у каждого игрока есть имя, команда,
# в которой он играет, а также его текущий статус, в котором указано,
# отдыхает он, тренируется или путешествует:


players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}

# print(players_dict.get('team',))
players_names_status = []

players_list_1 = [player['name'] for player in players_dict.values()
                  if player['team'] == 'A' and player['status'] == 'Rest']
players_names_status.append(players_list_1)

players_list_2 = [player['name'] for player in players_dict.values()
                  if player['team'] == 'B' and player['status'] == 'Training']
players_names_status.append(players_list_2)

players_list_3 = [player['name'] for player in players_dict.values()
                  if player['team'] == 'C' and player['status'] == 'Travel']
players_names_status.append(players_list_3)

for i_name in players_names_status:
    print(i_name)

# Напишите программу, которая выводит на экран вот такие
# данные в разных строчках:
#
# Все члены команды из команды А, которые отдыхают.
# Все члены команды из группы B, которые тренируются.
# Все члены команды из команды C, которые путешествуют.