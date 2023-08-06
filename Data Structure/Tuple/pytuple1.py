'''
mytuple = ("apple", "banana", "cherry")
print(mytuple)
'''


'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(f'{thistuple} with length of {len(thistuple)} and type of thistuple is {type(thistuple)}')
'''

'''
tuple1 = ("apple")
tuple2 = ("apple",)
print(f'{type(tuple1)} and {type(tuple2)}')
'''


# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# tuple1 = ("abc", 34, True, 40, "male")

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# del thistuple

# print(thistuple)

# fruits = ("apple", "banana", "cherry")

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# thistuple = ("apple", "banana", "cherry")



'''
thistuple = ("apple", "banana", "cherry", "mango", "guava")

for x in thistuple:
  print(x)

print()
for i in range(len(thistuple)):
  print(thistuple[i])


print()
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
'''


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# tupleList = ('a', ['a', 'b', 'c'])
# print(tupleList)
# print(tupleList.count('a'))


myset = {'a', 'b', 'c'}

print(len(myset))

i = 0

while i < len(myset):
    print(i)
    i +=1

