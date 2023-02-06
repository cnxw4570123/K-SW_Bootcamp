class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_nodes(self):
        last = self.head
        print("forward -->", end=" ")
        while last.next is not None:
            print(last, end=" ")
            last = last.next
        print(last)

        print("backward -->", end=" ")
        while last.prev is not None:
            print(last, end=" ")
            last = last.prev
        print(last)

    def push_back(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.size += 1
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = node
        node.prev = last
        self.size += 1


twice = ["다현", "정연", "쯔위", "사나", "지효"]
d = DoublyLinkedList()
for member in twice:
    d.push_back(member)

d.print_nodes()
