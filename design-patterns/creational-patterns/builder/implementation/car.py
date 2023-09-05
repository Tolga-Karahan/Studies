class Car:
    _engine: str
    _n_seats: int
    _has_gps: bool
    _has_trip_computer: bool

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value: str):
        self._engine = value

    @property
    def n_seats(self):
        return self._n_seats

    @n_seats.setter
    def n_seats(self, value):
        self._n_seats = value

    @property
    def has_gps(self):
        return self._has_gps

    @has_gps.setter
    def has_gps(self, value):
        self._has_gps = value

    @property
    def has_trip_computer(self):
        return self._has_trip_computer

    @has_trip_computer.setter
    def has_trip_computer(self, value):
        self._has_trip_computer = value

    def __str__(self):
        return f"Car:\n\tEngine: {self.engine}\n\tNumber of seats: {self.n_seats}\n\tHas GPS: {self.has_gps}\n\tHas Trip Computer: {self.has_trip_computer}\n"
