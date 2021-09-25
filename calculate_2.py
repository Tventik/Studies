action = input('Введите действие: ')
numerals = int(input('Введите количество операндов: '))

if numerals > 0:
	first_num = int(input('Введите операнд № 1: '))
else:
	print('Ошибка ввода')

result = first_num
string = str(first_num)

if action == '+':
	for num in range(2, numerals + 1):
		print('Введите операнд № ',num, ': ', sep= '', end= '')
		number = int(input())
		result += number
		number = str(number)
		string += ' ' + action + ' ' + number
print(string, '=', result)



