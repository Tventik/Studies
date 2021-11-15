def increase(percent, price):
    return price * (1 + percent/100)


initial_prices = [float(input('Цена на товар: ')) for i_price in range(5)]
first_increase = float(input('\nПовышение на первый год: '))
second_increase = float(input('Повышение на второй год: '))

first_year_prices = [increase(first_increase, i_price) for i_price in initial_prices]
second_year_prices = [increase(second_increase, i_price) for i_price in first_year_prices]
print('\nСумма цен за каждый год:', round(sum(initial_prices), 2),
      round(sum(first_year_prices), 2),
      round(sum(second_year_prices), 2))

# Задача 3. Повышение цен
#
# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать,
# мы спрогнозировали, что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.
#
# Напишите программу, которая получает на вход список цен на товары
# (вещественные числа, список генерируется также с помощью list comprehensions)
# и выводит в одну строку общую сумму стоимости товаров за каждый год.
#
#
# Пример:
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
#
# Повышение на первый год: 0
# Повышение на второй год: 10
# Сумма цен за каждый год: 93.83 93.83 103.22