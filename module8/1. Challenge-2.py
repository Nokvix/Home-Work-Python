def print_num(cur_num, num):
    if cur_num == num:
        return cur_num
    else:
        print(cur_num)
        return print_num(cur_num + 1, num)


number = int(input("Введите num: "))
print(print_num(1, number))
