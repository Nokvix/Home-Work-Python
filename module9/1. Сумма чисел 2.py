numbers_file = open("numbers.txt", "r", encoding="utf-8")
total_amount = 0
for i_number in numbers_file:
    total_amount += int(i_number.strip())
numbers_file.close()
answer_file = open("answer.txt", "w", encoding="utf-8")
answer_file.write(str(total_amount))
