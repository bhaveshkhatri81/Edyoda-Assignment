# Count number of trees in a forest

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph.adjacency_list[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def count_trees_in_forest(graph):
    visited = [False] * graph.vertices
    count = 0

    for v in range(graph.vertices):
        if not visited[v]:
            dfs(graph, v, visited)
            count += 1

    return count

if __name__ == "__main__":
    num_vertices = 6
    forest_graph = Graph(num_vertices)
    forest_graph.add_edge(0, 1)
    forest_graph.add_edge(0, 2)
    forest_graph.add_edge(3, 4)

    num_trees = count_trees_in_forest(forest_graph)
    print(f"The number of trees in the forest is: {num_trees}")
