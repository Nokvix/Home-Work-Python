def send_message(chat_history, name):
    message = input("Введите сообщение: ")
    chat_history.write("{0}:\t{1}\n".format(
        name,
        message
    ))


def view_chat(chat_history):
    chat_history.seek(0)
    print(chat_history.read())


def select_action(chat_history, name):
    action = -1
    while True:
        action = int(input("\nВыберите действие, которое хотите сделать:\n"
                           "1. Посмотреть текущий текст чата\n"
                           "2. Отправить сообщение\n"
                           "3. Перелогиниться\n"
                           "4. Полностью выйти из чата\n"
                           "Выбор: "))
        print()
        match action:
            case 1:
                view_chat(chat_history)
            case 2:
                send_message(chat_history, name)
            case 3:
                break
            case 4:
                break
            case _:
                print("Неккоректная команда")
    return action


user_name = ""
with open("chat_history", "w+", encoding="utf-8") as chat_history:
    while True:
        user_name = input("Введите своё имя: ")
        cur_action = select_action(chat_history, user_name)
        if cur_action == 3:
            continue
        elif cur_action == 4:
            break
