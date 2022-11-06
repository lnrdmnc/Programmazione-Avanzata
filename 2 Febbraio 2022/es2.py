

def decoraClasse(cls):
    oldInit =cls.__init__
    def newInit(self,*args,**kwargs):
        self.tupla=(*(arg for arg in args),*(key for key in kwargs.items()))
        oldInit(self,*args,**kwargs)
    cls.__init__=newInit

    def conQualiArgomenti(self):
            return self.tupla
    setattr(cls,"conQualiArgomenti",conQualiArgomenti)

    return cls

@decoraClasse
class C():
    def __init__(self,*args,**kwargs):
        pass

c=C(10,"a","b",*[9,11],k1=3,k2="pop",**{"k3":"pippo"})

print(c.conQualiArgomenti())
