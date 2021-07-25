# python3


"""
Введение в проблему
Деревья используются для управления иерархическими данными,
такими как иерархия категорий продавца или структура каталогов на вашем компьютере.
Они также используются в анализе данных и машинном обучении как для иерархической кластеризации,
так и для построения сложных прогнозных моделей, в том числе некоторых из наиболее эффективных на практике алгоритмов,
таких как градиентный бустинг по деревьям решений и случайным лесам.
В последующих модулях этого курса мы познакомим вас со сбалансированными двоичными деревьями поиска (BST) -
особым видом деревьев, которые позволяют очень эффективно хранить, манипулировать и извлекать данные.
Таким образом, сбалансированные BST используются в базах данных для эффективного хранения
и фактически в любых нетривиальных программах,
обычно через встроенные структуры данных используемого языка программирования.
В этой задаче ваша цель - привыкнуть к деревьям.
Вам нужно будет прочитать описание дерева из входных данных,
реализовать древовидную структуру данных, сохранить дерево и вычислить его высоту.

Описание проблемы
Задача. Вам дается описание дерева с корнями.
Ваша задача - вычислить и вывести его высоту.
Напомним, что высота (корневого) дерева - это максимальная глубина узла или максимальное расстояние от листа до корня.
Вам дано произвольное дерево, не обязательно двоичное.
Формат ввода. В первой строке записано количество узлов 𝑛.
Во второй строке записано 𝑛 целых чисел от −1 до 𝑛 - 1 - родители узлов.
Если 𝑖-й из них (0 ≤ 𝑖 ≤ 𝑛 - 1) равен -1, узел 𝑖 является корнем,
в противном случае это отсчитываемый от 0 индекс родителя 𝑖-го узла.
Гарантируется, что существует ровно один корень. Гарантируется, что входные данные представляют собой дерево.


Пример 1
5
4 -1 4 1 1

3

Ввод означает, что имеется 5 узлов с номерами от 0 до 4, узел 0 - дочерний узел 4, узел 1 - корень,
узел 2 - дочерний узел 4, узел 3 - дочерний узел 1 и узел 4. является дочерним по отношению к узлу 1.
Чтобы увидеть это, давайте напишем номера узлов от 0 до 4 в одной строке,
а числа, указанные во входных данных, во второй строке ниже:
0 1234
4–1 4 1 1
Теперь мы видим, что узел номер 1 является корнем, потому что -1 соответствует ему во второй строке.
Также мы знаем, что узлы номер 3 и номер 4 являются дочерними по отношению к корневому узлу 1.
Также мы знаем, что узлы номер 0 и номер 2 являются дочерними узлами узла 4.



"""

import sys
import threading
from collections import deque

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_index):
        self.children.append(child_index)

    def __str__(self):
        children_names = [child.name for child in self.children]
        return f"Node #{self.name} children: {children_names}"

    def __repr__(self):
        children_names = [child.name for child in self.children]
        return f"Node #{self.name} children: {children_names}"


class TreeHeight:
    def __init__(self, parent):
        self.parent = parent
        self.n = len(self.parent)

        if -1 not in self.parent:
            raise ValueError("No root node!")

        self.nodes = [Node(i) for i in range(self.n)]

        for child_index in range(self.n):
            parent_index = self.parent[child_index]
            if parent_index == -1:
                self.root = child_index
            else:
                self.nodes[parent_index].add_child(self.nodes[child_index])

    def compute_height(self):
        d = deque()
        d.append(self.nodes[self.root])
        height = 0

        while len(d):
            height += 1
            for i in range(len(d)):
                node = d.popleft()

                for child in node.children:
                    d.append(child)

        return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = TreeHeight(parents)
    print(tree.compute_height())


threading.Thread(target=main).start()
