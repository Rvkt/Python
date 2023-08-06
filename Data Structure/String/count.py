string="A Paragraph is a series of related sentences Developing a Central idea"

upChar = []
lowChar = []

for i in string:
    if i.strip():
        if i == i.upper():
            upChar.append(i)
        else:
            lowChar.append(i)

# Strip check

print(upChar)
print(lowChar)

print(f'Number of Uppercase is {len(upChar)} and number of lowercase is {len(lowChar)}')