# Uses python3
import sys

"""
Введение

Вам предоставляется примитивный калькулятор,
который может выполнять следующие три операции с текущим числом 𝑥: 
умножить 𝑥 на 2, умножить 𝑥 на 3 или прибавить 1 к 𝑥. 
Вашей цели дано положительное целое число 𝑛, 
найдите минимальное количество операций, необходимых для получения числа 𝑛, начиная с числа 1. 

Описание проблемы

Таска

Учитывая целое число, вычислите минимальное количество операций, необходимых для получения числа 𝑛, начиная с числа 1. 

Формат инпута
Входные данные состоят из единственного целого числа 1 ≤ 𝑛 ≤ 10^6.

Формат отпута
В первой строке выведите минимальное количество операций operations, необходимое для получения из 1. 
Во второй строке выведите последовательность промежуточных чисел. 
То есть во второй строке должны быть положительные целые числа 𝑎0, 𝑎2, ..., 𝑎𝑘 − 1 такие, 
что 𝑎0 = 1, 𝑎𝑘 − 1 = 𝑛 и для всех 0≤𝑖 <𝑘 − 1 + 1 равно либо 𝑎𝑖 + 1 , 2𝑎𝑖 или 3𝑎𝑖. 
Если таких последовательностей много, выведите любую из них.  

Пример 1
5

3
1245
   1 2 3 4 5
1 |1|2|3|4|5|
2 |2|4|6| | |
3 | | | | | |


Пример 2
1

0
1

Пример 3
96234

14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
"""


def new_sequence(n):
    count = [0] * (n + 1)
    count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        min_hops = min([count[x] for x in indices])

        count[i] = min_hops + 1
    point = n
    optimal_seq = [point]
    while point != 1:
        candidates = [point - 1]
        if point % 2 == 0:
            candidates.append(point // 2)
        if point % 3 == 0:
            candidates.append(point // 3)

        point = min(
            [(c, count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(point)

    return reversed(optimal_seq)


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(new_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
