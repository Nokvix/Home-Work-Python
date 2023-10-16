def filter_data(data_file):
    print("Начата обработка данных...")
    passing_data = int(data_file.readline())
    data = []
    for i_data in data_file:
        surname, name, scores = i_data.split()
        scores = int(scores)
        if scores > passing_data:
            new_data = (scores, "".join([name[:1], ". ", surname]))
            data.append(new_data)
    data_file.close()
    data = sorted(data, reverse=True)
    print("Обработка данных закончена")
    return data


def record_data(data):
    print("Начата запись результатов в файл second_tour.txt")
    counter = 1
    for i_scores, i_fullname in data:
        second_tour.write(f"{counter}) {i_fullname} {i_scores}\n")
        counter += 1
    second_tour.close()
    print("Результаты записаны в файл second_tour.txt")


tournament_data = open("first_tour.txt", "r", encoding="utf-8")
filtered_data = filter_data(tournament_data)
second_tour = open("second_tour.txt", "w", encoding="utf-8")
record_data(filtered_data)
