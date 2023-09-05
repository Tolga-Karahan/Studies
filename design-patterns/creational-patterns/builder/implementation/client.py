from builders import CarBuilder
from director import Director

if __name__ == "__main__":
    car_builder = CarBuilder()
    director = Director(car_builder)

    print(director.build_car())
