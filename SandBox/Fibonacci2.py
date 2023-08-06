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
