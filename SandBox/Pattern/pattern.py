symbol = '❋'

# num =int(input('Enter the number of rows: '))
num = 9
for i in range(1,num+1):
    for j in range(1,i+1):
        print(symbol, end='')
    print('')

"""#### **Pyramid Shape**"""

# num =int(input('Enter the number of rows: '))
num = 4

for i in range(0,num):
    for j in range(0,num-i-1):
        print(end='')
    for j in range(0,i+1):
        print(symbol, end='')
    print('')

"""#### **Floyd's triangle**"""

n = int(input('Enter the number of rows: '))