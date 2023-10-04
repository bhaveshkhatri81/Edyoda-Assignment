# Evaluate a postfix expression using stack

def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token not in operators:
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack[0]


expression = "3 4 + 2 * 7 /"
result = evaluate_postfix(expression)
print("Result:", result)
