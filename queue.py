class  Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
       if not self.is_empty():
           self.queue.pop(0)
       else:
           return "stack is empty"
       
    def is_empty(self):
        return len(self.queue)==0
    
        
my_queue = Queue()

my_queue.enqueue('ali')
my_queue.enqueue('hosein')
my_queue.enqueue('hasan')
my_queue.enqueue('mohsen')

my_queue.dequeue()

print(my_queue.queue)
