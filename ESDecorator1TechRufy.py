def ControlloStringhe(function):
    def wrapper(*args):
        for arg in args:
            if type(arg) != str:
                raise TypeError

        return function(*args)

    return wrapper


@ControlloStringhe
def FuncString(*args):
    risultato = ""
    stringa = ""
    for arg in args:
        risultato += arg

    for arg in args:
        arg += " "
        stringa += arg

    return stringa + risultato


print(FuncString("il", "sei", "un", "coglione"))
