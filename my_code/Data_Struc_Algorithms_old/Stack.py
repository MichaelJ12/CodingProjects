from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, items):
        # Add an item to the top of the stack
        self.items.append(items) 

    def pop(self):
        # Remove and return an item from the top stack
        return self.items.pop()

    def peek(self):
        # return item from the top of the stack 
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from a empty stack")

    def is_empty(self):
       # check if the stack is empty
       return len(self.items) == 0 

    def size(self):
        # return the amount of items in the stack
        return len(self.items)
    



if __name__ == '__main__':
    stack = Stack()

    stack.push('michaerl')
    stack.push('test')
    stack.push('julius')

    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())    

    print(stack.size())
    print(stack.is_empty())
