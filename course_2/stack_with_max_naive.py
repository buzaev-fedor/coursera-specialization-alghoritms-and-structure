#python3
import sys

"""
Введение в задачу
Стек - это абстрактный тип данных, поддерживающий операции Push () и Pop (). 
Нетрудно реализовать это таким образом, чтобы обе эти операции работали в постоянное время. 
В этой задаче ваша цель - реализовать стек, который также поддерживает поиск максимального значения 
и гарантирует, что все операции по-прежнему работают в постоянное время. 

Задача. 

Реализуйте стек, поддерживающий операции Push (), Pop () и Max ().

Формат ввода. 

Первая строка входных данных содержит количество запросов 𝑞. 
Каждая из следующих 𝑞 строк задает запрос одного из следующих форматов: push v, pop или max. 

"""


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.tmp = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.tmp:
            self.tmp.append(a)
        elif a >= self.tmp[-1]:
            self.tmp.append(a)

    def Pop(self):
        if self.__stack[-1] == self.tmp[-1]:
            self.tmp.pop()

        assert (len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.tmp))
        # return self.tmp[-1]
        return self.tmp[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
