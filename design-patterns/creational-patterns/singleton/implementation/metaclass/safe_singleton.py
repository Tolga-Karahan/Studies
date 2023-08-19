from threading import Lock


class SafeSingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


class Singleton(metaclass=SafeSingletonMeta):
    pass


s1 = Singleton()
s2 = Singleton()

print(f"ID of first instance: {id(s1)}, ID of second instance: {id(s2)}")
print(f"ID of first instance equals to second instance: {id(s1)==id(s2)}")
