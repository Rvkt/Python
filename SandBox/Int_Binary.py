def int_to_binary(integer):
    binary_string = ''
    while integer > 0:
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    return binary_string


print(int_to_binary(123))

a = 5
b = 4

print(f'{a & b}')
