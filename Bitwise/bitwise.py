print(1234)

print(4*1 + 3*10 + 2*100 + 1*1000)

print(4*10**0   + 3*10**1   + 2*10**2   + 1*10**3)

print(0b1101)   # Output 13

# right to left to deciper the bin number

1*2**0    + 0*2**1    + 1*2**2    + 1*2**3    # Output 13

x = 0b11001011    #Output 203
y = 0b10101101    #Output 173

print(x, y)

# Bitwise AND -- use &
# if both of them is 1, we get 1

# x = 0b11001011
# y = 0b10101101

#     0b10001001

print(x & y, bin(137))

# Bitwise OR  -- use |
# if one of them is 1, then we get 1

# x = 0b11001011
# y = 0b10101101

#     0b11101111

print(x | y, bin(239))

# Bitwise XOR -- use ^
# if one of them is 1, but not both, then we get 1

# x = 0b11001011
# y = 0b10101101

#     0b01100110

print(x ^ y, bin(102))