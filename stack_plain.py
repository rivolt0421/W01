MAX_STACK_SIZE = 5
stack = [None] * MAX_STACK_SIZE
ptr = 0

def init_stack():
    global ptr
    ptr = 0

def is_empty():
    return ptr <= 0

def is_full():
    return ptr >= MAX_STACK_SIZE

def push(value):
    global ptr
    print("push ", end='')
    if is_full():
        print("stack is full!!")
    else:
        stack[ptr] = value
        ptr += 1
        print(stack)

def pop():
    global ptr
    print("pop ", end='')
    if is_empty():
        print("stack is empty!!")
    else:
        ptr -= 1
        return stack[ptr]
    
    
    
push('1')
push('2')
push('3')
push('4')
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
push('5')
push('6')
push('7')