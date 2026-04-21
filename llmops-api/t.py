print('123')
from injector import inject, Injector


class A:
    name: str = 'str'



@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def printName(self):
        print(self.a.name)


injector = Injector()
b = injector.get(B)
b.printName()
