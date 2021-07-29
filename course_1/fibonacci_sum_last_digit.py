# Uses python3
import sys


# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#     sum = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10


# def fibonacci_sum_upgrade(n):
#     if n <= 1:
#         return n
#     fib_list = [0, 1]
#     for i in range(2, n + 1):
#         fib_list.append(fib_list[i - 2] % 10 + fib_list[i - 1] % 10)
#     return sum(fib_list) % 10


def fibonacci_sum_upgrade_1(n):
    sum = 1
    if n <= 1:
        return n
    fib_list = (0, 1)
    for i in range(2, n + 1):
        fib_list = (fib_list[1] % 10, fib_list[0] % 10 + fib_list[1])
        sum += fib_list[1] % 10
    return sum % 10


# def fibonacci_sum_upgrade_2(n):
#     sum = 1
#     if n <= 1:
#         return n
#     fib_list = (0, 1)
#     for i in range(2, n + 1):
#         fib_list = (fib_list[1] % 10, fib_list[0] + fib_list[1] % 10)
#         sum += fib_list[1]
#     return sum % 10

def fib_digit(n):
    sum = 1
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, (a + b) % 10
        sum = (sum + b) % 10
    return sum


def fib_sum_digit(n):
    if n <= 1:
        return n
    n = (n + 2) % 60
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, (a + b) % 10
    if b != 0:
        return b - 1
    else:
        return 9


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = int(input())
    # print(fibonacci_sum_upgrade_1(n))
    print(fib_sum_digit(n))
