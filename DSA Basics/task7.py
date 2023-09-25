# 7. Write a program to convert prefix expression to infix expression.

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(prefix_expr):
    stack = []
    operators = set(['+', '-', '*', '/'])
    prefix_expr = prefix_expr[::-1]

    for char in prefix_expr:
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = f"({operand1}{char}{operand2})"
            stack.append(expression)

    return stack[0]

# Example
prefix_expression = "*+AB-CD"
infix_expression = prefix_to_infix(prefix_expression)
print("Infix Expression:", infix_expression)
