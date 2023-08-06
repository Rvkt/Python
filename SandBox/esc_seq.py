myName = "My Name\nis \tHar\'ry"
print(myName)

print('\n')

letter = "Dear Harry,\n\tThis python course is nice.\nThanks"
print(letter)

print('\n')

formatted_letter = 'Dear harry,\n\tThis python course is nice.\nThanks!'
print(formatted_letter)

print('\nLetter Format')

letter1 = '''
Dear <|name|>,
you are selected!
<|date|>.
'''
name = input("Enter the name:\n ")
date = input("Enter the date:\n ")
letter1 = letter1.replace("<|name|>", name)
letter1 = letter1.replace("<|date|>", date)
print(letter1)

# print(template.replace('<|name|>', name).replace('<|date|>', date))
