given_str = input('Enter String: ')
str = []
for i in range(len(given_str)):
    if i % 2 == 0:
        str.append(given_str[i].upper())
    else:
        str.append(given_str[i].lower())
        sorted_str = ''.join(str)
print(sorted_str)

with open("strts.txt",'w',encoding = 'utf-8') as f:
   f.write(f'{sorted_str}')