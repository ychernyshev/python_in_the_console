from termcolor import cprint

from about import about_descr

variables_and_data_types = {
        'variable': 'Variable - це "комірка" пам\'яті, у котру вкладається необхідний тип даних: літера, символ,'
                    ' число, список, кортеж, словник, set, логічний тип даних, бинарний тип даних (байт), None '
                    '(тобто, нічого)',
        'data_types': 'Те, над чим необхідно провести операцію. Тобто, символьна строка, число (може бути ціле, дробне)',
        'data_types__str': 'Будь який набір елементів, будь то літери, цифри, спеціальні символи, що огортаються подвійними або одинарними лапками.\nНаприклад: "приклад, 3332, !?&@".\nІніціалізується як variable_name = "text".\nВикликається за назвою змінної, тобто - variable_name\nНаприклад: new_variable = variable_name (При команді print(new_variable) отримаємо строку - "text")',
        'data_types__int': '',
        'data_types__float': '',
        'data_types__ complex': '',
        'data_types__list': '',
        'data_types__tuple': '',
        'data_types__ range': '',
        'data_types__dict': '',
        'data_types__set': '',
        'data_types__frozenset': '',
        'data_types__bool': '',
        'data_types__bytes': '',
        'data_types__bytearray': '',
        'data_types__memoryview': '',
        'data_types__NoneType': '',
    }


def command_list(user_command):
    for key, value in variables_and_data_types.items():
        if user_command == key:
            print(value)
        # else:
        #     cprint(f'Невідома команда "{user_command}". Команда "help" покаже список діючих команд', 'yellow')
        #     break

