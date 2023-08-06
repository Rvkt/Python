from pathlib import *
import os
import errno

# print(Path.cwd())
# print(Path.home())
file1 = Path('file1.txt')
file2 = Path('file2.txt')
file3 = Path('file3.txt')
folder1 = Path('folder1')
folder2 = Path('folder2')
folder3 = Path('folder3')

# Create a file
file1.touch()
file2.touch()
file3.touch()

# Create a folder
# try:
#     folder.mkdir()
# finally:
#     pass

# Version 2
try:
    os.mkdir(folder1)
except OSError as e:
    if e.errno == errno.EEXIST:
        pass

# file inside folder / directory

try:
    file3 = folder2 / 'file3.txt'
    file3.touch()
except OSError as e:
    if e.errno == errno.EEXIST:
        pass

