# str = input('Enter the string:\n')

# sourcery skip: avoid-builtin-shadow
str = 'abcdefghijklmnopqrstuvwxyz'

# camelcase the indices of the given string
def camelCase(str):
    sorted_str = []
    for i in range(len(str)):
        if i % 2 != 0:
            sorted_str.append(str[i].upper())
        else:
            sorted_str.append(str[i].lower())
    print(''.join(sorted_str))

camelCase(str)

# camelcase the indices of the given reversed string
def camelCaseRev(str):
    rev_str = str[::-1]
    sorted_str = []
    for i in range(len(rev_str)):
        if i % 2 != 0:
            sorted_str.append(rev_str[i].upper())
        else:
            sorted_str.append(rev_str[i].lower())
    print(''.join(sorted_str))

camelCaseRev(str)