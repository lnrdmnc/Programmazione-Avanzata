def apply(due_things):
    i=0
    for arg in due_things:
        if(i==0):
            c, *args = due_things.__getitem__(0)
            cl = c(*args)
            i+=1
        else:
            func,*args=arg
            function=getattr(c,func)
            function(cl,*args)


class C():
    def __init__(self,i,e):
        self.i=i
        self.e=e
    def metodo1(self,a):
        print(a)

t=((C,1,2),("metodo1",1))
apply(t)