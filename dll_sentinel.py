class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
class DLL:
    def __init__(self):
        self.nil = Node()
        self.nil.prev = self.nil
        self.nil.next = self.nil
        
    def add_first(self, data):
        new_node = Node(data, self.nil, self.nil.next)
        self.nil.next.prev = new_node
        self.nil.next = new_node
        
    def add_last(self, data):
        new_node = Node(data, self.nil.prev, self.nil)
        self.nil.prev.next = new_node
        self.nil.prev = new_node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def dequeue(self):
        node = self.nil.next
        self.remove(node)
        return node
    
    def enqueue(self, data):
        self.add_last(data)
    
    def search(self, data):
        x = self.nil.next
        while x is not self.nil and data != x.data:
            x = x.next
            
        return x
    
    
    