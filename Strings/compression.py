user_input = input('Ввеедите строку: ').split('.')
for i_sym in user_input:
    if not i_sym.isdigit():
        print(i_sym, '- не целое число')
    elif int(i_sym) > 255:
        print(i_sym, 'превышает 255')
else:
    print('ip_address корректен')
    # return break
    # return False