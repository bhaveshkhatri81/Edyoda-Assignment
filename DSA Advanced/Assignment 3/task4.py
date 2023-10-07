# Function to print all the leaves in a given binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_leaves(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.val)

    if root.left is not None:
        print_leaves(root.left)

    if root.right is not None:
        print_leaves(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Leaves of the tree:")
print_leaves(root)
