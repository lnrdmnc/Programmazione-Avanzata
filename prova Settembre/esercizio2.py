"""

Modificare l’esercizio al punto 1 in modo che il decoratore myDecorator possa essere
parametrizzato con un intero n e che il metodo di istanza contaVarClasse conti le
variabili di tipo t non solo della classe decorata ma delle prime n classi nella gerarchia
formata dalla classe decorata e dalle sue superclassi, le prime n secondo l’ordine
indicato in __mro__ . Se il numero di classi nella suddetta gerarchia è minore di n allora
vengono considerate tutte le classi nella gerarchia.
Scrivere il codice nel file esercizio2.py.

"""

def myDecorator(n:int):
    def wrapper(cls):
        def contaVarClasse(self,t):
            numero=0
            for v in vars(cls).values():
                if isinstance(v,t):
                    numero+=1

            cls_mro=cls.mro()
            mro_len=len(cls_mro)

            if mro_len < n:
                for c in cls_mro[1:]:
                    numero+=1
            else:
                tmp=cls_mro[1:n+1]
                for c in tmp:
                    for b in vars(c).values():
                        numero+=1
            return numero
        setattr(cls, "contaVarClasse", contaVarClasse)
        return cls
    return wrapper





@myDecorator(3)
class classeB:
	interoClasseB=3
	
	def method1(self):
		self.interoI1=6
		self.d=dict({'bob': 4139})
		self.b1=classeB()
		self._a=3
		

	def method2(self):
		self.d2=dict({'jack': 4098, 'sape': 4139})
		self.interoI2=5
		self.b2=classeB()
		self.d4=dict({'jack1': 4098, 'sape1': 4139})
		classeB.dictClasseB=dict({'jack1': 9, 'sape1': 6})


@myDecorator(4)
class classeD(classeB):
      interoClasseD1=4
      interoClasseD2=21
      def __init__(self):
              self.b=classeB()

@myDecorator(4)
class classeF(classeD):
      classeD.dictClasseD=dict({'jack1': 9, 'sape1': 6})
      interoClasseF1=4
      interoClasseF2=21
      def __init__(self):
              self.b=classeB()              

@myDecorator(3)
class classeH(classeF):
      interoClasseH1=4
      interoClasseH2=21
      def __init__(self):
              self.b=classeB() 
x=classeB()
print("numero di variabili della classe  classeB di tipo int =",x.contaVarClasse(int))
print("numero di variabili della classe  classeB di tipo dict =",x.contaVarClasse(dict))
print("invochiamo method1 su x")
x.method1()
print("numero di variabili della classe  classeB di tipo int =",x.contaVarClasse(int))
print("numero di variabili della classe  classeB di tipo dict =",x.contaVarClasse(dict))
print("numero di variabili della classe classeB di tipo classeB =",x.contaVarClasse(classeB))
print("invochiamo method2 su x")
x.method2()
print("numero di variabilidella classe  classeB di tipo dict =",x.contaVarClasse(dict))
print("numero di variabili della classe  classeB di tipo dict =",x.contaVarClasse(dict))
print("numero di variabili della classe classeB di tipo classeB =",x.contaVarClasse(classeB))
print()
z=classeD()
print("numero di variabili della classe  classeD di tipo int =",z.contaVarClasse(int))
print("numero di variabili della classe classeD di tipo classeB =",z.contaVarClasse(classeB))
print("numero di variabili della classe  classeD di tipo dict =",z.contaVarClasse(dict))
print("numero di variabili della classe  classeB di tipo int =",x.contaVarClasse(int))
print("invochiamo method1 su z")
z.method1()
print("numero di variabili della classe  classeD di tipo int =",z.contaVarClasse(int))
print("numero di variabili della classe classeD di tipo classeB =",z.contaVarClasse(classeB))
print("numero di variabili della classe  classeD di tipo dict =",z.contaVarClasse(dict))
print("numero di variabili della classe  classeB di tipo int =",x.contaVarClasse(int))
print("invochiamo method2 su z")
z.method2()
print("numero di variabili della classe  classeD di tipo int =",z.contaVarClasse(int))
print("numero di variabili della classe classeD di tipo classeB =",z.contaVarClasse(classeB))
print("numero di variabili della classe  classeD di tipo dict =",z.contaVarClasse(dict))
print("numero di variabili della classe  classeB di tipo int =",x.contaVarClasse(int))
print()
w=classeF()
print("numero di variabili della classe  classeF di tipo int =",w.contaVarClasse(int))
print("invochiamo method1 su w")
w.method1()
print("numero di variabili della classe  classeF di tipo int =",w.contaVarClasse(int))
print("numero di variabili della classe classeF di tipo classeB =",w.contaVarClasse(classeB))
print("numero di variabili della classe  classeF di tipo dict =",w.contaVarClasse(dict))
print("invochiamo method2 su w")
w.method2()
print("numero di variabili della classe  classeF di tipo int =",w.contaVarClasse(int))
print("numero di variabili della classe classeF di tipo classeB =",w.contaVarClasse(classeB))
print("numero di variabili della classe  classeF di tipo dict =",w.contaVarClasse(dict))
print("numero di variabili della classe  classeD di tipo int =",z.contaVarClasse(int))

