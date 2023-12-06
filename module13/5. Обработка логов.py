# Генерация файла для тестирования
#
# from random import randint
#
#
# with open('logs.log', 'w', encoding='utf-8') as file:
#     for _ in range(100000):
#         num = randint(1, 10)
#         if num == 1:
#             file.write("1234124ERROR The payment didn't go through\n")
#         elif num == 2:
#             file.write("5242234ERROR Refusal to pay\n")
#         elif num == 3:
#             file.write("00000000ERROR Out of stock\n")
#         else:
#             file.write("Successful!\n")


def error_log_generator(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if "ERROR" in line:
                yield line.strip()


user_path = "D:\\Python Skilbox\\Часть 2\\Home-Work-Python\\module13\\logs.log"
error_log = error_log_generator(user_path)
with open("error_log.log", "w", encoding="utf=8") as error_file:
    for log in error_log:
        error_file.write(log + "\n")
