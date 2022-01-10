class Stack: # Defines a stack class
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
