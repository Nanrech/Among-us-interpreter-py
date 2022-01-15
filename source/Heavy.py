import random
class Stack: 
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item:int):
        self.items.insert(0, item)
        
    def pop(self):
        if len(self.items) == 0:
            return 
        else:
            self.items.pop(0)

    def print_stack(self):
        print(self.items)
        
    def get_first(self):
        if len(self.items) == 0:
            return 0
        else:
            return self.items[0]

    def get_all_items(self):
        return self.items
    
    def get_length(self):
        return len(self.items)

stack = Stack()
class Commands:
    acc1 = 0
    acc2 = -1
    def __init__(self):
        pass

    def red(self):
        self.acc1 += 1

    def blue(self):
        stack.push(self.acc1)
    
    def purple(self):
        stack.pop()
    
    def green(self):
        print(chr(stack.get_first()), end = '')

    def yellow(self):
        _input = input('\n>>> ')
        if _input == None or _input == '':
            stack.push(0)
        else:
            stack.push(ord(_input))
    
    def cyan(self):
        if self.acc1 > stack.get_length():
            for r in range(random.randint(0, stack.get_length())):
                stack.pop()
        else:
            for r in range(random.randint(0, self.acc1)):
                stack.pop()

    def black(self):
        print(stack.get_first())
    
    def white(self):
        self.acc1 -= 1
    
    def brown(self):
        self.acc1 = stack.get_first()
    
    def lime(self):
        first_char = stack.get_first() * 2
        stack.pop()
        stack.push(first_char)
    def pink(self):
        self.acc1 = 0

    def orange(self):
        self.acc1 += 10

    def vented(self):
        if self.acc2 < 0:
            self.acc2 = 0
        self.acc2 += 10
    
    def sussy(self):
        if self.acc2 < 0:
            self.acc2 = 0
        self.acc2 -= 1
    
    def electrical(self):
        self.acc2 = 0

    def print_stack(self):
        return stack.items
