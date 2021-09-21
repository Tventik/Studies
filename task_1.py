def factorial(number):
    summ = 1
    for num in range(1, number + 1):
        summ *= num
    print(summ)

number = int(input('Введите номер: '))
result = factorial(number)
