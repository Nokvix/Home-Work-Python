def main_func():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
             'Отступники', 'Деревня']
    favourite_films = make_list_favourite_films(films)
    print("Ваш список любимых фильмов: ", end="")
    for index in range(len(favourite_films)):
        if index == len(favourite_films) - 1:
            print(favourite_films[index], end="")
        else:
            print(favourite_films[index], end=", ")


def make_list_favourite_films(films):
    favourite_films = []
    n = int(input("Сколько фильмов хотите добавить? "))
    for _ in range(n):
        film = input("Введите название фильма: ")
        if film in films:
            favourite_films.append(film)
        else:
            print(f"Ошибка: фильма {film} у нас нет :(")
    return favourite_films


main_func()
