# string = 'abcdefghijklmnopqrstuvwxyz'

# Joining String

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'zyxwvutsrqponmlkjihgfedcba'
c = '<[{(!@#$%^&*??*&^%$#@!)}]>'
d = '21098765432100123456789012'
out = ''.join(a[i]+b[i]+c[i]+d[i] for i in range(len(a)))
# out.strip()
print(out)


# Joining String

str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2 = 'zyxwvutsrqponmlkjihgfedcba'
str3 = '<[{(!@#$%^&*??*&^%$#@!)}]>'
str4 = '21098765432100123456789012'

print("".join([f"{i}{j}{k}{l}" for i, j, k, l in zip(str1, str2, str3, str4)]))
