import functools
import datetime
from typing import Union, Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_message = f"Data: {datetime.datetime.now()}\n"
            error_message += f"Filename: {func.__name__}\n"
            error_message += f"Error: {str(e)}\n"
            file.write(error_message + "\n")
            print(error_message)

    return wrapper


@logging
def function1(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


@logging
def function2(a: Union[int, float], b: Union[int, float]) -> float:
    return a / b


@logging
def function3(a: Union[int, float], b: Union[int, float]) -> float:
    return a + b


@logging
def function4(a: Union[int, float], b: Union[int, float]) -> float:
    return a / b


with open("function_errors.log", "w", encoding="utf-8") as file:
    result1 = function1(2, 3)
    result2 = function2(5, 0)
    result3 = function3(2, "a")
    result4 = function4(5, "a")
