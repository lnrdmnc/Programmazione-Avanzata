def decoratorFactory(t):
    def decoratoreDiClasse(cls):
        def elencaVariabili(self):
            for arg in self.__dict__.values():
                if isinstance(arg,t):
                    yield arg
        setattr(cls,"elencaVariabili",elencaVariabili)
        return cls
    return decoratoreDiClasse
@decoratorFactory(int)
class C():
    c=5
    def __init__(self):
        self.a=2
        self.b=3
        self.c="w"
        print(self.__dict__.values())


c=C()

it=c.elencaVariabili()
for i in it:
    print(i)