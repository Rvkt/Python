fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):
  print(x)


for x in range(2, 6):
  print(x)


# range(start, end, step)

for x in range(2, 30, 3):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Nested for loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


for x in adj:
  for y in fruits:
    print(x, y)


'''for loops cannot be empty,
but if you for some reason have a for loop with no content,
put in the pass statement to avoid getting an error.'''

for x in [0, 1, 2]:
  pass


'''# For loop on a list to get the product of the numbers
numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
   product = product * number

print('The product is:', product)
'''
