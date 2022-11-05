import EsercizioRecap6ImportTechRufy


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


class Lavoratore:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "il lavoratore {}".format(self.nome)

    def lavora(self, lavoro):
        return "svolge il seguente {}".format(lavoro)


t = Lavoratore("Paolo")
ad = Adapter(t, {"lavora": EsercizioRecap6Import.Commesso.__dict__.get("vende"),
                 "__str__": EsercizioRecap6Import.Commesso.__dict__.get("__str__")})

print(ad.__str__(ad.obj), ad.lavora(ad.obj, "abiti"))

m = Lavoratore("Veronica")
ad = Adapter(m, {"lavora": EsercizioRecap6Import.Musicista.__dict__.get("suona"),
                 "__str__": EsercizioRecap6Import.Musicista.__dict__.get("__str__")})

print(ad.__str__(ad.obj), ad.lavora(ad.obj, "musica pop"))

c = Lavoratore("Antonio")
ad = Adapter(c, {"lavora": EsercizioRecap6Import.Cuoco.__dict__.get("cucina"),
                 "__str__": EsercizioRecap6Import.Cuoco.__dict__.get("__str__")})

print(ad.__str__(ad.obj), ad.lavora(ad.obj, "una lasagna"))
