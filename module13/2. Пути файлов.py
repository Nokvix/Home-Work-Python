import os


def gen_files_path(path: str = 'C:\\') -> list[str]:
    result = []

    for path, directory, files in os.walk(path):
        result.extend([os.path.join(path, file) for file in files])

    return result


user_path = input('Каталог: ')
print(gen_files_path(user_path))
# print(gen_files_path())
