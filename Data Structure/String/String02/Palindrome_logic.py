# Palindrome logic
while 1:
    txt1 = input('Enter String: ')
    if txt1 == 'exit':
        exit()
    else:
        txt2 = txt1[-2::-1]
        txt3 = f'{txt1}{txt2}'
        print(txt3)