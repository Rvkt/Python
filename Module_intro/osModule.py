import os

print('Home Directory is: ' + '\n\t' + os.path.expanduser("~"))

dstn = os.path.expanduser('~')
file_list = (os.listdir(dstn))

# for file in file_list:
#     print(file)
#     if not file.startswith('.'):
#         if not file.startswith('_'):
#             print(file)
