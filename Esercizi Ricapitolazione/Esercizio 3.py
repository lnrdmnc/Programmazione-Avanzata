def decoratore(cls):
    cls.istanze=0

    def __init__(self):
        self.aggiornaIstanze()
    cls.__init__=__init__

    @classmethod
    def aggiornaIstanze(cls):
        cls.istanze+=1
    setattr(cls,"aggiornaIstanze",aggiornaIstanze)

    @classmethod
    def getIstanze(cls):
        return cls.istanze
    setattr(cls,"getIstanze",getIstanze)

    return cls

@decoratore
class classe():
    pass

c=classe()
print(c.getIstanze())
d=classe()
print(d.getIstanze())
