# Uses python3
import sys
"""
Введение в задачу
Обращение последовательности 𝑎0, 𝑎1, ..., 𝑎𝑛 − 1 - это пара индексов 0 ≤ 𝑖 <𝑗 <𝑛  такая, что 𝑎𝑖 > 𝑎𝑗. 
Количество инверсий последовательности в некотором смысле измеряет, насколько близка последовательность к сортировке. 
Например, отсортированная (в порядке убывания) последовательность вообще не содержит инверсий, 
тогда как в последовательности, отсортированной в порядке убывания, 
любые два элемента составляют инверсию (всего for (𝑛 - 1) / 2 инверсий) . 

Описание проблемы

Задача. Цель этой задачи - подсчитать количество инверсий данной последовательности. 

Формат инпута
В первой строке записано целое число 𝑛, в следующей - последовательность целых чисел.
𝑎0, 𝑎1, ..., 𝑎𝑛 − 1. 

Формат вывода
Выведите количество инверсий в последовательности. 

Пример
Ввод
5
23929
Вывод
2

Что надо делать
Эту проблему можно решить, изменив алгоритм сортировки слиянием. 
Для этого мы изменим обе процедуры Merge и MergeSort следующим образом: 

Merge (𝐵, 𝐶) возвращает результирующий отсортированный массив и количество пар (𝑏, such) таких, что 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶 и 𝑏> 𝑐; 

MergeSort (𝐴) возвращает отсортированный массив 𝐴 и количество инверсий в 𝐴. 

"""



def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
