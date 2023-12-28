#implementation of binary search tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root

        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

    # finding the min node
    def min(self):
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.data

    # finding the max node
    def max(self):
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.data

    # searching for a value on the tree
    def search(self,value):
        current_node = self.root
        while current_node is not None:
            if current_node.data == value:
                return f" found {current_node.data}"

            if value < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return " node not found "




tree = BinaryTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(7)
tree.insert(8)
tree.insert(6)


print(tree.root.data)
print(f"the minimum number from the tree is {tree.min()}")
print(f"the maximum number from the tree is {tree.max()}")

print(tree.search(4))
print(tree.search(8))
print(tree.search(2))
print(tree.search(9))