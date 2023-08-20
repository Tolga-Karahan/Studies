class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


s1 = Singleton()
s2 = Singleton()

print(f"ID of first instance: {id(s1)}, ID of second instance: {id(s2)}")
print(f"ID of first instance equals to second instance: {id(s1)==id(s2)}")
