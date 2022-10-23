"""
Scrivere un decoratore di classe che, se applicato a una classe, la modifica in modo che funzioni come
se fosse stata derivata dalla seguente classe base. N.B. le classi derivate da Classe Base non hanno bisogno di
modificare i metodi f() e g() e la variabile varC. Inoltre quando vengono create le istanze di una classe derivata
queste ’’nascono’’ con lo stesso valore di varI settato da __init__ di ClasseBase.
By TechRufy
"""


class ClasseBase:
    varC = 1000

    def __init__(self):
        self.varI = 10

    def f(self, v):
        print(v * self.varI)

    @staticmethod
    def g(x):
        print(x * ClasseBase.varC)


def ClasseBas(Class):
    setattr(Class, "varC", 1000)

    def __init__(self):
        self.varI = 10

    setattr(Class, "__init__", __init__)

    def f(self, v):
        print(v * self.varI)

    setattr(Class, "f", f)

    def g(x):
        print(x * Class.varC)

    g = staticmethod(g)

    setattr(Class, "g", g)
    return Class


@ClasseBas
class ClasseC(object):
    pass


c = ClasseC()

ClasseC.g(100)
