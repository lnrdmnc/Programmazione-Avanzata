"""
Scrivere nel file esercizio3.py una coroutine invia(n,destinatario) che prende in input un
carattere x e una coroutine destinatario e si comporta come segue: ogni volta che riceve
un testo, cerca al suo interno le stringhe che cominciano con x e le invia al destinatario.
Scrivere inoltre una coroutine scrive(nome_file) che ogni volta che riceve una stringa
la inserisce nel file di nome nome_file seguita da uno spazio. Il parametro
destinatario e` una coroutine scrive.


Suggerimento: potete usare re.findall(r'\w+', testo) per estrarre parole da testo
"""
import functools
import re

def coroutine(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		generator = function(*args, **kwargs)
		next(generator)
		return generator
	return wrapper

@coroutine
def invia(x,destinatario):
	while True:
		testo=yield
		stringa=re.findall(r'\w+',testo)
		for arg in stringa:
			if arg.startswith(x):
				destinatario.send(arg)

@coroutine
def scrive(nome_file):
	while True:
		try:
			testo=yield
			with open(nome_file,'a+') as f:
				f.write(testo+" ")
		except FileNotFoundError:
			print("Errori sul file")




def main(): 
	mittenti=[invia('a',scrive("file1")),invia('P',scrive("file2")),invia('m',scrive("file3"))]

	for s in mittenti:
		s.send("mela pera ananas Arancia cocomero anguria Anguria ciliegia cocomero melone Papaya")


	for s in mittenti:
		s.send("verza cavolo Peperone melanzana Melanzana Pomodoro pomodoror")
 
	for s in mittenti:
		s.close()

if __name__ == "__main__":
    main()


