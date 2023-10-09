string = input("Введите строку: ")
current_symbol = string[0]
counter = 1
new_string = ""
for i_symbol in range(1, len(string)):
    if string[i_symbol] == current_symbol:
        counter += 1
    else:
        new_string = "".join([new_string, current_symbol, str(counter)])
        counter = 1
        current_symbol = string[i_symbol]
new_string = "".join([new_string, current_symbol, str(counter)])
print("Закодированная строка: {string}.".format(string=new_string))
