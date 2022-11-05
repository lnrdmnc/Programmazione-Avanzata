def decoratore(funz):
    def wrapper(*args,**kwargs):
        flag=0
        for arg in args:
            if not isinstance(arg,list) and flag==1:
                raise TypeError
            lista=arg
            flag=1
        for kwarg in kwargs:
            if not isinstance(kwarg,int) and flag==1:
                raise TypeError
            flag=1
        lis=[]
        for l in lista:
            if isinstance(l,int) or isinstance(l,float) or isinstance(l,str) and l.isdigit():
                lis.append(float(l))
        funz(*(el for el in lis))

    return wrapper

@decoratore
def funzione(*args):
    somma=0
    for arg in args:
        somma+=arg
    print(somma)

l=[1,"2",3.5,"w",[3,"d"],(3,"r"),5]

funzione(l)