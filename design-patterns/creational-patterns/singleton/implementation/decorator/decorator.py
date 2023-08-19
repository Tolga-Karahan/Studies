from functools import wraps


def singleton(class_obj):
    _instance = None
    orig_new = class_obj.__new__

    @wraps(class_obj.__new__)
    def __new__(cls, *args, **kwargs):
        nonlocal _instance
        if not _instance:
            _instance = orig_new(cls, *args, **kwargs)
        return _instance

    class_obj.__new__ = __new__
    return class_obj


@singleton
class Singleton:
    pass


s1 = Singleton()
s2 = Singleton()

print(f"ID of first instance: {id(s1)}, ID of second instance: {id(s2)}")
print(f"ID of first instance equals to second instance: {id(s1)==id(s2)}")
