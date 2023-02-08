from collections import deque


class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


g = None
queue = deque([])
visited_ary = []

g = Graph(9)
A, B, C, D, E, F, G, H, I = 0, 1, 2, 3, 4, 5, 6, 7, 8
g.graph[A][B] = 1
g.graph[A][C] = 1
g.graph[A][E] = 1
g.graph[B][A] = 1
g.graph[B][C] = 1
g.graph[B][D] = 1
g.graph[C][A] = 1
g.graph[C][B] = 1
g.graph[C][D] = 1
g.graph[C][E] = 1
g.graph[D][B] = 1
g.graph[D][C] = 1
g.graph[E][A] = 1
g.graph[E][C] = 1
g.graph[E][H] = 1
g.graph[E][G] = 1
g.graph[F][C] = 1
g.graph[G][E] = 1
g.graph[G][I] = 1
g.graph[H][E] = 1
g.graph[H][I] = 1
g.graph[I][G] = 1
g.graph[I][H] = 1

for row in range(g.SIZE):
    for col in range(g.SIZE):
        print(g.graph[row][col], end=" ")
    print()

current = 0  # 시작 정점 A
queue.append(current)
visited_ary.append(current)

while len(queue) != 0:
    next = None
    for vertex in range(g.SIZE):
        if g.graph[current][vertex] == 1:
            if vertex in visited_ary:
                pass
            else:
                next = vertex
                break

    if next:
        current = next
        queue.append(current)
        visited_ary.append(current)
    else:
        current = queue.popleft()


for i in visited_ary:
    print(i, end=" --> ")
print("END")
