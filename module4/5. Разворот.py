string = input("Введите строку: ")
first_h_index = string.index("h")
last_h_index = string.rindex("h")
print(f"Развёрнутая последовательность между первым и последним h: {string[last_h_index - 1:first_h_index:-1]}")
