# Program to sum all the prime numbers in a list

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

for n in primeNum:
    if n < 0:
        pass
    else:
        sum = 0
        while n > 0:
            sum += n
            n -= 1

print(f'Sum of numbers is: {sum}')





