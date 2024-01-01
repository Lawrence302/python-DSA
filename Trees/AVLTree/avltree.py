# implementation of avl tree
print(" AVL tree implementation ")

# creating the node
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

# defining the AVL Tree
class AVLTree:
    def __init__(self):
        self.root = None

    # getting the node height
    def get_height(self,node):
        if node:
            return node.height
        return 0

    # updating the node height
    def update_height(self,node):
        if node is not None:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # calculating balance factor
    def balance_factor(self,node):
        if node is not None:
            return self.get_height(node.left) - self.get_height(node.right)

    # rotating left
    def rotate_left(self, root):
        new_root = root.right
        temp = new_root.left

        new_root.left = root
        root.right = temp

        self.update_height(root)
        self.update_height(new_root)

        return new_root

    # rotating right
    def rotate_right(self,root):
        new_root = root.left
        temp = new_root.right

        new_root.right = root
        root.left = temp

        self.update_height(root)
        self.update_height(new_root)

        return new_root


    # inserting key value  into the tree
    def insert_key(self,key):
        self.root = self.insert(self.root,key)

    # insert node into tree 
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)
        balance = self.balance_factor(root)

        # left heavy tree
        if balance > 1:
            if key < root.left.data:
                return self.rotate_right(root)
            else:
                # peform left-right rotation
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # right heavy tree
        if balance < -1:
            if key > root.right.data:
                return self.rotate_left(root)
            else:
                # peform right-left rotation
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    elements = []
    # printing the elements in inorderTraversal
    def inorderTraversal(self,root):
        if root is  None:
            return None

        self.inorderTraversal(root.left)
        self.elements.append(root.data)
        self.inorderTraversal(root.right)





tree = AVLTree()
print(tree.root)

tree.insert_key(50)
tree.insert_key(70)
tree.insert_key(60)

print(tree.root.data)

tree.inorderTraversal(tree.root)
print(tree.elements)

tree2 = AVLTree()
tree2.insert_key(10)
tree2.insert_key(9)
tree2.insert_key(8)
tree2.insert_key(7)
tree2.insert_key(6)
tree2.insert_key(5)
tree2.insert_key(4)
tree2.insert_key(3)
tree2.insert_key(2)
tree2.insert_key(1)

tree2.elements = []
tree2.inorderTraversal(tree2.root)
print(tree2.elements)
