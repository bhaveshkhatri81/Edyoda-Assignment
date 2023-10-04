# Reverse a string using a stack data structure

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()

    for char in input_string:
        stack.push(char)

    reversed_string = ""

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

input_string = "Hello"
reversed_string = reverse_string(input_string)
print(reversed_string)  
