keys = {'a', 'b', 'c'}
value = 'Letter'
dictionary = dict.fromkeys(keys, value)
print(dictionary)


keys1 = {'A', 'B', 'C'}
value1 = [1]
vowels = dict.fromkeys(keys1, value1)
print(vowels)
value1.append(2)
print(vowels)


# vowels keys
keys2 = {'a', 'e', 'i', 'o', 'u' }
value2 = [1]

# creates dictionary using dictionary comprehension
vowels2 = { key : list(value2) for key in keys2 }

print(vowels2)

# updates the value list
value2.append(2)

print(vowels2)