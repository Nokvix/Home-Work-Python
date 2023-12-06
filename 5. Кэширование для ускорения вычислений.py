import functools
from typing import Any, Callable, Dict


def memoize(func: Callable) -> Callable:
    cache = {}

    @functools.wraps(func)
    def wrapper(*args) -> Dict[int, int]:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(number: int) -> int:
    if number == 1 or number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(500))
