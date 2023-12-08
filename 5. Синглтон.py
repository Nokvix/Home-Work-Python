import functools
from typing import Callable


def singleton(cls) -> Callable:
    instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Callable:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Example:
    pass


@singleton
class Class:
    pass


my_obj = Example()
my_another_obj = Example()
my_class = Class()

print(id(my_obj))
print(id(my_another_obj))
print(id(my_class))

print(my_obj is my_another_obj)
print(my_class is my_obj)
print(my_class is my_another_obj)
