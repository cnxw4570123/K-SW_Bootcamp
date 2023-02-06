Stack = [None for _ in range(5)]
top = -1

top += 1
Stack[top] = "커피"
top += 1
Stack[top] = "녹차"
top += 1
Stack[top] = "꿀물"
top += 1
Stack[top] = "바닐라라떼"
top += 1
Stack[top] = "아이스티"
# top += 1  # stack overFlow
# Stack[top] = "카라멜마끼아또"

for i in range(len(Stack) - 1, -1, -1):
    print(Stack[i])

data = Stack[top]
Stack[top] = None
top -= 1
print(f"pop -> {data}")

data = Stack[top]
Stack[top] = None
top -= 1
print(f"pop -> {data}")

data = Stack[top]
Stack[top] = None
top -= 1
print(f"pop -> {data}")

for i in range(len(Stack) - 1, -1, -1):
    print(Stack[i])
