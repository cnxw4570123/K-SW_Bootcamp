import random


class Queue:
    time = 0

    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.size = size
        self.items = [None for _ in range(size)]

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full")
            return
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = data
        Queue.time += data[1]

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        self.front = (self.front + 1) % self.size
        data = self.items[self.front]
        self.items[self.front] = None
        Queue.time -= data[1]

    def __str__(self):
        return f"Queue status : {self.items}"

    @staticmethod
    def print_time():
        print(f"Time to be waited : {Queue.time}")


if __name__ == "__main__":
    queue = Queue(5)
    time_table = [("Inquery", 9), ("repair", 3), ("refund", 4), ("other", 1)]

    Queue.print_time()
    print(queue)

    for guest in random.choices(time_table, k=queue.size - 1):
        queue.enqueue(guest)
        Queue.print_time()
        print(queue)
    print("------------------------------------------------------------------")
    for _ in range(queue.size - 1):
        queue.dequeue()
        Queue.print_time()
        print(queue)
