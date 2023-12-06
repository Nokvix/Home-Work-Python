import functools
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.calls += 1
        print(f"Функция '{func.__name__}' была вызвана {wrapper.calls} раз(-а)")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@counter
def function1() -> None:
    print("Функция 1")


@counter
def function2() -> None:
    print("Функция 2")


function1()
function1()
function2()
function1()
function2()
