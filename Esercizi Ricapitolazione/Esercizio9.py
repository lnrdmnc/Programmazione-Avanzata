from functools import wraps


def decFact(metodo):
    def decoratore(cls):
        name=metodo+"_count"
        setattr(cls,name,0)
        met=getattr(cls,metodo)
        def newMetodo(*args,**kwargs):
            setattr(cls,name,getattr(cls,name)+1)
            met(*args,**kwargs)
        setattr(cls,metodo,newMetodo)
        return cls
    return decoratore


@decFact("metodo")
@decFact("metodo2")
class Cls():
    def __init__(self):
        pass
    def metodo(self):
        print("Ciao")
    def metodo2(self):
        print("Ciao2")

c=Cls()
c.metodo()
c.metodo2()
print(c.metodo_count)
print(c.metodo2_count)

