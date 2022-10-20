def ClasseBase(cls):
    varC=1000
    setattr(cls,"varC",varC)

    def __init__(self):
        self.varl=100
    setattr(cls,"__init__",__init__)

    def f(self,v):
        print(v*self.varl)
    setattr(cls,"f",f)

    @staticmethod
    def g(x):
        print(x*varC)
    setattr(cls,"g",g)

    return cls

@ClasseBase
class classe():
    def __init__(self):
        super.__init__()

c=classe()

c.f(10)
c.g(23)
print(c.varl)
