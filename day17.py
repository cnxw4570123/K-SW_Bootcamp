class CircularQueue:
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
            print("Queue is Full!")
            return
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        self.front = (self.front + 1) % self.size
        data = self.items[self.front]
        self.items[self.front] = None
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        return self.items[(self.front + 1) % self.size]

    def __str__(self):
        return f"{self.items}"


if __name__ == "__main__":
    Q_size = int(input("Input Queue Size: "))
    queue = CircularQueue(Q_size)

    while True:
        select = input("Insertion(I)/Extraction(E)/Verify(V)/Exit(X) Choose one ==> ")
        if select == "X" or select == "x":
            break
        if select == "I" or select == "i":
            data = input("Input Data ==> ")
            queue.enqueue(data)
            print("Queue Status : ", queue)
            print("front : ", queue.front, ", rear : ", queue.rear)
        elif select == "E" or select == "e":
            data = queue.dequeue()
            print("Extracted Data ==> ", data)
            print("Queue Status : ", queue)
            print("front : ", queue.front, ", rear : ", queue.rear)
        elif select == "V" or select == "v":
            data = queue.peek()
            print("Verified Data ==> ", data)
            print("Queue Status : ", queue)
            print("front : ", queue.front, ", rear : ", queue.rear)
        else:
            print("Wrong Input")

    print("End!")
