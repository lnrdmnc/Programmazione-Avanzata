class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj= obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


class Lavoratore:
    def __init__(self, nome):
        self.nome= nome
    def __str__(self):
        return"il lavoratore {}".format(self.nome)
    def lavora(self,lavoro):
        return"svolge il seguente {}".format(lavoro)

class Commesso:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return "il commesso  {}".format(self.nome)
    def vende(self, merce):
        return "vende {}".format(merce)

class Cuoco:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return "il cuoco  {}".format(self.nome)
    def cucina(self, pietanza):
        return "cucina {}".format(pietanza)

class Musicista:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return "il musicista  {}".format(self.nome)
    def suona(self, tipoMusica):
        return "suona {}".format(tipoMusica)


p=Commesso("Paolo")
adCommesso=Adapter(p,dict(lavora=p.vende))


m=Musicista("Veronica")
adMusicista=Adapter(m,dict(lavora=m.suona))

c=Cuoco("Antonio")
adCuoco=Adapter(c,dict(lavora=c.cucina))

print(adCommesso,adCommesso.lavora("abiti"))
print(adMusicista,adMusicista.lavora("musica poo"))
print(adCuoco,adCuoco.lavora("lasagna"))

