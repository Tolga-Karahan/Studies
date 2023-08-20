class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(f"ID of first instance: {id(s1)}, ID of second instance: {id(s2)}")
print(f"ID of first instance equals to second instance: {id(s1)==id(s2)}")
