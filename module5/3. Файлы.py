file_name = input("Название файла: ")
invalid_characters = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
if any(file_name.startswith(characters) for characters in invalid_characters):
    print("Ошибка: название начинается недопустимым символом.")
elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")
