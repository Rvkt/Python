# This is a module called `my_module.py`

class MyClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name, 'and i am', self.age, "years old.")
