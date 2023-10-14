from math import sqrt


def crypto(obj):
    symbols = []
    for index, i_symbol in enumerate(obj):
        if is_prime(index):
            symbols.append(i_symbol)
    return symbols


def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i_prime_number in prime_numbers:
        if number == i_prime_number:
            return True
        elif number % i_prime_number == 0:
            return False
    for i_number in range(prime_numbers[-1], round(sqrt(number)) + 1):
        if number % i_number == 0:
            return False
    prime_numbers.append(number)
    return True


prime_numbers = [2]
print(crypto([number for number in range(10000)]))
