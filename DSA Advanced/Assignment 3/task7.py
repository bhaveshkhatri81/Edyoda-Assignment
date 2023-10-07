# Find sum of all nodes of the given perfect binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_nodes(root):
    if root is None:
        return 0

    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Calculating the sum of nodes
total_sum = sum_of_nodes(root)

print(f"The sum of all nodes in the tree is: {total_sum}")
