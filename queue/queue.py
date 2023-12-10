#implementation of a queue in python

class Queue:
    
    def __init__(self):
        self.queue_limit = self.limit()
        self.queue = []
        
    # seting lmit of the queue
    def limit(self):
        number = input(" Enter the size limit of the queue: ")
        return int(number)

# checking if the queue is empty
    def is_empty(self):
        return not self.queue

    # checking the size of the queue
    def size(self):
        return  len(self.queue)

# adding data to the queue
    def enqueue(self,data): 
        self.queue.append(data) if self.queue_limit > self.size() else print(" queue is full")

# removing data from the queue
    def dequeue(self):
       return self.queue.pop(0) if self.queue else print(" queue is empty ")


q1 = Queue()
q1.queue
print(q1.queue)
print(q1.is_empty())
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.enqueue(9)
print(q1.queue)
print(q1.is_empty())
print(q1.size())
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(q1.queue)
