from computer import Computer


class PC(Computer):
    def __init__(self, cpu, ram, disk):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk

    def __str__(self):
        return f"{self.__class__.__name__}:\n\tcpu:{self.cpu}\n\tram:{self.ram}\n\tdisk:{self.disk}"
