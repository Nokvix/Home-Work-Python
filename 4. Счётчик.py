import functools
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@counter
def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
print(fibonacci.calls)
