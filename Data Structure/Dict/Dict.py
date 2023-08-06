dict = {
    '1': ['A', 'B'],
    '2': ['C', 'D']
}
# update the dict
key3 = {3: ['E', 'F']}
dict.update(key3)

kv_list = []

for key in dict.keys():
    for value in (dict.get(key)):
        print(f'{key}{value}')
        kv_list.append(f'{key}{value}')


print(kv_list)
print(''.join(kv_list))