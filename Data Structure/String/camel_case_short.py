# sourcery skip: avoid-builtin-shadow
str = 'abcdefghijklmnopqrstuvwxyz'



def camelCase(str):
    return ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(str))

def camelCase_rev(str):
    return ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(str[::-1]))

print(camelCase(str))



'''
The def keyword defines a function called camelCaseRev.
The str parameter is the input string that will be converted to CamelCase format.
The return statement returns a string, which is the result of joining the characters in the c list together, with no spaces.
The c list is created using a list comprehension, which creates a list of characters, where every other character is capitalized.
The enumerate() method is used to get the index of each character in the string,
and then the i % 2 expression is used to determine whether to capitalize the character or not.
The str[::-1] expression reverses the order of the characters in the string.'''


def camelCase_rev(str):
    return ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(str[::-1]))

print(camelCase_rev(str))