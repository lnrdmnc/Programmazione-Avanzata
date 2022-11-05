def generatore(n):
    if not isinstance(n,int) or n<=0:
        raise TypeError
    somma=0
    for i in range(0,n):
        somma+=i
        yield somma

g=generatore(20)
for i in range(0,20):
    print(next(g))