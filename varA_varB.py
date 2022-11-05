
class C:

    __slots__=['varA','varB']

    def __init__(self):
        self.varA='varA'
        self.varB='varB'

    def __setattr__(self,name,value):
        if(name in C.__slots__):
            super(C,self).__setattr__(name,value)
        else:
            setattr(C,name,value)


c=C()

c.varA=10
c.varB=20

print(c.__dict__)


    


