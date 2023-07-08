from abc import ABC, abstractmethod

from product import Product, ConcreteProduct1, ConcreteProduct2


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def operation(self) -> str:
        product = self.factory_method()
        return product.operation()


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
