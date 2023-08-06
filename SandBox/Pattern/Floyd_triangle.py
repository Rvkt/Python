n = int(input('Enter the number of the rows: '))
symbol = '•'
num = 1
str = input('Enter String: ')

print('\nFloyd\'s Triangle\n')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(symbol, end=' ')
    print()

print('\nFloyd\'s Triangle with numbers\n')
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(num, end=' ')
        num = num + 1
    print()



