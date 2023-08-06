given_string = input('Enter a string: ')

even_chars = []
odd_chars = []

for i in range(len(given_string)):
    if i % 2 == 0:
        even_chars.append(given_string[i])
    else:
        odd_chars.append(given_string[i])


odd_chars = ''.join(odd_chars)
# odd_chars = (odd_chars).upper()
print(odd_chars)

even_chars = ''.join(even_chars)
print(even_chars)

txt = (odd_chars, even_chars)
txt = ''.join(txt)
print(txt)