stuff = int(input('Введите количество сотрудников организации: '))
stuff_id = []
for employee in range(stuff):
    id = int(input('\nВведите ID работника: '))
    stuff_id.append(id)
search = int(input('\nКакого работиника ищем? '))
if search in stuff_id:
    print('\nСотрудник на месте')
else:
    print('\nСотрудник не работает!')