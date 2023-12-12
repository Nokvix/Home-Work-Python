from collections import Counter


def can_be_poly(string: str) -> bool:
    return len(list(filter(lambda counter: counter % 2 == 1, Counter(string).values()))) < 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
