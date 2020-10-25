""""Создайте суперкласс «Персональные компьютеры» и на его основе подклассы: «Настольные ПК» и «Ноутбуки». В базовом
классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных классах уникальные свойства:

для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль;
для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль."""


class PersonalComputer:
    def __init__(self, memory: int, ssd: int, model: str, cpu: str):
        self._memory = memory
        self._ssd = ssd
        self._model = model
        self._cpu = cpu


class StationaryPc(PersonalComputer):
    def __init__(self, monitor: str, keyboard: str, mouse: str, *args):
        super().__init__(*args)
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    def demonstrationPC(self):
        print(f"Пк модели {self._model}, monitor {self._monitor}, mouse {self._mouse}, keyboard {self._keyboard},\
ssd обьем {self._ssd} Gb,на основе процессора {self._cpu},{self._memory}гб ОЗУ")


class Notebook(PersonalComputer):
    def __init__(self, display: int, weight: int,  *args):
        super().__init__(*args)
        self._display = display
        self._weight = weight

    def demonstrationNb(self):
        print(f"У ноутбука модели {self._model},диагональ экрана {self._display},вес {self._weight}\
,ssd обьем {self._ssd} Gb,на основе процессора {self._cpu},{self._memory}гб ОЗУ")


Ntb = Notebook(17, 56, 8, 256, "hp", "razen")
Ntb.demonstrationNb()
Pc = StationaryPc("dell", "razer", "red dragon", 64, 1000, "StuffingCo", "Intel core 7")
Pc.demonstrationPC()