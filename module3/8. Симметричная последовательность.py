numbers = []


def main_func():
    n = int(input("Количество чисел: "))
    for _ in range(n):
        numbers.append(int(input("Число: ")))
    print(numbers)
    if is_symmetry():
        print("Последовательность симметрична. Ничего добавлять не нужно")
    else:
        result = complete_to_symmetry(n)
        print(f"Нужно приписать чисел: {result[0]}")
        print(f"Сами числа: {result[1]}")


def is_symmetry():
    for index in range(len(numbers) // 2):
        if numbers[index] != numbers[-(index + 1)]:
            return False
    return True


def complete_to_symmetry(n):
    missing_digits = []
    counter = 0
    index = 0
    while True:
        number_numbers = len(numbers)
        first_part = numbers[0:number_numbers // 2]
        numbers.insert(n, first_part[index])
        missing_digits.append(first_part[index])
        counter += 1
        index += 1
        if is_symmetry():
            return [counter, missing_digits[::-1]]


main_func()
