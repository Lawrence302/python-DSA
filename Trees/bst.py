# implementation of a binary search tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# tree

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
print(tree.root.right.data)
print(tree.root.right.left.data)
print(tree.root.right.right.data)
print(" ")
print(" ")
print(tree.root.left.data)
print(tree.root.left.left.data)
print(tree.root.left.left.left.data)