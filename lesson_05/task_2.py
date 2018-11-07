class ConstAttributeError(Exception):
    pass


class Const(type):

    def __setattr__(self, name, value):
        raise ConstAttributeError


class MyClass(metaclass=Const):
    x = 37


MyClass().a = 12
print(MyClass.x)
try:
    MyClass.x = 10
except ConstAttributeError:
    print("ConstAttributeError")
