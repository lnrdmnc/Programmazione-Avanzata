class C():
    _shared_state={}
    class TaleEQuale1():
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls, *args, **kwargs)
            obj.__dict__ =cls._shared_state
            return obj
    class TaleEQuale2():
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls, *args, **kwargs)
            obj.__dict__ = cls._shared_state
            return obj
    class Diversa(TaleEQuale1, TaleEQuale2):
        _shared_state={}
        def __new__(cls,*args,**kwargs):
            obj=super().__new__(cls,*args,**kwargs)
            obj.__dict__=cls._shared_state
            return obj
    c=TaleEQuale1()
    c.a=5
    d = TaleEQuale2()
    print(d.a)

