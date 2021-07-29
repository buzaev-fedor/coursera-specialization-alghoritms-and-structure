# Uses python3
import sys
import random


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_upgrade(from_, to):
    if to <= 1:
        return to
    fib_list = [0, 1]
    sum = 0
    for i in range(2, to + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
        if i >= from_:
            sum += fib_list[i]
    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_upgrade(from_, to))
