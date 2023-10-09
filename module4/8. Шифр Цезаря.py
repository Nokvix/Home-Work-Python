alfabet = [chr(i_letter) for i_letter in range(ord("а"), ord("я") + 1)]


def main_func():
    index_e = find_index("е")
    alfabet.insert(index_e + 1, "ё")
    message = input("Введите сообщение: ").lower()
    shift = int(input("Введите сдвиг: "))
    encrypted_message = caesar_code(message, shift)
    print(f"Зашифрованное сообщение: {encrypted_message}.")


def find_index(letter):
    for i_letter in range(len(alfabet)):
        if alfabet[i_letter] == letter:
            return i_letter


def caesar_code(message, shift):
    encrypted_message_list = [alfabet[(find_index(i_letter) + shift) % len(alfabet)] if i_letter != " " else " " for
                              i_letter in message]
    encrypted_message_string = "".join(encrypted_message_list)
    return encrypted_message_string


main_func()
