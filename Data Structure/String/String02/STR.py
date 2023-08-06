string = 'abcdefghijklmnopqrstuvwxyz'

#str_BKWRD = []
#camelCase_str = []
#camelCase_BKWD = []


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

print(string)
reverse(string)
camelCase(string)
camelCase_rev(string)