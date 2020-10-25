class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def isDigit(self):
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and (
                isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        return False

    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width

    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep

    def draw(self):
        raise NotImplementedError("Необходим метод draw()")

class Line(Prop):
    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")
    #
    # def __setOneCoord(self, sp):
    #     if sp.isInt():
    #         self._sp = sp
    #     else:
    #         print("Координаты должны быть целочислеными")
    #
    # def __setTwoCoords(self, sp, ep):
    #     if sp.isInt() and ep.isInt():
    #         Prop.setCoords(self, sp, ep)
    #     else:
    #         print("Координаты должны быть целочислеными")
    #
    # def setCoords(self, sp: Point, ep: Point = None):
    #     if ep is None:
    #         self.__setOneCoord(sp)
    #     else:
    #         self.__setTwoCoords(sp, ep)


class Rect(Prop):
    def draw(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


class Ellipse(Prop):
    def draw(self):
        print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


figs = []
figs.append(Line(Point(0, 0), Point(10, 10)))
figs.append(Line(Point(10, 10), Point(20, 10)))
figs.append(Rect(Point(50, 50), Point(100, 100)))
figs.append(Ellipse(Point(-10, -10), Point(10, 10)))

for f in figs:
    f.draw()
