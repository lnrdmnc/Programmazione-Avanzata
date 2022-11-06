

def decoratoreDiClasse(cls):
    def elencaVariabili(self):
        for arg in self.__dict__.values():
            if isinstance(arg,int):
                yield arg
    setattr(cls,"elencaVariabili",elencaVariabili)
    return cls

@decoratoreDiClasse
class C():
    def __init__(self):
        self.a=2
        self.b=3
        self.c="w"
        print(self.__dict__.values())


c=C()

it=c.elencaVariabili()
for i in it:
    print(i)