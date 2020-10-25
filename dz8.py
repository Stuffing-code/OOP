"""
Создайте класс Animal и разные производные от него подклассы: Fox, Bird,
Cat, Dog и т.п. Реализуйте у них общий метод say(), который бы возвращал
звукб издаваемый этими животными. Создайте кортеж из нескольких этих
экземпляров классов, переберите их в цикле и выведите в консоль.
"""
from playsound import playsound
"""Импорт библиотеки для запуска мп3 файла"""


class Animal:
    @staticmethod
    def say():
        raise NotImplementedError("В классе необходима реализация "
                                  "метода say()")


class Fox(Animal):
    @staticmethod
    def say():
        playsound("C:\\Users\\Stuffing\\PycharmProjects\\pythonProject\\OOP\\fox_say.mp3")
        print("Fox say: 'Ring-ding-ding-ding-dingeringeding! "
              "Gering-ding-ding-ding-dingeringeding!'")


class Bird(Animal):
    @staticmethod
    def say():
        print("Bird say: 'tweet'")


class Cat(Animal):
    @staticmethod
    def say():
        print("Cat say: 'meow'")


class Dog(Animal):
    @staticmethod
    def say():
        print("Dog say: 'woof'")


class Fish(Animal):
    @staticmethod
    def say():
        print("Fish say: 'blub'")


class Mouse(Animal):
    @staticmethod
    def say():
        print("Mouse say: 'squeek'")


class Cow(Animal):
    @staticmethod
    def say():
        print("Cow say: 'moo'")


class Frog(Animal):
    @staticmethod
    def say():
        print("Frog say: 'croak'")


animals = (Frog, Cow, Mouse, Fish, Dog, Cat, Bird, Fox)

for f in animals:
    f.say()
