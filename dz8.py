"""
Создайте класс Animal и разные производные от него подклассы: Fox, Bird,
Cat, Dog и т.п. Реализуйте у них общий метод say(), который бы возвращал
звукб издаваемый этими животными. Создайте кортеж из нескольких этих
экземпляров классов, переберите их в цикле и выведите в консоль.
"""


class Animal:
    @staticmethod
    def say():
        raise NotImplementedError("В классе необходима реализация "
                                  "метода say()")


class Fox(Animal):

    @staticmethod
    def say():
        print("Fox say: 'Ring-ding-ding-ding-dingeringeding! "
              "Gering-ding-ding-ding-dingeringeding!'")


class Bird(Animal):
    @staticmethod
    def say():
        print("Bird goes tweet")


class Cat(Animal):
    @staticmethod
    def say():
        print("Cat goes meow")


class Dog(Animal):
    @staticmethod
    def say():
        print("Dog goes woof")


class Fish(Animal):
    @staticmethod
    def say():
        print("Fish go blub")


class Mouse(Animal):
    @staticmethod
    def say():
        print("Mouse goes squeek")


class Cow(Animal):
    @staticmethod
    def say():
        print("Cow goes moo")


class Frog(Animal):
    @staticmethod
    def say():
        print("Frog goes croak")


animals = (Frog, Cow, Mouse, Fish, Dog, Cat, Bird, Fox)

for f in animals:
    f.say()
