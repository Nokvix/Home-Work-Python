import datetime
from typing import Callable
import functools
import time


def get_datetime(format_data: str) -> str:
    months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
              11: "Nov", 12: "Dec"}

    cur_datetime = datetime.datetime.now()
    return (format_data
            .replace("b", months[cur_datetime.month])
            .replace("d", str(cur_datetime.day))
            .replace("Y", str(cur_datetime.year))
            .replace("H", str(cur_datetime.hour))
            .replace("M", str(cur_datetime.minute))
            .replace("S", str(cur_datetime.second)))


def log_methods(format_data: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_data = get_datetime(format_data)
            print(f"Запускается '{func.__name__}'. Дата и время запуска: {log_data}. ")

            start_time = time.time()
            result = func(*args, **kwargs)
            total_time = round(time.time() - start_time, 3)

            print(f"Завершение '{func.__name__}', время работы = {total_time} s. ")
            return result

        return wrapper

    @functools.wraps(decorator)
    def all_methods(cls):
        for method in dir(cls):
            if not method.startswith("__"):
                cur_method = getattr(cls, method)
                decorated_method = decorator(cur_method)
                setattr(cls, method, decorated_method)
        return cls

    return all_methods


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
