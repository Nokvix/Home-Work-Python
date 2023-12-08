from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorated_decorator_func: Callable) -> Callable:
    def decorator(*args, **kwargs):
        @functools.wraps(decorated_decorator_func)
        def wrapper(func):
            print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
            return decorated_decorator_func(func, *args, **kwargs)

        return wrapper

    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        func(*func_args, **func_kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)
