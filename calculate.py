action = input('Введите действие: ')
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
if action == '-':
	print(num_1, action, num_2, '=', num_1 - num_2)
elif action == '+':
	print(num_1, action, num_2, '=', num_1 + num_2)
else:
	print('Ошибка ввода')
