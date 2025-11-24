class EvenIterator:
    def __init__(self, numbers) -> None:
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        
        
        if self.index >= len(self.numbers):
            raise StopIteration
        
        while self.index < len(self.numbers):
            current = self.numbers[self.index]
            self.index += 1 
            if current % 2 == 0:
                return current
    
        raise StopIteration

if __name__ == "__main__":
    a = [10,20,30]
    even = EvenIterator(a)
    
    for n in even:
        print(n)