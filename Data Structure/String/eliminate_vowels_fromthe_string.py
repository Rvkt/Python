string = 'Hello John'

str_vowels = ['a', 'e', 'i', 'o', 'u']

def eliminate_vowels(string):
    
    for i in string:
        if i.lower() in str_vowels:
            string = string.replace(i, '_')
    print(string)

eliminate_vowels(string)