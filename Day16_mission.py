import math
import random


class Node:
    name_num = 65

    def __init__(self, x=None, y=None):
        self.name = chr(self.name_num)
        self.x = x
        self.y = y
        Node.name_num += 1
        self.next = self

    def __str__(self):
        return f"{self.name} 편의점, 거리: {self.dist()}"

    def dist(self):
        return math.sqrt(self.x**2 + self.y**2)


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_nodes(self):
        current = self.head

        if self.size == 0:
            return

        while current.next != self.head:
            print(current)
            current = current.next
        print(current)

    def push_inorder(self, data):
        node = Node(*data)
        if self.size == 0:  # 첫 노드 삽입
            self.head = node
            self.size += 1
            return

        if self.head.dist() > node.dist():  # 맨 앞에 삽입
            node.next = self.head
            v = self.head
            while v.next != self.head:
                v = v.next
            v.next = node
            self.head = node
            self.size += 1
            return

        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
            if current.dist() > node.dist():
                prev.next = node
                node.next = current
                self.size += 1
                return
        else:
            current.next = node
            node.next = self.head
            self.size += 1


C = CircularLinkedList()
for i in range(10):
    C.push_inorder((random.randint(1, 100), random.randint(1, 100)))
C.print_nodes()
