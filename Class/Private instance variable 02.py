# Python program to demonstrate how to access private members of the parent class.
class C(object):
    def __init__(self):
        self.a = 3
        self.b = 9
        self.c = 27
        # d is private instance variable
        self.__d = 81


# class D have access to all the attributes of class C except attribute d.
class D(C):
    def __init__(self):
        self.e = 243
        self.__f = 729
        C.__init__(self)


# class E have access to all the attributes of class D except attribute f.
class E(D):
    def __init__(self):
        self.__g = 2187
        D.__init__(self)


object1 = D()
object2 = E()


print(object1.a)
print(object1.b)
print(object1.c)

#  You can access private variables with print(object._class__attribute)
print(object1._C__d)
print(object1.e)

#  You can access private variables with print(object._class__attribute)
print(object1._D__f)
print(object2._E__g)

