
class Cls():
    inv=0

    def __getattribute__(self, item):
        Cls.inv+=1
        return super(Cls, self).__getattribute__(item)

    def metodo(self):
        print("Ciao")

    def metodo2(self):
        print("Ciao2")


c=Cls()
c.metodo()
c.metodo2()
print(c.inv)