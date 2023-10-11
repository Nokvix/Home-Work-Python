def calculate_cost_goods(product_title):
    quantity = 0
    price = 0
    for i_data in store[goods[product_title]]:
        quantity += i_data["quantity"]
        price += i_data["price"] * i_data["quantity"]
    return quantity, price


def word_end_quantity(quantity):
    balance_of_100 = quantity % 100
    balance_of_10 = quantity % 10
    if balance_of_10 == 1 and balance_of_100 != 11:
        return "штука"
    elif (balance_of_10 == 2 or balance_of_10 == 3 or balance_of_10 == 4) and (
            balance_of_100 != 12 or balance_of_100 != 13 or balance_of_100 != 14):
        return "штуки"
    return "штук"


def word_end_price(price):
    balance_of_100 = price % 100
    balance_of_10 = price % 10
    if balance_of_10 == 1 and balance_of_100 != 11:
        return "рубль"
    elif (balance_of_10 == 2 or balance_of_10 == 3 or balance_of_10 == 4) and (
            balance_of_100 != 12 or balance_of_100 != 13 or balance_of_100 != 14):
        return "рубля"
    return "рублей"


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for i_product_title in goods.keys():
    current_quantity, current_price = calculate_cost_goods(i_product_title)
    word_end_quantity_variable = word_end_quantity(current_quantity)
    word_end_price_variable = word_end_price(current_price)
    print("{product_title} - {quantity} {word_end_quantity}, стоимость {price} {word_end_price}.".format(
        product_title=i_product_title, quantity=current_quantity, word_end_quantity=word_end_quantity_variable,
        price=current_price, word_end_price=word_end_price_variable))
