"""

Scrivere nel file esercizio1.py un decoratore di classe myDecorator che dota la classe
decorata di un metodo di istanza contaVarClasse che prende in input un tipo t e
restituisce il numero di variabili di classe di tipo t della classe. Il codice della classe non
deve essere modificato.

"""

def myDecorator(cls):
	def contaVarClasse(self,t):
		numero = 0
		for arg in vars(cls).values():
			if(type(arg)==t):
				print(arg)
				numero=numero+1
		return numero
	setattr(cls, "contaVarClasse", contaVarClasse)
	return cls



@myDecorator
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



@myDecorator
class classeD(classeB):
      interoClasseD1=4
      interoClasseD2=21
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

z=classeD()
print("numero di variabili della classe  classeD di tipo int =",z.contaVarClasse(int))
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
numero di variabili della classe  classeD di tipo int = 2
invochiamo method1 su z
numero di variabili della classe  classeD di tipo int = 2
numero di variabili della classe classeD di tipo classeB = 0
numero di variabili della classe  classeD di tipo dict = 0
numero di variabili della classe  classeB di tipo int = 1
invochiamo method2 su z
numero di variabili della classe  classeD di tipo int = 2
numero di variabili della classe classeD di tipo classeB = 0
numero di variabili della classe  classeD di tipo dict = 0
numero di variabili della classe  classeB di tipo int = 1

"""
