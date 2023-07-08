from abc import ABC, abstractmethod

from product import ConcreteProduct1, ConcreteProduct2


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self) -> str:
        product = self.factory_method()
        return product.operation()


class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()
