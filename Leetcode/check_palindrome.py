# How to check if a string is a palindrome?


string = input("Enter the string:")

if string == string[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

print("It is a palindrome") if string == string[::-1] else print("it is not a palindrome")
