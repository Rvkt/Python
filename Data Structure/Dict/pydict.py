# join two dict

dict1 = {'name': 'Ravi', 'age': 223416}
dict2 = {'class': 'xyz', 'course': 'python basics'}

dict1.update(dict2)
print(dict1)

dict3 = dict(dict1, **dict2)
print(dict3)

dict4 = {**dict1, **dict2}
print(dict4)

print({**dict1})


'''
# key check

dict3 = {'name': 'Ravi', 'age': 223416, 'class': 'xyz', 'course': 'python basics'}

if 'name' in dict3:
    print('exists')

for i in dict3:
    if i == 'name':
        print('Exists')
'''


'''
# print only keys of the dictionary

dict4 = {'name': 'Ravi', 'age': 223416, 'class': 'xyz', 'course': 'python basics'}

print(dict4.keys())
'''



'''
# List to dicttionary

list1 = ['name', 'roll number', 'class', 'course']
list2 = ['Ravi', 223416, 'xyz', 'python']

dict5 = {}

for a, b in zip(list1, list2):
    dict5.update({a: b})

print(dict5)


'''


'''
# Problem 7

dict = {
    '1': 'A',
    '2': 'B',
}
# update the dict
key = input('Enter to Add Key:')
value1 = input('Enter to Value:')
key3 = {key: value1}
dict.update(key3)

print(dict)
'''


'''
# Problem 8

def returnSum(dict):
 
    sum = 0
    for i in dict.values():
        sum = sum + i
 
    return sum
 
 
# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
'''


''' # Access items in dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)
print(people[1])
print(people[1]['name'])
'''
