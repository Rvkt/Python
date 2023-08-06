from pathlib import *

user_input = input('Input: ')


def create_file():
    file_name = input('Enter file name: ')
    file = Path(file_name)
    if file.exists():
        print('File already exists!!')
    else:
        file.touch()
        print(f'{file_name} is created !!')

if user_input == 'create file':
    create_file()