""" 

Scrivere nel file esercizio1.py una funzione che prende in input una sequenza di richieste
(numeri) e passa ciascuna richiesta ad una catena di gestori ciascuno dei quali e` una
coroutine.

• Se il numero è compreso tra 0 e 100 allora la richiesta viene gestita dal gestore
gestore_0_100 che stampa “Richiesta {} gestita da gestore_0_100”.
• Se il numero è compreso tra 101 e 200 allora la richiesta viene gestita dal gestore
gestore_101_200 che stampa “Richiesta {} gestita da gestore_101_200”.
• Se il numero comincia con un numero negativo allora la richiesta viene gestita dal
gestore gestore_negativo che smette di funzionare immediatamente dopo aver
stampato “Richiesta {} gestita da gestore_negativo: la catena smette di funzionare”.
• Se il numero è maggiore di 200, allora la richiesta viene gestita dal gestore
gestoreDiDefault che stampa “Messaggio da gestoreDiDefault: non e` stato possibile
gestire la richiesta {}".

Se un gestore tenta di inviare una richiesta al suo successore e si accorge che questo
ha smesso di funzionare allora anch’esso deve smettere di funzionare.
NB: nelle suddette stampe la richiesta (il numero) deve comparire al posto delle parentesi
graffe.


"""

import functools
def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def gestoreDiDefault(successor):
    while True:
        num=yield
        if(num >200):
            print(f"Messaggio da gestoreDiDefault: non e` stato possibilegestire la richiesta {num}")
       

@coroutine
def gestore_0_100(richiesta):
    while True:
        num=yield
        if(num >=0 and num <= 100):
            print(f"Richiesta {num} gestita da gestore_0_100")
        else:
            try:
                richiesta.send(num)
            except StopIteration:
                break
            

@coroutine
def gestore_101_200(successor):
    while True:
        num=yield
        if(num >=101 and num <= 200):
            print(f"Richiesta {num} gestita da gestore_101_200")
        else:
            try:
                successor.send(num)
            except StopIteration:
                break
@coroutine
def gestore_negativo(successor):
        while True:
            num=yield
            if(num <= 0):
                print(f"Richiesta {num} gestita da gestore_negativo: la catena smette di funzionare")
                break

            else:
                try:
                    successor.send(num)
                except StopIteration:
                    break
                


class Client:
        '''Client: Uses handlers'''
        def __init__(self):
            self.handler = gestore_0_100(gestore_101_200(gestore_negativo(gestoreDiDefault(None))))
        def delegate(self, requests):
                '''Iterates over requests and sends them, one by one, to handlers as per sequence of handlers defined above.'''
                for request in requests:
                    try:
                        self.handler.send(request)
                    except:
                        print("La catena ha smesso di accettare richieste")
                        
                self.handler.close()
# Create a client object
cliente = Client()
 
# Create richieste to be processed.
richieste = []



richieste=[101,99,300,-1,5]

cliente.delegate(richieste)


"""
Il programma stampa:
Richiesta 101 gestita da gestore_101_200
Richiesta 99 gestita da gestore_0_100
Messaggio da gestoreDiDefault: non e` stato possibile gestire la richiesta 300
Richiesta -1 gestita da gestore_negativo: la catena smette di funzionare
La catena ha smesso di accettare richieste
La catena ha smesso di accettare richieste

"""
