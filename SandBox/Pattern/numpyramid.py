nr = int(input('Enter the number of the rows: '))
# num = 1

for i in range(1, nr+1):
    for j in range(1, nr-i+1):
        print(' ', end=' ')
    for j in range(i, 0, -1):
        print(j, end=' ')
    for j in range(2, i+1):
        print(j, end=' ')
    print()

"""
4 3 2  1  2 3 4
4 3  2 1 2  3 4
4  3 2 1 2 3  4
 4 3 2 1 2 3 4
"""
4