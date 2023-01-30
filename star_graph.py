from collections import defaultdict

def is_star_graph(graph):
    degree_count = defaultdict(int)
    for vertex in graph:
        degree_count[vertex] = len(graph[vertex])
    center = max(degree_count, key=degree_count.get)
    for vertex in graph:
        if vertex != center and len(graph[vertex]) != 1:
            return False
    return True

# Example usage
graph = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
if is_star_graph(graph):
    print("The given graph is a star graph.")
else:
    print("The given graph is not a star graph.")
