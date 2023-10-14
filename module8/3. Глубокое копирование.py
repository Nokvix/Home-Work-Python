def deep_copy(obj):
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, dict):
        return {key: deep_copy(value) for key, value in obj.items()}


def find_key_replace_data(struct, key, string):
    if key in struct:
        struct[key] = string
        return
    result = None
    for i_key, i_value in struct.items():
        if isinstance(i_value, dict):
            find_key_replace_data(i_value, key, string)


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

list_sites = []
number_sites = int(input("Сколько сайтов: "))
for _ in range(number_sites):
    product_name = input("Введите название продукта для нового сайта: ")
    site_copy = deep_copy(site)
    list_sites.append((site_copy, product_name))
    find_key_replace_data(site_copy, "title", f"Куплю/продам {product_name} недорого")
    find_key_replace_data(site_copy, "h2", f"Куплю/продам {product_name} недорого")
    for i_site, i_product_name in list_sites:
        print(f"Сайт для {i_product_name}:\n"
              f"{i_site}\n")
