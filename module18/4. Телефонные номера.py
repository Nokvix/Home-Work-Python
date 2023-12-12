import re


def check_number(number: str):
    if len(re.findall(r"[89][1234567890]{9}", number)) == 1:
        print(f"Номер {number}: всё в порядке")
    else:
        print(f"Номер {number}: не подходит")


numbers_list = ['9999999999', '999999-999', '99999x9999']

for number in numbers_list:
    check_number(number)
