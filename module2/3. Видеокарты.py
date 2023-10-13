def main_func():
    video_cards = []
    n = int(input("Количество видеокарт: "))
    for index in range(n):
        video_cards.append(int(input(f"Видеокарта {index + 1}: ")))
    print(f"Старый список видеокарт: {video_cards}")
    print(f"Новый список видеокарт: {delete_oldest_generation(video_cards)}")


def find_oldest_generation(video_cards):
    return max(video_cards)


def delete_oldest_generation(video_cards):
    counter = 0
    oldest_generation = find_oldest_generation(video_cards)
    while True:
        if video_cards[counter] == oldest_generation:
            video_cards.remove(oldest_generation)
        else:
            counter += 1
        if counter >= len(video_cards):
            break
    return video_cards


main_func()
