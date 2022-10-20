class C():

    def __setattr__(self, key, value):
        if self.__dict__.__len__()<2:
            self.__dict__[key]=value
        else:
            setattr(C,key,value)


c=C()
d=C()

c.varA=1
c.varB=2
c.varC=3
d.varA=3
d.varB=45
d.varF=234
print(d.__dict__)
print(c.__dict__)
print(C.__dict__)
