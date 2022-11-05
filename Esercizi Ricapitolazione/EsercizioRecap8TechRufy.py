"""Scrivere una classe che contiene un metodo che restituisce il numero d'invocazioni degli altri
metodi della classe. Il codice dei suddetti metodi non deve essere modificato."""


def Contatore(funcD, funcU):
    def Wrapper(*args, **kwargs):
        funcU()

        return funcD(*args, **kwargs)

    return Wrapper


def Decoratorfactory(cls):
    cls.numInvocazioni = 0

    @classmethod
    def count(classe):
        classe.numInvocazioni += 1

    setattr(cls, "count", count)

    @classmethod
    def StampaInvocazioni(classe):
        print(classe.numInvocazioni)

    setattr(cls, "StampaInvocazioni", StampaInvocazioni)

    for key, func in cls.__dict__.items():
        if callable(func) and key != "StampaInvocazioni":
            setattr(cls, key, Contatore(func, cls.count))

    return cls


@Decoratorfactory
class Base:

    def __init__(self):
        self.c = 10

    def StampaRoba(self):
        print("ciao " + str(self.c))

    def Prove(self):
        print("hello")


b = Base()



