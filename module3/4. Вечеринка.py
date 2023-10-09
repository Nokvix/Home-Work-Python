guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def main_func():
    while True:
        print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
        action = input("Гость пришёл или ушёл? ")
        if action == "Пора спать":
            print("Вечеринка закончилась, все легли спать.")
            break
        action_processing(action)


def action_processing(action):
    guest_name = input("Имя гостя: ")
    if action == "пришёл":
        if len(guests) < 6:
            guests.append(guest_name)
            print(f"Привет, {guest_name}!\n")
        else:
            print(f"Прости, {guest_name}, но мест нет.\n")
    elif action == "ушёл":
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!\n")
    else:
        print(f"Команды \"{action}\" нет попробуйте ещё раз\n")


main_func()
