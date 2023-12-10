#implementation of double linked list
#creating the node

class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return f" <--|{self.data}|--> {self.next}->"

# creating double linked list 
class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    # adding node at the head
    def prepend(self,data):
        if self.is_empty():
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head
            return

        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # add at end
    def append(self,data):
        if self.is_empty():
            self.prepend(data)
            return
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # add at a specific point
    def insert(self,data,index):
        if index <= 0:
            self.prepend(data)
            return
        start = self.head
        current = start
        count = 0

        while current:
            if count > index:
                print("index out of bounds")
                return
            if index == count :
                # print('insert location found ', current.data)
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node  
                return

            count += 1
            current = current.next

        print("index out of bounds out")

    # remove at beginning
    def remove_head(self):
        if self.is_empty():
            print(" list is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        current = self.head
        self.head = current.next
        self.head.prev = None
        current.next = None
        current = None
        
        

    #remove at index
    def remove_At(self,index):
        if self.is_empty():
            print(" sorry list is empty")
            return
        if index <= 0 :
            self.remove_head()
            return
        
        count = 0
        current = self.head
        while current:
            if count > index :
                print(" index out of bounds")
                return
            if count == index:
                if current == self.tail:
                    self.pop()
                    return
                
                temp = current
                current.prev.next = current.next
                current.next.prev = current.prev
                current.next = None
                current.prev = None
                current = None
                return

            count += 1
            current = current.next
        

    #remove at end
    def pop(self):
        if self.is_empty() :
            print("cannot pop from an empty list")
            return
        if self.head == self.tail :
            self.head = None
            self.tail = None
            return
        # print(self.tail, " tail before delete")
        temp = self.tail.prev
        self.tail.prev = None
        self.tail = temp
        self.tail.next = None
        temp = None

    #checking if the list is empty
    def is_empty(self):
        return True if  self.head == None else False
           

    # printing the list 
    def print_list(self):
        print(self.head)



l1 = Double_linked_list()
l1.print_list()
print("inserting into list")
l1.prepend(5)
l1.prepend(6)
l1.append(7)
l1.insert(4,1)
l1.insert(8,2)
l1.append(9)
l1.print_list()
print("deleting from list")
l1.pop()
l1.remove_head()
l1.remove_At(1)
l1.print_list()









