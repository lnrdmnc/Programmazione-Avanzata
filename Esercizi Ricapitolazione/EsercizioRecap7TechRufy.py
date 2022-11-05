class ClsBase:

    @classmethod
    def adAttr(cls, s, v):
        for key, arg in cls.__dict__.items():
            if key == s:
                return

        setattr(cls, s, v)


class ClsDer(ClsBase):
    pass


c = ClsBase()

ClsBase.adAttr("boh", 3)

print(c.boh)
ClsDer.adAttr("cosa", 5)

print(ClsDer.cosa)
