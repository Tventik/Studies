family = dict()
family_members_count = int(input('Кол-во членов семьи: '))

for i_member in range(1, family_members_count + 1):
    family_member = dict()
    print(i_member, '-й', ' член семьи: ', sep='', end='')
    status = input()
    age = int(input('Возраст: '))
    hobby = input('Хобби (через запятую): ').split(',')
    kids = int(input('Кол-во детей: '))
    family_member['Возраст'] = age
    family_member['Хобби'] = hobby
    family_member['Кол-во детей'] = kids
    family[status] = family_member
    print()
print('Моя семья:')
for i_member in family:
    print(i_member, family[i_member])


