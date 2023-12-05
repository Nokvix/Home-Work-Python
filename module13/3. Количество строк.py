import os
import collections


def count_number_lines(path: str) -> int:
    counter = 0
    with open(path, 'r') as file:
        for line in file:
            if '#' not in line and not line.isspace():
                counter += 1
    return counter


def get_line_count_python_file(paths: list[str]) -> collections:
    for path in paths:
        basename = os.path.basename(path)

        if os.path.isfile(path) and basename.endswith('.py'):
            counter = count_number_lines(path)
            print(f'В файле: {basename}', end=' ')
            yield counter


def gen_files_path(path: str) -> list[str]:
    result = []

    for path, directory, files in os.walk(path):
        result.extend([os.path.join(path, file) for file in files])
        break

    return result


user_path = input('Введите путь до директории: ')
line_count_generator = get_line_count_python_file(gen_files_path(user_path))
for line_count in line_count_generator:
    print(line_count, 'строк')
