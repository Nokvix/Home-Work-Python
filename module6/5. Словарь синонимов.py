word_count = int(input("Введите количество пар слов: "))
dictionary_synonyms = dict()
for i_word in range(1, word_count + 1):
    words = input("{0}-я пара (вводитие пару слов через - (тире) без пробелов): ".format(i_word)).split("-")
    dictionary_synonyms[words[0].title()] = words[1].title()
    dictionary_synonyms[words[1].title()] = words[0].title()
print(dictionary_synonyms)
while True:
    word = input("Введите слово: ").title()
    if word in dictionary_synonyms:
        print("Синоним: {0}".format(dictionary_synonyms[word]))
        break
    else:
        print("Такого слова в словаре нет.")
