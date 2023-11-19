from termcolor import colored, cprint
from about import about_descr
from commands import command_list

from topics import variables_and_data_types, string_and_string_methods


cprint('Вас вітає Python у консолі.\nПишіть "help", щоб отримати список команд.\nОпис методів викликається '
       'через подвійне підкреслення. Наприклад: string__\nПишіть "about", щоб дізнатися контакти для зворотнього '
       'зв\'язку та відгуків.\nДля закриття програми введіть "quit"', 'yellow')


separete_line = colored('--------------------', 'yellow')
console_seperation_template = f'{separete_line}\n'
i = 0

# HELP. COMMANDS LIST---------------
help__commands = []

for key in variables_and_data_types:
    help__commands.append(key)

for key in string_and_string_methods:
    help__commands.append(key)
# END-------------------------------


while True:
    user_command = str(input(colored(f'{console_seperation_template}\nВведіть команду: ', 'green')).lower())

    if user_command == 'help':
        for item in help__commands:
            print(item)
    if user_command == 'about':
        about_descr()
    if user_command == 'quit':
        cprint('-> Команда "quit".\nПрограма закривається.', 'yellow')
        break
    if user_command != 'quit' and user_command != 'help' and user_command != 'about':
        command_list(user_command)
        # for key in variables_and_data_types:
        #     print(user_command, key)
    if user_command not in help__commands:
        cprint(f'Невідома команда "{user_command}". Команда "help" покаже список діючих команд', 'yellow')
