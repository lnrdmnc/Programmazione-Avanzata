class MyClass():
        def __init__(self,x):
            self.x=x

        def somma(self,y):
            return self.x+y

        def stampa(self):
            print(self.x)

class MyProxy():
    def __init__(self,x):
        self.__myClass=MyClass(x)
    def __getattr__(self, item):
        return getattr(self.__myClass,item)

p=MyProxy(3)

p.stampa()
print(p.somma(2))