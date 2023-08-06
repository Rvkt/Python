# Program:- 1
'''
list1 = ['m', 'na', 'i', 'li']
list2 = ["y", "me", "s", "st"]
list3 = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        list3.append(list1[i]+list2[i])
else:
    print("Both list length are different")
print(list3)
'''
# *********************************************************************
# Program:- 2
'''
list1 = [1, 2, 3, 4, 5]
list3 = [i**2 for i in list1]
print(list3)
'''
# *********************************************************************
# Program:- 3
'''
list1 = ['Hellow', 'take']
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i+' '+j)
print(list3)
'''
# *********************************************************************
# Program:- 4
'''
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
if len(list1) == len(list2):
    for i in range(len(list1)):
        print(list1[i] , list2[i])
else:
    print("Both list length are different")
'''
# *********************************************************************
# Program:- 5
'''
list1 = ["this", " ", "is", "python", "programming", " "]
list1.remove(" ")
print(list1)
'''
# *********************************************************************
# Program:- 6
'''
list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []
duplicateitem = set()
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        duplicateitem.add(i)

for i in duplicateitem:
    list2.remove(i)
print(list2)
'''
# *********************************************************************
# Program:- 7
'''
numbers = [1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in numbers:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
print("Even:- ", even)
print("Odd:- ", odd)
'''
#********************************************************************
# Program:- 8
'''
colors = [['Red'], ['Green'], ['Black']]
for i in colors:
  print(i)
'''
#********************************************************************
# Program:- 10
'''
numbers = [1,2,3,4,5,6,7,8,9, 12, 11, 30, 31]
s=0
for i in numbers:
  flag = 0
  if i == 1 or i == 2:
    s += i
    continue
  else:
    for j in range(2, i):
      if i%j == 0:
        flag = 1
        break
    if flag == 0:
      s += i
print(s)
'''
#********************************************************************
# Program:- 9
'''
def negativeFilter(v):
    if v < 0:
        return True
    else:
        return False


list = [-1, -10, 100, 5, 61, -2, -23, 8, -90, 51]

negativeElements = filter(negativeFilter, list)
for elem in negativeElements:
    print(elem)
'''