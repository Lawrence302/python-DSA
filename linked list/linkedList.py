# # implementation of a link list and its operations


# class Node:
#     next_node = None
#     def __init__(self,data):
#         self.data = data


#     def __repr__(self):
#         return "<Node data: %s next_node %s >" % (self.data , self.next_node)

# # creating the linke list
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def is_empty(self):
#         return self.head == None

#     def prepend(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.tail = new_node
#         new_node.next_node = self.head
#         self.head = new_node

#     #insert at specific position
#     def insert(self,data,position):
#         new_node = Node(data)
#         start = self.head
#         current = start
#         count = 0

#         while current:
#             if position == 0 :
#                 new_node.next_node = current
#                 self.head = new_node
#                 return
#             if count < position-1:
#                 count += 1
#                 current = current.next_node
#             else:
#                 new_node.next_node = current.next_node
#                 current.next_node = new_node
#                 return
#         print("sorry the index position was to large")

#     # addint a node at the tail
#     def append(self,data):
#             new_node = Node(data)
#             self.tail.next_node = new_node
#             self.tail = new_node

#     def remove(self,data):
#         start = self.head
#         current = start
#         previous = None
#         while current:
#             if current.data == data:
                
#                 if current == self.head:
#                     print(current, " removed ")
                    
#                     self.head = current.next_node
#                     current.next_node = None
#                     return
#                 elif current.next_node == None:
#                     current = None
#                     previous.next_node = None
#                     self.tail = previous
#                     return
#                 else:
#                     current.data = None
#                     previous.next_node = current.next_node
#                     current.next_node = None
#                     return
#             else:
#                 previous = current
#                 current = current.next_node
            
#         print("did not find the item to remove")
        
        



#     def size(self):
#         count = 0
#         start = self.head
#         current = start

#         while current:
#             count += 1
#             current = current.next_node

#         return count

#     def search(self,value):
#         start = self.head
#         current = start

#         while current:
#             if current.data == value:
#                 print(f"data found : {value}")
#                 return
#             else:
#                 current = current.next_node
                

#         print(f" sorry the value {value} is not found in the list")

#     def display(self):
#         items = []
#         start = self.head
#         current = start

#         while current:
#             # print(current.data)
#             items.append(current.data)
#             current = current.next_node
#         print(items)
        


# l = LinkedList()
# print(l.is_empty() )  

# l.prepend(40)

# l.prepend(20)

# print(l.is_empty() ) 

# print( "size of the list is : ", l.size())

# # l.display()
# l.search(4)
# l.insert(5,1)
# # l.insert(7,3)
# l.display()
# print(l.tail)
# l.append(88)
# l.append(89)
# # l.display()
# l.remove(88)
# # l.remove(5)
# l.remove(20)
# print(l.tail)
# l.display()

print("hello world")

# creating the node
class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return f"{self.data} --> {self.next_node}"

#creating the linke list and its operations

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    #adding a node at the head

    def prepend(self,data):
        node = Node(data)
        
        if self.head == None:
            node.next_node = self.head
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head = node
            


    #adding at the end
    def append(self,data):
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node

    # insert at a specific position
    def insert(self,data,index):
        count = 0
        start = self.head
        current = start
        prev = current

        if index == 0 :
            self.prepend(data)
            return

        while current:
            if count > index:
                print("index ouf of bounds")
                return
            # print(count)
            if count == index :
                new_node = Node(data)
                new_node.next_node = current
                prev.next_node = new_node
                return
            count += 1
            prev = current
            current = current.next_node
            
    # removing elements at start
    def remove_start(self):
        old_head = self.head
        self.head = self.head.next_node
        old_head = None
        return

    # removing from end
    def remove_end(self):
        start = self.head
        current = start
        prev = current
        
        while current.next_node :
            prev = current
            current = current.next_node
            if current == self.tail:
                print("tail arived ", current.data)
        current = None
        prev.next_node = None
        self.tail = prev
    
    # remove at index
    def remove_at_index(self,index):
        if index == 0 :
            print( 'removing at start')
            self.remove_start()
            return
        
        start = self.head
        current = start
        prev = current
        count = 0

        while current:
            if count > index:
                print("index out of bounds")
                return
            if count == index:
                print('removing ',current.data, " at index ", index)
                old_node = current
                prev.next_node = current.next_node
                current = None
                return
            count += 1
            prev = current
            current = current.next_node


    #checking if the list is empty
    def is_empty(self):
        if self.head == None:
            return True
    #printint list items
    def display(self):
        start = self.head
        current = start

        while current:
            print(current.data)
            current = current.next_node
    #printList at once
    def display_pic(self):
        print(self.head)

    


l1 = Linked_list()
l1.prepend(15)
l1.prepend(12)
l1.prepend(14)

if l1.is_empty:
    print("the list is empty")

print(l1.display())
print(l1.display_pic())
print(l1.tail)

l1.append(5)
l1.append(6)
print(l1.display_pic())
print(l1.tail)

l1.insert(11,0)
print(l1.display_pic())
l1.insert(44,2)
print(l1.display_pic())
l1.insert(46,4)
print(l1.display_pic())
l1.insert(46,7)
print(l1.display_pic())
# l1.remove_start()
# print(l1.display_pic())
# l1.remove_start()
# print(l1.display_pic())
l1.remove_start()
print(l1.display_pic())
l1.remove_end()
print(l1.display_pic())
l1.remove_end()
print(l1.display_pic())
l1.remove_at_index(0)
print(l1.display_pic())
l1.remove_at_index(2)
print(l1.display_pic())
print(l1.tail)
