# Create and stop an iteration

month = []


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 12:
            x = self.a
            self.a += 1
            return str(x).zfill(2)
        else:
            raise StopIteration


myiter = iter(MyNumbers())

for x in myiter:
    month.append(x)

print(month)