N = int(input("Введите число: "))
list_number = []
for number in range(1, N + 1, 2):
    list_number.append(number)
print(f"Список из нечётных чисел от одного до {N}: {list_number}")
