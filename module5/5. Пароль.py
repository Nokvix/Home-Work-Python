while True:
    digits_counter = 0
    capital_letter_counter = 0
    password = input("Придумайте пароль (латиница): ")
    for i_symbol in password:
        if i_symbol.isupper():
            capital_letter_counter += 1
        elif i_symbol.isdigit():
            digits_counter += 1
    if len(password) < 8 or digits_counter < 3 or capital_letter_counter < 1:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print("Это надёжный пароль.")
        break
