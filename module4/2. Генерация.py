list_length = int(input("Введите длину списка: "))
list_numbers = [(1 if number % 2 == 0 else number % 5) for number in range(list_length)]
print(list_numbers)
