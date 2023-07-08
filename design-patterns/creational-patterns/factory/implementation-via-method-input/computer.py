from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def __str__() -> str:
        pass
