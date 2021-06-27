# Uses python3
import sys
import random

"""
Введение в задачу:
Правило большинства - это правило принятия решений, которое выбирает альтернативу, 
имеющую большинство, то есть более половины голосов.
Дана последовательность элементов 𝑎1, 𝑎2,. . . , 𝑎𝑛, 
вы хотите проверить, содержит ли он элемент, 
который встречается более 𝑛 / 2 раз.

Описание задачи: 
Задача: 
Цель этой проблемы кода - проверить, содержит ли входная последовательность элемент большинства.
 
Формат ввода:
В первой строке записано целое число 𝑛, в следующей - последовательность 𝑛 неотрицательных
целые числа 𝑎0, 𝑎1,. . . , 𝑎𝑛 − 1. 

Формат вывода
Выведите 1, если в последовательности есть элемент, который встречается строго более / 2 раз, и 0 в противном случае. 

Пример 1:
5
2 3 9 2 2
1

4
1 2 3 4
0

MajorityElement(𝑎1, 𝑎2, . . . , 𝑎𝑛): for 𝑖 from 1 to 𝑛:
currentElement ← 𝑎𝑖 count ← 0
for 𝑗 from 1 to 𝑛:
if 𝑎𝑗 = currentElement: count ← count + 1
if count > 𝑛/2: return 𝑎𝑖
return “no majority element”
"""


def old_vmajority_element(a):
    n = len(a)
    for i in range(len(a)):
        current_element = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == current_element:
                count += 1
        if count > n / 2:
            return 1
    return -1


def get_majority_element(a, left, right):
    maj_element = 0
    count = 1
    for i in range(1, right):

        if a[i] == a[maj_element]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_element = i
            count = 1

    count = 0
    for i in range(right):
        if a[i] == a[maj_element]:
            count += 1

    if count > right // 2:
        return a[maj_element]
    return -1


if __name__ == '__main__':
#     while True:
#         input_numbers = []
#         input_n = random.randint(4, 8)
#         for i in range(input_n):
#             input_numbers.append(random.randint(0, 100))
#
#         input_numbers = sorted(input_numbers)
#         out_1 = get_majority_element(input_numbers, 0, len(input_numbers))
#
#         out_2 = old_vmajority_element(input_numbers)
#
#         # if res_1 == res_2:
#         #     print("Ok")
#         #     print(f"out_1 = {out_1} ")
#         #     print(f"out_2 = {out_2} ")
#         if out_1 != out_2:
#             print("WARNING")
#             print(f"out_1 = {out_1} ")
#             print(f"out_2 = {out_2} ")
#             print(input_numbers)

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [6, 55, 67, 67, 67]
    # n = len(a)
    a = sorted(a)
    # n = 5
    # n = 4
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
