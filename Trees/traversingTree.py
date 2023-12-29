# binary tree traversal inoder, preorder and postorder

# tree node 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# binary search tree implementation

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root

        while True:
            if value < current_node.data:
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

    # print in inorder traversal
    inorder_elements = []
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            self.inorder_elements.append(node.data)
            self.inorder(node.right)

    # preorder traversal
    preorder_elements = []
    def preorder(self,node):
        
        if node is not None:
            self.preorder_elements.append(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    # postorder traversal
    postorder_elements = []
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            self.postorder_elements.append(node.data)

        



tree = BinaryTree()

tree.insert(100)
tree.insert(200)
tree.insert(150)
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(300)

tree.inorder(tree.root)
print( f"inorder Traversal : {tree.inorder_elements }")
tree.preorder(tree.root)
print(f"Preorder Traversal : {tree.preorder_elements }")
tree.postorder(tree.root)
print(f"Postorder Traversal : {tree.postorder_elements}")