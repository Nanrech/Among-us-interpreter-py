import random
from Stack import Stack

stack = Stack()

class Colours:
    acc1 = 0
    acc2 = 0
    def __init__(self):
        pass

    def _red(self):
        self.acc1 += 1

    def _blue(self):
        stack.push(self.acc1)
    
    def _purple(self):
        stack.pop()
    
    def _green(self):
        print(chr(stack.get_first()), end = '')
    
    def _yellow(self):
        _input = bytes(input('>>> '), 'ascii')
        if _input == None or _input == '':
            stack.push(0)
        else:
            for byte in _input:
                stack.push(byte)
                break
    
    def _cyan(self):
        if self.acc1 > stack.get_length():
            for r in range(random.randint(0, stack.get_length())):
                stack.pop()
        else:
            for r in range(random.randint(0, self.acc1)):
                stack.pop()

    def _black(self):
        print(stack.get_first())
    
    def _white(self):
        self.acc1 -= 1
    
    def _brown(self):
        self.acc1 = stack.get_first()
    
    def _lime(self):
        first_char = stack.get_first() * 2
        stack.pop()
        stack.push(first_char)
    def _pink(self):
        self.acc1 = 0

    def _orange(self):
        self.acc1 += 10

    def _vented(self):
        self.acc2 += 10
    
    def _sussy(self):
        self.acc2 -= 1
    
    def _electrical(self):
        self.acc2 = 0

    def print_stack(self):
        print(stack.items)
