# Join string in python

# ___________________________________________________

# Solution: 1
s1_first_string = 'ABC'
s1_second_string = '123'

s1_output_list = []
i = 0

for a in s1_first_string:
    s1_output_list.append(a)
    while 1 < len(s1_first_string):
        s1_output_list.append(s1_second_string[i])
        i += 1
        break

s1_output = ''.join(s1_output_list)

# ___________________________________________________

# Solution: 2
s2_first_string = 'ABC'
s2_second_string = '123'
s2_output = ''

for (a, b) in zip(s2_first_string, s2_second_string):
    s2_output += a + b

# ___________________________________________________

# Solution: 3
s3_first_string = 'ABC'
s3_second_string = '123'
s3_output = ''

for i in range(len(s3_first_string)):
    s3_output += s3_first_string[i] + s3_second_string[i]

# ___________________________________________________

print(f'Solution 1: {s1_output}')
print(f'Solution 2: {s2_output}')
print(f'Solution 3: {s3_output}')

# ___________________________________________________

# OUTPUT
# Solution 1: A1B2C3
# Solution 2: A1B2C3
# Solution 3: A1B2C3

