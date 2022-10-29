class Commesso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "il commesso  {}".format(self.nome)

    def vende(self, merce):
        return "vende {}".format(merce)


class Musicista:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "il musicista  {}".format(self.nome)

    def suona(self, tipoMusica):
        return "suona {}".format(tipoMusica)


class Cuoco:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "il cuoco  {}".format(self.nome)

    def cucina(self, pietanza):
        return "cucina {}".format(pietanza)
