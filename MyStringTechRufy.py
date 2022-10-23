"""by TechRufy"""


class MyString(str):

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj = obj.upper()
        return obj


c = MyString("cia342o")

print(c)
