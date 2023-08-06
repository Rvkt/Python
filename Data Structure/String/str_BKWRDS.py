string = 'abcdefghijklmnopqrstuvwxyz'

# Reverse the given string
def bkwrds(x):
    return x[::-1]

print(f'Given String is {string} \nand\nthe reverse of the string is: {bkwrds(string)}')

print(f'\nPalindrome of the given string: \n{string[:-1]}{bkwrds(string)}')