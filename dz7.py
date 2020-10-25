"""Создайте базовый класс Стол и дочерние: Прямоуголный столы и Круглыстолы.
Через конструктор базового класса передайте размер поверхности стола: для прямоуголного
 - ширина и длина, для круглого - радиус. В дочерних классах реализуйте метод
 вычисления площади поверхности стола."""

from math import pi

""" импорт числа пи для расчета площади круглых столов"""


class Table:
    """ Main class Tables """
    def __init__(self, x, width=0):
        """ Общий конструктор размеров стола """
        if width == 0:
            self._x = x
        else:
            self._x = x
            self._width = width


class Rectangular(Table):
    """ Прямоугольные столы """
    def area(self):
        """ Площадь прямоугольного стола """
        print(self._x * self._width)


class Circle(Table):
    """ Крыглые столы """
    def area(self):
        """ Вычисление площади круглого стола """
        print(pi * (pow(self._x, 2)))


rect = Rectangular(10, 20)
rect.area()
round1 = Circle(5)
round1.area()
