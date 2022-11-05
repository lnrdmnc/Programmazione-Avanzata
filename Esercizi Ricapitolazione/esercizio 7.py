class ClsBase():
    @classmethod
    def addAttr(cls,s,v):
        try:
            getattr(cls,s)
        except:
            setattr(cls,s,v)

class ClsDer(ClsBase):
    pass

c=ClsBase()

c.addAttr("Ciao",5)
print(c.Ciao)

d=ClsDer()
d.addAttr("Pino",6)
print(d.Pino)