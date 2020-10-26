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

        self.__x = x
        self.__y = y
        self.__z = z

    #TODO: 1. +, 2. -, 3. *, 4. /.
    def __add__(self, other):


    #TODO: сравнение через ключи


    #TODO: запись считывание через ключи



x1 = Point3D(1.1, 2, 3)
