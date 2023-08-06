string = 'lengthofthestring'
count = 0

for i in string:
    count = count + 1

print("The length of a list is", count)

"""*2. Write a python program to count the number of characters(character frequency) in a string.*



"""

str = "google.com"

for i in range(0, len(str)):
    print(str[i], str.count(str[i]))

str = 'google.com'
edict = {}
for i in str:
    if i in edict.keys():
        edict[i] += 1
    else:
        edict.update({i:1})

print(edict)

"""*3. Write a python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.*"""

txt = 'restart'

print(txt.find(txt[0], 1))

print(txt[0] + txt[1:].replace(txt[-2], '$'))

"""*4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.*"""

str = 'abc, xyz'

str1 = str.split(", ")

print(str1[0].replace('ab', 'xy') + str1[1].replace('xy', 'ab'))

print(str1[0].replace(str1[0][0], str1[1][0]))

"""*5. Write a Python program to change a given string where the first and last chars have been exchanged.*

*6. Write a Python program to remove the characters which have odd index values of a given string.*
"""

txt = '123456789'

print(txt[0::2])

for i in range(len(txt)):
  if i % 2 != 0:
    print(txt[i])

"""*7. write a Python program to count the occurrences of each word in a given sentence.*"""

str = 'The quick brown fox jumps over the lazy dog'

# str_list = str.split(' ')
edict = {}
for i in str.split(' '):
    if i in edict.keys():
        edict[i] += 1
    else:
        edict.update({i:1})

print(edict)