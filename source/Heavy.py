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
        print(stack.items)
        
    def get_first(self):
        if len(stack.items) < 1:
            return None
        else:
            return stack.items[0]

    def get_all_items(self):
        return self.items
    
    def get_length(self):
        return len(self.items)

stack = Stack()
class Commands:

    def __init__(self):
        self.acc1 = 0
        self.acc2 = 0

    def red(self):
        self.acc1 += 1

    def blue(self):
        stack.push(self.acc1)
    
    def purple(self):
        stack.pop()
    
    def green(self):
        if stack.get_first() == None:
            print('')
            exit()
        
        else:
            if stack.get_first() in range(32):
                print('')
            else:
                print(chr(int(stack.get_first())), end = '')

    def yellow(self):
        inp = input('\n>>> ')

        if inp == '':
            stack.push(0)
        else:
            if ord(inp) > 127:
                print("\n\tUnexpected error; Input's ASCII value was higher than 128")
            else:
                stack.push(ord(inp))

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
        self.acc2 += 10
    
    def sussy(self):
        self.acc2 -= 1
    
    def electrical(self):
        self.acc2 = 0
