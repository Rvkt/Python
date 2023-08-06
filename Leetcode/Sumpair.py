# print the pair with given sum

list1 = [8, 7, 2, 5, 3, 1, 9, 4, 6]
n = len(list1)
numSum = 10

for i in range(n):
    for j in range(i + 1, n):
        if (list1[i] + list1[j]) == numSum:
            print(f'{list1[i]}, {list1[j]}')
