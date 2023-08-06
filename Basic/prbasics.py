# Reverse string

def my_function(x):
  return x[::-1]

string = input("Enter String: ")
gnirts = my_function(string)
print(f'Reverse of {string} is {gnirts}.')

"""Python Iterators"""

# Tuple iteration
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Tuple iteration with for loop

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# String iteration

mystr = "red"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

# String iteration with for loop
mystr1 = "string"

for x in mystr1:
  print(x)

# Create and stop an itertaion

month = []

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 12:
      x = self.a
      self.a += 1
      return str(x).zfill(2)
    else:
      raise StopIteration

# myclass = MyNumbers()
myiter = iter(MyNumbers())

for x in myiter:
  month.append(x)

print(month)

from datetime import date, datetime
now = datetime.now()
month = (now.strftime('%m').zfill(2))
print(month)

import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_long = []

for i in range(1, 13):
    month_long.append(calendar.month_name[i]) # month_name is an array
for i in month_long:
    print(f'{year}{i[0:3].upper()}')

import calendar
from datetime import date, datetime

now = datetime.now()
year = now.strftime('%Y')
month_short = calendar.month_abbr[1:]

for i in month_short:
    print(f'{year}{i.upper()}')

from datetime import datetime
import calendar

now = datetime.now()
yr = now.strftime('%Y')
month = []
month2 = calendar.month_abbr[1:]
yearmonth = []
yearmonth2 = []

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 12:
      x = self.a
      self.a += 1
      return str(x).zfill(2)
    else:
      raise StopIteration
      
for x in iter(MyNumbers()):
    month.append(x)
for i in month:
    yearmonth.append(f'{yr}{i}')
for i in month2:
  yearmonth2.append(f'{yr}{i.upper()}')


for i in iter(yearmonth):
    print(i)
print(' ')
for i in iter(yearmonth2):
    print(i)

# Palindrome logic

def reverse_str(str):
    str1 = str[::-1]
    print(f'Original string {str} and Reversed string {str1}.')

def palindrome(str):
    txt2 = str[-2::-1]
    txt3 = f'{str}{txt2}'
    print(f'Palindrome of the given string is: {txt3}.')

reverse_str('123')
palindrome('abc')

string = 'abc'

def reverse(str):
    str1 = str[::-1]
    print(f'{str1}')

reverse(string)

def camelCase(str):
    sorted_str = []
    for i in range(len(str)):
        if i % 2 == 0:
            sorted_str.append(str[i].upper())
        else:
            sorted_str.append(str[i].lower())
    print(''.join(sorted_str))

camelCase(string)

def camelCase_rev(str):
    rev_str = str[::-1]
    sorted_str = []
    for i in range(len(rev_str)):
        if i % 2 == 0:
            sorted_str.append(rev_str[i].upper())
        else:
            sorted_str.append(rev_str[i].lower())
    print(''.join(sorted_str))

camelCase_rev(string)

def palindrome(str):
    txt2 = str[-2::-1]
    txt3 = f'{str}{txt2}'
    print(f'Palindrome of the given string is: \n----> {txt3}.')

palindrome(string)