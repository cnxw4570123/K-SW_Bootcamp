class Node:
    def __init__(self, data=None):
        self.left = None
        self.data = data
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def append_child(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if current.data > node.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.data < node.data:
                    if current.right is None:
                        current.right = node
                        break
                    current = current.right

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=" -> ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" -> ")
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" -> ")


if __name__ == "__main__":
    group = ["화사", "솔라", "문별", "휘인", "쯔위", "선미", "다현", "사나"]
    b_tree = BinaryTree()
    for member in group:
        b_tree.append_child(member)
    print("전위 순회:", end=" ")
    b_tree.preorder(b_tree.root)
    print("끝")
    print("중위 순회:", end=" ")
    b_tree.inorder(b_tree.root)
    print("끝")
    print("후위 순회:", end=" ")
    b_tree.postorder(b_tree.root)
    print("끝")
