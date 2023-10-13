list_sportsmen = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
new_list_sportsmen = []
for index in range(0, len(list_sportsmen), 2):
    new_list_sportsmen.append(list_sportsmen[index])
print(new_list_sportsmen)
