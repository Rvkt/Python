# 1. Take input of 'a','d' and 'n'
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))
n = int(input("Enter the value of n: "))
 
apSeries = []

# 2. Loop for n terms
for i in range(1,n+1):
    t_n = a + (i-1)*d
    apSeries.append(t_n)

# 3. Sum of first n terms
S_n = (n/2)*(2*a + (n-1)*d)


print(f'Arithmetic Progression Series: {apSeries}.')
print(f'Sum of first {n} terms: {S_n}')