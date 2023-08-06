string1 = "calvin klein design dress calvin klein"
words = string1.split()
print(" ".join(sorted(set(words), key=words.index)))
