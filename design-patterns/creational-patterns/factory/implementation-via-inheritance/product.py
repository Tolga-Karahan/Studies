from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "ConcreteProduct1 operation"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "ConcreteProduct2 operation"
