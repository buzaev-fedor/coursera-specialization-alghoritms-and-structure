# python3
from collections import deque

"""
Введение в проблему
Дана последовательность 𝑎1 ,. ... ..., 𝑎𝑛 целых чисел и целого 𝑚 ≤ 𝑛,
найдите максимум среди {𝑎𝑖 ,. ... ..., 𝑎𝑖 + 𝑚 - 1} для каждого 1 ≤ 𝑖 ≤ 𝑛 - 𝑚 + 1.
Наивный алгоритм 𝑂 (𝑛𝑚) для решения этой задачи сканирует каждое окно отдельно. Ваша цель - разработать алгоритм 𝑂 (𝑛).


Описание проблемы
Формат ввода.
В первой строке записано целое число 𝑛, во второй строке - 𝑛 целых чисел 𝑎1,. . . , 𝑎𝑛 через пробел,
в третьей строке записано целое число.

Пример 1
8
2 7 3 1 5 2 6 2
4


Что делать
Мы даем подсказки для трех различных решений.
1. Реализуйте очередь, используя два стека.
Используйте структуру данных очереди для перемещения окна по последовательности:
чтобы сдвинуть окно на одну позицию вправо, вытолкните крайний левый элемент очереди и
вытолкните новый элемент из нового окна.
Очередь может быть реализована с использованием двух стеков,
так что каждая операция очереди занимает в среднем постоянное время.
Затем используйте свою реализацию стека с max.
2. Предварительная обработка суффиксов и префиксов блоков.
Разделите входную последовательность на блоки длиной 𝑚 и предварительно вычислите максимум для каждого суффикса
и каждого префикса каждого блока. Впоследствии максимум в каждом скользящем окне можно найти,
рассматривая суффикс и префикс двух последовательных блоков.
3. Храните соответствующие элементы в исключении из очереди.
Используйте двустороннюю очередь (dequeue) для хранения элементов текущего окна.
При этом сохраняйте только релевантные элементы: перед добавлением нового элемента отбросьте все более мелкие элементы.


"""


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums


# def max_sliding_window(sequence, m):
#     maximums = []
#     for i in range(len(sequence) - m + 1):
#         maximums.append(max(sequence[: m]))
#         sequence.pop(0)
#     return maximums


def max_sliding_window_deque_idx(sequence, m):
    tmp_deque = deque()

    maximums = []

    for i in range(m):
        new_elem = sequence[i]
        while (len(tmp_deque) > 0) and (sequence[tmp_deque[-1]] < new_elem):
            tmp_deque.pop()
        tmp_deque.append(i)

    for i in range(m, len(sequence)):
        maximums.append(sequence[tmp_deque[0]])

        new_elem = sequence[i]

        while (len(tmp_deque) > 0) and (tmp_deque[0] <= (i - m)):
            tmp_deque.popleft()

        while (len(tmp_deque) > 0) and (sequence[tmp_deque[-1]] < new_elem):
            tmp_deque.pop()

        tmp_deque.append(i)

    maximums.append(sequence[tmp_deque[0]])

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    # input_sequence = StackWithMax()
    # for i in input().split():
    #     input_sequence.Push(int(i))
    # assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window_deque_idx(input_sequence, window_size))

