"""

Scrivere nel file esercizio4.py una funzione applica(cose_da_fare) che prende in input
una tupla cose_da_fare che contiene tuple della forma (metodo, arg1,arg2,…) dove
metodo è un metodo di istanza di una certa classe C e arg1, arg2,… sono gli argomenti diversi da self con cui deve essere invocato metodo. Nella prima di queste tuple,
metodo è la classe C e gli argomenti sono quelli che applica deve passare al costruttore per creare un’istanza di C.
Una volta creata un'istanza di C, la funzione applica invoca i metodi delle restanti tuple di cose_da_fare sui relativi argomenti.
Alla fine la funzione applica restituisce una lista contenente i valori restituiti dalle invocazioni dei suddetti metodi.

"""


def applica(cose_da_fare):
    construttore=cose_da_fare[0][0]
    print(construttore)
    argomenti=cose_da_fare[0][1:]
    print(argomenti)
    oggetto=construttore(*argomenti)


    list=[]

    for funzione, *argomenti in cose_da_fare[1:]:
        list.append(funzione(oggetto,*argomenti))
        return list




























class MyClass:
    val = 8
    def f(self, x, y):
        return x + y

    def g(self, *args):
        return args[0] * args[1] + MyClass.val

class AnotherClass:
    def __init__(self,v):
        self.val=v
        
    def f(self,x,y):
        return x+y
    def g(self,*args):
        return args[0]*args[1]+self.val

def main():
    
    cose_da_fare1=((MyClass,),(MyClass.f,"a","bc"),(MyClass.g,3,9))
    cose_da_fare2=((AnotherClass,10),(AnotherClass.f,9,11),(AnotherClass.g,7,8))
    l_1=applica(cose_da_fare1)
    l_2= applica(cose_da_fare2)
    print("questo e` il contenuto di l_1:",l_1)
    print("questo e` il contenuto di l_2:",l_2)    
    
if __name__=='__main__':
    main()




"""Il programma deve stampare:
questo e` il contenuto di l_1: ['abc', 35]
questo e` il contenuto di l_2: [20, 66]
"""
