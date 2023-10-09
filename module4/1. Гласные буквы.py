vowels = ["у", "е", "ы", "а", "о", "э", "я", "и", "ю", "ё"]


def is_vowel(letter):
    return letter.lower() in vowels


text = input("Введите текст: ")
vowel_letters = [letter for letter in text if is_vowel(letter)]
print(f"Список гласных букв: {vowel_letters}")
print(f"Длина списка: {len(vowel_letters)}")
