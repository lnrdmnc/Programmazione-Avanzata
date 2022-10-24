def decoratorFactory(cls,funz="funz",ff="ff"):

    setattr(cls,funz,getattr(cls,ff))

    return cls

@decoratorFactory
class ClasseConFF():
    def funz(self):
        print("Invocato funz")

    def ff(self):
        print("Invocato ff")

c=ClasseConFF()

c.funz()
c.ff()