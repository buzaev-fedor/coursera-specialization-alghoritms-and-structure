# Uses python3
import sys


# def get_fibonacci_last_digit_upgrade(n):
#     if n <= 1:
#         return n
#     fib_list = [0, 1]
#     for i in range(2, n + 1):
#         # fib_list.append(fib_list[i - 2] + fib_list[i - 1])
#         fib_list = [fib_list[1], fib_list[0] + fib_list[1]]
#     return fib_list[1] % 10


def get_fibonacci_last_digit_upgrade(n):
    if n <= 1:
        return n
    fib_list = (0, 1)
    for i in range(2, n + 1):
        # fib_list.append(fib_list[i - 2] + fib_list[i - 1])
        fib_list = (fib_list[1] % 10, fib_list[0] % 10 + fib_list[1] % 10)
    return fib_list[1] % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_upgrade(n))
