from builders import Builder


class Director:
    _builder: Builder

    def __init__(self, builder: Builder):
        self.builder = builder

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_car(self):
        (
            self._builder.set_engine("Ferrari F140")
            .set_number_of_seats(2)
            .set_gps(True)
            .set_trip_computer(True)
        )

        return self._builder.car

    def build_car_manual(self):
        (
            self._builder.set_engine("Lamborghini V12")
            .set_number_of_seats(2)
            .set_gps(True)
            .set_trip_computer(True)
        )

        return self._builder.car_manual
