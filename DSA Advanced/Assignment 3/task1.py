# Implement Binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, node, new_node):
        if node.value < new_node.value:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_recursive(node.right, new_node)
        else:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_recursive(node.left, new_node)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

tree = BinaryTree()
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in values:
    tree.insert(value)

print(tree.search(6))  
print(tree.search(11)) 
