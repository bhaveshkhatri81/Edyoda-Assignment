# Print the nodes at odd levels of a tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root):
    def dfs(node, level):
        if node is None:
            return
        if level % 2 != 0:
            print(node.value)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 1)  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Nodes at odd levels:")
print_nodes_at_odd_levels(root)

