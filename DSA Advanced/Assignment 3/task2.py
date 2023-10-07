# Find height of a given tree

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_height(node):
    if node is None:
        return -1
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return 1 + max(left_height, right_height)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

height = find_height(root)

print("The height of the tree is:", height)
