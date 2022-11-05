"""Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo che
restituisce il numero d'invocazioni del metodo passato come parametro al decorator factory."""


def Contatore(funcD, funcU):
    def Wrapper(*args, **kwargs):
        funcU()

        return funcD(*args, **kwargs)

    return Wrapper


def DecoratorFactory(func):
    def Wrapper(cls):
        name = "numeroInvocazioni" + func
        setattr(cls, name, 0)

        @classmethod
        def count(classe):
            valore = classe.__dict__.get(name)
            valore += 1
            setattr(cls, name, valore)

        setattr(cls, "count", count)

        @classmethod
        def Count(classe, func):
            print(classe.__dict__.get("numeroInvocazioni" + func))

        setattr(cls, "Count", Count)

        setattr(cls, func, Contatore(cls.__dict__.get(func), cls.count))

        return cls

    return Wrapper


@DecoratorFactory("__init__")
@DecoratorFactory("prova")
class ClasseBase:

    def __init__(self):
        self.t = 3

    def prova(self):
        print("prova" + str(self.t))

    def prova2(self):
        pass


C = ClasseBase()
T = ClasseBase()

C.prova()
C.prova()
C.prova()
C.prova()
C.prova2()
C.prova2()
C.prova2()
C.Count("__init__")
