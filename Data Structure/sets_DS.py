my_set = {1, 2, 3, 4, 5}
print('SET \t:', my_set)
print('TYPE \t:', type(my_set))
print('Length \t:', len(my_set))

# duplicated are not allowed in set
print('\n')
my_set2 = {1, 1, 2, 2}
print('SET \t:', my_set2)
print('Length \t:', len(my_set2))

print('\n')
print([1, 2] == [2, 1])

print({1, 2, 3} == {3, 2, 1, 1, 1})
