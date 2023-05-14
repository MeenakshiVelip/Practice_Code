
class Queue:
    def __init__(self):
        self.queue = []

    def equeue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue)<1:
           return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
q=Queue()
q.equeue(1)
q.equeue(2)
q.equeue(3)
q.equeue(4)
q.display()
q.dequeue()
print("after removing an element")
q.display()