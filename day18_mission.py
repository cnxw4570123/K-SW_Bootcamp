from collections import deque


class Graph:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.SIZE = len(vertex)
        self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        for edge in edges:
            self.graph[vertex.index(edge[0])][vertex.index(edge[1])] = 1
            self.graph[vertex.index(edge[1])][vertex.index(edge[0])] = 1

    def snack_BFS(self):
        # preparation
        queue = deque([])
        conv_list = []
        # first vertex insertion
        current = 0
        queue.append(current)
        conv_list.append(current)

        next = None
        for vtx in range(self.SIZE):
            # if self.graph[current][vtx] == 1:
            if self.graph[current][vtx]:
                if vtx in conv_list:
                    pass
                else:
                    next = vtx
                    break

        if current:  # if current is None
            current = next
            queue.append(current)
            conv_list.append(current)
        else:
            current = queue.popleft()
        return conv_list

    def print_graph(self):
        print("\t", end="")
        for vtx in self.vertex:
            print(f"{vtx:4s}")

        for i in range(self.SIZE):
            print(f"{self.vertex[i]:4s}", end="")
            for j in range(self.SIZE):
                print(f"{self.graph[i][j]:4d}", end="")
        print("End")


def make_graph():
    global vertex, edges
    vertex = input("Input vertexs with space: ").split()
    vertex.sort()

    # directed Graph without weight
    edges = []
    while True:
        edge = input("Input edges with space (vertex vertex weight) (To quit > exit): ")
        if edge == "exit" or edge == "EXIT":
            break
        edges.append(edge.split())
    g1 = Graph(vertex, edges)
    return g1


edges = []
g1 = make_graph()
print(g1.snack_BFS())
print("==")
g1.print_graph()
