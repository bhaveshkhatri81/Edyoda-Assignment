# Count subtress that sum up to a given value x in a binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_subtrees_with_sum(root, x):
    def count_subtrees(node, x):
        nonlocal count

        if node is None:
            return 0

        left_sum = count_subtrees(node.left, x)
        right_sum = count_subtrees(node.right, x)

        current_sum = left_sum + right_sum + node.val

        if current_sum == x:
            count += 1

        return current_sum

    count = 0
    count_subtrees(root, x)
    return count


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right.left = TreeNode(2)
root.right.right = TreeNode(6)

result = count_subtrees_with_sum(root, 10)
print(f'Number of subtrees with sum 10: {result}')
