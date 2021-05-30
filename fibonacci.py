# Uses python3
import sys


def upgrade_fib(n):
    if n <= 1:
        return n
    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(upgrade_fib(n))
