violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
total_time = 0
number_songs = int(input("Сколько песен выбрать? "))
for i_song in range(1, number_songs + 1):
    song_title = input("Название {0}-й песни: ".format(i_song))
    if song_title in violator_songs:
        total_time += violator_songs[song_title]
    else:
        print("Такой песни в списке нет")
total_time = round(total_time, 2)
print("Общее время звучания песен: {0} минуты".format(total_time))
