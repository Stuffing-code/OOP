class NoDateDescr:
    def __set_name__(self, owner, name):
        self.n__name = name

    def __get__(self, instance, owner):
        return "NoDateDescr __get__"

class CoordValue:  #descriptor
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value



class Point:
    nodate = NoDateDescr()
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt = Point(1, 2)
print(pt.coordX, pt.coordY)
pt = Point(100, 32)
print(pt.coordX, pt.coordY)

