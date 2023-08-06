# -*- coding: utf-8 -*-
"""PyMaths.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bBMG_iIiBe3SLXlq0v4UE-IG9ABLHfpC
"""

import math

a = pow(5, 2)
print(f'Square of 5 is {a}.')

b = math.sqrt(25)
print(f'Square root of 25 is {b}.')
print(f'Square root of 25 is {int(b)}.')

c = math.ceil(1.4)
d = math.floor(1.4)
print(f'Rounds a number up to the nearest integer {c}')
print(f'Rounds a number down to the nearest integer {d}')

e = math.pi
print(e)

"""**Power Of the given number.**"""

n1 = int(input('Enter The number: '))
pr = int(input('Enter the power: '))
n2 = n1**pr
print(n2)

"""**LCM of three number V1**"""

A = int(input('Enter a number: '))
B = int(input('Enter a number: '))
C = int(input('Enter a number: '))

max_n = int(max(A,B,C))

print(max_n2)

while max_n > 0:
    if max_n % A == 0 and max_n % B == 0 and max_n % C ==0:
        lcm = max_n
        break
    else:
        max_n += 1

print(f'LCM of {A}, {B} & {C} is', max_n)

"""**LCM of three number V2**"""

A,B,C = input('enter a three numbers with space in between:\n').split(' ')

max_n = int(max(A,B,C))

while max_n > 0:
    if max_n % int(A) == 0 and max_n % int(B) == 0 and max_n % int(C) ==0:
        lcm = max_n
        break
    else:
        max_n += 1

print(f'LCM of {A}, {B} & {C} is', max_n)

"""**Factorial**"""

num = int(input("Enter Number: "))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(f'Factorial of {num} is {factorial(num)}.')

import math

num = int(input("Enter Number: "))
numFact = math.factorial(num)

print(numFact)

"""**Fibonacci Series 01**"""

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

"""**Fibonacci Series 02**"""

# Python program to display the Fibonacci sequence

def recursion_fibo(n):
    if n <= 1:
        return n
    else:
        return recursion_fibo(n - 1) + recursion_fibo(n - 2)


terms = int(input("How many terms?\n"))

# check if the number of terms is valid
if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(recursion_fibo(i))

"""**Leap Year**"""

year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

"""**Nested for loop**"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for row in adj:
    for col in fruits:
        print(row, col, end=' ')
    print()

"""**Prime numbers within an interval**"""

# Python program to display all the prime numbers within an interval

lower = int(input("Enter the lower limit of the interval:\n"))
upper = int(input("Enter the upper limit of the interval:\n"))

print(f'Prime numbers between {lower} and {upper} are:')

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

primeNum = []

for num in numList:
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primeNum.append(num)

print(f'Prime numbers from the list: {primeNum}')

for pn in primeNum:
    if pn < 0:
        pass
    else:
        sum = 0
        while pn > 0:
            sum += pn
            pn -= 1

print(f'Sum of numbers is: {sum}')

"""**Palindrome**"""

while 1:
    text_1 = input('Enter Text: \n')
    text_2 = text_1[-2::-1]
    join_txt = (text_1, text_2)
    join_txt = ''.join(join_txt)
    print(join_txt)

square = [i*i for i in range(1,11)]
print(square)

cube = [i*i*i for i in range(1,11)]
print(cube)

lower = int(input("Enter the lower limit of the interval:\n"))
upper = int(input("Enter the upper limit of the interval:\n"))

odd_Num = []
even_Num = []

for i in range(lower, upper+1):
    if i % 2 != 0:
        odd_Num.append(i)
    else:
        even_Num.append(i)
        

print(f'There are {len(odd_Num)} odd number between {lower} and {upper} is:\n{odd_Num}')
print(f'There are {len(even_Num)} even number between {lower} and {upper} is:\n{even_Num}')

odd = []
even = []

for i in range(1, 10+1):
    if i % 2 != 0:
        odd.append(str(i).zfill(3))
    else:
        even.append(str(i).zfill(3))

print(odd)
print(even)

odd = []
even = []

for i in range(100, 1):
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

print(odd)
print(even)

num = int(input("Enter the upper limit of the interval:\n"))

if num < 0:
    pass
else:
    sum = 0
    while num>0:
        sum += num
        num -= 1

    print(f'Sum of numbers is: {sum}')

num = int(input("Enter the number:\n"))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(num))

# Print the number that is multiple of 5, 7

fiveSeven = []

for i in range(1500, 2000):
    if i % 5 == 0 and i % 7 == 0:
        fiveSeven.append(i)

print(fiveSeven)