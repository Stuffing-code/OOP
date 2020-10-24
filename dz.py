class DayValue:  # descriptor
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError("not int value")


class Calendar:
    days = DayValue()
    months = DayValue()
    years = DayValue()

    def __init__(self, day, month, year):
        if day <= 31 and day >= 0:
            self.days = day
        else:
            raise ValueError("Day is not true")

        if month <= 12 and month >= 0:
            self.months = month
        else:
            raise ValueError("Month is not true")

        self.years = year


pt = Calendar(31, 12, 2020)
print(pt.days, pt.months, pt.years)
pt2 = Calendar(1, 130, 2020)
print(pt2.days, pt2.months, pt2.years)
