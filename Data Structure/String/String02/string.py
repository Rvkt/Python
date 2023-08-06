string = 'abcdefghijklmnopqrstuvwxyz'

def reverse(str):
    str1 = str[::-1]
    print(f'{str1}')

def camelCase(str):
    sorted_str = []
    for i in range(len(str)):
        if i % 2 == 0:
            sorted_str.append(str[i].upper())
        else:
            sorted_str.append(str[i].lower())
    print(''.join(sorted_str))

def camelCase_rev(str):
    rev_str = str[::-1]
    sorted_str = []
    for i in range(len(rev_str)):
        if i % 2 == 0:
            sorted_str.append(rev_str[i].upper())
        else:
            sorted_str.append(rev_str[i].lower())
    print(''.join(sorted_str))

print('')
print(string)
print('')
camelCase(string)
print('')
reverse(string)
print('')
camelCase_rev(string)