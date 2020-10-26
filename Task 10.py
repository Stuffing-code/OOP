"""
напишите класс Point3D для хранения координат в трехмерном пространстве (x, y, z)
Реализуйте перегрузку операторов сложения, вычитания, умножения и деления для этого
класса. Так же сделайте возможность сравнения кооржинат между собой и запись\считывание
значений через ключи: 'x', 'y', 'z'.
"""


class Point3D:
    def __init__(self, x, y, z):
        if not (
                (isinstance(x, int) or isinstance(x, float))
                and (isinstance(y, int) or isinstance(y, float))
                and (isinstance(z, int) or isinstance(y, float))
        ):
            raise ValueError("Координаты должны числами")
        self.__coord = (x, y, z)

    def get_Coord(self):
        return self.__coord

    @staticmethod
    def checkPoint3D(x):
        if not isinstance(x, Point3D):
            raise ArithmeticError("Правый операнд должен быть типа Point3D")

    def __add__(self, other):
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] + other.get_Coord()[i])
        return Point3D(*total)

    def __sub__(self, other):
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] - other.get_Coord()[i])
        return Point3D(*total)

    def __mul__(self, other):
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] * other.get_Coord()[i])
        return Point3D(*total)

    def __truediv__(self, other):
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] / other.get_Coord()[i])
        return Point3D(*total)
    # TODO: сравнение через ключи

    # TODO: запись считывание через ключи


x1 = Point3D(1, 2, 3)
x2 = Point3D(1, 2, 3)
x3 = x1 + x2
print(x3.get_Coord())
