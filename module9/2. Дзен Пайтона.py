zen_file = open("zen.txt", "r", encoding="utf-8")
list_strings = []
for i_line in zen_file:
    list_strings.append(i_line.strip("\n"))
for i_line in reversed(list_strings):
    print(i_line)
zen_file.close()
