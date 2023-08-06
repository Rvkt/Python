# Sets are written with curly brackets.
'''
myset = {"apple", "banana", "cherry"}
print(myset)
'''


# Sets cannot have two items with the same value.
'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
'''


# To determine how many items a set has, use the len() function.
'''
len_set = {"apple", "banana", "cherry"}
print(len(len_set))
'''


# Set items can be of any data type:
'''
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
'''


# A set can contain different data types:
'''
set1 = {"abc", 34, True, 40, "male"}
'''


# What is the data type of a set?
'''
type_set = {"apple", "banana", "cherry"}
print(type(type_set))
'''


# It is also possible to use the set() constructor to make a set.
'''
create_set = set(("apple", "banana", "cherry")) # note the double round-brackets
print(create_set)
'''



'''

# Python - Access Set Items

as you cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop,
or ask if a specified value is present in a set, by using the in keyword.

'''





thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)