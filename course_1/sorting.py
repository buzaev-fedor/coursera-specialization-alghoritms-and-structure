# Uses python3
import sys
import random

"""
Improving Quick Sort

Введение
Цель этой проблемы - переработать данную реализацию алгоритма рандомизированной быстрой сортировки так, 
чтобы она работала быстро даже с последовательностями, содержащими много равных элементов. 

Описание задачи

Таска:
Чтобы заставить данную реализацию алгоритма быстрой сортировки эффективно обрабатывать последовательности 
с несколькими уникальными элементами, 
ваша цель - заменить двухсторонний раздел на трехсторонний. 
То есть ваша новая процедура разделения должна разбить массив на три части: <𝑥 часть, = 𝑥 часть и> 𝑥 часть. 

Формат инпута
Первая строка входных данных содержит целое число ger. 
В следующей строке записана последовательность из 𝑛 целых чисел 𝑎0, 𝑎1,. . . , 𝑎𝑛 − 1. 

Выходной формат. 
Выведите эту последовательность в порядке неубывания. 

Example:
5
23922

22239

"""


def partition3(a, l, r):
    # left(<x) - m1 (=x) m2 - right(>x)
    pivot = a[l]
    i = l
    m1 = l
    m2 = r
    while i <= m2:
        if a[i] < pivot:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j

#
# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     m = partition2(a, l, r)
#     randomized_quick_sort(a, l, m - 1);
#     randomized_quick_sort(a, m + 1, r);


def randomized_quick_sort(a, l, r):
    if l >= r:
        return

    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    middle1, middle2 = partition3(a, l, r)
    randomized_quick_sort(a, l, middle1 - 1)
    randomized_quick_sort(a, middle2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [2, 3, 9, 2, 2]
    # n = len(a)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
