from collections import deque 

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        return self.items.popleft()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        raise IndexError("Peek from a empty stack")
    
    def isEmpty(self):
        return len(self.items) == 0 
    
    def size(self):
        return len(self.items)
    

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue('10')
    queue.enqueue('20')
    queue.enqueue('30')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.peek())
   
  
    print(queue.size())