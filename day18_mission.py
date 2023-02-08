class Graph:
    def __init__(self, size, edges):
        global vertex
        self.SIZE = size
        self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        for edge in edges:
            self.graph[vertex.index(edge[0])][vertex.index(edge[1])] = edge[2]
            self.graph[vertex.index(edge[1])][vertex.index(edge[0])] = edge[2]


def make_graph():
    vertex = input("Input vertexs with space: ").split()
    vertex.sort()

    # directed Graph without weight
    edges = []
    while True:
        edge = input("Input edges with space (vertex vertex weight) (To quit > exit): ")
        if edge == "exit" or edge == "EXIT":
            break
        edges.append(edge.split())
    # print(vertex)
    # print(edges)
    g1 = Graph(len(vertex), edges)
    # print(g1.graph)

    return g1


g1 = make_graph()
