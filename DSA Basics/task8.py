# 8. Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_closed(code):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in code:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Example
code_snippet = "{[()]}"
if are_brackets_closed(code_snippet):
    print("All brackets are closed.")
else:
    print("Brackets are not properly closed.")
