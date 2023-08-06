# Reverse the given string
def bkwrds(x):
    return x[::-1]

# camelcase the indices of the given string
def camelCase(str):
    sorted_str = []
    for i in range(len(str)):
        if i % 2 == 0:
            sorted_str.append(str[i].upper())
        else:
            sorted_str.append(str[i].lower())
    print(''.join(sorted_str))
    
# camelcase the indices of the given reversed string
def camelCaseRev(str):
    rev_str = str[::-1]
    sorted_str = []
    for i in range(len(rev_str)):
        if i % 2 == 0:
            sorted_str.append(rev_str[i].upper())
        else:
            sorted_str.append(rev_str[i].lower())
    print(''.join(sorted_str))