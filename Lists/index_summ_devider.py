nums_list = []
N = int(input('Кол-во чисел в списке: '))

for i in range(1, N + 1):
    print('Введите', i, 'число: ', end='')
    num = int(input())
    nums_list.append(num)

K = int(input('\nВведите делитель: '))
indexCount = 0
print()

for num in range(N):
    if nums_list[num] % K == 0:
        print('Индекс числа', nums_list[num], 'равен:', num)
        indexCount += num
print('Сумма индексов:', indexCount)