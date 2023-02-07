class Queue:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.items = [None for _ in range(size)]

    def is_full(self):
        if self.rear != self.size - 1:
            return False
        elif self.rear == self.size - 1 and self.front == -1:
            return True
        return False

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full")
            return
        self.rear += 1
        self.items[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        self.front += 1
        data = self.items[self.front]
        for i in range(self.front + 1, self.size):
            self.items[i - 1] = self.items[i]
            self.items[i] = None
        self.front -= 1
        self.rear -= 1
        # self.items[self.front] = None
        return f"{data} enters into cafeteria"

    def __str__(self):
        return f"Queue status : {self.items}"


if __name__ == "__main__":
    guests = ["guest1", "guest2", "guest3", "guest4", "guest5"]
    queue = Queue(5)
    for guest in guests:
        queue.enqueue(guest)
    for _ in range(queue.size):
        print(queue)
        print(queue.dequeue())