print()
r=classeH()
print("numero di variabili della classe  classeH di tipo int =",r.contaVarClasse(int))
print("invochiamo method1 su r")
r.method1()
print("numero di variabili della classe  classeH di tipo int =",r.contaVarClasse(int))
print("numero di variabili della classe classeH di tipo classeB =",r.contaVarClasse(classeB))
print("numero di variabili della classe  classeH di tipo dict =",r.contaVarClasse(dict))
print("invochiamo method2 su r")
r.method2()
print("numero di variabili della classe  classeH di tipo int =",r.contaVarClasse(int))
print("numero di variabili della classe classeH di tipo classeB =",r.contaVarClasse(classeB))
print("numero di variabili della classe  classeH di tipo dict =",r.contaVarClasse(dict))



"""Il programma deve stampare :
numero di variabili della classe  classeB di tipo int = 1
numero di variabili della classe  classeB di tipo dict = 0
invochiamo method1 su x
numero di variabili della classe  classeB di tipo int = 1
numero di variabili della classe  classeB di tipo dict = 0
numero di variabili della classe classeB di tipo classeB = 0
invochiamo method2 su x
numero di variabilidella classe  classeB di tipo dict = 1
numero di variabili della classe  classeB di tipo dict = 1
numero di variabili della classe classeB di tipo classeB = 0

numero di variabili della classe  classeD di tipo int = 3
numero di variabili della classe classeD di tipo classeB = 0
numero di variabili della classe  classeD di tipo dict = 2
numero di variabili della classe  classeB di tipo int = 1
invochiamo method1 su z
numero di variabili della classe  classeD di tipo int = 3
numero di variabili della classe classeD di tipo classeB = 0
numero di variabili della classe  classeD di tipo dict = 2
numero di variabili della classe  classeB di tipo int = 1
invochiamo method2 su z
numero di variabili della classe  classeD di tipo int = 3
numero di variabili della classe classeD di tipo classeB = 0
numero di variabili della classe  classeD di tipo dict = 2
numero di variabili della classe  classeB di tipo int = 1

numero di variabili della classe  classeF di tipo int = 5
invochiamo method1 su w
numero di variabili della classe  classeF di tipo int = 5
numero di variabili della classe classeF di tipo classeB = 0
numero di variabili della classe  classeF di tipo dict = 2
invochiamo method2 su w
numero di variabili della classe  classeF di tipo int = 5
numero di variabili della classe classeF di tipo classeB = 0
numero di variabili della classe  classeF di tipo dict = 2
numero di variabili della classe  classeD di tipo int = 3

numero di variabili della classe  classeH di tipo int = 6
invochiamo method1 su r
numero di variabili della classe  classeH di tipo int = 6
numero di variabili della classe classeH di tipo classeB = 0
numero di variabili della classe  classeH di tipo dict = 1
invochiamo method2 su r
numero di variabili della classe  classeH di tipo int = 6
numero di variabili della classe classeH di tipo classeB = 0
numero di variabili della classe  classeH di tipo dict = 1

"""
