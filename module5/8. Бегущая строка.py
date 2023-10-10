def main_func():
    first_row = input("Первая строка: ")
    second_row = input("Вторая строка: ")
    string_can_be_obtained_by_shifting(first_row, second_row)


def string_can_be_obtained_by_shifting(line_sample, checked_string):
    initial_symbol_indexes = [i_symbol for i_symbol in range(len(checked_string)) if
                              checked_string[i_symbol] == line_sample[0]]
    for symbol_index in initial_symbol_indexes:
        new_string = checked_string[symbol_index:]
        if symbol_index != 0:
            new_string = "".join([new_string, checked_string[:symbol_index]])
        if new_string == line_sample:
            print(f"Первая строка получается из второй со сдвигом {symbol_index}.")
            break
    else:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")


if __name__ == '__main__':
    main_func()
