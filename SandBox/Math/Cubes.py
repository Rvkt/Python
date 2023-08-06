cube_dict = dict()

num1 = int(input('num1: '))
num2 = int(input('num2: '))

for num in range(num1, num2+1):
    cube_dict[num] = num*num*num
    

print(cube_dict)