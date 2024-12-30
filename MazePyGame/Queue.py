

class MyQueue: 
    def __init__(self) -> list:
        self.queue = []
    
    def enqueue(self, item) -> None:
        self.queue.append(item)
    
    def dequeue(self) -> any:
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def print_queue(self) -> list:

        for item in self.queue:
            print(item, end=", ")\
        
        print("\n")
        

    
