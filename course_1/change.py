# Uses python3
"""
Таск: цель этой задачи найти минимальное количество монет нужных
для размена целого значения
Монеты со значениями: 1, 5, 10
"""
import sys


def get_change(m):
    number = 0
    while m != 0:
        if m - 10 >= 0:
            m = m - 10
            number += 1
        elif m - 5 >= 0:
            m = m - 5
            number += 1
        elif m - 1 >= 0:
            m = m - 1
            number += 1
        else:
            break
    return number


if __name__ == '__main__':
    # m = int(input())
    m = int(sys.stdin.read())
    print(get_change(m))
