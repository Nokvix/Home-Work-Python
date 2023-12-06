from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func

    return wrapper()


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


test()
