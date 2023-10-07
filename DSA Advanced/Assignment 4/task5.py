# Detect Cycle in a Directed Graph

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, stack):
        visited[v] = True
        stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True

        stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.vertices
        stack = [False] * self.vertices

        for node in range(self.vertices):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, stack):
                    return True
        return False

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

if g.is_cyclic():
    print("Graph contains a cycle")
else:
    print("Graph doesn't contain a cycle")
