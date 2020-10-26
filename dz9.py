"""
Создайте дочерний класс Motherboard, которая наследуеться
отк класов: CPU, GPU, Memory. В свою очередь CPU
наследуется от классов: AMD и Intel, GPU от классов
Nvidia, GeForce.

Создайте экземпляр класса Motherboard и наполните его конкретным содержимым( локальным
свойствам этого обьекта присвойте определенные значения). Определите вспомогательные методы в базовых
классах и выведите итоговую информацию в консоль с помощью метода showinfo()
класса Motherboard.
"""


class AMD:
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"AMD {self.model}"


class Intel:
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Intel {self.model}"


class Nvidia:
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Nvidia {self.model}"


class GeForce:
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"GeForce {self.model}"


class CPU(AMD, Intel):
    def __init__(self, cores: int, *args):
        super().__init__(*args)
        self.cores = cores


class GPU(Nvidia, GeForce):
    def __init__(self, cores: int, *args):
        super().__init__(*args)
        self.cores = cores


class Memory:
    def __init__(self, model: str, cores: int):
        self.model = model
        self.cores = cores

    def __str__(self):
        return f"Memory {self.model}, cores {self.cores}"


class Motherboard:
    def __init__(self, cpu: CPU, gpu: GPU, memory: Memory):
        super().__init__()
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory

    def showinfo(self):
        print(
            f"Motherboard info: \n"
            f"CPU модели {self.cpu.model} \n"
            f'GPU модели {self.gpu.model} \n'
            f'Memory модели {self.memory.model}, cores {self.memory.cores}'
        )


mb = Motherboard(CPU(1, AMD('Ryzen')),
                 GPU(2, GeForce('1080Ti')),
                 Memory("Kingston", 5)
                 )
mb.showinfo()
