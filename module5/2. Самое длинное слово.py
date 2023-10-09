string_list = input("Введите строку: ").split()
maximum_word = ''
number_symbols = 0
for i_word in string_list:
    if len(i_word) > number_symbols:
        number_symbols, maximum_word = len(i_word), i_word
print('Самое длинное слово: «{word}».'.format(word=maximum_word))
print('Длина этого слова: {number_symbols} символов.'.format(number_symbols=number_symbols))
