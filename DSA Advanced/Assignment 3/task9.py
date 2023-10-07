# Find maximum level sum in Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root):
    if not root:
        return 0

    queue = [root]
    level = 1
    max_level = 1
    max_sum = root.val

    while queue:
        level_sum = 0
        new_queue = []

        for node in queue:
            level_sum += node.val
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

        queue = new_queue
        level += 1

    return max_level

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

max_level = maxLevelSum(root)
print("Maximum level sum is at level:", max_level)
