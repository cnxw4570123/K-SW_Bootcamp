import random


class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None for _ in range(size)]
        self.top = -1

    def peek(self):
        try:
            return self.items[self.top]
        except:
            print("Stack is Empty!")

    def pop(self):
        try:
            data = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return data
        except:
            print("Stack is Empty!")

    def push(self, data):
        try:
            self.top += 1
            self.items[self.top] = data
        except:
            print("Stack is Full")


if __name__ == "__main__":
    stk = Stack(10)
    stones = ["red", "blue", "green", "yellow", "purple", "orange"]
    random.shuffle(stones)

    for stone in stones:
        stk.push(stone)

    print("way to Gingerbread house", end=" ")
    while stk.peek() is not None:
        print(stk.pop(), end=" --> ")
    print("Gingerbread house")

    print("way to my home", end=" ")
    for stone in stones:
        stk.push(stone)
        print(stk.peek(), end=" --> ")
    print("my home")
