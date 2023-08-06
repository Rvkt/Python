# sourcery skip: avoid-builtin-shadow
str = ("hellojohn").upper()


def print_triangle(str):
  n = len(str)
  for i in range(n):
    for j in range(i + 1):
      print(str[j], end=" ")
    print()


print_triangle(str)
