"""Definire un decoratore di classe che permette alla classe decorata di contare le sue istanze. """


def ContaIstanz(aClass):
    aClass.numInstances = 0
    oldInit = aClass.__init__

    def __newInit__(self, *args, **kwargs):
        aClass.numInstances += 1
        oldInit(self, *args, **kwargs)

    aClass.__init__ = __newInit__
    return aClass


@ContaIstanz
class ClasseProva:
    pass


for i in range(10):
    l = []
    i = ClasseProva()
    l.append(i)

print(l[0].numInstances)
