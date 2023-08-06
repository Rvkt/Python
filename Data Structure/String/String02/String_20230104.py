# -*- coding: utf-8 -*-
txt= 'rohan-is-a-good-boy'

txt1= txt.split('-')

print(txt1)

TXT='HELLO%WORLD%%HELLO%'
# COUNT:- ”%”


x = TXT.count("%")

print(x)

# 1):- FIND ALL THE OCCURRENCES OF OF GIVEN SUBSTRING IN THE PROVIDED STRING

STR='TIGER IS A GOOD DOG AND DOG ARE FRIENDLY IN NATURE'
SUBSTRING="DOG"

print(STR.count(SUBSTRING))

# 2):- CREATE A STRING MADE OF THE FIRST, MIDDLE AND LAST CHARACTER:-

TXT="Hello World Welcome"

print(f'{TXT[0]}{TXT[2]}{TXT[4]}')

# CREATE A STRING MADE OF THE LAST CHARACTERS:-

TXT1="HELLO"
TXT2="WORLD"



print(f"{TXT[0]}{TXT1[1]}{TXT2[-1]}")

# 3):-  CREATE A STRING MADE OF THE LAST CHARACTERS:-
TXT="HELLO"
TXT1="WORLD"

print(f'{TXT[-1]}{TXT1[-1]}')

txt="jidfhuishdifnasdnfjhaiuenfijnadjksbnfjibdsafndsafindsanfnkjsanfjnbdafefe"

print(len(txt))



print(txt[len(txt) // 2 + 1])
print(txt[len(txt) // 2])