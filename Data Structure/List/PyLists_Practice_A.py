# Q1. Write a python program to sum all the items in a list.
'''
#Solution type-1
numbers = [1,2,3,4,5,1,4,5]

print(sum(numbers))
'''
'''
#Solution type-2
numbers = [1,2,3,4,5,1,4,5]
s=0
for i in numbers:
  s +=i
print(s)
'''
# *********************************************************************
# Q2. Write a python program to get the largest number from a list.
''' 
#Solution type-1
numbers = [59, 47, 7, 17, 45]
print(max(numbers))
'''
'''
#Solution type-2
numbers = [59, 47, 7, 17, 45]
numbers.sort()
print(numbers[-1])
'''

# Q3. Write a python program to count the number of strings where the string length is 2 or 
# more and the first and last characteristics are same from a given list of strings.

# Sample list = 
'''
#Solution type-3
numbers = [59, 47, 7, 17, 45]
larg=numbers[0]
for i in numbers:
  if i > larg:
    larg=i
print(larg)
'''
'''
#Solution type-4
numbers = [59, 47, 7, 17, 45]
larg=numbers[0]
[larg:=i for i in numbers if i > larg]
print(larg)
'''
# *********************************************************************
# Question:- 3
'''
#Solution type-1
cars = ['Ford', 'BMW', 'Volvo', 'a', 'aba', 989, '1221']
newlist =[]
for elem in cars:
  elem=str(elem)
  if len(elem) > 1 and elem[0] == elem[-1]:
    newlist.append(elem)
print(newlist)
'''
'''
#Solution type-2
cars = ['Ford', 'BMW', 'Volvo', 'a', 'aba', 989, '1221']
newlist = [elem for elem in cars if len(str(elem)) > 1 and str(elem)[0] == str(elem)[-1]]
print(newlist)
'''
# *********************************************************************
# Question:- 4
'''
#Solution type-1
cars = ['Ford', 'BMW', 'Ford', 'a', 'aba', 'BMW', '1221']
cars =list(set(cars))
print(cars)
'''
# *********************************************************************
# Question:- 5
'''
#Solution type-1
cars = []
if len(cars):
    print("Not Empty")
else:
    print("Empty")
'''
'''
#Solution type-2
cars = []
if len(cars) > 0:
    print("Not Empty")
else:
    print("Empty")
'''
'''
#Solution type-3
cars = []
print("Not Empty") if len(cars) > 0 else print("Empty")
'''
'''
#Solution type-4
cars = []
print("Not Empty") if len(cars) else print("Empty")
'''
'''
#Solution type-5
cars = []
if cars:
    print("Not Empty")
else:
    print("Empty")
'''
# *********************************************************************
# Question:- 6
'''
#Solution type-1
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index = [0, 4, 5]
index.sort(reverse=True)
for i in index:
    color.pop(i) # also use this instead of color.pop(i)-> del color[i]
print(color)
'''
'''
#Solution type-2
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index = [0, 4, 5]
index.sort(reverse=True)
[color.pop(i) for i in index] # also use this instead of color.pop(i)-> del color[i]
print(color)
'''
# *********************************************************************
# Question:- 7
'''
# Solution type-1
numers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numers:
    if i % 2 == 0:
        numers.remove(i)
print(numers)
'''
'''
# Solution type-2
numers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[numers.remove(i) for i in numers if i % 2 == 0]
print(numers)
'''
# *********************************************************************
# Question:- 8
'''
# Solution type-1
stringlist = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
string ="".join(stringlist)
print(string)
'''
'''
# Solution type-2
stringlist = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
string =""
for ch in stringlist:
    string += ch
print(string)
'''
# *********************************************************************
# Question:- 9
'''
# Solution type-1
numbers = [12, 35, 1, 10, 34, 1] #[50, 56, 34, 35, 12]
numbers.sort()
print("firstlasg=", numbers[-1], "secondlarg=", numbers[-2])
'''
'''
# Solution type-2
numbers = [50, 56, 34, 35, 12] #[12, 35, 1, 10, 34, 1]
firstlasg = numbers[0]
secondlarg = numbers[1]
for i in range(1, len(numbers)):
    if numbers[i] > firstlasg:
        secondlarg = firstlasg
        firstlasg = numbers[i]
    elif numbers[i] > secondlarg and secondlarg < firstlasg:
        secondlarg = numbers[i]
print("firstlasg=", firstlasg, "secondlarg=", secondlarg)
'''
# *********************************************************************
# Question:- 10 same as ques no.- 4
