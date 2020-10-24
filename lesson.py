class Counter:
    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.value}")

    def reset(self):
        self.value = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display()  # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display()  # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display()  # печатает "Текущее значение счетчика = 4"
