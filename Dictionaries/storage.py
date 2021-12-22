# Задача 1. Склады
#
# У мебельного магазина есть два склада, на которых хранятся
# разные категории товаров по парам «название — количество»:
#
# Магазин решил сократить аренду и скинуть все товары в большой склад (big_storage).
# После этого нас попросили реализовать поиск по товарам.
#
# Напишите программу, которая объединяет оба словаря в один (в big_storage),
# затем запрашивает у пользователя название товара и выводит на экран его количество.
# Если такого товара нет, то выводит об этом ошибку. Для получения значения используйте метод get.

small_storage = {

    'гвозди': 5000,

    'шурупы': 3040,

    'саморезы': 2000

}

big_storage = {

    'доски': 1000,

    'балки': 150,

    'рейки': 600

}

big_storage.update(small_storage)
print('Вам нужен товар со склада? (да/нет)', end=' ')
answer = input().lower()
while answer != 'нет':
    item = input('Укажите название товара: ').lower()
    if big_storage.get(item):
        print('Товара', item, 'на складе', big_storage[item], 'единиц')
    else:
        print('Товара {} нет на складе'.format(item))
    print('Вам нужен товар со склада?', end=' ')
    answer = input().lower()
print('До свидания!')



