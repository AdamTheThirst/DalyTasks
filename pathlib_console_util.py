from pathlib import Path


commands_list = ('exit', 'dir name', 'dir path')

def command_cur_dir_name() -> Path:
    return Path.cwd()

def command_get_dir_list():
    return list()

commands = {'exit': 'exit',
            'cur dir name': command_cur_dir_name,
            'where i am': command_cur_dir_name,
            'get dir list': command_get_dir_list}

while True:
    command = input(str('input command: '))

    if command.lower() in commands:
        if command == 'exit':
           print('Terminate the program')
           break

        get_command_result = commands[command.lower()]()
        print(get_command_result)

    else:
        print('Invalid command!')


