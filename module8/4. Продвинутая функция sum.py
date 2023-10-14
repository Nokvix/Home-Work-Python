def my_sum(*args):
    total_amount = 0
    for arg in args:
        if isinstance(arg, list):
            for element in arg:
                total_amount += my_sum(element)
        else:
            total_amount += arg
    return total_amount


print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum(1, 2, 3, 4, 5))
