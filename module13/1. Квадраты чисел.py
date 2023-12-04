class ClassIterator:
    def __init__(self, limit: int):
        self.cur_number = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.cur_number == self.limit:
            raise StopIteration
        self.cur_number += 1
        return self.cur_number ** 2


number = int(input('Введите число: '))
print()
print('1-е решение')
class_iterator = ClassIterator(limit=number)
for square in class_iterator:
    print(square)
print()


def generator_function(number: int) -> int:
    current_number = 1
    for _ in range(number):
        yield current_number ** 2
        current_number += 1


print('2-е решение')
generator_function_variable = generator_function(number)
for square in generator_function_variable:
    print(square)
print()

print('3-е решение')
generating_expression = (num ** 2 for num in range(1, number + 1))
for square in generating_expression:
    print(square)
