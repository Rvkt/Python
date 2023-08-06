import os

os.chdir(os.getcwd())

print('What are you learning?')

string = input('Enter the topic: ')

os.mkdir(f'{string}Learn')
