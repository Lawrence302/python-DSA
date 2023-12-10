# implementing a stack in python

class Stack:
    def __init__(self):
        self.stack_limit = self.limit()
        self.stack = []

    def limit(self):
        number = input(" Enter the limit of the stack : ")
        return int(number)
    def size(self):
        return len(self.stack)

    # checking if the stack is empty
    def is_empty(self):
        return not self.stack

    # adding data to the stack
    def push(self,data):
        self.stack.append(data) if self.stack_limit > len(self.stack) else print(" stack is full ")

    def pop(self):
        if self.is_empty() :
            print(" stack is empty ")
            return

        return self.stack.pop(-1)

st1 = Stack()
print(st1.is_empty() )
st1.push(5)
st1.push(6)
print(st1.size())
st1.push(7)
st1.push(8)

print(st1.stack)
st1.pop()
print(st1.stack)
st1.pop()
st1.pop()
st1.pop()
print(st1.stack)