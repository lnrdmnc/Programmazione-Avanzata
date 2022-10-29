"""Definire un decoratore di funzione che trasforma una funzione che prende in input un numero variabile di numeri in una
funzione che prende in input una lista e opera solo sugli elementi della lista di tipo float, int e str convertiti in int."""


def DecConvertitore(funz):
    def wrapper(*args, **kwargs):
        L = []
        for arg in args:
            for elem in arg:
                if isinstance(elem, str):
                    L.append(int(elem))
                elif isinstance(elem, int) or isinstance(elem, float):
                    L.append(elem)
        print(L)
        return funz(*L)

    return wrapper


@DecConvertitore
def somma(*args):
    tot = 0
    for arg in args:
        tot += arg

    return tot


print(somma([1, 2, 3, 4,"anna",45.5]))