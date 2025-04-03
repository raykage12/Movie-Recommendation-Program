import random
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None
    
    def random_movie(self):
        return self.stack[random.randint(0, len(self.stack)-1)] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def get_all(self):
       return self.stack[::-1]