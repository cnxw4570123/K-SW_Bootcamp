import random


class Node:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None

    def __str__(self):
        return f"{self.data}"


class BTree:
    def __init__(self):
        self.root = None

    def append_child(self, x):
        node = Node(x)
        if not self.root:
            self.root = node
            return

        current = self.root
        while True:
            if current.data > node.data:
                if not current.left:
                    current.left = node
                    break
                current = current.left

            elif current.data < node.data:
                if not current.right:
                    current.right = node
                    break
                current = current.right
            else:
                return

    @staticmethod
    def preorder(node):
        if not node:
            return None
        print(node.data, end=" ")
        BTree.preorder(node.left)
        BTree.preorder(node.right)


if __name__ == "__main__":
    data_arr = [
        "cheetos",
        "banana milk",
        "powerade",
        "shinramyeon",
        "hershey's",
        "sprite",
        "pepsi",
    ]
    btree = BTree()

    for data in random.choices(data_arr, k=20):
        btree.append_child(data)

    print("sold products with no duplicate -> ", end="")
    BTree.preorder(btree.root)
