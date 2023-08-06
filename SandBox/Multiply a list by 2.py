def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


def power2(li):
    new_list2 = []
    for item in li:
        new_list2.append(item ** 2)
    return new_list2


print(multiply_by2([1, 2, 3]))
print(power2([2, 3, 4]))
