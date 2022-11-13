import random


class Stack:
    """
    A smol stack implementation
    """
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.insert(0, i)

    def pop(self):
        self.items.pop(0)

    @property
    def first(self):
        return self.items[0]

    @property
    def size(self):
        return len(self.items)


class TheSkeld:
    """
    this is the thing I'm using to track the accumulators and stack because why not
    """
    def __init__(self):
        self.acc1: int = 0
        self.acc2: int = 0
        self.stack: Stack = Stack()
        self.call_stack: Stack = Stack()

    def red(self):
        self.acc1 += 1

    def blue(self):
        self.stack.push(self.acc1)

    def purple(self):
        self.stack.pop()

    def green(self):
        if self.stack.first:
            print(chr(self.stack.first), end='')
        else:
            print('\0')

    def yellow(self):
        i = input("\n>>> ")
        for char in i:
            self.stack.push(ord(char))

    def cyan(self):
        random_range = self.stack.first if self.stack.first < self.stack.size else self.stack.size
        r = random.randint(0, random_range)

        for i in range(0, r):
            self.stack.pop()

    def black(self):
        print(self.stack.first)

    def white(self):
        self.acc1 -= 1

    def brown(self):
        self.acc1 = self.stack.first

    def lime(self):
        i = self.stack.first * 2
        self.stack.pop()
        self.stack.push(i)

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

    def interpret(self, token: str):
        """
        yep I'm putting it here
        """
        if token == "red":
            self.red()
        elif token == "blue":
            self.blue()
        elif token == "purple":
            self.purple()
        elif token == "green":
            self.green()
        elif token == "yellow":
            self.yellow()
        elif token == "cyan":
            self.cyan()
        elif token == "black":
            self.black()
        elif token == "white":
            self.white()
        elif token == "brown":
            self.brown()
        elif token == "lime":
            self.lime()
        elif token == "pink":
            self.pink()
        elif token == "orange":
            self.orange()
        elif token == "vented":
            self.vented()
        elif token == "sussy":
            self.sussy()
        elif token == "electrical":
            self.electrical()
