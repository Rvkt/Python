string = 'abcdefghijklmnopqrstuvwxyz'



'''# Reverse the given string
def bkwrds(x):
    return x[::-1]

print(f'{string}')
print(f'{bkwrds(string)}')
print(f'Palindrome of the given string: \n{string[0:-1:]}{bkwrds(string)}')
'''


'''# camelcase the indices of the given string
def camelCase(str):
    sorted_str = []
    for i in range(len(str)):
        if i % 2 == 0:
            sorted_str.append(str[i].upper())
        else:
            sorted_str.append(str[i].lower())
    print(''.join(sorted_str))

camelCase(string)
'''


'''# camelcase the indices of the given reversed string
def camelCase_rev(str):
    rev_str = str[::-1]
    sorted_str = []
    for i in range(len(rev_str)):
        if i % 2 == 0:
            sorted_str.append(rev_str[i].upper())
        else:
            sorted_str.append(rev_str[i].lower())
    print(''.join(sorted_str))

camelCase_rev(string)
'''


# String to list conversion
string = 'abcdefghijklmnopqrstuvwxyz'

def list_str(x):
   return list(string)

print(list_str(string))



