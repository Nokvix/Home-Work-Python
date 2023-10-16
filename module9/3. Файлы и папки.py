import os


def calculate_data(path):
    data = os.listdir(path)
    number_files = 0
    number_dir = 0
    total_size = 0
    for i_elem in data:
        new_path = os.path.join(os.sep, path, i_elem)
        if os.path.isdir(new_path):
            number_dir += 1
            number_dir_cur, number_files_cur, total_size_cur = calculate_data(new_path)
            number_files += number_files_cur
            number_dir += number_dir_cur
            total_size += total_size_cur
        elif os.path.isfile(new_path):
            number_files += 1
            total_size += os.path.getsize(new_path)
    return number_dir, number_files, total_size


user_path = input("Введите путь до каталога:\n")
directories, files, size = calculate_data(user_path)
size_kb = size / 1024
print("Размер каталога (в Кбайтах):", size_kb)
print("Количество подкаталогов:", directories)
print("Количество файлов:", files)
