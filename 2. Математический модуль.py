from typing import Union
from math import pi


class MyMath:
    @staticmethod
    def circle_len(radius: Union[int, float]) -> float:
        return 2 * pi * radius

    @staticmethod
    def circle_sq(radius: Union[int, float]) -> float:
        return pi * radius ** 2

    @staticmethod
    def cube_volume(side: Union[int, float]) -> Union[int, float]:
        return side ** 3

    @staticmethod
    def sphere_surface_sq(radius: Union[int, float]) -> float:
        return 4 * pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(side=6)
res_4 = MyMath.sphere_surface_sq(radius=6)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
