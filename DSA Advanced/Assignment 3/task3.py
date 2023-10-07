# Perform Pre-order, Post-order, In-order traversal

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=" ")

# Example usage:
# Let's create a simple binary tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Pre-order traversal:")
pre_order_traversal(root)

print("\nIn-order traversal:")
in_order_traversal(root)

print("\nPost-order traversal:")
post_order_traversal(root)
