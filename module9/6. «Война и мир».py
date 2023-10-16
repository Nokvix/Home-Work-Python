def analysis_text(text):
    print("Идёт анализ текста...")
    frequency_dict = dict()
    for i_symbol in text:
        if i_symbol.isalpha():
            if i_symbol in frequency_dict:
                frequency_dict[i_symbol] += 1
            else:
                frequency_dict[i_symbol] = 1
    sorted_frequency_list = []
    for letter, frequency in frequency_dict.items():
        sorted_frequency_list.append((frequency, letter))
    sorted_frequency_list = sorted(sorted_frequency_list, reverse=True)
    print("Анализ закончен")
    return sorted_frequency_list


def write_analysis(frequency_list):
    print("Идёт вывод результатов анализа в файл War_and_Peace_analysis.txt")
    for frequency, letter in frequency_list:
        analysis_file.write(f"{letter} {frequency}\n")
    print("Результаты выведены")


text_file = open("War_and_Peace.txt", "r", encoding="utf-8")
text = text_file.read()
frequency_list = analysis_text(text)
text_file.close()

analysis_file = open("War_and_Peace_analysis.txt", "w", encoding="utf-8")
write_analysis(frequency_list)
analysis_file.close()
