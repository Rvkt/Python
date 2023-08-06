txt1 = input('  Enter String: ')
text2 = f"{txt1[-1::-1]}"
str = []
for i in range(len(text2)):
    if i % 2 == 0:
        str.append(text2[i].upper())
    else:
        str.append(text2[i].lower())
print(''.join(str))