def create_dictionary(string):
    dictionary = dict()
    for symbol in string:
        if symbol in dictionary:
            dictionary[symbol] += 1
        else:
            dictionary[symbol] = 1
    return dictionary


def see_if_it_can_be_made_into_palindrome(dictionary):
    number_characters_that_occur_odd_number_times = 0
    is_palindrome_possible = True
    for key in dictionary.keys():
        if dictionary[key] % 2 == 1:
            number_characters_that_occur_odd_number_times += 1
            if number_characters_that_occur_odd_number_times == 2:
                is_palindrome_possible = False
                break
    return is_palindrome_possible


def main():
    string = input("Введите строку: ")
    symbol_frequency_dictionary = create_dictionary(string)
    print("Можно сделать палиндромом" if see_if_it_can_be_made_into_palindrome(
        symbol_frequency_dictionary) else "Нельзя сделать палиндромом")


if __name__ == '__main__':
    main()
