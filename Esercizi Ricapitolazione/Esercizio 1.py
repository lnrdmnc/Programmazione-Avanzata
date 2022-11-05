def fact(n: int):
    if n == 0:
        return 1
    return n * fact(n - 1)


def sublist(l: list, index: int):
    f = l.copy()
    for i in range(0, index):
        f.pop(i)
    return f


def permuta(l: list):
    if l.__len__() <= 1:
        return l
    if l.__len__() == 2:
        l.reverse()
        return l
    for i in range(0, l.__len__()):
        g = []
        f = []
        l[0],l[i]=l[i],l[0]
        g.append(l.__getitem__(i))
        t=permuta(sublist(l,1))
        if t.__len__() <= 2 :
            for j in range(0,t.__len__()):
                g.append(t.pop(0))
        else:
            g.append(t)
        f.append(g)

        return f

def funz(l: list):
    f = []
    f.append(l.copy())
    if(l.__len__()>2):
        g=permuta(l.copy())
        for i in range(0,g.__len__()):
            f.append(g.pop(0))
    return f


l = [1, 2, 3]

f = funz(l)
print(f)
