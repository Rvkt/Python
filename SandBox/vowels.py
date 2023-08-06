sentence = input('Enter the sentence:\n')

string = sentence.lower()

print(string)

count = 0

vowels = ['a', 'e', 'i', 'o', 'u']

for i in string:
    print(i)
    if i in vowels:
        count += 1


print(count)

