"""
напишите класс Point3D для хранения координат в трехмерном пространстве (x, y, z)
Реализуйте перегрузку операторов сложения, вычитания, умножения и деления для этого
класса. Так же сделайте возможность сравнения координат между собой и запись\считывание
значений через ключи: 'x', 'y', 'z'.
"""


class Point3D:
    def __init__(self, x, y, z):
        """
        конструктор создания координат в 3х мерном пространстве
        :param x: координата
        :param y: координата
        :param z: кооордината
        """
        if not (
                (isinstance(x, int) or isinstance(x, float))
                and (isinstance(y, int) or isinstance(y, float))
                and (isinstance(z, int) or isinstance(y, float))
        ):
            raise ValueError("Координаты должны быть числами")
        self.__coord = (x, y, z)

    def get_Coord(self):
        """
        :return: обращение к кортежу координат
        """
        return self.__coord

    @staticmethod
    def checkPoint3D(x):
        """
        Проверка на причасность к данному классу
        :param x: other из функций для произведения математических расчетов
        :return: выводит ошибку если заданы неверные параметры
        """
        if not isinstance(x, Point3D):
            raise ArithmeticError("Правый операнд должен быть типа Point3D")

    """Реализация математических операций координат"""

    def __add__(self, other):
        """
        функция сложения
        :param other: второй кортеж координат
        :return: вызывает коснтруктор класса на основе списка total
        total - список сумм двух кортежей
        """
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] + other.get_Coord()[i])
        return Point3D(*total)

    def __sub__(self, other):
        """
        функция вычитания
        :param other: второй кортеж координат
        :return: вызывает коснтруктор класса на основе списка total
        total - список разности двух кортежей
        """
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] - other.get_Coord()[i])
        return Point3D(*total)

    def __mul__(self, other):
        """
        функция умножения
        :param other: второй кортеж координат
        :return: вызывает коснтруктор класса на основе списка total
        total - список произведений двух кортежей
        """
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] * other.get_Coord()[i])
        return Point3D(*total)

    def __truediv__(self, other):
        """
        функция деления
        :param other: второй кортеж координат
        :return: вызывает коснтруктор класса на основе списка total
        total - список  частное двух кортежей
        """
        Point3D.checkPoint3D(other)
        total = []
        for i in range(len(self.__coord)):
            total.append(self.__coord[i] / other.get_Coord()[i])
        return Point3D(*total)

    """Реализация сравнения координат"""

    def __eq__(self, other):
        return self.__coord == other.get_Coord()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__coord < other.get_Coord()

    def __gt__(self, other):
        return self.__coord > other.get_Coord()

    def __le__(self, other):
        return self.__coord <= other.get_Coord()

    def __ge__(self, other):
        return self.__coord >= other.get_Coord()

    """Реализация вызова координат по ключам"""

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "x":
            return self.__coord[0]
        elif item == "y":
            return self.__coord[1]
        elif item == "z":
            return self.__coord[2]

        return "Неверный ключ"

    """Реализация записи координат по ключам"""

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        x = self.__coord[0]
        y = self.__coord[1]
        z = self.__coord[2]

        if key == "x":
            self.__coord = (value, y, z)
        elif key == "y":
            self.__coord = (x, value, z)
        elif key == "z":
            self.__coord = (x, y, value)

        return "Неверный ключ"


x1 = Point3D(1, 4, 3)
x2 = Point3D(1, 2, 3)
x3 = x1 - x2
print(x3.get_Coord())
if x1 > x2:
    print("x1>x2")
print(x1["z"])
x1["z"] = 2
print(x1['z'])
