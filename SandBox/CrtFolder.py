from pathlib import *

folder1 = Path('folder1')

a = folder1.exists()  # returns bool (False) if directory does not exist.

folder1.mkdir(exist_ok=True)

b = folder1.exists()  # returns bool (True) if directory does exist.


