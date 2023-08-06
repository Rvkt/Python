def my_function(x):
  return list(dict.fromkeys(x))

mylist = ["a", "b", "a", "c", "c", "d"]


mylist1 = my_function(mylist)

print(mylist1)