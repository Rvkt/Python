# Convert tuple to string

# reverse a tuple



''' # unpack a tuple

tuple = (10, 20, 30)

(a, b, c) = tuple

print(a, b, c)

'''

'''
tup = (10, 20, 30)

tuple1 = list(tup)
tuple1[-1] = 50
tup = tuple(tuple1)

print(tup)
'''



# Problem 10

t = ('harish', 13, 55, 'play', ['hello', 123], 'hockey')

list_t = list(t)

print('Prob10a', list_t[0])

prob10b = []

for i in list_t:
    if i == str(i):
        prob10b.append(i)

print('Prob10b ' + ' '.join(prob10b))
