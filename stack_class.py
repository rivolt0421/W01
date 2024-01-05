class Stack:
    class Full(Exception):
        pass
    class Empty(Exception):
        pass
    
    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.ptr = 0
        self.capacity = capacity
        
    def is_empty(self):
        return self.ptr <= 0
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, value):
        if self.is_full():
            raise Stack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
        print("push ", end='')
        print(self.stk)
        
    def pop(self):
        if self.is_empty():
            raise Stack.Empty
        self.ptr -= 1
        print("pop ", end='')
        print(self.stk[self.ptr])
        return self.stk[self.ptr]
    
    def clear(self):
        self.ptr = 0
    
s = Stack(5)

s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
s.pop()
s.pop()
s.pop()
s.pop()
# s.pop()
s.push('6')
s.push('7')
s.push('8')
s.push('9')
s.push('10')