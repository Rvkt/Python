# sort a list without using SORT keyword

list1 = [41, 2, 12, 45, 32, 51, 6, 11, 9, 101]

n = len(list1)

for i in range(n):
    for j in range(i + 1, n):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)
