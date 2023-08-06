square_dict = dict()
cube_dict = dict()


num1 = int(input('num1: '))
num2 = int(input('num2: '))


for num in range(num1, num2+1):
    square_dict[num] = num*num


for num in range(num1, num2+1):
    cube_dict[num] = num*num*num
    
    
print(f'Square of given numbers is {square_dict}')
print(f'Cube of given numbers is {cube_dict}')