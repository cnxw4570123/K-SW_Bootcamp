# 클래스와 함수 선언 부분
class Node:
    def __init__(self, data=None):
        self.data = data
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


def insert_node(find_data, insert_data):
    global head, current, pre
    node = Node(insert_data)

    if head.data == find_data:  # 첫 번째 노드 삽입
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node.link = current
            pre.link = node
            return
    current.link = node


def delete_node(del_data):
    global head, current, pre

    if head.data == del_data:
        print("첫 노드가 삭제됨")
        current = head
        head = head.link
        del current
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == del_data:
            print("중간 노드가 삭제됨")
            pre.link = current.link
            del current
            return
    # 삭제할 데이터가 없음
    print("삭제할 노드가 없음")
    return


def find_node(find_data):
    global memory, head, current, pre
    # current = head
    # if current.data == find_data:
    #     return current

    current = head
    while current.link is not None:
        if current.data == find_data:
            if head == current:
                print("첫 노드")
            return current
        current = current.link
    return Node()


# 전역 변수 선언 부분
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]
# 메인 코드 부분
if __name__ == "__main__":

    node = Node(data_array[0])  # 첫 번째 노드
    head = node

    for data in data_array[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node(data)
        pre.link = node

    print_nodes(head)
    insert_node("피카츄", "잠만보")
    print_nodes(head)
    insert_node("꼬부기", "어니부기")
    print_nodes(head)
    insert_node("성윤모", "거북왕")
    print_nodes(head)
    delete_node("잠만보")
    print_nodes(head)
    delete_node("어니부기")
    print_nodes(head)
    delete_node("강찬석")
    print_nodes(head)
    print(find_node("파이리").data)
    print(find_node("박민석").data)
