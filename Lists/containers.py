def weight_control():
    while True:
        weight = int(input())
        if weight >= 200:
            print('\nВес контейнера не должен превышать 200 кг!')
            print('Введите вес контейнера: ', end='')
        else:
            return weight


def weight_counter(containers_weight, new_container_weight):
    containers_count = 0
    new_containers = []
    for i in containers_weight:
        if new_container_weight <= i:
            new_containers.append(i)
            containers_count += 1

    new_containers.append(new_container_weight)
    containers_count += 1
    return containers_count, new_containers


def new_weight_control(containers_weight, new_containers):
    containers_added = []
    for el in containers_weight:
        if el not in new_containers:
            containers_added.append(el)
    containers_united = new_containers + containers_added
    return containers_united


print('\nПРОГРАММА ДЛЯ УЧЕТА КОНТЕЙНЕРОВ НА СКЛАДЕ')
print('-------------------------------------------')

N = int(input('Кол-во контейнеров: '))
containers_mass = []

for container in range(N):
    print('Введите вес контейнера: ', end='')
    containers_mass.append(weight_control())

print('\nВведите вес нового контейнера: ', end='')
new_container = weight_control()

new_container_position, new_container_list = weight_counter(containers_mass, new_container)
containers_updated = new_weight_control(containers_mass, new_container_list)
print('\nНовый список контенеров: ', containers_updated)
print('Номер, куда встанет новый контейнер: ', new_container_position)