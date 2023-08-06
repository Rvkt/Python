# Fibonacci series 
# 0 1 1 2 3 5 8 13

fibonacii_memoization = {}

def fibonacci(n):
    # if the solution for the problem is avaliable in the 
    # fibonacii_memoization i.e. dictionary then take the solution
    # from here 
    
    if n in fibonacii_memoization:
        return fibonacii_memoization.get(n)
    
    # Compute the solution 
    # base condition
    if n == 1:
        value = 1
    # base condition
    elif n == 2:
        value = 2
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
    
    # Cache the value / save the value in fibonacii_memoization
    fibonacii_memoization[n] = value
    return value

for n in range(1,20):
    print(n,":",fibonacci(n))