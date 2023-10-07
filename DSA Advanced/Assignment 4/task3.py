# Count the number of nodes at given level in a tree using BFS

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def count_nodes_at_level(root, level):
    if not root:
        return 0
    
    queue = [(root, 0)]
    count = 0
    
    while queue:
        node, current_level = queue.pop(0)
        
        if current_level == level:
            count += 1
        
        if current_level > level:
            break
        
        for child in node.children:
            queue.append((child, current_level + 1))
    
    return count


root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
root.children[1].children = [Node(6)]

level_to_count = 2
result = count_nodes_at_level(root, level_to_count)
print(f"The number of nodes at level {level_to_count} is: {result}")
