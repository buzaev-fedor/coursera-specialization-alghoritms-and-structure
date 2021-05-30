import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_index_1 = -1
    for i in range(n):
        if max_index_1 == -1 or numbers[i] > numbers[max_index_1]:
            max_index_1 = i

    max_index_2 = -1
    for j in range(n):
        if j != max_index_1 and (max_index_2 == -1 or numbers[j] > numbers[max_index_2]):
            max_index_2 = j

    return numbers[max_index_1] * numbers[max_index_2]


if __name__ == '__main__':
    # while True:
    #     input_numbers = []
    #     input_n = random.randint(2, 20)
    #     for i in range(input_n):
    #         input_numbers.append(random.randint(100000, 1000000))
    #
    #     res_1 = max_pairwise_product(input_numbers)
    #     res_2 = max_pairwise_product_fast(input_numbers)
    #
    #     if res_1 == res_2:
    #         # print(f"{input_n}")
    #         # print(f"{input_numbers} ")
    #         print("Ok")
    #     else:
    #         print(f"{input_n}")
    #         print(f"{input_numbers} ")
    #         print(f"ALERT: {res_1} {res_2}")
    #         break

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
