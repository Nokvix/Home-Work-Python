def find_even_numbers():
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    index = len(list_numbers) - 1
    while index >= 0:
        if list_numbers[index] % 2 == 0:
            print(list_numbers[index], end=" ")
        index -= 1


find_even_numbers()
