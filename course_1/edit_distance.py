# Uses python3
"""
Введение
Расстояние редактирования между двумя строками - это минимальное количество операций
(вставки, удаления и замены символов) для преобразования одной строки в другую.
Это мера сходства двух струн.
У расстояния редактирования есть приложения, например, в вычислительной биологии,
обработке естественного языка и проверке орфографии.
Ваша цель в этой задаче - вычислить расстояние редактирования между двумя строками.

Описание проблемы

Задача.
Цель этой задачи - реализовать алгоритм вычисления расстояния редактирования между двумя строками.

Формат ввода.
Каждая из двух строк ввода содержит строку, состоящую из строчных латинских букв.

Ограничения.
Длина обеих строк от 1 до 100.

Выходной формат.
Выведите расстояние редактирования между заданными двумя строками.

Пример 1
ab
ab
0

Пример 2

short
ports
3

|s|h|o|r|t|-|
|-|p|o|r|t|s|

Пример 3

editing
distance
5

|e|d|i|-|t|i|n|g|-|
|-|d|i|s|t|a|n|c|e|

"""


def edit_distance(s, t):
    d = [[x] + [0] * (len(t)) for x in range(len(s) + 1)]
    d[0] = [x for x in range(len(t)+1)]

    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)
    return d[-1][-1]


if __name__ == "__main__":
    # s = input()
    # t = input()
    # print(edit_distance(s, t))
    print(edit_distance(input(), input()))
