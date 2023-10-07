# Find sum of all left leaves in a given Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    def dfs(node, is_left):
        if not node:
            return 0

        if not node.left and not node.right and is_left:
            return node.val

        return dfs(node.left, True) + dfs(node.right, False)

    return dfs(root, False)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = sum_of_left_leaves(root)
print(result)  
