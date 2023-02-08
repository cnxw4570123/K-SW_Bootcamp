class Graph:
    def __init__(self, size):
        self.SIZE = size
        # n * n 행렬 구현
        self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]


vertex = input("Input vertex with whitespace('a' 'b')").split()
vertex.sort()
direct = input("1) Directed graph 2) Undirected graph :")

edges = input("input edges with comma(a b, e f): ").split(", ")  # set으로 받아서 중복 제거
if direct == "1":
    pass
elif direct == "2":
    pass
else:
    pass
