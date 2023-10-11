def generate_dictionary():
    text_list = sorted(i_symbol for i_symbol in text)
    for i_symbol in text_list:
        if i_symbol in frequency_dictionary:
            frequency_dictionary[i_symbol] += 1
        else:
            frequency_dictionary[i_symbol] = 1


def invert_dictionary():
    value = {i_value for i_value in frequency_dictionary.values()}
    for number in value:
        inverted_dictionary[number] = []
    for i_key in frequency_dictionary.keys():
        inverted_dictionary[frequency_dictionary[i_key]].append(i_key)


text = input("Введите текст: ")
frequency_dictionary = dict()
generate_dictionary()
print("Оригинальный словарь частот:")
for i_key in frequency_dictionary.keys():
    print("{0}:{1}".format(i_key, frequency_dictionary[i_key]))
print("Инвертированный словарь частот:")
inverted_dictionary = dict()
invert_dictionary()
for i_key in inverted_dictionary.keys():
    print("{0}:{1}".format(i_key, inverted_dictionary[i_key]))
