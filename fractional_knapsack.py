# Uses python3
import sys
from collections import namedtuple
"""
Задача: 
Реализовать алгоритм рюкзака
Формат входа:
Первая строка входных данных содержит количество предметов и вместимость рюкзака. 
Следующие 𝑛 строки определяют стоимость и вес предметов.
В 𝑖-й строке записаны целые числа 𝑣𝑖 и 𝑤𝑖 - значение и вес 𝑖-го элемента соответственно. 
Формат вывода:
Выведите максимальное значение долей предметов, помещающихся в рюкзак.
Абсолютное значение разницы между ответом вашей программы 
и оптимальным значением должно быть не более 10−3. 
Чтобы убедиться в этом, выведите свой ответ, 
состоящий как минимум из четырех цифр после десятичной точки 
(в противном случае ваш ответ, будучи вычисленным правильно, может оказаться неправильным из-за проблем с округлением). 
"""


Item = namedtuple("Item", "value weight")


def get_optimal_value(capacity, weights, values):
    value = 0.
    weight_value_pairs = sorted(
        [Item(v, w) for v, w in zip(values, weights)],
        key=lambda i: i.value / i.weight,
        reverse=True
    )
    space_backpack = int(capacity)
    print(weight_value_pairs)
    for item in weight_value_pairs:
        if space_backpack - item[1] >= 0:
            value += item[0]
            space_backpack -= item[1]
            print(space_backpack)
        else:
            value += (item.value / item.weight) * space_backpack
            space_backpack = 0
    return round(value, 4)


if __name__ == "__main__":
    # data = [3, 50, 60, 20, 100, 50, 120, 30]
    # data = [1, 10, 500, 30]
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
