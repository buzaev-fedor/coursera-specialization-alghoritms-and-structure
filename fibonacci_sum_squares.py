# Uses python3
from sys import stdin


def fibonacci_sum_squares_upgrade(n):
    fib_list = [0, 1]
    sum = 1
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
        sum += fib_list[i] * fib_list[i]
    return sum % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_upgrade(n))
