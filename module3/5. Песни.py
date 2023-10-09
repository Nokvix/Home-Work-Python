violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def main_func():
    number_songs = int(input("Сколько песен выбрать? "))
    print(song_selection(number_songs))


def song_selection(number_songs):
    total_time = 0
    for index in range(number_songs):
        song_title = input(f"Название {index + 1}-й песни: ")
        for song_data in violator_songs:
            if song_title == song_data[0]:
                total_time += song_data[1]
    return round(total_time, 2)


main_func()
