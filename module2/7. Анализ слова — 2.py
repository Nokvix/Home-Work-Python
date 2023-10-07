def main_func():
    word = input("Введите слово: ")
    print(palindrome_test(word))


def palindrome_test(word):
    if word == word[::-1]:
        return "Слово является палиндромом"
    else:
        return "Слово не является палиндромом"


main_func()
