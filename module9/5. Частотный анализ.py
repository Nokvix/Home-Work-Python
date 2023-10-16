def analyze_text(cur_text):
    frequency_dictionary = dict()
    total_letters = 0
    for symbol in cur_text:
        if symbol.isalpha():
            total_letters += 1
            if symbol in frequency_dictionary:
                frequency_dictionary[symbol] += 1
            else:
                frequency_dictionary[symbol] = 1
    text_file.close()
    for letter, frequency in frequency_dictionary.items():
        frequency_dictionary[letter] = round(frequency / total_letters, 3)
    sorted_frequency_dict = dict(sorted(frequency_dictionary.items(), key=lambda item: (-item[1], item[0])))
    return sorted_frequency_dict


def write_analysis(sorted_frequency_dict):
    for letter, frequency in sorted_frequency_dict.items():
        analysis_file.write(f"{letter} {frequency}\n")


text_file = open("text.txt", "r", encoding="utf-8")
text = text_file.read().lower()
frequency_dict = analyze_text(text)
text_file.close()

analysis_file = open("analysis.txt", "w", encoding="utf-8")
write_analysis(frequency_dict)
analysis_file.close()
