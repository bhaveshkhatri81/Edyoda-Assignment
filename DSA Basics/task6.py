# 6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def is_operator(char):
    return char in ['+', '-', '*', '/']

def postfix_to_prefix(postfix):
    stack = []
    for char in postfix:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
    return stack[0]

# Example
postfix_expression = "ab+c*"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)
