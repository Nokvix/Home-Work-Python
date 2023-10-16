site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth):
    if depth == 0:
        return None
    if key in struct:
        return struct[key]
    result = None
    for i_key, i_value in struct.items():
        if isinstance(i_value, dict):
            if depth is not None:
                result = find_key(i_value, key, depth - 1)
            else:
                result = find_key(i_value, key, depth)
            if result:
                return result
    return result


user_key = input("Введите искомый ключ: ").lower()
depth_entry = input("Хотите ввести максимальную глубину? Y/N: ").lower()
max_depth = None
if depth_entry == "y":
    max_depth = int(input("Введите максимальную глубину: "))
    if max_depth < 0:
        print("Ошибка: некорректное значение глубины")
answer = find_key(site, user_key, max_depth)
print("Значение ключа:", answer)
