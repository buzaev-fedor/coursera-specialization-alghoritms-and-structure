import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_upgrade(n, m):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    return fib_list[n] % m


def get_pisano_array(n: int, m: int) -> list:
    pisano = [0]
    if m == 1:
        return pisano
    pisano.append(1)
    if n <= 1:
        return pisano
    pisano.append((pisano[len(pisano) - 1] + pisano[len(pisano) - 2]) % m)
    while not (pisano[- 1] == 1 and pisano[- 2] == 0):
        pisano.append((pisano[len(pisano) - 1] + pisano[len(pisano) - 2]) % m)
    return pisano[:-2]


def fib_mod(n, m):
    pisano = get_pisano_array(n, m)
    return pisano[n % len(pisano)]


if __name__ == '__main__':
    input = sys.stdin.read();
    # n = int(input())
    # m = int(input())
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(fib_mod(n, m))
