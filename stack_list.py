class Node:
        
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        new_node = Node(data, None, self.head)
        self.head = new_node
        
    def pop(self):
        if self.is_empty() :
            print("stack is empty!!")
        else :
            x = self.head
            self.head = x.next
            return x