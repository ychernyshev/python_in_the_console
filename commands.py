from parts.topics import variables_and_data_types, string_and_string_methods


def command_list(user_command):
    for key, value in variables_and_data_types.items():
        if user_command == key:
            print(value)


    for key, value in string_and_string_methods.items():
        if user_command == key:
            print(value)
        # else:
        #     cprint(f'Невідома команда "{user_command}". Команда "help" покаже список діючих команд', 'yellow')
        #     break

