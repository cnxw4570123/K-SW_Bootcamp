# 클래스와 함수 선언 부분
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    """
    현재 노드부터 마지막 노드 까지 출력해주는 메소드
    :param start: 첫 노드
    :return: None
    """
    current = start
    if current is None:
        return
    print(current.data, end=" ")
    while current.link is not None:
        current = current.link
        print(current.data, end=" ")
    print()


# 전역 변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]

# 메인 코드 부분
if __name__ == "__main__":

    node = Node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)
    print(node.data)
