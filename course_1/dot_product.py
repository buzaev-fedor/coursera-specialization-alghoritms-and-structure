# Uses python3
"""
Задача:
У вас есть 𝑛 объявлений для размещения на популярной странице в Интернете.
По каждому объявлению вы знаете, сколько рекламодатель готов платить за один клик по этому объявлению.
Вы создали 𝑛 рекламных мест на своей странице и оценили ожидаемое количество кликов в день для каждого рекламного места.
Теперь ваша цель - распределить рекламу по рекламным местам, чтобы максимизировать общий доход.

Описание проблемы:
Даны две последовательности 𝑎1, 𝑎2, ..., 𝑎𝑛 (𝑎𝑖 - прибыль на клик 𝑖-го объявления) и 𝑏1, 𝑏2, ..., 𝑏𝑛
(𝑏𝑖 - среднее количество кликов в день 𝑖- -й слот),
нам нужно разделить их на 𝑛 пар (𝑎𝑖, 𝑏𝑗) так, чтобы сумма их произведений была максимальной.

input format:
В первой строке записано целое число 𝑛,
во второй - последовательность целых чисел 𝑎1, 𝑎2, ..., 𝑎𝑛,
в третьей - последовательность целых чисел 𝑏1, 𝑏2, ..., 𝑏𝑛

Output format
Выведите максимальное значение ∑︀ 𝑎𝑖𝑐𝑖, где 𝑐1, 𝑐2,. . . , 𝑐𝑛 - перестановка
𝑏1, 𝑏2, ..., 𝑏𝑛.

Примеры:
1
23
39
: 897 (23*39)

3
1 3 -5
-2 4 1
: 23 (3*4 + 1*1 + (-5)*(-2))
"""
import sys


def max_dot_product(n, a, b):
    res = 0
    for i in range(n):
        if max(a) > 0 and max(b) > 0:
            res += max(a) * max(b)
            a.remove(max(a))
            b.remove(max(b))
        elif max(a) == 0 and max(b) == 0 or max(a) < 0 and max(b) < 0:
            res += min(a) * min(b)
            a.remove(max(a))
            b.remove(max(b))

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    # a = [1, 3, -5]
    # b = [-2, 4, 1]
    # n = 3
    print(max_dot_product(n, a, b))
