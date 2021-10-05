nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

first_num = nums_list[0]

for i in nums_list:
    if i == first_num:
        maximum = i
        minimum = i
    elif i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i

print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)
