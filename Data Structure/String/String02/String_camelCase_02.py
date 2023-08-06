# sourcery skip: avoid-builtin-shadow
given_str = 'hello world'
str = []
for i in range(len(given_str)):
    if i % 2 == 0:
        str.append(given_str[i].upper())
    else:
        str.append(given_str[i].lower())
        sorted_str = ''.join(str)
print(''.join(str))