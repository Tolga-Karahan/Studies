from computer import Computer


class Server(Computer):
    def __init__(self, cpu, ram, disk, purpose):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.purpose = purpose

    def __str__(self):
        return f"{self.__class__.__name__}:\n\tcpu:{self.cpu}\n\tram:{self.ram}\n\tdisk:{self.disk}\n\tpurpose:{self.purpose}"
