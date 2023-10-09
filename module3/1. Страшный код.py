a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
number_digits_5 = a.count(5)
print(f"Количество цифр 5 при первом объединении: {number_digits_5}")
while number_digits_5 > 0:
    a.remove(5)
    number_digits_5 -= 1
a.extend(c)
print(f"Количество цифр 3 при втором объединении: {a.count(3)}")
print(f"Итоговый список: {a}")
