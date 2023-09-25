# 9. Write a program to reverse a stack.

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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def reverse_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        aux_stack.push(stack.pop())

    return aux_stack

# Example 
if __name__ == "__main__":
    original_stack = Stack()
    original_stack.push(1)
    original_stack.push(2)
    original_stack.push(3)
    original_stack.push(4)

    reversed_stack = reverse_stack(original_stack)

    print("Reversed Stack is")
    while not reversed_stack.is_empty():
        print(reversed_stack.pop())
