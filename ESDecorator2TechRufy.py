def contaVarClasse(ClasseA):
    def wrapper(self, t):

        occorrenze = 0
        for arg in ClasseA.__dict__:
            if arg == "__module__" or arg == "__doc__" or arg == "__name__":
                continue

            p = vars(ClasseA).get(arg)

            if type(p) == t:
                occorrenze += 1

        return occorrenze

    ClasseA.contaVar = wrapper

    return ClasseA


@contaVarClasse
class ClasseB:
    a = 4
    b = "rona"
    c = "ciao"


@contaVarClasse
class ClasseC:
    a = 5
    t = 4
    i = 90


w = ClasseC()
q = ClasseB()
print(w.contaVar(int))
