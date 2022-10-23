"""
Modificare la classe al punto precedente in modo tale che le istanze abbiano al piu`due variabili d'istanza: varA
e varB e non deve essere possibile aggiungere altre variabili d'istanza oltre a queste due. Se il programma avesse
bisogno di aggiungere altre variabili oltre a quelle sopra indicate, queste altre variabili verrebbero create come
variabili di classe e non d'istanza.
By TechRufy
"""


class C:

    def __init__(self):
        self.varB = None
        self.varA = None

    def __setattr__(self, key, value):
        if key == "varA" or key == "varB":
            super(C, self).__setattr__(key, value)

        return setattr(C, key, value)


c = C()
d = C()

d.varA = 200
c.varA = 1000

c.varC = 23

print(d.varA, c.varA, c.varC, d.varC)
