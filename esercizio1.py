"""
Scrivere uno script in cui vengono importati alcuni moduli
tra quelli forniti da Python e in cui poi viene effettuata la ricerca di una certa funzione a vostra scelta. 
Lo script non deve lanciare eccezioni e non ne deve catturare." 

"""


import sys
import math

#in dir sys ci sta tutto il name space
for arg in dir(sys):
    if(arg=="getsizeof"):
        print("Ho trovato la funzione:",arg)

    


#nome funzione: oggetto
for arg in vars(math):
    if(arg=='sqrt'):
        print("ho trovato",arg)
        break



from copy import * 
from os import *
from math import *
#questo serve per non farti dare RunTime Error
k=0
for k in vars():
    if(k=='sqrt'):
        print('ho trovato z',k)
        break

from math import *
from copy import *

#un altro trucco per evitare che il namespace cambi di taglia in questo caso si ha una copia del namespace in quel momento e non va  a cambiare il namespace perde tutto ciò che viene dopo la prima iterazione
#alla prima iterazione si hanno 1000 elementi e alla seconda diventano 1001
d=vars().copy()
for k,v in d.items():
    if(k=='sqrt'):
        print('ho trovato {}nel modulo {}'.format(k,v.__module__))



