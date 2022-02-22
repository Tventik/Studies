server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }

}

for i_key, i_value in server_data.items():
    print(i_key, ':', sep='')
    for j_key, j_value in i_value.items():
        print('\t', j_key, ': ', j_value, sep='')

