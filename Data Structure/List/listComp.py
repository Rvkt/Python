# list comprehension

fruits = ['apples', 'bananas', 5]

str_fruits = [i.upper() for i in fruits if type(i) == str]

print(str_fruits)
