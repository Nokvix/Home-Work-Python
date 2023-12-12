from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

result_floats: List[float] = list(map(lambda num: round(num ** 3, 3), floats))
result_names: List[str] = list(filter((lambda name: len(name) >= 5), names))
result_numbers: int = reduce((lambda total, num: num * total), numbers)

print(result_floats)
print(result_names)
print(result_numbers)
