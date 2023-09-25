# Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 != 0:
            return self.num2 / self.num1
        else:
            return "Division by zero is not allowed"

# Sample input
obj = Calculator(10, 94)
print("Addition of the two number is", obj.add())
print("Subtraction of the two number is", obj.subtract())
print("Multiplication of the two number is", obj.multiply())
print("Division of the two number is", obj.divide())
