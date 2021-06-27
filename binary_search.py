# Uses python3
import sys

"""
В этой задаче вы реализуете алгоритм двоичного поиска, 
который позволяет очень эффективно искать 
(даже в огромных) списках при условии, что список отсортирован. 

Описание задачи
Таск:
Целью этой проблемы кода является реализация алгоритма двоичного поиска. 

Формат инпута:
Первая строка входных данных содержит целое число 𝑛 и последовательность 𝑎0 <𝑎1 <. . . <𝑎𝑛 − 1 
из 𝑛 попарно различных натуральных чисел в порядке возрастания. 
В следующей строке записано целое число 𝑘 и 𝑘 натуральные числа 𝑏0, 𝑏1,. . . , 𝑏𝑘 − 1. 

Формат отпута
Для всех от 0 до − 1, выходной индекс 0 − 1 такой, что = if или −1, если существует
такого индекса нет. 
"""


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        middle = (left + right) // 2
        # print(f"{middle} : {x}")
        if x == a[middle]:
            return middle
        if a[middle] > x:
            right = middle - 1
        elif a[middle] < x:
            left = middle + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')

# n = 5
# a = [1, 5, 8, 12, 13]
# data = [5, 1, 5, 8, 12, 13]
# # n = data[0]
# # m = data[n + 1]
# # a = data[1: n + 1]
# for x in data[n + 2:]:
#     print(data)
#     # replace with the call to binary_search when implemented
#     print(linear_search(a, x), end=' ')
