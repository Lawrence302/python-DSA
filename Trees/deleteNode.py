# deleting node from a binary search tree

# defining the node 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# defining the binary tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

    # traversing the binary Tree in inorder Traversal
    elements = []
    def inorderTraversal(self,root):
        if root is not None:
            self.inorderTraversal(root.left)
            self.elements.append(root.data)
            self.inorderTraversal(root.right)
                
    # deleting node from a binary tree
    def deleteNode(self,root,key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        elif key > root.data:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # search for the smallest value on the right sub tree
            current = root.right
            while current.left:
                current = current.left
            root.data = current.data

            # replacing the sucessor node
            root.right = self.deleteNode(root.right, root.data)

        return root





tree = BinaryTree()
tree.insert(100)
tree.insert(200)
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(150)
tree.insert(300)
tree.inorderTraversal(tree.root)
print(tree.elements)

tree.deleteNode(tree.root,20)
tree.elements = []
tree.inorderTraversal(tree.root)
print(tree.elements)