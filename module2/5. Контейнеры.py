def input_container_weight(input_proposal):
    container_weight = int(input(input_proposal))
    if container_weight > 200:
        while container_weight > 200:
            print("Вес контейнера не может превышать 200!")
            container_weight = int(input(input_proposal))
        return container_weight
    else:
        return container_weight


n = int(input("Количество контейнеров: "))
containers = []
for _ in range(n):
    # containers.append(int(input("Введите вес контейнера: ")))
    containers.append(input_container_weight("Введите вес контейнера: "))
new_container = input_container_weight("Введите вес нового контейнера: ")
for index in range(n):
    if new_container > containers[index]:
        print(f"Номер, который получит новый контейнер: {index + 1}")
        break
    elif index == len(containers) - 1:
        print(f"Номер, который получит новый контейнер: {len(containers) + 1}")
