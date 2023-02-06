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


def count_plus_minus():
    global head, current
    plus, minus, zero = 0, 0, 0
    current = head
    while True:
        if current.data > 0:
            plus += 1
        elif current.data < 0:
            minus += 1
        else:
            zero += 1
        if current.link == head:
            break
        current = current.link
    return plus, minus, zero


def reverse_sign():
    global head, current

    current = head
    while True:
        if current.data:
            current.data *= -1
        if current.link == head:
            break
        current = current.link


head, current, pre = None, None, None
data_array = list()
# 메인 코드 부분
if __name__ == "__main__":
    # odd_even = count_odd_even() # False 리턴
    for _ in range(7):
        data_array.append(random.randint(-100, 100))
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
    plus_minus_zero = count_plus_minus()
    print(
        f"+ : {plus_minus_zero[0]}, - : {plus_minus_zero[1]}, 0 : {plus_minus_zero[2]}"
    )
    reverse_sign()
    print_nodes(head)
