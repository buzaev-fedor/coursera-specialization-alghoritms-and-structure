# python3
"""
Описание проблемы:
Вы собираетесь отправиться в другой город, который находится в 𝑑 милях от вашего родного города.
Ваша машина может проехать не более миль с полным баком, и вы начинаете с полным баком.
По пути заправки будут на расстояниях stop1, stop2,. . . , stop𝑛 от вашего родного города.
Какое минимальное количество заправок необходимо?

Формат ввода:
В первой строке записано целое число. Во второй строке записано целое число.
В третьей строке указано целое число. Наконец, последняя строка содержит целые числа stop1, stop2,. . . , stop𝑛.

Формат вывода:
Если предположить, что расстояние между городами составляет мили,
автомобиль может проехать не более миль с полным баком,
а заправочные станции находятся на расстояниях stop1, stop2,. . . , остановка𝑛 по пути,
выведите минимальное количество заправок.
Предположим, что машина заводится с полным баком. Если добраться до места назначения невозможно, выведите −1.

Пример:
input:
950 - distance
400 - tank
4 - n stops
200 375 550 750 - array of oil stations

Output:
2
"""
import sys


def compute_min_refills(distance, tank, stops):
    n = len(stops)
    stops = [0] + stops
    stops.append(distance)
    num_refills, current_refills = 0, 0
    while current_refills <= n:
        last_refill = current_refills
        while current_refills <= n and (stops[current_refills + 1] - stops[last_refill]) <= tank:
            current_refills += 1
        if current_refills <= n:
            num_refills += 1
        if current_refills == last_refill:
            return -1
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d = 950
    # m = 400
    # stops = [200, 375, 550, 750]
    print(compute_min_refills(d, m, stops))
