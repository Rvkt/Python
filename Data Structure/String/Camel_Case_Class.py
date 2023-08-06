class StringMethods:

    def __init__(self, str):
        self.str = str

    def camelCase(self):
        return ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(self.str))

    def camelCase_rev(self):
        return ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(self.str[::-1]))




# sourcery skip: avoid-builtin-shadow
str = 'hello world'


strfunc = StringMethods(str)

print(strfunc.camelCase())
print(strfunc.camelCase_rev())
