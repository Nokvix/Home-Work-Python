import time
from typing import Callable, Any
import functools


def sleep_time(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        time.sleep(3)
        func()

    return wrapper


def get_number_1_5() -> None:
    for i in range(1, 6):
        print(i)


@sleep_time
def get_number_6_10() -> None:
    for i in range(6, 11):
        print(i)


get_number_1_5()
get_number_6_10()
