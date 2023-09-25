# 10. Write a program to find the smallest number using a stack.

class MinStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = []  

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]

# Example 
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)

print("Smallest element:", stack.get_min())  

stack.pop()
print("Smallest element after pop:", stack.get_min())  
