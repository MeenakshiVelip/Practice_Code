#Create a Node
class Node:
    def __init__(self, data, next=None):
        self.data= data
        self.next= next

# Join nodes to get a linked list   
class LinkedList:
    def __init__(self):
        self.head = None
l = LinkedList()        
l.head = Node(4)
print(l.head.data)        