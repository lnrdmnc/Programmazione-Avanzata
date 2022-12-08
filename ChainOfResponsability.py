import functools
def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        generator = function(*args,**kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def DefaultHandler(successor):
    while True:
        event= (yield)
        if (not isinstance(event, list) ) or (not isinstance(event[0],int) or not isinstance(event[1],int)) or (isinstance(event[0], int) and event[0]<0) or len(event)!=2:
            print("Richiesta {} gestita da Default_Handler: non e' stato possibile gestire la richiesta {}".format(event, event))
        elif successor is not None:
            successor.send(event)

@coroutine
def Handler_gt9(successor):
    while True:
        event= (yield)
        if isinstance(event[0], int) and isinstance(event[1], int) and event[0]>9 and len(event)==2:
            print("Messaggio da Handler_gt9: non e' stato possibile gestire la richiesta {}. Richiesta modificata".format(event))
            event[0]-=event[1]
            handler=Handler_04(Handler_59(Handler_gt9(DefaultHandler(None))))
            handler.send(event)
        elif successor is not None:
            successor.send(event)


@coroutine
def Handler_59(successor):
    while True:
        event= (yield)
        if isinstance(event[0], int) and 5 <= event[0] <= 9 and len(event)==2:
            print("Richiesta {} gestita da Handler_59".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def Handler_04(successor):
    while True:
        event= (yield)
        if isinstance(event[0], int) and 0 <= event[0] <= 4 and len(event)==2:
            print("Richiesta {} gestita da Handler_04".format(event))
        elif successor is not None:
            successor.send(event)

class Client:
    '''Client: Uses handlers'''

    def __init__(self):
        self.handler = Handler_04(Handler_59(Handler_gt9(DefaultHandler(None))))

    def delegate(self, requests):
        '''Iterates over requests and sends them, one by one, to handlers as per sequence of handlers defined above.'''
        for request in requests:
            self.handler.send(request)
        self.handler.close()


# Create a client object
cliente = Client()

# Create richieste to be processed.
richieste = []

for i in range(0, 15, 2):
    richieste.append([i, 7])
richieste.append([-3, 4])
richieste.append(["a", 2])
richieste.append([1, 2, 4])
cliente.delegate(richieste)


"""Il programma deve stampare:

Richiesta [0, 7] gestita da Handler_04
Richiesta [2, 7] gestita da Handler_04
Richiesta [4, 7] gestita da Handler_04
Richiesta [6, 7] gestita da Handler_59
Richiesta [8, 7] gestita da Handler_59
Messaggio da Handler_gt9:  non e' stato possibile gestire la richiesta [10, 7]. Richiesta modificata
Richiesta [3, 7] gestita da Handler_04
Messaggio da Handler_gt9:  non e' stato possibile gestire la richiesta [12, 7]. Richiesta modificata
Richiesta [5, 7] gestita da Handler_59
Messaggio da Handler_gt9:  non e` stato possibile gestire la richiesta [14, 7]. Richiesta modificata
Richiesta [7, 7] gestita da Handler_59
Richiesta [-3, 4] gestita da Default_Handler:  non e` stato possibile gestire la richiesta [-3, 4]
Richiesta ['a', 2] gestita da Default_Handler:  non e` stato possibile gestire la richiesta ['a', 2]
Richiesta [1, 2, 4] gestita da Default_Handler:  non e` stato possibile gestire la richiesta [1, 2, 4]
"""