"Primo esempio di decoratore: Il decoratore di Classe"

"Come prima cosa definiamo una funzione alla quale passeremo la classe che vogliamo decorare"

from functools import wraps


def MyDecorator(Cls):

    #codice 
    pass
    return Cls

#Decoratore di funzione alla quale si passa la funzione che vogliamo decorare

def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        pass
        #pass
    return wrapper

#decorator factory che non è niente altro che un decorator che prende in input un parametro parametrizzato e al suo interno contiene un decoratore di funzione o un decoratore di classe e lo restituisce 
def decF(i:int):
    def MyDecorator(Cls):
        pass
        #code
        return Cls
    return MyDecorator

def decF(i:int):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            pass
            #code
        return wrapper
    return decorator



        