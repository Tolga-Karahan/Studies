from abc import ABC, abstractmethod

from car import Car
from car_manual import CarManual


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_engine(self, engine: str):
        pass

    @abstractmethod
    def set_number_of_seats(self, n_seats: int):
        pass

    @abstractmethod
    def set_gps(self, has_gps: bool):
        pass

    @abstractmethod
    def set_trip_computer(self, has_trip_computer: bool):
        pass


class CarBuilder(Builder):
    _car: Car

    def __init__(self):
        self.reset()

    @property
    def car(self):
        car = self._car
        self.reset()
        return car

    def reset(self):
        self._car = Car()
        return self

    def set_engine(self, engine: str):
        self._car.engine = engine
        return self

    def set_number_of_seats(self, n_seats):
        self._car.n_seats = n_seats
        return self

    def set_gps(self, has_gps: bool):
        self._car.has_gps = has_gps
        return self

    def set_trip_computer(self, has_trip_computer: bool):
        self._car.has_trip_computer = has_trip_computer
        return self


class CarManualBuilder(Builder):
    _car_manual: CarManual

    def __init__(self):
        self.reset()

    @property
    def car_manual(self):
        car = self._car_manual
        self.reset()
        return car

    def reset(self):
        self._car_manual = Car()
        return self

    def set_engine(self, engine: str):
        self._car_manual.engine = engine
        return self

    def set_number_of_seats(self, n_seats):
        self._car_manual.n_seats = n_seats
        return self

    def set_gps(self, has_gps: bool):
        self._car_manual.has_gps = has_gps
        return self

    def set_trip_computer(self, has_trip_computer: bool):
        self._car_manual.has_trip_computer = has_trip_computer
        return self
