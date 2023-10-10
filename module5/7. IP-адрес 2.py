ip_address = input("Введите IP: ").split(".")
for element in ip_address:
    if len(ip_address) != 4:
        print("IP-адрес — это четыре числа, разделённые точками.")
        break
    elif not element.isdigit():
        print(f"{element} - это не целое число.")
        break
    elif int(element) > 255 or int(element) < 0:
        conclusion = f"{element} превышает 255." if int(element) > 255 else f"{element} меньше 0"
        print(conclusion)
        break
else:
    print("IP-адрес корректен.")
