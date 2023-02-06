import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = self


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
    while current.link != start:
        current = current.link
        print(current.data, end=" ")
    print()


def insert_node(find_data, insert_data):
    global head, current, pre
    node = Node(insert_data)

    if head.data == find_data:  # 첫 번째 노드 삽입
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node.link = current
            pre.link = node
            return
    current.link = node
    node.link = head


def delete_node(del_data):
    global head, current, pre

    if head.data == del_data:
        print("첫 노드가 삭제됨")
        current = head
        head = head.link
        del current
        return

    current = head
    while current.link != head:
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
    global head, current, pre
    current = head
    if current.data == find_data:
        return current

    current = head
    while current.link != head:
        if current.data == find_data:
            return current
        current = current.link
    return Node()


def is_find(find_data):
    """
    찾으면 True를 못찾으면 False를 반환하는 함수
    :param find_data : 찾고자 하는 원소. str
    :return: True or False
    """
    global head, current, pre
    current = head
    if current.data == find_data:
        return True

    current = head
    while current.link != head:
        if current.data == find_data:
            return True
        current = current.link
    return False


def count_odd_even():
    global head, current
    # SRP 위배
    # if head is None:
    #     return False
    even, odd = 0, 0
    current = head
    while True:
        if current.data % 2 == 0:
            even += 1
        else:
            odd += 1
        if current.link == head:
            break
        current = current.link
    return even, odd


def make_minus_no(even, odd):
    global current, head
    if even > odd:
        remainder = 0
    else:
        remainder = 1

    current = head
    while current.link != head:
        if current.data % 2 == remainder:
            current.data *= -1
        current = current.link


# 전역 변수 선언 부분
head, current, pre = None, None, None
data_array = list()
# 메인 코드 부분
if __name__ == "__main__":
    # odd_even = count_odd_even() # False 리턴
    for _ in range(7):
        data_array.append(random.randint(1, 100))
    # print(data_array)

    node = Node(data_array[0])
    head = node
    node.link = node

    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print_nodes(head)
    odd_even = count_odd_even()
    print(f"Even Number : {odd_even[0]} Odd Number : {odd_even[1]}")
    make_minus_no(*odd_even)
    print_nodes(head)
